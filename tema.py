"""Palet warna terminal: deteksi kemampuan, tema, dan peran warna.

Kenapa modul terpisah dari `utils.py`?

`utils.C` menyimpan kode ANSI MENTAH (merah, hijau, tebal). Memakainya langsung
di seluruh aplikasi berarti setiap layar memutuskan sendiri "error itu warna
apa" -- dan begitu ada yang ingin tema terang atau terminal tanpa warna, semua
keputusan itu tersebar di puluhan berkas.

Modul ini menambahkan satu lapis di atasnya: PERAN. Kode aplikasi meminta
warna untuk peran ("galat", "sukses", "kode_kunci"), bukan warna literal.
Tema yang menentukan peran itu jadi warna apa, dan seberapa kaya warnanya
menyesuaikan kemampuan terminal (truecolor / 256 / 16 / tanpa warna).

`utils.C` tetap ada dan tetap bekerja supaya kode lama tidak perlu disentuh.
"""

import os
import sys

# --------------------------------------------------------------- kemampuan

TANPA_WARNA = 0
WARNA_16 = 1
WARNA_256 = 2
WARNA_PENUH = 3

_NAMA_KEDALAMAN = {
    TANPA_WARNA: "tanpa warna",
    WARNA_16: "16 warna",
    WARNA_256: "256 warna",
    WARNA_PENUH: "16 juta warna",
}


def deteksi_kedalaman(aliran=None):
    """Tebak berapa banyak warna yang sanggup ditampilkan terminal ini.

    Urutan pemeriksaan mengikuti kesepakatan umum: NO_COLOR menang atas
    segalanya, FORCE_COLOR memaksa nyala, sisanya ditebak dari TERM &
    COLORTERM.
    """
    aliran = aliran if aliran is not None else sys.stdout

    if os.environ.get("NO_COLOR"):
        return TANPA_WARNA

    dipaksa = os.environ.get("FORCE_COLOR", "")
    if dipaksa and dipaksa != "0":
        # FORCE_COLOR=1/2/3 dipakai sebagian tooling untuk memilih kedalaman.
        return {"1": WARNA_16, "2": WARNA_256, "3": WARNA_PENUH}.get(dipaksa, WARNA_PENUH)

    if not (hasattr(aliran, "isatty") and aliran.isatty()):
        return TANPA_WARNA

    term = os.environ.get("TERM", "")
    if term == "dumb":
        return TANPA_WARNA

    if os.name == "nt":
        modern = (
            os.environ.get("WT_SESSION")
            or os.environ.get("ANSICON")
            or os.environ.get("ConEmuANSI") == "ON"
        )
        if modern:
            return WARNA_PENUH
        try:
            if sys.getwindowsversion().major >= 10:  # type: ignore[attr-defined]
                return WARNA_256
        except (AttributeError, OSError):
            pass
        return TANPA_WARNA

    colorterm = os.environ.get("COLORTERM", "").lower()
    if "truecolor" in colorterm or "24bit" in colorterm:
        return WARNA_PENUH
    if "256" in term or os.environ.get("TERM_PROGRAM") in ("iTerm.app", "Apple_Terminal"):
        return WARNA_256
    if term:
        return WARNA_16
    return TANPA_WARNA


def nama_kedalaman(kedalaman):
    return _NAMA_KEDALAMAN.get(kedalaman, "?")


# ------------------------------------------------------------------- warna

def _rgb(r, g, b, latar=False):
    return f"\033[{48 if latar else 38};2;{r};{g};{b}m"


def _x256(n, latar=False):
    return f"\033[{48 if latar else 38};5;{n}m"


class Warna:
    """Satu warna yang tahu cara menurunkan dirinya ke terminal miskin warna.

    Disimpan sebagai tiga varian sekaligus supaya perpindahan tema tidak perlu
    menghitung ulang apa pun: cukup pilih varian sesuai kedalaman terminal.
    """

    __slots__ = ("rgb", "x256", "ansi16")

    def __init__(self, rgb, x256, ansi16):
        self.rgb = rgb
        self.x256 = x256
        self.ansi16 = ansi16

    def kode(self, kedalaman, latar=False):
        if kedalaman >= WARNA_PENUH:
            return _rgb(*self.rgb, latar=latar)
        if kedalaman >= WARNA_256:
            return _x256(self.x256, latar=latar)
        if kedalaman >= WARNA_16:
            # 30..37 -> 40..47 dan 90..97 -> 100..107 untuk versi latar.
            return f"\033[{self.ansi16 + 10 if latar else self.ansi16}m"
        return ""


# Palet dasar. Nilai 16-warna sengaja memakai varian TERANG (90-97) untuk tema
# gelap karena varian gelap sering nyaris tak terbaca di latar hitam.
_P = {
    "putih":      Warna((230, 233, 239), 253, 97),
    "abu":        Warna((150, 158, 172), 245, 37),
    "abu_gelap":  Warna((122, 130, 145), 242, 90),
    "merah":      Warna((240, 105, 105), 203, 91),
    "hijau":      Warna((126, 204, 128), 114, 92),
    "kuning":     Warna((240, 200, 110), 221, 93),
    "biru":       Warna((114, 170, 245), 111, 94),
    "ungu":       Warna((198, 146, 244), 176, 95),
    "sian":       Warna((110, 208, 214), 80, 96),
    "jingga":     Warna((238, 160, 96), 215, 33),
    "merah_muda": Warna((240, 140, 190), 211, 95),

    # Varian untuk latar terang.
    "t_teks":   Warna((32, 36, 46), 235, 30),
    "t_abu":    Warna((90, 98, 112), 240, 90),
    "t_merah":  Warna((176, 32, 48), 124, 31),
    "t_hijau":  Warna((24, 122, 60), 28, 32),
    "t_kuning": Warna((150, 104, 8), 136, 33),
    "t_biru":   Warna((28, 90, 190), 25, 34),
    "t_ungu":   Warna((118, 52, 174), 91, 35),
    "t_sian":   Warna((14, 110, 122), 30, 36),
}


# Peran yang dikenal aplikasi. Menambah peran baru wajib menambahkannya di
# SEMUA tema di bawah -- `_periksa_tema()` menegakkan aturan itu saat impor.
PERAN = (
    "teks", "redup", "judul", "subjudul", "garis",
    "sukses", "galat", "peringatan", "info", "aksen",
    "tingkat_mudah", "tingkat_sedang", "tingkat_menengah", "tingkat_sulit",
    "kode_teks", "kode_kunci", "kode_tipe", "kode_bawaan", "kode_string",
    "kode_angka", "kode_komentar", "kode_fungsi", "kode_operator", "kode_khusus",
    "beda_tambah", "beda_kurang", "beda_sama", "sorot",
)


TEMA = {
    "gelap": {
        "keterangan": "Bawaan. Untuk terminal berlatar gelap.",
        "warna": {
            "teks": "putih", "redup": "abu_gelap", "judul": "kuning",
            "subjudul": "ungu", "garis": "sian",
            "sukses": "hijau", "galat": "merah", "peringatan": "kuning",
            "info": "biru", "aksen": "sian",
            "tingkat_mudah": "hijau", "tingkat_sedang": "kuning",
            "tingkat_menengah": "jingga", "tingkat_sulit": "merah",
            "kode_teks": "putih", "kode_kunci": "ungu", "kode_tipe": "sian",
            "kode_bawaan": "biru", "kode_string": "hijau", "kode_angka": "jingga",
            "kode_komentar": "abu_gelap", "kode_fungsi": "kuning",
            "kode_operator": "merah_muda", "kode_khusus": "merah",
            "beda_tambah": "hijau", "beda_kurang": "merah", "beda_sama": "abu",
            "sorot": "kuning",
        },
    },
    "terang": {
        "keterangan": "Untuk terminal berlatar putih/terang.",
        "warna": {
            "teks": "t_teks", "redup": "t_abu", "judul": "t_ungu",
            "subjudul": "t_biru", "garis": "t_sian",
            "sukses": "t_hijau", "galat": "t_merah", "peringatan": "t_kuning",
            "info": "t_biru", "aksen": "t_sian",
            "tingkat_mudah": "t_hijau", "tingkat_sedang": "t_kuning",
            "tingkat_menengah": "t_merah", "tingkat_sulit": "t_merah",
            "kode_teks": "t_teks", "kode_kunci": "t_ungu", "kode_tipe": "t_sian",
            "kode_bawaan": "t_biru", "kode_string": "t_hijau", "kode_angka": "t_merah",
            "kode_komentar": "t_abu", "kode_fungsi": "t_biru",
            "kode_operator": "t_merah", "kode_khusus": "t_merah",
            "beda_tambah": "t_hijau", "beda_kurang": "t_merah", "beda_sama": "t_abu",
            "sorot": "t_kuning",
        },
    },
    "kontras": {
        "keterangan": "Kontras tinggi, sedikit warna. Ramah low-vision.",
        "warna": {
            "teks": "putih", "redup": "abu", "judul": "putih",
            "subjudul": "kuning", "garis": "putih",
            "sukses": "hijau", "galat": "merah", "peringatan": "kuning",
            "info": "putih", "aksen": "kuning",
            "tingkat_mudah": "hijau", "tingkat_sedang": "kuning",
            "tingkat_menengah": "kuning", "tingkat_sulit": "merah",
            "kode_teks": "putih", "kode_kunci": "kuning", "kode_tipe": "putih",
            "kode_bawaan": "putih", "kode_string": "hijau", "kode_angka": "putih",
            "kode_komentar": "abu", "kode_fungsi": "kuning",
            "kode_operator": "putih", "kode_khusus": "merah",
            "beda_tambah": "hijau", "beda_kurang": "merah", "beda_sama": "abu",
            "sorot": "kuning",
        },
    },
    "mono": {
        "keterangan": "Tanpa warna sama sekali. Hanya tebal & redup.",
        "warna": {},  # diisi otomatis di bawah: semua peran -> tanpa warna
    },
}

for _p in PERAN:
    TEMA["mono"]["warna"][_p] = None


def _periksa_tema():
    """Pastikan setiap tema mendefinisikan setiap peran, dan warnanya ada.

    Peran yang lupa didefinisikan akan diam-diam jadi teks tanpa warna di
    tengah aplikasi. Lebih baik meledak di sini, saat impor.
    """
    for nama, tema in TEMA.items():
        kurang = [p for p in PERAN if p not in tema["warna"]]
        if kurang:
            raise ValueError(f"tema '{nama}' belum mendefinisikan peran: {kurang}")
        for peran, kunci_warna in tema["warna"].items():
            if kunci_warna is not None and kunci_warna not in _P:
                raise ValueError(
                    f"tema '{nama}' peran '{peran}' memakai warna tak dikenal: {kunci_warna}"
                )


_periksa_tema()


# ------------------------------------------------------------ status aktif

RESET = "\033[0m"
TEBAL = "\033[1m"
SAMAR = "\033[2m"
MIRING = "\033[3m"
GARIS_BAWAH = "\033[4m"
BALIK = "\033[7m"

_nama_aktif = "gelap"
_kedalaman = deteksi_kedalaman()
_peta = {}


def _bangun():
    """Terjemahkan tema aktif jadi tabel peran -> kode ANSI siap pakai."""
    global _peta
    tema = TEMA.get(_nama_aktif, TEMA["gelap"])
    _peta = {}
    for peran in PERAN:
        kunci_warna = tema["warna"].get(peran)
        if kunci_warna is None or _kedalaman == TANPA_WARNA:
            _peta[peran] = ""
        else:
            _peta[peran] = _P[kunci_warna].kode(_kedalaman)


_bangun()


def pakai_tema(nama):
    """Ganti tema aktif. Return True kalau namanya dikenal."""
    global _nama_aktif
    if nama not in TEMA:
        return False
    _nama_aktif = nama
    _bangun()
    return True


def pakai_kedalaman(kedalaman):
    """Paksa kedalaman warna tertentu (dipakai flag --tanpa-warna dan pengaturan)."""
    global _kedalaman
    _kedalaman = kedalaman
    _bangun()


def tema_aktif():
    return _nama_aktif


def kedalaman_aktif():
    return _kedalaman


def berwarna():
    return _kedalaman != TANPA_WARNA


def w(peran):
    """Kode ANSI untuk sebuah peran. String kosong kalau warna mati."""
    return _peta.get(peran, "")


def cat(teks, peran=None, *gaya):
    """Warnai teks menurut peran + gaya tambahan (TEBAL, SAMAR, ...).

    Selalu aman: kalau warna mati, teks dikembalikan apa adanya sehingga
    perhitungan lebar kolom tidak perlu tahu-menahu soal ANSI.
    """
    if _kedalaman == TANPA_WARNA:
        return teks
    awalan = (_peta.get(peran, "") if peran else "") + "".join(gaya)
    if not awalan:
        return teks
    return f"{awalan}{teks}{RESET}"


def daftar_tema():
    """[(nama, keterangan, aktif?)] untuk ditampilkan di menu pengaturan."""
    return [(n, t["keterangan"], n == _nama_aktif) for n, t in TEMA.items()]
