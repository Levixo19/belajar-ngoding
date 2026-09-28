"""Status bab: mana yang sudah tuntas, mana yang terbuka, mana yang menunggu.

Modul ini TIDAK menyimpan apa pun dan tidak memutuskan apa pun soal kelulusan.
Ia membaca `materi_dibaca` yang sudah dicatat progress.py, lalu menjawab satu
pertanyaan: bab mana yang boleh dibuka sekarang. Batas itu penting dan dijaga
di seluruh aplikasi (lihat AGENTS.md): begitu ada tempat kedua yang memutuskan
"selesai", terminal dan web akan berbeda pendapat tentang hal yang sama.

ATURAN MEMBUKANYA sengaja cuma satu, dan sengaja longgar:

    Bab berikutnya terbuka kalau SELURUH MATERI bab sebelumnya sudah dibaca
    tuntas. Kuis dan latihan tidak ikut menentukan.

Menuntut kuisnya lulus atau latihannya selesai terdengar lebih ketat dan lebih
"benar", tapi akibatnya bisa diperkirakan: satu latihan sulit yang belum
ditaklukkan mengunci seluruh sisa kurikulum, dan orang yang mandek di situ
tidak punya apa pun lagi untuk dikerjakan selain hal yang sedang membuatnya
mandek. Membaca sampai habis adalah syarat yang bisa dipenuhi siapa pun yang
memang mengerjakannya, dan itu yang dibutuhkan sebuah pintu.

Bab PERTAMA selalu terbuka. Bab yang sudah pernah dimasuki tidak pernah
terkunci lagi.

PINTU DARURATNYA satu saklar: `buka_semua_bab` di Pengaturan. Jalur linear
tanpa jalan keluar menghukum orang yang sudah bisa — seseorang yang sudah
tiga tahun menulis Python tidak perlu membaca "Variabel & Tipe Data" sampai
habis hanya untuk boleh membuka materi decorator. Semua fungsi di sini
menerima `buka_semua`; nilai None (bawaannya) berarti "baca saklarnya
sendiri", sehingga pemanggil yang lupa tetap menghormati setelan pemakai.

Importir: main.py & layar/materials.py (terminal), webapp/api.py & webapp/isi.py
(web), tests/test_bab.py.
"""

from pelajar import progress
from data.bab import BAB

try:
    from pelajar import konfigurasi
except ImportError:                                    # pragma: no cover
    konfigurasi = None


TERKUNCI = "terkunci"
TERBUKA = "terbuka"
TUNTAS = "tuntas"

# Urutannya bermakna: dipakai untuk memeriksa bahwa tingkat sebuah bab tidak
# pernah MENURUN dari bab sebelumnya (dijaga tes).
TINGKAT = ("dasar", "menengah", "mahir")

LABEL_TINGKAT = {
    "dasar": "Dasar",
    "menengah": "Menengah",
    "mahir": "Mahir",
}

KETERANGAN_TINGKAT = {
    "dasar": "Bisa dikerjakan tanpa pengalaman apa pun sebelumnya.",
    "menengah": "Menggabungkan yang di bab dasar jadi program yang utuh.",
    "mahir": "Hal-hal yang muncul di kode orang lain dan bikin tersandung.",
}

# Aturannya dijelaskan ke pelajar dari beberapa layar sekaligus: daftar bab di
# terminal, hasil pencarian global, dan layar penolakan di web. Kalimatnya
# tinggal DI SINI, satu kali, bersama logika yang menegakkannya. Sebelumnya tiap
# layar menuliskannya dengan kata-katanya sendiri — logikanya memang tetap satu,
# tapi rumusannya bisa melenceng satu per satu tanpa satu tes pun gagal, dan
# yang dibaca pelajar jadi dua aturan berbeda tergantung dari pintu mana ia
# sampai.
KALIMAT_ATURAN = (
    "Sebuah bab terbuka begitu SELURUH materi bab sebelumnya dibaca sampai "
    "habis. Kuis dan latihan tidak ikut menentukan — satu latihan sulit yang "
    "belum ditaklukkan tidak boleh mengunci sisa kurikulum."
)

KALIMAT_PINTU_DARURAT = (
    "Kalau kamu sudah menguasainya, nyalakan \"Buka semua bab tanpa syarat\" "
    "di Pengaturan."
)


def _saklar_buka_semua():
    if konfigurasi is None:
        return False
    return bool(konfigurasi.ambil("buka_semua_bab", False))


def punya_bab(key):
    return key in BAB


def _bereskan(entri):
    """Satu entri BAB (dict) -> dict lengkap dengan bidang yang selalu ada."""
    return {
        "judul": entri["judul"],
        "ket": entri.get("ket", ""),
        "tingkat": entri.get("tingkat", "dasar"),
        "awal": entri["awal"],
        "akhir": entri["akhir"],
    }


def _satu_bab(jumlah_materi):
    return {"judul": "Semua materi", "ket": "", "tingkat": "dasar",
            "awal": 0, "akhir": jumlah_materi}


def _rentang(key, jumlah_materi):
    """Daftar bab sebuah bahasa, sudah dipastikan menutupi seluruh materi.

    Bahasa yang belum punya pembagian bab — atau yang pembagiannya tidak lagi
    cocok dengan jumlah materinya karena materi baru ditambahkan — jatuh ke
    satu bab berisi semuanya. Itu pilihan yang disengaja: kurikulum yang
    seluruhnya terbuka jauh lebih baik daripada kurikulum yang separuhnya
    hilang karena sebuah angka lupa diperbarui. Tes menjaga supaya jalur
    cadangan ini tidak pernah benar-benar terpakai di data yang dirilis.
    """
    daftar = BAB.get(key)
    if not daftar:
        return [_satu_bab(jumlah_materi)]

    tertutup = []
    for entri in daftar:
        tertutup.extend(range(entri["awal"], entri["akhir"]))
    if tertutup != list(range(jumlah_materi)):
        return [_satu_bab(jumlah_materi)]
    return [_bereskan(e) for e in daftar]


def status(lang, data=None, buka_semua=None):
    """Ringkasan tiap bab sebuah bahasa.

    @param lang        entri LANGUAGES
    @param data        progres; dibaca sendiri kalau tidak diberikan
    @param buka_semua  abaikan penguncian; None = ikuti setelan pemakai

    Return daftar dict: nomor, judul, ket, tingkat, awal, akhir, materi
    (indeks), selesai, jumlah, kurang, persen, status, dan `alasan` — satu
    kalimat yang menjelaskan APA yang harus dilakukan supaya bab ini terbuka.
    Kalimat itu ditulis di sini, bukan di antarmuka, supaya terminal dan web
    tidak pernah menjelaskan aturan yang sama dengan dua cara berbeda.
    """
    if data is None:
        data = progress.load_progress()
    if buka_semua is None:
        buka_semua = _saklar_buka_semua()

    dibaca = set(data.get("materi_dibaca") or [])
    kategori = f"{lang['key']}_materi"
    materi = lang["materials"]

    hasil = []
    boleh = True                  # bab pertama selalu terbuka
    sebelumnya = None
    for nomor, b in enumerate(_rentang(lang["key"], len(materi)), start=1):
        indeks = list(range(b["awal"], b["akhir"]))
        selesai = sum(
            1 for i in indeks
            if progress.kunci(kategori, materi[i]["title"]) in dibaca)
        jumlah = len(indeks)
        tuntas = jumlah > 0 and selesai == jumlah

        if buka_semua or boleh or selesai > 0:
            # `selesai > 0` = sudah pernah disentuh, jadi tidak pernah dikunci
            # lagi. Menutup kembali sesuatu yang sudah dibuka adalah cara
            # tercepat membuat orang mengira progresnya hilang.
            keadaan = TUNTAS if tuntas else TERBUKA
            alasan = ""
        else:
            keadaan = TERKUNCI
            alasan = _alasan(sebelumnya)

        hasil.append({
            "nomor": nomor,
            "judul": b["judul"],
            "ket": b["ket"],
            "tingkat": b["tingkat"],
            "label_tingkat": LABEL_TINGKAT.get(b["tingkat"], b["tingkat"]),
            "awal": b["awal"],
            "akhir": b["akhir"],
            "materi": indeks,
            "selesai": selesai,
            "jumlah": jumlah,
            "kurang": jumlah - selesai,
            "status": keadaan,
            "alasan": alasan,
            "persen": round(selesai / jumlah * 100) if jumlah else 0,
        })
        sebelumnya = hasil[-1]
        boleh = tuntas
    return hasil


def _alasan(sebelumnya):
    """Kalimat "kenapa terkunci" yang menyebut angka, bukan cuma melarang.

    "Terkunci" sendirian membuat orang menebak-nebak apa yang kurang. Yang
    dibutuhkan justru sisa pekerjaannya, dan sisa itu selalu bisa dihitung.
    """
    if sebelumnya is None:
        return ""
    kurang = sebelumnya["kurang"]
    judul = f"Bab {sebelumnya['nomor']} · {sebelumnya['judul']}"
    if kurang <= 0:
        return f"Selesaikan {judul} lebih dulu."
    if kurang == 1:
        return f"Tinggal 1 materi lagi di {judul}."
    return f"Baca {kurang} materi lagi di {judul}."


def bab_materi(lang, indeks, data=None, buka_semua=None):
    """Bab yang memuat materi ke-`indeks`, atau None kalau di luar jangkauan."""
    for b in status(lang, data, buka_semua):
        if b["awal"] <= indeks < b["akhir"]:
            return b
    return None


def terkunci(lang, indeks, data=None, buka_semua=None):
    """Apakah materi ke-`indeks` sedang terkunci."""
    b = bab_materi(lang, indeks, data, buka_semua)
    return bool(b and b["status"] == TERKUNCI)


def indeks_terbuka(lang, data=None, buka_semua=None):
    """Himpunan indeks materi yang boleh dibuka sekarang.

    Dipakai antarmuka untuk menyaring daftar tanpa memanggil `terkunci()`
    sekali per materi — tiap panggilan itu membaca ulang seluruh progres.
    """
    terbuka = set()
    for b in status(lang, data, buka_semua):
        if b["status"] != TERKUNCI:
            terbuka.update(b["materi"])
    return terbuka


def ringkas(lang, data=None, buka_semua=None):
    """(bab tuntas, jumlah bab, bab yang sedang dikerjakan atau None)."""
    daftar = status(lang, data, buka_semua)
    tuntas = sum(1 for b in daftar if b["status"] == TUNTAS)
    kini = next((b for b in daftar if b["status"] == TERBUKA), None)
    return tuntas, len(daftar), kini


def kalimat_ringkas(lang, data=None, buka_semua=None):
    """Satu kalimat status bab untuk ditaruh di kepala halaman bahasa."""
    tuntas, jumlah, kini = ringkas(lang, data, buka_semua)
    if jumlah <= 1:
        return ""
    if tuntas >= jumlah:
        return f"Semua {jumlah} bab tuntas."
    if kini is None:
        return f"{tuntas} dari {jumlah} bab tuntas."
    return (f"Bab {kini['nomor']} dari {jumlah}: {kini['judul']} "
            f"({kini['selesai']}/{kini['jumlah']} materi)")


def tingkat_materi(lang, indeks, data=None, buka_semua=None):
    """Tingkat ("dasar"/"menengah"/"mahir") materi ke-`indeks`."""
    b = bab_materi(lang, indeks, data, buka_semua)
    return b["tingkat"] if b else "dasar"
