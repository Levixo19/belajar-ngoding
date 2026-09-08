"""Mengubah konten kurikulum jadi struktur yang bisa dikirim sebagai JSON.

`materials.py` sudah melakukan hal yang mirip, tapi keluarannya berupa baris
teks ber-ANSI yang lebarnya dihitung dari ukuran terminal. Web butuh yang
sebaliknya: struktur bertingkat tanpa keputusan tampilan apa pun, supaya
lebar, jenis huruf, dan pemenggalan baris diputuskan oleh CSS.

Tiga hal yang dikerjakan di sini:

1. **Badan materi dipecah jadi blok bertipe.** Di sumbernya, `body` cuma daftar
   baris polos. Baris yang menjorok dua spasi adalah tabel atau contoh yang
   spasinya bermakna; baris berawalan "- " adalah daftar. Kalau semuanya
   dilempar ke HTML sebagai satu blok teks, tabel ASCII-nya rusak dan daftarnya
   kehilangan bentuk. Pengelompokan dilakukan di sini, sekali, bukan ditebak
   ulang oleh JavaScript.

2. **Kode dipecah jadi token, bukan diwarnai.** `sorot.token()` mengembalikan
   (jenis, teks) tanpa satu pun kode ANSI, jadi jenisnya bisa dipetakan langsung
   ke kelas CSS. Aturan leksikalnya tetap satu-satunya yang ada di `sorot.py`.

3. **Setiap blok kode membawa petunjuk berkasnya** dari `berkas.py` -- apakah ia
   program utuh yang perlu disimpan, potongan penjelas, sesi database, atau
   ilustrasi. Itu jawaban atas pertanyaan "ini perlu aku ketik atau tidak?" yang
   di web justru lebih mendesak, karena tidak ada terminal di sebelahnya.

Semua fungsi di sini MURNI membaca. Tidak ada yang menulis progres.

Importir: webapp/api.py.
"""

import re

import bab
import berkas
import runner
import sorot
from progress import kunci, kuis_jatuh_tempo

# Bahasa yang aturan penyorotannya ada di sorot.py. "aplikasi" memakai aturan
# Java (didaftarkan di akhir sorot.py) karena contoh kodenya memang Java.
_BAHASA_SOROT = set(sorot.ATURAN)


def bahasa_sorot(lang):
    """Kunci aturan penyorot untuk sebuah entri LANGUAGES."""
    return lang["key"] if lang["key"] in _BAHASA_SOROT else lang["runner"]


def token_kode(kode, bahasa):
    """[(jenis, teks)] -> [[jenis, teks]] siap JSON.

    Gabungan seluruh `teks` dijamin sama persis dengan `kode` aslinya --
    sifat itu diuji di tests/test_sorot.py untuk SELURUH kode di kurikulum.
    """
    return [[jenis, teks] for jenis, teks in sorot.token(kode, bahasa)]


# ------------------------------------------------------------- badan materi

_POLA_BUTIR = re.compile(r"^\s*[-*•]\s+")
_POLA_NOMOR = re.compile(r"^\s*\d+[.)]\s+")


def _jenis_baris(baris):
    if not baris.strip():
        return "kosong"
    if baris[:1] in (" ", "\t"):
        return "pra"
    if _POLA_BUTIR.match(baris):
        return "butir"
    if _POLA_NOMOR.match(baris):
        return "nomor"
    return "teks"


def blok_badan(baris_list):
    """Kelompokkan daftar baris jadi blok bertipe.

    Jenis blok yang dihasilkan:
      {"jenis": "teks",   "teks": "..."}      paragraf, baris aslinya dipertahankan
      {"jenis": "pra",    "teks": "..."}      spasi bermakna (tabel, contoh menjorok)
      {"jenis": "daftar", "butir": [...], "urut": bool}

    Baris menjorok digabung apa adanya termasuk indentasi relatifnya, karena di
    situlah letak informasinya: tabel tipe data di materi Java hanya terbaca
    kalau kolomnya tetap sejajar.
    """
    blok = []
    kini = []
    jenis_kini = None

    def tutup():
        nonlocal kini, jenis_kini
        if not kini:
            return
        if jenis_kini == "pra":
            # Buang indentasi BERSAMA supaya tidak ada lautan spasi di kiri,
            # tapi pertahankan indentasi relatif antar baris.
            umum = min((len(b) - len(b.lstrip()) for b in kini if b.strip()),
                       default=0)
            blok.append({"jenis": "pra",
                         "teks": "\n".join(b[umum:] if b.strip() else ""
                                           for b in kini)})
        elif jenis_kini in ("butir", "nomor"):
            pola = _POLA_NOMOR if jenis_kini == "nomor" else _POLA_BUTIR
            blok.append({"jenis": "daftar",
                         "urut": jenis_kini == "nomor",
                         "butir": [pola.sub("", b).strip() for b in kini]})
        else:
            blok.append({"jenis": "teks", "teks": "\n".join(kini)})
        kini = []
        jenis_kini = None

    for baris in baris_list:
        jenis = _jenis_baris(baris)
        if jenis == "kosong":
            tutup()
            continue
        if jenis_kini is not None and jenis != jenis_kini:
            tutup()
        jenis_kini = jenis
        kini.append(baris.rstrip())

    tutup()
    return blok


def _petunjuk(bahasa, kode, konteks):
    p = berkas.petunjuk_kode(bahasa, kode, konteks)
    return {
        "jenis": p.jenis,
        "nama": p.nama,
        "perintah": list(p.perintah),
        "instruksi": p.instruksi,
        "keterangan": p.keterangan,
        "berkas": list(p.berkas),
        "perlu_berkas": p.perlu_berkas,
        # Blok yang berdiri sendiri boleh dicoba langsung dari halaman materi;
        # potongan dan ilustrasi tidak, karena pasti gagal dan itu menyesatkan.
        "bisa_dijalankan": p.jenis in (berkas.PROGRAM, berkas.SESI),
    }


def bagian_materi(materi, lang):
    """Ubah `sections` satu materi jadi blok siap render."""
    bhs_sorot = bahasa_sorot(lang)
    bhs_berkas = lang["runner"]
    keluar = []

    for bagian in materi["sections"]:
        # Sebuah bagian boleh punya body DAN code sekaligus, dan kalau begitu
        # keduanya harus keluar. Versi sebelumnya menulis if/else: begitu ada
        # "code", prosanya dibuang tanpa jejak — sementara antarmuka terminal
        # (materials.baris_materi) tetap menampilkan keduanya. Dua antarmuka
        # yang menampilkan isi berbeda untuk materi yang SAMA adalah kegagalan
        # yang tidak menimbulkan error di mana pun: yang membaca di browser
        # cuma melihat blok kode tanpa penjelasannya, dan tidak punya cara tahu
        # ada yang hilang. Kebetulan tidak ada satu pun materi lama yang
        # mencampur keduanya, jadi bug ini menunggu materi baru untuk meledak.
        badan = bagian.get("body") or []
        kode = bagian.get("code")

        if badan:
            keluar.append({
                "jenis": "prosa",
                "judul": bagian.get("heading", ""),
                "blok": blok_badan(badan),
            })
        if kode is not None:
            keluar.append({
                "jenis": "kode",
                # Judulnya menempel pada blok PERTAMA saja. Mengulangnya di
                # blok kode membuat satu heading tercetak dua kali berturut
                # turut di layar.
                "judul": "" if badan else bagian.get("heading", ""),
                "kode": kode,
                "token": token_kode(kode, bhs_sorot),
                "petunjuk": _petunjuk(bhs_berkas, kode,
                                      bagian.get("heading") or materi["title"]),
            })
        if not badan and kode is None:
            # Bagian yang cuma berisi heading. Jarang, tapi test_data
            # mengizinkannya, dan menjatuhkannya berarti judul yang hilang.
            keluar.append({
                "jenis": "prosa",
                "judul": bagian.get("heading", ""),
                "blok": [],
            })
    return keluar


# --------------------------------------------------------------- ringkasan

def status_materi(data, kat, judul):
    k = kunci(kat, judul)
    if k in data["materi_dibaca"]:
        return "selesai"
    if k in data["materi_sebagian"]:
        return "sebagian"
    return "baru"


def status_latihan(data, kat, judul):
    k = kunci(kat, judul)
    if k in data["latihan_lulus"]:
        return "lulus"
    if k in data["latihan_manual"]:
        return "manual"
    if k in data["latihan_dilihat"]:
        return "dibuka"
    return "baru"


def daftar_materi(lang, data, daftar_bab=None):
    """Daftar materi satu bahasa, lengkap dengan bab dan status kuncinya.

    `daftar_bab` sengaja diminta dari luar: `bab.status()` membaca progres
    setiap kali dipanggil, jadi pemanggil yang sudah memegang hasilnya
    (lihat `api.bahasa`) menyerahkannya ke sini alih-alih membuat permintaan
    yang sama menghitungnya dua kali. Kalau tidak diberikan, ia dihitung dari
    `data` yang sudah ada di tangan -- tetap tanpa membuka berkas progres lagi.

    Materi yang babnya terkunci TETAP ikut terdaftar, lengkap dengan judulnya.
    Menyembunyikannya menghapus satu-satunya hal yang membuat pintu bertahap
    ada gunanya: tahu apa yang sedang ditunggu di baliknya.
    """
    kat = f"{lang['key']}_materi"
    if daftar_bab is None:
        daftar_bab = bab.status(lang, data)

    # `bab.status()` dijamin menutupi seluruh materi -- pembagian yang tidak
    # lagi cocok dengan jumlah materi jatuh ke satu bab berisi semuanya -- jadi
    # peta ini pasti punya entri untuk tiap indeks.
    peta = {i: b for b in daftar_bab for i in b["materi"]}

    keluar = []
    for i, m in enumerate(lang["materials"]):
        b = peta[i]
        keluar.append({
            "indeks": i,
            "judul": m["title"],
            "status": status_materi(data, kat, m["title"]),
            "bagian": len(m["sections"]),
            "bookmark": kunci(kat, m["title"]) in data["bookmark"],
            "bab": b["nomor"],
            "terkunci": b["status"] == bab.TERKUNCI,
            "tingkat": b["tingkat"],
        })
    return keluar


def daftar_kuis(lang, data):
    kat = f"{lang['key']}_kuis"
    keluar = []
    for i, q in enumerate(lang["quizzes"]):
        k = kunci(kat, q["title"])
        skor = data["kuis_skor"].get(k, {})
        keluar.append({
            "indeks": i,
            "judul": q["title"],
            "soal": len(q["questions"]),
            "terbaik": skor.get("terbaik", 0),
            "percobaan": skor.get("percobaan", 0),
            "total_soal": skor.get("total_soal", 0) or len(q["questions"]),
            "terakhir_waktu": skor.get("terakhir_waktu", ""),
            "pernah": bool(skor),
            "jatuh_tempo": kuis_jatuh_tempo(data, kat, q["title"]),
            "jadwal": (data["jadwal_kuis"].get(k) or {}).get("jatuh_tempo", ""),
            "salah_tersisa": len(data["salah_kuis"].get(k, [])),
            "bookmark": k in data["bookmark"],
        })
    return keluar


def daftar_latihan(lang, data):
    kat = f"{lang['key']}_latihan"
    siap = runner.tersedia(lang["runner"])
    keluar = []
    for i, e in enumerate(lang["exercises"]):
        keluar.append({
            "indeks": i,
            "judul": e["title"],
            "tingkat": e.get("difficulty", "Menengah"),
            "status": status_latihan(data, kat, e["title"]),
            "dinilai": siap and e.get("auto_check") is not False,
            "alasan": e.get("alasan_tidak_dicek", ""),
            "hint": len(e.get("hints") or []),
            "bookmark": kunci(kat, e["title"]) in data["bookmark"],
        })
    return keluar


# ------------------------------------------------------------------ pencarian

def _cuplik(baris_list, kata, panjang=150):
    """Potongan teks di sekitar kata yang dicari."""
    rendah = kata.lower()
    for baris in baris_list:
        pos = baris.lower().find(rendah)
        if pos < 0:
            continue
        mulai = max(0, pos - panjang // 3)
        teks = baris[mulai:mulai + panjang].strip()
        return (("…" if mulai else "") + teks
                + ("…" if len(baris) > mulai + panjang else ""))
    return ""


def _teks_materi(m):
    keluar = [m["title"]]
    for bagian in m["sections"]:
        if bagian.get("heading"):
            keluar.append(bagian["heading"])
        keluar.extend(bagian.get("body") or [])
        if "code" in bagian:
            keluar.extend(bagian["code"].splitlines())
    return keluar


def cari(languages, kata, tipe="semua", batas=80, data=None):
    """Pencarian teks lintas bahasa.

    Judul dinilai lebih tinggi daripada isi supaya hasil yang paling mungkin
    dimaksud muncul di atas, dan setiap hasil membawa cuplikan berisi kata yang
    dicari -- tanpa itu daftar hasil cuma deretan judul yang harus dibuka satu
    per satu untuk tahu mana yang relevan.

    Hasil bertipe "materi" membawa bidang `terkunci`. Tanpa itu hasil pencarian
    tampak seperti tautan biasa dan baru ditolak SESUDAH diklik -- persis pola
    "tombol yang berujung penolakan" yang dihindari di tempat lain, dan
    padanannya di terminal (`navigasi`) sudah menandainya sejak awal.

    Statusnya dihitung MALAS dan sekali per bahasa: progres dibaca satu kali di
    sini lalu dibagikan, dan sebuah bahasa baru dihitung babnya kalau ia benar
    benar punya hasil materi. Pencarian dipanggil tiap ketikan, jadi menghitung
    bab untuk sebelas bahasa yang sebagian besarnya tidak punya satu hasil pun
    adalah biaya yang tidak dibayar siapa-siapa.
    """
    kata = (kata or "").strip()
    if len(kata) < 2:
        return []
    rendah = kata.lower()
    hasil = []
    terbuka = {}

    def _terbuka(lang):
        if lang["key"] not in terbuka:
            terbuka[lang["key"]] = bab.indeks_terbuka(lang, data)
        return terbuka[lang["key"]]

    for lang in languages:
        if tipe in ("semua", "materi"):
            for i, m in enumerate(lang["materials"]):
                baris = _teks_materi(m)
                if not any(rendah in b.lower() for b in baris):
                    continue
                hasil.append({
                    "tipe": "materi", "bahasa": lang["key"],
                    "label_bahasa": lang["label"], "indeks": i,
                    "judul": m["title"], "cuplikan": _cuplik(baris[1:], kata),
                    "terkunci": i not in _terbuka(lang),
                    "skor": 0 if rendah in m["title"].lower() else 1,
                })

        if tipe in ("semua", "kuis"):
            for i, q in enumerate(lang["quizzes"]):
                baris = [q["title"]]
                for s in q["questions"]:
                    baris.append(s["q"])
                    baris.extend(s["options"])
                    baris.append(s.get("explanation", ""))
                if not any(rendah in b.lower() for b in baris):
                    continue
                hasil.append({
                    "tipe": "kuis", "bahasa": lang["key"],
                    "label_bahasa": lang["label"], "indeks": i,
                    "judul": q["title"], "cuplikan": _cuplik(baris[1:], kata),
                    "skor": 0 if rendah in q["title"].lower() else 1,
                })

        if tipe in ("semua", "latihan"):
            for i, e in enumerate(lang["exercises"]):
                baris = ([e["title"]] + list(e.get("question") or [])
                         + list(e.get("hints") or [])
                         + e.get("solution", "").splitlines())
                if not any(rendah in b.lower() for b in baris):
                    continue
                hasil.append({
                    "tipe": "latihan", "bahasa": lang["key"],
                    "label_bahasa": lang["label"], "indeks": i,
                    "judul": e["title"], "cuplikan": _cuplik(baris[1:], kata),
                    "skor": 0 if rendah in e["title"].lower() else 1,
                })

    hasil.sort(key=lambda h: (h["skor"], h["label_bahasa"], h["judul"]))
    return hasil[:batas]


# ------------------------------------------------------------------- ekspor

def aturan_penyorot():
    """Tabel leksikal semua bahasa, untuk penyorot sisi-klien di editor.

    Editor kode harus menyorot ulang setiap kali pelajar mengetik; menempuh
    jaringan untuk itu -- meski cuma ke localhost -- membuat kursor terasa
    berat. Jadi algoritma pemindainya diporting ke JavaScript, TAPI daftar kata
    kuncinya tetap dikirim dari sini. Dengan begitu `sorot.py` tetap
    satu-satunya tempat kata kunci dituliskan; menambah bahasa baru di sana
    otomatis menyalakannya di editor juga.
    """
    keluar = {}
    for nama in sorot.bahasa_didukung():
        a = sorot.ATURAN[nama]
        keluar[nama] = {
            "komentar_baris": list(a.komentar_baris),
            "komentar_blok": [list(p) for p in a.komentar_blok],
            "kutip": list(a.kutip),
            "kutip_mentah": sorted(a.kutip_mentah),
            "escape": a.escape,
            "kunci": sorted(a.kunci),
            "tipe": sorted(a.tipe),
            "bawaan": sorted(a.bawaan),
            "praprosesor": a.praprosesor,
            "variabel_dolar": a.variabel_dolar,
            "tanpa_bedakan_kapital": a.tanpa_bedakan_kapital,
        }
    # "aplikasi" bukan bahasa tersendiri; contohnya Java.
    keluar["aplikasi"] = keluar["java"]
    return keluar
