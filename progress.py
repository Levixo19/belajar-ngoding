"""Penyimpanan progres belajar, gamifikasi, bookmark, dan penjadwalan ulang kuis.

Semua data disimpan di satu file JSON di home directory user. Kegagalan baca/tulis
tidak boleh pernah menghentikan aplikasi -- progres itu bonus, bukan syarat.
"""

import json
import os
import tempfile
from datetime import date, datetime, timedelta

VERSI_DATA = 2

PROGRESS_FILE = os.environ.get(
    "BELAJAR_PROGRESS_FILE",
    os.path.join(os.path.expanduser("~"), ".belajar_ngoding_progress.json"),
)

# File lama dari versi sebelum aplikasi mendukung banyak bahasa.
PROGRESS_FILE_LAMA = os.path.join(os.path.expanduser("~"), ".belajar_java_progress.json")

XP_MATERI = 10
XP_LATIHAN_DILIHAT = 3
XP_LATIHAN_LULUS = 25
XP_PER_JAWABAN_BENAR = 2
XP_BONUS_KUIS_SEMPURNA = 20


def _default():
    return {
        "versi": VERSI_DATA,
        "materi_dibaca": [],
        "kuis_skor": {},
        "latihan_dilihat": [],
        "latihan_lulus": [],
        "bookmark": [],
        "salah_kuis": {},
        "jadwal_kuis": {},
        "terakhir": {},
        "xp": 0,
        "streak": {"tanggal_terakhir": "", "beruntun": 0, "terpanjang": 0, "total_hari": 0},
        "badge": [],
    }


def _migrasi(data):
    """Lengkapi field yang hilang dan naikkan versi skema tanpa membuang data lama."""
    default = _default()
    for key, val in default.items():
        if key not in data:
            data[key] = val() if callable(val) else val
    # v1 tidak punya "total_soal" di sebagian entri kuis.
    for info in data["kuis_skor"].values():
        info.setdefault("terbaik", 0)
        info.setdefault("percobaan", 0)
        info.setdefault("total_soal", 0)
    data["versi"] = VERSI_DATA
    return data


def load_progress():
    """Muat progres. Aman kalau file belum ada, rusak, atau tidak bisa dibaca."""
    path = PROGRESS_FILE
    if not os.path.exists(path) and os.path.exists(PROGRESS_FILE_LAMA):
        path = PROGRESS_FILE_LAMA  # otomatis pindah dari file versi lama

    if not os.path.exists(path):
        return _default()
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            return _default()
        return _migrasi(data)
    except (json.JSONDecodeError, OSError, ValueError):
        return _default()


def save_progress(data):
    """Tulis atomik supaya file tidak korup kalau aplikasi mati di tengah proses."""
    try:
        folder = os.path.dirname(PROGRESS_FILE) or "."
        os.makedirs(folder, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=folder, prefix=".progress-", suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        os.replace(tmp, PROGRESS_FILE)
    except OSError:
        pass


def kunci(kategori, judul):
    return f"{kategori}::{judul}"


# ---------------------------------------------------------------- streak & xp

def _hari_ini():
    return date.today().isoformat()


def catat_aktivitas(data):
    """Perbarui streak harian. Dipanggil setiap kali user melakukan sesuatu."""
    streak = data["streak"]
    hari_ini = _hari_ini()
    terakhir = streak.get("tanggal_terakhir", "")

    if terakhir == hari_ini:
        return data

    if terakhir:
        try:
            selisih = (date.fromisoformat(hari_ini) - date.fromisoformat(terakhir)).days
        except ValueError:
            selisih = 999
    else:
        selisih = 999

    streak["beruntun"] = streak.get("beruntun", 0) + 1 if selisih == 1 else 1
    streak["tanggal_terakhir"] = hari_ini
    streak["total_hari"] = streak.get("total_hari", 0) + 1
    streak["terpanjang"] = max(streak.get("terpanjang", 0), streak["beruntun"])
    return data


def tambah_xp(data, jumlah):
    data["xp"] = data.get("xp", 0) + max(0, jumlah)
    return data


# Ambang XP tiap level. Naik makin lambat supaya level tinggi terasa berharga.
def xp_untuk_level(level):
    return int(50 * (level - 1) ** 1.6)


def level_dari_xp(xp):
    level = 1
    while xp >= xp_untuk_level(level + 1):
        level += 1
        if level > 200:
            break
    return level


def info_level(xp):
    """Return (level, xp_di_level_ini, xp_dibutuhkan_untuk_naik)."""
    level = level_dari_xp(xp)
    dasar = xp_untuk_level(level)
    berikut = xp_untuk_level(level + 1)
    return level, xp - dasar, max(1, berikut - dasar)


GELAR = [
    (1, "Pemula"),
    (3, "Penjelajah"),
    (6, "Perakit Kode"),
    (10, "Pengrajin"),
    (15, "Insinyur"),
    (21, "Arsitek"),
    (30, "Mahaguru"),
]


def gelar_dari_level(level):
    nama = GELAR[0][1]
    for minimal, judul in GELAR:
        if level >= minimal:
            nama = judul
    return nama


# ------------------------------------------------------------------- badge

# (id, nama, deskripsi, fungsi pengecek)
DAFTAR_BADGE = [
    ("langkah_pertama", "Langkah Pertama", "Baca materi pertamamu",
     lambda d: len(d["materi_dibaca"]) >= 1),
    ("kutu_buku", "Kutu Buku", "Baca 25 materi",
     lambda d: len(d["materi_dibaca"]) >= 25),
    ("perpustakaan", "Perpustakaan Berjalan", "Baca 100 materi",
     lambda d: len(d["materi_dibaca"]) >= 100),
    ("kuis_perdana", "Kuis Perdana", "Selesaikan satu kuis",
     lambda d: len(d["kuis_skor"]) >= 1),
    ("nilai_sempurna", "Nilai Sempurna", "Dapat 100% di satu kuis",
     lambda d: any(i.get("terbaik", 0) == i.get("total_soal", 0) and i.get("total_soal", 0) > 0
                   for i in d["kuis_skor"].values())),
    ("sapu_bersih", "Sapu Bersih", "Dapat 100% di 5 kuis berbeda",
     lambda d: sum(1 for i in d["kuis_skor"].values()
                   if i.get("terbaik", 0) == i.get("total_soal", 0) and i.get("total_soal", 0) > 0) >= 5),
    ("tangan_kotor", "Tangan Kotor", "Lulus satu latihan dengan kode sendiri",
     lambda d: len(d["latihan_lulus"]) >= 1),
    ("rajin_ngoding", "Rajin Ngoding", "Lulus 10 latihan",
     lambda d: len(d["latihan_lulus"]) >= 10),
    ("mesin_koding", "Mesin Koding", "Lulus 30 latihan",
     lambda d: len(d["latihan_lulus"]) >= 30),
    ("poliglot", "Poliglot", "Sentuh 3 bahasa berbeda",
     lambda d: len(_bahasa_tersentuh(d)) >= 3),
    ("poliglot_sejati", "Poliglot Sejati", "Sentuh 6 bahasa berbeda",
     lambda d: len(_bahasa_tersentuh(d)) >= 6),
    ("tiga_hari", "Konsisten", "Belajar 3 hari beruntun",
     lambda d: d["streak"].get("terpanjang", 0) >= 3),
    ("seminggu", "Seminggu Penuh", "Belajar 7 hari beruntun",
     lambda d: d["streak"].get("terpanjang", 0) >= 7),
    ("sebulan", "Sebulan Penuh", "Belajar 30 hari beruntun",
     lambda d: d["streak"].get("terpanjang", 0) >= 30),
]


def _bahasa_tersentuh(data):
    bahasa = set()
    semua = (
        list(data["materi_dibaca"])
        + list(data["kuis_skor"].keys())
        + list(data["latihan_dilihat"])
        + list(data["latihan_lulus"])
    )
    for k in semua:
        prefix = k.split("::", 1)[0]
        if "_" in prefix:
            bahasa.add(prefix.rsplit("_", 1)[0])
    return bahasa


def cek_badge_baru(data):
    """Return list badge yang baru saja terbuka, sekaligus simpan ke data."""
    dimiliki = set(data.get("badge", []))
    baru = []
    for bid, nama, deskripsi, syarat in DAFTAR_BADGE:
        if bid in dimiliki:
            continue
        try:
            if syarat(data):
                data.setdefault("badge", []).append(bid)
                baru.append((bid, nama, deskripsi))
        except (KeyError, TypeError):
            continue
    return baru


# -------------------------------------------------------------- pencatatan

def _selesaikan(data):
    """Update streak, cek badge, simpan. Return list badge baru."""
    catat_aktivitas(data)
    baru = cek_badge_baru(data)
    save_progress(data)
    return baru


def record_material_read(kategori, judul):
    data = load_progress()
    k = kunci(kategori, judul)
    if k not in data["materi_dibaca"]:
        data["materi_dibaca"].append(k)
        tambah_xp(data, XP_MATERI)
    data["terakhir"] = {"tipe": "materi", "kategori": kategori, "judul": judul,
                        "waktu": datetime.now().isoformat(timespec="seconds")}
    return _selesaikan(data)


def record_exercise_viewed(kategori, judul):
    data = load_progress()
    k = kunci(kategori, judul)
    if k not in data["latihan_dilihat"]:
        data["latihan_dilihat"].append(k)
        tambah_xp(data, XP_LATIHAN_DILIHAT)
    data["terakhir"] = {"tipe": "latihan", "kategori": kategori, "judul": judul,
                        "waktu": datetime.now().isoformat(timespec="seconds")}
    return _selesaikan(data)


def record_exercise_passed(kategori, judul):
    data = load_progress()
    k = kunci(kategori, judul)
    if k not in data["latihan_lulus"]:
        data["latihan_lulus"].append(k)
        tambah_xp(data, XP_LATIHAN_LULUS)
    return _selesaikan(data)


def record_quiz_score(kategori, judul, benar, total, salah_index=None):
    data = load_progress()
    k = kunci(kategori, judul)
    riwayat = data["kuis_skor"].get(k, {"terbaik": 0, "percobaan": 0})
    riwayat["percobaan"] = riwayat.get("percobaan", 0) + 1
    riwayat["terbaik"] = max(riwayat.get("terbaik", 0), benar)
    riwayat["total_soal"] = total
    riwayat["terakhir_skor"] = benar
    riwayat["terakhir_waktu"] = datetime.now().isoformat(timespec="seconds")
    data["kuis_skor"][k] = riwayat

    tambah_xp(data, benar * XP_PER_JAWABAN_BENAR)
    if total > 0 and benar == total:
        tambah_xp(data, XP_BONUS_KUIS_SEMPURNA)

    if salah_index is not None:
        if salah_index:
            data["salah_kuis"][k] = sorted(set(salah_index))
        else:
            data["salah_kuis"].pop(k, None)

    _jadwalkan_ulang(data, k, benar, total)
    data["terakhir"] = {"tipe": "kuis", "kategori": kategori, "judul": judul,
                        "waktu": datetime.now().isoformat(timespec="seconds")}
    return _selesaikan(data)


def soal_salah_terakhir(kategori, judul):
    data = load_progress()
    return data["salah_kuis"].get(kunci(kategori, judul), [])


# --------------------------------------------------- spaced repetition ringan

def _jadwalkan_ulang(data, k, benar, total):
    """SM-2 versi sederhana: makin bagus skornya, makin jauh jadwal ulangnya."""
    jadwal = data["jadwal_kuis"].get(k, {"interval": 1})
    rasio = (benar / total) if total else 0

    if rasio >= 0.9:
        interval = max(1, int(jadwal.get("interval", 1) * 2.5))
    elif rasio >= 0.7:
        interval = max(1, int(jadwal.get("interval", 1) * 1.6))
    elif rasio >= 0.5:
        interval = 2
    else:
        interval = 1

    interval = min(interval, 120)
    data["jadwal_kuis"][k] = {
        "interval": interval,
        "jatuh_tempo": (date.today() + timedelta(days=interval)).isoformat(),
    }


def kuis_jatuh_tempo(data, kategori, judul):
    """True kalau kuis ini sudah waktunya diulang (atau belum pernah dikerjakan)."""
    k = kunci(kategori, judul)
    if k not in data["kuis_skor"]:
        return False  # belum pernah dikerjakan -> bukan "ulangan", tapi materi baru
    jadwal = data["jadwal_kuis"].get(k)
    if not jadwal or not jadwal.get("jatuh_tempo"):
        return True
    try:
        return date.fromisoformat(jadwal["jatuh_tempo"]) <= date.today()
    except ValueError:
        return True


# ------------------------------------------------------------------ bookmark

def toggle_bookmark(kategori, judul):
    """Return True kalau baru ditambahkan, False kalau dihapus."""
    data = load_progress()
    k = kunci(kategori, judul)
    if k in data["bookmark"]:
        data["bookmark"].remove(k)
        hasil = False
    else:
        data["bookmark"].append(k)
        hasil = True
    save_progress(data)
    return hasil


def is_bookmarked(kategori, judul):
    return kunci(kategori, judul) in load_progress()["bookmark"]


def daftar_bookmark():
    return list(load_progress()["bookmark"])


# ------------------------------------------------------------------ statistik

def statistik_bahasa(data, prefix, total_materi, total_kuis, total_latihan):
    materi = sum(1 for k in data["materi_dibaca"] if k.startswith(f"{prefix}_materi::"))
    kuis = sum(1 for k in data["kuis_skor"] if k.startswith(f"{prefix}_kuis::"))
    lulus = sum(1 for k in data["latihan_lulus"] if k.startswith(f"{prefix}_latihan::"))
    dilihat = sum(1 for k in data["latihan_dilihat"] if k.startswith(f"{prefix}_latihan::"))

    skor = 0
    maks = 0
    for k, info in data["kuis_skor"].items():
        if k.startswith(f"{prefix}_kuis::"):
            skor += info.get("terbaik", 0)
            maks += info.get("total_soal", 0)

    selesai = materi + kuis + lulus
    target = total_materi + total_kuis + total_latihan
    return {
        "materi": materi, "total_materi": total_materi,
        "kuis": kuis, "total_kuis": total_kuis,
        "latihan_lulus": lulus, "latihan_dilihat": dilihat, "total_latihan": total_latihan,
        "skor": skor, "skor_maks": maks,
        "persen": (selesai / target * 100) if target else 0.0,
    }
