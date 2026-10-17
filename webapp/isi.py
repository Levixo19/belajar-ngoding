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

from pelajar import bab
from pelajar import kuis_materi
from inti import berkas
from inti import runner
from inti import sorot
from pelajar.progress import kunci, kuis_jatuh_tempo

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

# Penanda diikuti TEPAT SATU spasi, lalu isi. Angkanya bukan selera: dari 449
# blok berpenanda di seluruh kurikulum, 446 memakai satu spasi -- dan ketiga
# sisanya justru BUKAN daftar melainkan tabel yang kolom pertamanya kebetulan
# sebuah bintang ("  *  perkalian        a * b" di Java Operator, "  *  di GLOB"
# di Bash Pola). Menerima `\s+` berarti mengubah tabel operator jadi daftar
# berbulatan dan membuang perataan kolom yang justru isi informasinya.
_POLA_BUTIR = re.compile(r"^(\s*)[-*•] (?=\S)")
_POLA_NOMOR = re.compile(r"^(\s*)(\d+)[.)] (?=\S)")

# Butir YAML ("- uses: actions/checkout@v4", "- run: ...") di dalam contoh
# berkas konfigurasi. Tanda hubungnya bagian dari sintaks YAML, bukan penanda
# daftar prosa, dan bentuk "kata: " sesudahnya nggak pernah muncul di butir
# daftar berbahasa Indonesia di kurikulum ini.
_POLA_BUTIR_YAML = re.compile(r"^- [\w-]+:(\s|$)")
# Kunci YAML polos di baris sebelumnya ("steps:"). Huruf kecil dan tanpa spasi:
# label prosa seperti "Dua jenis exception:" atau "Interface:" nggak cocok,
# jadi daftar "- Checked: ..." di bawah label begitu tetap daftar.
_POLA_KUNCI_YAML = re.compile(r"^[a-z][\w-]*:$")

# Baris yang kolomnya disejajarkan dengan spasi ganda. Di dalam sebuah daftar,
# baris begini adalah contoh kode atau tabel milik butirnya -- bukan sambungan
# kalimatnya -- dan menyambungnya jadi satu paragraf menghapus perataan yang
# jadi satu-satunya alasan baris itu ditulis begitu.
_POLA_KOLOM = re.compile(r"\S {2,}\S")

# Ciri kode yang tidak pernah muncul di prosa Indonesia. Dipakai untuk
# memutuskan apakah sebuah blok menjorok itu contoh kode atau cuma paragraf
# yang kebetulan ditulis menjorok.
_POLA_KODEISH = re.compile(r"[{}<>;=|@$\\]|->|::|\(\)|\[\]|/\*|//|#include|--")
_POLA_KATA = re.compile(r"\b[A-Za-z\u00c0-\u00ff]{2,}\b")


# Kata yang terpenggal di ujung baris. Di kurikulum ini semuanya kata ulang
# ("diam-diam", "benar-benar", "satu-satunya", "seluk-beluk") -- 18 buah, dan
# tanda hubungnya BAGIAN DARI KATANYA. Yang salah cuma spasi yang muncul kalau
# barisnya disambung apa adanya: "diam- diam".
_POLA_PENGGAL = re.compile(r"[^\W\d_]-$")


# Blok prosa yang cara MEMBACANYA berbeda, bukan cuma isinya.
#
# Kurikulum ini sudah menulisnya sejak awal — 384 blok dibuka dengan kata yang
# mengumumkan perannya ("JEBAKAN: gambar pertama halaman justru TIDAK BOLEH
# lazy", "Aturan yang menyelamatkanmu dari banyak kebingungan:"). Yang hilang
# cuma satu: di layar semuanya menjadi paragraf abu-abu yang sama, sehingga
# peringatan yang ditulis penulisnya dengan huruf kapital punya bobot visual
# yang persis sama dengan kalimat penghubung di sebelahnya.
#
# Sengaja DUA peran, bukan lima. Tiap warna baru yang ditambahkan mengurangi
# arti semua warna yang sudah ada, dan halaman dengan lima jenis kotak
# berwarna sama tidak terbacanya dengan halaman tanpa kotak sama sekali.
# 6% dari blok prosa: cukup untuk memberi irama, terlalu jarang untuk jadi
# wallpaper.
_PERAN = (
    ("jebakan", re.compile(
        r"^(JEBAKAN|Jebakan|HATI-HATI|Hati-hati|AWAS|Awas|JANGAN|Jangan"
        r"|KESALAHAN|Kesalahan)\b")),
    ("aturan", re.compile(
        r"^(ATURAN|Aturan|INGAT|Ingat|CATATAN|Catatan|PERHATIKAN|Perhatikan"
        r"|Perlu diingat)\b")),
)


def _peran(teks):
    """"jebakan", "aturan", atau "" untuk sebuah blok prosa."""
    for nama, pola in _PERAN:
        if pola.match(teks):
            return nama
    return ""


def _sambung(baris):
    """Sambung baris-baris sebuah paragraf jadi satu, hormati pemenggalan."""
    keluar = ""
    for b in baris:
        potong = b.strip()
        if not potong:
            continue
        if not keluar:
            keluar = potong
        elif _POLA_PENGGAL.search(keluar) and potong[:1].islower():
            keluar += potong           # "benar-" + "benar" -> "benar-benar"
        else:
            keluar += " " + potong
    return keluar


def _prosa_menjorok(baris):
    """Blok menjorok ini sebenarnya paragraf biasa?

    Di sumbernya, penulis memakai indentasi untuk dua hal yang sangat berbeda:
    menyejajarkan kolom (tabel, contoh kode) DAN menandai "ini penjelasan
    tambahan di bawah kalimat tadi". Yang pertama wajib monospace; yang kedua
    justru rusak karenanya -- 420 paragraf biasa muncul sebagai kotak abu-abu
    berhuruf mesin ketik, dan pembaca kehilangan satu-satunya petunjuk bahwa
    yang di depannya bukan sesuatu yang perlu diketik ulang.

    Syaratnya sengaja KETAT, dan sisi salahnya dipilih: menyangka prosa sebagai
    kode cuma mempertahankan keadaan sekarang, sedangkan menyangka kode sebagai
    prosa MENGHAPUS perataan yang jadi isinya. Dari 420 calon, 181 lolos.
    """
    isi_baris = [b for b in baris if b.strip()]
    if len(isi_baris) < 2:
        return False                      # "bash --version" juga satu baris
    if any(len(b) - len(b.lstrip()) for b in isi_baris):
        return False                      # masih ada indentasi relatif
    if any(_POLA_KOLOM.search(b) for b in isi_baris):
        return False
    if any(_POLA_KODEISH.search(b) for b in isi_baris):
        return False
    if not isi_baris[-1].rstrip().endswith((".", "?", "!", '."', ".'")):
        return False                      # kalimat selalu ditutup
    gabung = " ".join(isi_baris)
    kata = _POLA_KATA.findall(gabung)
    return (len(kata) >= 12
            and len(kata) / max(1, len(gabung.split())) > 0.72)


def _penanda(baris):
    """(indentasi, urut, isi) kalau baris ini butir daftar; None kalau bukan.

    Penanda diperiksa TANPA peduli baris itu menjorok atau tidak. Versi
    sebelumnya memeriksa indentasi lebih dulu -- `if baris[:1] in (" ", "\\t")`
    -> "pra" -- sehingga setiap daftar yang ditulis menjorok (dan hampir semua
    daftar di kurikulum ini ditulis begitu) berakhir sebagai blok monospace
    abu-abu. 508 daftar di 11 bahasa terkena; yang terlihat pelajar adalah
    halaman materi yang seluruh prosanya menyerupai keluaran terminal, dan
    tidak ada cara membedakan mana penjelasan mana contoh kode.
    """
    m = _POLA_BUTIR.match(baris)
    if m:
        return len(m.group(1)), False, baris[m.end():].strip(), m.end()
    m = _POLA_NOMOR.match(baris)
    if m:
        return len(m.group(1)), True, baris[m.end():].strip(), m.end()
    return None


def _jenis_baris(baris):
    if not baris.strip():
        return "kosong"
    if _penanda(baris) is not None:
        return "daftar"
    if baris[:1] in (" ", "\t"):
        return "pra"
    return "teks"


def _susun_daftar(baris_list):
    """Baris-baris bertanda -> pohon butir.

    Tiga hal yang tidak boleh hilang di sini:

    * **Baris lanjutan disambung ke butirnya.** Butir yang kalimatnya lebih
      panjang dari satu baris ditulis menjorok di baris berikutnya tanpa
      penanda. Memperlakukannya sebagai butir tersendiri memecah satu kalimat
      jadi beberapa bulatan -- dan pemenggalannya jatuh di tempat yang cuma
      ditentukan lebar kolom berkas sumbernya, bukan oleh artinya.
    * **Yang menjorok LEBIH DALAM daripada kolom teks butirnya bukan lanjutan
      kalimat, melainkan contoh milik butir itu.** Begitu juga baris yang
      kolomnya disejajarkan spasi ganda. Keduanya disimpan apa adanya, karena
      perataannya memang isinya: `Integer.parseInt("3.0")` dengan komentar
      `// int tidak kenal titik desimal` di sebelahnya kehilangan seluruh
      maksudnya kalau dijadikan satu kalimat mengalir.
    * **Urutan asli dipertahankan.** Sebuah butir boleh berbentuk
      prosa -> contoh -> prosa lagi (CSS materi 1 menulisnya begitu), dan
      prosa penutupnya MENUNJUK contoh di atasnya. Menyatukan semua prosa di
      depan lalu menaruh contohnya di bawah membuat kata "itu" menunjuk ke
      belakang, ke sesuatu yang belum dibaca.
    * **Sarang dibaca dari indentasi penandanya.** Cuma 8 butir di seluruh
      kurikulum yang bersarang, tapi merataskannya berarti "syaratnya" dan
      "pengecualian syarat itu" berdiri sejajar seolah setara.

    Hasilnya:
    [{"teks": str,                              paragraf pertama butir
      "blok": [{"jenis": "teks"|"pra", "teks": str}],   sisanya, berurut
      "anak": {"urut": bool, "butir": [...]} | None}]
    """
    butir = []           # butir tingkat ini
    dasar = None         # indentasi penanda tingkat ini
    kolom = 0            # kolom tempat teks butir terakhir dimulai
    bagian = []          # [(jenis, [baris])] milik butir terakhir
    sarang = []          # baris mentah milik sarang yang sedang dikumpulkan
    urut_sarang = False

    def tumpuk(jenis, baris):
        if bagian and bagian[-1][0] == jenis:
            bagian[-1][1].append(baris)
        else:
            bagian.append((jenis, [baris]))

    def tutup_bagian():
        """Bagian -> teks butir + blok lanjutannya."""
        nonlocal bagian
        if not bagian:
            return
        keluar = []
        for jenis, baris in bagian:
            if jenis == "pra":
                umum = min(len(b) - len(b.lstrip()) for b in baris)
                keluar.append({"jenis": "pra",
                               "teks": "\n".join(b[umum:] for b in baris)})
            else:
                keluar.append({"jenis": "teks", "teks": _sambung(baris)})
        # Prosa pertama menempel ke butirnya sendiri; ia yang dibaca sebagai
        # "isi butir ini" oleh pencarian, peta halaman, dan pembaca layar.
        if keluar and keluar[0]["jenis"] == "teks":
            butir[-1]["teks"] = _sambung([butir[-1]["teks"],
                                          keluar.pop(0)["teks"]])
        butir[-1]["blok"] = keluar
        bagian = []

    def tutup_sarang():
        nonlocal sarang
        if not sarang:
            return
        butir[-1]["anak"] = {"urut": urut_sarang, "butir": _susun_daftar(sarang)}
        sarang = []

    for baris in baris_list:
        tanda = _penanda(baris)
        if tanda is None:
            if sarang:
                sarang.append(baris)
            elif butir:
                menjorok = len(baris) - len(baris.lstrip())
                tumpuk("pra" if (menjorok > kolom
                                 or _POLA_KOLOM.search(baris.strip()))
                       else "teks", baris)
            continue

        indent, urut, isi_butir, kol = tanda
        if dasar is None:
            dasar = indent
        if indent > dasar and butir:
            if not sarang:
                tutup_bagian()
                urut_sarang = urut
            sarang.append(baris)
            continue

        tutup_bagian()
        tutup_sarang()
        butir.append({"teks": isi_butir, "blok": [], "anak": None})
        kolom = kol

    tutup_bagian()
    tutup_sarang()
    return butir


_POLA_KEPALA_KELUARAN = re.compile(
    r"^(?:untuk input\s+.+?,\s*)?(?:keluaran|output)(?:nya)?"
    r"(?:\s+yang\s+(?:benar|diharapkan))?\s*(?:\([^)]*\))?\s*:$", re.I)


def blok_badan(baris_list):
    """Kelompokkan daftar baris jadi blok bertipe.

    Jenis blok yang dihasilkan:
      {"jenis": "teks",   "teks": "..."}      paragraf, baris aslinya dipertahankan
      {"jenis": "pra",    "teks": "..."}      spasi bermakna (tabel, contoh menjorok)
      {"jenis": "catatan","teks": "..."}      paragraf yang kebetulan ditulis menjorok
      {"jenis": "daftar", "butir": [...], "urut": bool, "mulai": int}

    Baris menjorok digabung apa adanya termasuk indentasi relatifnya, karena di
    situlah letak informasinya: tabel tipe data di materi Java hanya terbaca
    kalau kolomnya tetap sejajar. Kecuali satu hal: begitu sebuah daftar sedang
    berjalan, baris menjorok tanpa penanda adalah LANJUTAN butir terakhir, bukan
    tabel baru -- lihat `_susun_daftar`.
    """
    blok = []
    kini = []
    jenis_kini = None

    def tutup():
        nonlocal kini, jenis_kini
        if not kini:
            return
        if jenis_kini in ("pra", "keluaran"):
            # Buang indentasi BERSAMA supaya tidak ada lautan spasi di kiri,
            # tapi pertahankan indentasi relatif antar baris.
            umum = min((len(b) - len(b.lstrip()) for b in kini if b.strip()),
                       default=0)
            rata = [b[umum:] if b.strip() else "" for b in kini]
            if jenis_kini == "pra" and _prosa_menjorok(rata):
                # Baris digabung, BUKAN dipertahankan: lebar barisnya berasal
                # dari kolom berkas sumbernya (~62 huruf), bukan dari kolom
                # baca di layar. Menahannya berarti paragraf yang patah di
                # tempat yang tidak ada hubungannya dengan apa pun yang
                # dilihat pembaca.
                catatan = _sambung(rata)
                blok.append({"jenis": "catatan", "teks": catatan,
                             "peran": _peran(catatan)})
            else:
                blok.append({"jenis": "pra", "teks": "\n".join(rata)})
        elif jenis_kini == "daftar":
            tanda = _penanda(kini[0])
            # Nomor awal ikut dicatat. Daftar bernomor yang dipotong contoh
            # kode atau baris kosong pecah jadi beberapa blok; tanpa "mulai",
            # tiap potongan digambar sebagai <ol> baru dan nomornya tampil
            # 1, 1, 1, padahal di sumber (dan di terminal) tertulis 1, 2, 3.
            mulai = int(_POLA_NOMOR.match(kini[0]).group(2)) if tanda[1] else 1
            blok.append({"jenis": "daftar",
                         "urut": tanda[1],
                         "mulai": mulai,
                         "butir": _susun_daftar(kini)})
        else:
            # Paragraf disambung jadi satu baris, bukan dipertahankan
            # patahannya. Alasannya bisa diukur: baris di sumbernya dibungkus
            # untuk terminal 80 kolom (median 68 huruf, p90 81), sedangkan
            # kolom baca di layar 72ch -- jadi SEBAGIAN baris patah terlalu
            # cepat dan sisanya justru terbungkus ulang, dan yang terlihat
            # adalah tepi kanan yang bergerigi dengan potongan satu-dua kata
            # menggantung. Pemenggalan itu tidak membawa satu pun informasi;
            # ia cuma jejak lebar berkas sumbernya.
            #
            # Kecualinya blok yang kolomnya disejajarkan ("printf() -> ...",
            # "scanf()  -> ..."). Cuma 7 di seluruh kurikulum, dan di situ
            # patahan barisnya memang yang memisahkan dua entri.
            if any(_POLA_KOLOM.search(b) for b in kini):
                blok.append({"jenis": "teks", "teks": "\n".join(kini),
                             "peran": _peran(kini[0])})
            else:
                gabung = _sambung(kini)
                blok.append({"jenis": "teks", "teks": gabung,
                             "peran": _peran(gabung)})
        kini = []
        jenis_kini = None

    # Blok sesudah kepala keluaran ("Keluaran yang diharapkan:", "Untuk input
    # 80, keluarannya:") adalah contoh APA ADANYA sampai baris kosong pertama,
    # menjorok atau tidak. Pohon HTML yang diharapkan berbaris
    # `<!doctype html>` tanpa indentasi dulu disambung jadi paragraf prosa dan
    # baru `head` dst. masuk blok kode (19 soal, audit 2026-10-17), padahal
    # soalnya meminta "cocokkan sampai ke tanda bacanya". Semantiknya sama
    # dengan pembaca janji keluaran di tests/test_solutions.py: baris kosong
    # SEBELUM bloknya dilewati, baris kosong SESUDAHNYA menutupnya.
    menunggu_keluaran = False
    for baris in baris_list:
        jenis = _jenis_baris(baris)
        if jenis == "kosong":
            if jenis_kini == "keluaran":
                menunggu_keluaran = False
            tutup()
            continue
        if menunggu_keluaran or jenis_kini == "keluaran":
            if jenis_kini != "keluaran":
                tutup()
                jenis_kini = "keluaran"
                menunggu_keluaran = False
            kini.append(baris.rstrip())
            continue
        # Hanya kepala yang berdiri sebagai PROSA (tidak menjorok). "Output:"
        # di dalam contoh kode yang menjorok adalah bagian contoh itu, dan
        # memotongnya di situ memisahkan kode dari keluarannya.
        if baris[:1].strip() and _POLA_KEPALA_KELUARAN.match(baris.strip()):
            menunggu_keluaran = True
        # Baris menjorok tanpa penanda di TENGAH daftar adalah lanjutan butir
        # terakhir, jadi ia tidak menutup bloknya.
        if jenis == "pra" and jenis_kini == "daftar":
            kini.append(baris.rstrip())
            continue
        # Kebalikannya: butir YAML yang menempel di bawah contoh menjorok
        # adalah bagian contoh itu. Tanpa aturan ini, steps: di contoh
        # GitHub Actions terpotong dan sisanya digambar sebagai daftar
        # berbulatan di tengah berkas YAML.
        if (jenis == "daftar" and jenis_kini == "pra"
                and _POLA_BUTIR_YAML.match(baris.strip())
                and (_POLA_KUNCI_YAML.match(kini[-1].strip())
                     or any(_POLA_BUTIR_YAML.match(x.strip()) for x in kini))):
            kini.append(baris.rstrip())
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
        # Aturannya TIDAK ditulis ulang di sini -- lihat komentar panjang di
        # berkas.boleh_dijalankan_aplikasi soal kenapa SESI tidak seragam.
        "bisa_dijalankan": berkas.boleh_dijalankan_aplikasi(bahasa, p.jenis),
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
            # Penanda, bukan kunci: kuis tetap bisa dibuka kapan saja.
            "siap": kuis_materi.kuis_siap(lang, q, data),
            "sisa_materi": len(kuis_materi.sisa_materi(lang, q, data)),
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
            # Proyek akhir: satu latihan penutup yang menguji apakah materinya
            # benar-benar nyambung, bukan apakah tiap bagiannya hafal. Ia
            # tetap latihan biasa di mata seluruh mesin — dinilai runner yang
            # sama, XP dari progress yang sama — karena definisi "lulus" cuma
            # boleh ada satu. Yang ditambahkan cuma penandanya.
            "proyek": bool(e.get("proyek")),
            "bookmark": kunci(kat, e["title"]) in data["bookmark"],
        })
    return keluar


# ------------------------------------------------------------------ pencarian

def _cuplik(baris_list, kata, panjang=150, rendah_list=None):
    """Potongan teks di sekitar kata yang dicari.

    `rendah_list` (opsional) adalah `baris_list` yang sudah dikecilkan, dari
    indeks pencarian; hasilnya sama persis, tanpa mengecilkan ulang.
    """
    rendah = kata.lower()
    kecil = rendah_list if rendah_list is not None else (
        b.lower() for b in baris_list)
    for baris, bawah in zip(baris_list, kecil):
        pos = bawah.find(rendah)
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


_INDEKS_CARI = {}


def _entri_indeks(baris):
    """(baris, versi huruf kecil, gabungan huruf kecil) untuk satu butir."""
    kecil = [b.lower() for b in baris]
    return baris, kecil, "\x00".join(kecil)


def _indeks_bahasa(lang):
    """Teks tiap materi/kuis/latihan, dikecilkan SEKALI lalu dipakai ulang.

    Pencarian dipanggil tiap ketikan; mengecilkan ulang jutaan baris per
    permintaan adalah biaya terbesarnya. Kurikulum statis selama proses hidup,
    tapi indeks disahkan dengan identitas daftar sumbernya supaya tes yang
    memasang bahasa buatan tidak membaca indeks bahasa lain.
    """
    sumber = (lang["materials"], lang["quizzes"], lang["exercises"])
    ada = _INDEKS_CARI.get(lang["key"])
    if ada is not None and all(a is b for a, b in zip(ada[0], sumber)):
        return ada[1]
    materi = [_entri_indeks(_teks_materi(m)) for m in lang["materials"]]
    kuis = []
    for q in lang["quizzes"]:
        baris = [q["title"]]
        for s in q["questions"]:
            baris.append(s["q"])
            baris.extend(s["options"])
            baris.append(s.get("explanation", ""))
        kuis.append(_entri_indeks(baris))
    latihan = []
    for e in lang["exercises"]:
        baris = ([e["title"]] + list(e.get("question") or [])
                 + list(e.get("hints") or [])
                 + e.get("solution", "").splitlines())
        latihan.append(_entri_indeks(baris))
    indeks = {"materi": materi, "kuis": kuis, "latihan": latihan}
    _INDEKS_CARI[lang["key"]] = (sumber, indeks)
    return indeks


def _ada(entri, rendah):
    """Sama dengan `any(rendah in b.lower() for b in baris)`."""
    if "\x00" in rendah:
        return any(rendah in b for b in entri[1])
    return rendah in entri[2]


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
        indeks = _indeks_bahasa(lang)
        if tipe in ("semua", "materi"):
            for i, m in enumerate(lang["materials"]):
                entri = indeks["materi"][i]
                baris = entri[0]
                if not _ada(entri, rendah):
                    continue
                hasil.append({
                    "tipe": "materi", "bahasa": lang["key"],
                    "label_bahasa": lang["label"], "indeks": i,
                    "judul": m["title"],
                    "cuplikan": _cuplik(baris[1:], kata,
                                        rendah_list=entri[1][1:]),
                    "terkunci": i not in _terbuka(lang),
                    "skor": 0 if rendah in m["title"].lower() else 1,
                })

        if tipe in ("semua", "kuis"):
            for i, q in enumerate(lang["quizzes"]):
                entri = indeks["kuis"][i]
                baris = entri[0]
                if not _ada(entri, rendah):
                    continue
                hasil.append({
                    "tipe": "kuis", "bahasa": lang["key"],
                    "label_bahasa": lang["label"], "indeks": i,
                    "judul": q["title"],
                    "cuplikan": _cuplik(baris[1:], kata,
                                        rendah_list=entri[1][1:]),
                    "skor": 0 if rendah in q["title"].lower() else 1,
                })

        if tipe in ("semua", "latihan"):
            for i, e in enumerate(lang["exercises"]):
                entri = indeks["latihan"][i]
                baris = entri[0]
                if not _ada(entri, rendah):
                    continue
                hasil.append({
                    "tipe": "latihan", "bahasa": lang["key"],
                    "label_bahasa": lang["label"], "indeks": i,
                    "judul": e["title"],
                    "cuplikan": _cuplik(baris[1:], kata,
                                        rendah_list=entri[1][1:]),
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
