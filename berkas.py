"""Menjawab satu pertanyaan pelajar: "kode ini perlu aku ketik ke file atau tidak?"

Sebelum ini, setiap contoh kode muncul begitu saja di dalam kotak tanpa
keterangan. Pemula tidak punya cara tahu apakah blok itu:

  * program utuh yang harus disimpan sebagai berkas lalu dijalankan,
  * potongan penggalan yang cuma menjelaskan sintaks dan akan error kalau
    dijalankan sendirian, atau
  * kumpulan perintah yang diketik langsung di sesi database/terminal.

Modul ini mengklasifikasikan blok kode ke salah satu dari tiga jenis itu,
lalu menyusun kalimat instruksi yang konkret: nama berkasnya apa dan
perintah untuk menjalankannya apa.

Deteksinya sengaja konservatif. Salah menyebut potongan sebagai "program utuh"
akan menyuruh pelajar menjalankan kode yang pasti gagal, dan itu jauh lebih
membingungkan daripada tidak memberi instruksi sama sekali. Kalau ragu,
kembalikan POTONGAN.
"""

import re

PROGRAM = "program"      # berkas mandiri, bisa langsung dijalankan
POTONGAN = "potongan"    # penggalan penjelas, tidak berdiri sendiri
SESI = "sesi"            # diketik di dalam sesi database / shell interaktif
MULTI = "multi"          # satu contoh yang terdiri dari beberapa berkas
ILUSTRASI = "ilustrasi"  # diagram, tabel, atau struktur folder -- bukan kode

# Panjang maksimal slug nama berkas supaya perintahnya enak dibaca.
MAKS_SLUG = 20


class Petunjuk:
    """Instruksi siap tampil untuk satu blok kode."""

    __slots__ = ("jenis", "nama", "perintah", "instruksi", "keterangan", "berkas")

    def __init__(self, jenis, nama="", perintah=(), instruksi="", keterangan="",
                 berkas=()):
        self.jenis = jenis
        self.nama = nama
        self.perintah = list(perintah)
        self.instruksi = instruksi
        self.keterangan = keterangan
        self.berkas = list(berkas)   # dipakai saat jenis == MULTI

    @property
    def perlu_berkas(self):
        return self.jenis in (PROGRAM, MULTI)

    def __repr__(self):
        return f"Petunjuk({self.jenis!r}, {self.nama!r}, {self.perintah!r})"


# --------------------------------------------------------------- nama berkas

def slug(teks, maks=MAKS_SLUG):
    """'2. Variabel & Tipe Data' -> 'variabel-tipe-data'.

    Nomor urut di depan judul dibuang karena tidak menjelaskan isi, dan kata
    penghubung dibuang supaya nama berkasnya tetap pendek.
    """
    teks = re.sub(r"^\s*\d+[\.\):]?\s*", "", teks or "")
    teks = re.sub(r"[^\w\s-]", " ", teks, flags=re.UNICODE)
    kata = [k for k in re.split(r"[\s_-]+", teks.lower()) if k]

    buang = {"contoh", "dan", "atau", "di", "ke", "dari", "untuk", "dengan",
             "yang", "pada", "the", "a", "an", "dalam", "cara", "amp"}
    inti = [k for k in kata if k not in buang] or kata
    if not inti:
        return "contoh"

    hasil = inti[0]
    for k in inti[1:]:
        if len(hasil) + 1 + len(k) > maks:
            break
        hasil += "-" + k
    return hasil[:maks].strip("-") or "contoh"


def _kelas_java(kode):
    m = re.search(r"\bpublic\s+(?:final\s+|abstract\s+)?class\s+([A-Za-z_]\w*)", kode)
    if m:
        return m.group(1)
    m = re.search(r"\b(?:class|interface|enum|record)\s+([A-Za-z_]\w*)", kode)
    return m.group(1) if m else None


def _pascal(teks):
    potongan = [p for p in slug(teks, maks=40).split("-") if p]
    nama = "".join(p.capitalize() for p in potongan) or "Contoh"
    return nama if nama[0].isalpha() else "Contoh" + nama


EKSTENSI = {
    "python": ".py", "javascript": ".js", "java": ".java", "c": ".c",
    "cpp": ".cpp", "go": ".go", "bash": ".sh", "sql": ".sql",
    "html": ".html", "css": ".css",
}


def nama_berkas(bahasa, kode, konteks=""):
    """Nama berkas yang disarankan untuk sebuah blok kode."""
    if bahasa == "java":
        # javac mewajibkan nama berkas sama persis dengan nama kelas public.
        return (_kelas_java(kode) or _pascal(konteks)) + ".java"
    if bahasa == "go":
        # `go run` pada satu berkas package main; nama bebas, main.go paling lazim.
        return "main.go"
    if bahasa == "html":
        # index.html adalah nama yang dicari server web mana pun saat sebuah
        # folder dibuka. Membiasakannya sejak halaman pertama menghemat satu
        # kebingungan besar nanti.
        return "index.html"
    if bahasa == "css":
        return "gaya.css"
    return slug(konteks) + EKSTENSI.get(bahasa, ".txt")


def perintah_jalan(bahasa, nama):
    """Perintah shell untuk menjalankan berkas tersebut."""
    batang = nama.rsplit(".", 1)[0]
    return {
        "python": [f"python3 {nama}"],
        "javascript": [f"node {nama}"],
        "java": [f"javac {nama}", f"java {batang}"],
        "c": [f"gcc {nama} -o {batang}", f"./{batang}"],
        "cpp": [f"g++ {nama} -o {batang}", f"./{batang}"],
        "go": [f"go run {nama}"],
        "bash": [f"bash {nama}"],
        "sql": [f"sqlite3 belajar.db < {nama}"],
        # HTML dan CSS tidak dijalankan dari terminal: keduanya dibuka browser.
        # Perintah yang benar-benar dipakai orang untuk melihat hasilnya adalah
        # membuka berkasnya, bukan mengetik apa pun.
        "html": [f"Buka {nama} di browser (klik dua kali, atau Ctrl+O)"],
        "css": ["Tautkan dari HTML: "
                f'<link rel="stylesheet" href="{nama}">',
                "lalu buka berkas HTML-nya di browser"],
    }.get(bahasa, [])


# ----------------------------------------------------------------- deteksi

def _diawali_indentasi(kode):
    """Baris berkode pertama menjorok ke dalam -> jelas cuplikan dari tengah blok."""
    for baris in kode.splitlines():
        if not baris.strip():
            continue
        if baris.strip().startswith(("#", "//", "--", "/*", "*")):
            continue  # komentar pembuka tidak menentukan
        return baris[:1] in (" ", "\t")
    return False


def _ada_elipsis(kode):
    """'...' di luar konteks Go/Python variadic menandakan kode sengaja dipotong."""
    return bool(re.search(r"^\s*(\.\.\.|…)\s*$", kode, re.MULTILINE))


def _ilustrasi(kode):
    """True kalau blok ini diagram, peta rute, atau pohon folder -- bukan kode.

    Materi konseptual memakai blok kode untuk menggambar relasi antar entitas
    dan struktur direktori. Menyebutnya "potongan kode" menyesatkan; pelajar
    bisa mengira ada yang perlu diketik.

    Penanda kode dihitung per baris, bukan sekali untuk seluruh blok, supaya
    diagram yang kebetulan memuat satu tanda kurung tidak salah dikira kode.
    """
    baris = [b for b in kode.splitlines() if b.strip()]
    if not baris:
        return False

    berkode = 0
    for b in baris:
        isi = b.strip()
        if isi.startswith(("#", "//", "--", "*", "/*")):
            continue
        # Tanda baca yang praktis selalu ada di kode sungguhan.
        # Kurung kurawal hanya dihitung kalau berperan sebagai pembatas blok
        # (di ujung baris atau sendirian), bukan placeholder seperti /items/{id}
        # pada peta rute.
        if re.search(r";\s*$"                # akhir pernyataan
                     r"|^[{}]\s*$"           # kurawal sendirian sebaris
                     r"|\{\s*$"              # kurawal pembuka di ujung baris
                     r"|^\}"                 # kurawal penutup di awal baris
                     r"|\w\s*=\s*\S"         # penugasan
                     r"|\w\s*\("             # pemanggilan fungsi
                     r"|::|=>", isi):
            berkode += 1

    if berkode / len(baris) >= 0.25:
        return False

    # Penanda visual khas diagram dan pohon direktori.
    penanda = re.search(r"-{2,}>|<-{2,}|─|│|├|└|\|\s{2,}\||^\s*\w+/\s*$",
                        kode, re.MULTILINE)
    kolom = sum(1 for b in baris if re.search(r"\S\s{3,}\S", b))
    return bool(penanda) or kolom / len(baris) >= 0.6


def _kurung_seimbang(kode):
    tanpa_teks = re.sub(r'"[^"\n]*"|\'[^\'\n]*\'', "", kode)
    return (tanpa_teks.count("{") == tanpa_teks.count("}")
            and tanpa_teks.count("(") == tanpa_teks.count(")"))


def _python_lengkap(kode):
    # Python punya pemeriksa sintaks bawaan, jadi tidak perlu menebak-nebak.
    try:
        compile(kode, "<materi>", "exec")
        return True
    except (SyntaxError, ValueError, TypeError, MemoryError):
        return False


# Komentar penanda seperti  /* ===== File: matematika.h ===== */
# atau  // ==== file: kalkulator/kalkulator.go ====
_PENANDA_BERKAS = re.compile(
    r"""(?:/\*|//|\#|--)\s*=*\s*[Ff]ile\s*:\s*([\w./-]+)""")


def berkas_ganda(kode):
    """Daftar nama berkas kalau blok ini sengaja memuat beberapa berkas sekaligus.

    Materi tentang kompilasi multi-file dan struktur package menuliskan
    beberapa berkas dalam satu blok, dipisah komentar penanda. Menyuruh
    pelajar menyimpannya sebagai satu berkas pasti gagal dikompilasi.
    """
    nama = _PENANDA_BERKAS.findall(kode or "")
    # Satu penanda saja bisa jadi cuma judul; baru disebut multi kalau >= 2.
    hasil = []
    for n in nama:
        if n not in hasil:
            hasil.append(n)
    return hasil if len(hasil) >= 2 else []


# Tipe java.util yang lazim dipakai di contoh tanpa disertai import-nya.
_TIPE_BUTUH_IMPORT = ("List", "ArrayList", "Map", "HashMap", "Set", "HashSet",
                      "Scanner", "Arrays", "Collections", "Optional", "Queue",
                      "LinkedList", "TreeMap", "Iterator", "Comparator")


def _java_import_kurang(kode):
    """True kalau kode memakai tipe java.util tapi tidak mengimpornya.

    Contoh materi sering fokus pada satu konsep dan menghilangkan baris import
    supaya ringkas. Kode seperti itu tidak akan dikompilasi kalau pelajar
    menyalinnya apa adanya, jadi jangan disebut program utuh.
    """
    if re.search(r"^\s*import\s+java\.util\.\*\s*;", kode, re.MULTILINE):
        return False
    for tipe in _TIPE_BUTUH_IMPORT:
        dipakai = re.search(rf"\b{tipe}\s*[<(\[]|\b{tipe}\s+\w+\s*[=;)]", kode)
        if dipakai and not re.search(rf"^\s*import\s+[\w.]*\b{tipe}\s*;",
                                     kode, re.MULTILINE):
            return True
    return False


def _java_lengkap(kode):
    if _java_import_kurang(kode):
        return False
    return bool(re.search(r"\bstatic\s+void\s+main\s*\(", kode)
                and re.search(r"\b(class|record|enum)\s+\w+", kode)
                and _kurung_seimbang(kode))


def _go_lengkap(kode):
    return bool(re.search(r"^\s*package\s+main\b", kode, re.MULTILINE)
                and re.search(r"\bfunc\s+main\s*\(\s*\)", kode)
                and _kurung_seimbang(kode))


def _c_lengkap(kode):
    return bool(re.search(r"\b(?:int|void)\s+main\s*\(", kode)
                and _kurung_seimbang(kode))


def _js_lengkap(kode):
    # JavaScript tidak mewajibkan fungsi pembungkus, jadi apa pun yang utuh
    # secara struktur bisa dijalankan node.
    return _kurung_seimbang(kode)


def _html_lengkap(kode):
    """Halaman utuh, bukan potongan markup.

    Yang dicari <html> atau <!doctype — bukan sekadar adanya tag. Sebagian
    besar contoh di materi HTML memang cuma beberapa elemen untuk menunjukkan
    satu hal, dan menyuruh pelajar menyimpan tiap potongan itu sebagai berkas
    justru mengaburkan mana yang benar-benar sebuah halaman.
    """
    rendah = kode.lower()
    return "<!doctype" in rendah or "<html" in rendah


def _bash_lengkap(kode):
    if re.search(r"^\s*(fi|done|esac|\})\s*$", kode.splitlines()[0] if kode.splitlines() else ""):
        return False
    return True


def jenis_kode(bahasa, kode):
    """Klasifikasikan blok kode: PROGRAM, MULTI, POTONGAN, atau SESI."""
    if not kode or not kode.strip():
        return POTONGAN
    if berkas_ganda(kode):
        return MULTI
    if _ilustrasi(kode):
        return ILUSTRASI
    if _ada_elipsis(kode) or _diawali_indentasi(kode):
        return POTONGAN

    if bahasa == "sql":
        # Query yang membuat tabelnya sendiri bisa disimpan sebagai berkas.
        # Selebihnya mengandalkan tabel dari materi sebelumnya, jadi harus
        # diketik di sesi database yang sudah berisi data.
        return PROGRAM if re.search(r"\bCREATE\s+TABLE\b", kode, re.I) else SESI

    if bahasa == "html":
        return PROGRAM if _html_lengkap(kode) else POTONGAN
    if bahasa == "css":
        # Satu blok aturan pun sudah berupa berkas gaya yang sah dan bisa
        # ditautkan apa adanya. CSS tidak punya "titik masuk" yang harus ada.
        return PROGRAM if "{" in kode and "}" in kode else POTONGAN

    pemeriksa = {
        "python": _python_lengkap,
        "java": _java_lengkap,
        "go": _go_lengkap,
        "c": _c_lengkap,
        "cpp": _c_lengkap,
        "javascript": _js_lengkap,
        "bash": _bash_lengkap,
    }.get(bahasa)

    if pemeriksa is None:
        return POTONGAN
    return PROGRAM if pemeriksa(kode) else POTONGAN


# ------------------------------------------------------------------ petunjuk

LABEL_SESI = {
    "sql": ("Ketik langsung di sesi database (mysql atau sqlite3)",
            "Perlu tabel dari materi sebelumnya, jadi bukan berkas terpisah."),
}


def petunjuk_kode(bahasa, kode, konteks=""):
    """Susun instruksi lengkap untuk satu blok kode materi."""
    jenis = jenis_kode(bahasa, kode)

    if jenis == MULTI:
        daftar = berkas_ganda(kode)
        return Petunjuk(
            MULTI, berkas=daftar,
            instruksi="Buat " + str(len(daftar)) + " berkas terpisah: "
                      + ", ".join(daftar),
            keterangan="Pisahkan sesuai komentar penanda di dalam kode.",
        )

    if jenis == ILUSTRASI:
        return Petunjuk(
            ILUSTRASI,
            instruksi="Diagram / ilustrasi - bukan kode, tidak perlu diketik",
        )

    if jenis == SESI:
        instruksi, keterangan = LABEL_SESI.get(
            bahasa, ("Ketik langsung di sesi interaktif", ""))
        return Petunjuk(SESI, instruksi=instruksi, keterangan=keterangan)

    if jenis == POTONGAN:
        return Petunjuk(
            POTONGAN,
            instruksi="Potongan contoh - tidak perlu dibuat berkas",
            keterangan="Bagian dari kode yang lebih besar, akan error kalau dijalankan sendiri.",
        )

    nama = nama_berkas(bahasa, kode, konteks)
    perintah = perintah_jalan(bahasa, nama)
    return Petunjuk(PROGRAM, nama=nama, perintah=perintah,
                    instruksi=f"Buat berkas: {nama}")


def petunjuk_latihan(bahasa, nama):
    """Instruksi untuk latihan, di mana nama berkasnya sudah ditentukan aplikasi."""
    return Petunjuk(PROGRAM, nama=nama, perintah=perintah_jalan(bahasa, nama),
                    instruksi=f"Berkas jawabanmu: {nama}")
