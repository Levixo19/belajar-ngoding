"""Penyimpanan progres belajar, gamifikasi, bookmark, dan penjadwalan ulang kuis.

Semua data disimpan di satu file JSON di home directory user. Kegagalan baca/tulis
tidak boleh pernah menghentikan aplikasi -- progres itu bonus, bukan syarat.

Kontrak "tidak boleh pernah menghentikan aplikasi" itu dulu hanya berlaku untuk
JSON yang gagal DIURAI. File yang berhasil diurai tapi salah TIPE (mis. entri
kuis berupa angka, bukan objek) tetap menjatuhkan aplikasi dengan AttributeError
di setiap peluncuran -- dan pengguna tidak punya cara memperbaikinya dari dalam
aplikasi. Sekarang `_migrasi` memvalidasi tipe setiap field, bukan sekadar
keberadaannya.
"""

import json
import os
import re
import shutil
from datetime import date, datetime, timedelta

from pelajar import simpanan

VERSI_DATA = 4

PROGRESS_FILE = os.environ.get(
    "BELAJAR_PROGRESS_FILE",
    os.path.join(os.path.expanduser("~"), ".belajar_ngoding_progress.json"),
)

# File lama dari versi sebelum aplikasi mendukung banyak bahasa. Diturunkan dari
# lokasi file aktif, bukan dari home secara mutlak: kalau tidak, profil yang
# diarahkan lewat BELAJAR_PROGRESS_FILE akan diam-diam membaca progres lama
# milik profil lain yang kebetulan ada di home.
PROGRESS_FILE_LAMA = os.environ.get(
    "BELAJAR_PROGRESS_FILE_LAMA",
    os.path.join(os.path.dirname(PROGRESS_FILE) or ".", ".belajar_java_progress.json"),
)

XP_MATERI = 10
XP_LATIHAN_DILIHAT = 3
XP_LATIHAN_LULUS = 25
XP_LATIHAN_MANUAL = 8
XP_PER_JAWABAN_BENAR = 2
XP_BONUS_KUIS_SEMPURNA = 20
RIWAYAT_KUIS_MAKS = 12
XP_TEBAK_BENAR = 3


def _default():
    return {
        "versi": VERSI_DATA,
        "materi_dibaca": [],
        "materi_sebagian": [],
        "kuis_skor": {},
        "latihan_dilihat": [],
        "latihan_lulus": [],
        "latihan_manual": [],
        "bookmark": [],
        "salah_kuis": {},
        "jadwal_kuis": {},
        # Riwayat skor sesi PENUH per kuis: [[tanggal, benar, total], ...],
        # paling banyak RIWAYAT_KUIS_MAKS terbaru. Dulu cuma skor terbaik dan
        # terakhir yang disimpan, jadi "4/10 -> 9/10" (bukti ulangan berjadwal
        # bekerja) tidak bisa ditunjukkan ke pelajar.
        "kuis_riwayat": {},
        # Tebak keluaran per blok contoh (pelajar/tebak.py):
        # {"<key>_materi::<judul>#<bagian>": {benar, coba, terakhir, salah_terakhir}}
        "tebakan": {},
        "riwayat_harian": {},
        "terakhir": {},
        "xp": 0,
        "streak": {"tanggal_terakhir": "", "beruntun": 0, "terpanjang": 0, "total_hari": 0},
        "badge": [],
    }


def _salin(nilai):
    if isinstance(nilai, dict):
        return dict(nilai)
    if isinstance(nilai, list):
        return list(nilai)
    return nilai


def _migrasi(data):
    """Lengkapi field yang hilang, buang yang tipenya salah, naikkan versi.

    Prinsipnya: lebih baik kehilangan SATU field yang rusak daripada menolak
    seluruh file (atau meledak saat dipakai). Field yang tipenya tidak cocok
    diganti nilai bawaan; sisanya dipertahankan apa adanya.
    """
    default = _default()

    for key, val in default.items():
        if key == "versi":
            continue
        if key not in data or not isinstance(data[key], type(val)):
            data[key] = _salin(val)

    # Entri kuis wajib berupa dict; yang bukan dibuang, bukan ditebak isinya --
    # menebak lebih berbahaya daripada kehilangan satu skor.
    data["kuis_skor"] = {k: v for k, v in data["kuis_skor"].items() if isinstance(v, dict)}
    for info in data["kuis_skor"].values():
        info.setdefault("terbaik", 0)
        info.setdefault("percobaan", 0)
        info.setdefault("total_soal", 0)

    data["jadwal_kuis"] = {k: v for k, v in data["jadwal_kuis"].items() if isinstance(v, dict)}
    data["tebakan"] = {k: v for k, v in data["tebakan"].items() if isinstance(v, dict)}
    data["kuis_riwayat"] = {
        k: [e for e in v if isinstance(e, list) and len(e) == 3
            and isinstance(e[0], str) and isinstance(e[1], int) and isinstance(e[2], int)]
        for k, v in data["kuis_riwayat"].items() if isinstance(v, list)
    }
    data["salah_kuis"] = {
        k: [i for i in v if isinstance(i, int)]
        for k, v in data["salah_kuis"].items() if isinstance(v, list)
    }
    data["riwayat_harian"] = {
        k: v for k, v in data["riwayat_harian"].items() if isinstance(v, dict)
    }

    for key in ("materi_dibaca", "materi_sebagian", "latihan_dilihat",
                "latihan_lulus", "latihan_manual", "bookmark", "badge"):
        data[key] = [x for x in data[key] if isinstance(x, str)]

    for key in ("beruntun", "terpanjang", "total_hari"):
        if not isinstance(data["streak"].get(key), int):
            data["streak"][key] = 0
    if not isinstance(data["streak"].get("tanggal_terakhir"), str):
        data["streak"]["tanggal_terakhir"] = ""

    if not isinstance(data.get("xp"), int) or isinstance(data.get("xp"), bool) or data["xp"] < 0:
        data["xp"] = 0

    _normalkan_kunci(data)

    data["versi"] = VERSI_DATA
    return data


_BIDANG_DAFTAR_KUNCI = ("materi_dibaca", "materi_sebagian", "latihan_dilihat",
                        "latihan_lulus", "latihan_manual", "bookmark")
_BIDANG_PETA_KUNCI = ("kuis_skor", "jadwal_kuis", "salah_kuis", "kuis_riwayat")


def _normalkan_kunci(data):
    """Buang nomor urut dari kunci yang tersimpan (skema v3 -> v4).

    Dijalankan setiap kali progres dimuat, bukan sekali saat naik versi. Itu
    disengaja: berkas progres bisa datang dari mana saja — cadangan lama,
    impor dari komputer lain, berkas yang disunting tangan — dan satu kunci
    bergaya lama di antaranya berarti satu materi yang sudah dibaca tampil
    sebagai belum. Biayanya sepersekian milidetik; harganya sebuah pencapaian
    yang tidak bisa dikumpulkan ulang.

    Kalau kunci lama dan kunci baru bertabrakan (mustahil dalam data yang
    sah, tapi mungkin di berkas yang disunting tangan), yang menang adalah
    yang sudah ada — menggabungkan dua catatan lebih aman daripada memilih
    salah satu untuk dibuang.
    """
    for bidang in _BIDANG_DAFTAR_KUNCI:
        terlihat = set()
        baru = []
        for k in data.get(bidang) or []:
            n = _kunci_baru(k)
            if n not in terlihat:
                terlihat.add(n)
                baru.append(n)
        data[bidang] = baru

    for bidang in _BIDANG_PETA_KUNCI:
        peta = {}
        for k, v in (data.get(bidang) or {}).items():
            peta.setdefault(_kunci_baru(k), v)
        data[bidang] = peta
    return data


def _kunci_baru(k):
    if not isinstance(k, str) or "::" not in k:
        return k
    kategori, judul = k.split("::", 1)
    return f"{kategori}::{judul_kunci(judul)}"


def load_progress():
    """Muat progres. Aman kalau file belum ada, rusak, atau tidak bisa dibaca."""
    path = PROGRESS_FILE
    if not os.path.exists(path) and os.path.exists(PROGRESS_FILE_LAMA):
        path = PROGRESS_FILE_LAMA  # otomatis pindah dari file versi lama

    if not os.path.exists(path):
        return _default()
    # Berkas yang tidak bisa diurai dikarantina oleh `simpanan`, jadi data
    # bawaan di bawah tidak akan pernah menimpa progres yang cuma rusak satu
    # koma. Bentuk yang salah (bukan objek, atau migrasi gagal) diperlakukan
    # sama: pindahkan ke samping dulu, baru mulai dari kosong.
    data = simpanan.baca_json(path)
    if data is None:
        return _default()
    if not isinstance(data, dict):
        simpanan.karantina(path)
        return _default()
    try:
        return _migrasi(data)
    except (ValueError, TypeError, AttributeError, KeyError):
        simpanan.karantina(path)
        return _default()


def save_progress(data):
    """Tulis atomik dengan cadangan `.bak`; lihat pelajar/simpanan.py."""
    return simpanan.tulis_json(PROGRESS_FILE, data, awalan=".progress-")


# Judul materi membawa nomornya sendiri ("2. Variabel & Tipe Data"), dan nomor
# itu BERGESER setiap kali sebuah materi disisipkan di tengah kurikulum.
_AWALAN_NOMOR = re.compile(r"^\s*\d+\.\s*")


def judul_kunci(judul):
    """Judul tanpa nomor urutnya — identitas sebuah materi yang tidak berubah.

    Kenapa ini ada, dan kenapa ia penting justru saat tidak terjadi apa-apa:
    kunci progres dulu memuat judul UTUH, jadi menyisipkan satu materi baru di
    posisi kedua menggeser nomor dua puluh materi sesudahnya — dan setiap
    materi yang pernah dibaca seseorang mendadak tidak dikenali lagi. Yang
    terlihat pemakainya bukan "kurikulumnya bertambah" melainkan "progresku
    hilang", dan tidak ada cara mengembalikannya karena kunci lamanya sudah
    tidak menunjuk apa pun.

    Dengan nomornya dibuang, urutan jadi urusan TAMPILAN saja. Kurikulum boleh
    disusun ulang berapa kali pun tanpa menyentuh satu pun catatan pencapaian.
    Judul kuis dan latihan ("Kuis 1: ...", "Latihan 3: ...") tidak berbentuk
    "angka-titik" sehingga tidak tersentuh sama sekali.
    """
    return _AWALAN_NOMOR.sub("", judul or "").strip()


def kunci(kategori, judul):
    return f"{kategori}::{judul_kunci(judul)}"


# ---------------------------------------------------------------- streak & xp

def _hari_ini():
    return date.today().isoformat()


def _selisih_hari(dari, sampai):
    """Selisih hari antara dua tanggal ISO. None kalau salah satu tidak sah."""
    try:
        return (date.fromisoformat(sampai) - date.fromisoformat(dari)).days
    except (ValueError, TypeError):
        return None


def catat_aktivitas(data):
    """Perbarui streak harian. Dipanggil setiap kali user melakukan sesuatu."""
    streak = data.get("streak")
    if not isinstance(streak, dict):
        streak = _default()["streak"]
        data["streak"] = streak

    hari_ini = _hari_ini()
    terakhir = streak.get("tanggal_terakhir", "")
    if terakhir == hari_ini:
        return data

    selisih = _selisih_hari(terakhir, hari_ini) if terakhir else None
    streak["beruntun"] = streak.get("beruntun", 0) + 1 if selisih == 1 else 1
    streak["tanggal_terakhir"] = hari_ini
    streak["total_hari"] = streak.get("total_hari", 0) + 1
    streak["terpanjang"] = max(streak.get("terpanjang", 0), streak["beruntun"])
    return data


def streak_aktif(data):
    """Streak yang benar-benar masih hidup HARI INI.

    `streak["beruntun"]` hanya diperbarui saat ada aktivitas baru, jadi angka
    di file bisa jadi peninggalan bulan lalu. Dashboard harus memakai fungsi
    ini supaya tidak memamerkan streak 40 hari yang sudah lama putus.
    """
    streak = data.get("streak")
    if not isinstance(streak, dict):
        return 0
    terakhir = streak.get("tanggal_terakhir", "")
    if not terakhir:
        return 0
    selisih = _selisih_hari(terakhir, _hari_ini())
    if selisih is None or selisih < 0 or selisih > 1:
        return 0
    return streak.get("beruntun", 0)


def _catat_harian(data, bidang, jumlah=1):
    """Catat aktivitas hari ini untuk heatmap, target harian, dan badge."""
    riwayat = data.get("riwayat_harian")
    if not isinstance(riwayat, dict):
        riwayat = data["riwayat_harian"] = {}
    hari = riwayat.get(_hari_ini())
    if not isinstance(hari, dict):
        hari = riwayat[_hari_ini()] = {}
    hari[bidang] = hari.get(bidang, 0) + jumlah

    # Simpan setahun terakhir saja; heatmap tidak butuh lebih dan file progres
    # tidak boleh tumbuh selamanya.
    if len(riwayat) > 400:
        for tanggal in sorted(riwayat)[:-370]:
            riwayat.pop(tanggal, None)


def tambah_xp(data, jumlah):
    jumlah = max(0, jumlah)
    data["xp"] = data.get("xp", 0) + jumlah
    if jumlah:
        _catat_harian(data, "xp", jumlah)
    return data


def xp_hari_ini(data):
    hari = (data.get("riwayat_harian") or {}).get(_hari_ini(), {})
    return hari.get("xp", 0) if isinstance(hari, dict) else 0


def riwayat_harian(data, jumlah_hari=91):
    """[(tanggal_iso, xp)] untuk `jumlah_hari` terakhir, termasuk hari kosong."""
    riwayat = data.get("riwayat_harian") or {}
    hari_ini = date.today()
    keluar = []
    for mundur in range(jumlah_hari - 1, -1, -1):
        tanggal = (hari_ini - timedelta(days=mundur)).isoformat()
        isi = riwayat.get(tanggal) or {}
        keluar.append((tanggal, isi.get("xp", 0) if isinstance(isi, dict) else 0))
    return keluar


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


# --------------------------------------------------------------------- badge

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


def _hari_capai_target(data, target=60):
    riwayat = data.get("riwayat_harian") or {}
    return sum(1 for isi in riwayat.values()
               if isinstance(isi, dict) and isi.get("xp", 0) >= target)


def _kuis_sempurna(data):
    return sum(1 for i in data["kuis_skor"].values()
               if i.get("total_soal", 0) > 0
               and i.get("terbaik", 0) == i.get("total_soal", 0))


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
     lambda d: _kuis_sempurna(d) >= 1),
    ("sapu_bersih", "Sapu Bersih", "Dapat 100% di 5 kuis berbeda",
     lambda d: _kuis_sempurna(d) >= 5),
    ("tak_tergoyahkan", "Tak Tergoyahkan", "Dapat 100% di 20 kuis berbeda",
     lambda d: _kuis_sempurna(d) >= 20),
    ("tangan_kotor", "Tangan Kotor", "Lulus satu latihan dengan kode sendiri",
     lambda d: len(d["latihan_lulus"]) >= 1),
    ("rajin_ngoding", "Rajin Ngoding", "Lulus 10 latihan",
     lambda d: len(d["latihan_lulus"]) >= 10),
    ("mesin_koding", "Mesin Koding", "Lulus 30 latihan",
     lambda d: len(d["latihan_lulus"]) >= 30),
    ("pandai_besi", "Pandai Besi Kode", "Lulus 75 latihan",
     lambda d: len(d["latihan_lulus"]) >= 75),
    ("poliglot", "Poliglot", "Sentuh 3 bahasa berbeda",
     lambda d: len(_bahasa_tersentuh(d)) >= 3),
    ("poliglot_sejati", "Poliglot Sejati", "Sentuh 6 bahasa berbeda",
     lambda d: len(_bahasa_tersentuh(d)) >= 6),
    ("poliglot_lengkap", "Poliglot Lengkap", "Sentuh 8 kurikulum berbeda",
     lambda d: len(_bahasa_tersentuh(d)) >= 8),
    ("tiga_hari", "Konsisten", "Belajar 3 hari beruntun",
     lambda d: d["streak"].get("terpanjang", 0) >= 3),
    ("seminggu", "Seminggu Penuh", "Belajar 7 hari beruntun",
     lambda d: d["streak"].get("terpanjang", 0) >= 7),
    ("sebulan", "Sebulan Penuh", "Belajar 30 hari beruntun",
     lambda d: d["streak"].get("terpanjang", 0) >= 30),
    ("seratus_hari", "Seratus Hari", "Belajar total 100 hari",
     lambda d: d["streak"].get("total_hari", 0) >= 100),
    ("disiplin", "Disiplin", "Capai 60 XP di 7 hari berbeda",
     lambda d: _hari_capai_target(d) >= 7),
    ("sultan_xp", "Kolektor XP", "Kumpulkan 1.000 XP",
     lambda d: d.get("xp", 0) >= 1000),
    ("legenda_xp", "Legenda XP", "Kumpulkan 5.000 XP",
     lambda d: d.get("xp", 0) >= 5000),
    ("penanda", "Tukang Tandai", "Simpan 10 bookmark",
     lambda d: len(d["bookmark"]) >= 10),
]


def cek_badge_baru(data):
    """Return list badge yang baru saja terbuka, sekaligus simpan ke data."""
    dimiliki = data.get("badge")
    if not isinstance(dimiliki, list):
        dimiliki = data["badge"] = []
    sudah = set(dimiliki)
    baru = []
    for bid, nama, deskripsi, syarat in DAFTAR_BADGE:
        if bid in sudah:
            continue
        try:
            if syarat(data):
                dimiliki.append(bid)
                baru.append((bid, nama, deskripsi))
        except (KeyError, TypeError, AttributeError, ValueError):
            continue
    return baru


# ---------------------------------------------------------------- pencatatan

def _selesaikan(data):
    """Update streak, cek badge, simpan. Return list badge baru."""
    catat_aktivitas(data)
    baru = cek_badge_baru(data)
    save_progress(data)
    return baru


def _tandai_terakhir(data, tipe, kategori, judul):
    data["terakhir"] = {
        "tipe": tipe, "kategori": kategori, "judul": judul,
        "waktu": datetime.now().isoformat(timespec="seconds"),
    }


def record_material_read(kategori, judul, tuntas=True):
    """Catat materi dibaca.

    `tuntas=False` berarti pengguna berhenti di tengah: dicatat sebagai
    "dibaca sebagian" tanpa XP, supaya statistik tidak mengaku-aku sudah
    selesai padahal baru satu halaman.
    """
    data = load_progress()
    k = kunci(kategori, judul)

    if tuntas:
        if k not in data["materi_dibaca"]:
            data["materi_dibaca"].append(k)
            tambah_xp(data, XP_MATERI)
            _catat_harian(data, "materi")
        if k in data["materi_sebagian"]:
            data["materi_sebagian"].remove(k)
    elif k not in data["materi_dibaca"] and k not in data["materi_sebagian"]:
        data["materi_sebagian"].append(k)

    _tandai_terakhir(data, "materi", kategori, judul)
    return _selesaikan(data)


def record_exercise_viewed(kategori, judul):
    data = load_progress()
    k = kunci(kategori, judul)
    if k not in data["latihan_dilihat"]:
        data["latihan_dilihat"].append(k)
        tambah_xp(data, XP_LATIHAN_DILIHAT)
    _tandai_terakhir(data, "latihan", kategori, judul)
    return _selesaikan(data)


def record_exercise_passed(kategori, judul):
    data = load_progress()
    k = kunci(kategori, judul)
    if k not in data["latihan_lulus"]:
        data["latihan_lulus"].append(k)
        tambah_xp(data, XP_LATIHAN_LULUS)
        _catat_harian(data, "latihan")
    return _selesaikan(data)


def tandai_latihan_manual(kategori, judul):
    """Tandai latihan selesai tanpa penilaian otomatis.

    Sebagian latihan memang tidak bisa dinilai mesin (butuh pustaka luar, atau
    toolchain-nya tidak terpasang di komputer ini). Tanpa jalur ini, sampai 30%
    latihan mustahil berstatus lulus dan progress bar bahasa itu mentok
    selamanya -- termasuk untuk pelajar yang mengerjakan semuanya dengan benar.
    """
    data = load_progress()
    k = kunci(kategori, judul)
    if k in data["latihan_lulus"]:
        return []
    if k not in data["latihan_manual"]:
        data["latihan_manual"].append(k)
        tambah_xp(data, XP_LATIHAN_MANUAL)
        _catat_harian(data, "latihan")
    return _selesaikan(data)


def batalkan_latihan_manual(kategori, judul):
    data = load_progress()
    k = kunci(kategori, judul)
    if k in data["latihan_manual"]:
        data["latihan_manual"].remove(k)
        save_progress(data)
        return True
    return False


def _simpan_salah(data, k, salah_index):
    if salah_index is None:
        return
    if salah_index:
        data["salah_kuis"][k] = sorted(set(salah_index))
    else:
        data["salah_kuis"].pop(k, None)


def record_quiz_score(kategori, judul, benar, total, salah_index=None,
                      sesi_penuh=True):
    """Catat hasil satu sesi kuis.

    `sesi_penuh=False` dipakai mode "ulangi soal yang masih salah". Sesi
    seperti itu TIDAK boleh menyentuh metrik resmi: dulu ia menimpa
    `total_soal` dengan jumlah subset sehingga daftar kuis menampilkan
    "terbaik 8/2", memicu badge "Nilai Sempurna" palsu, memberi bonus XP yang
    bisa dipanen berulang kali, dan mendorong jadwal ulang kuis yang justru
    lemah sampai 120 hari ke depan.
    """
    data = load_progress()
    k = kunci(kategori, judul)

    if not sesi_penuh:
        _simpan_salah(data, k, salah_index)
        _tandai_terakhir(data, "kuis", kategori, judul)
        return _selesaikan(data)

    # Dibaca SEBELUM riwayat diubah: apakah sesi ini ulangan yang memang
    # sudah waktunya (atau percobaan pertama), dan berapa skor terbaik lama.
    jatuh_tempo = kuis_jatuh_tempo(data, kategori, judul) or k not in data["kuis_skor"]
    terbaik_lama = data["kuis_skor"].get(k, {}).get("terbaik", 0)
    riwayat = data["kuis_skor"].get(k, {"terbaik": 0, "percobaan": 0})
    riwayat["percobaan"] = riwayat.get("percobaan", 0) + 1
    riwayat["terbaik"] = max(riwayat.get("terbaik", 0), benar)
    # max(): penyebut tidak boleh menyusut, apa pun yang terjadi sebelumnya.
    riwayat["total_soal"] = max(riwayat.get("total_soal", 0), total)
    riwayat["terakhir_skor"] = benar
    riwayat["terakhir_waktu"] = datetime.now().isoformat(timespec="seconds")
    data["kuis_skor"][k] = riwayat

    # XP penuh hanya untuk percobaan pertama dan ulangan yang jatuh tempo.
    # Mengulang kuis yang jawabannya masih segar di kepala dulu memberi 252 XP
    # sehari (audit 2026-10-17); sekarang yang dihargai cuma PENINGKATAN di
    # atas skor terbaik lama, dan bonus sempurna cuma sekali per kuis.
    if jatuh_tempo:
        tambah_xp(data, benar * XP_PER_JAWABAN_BENAR)
    else:
        tambah_xp(data, max(0, benar - terbaik_lama) * XP_PER_JAWABAN_BENAR)
    if total > 0 and benar == total and (jatuh_tempo or terbaik_lama < total):
        tambah_xp(data, XP_BONUS_KUIS_SEMPURNA)
    _catat_harian(data, "kuis")

    _simpan_salah(data, k, salah_index)
    riwayat_skor = data["kuis_riwayat"].setdefault(k, [])
    riwayat_skor.append([date.today().isoformat(), benar, total])
    del riwayat_skor[:-RIWAYAT_KUIS_MAKS]
    _jadwalkan_ulang(data, k, benar, total, jatuh_tempo)
    _tandai_terakhir(data, "kuis", kategori, judul)
    return _selesaikan(data)


def record_tebakan(kunci_blok, benar):
    """Catat satu tebakan keluaran (pelajar/tebak.py). Bukan latihan, bukan lulus.

    XP cuma untuk tebakan BENAR PERTAMA tiap blok: menebak ulang contoh yang
    keluarannya baru saja dilihat bukan membaca kode, dan tidak boleh jadi
    tambang XP (pelajaran dari jadwal kuis yang dulu bisa digeber).
    """
    data = load_progress()
    info = data["tebakan"].setdefault(kunci_blok, {"benar": 0, "coba": 0})
    pertama_benar = benar and not info.get("benar")
    info["coba"] = info.get("coba", 0) + 1
    info["benar"] = info.get("benar", 0) + (1 if benar else 0)
    info["salah_terakhir"] = not benar
    info["terakhir"] = date.today().isoformat()
    if pertama_benar:
        tambah_xp(data, XP_TEBAK_BENAR)
    return _selesaikan(data)


def perbarui_soal_salah(kategori, judul, salah_index):
    """Perbarui daftar soal yang masih salah, tanpa menyentuh skor apa pun."""
    return record_quiz_score(kategori, judul, 0, 0, salah_index, sesi_penuh=False)


def soal_salah_terakhir(kategori, judul):
    data = load_progress()
    return data["salah_kuis"].get(kunci(kategori, judul), [])


# ---------------------------------------------------- spaced repetition ringan

def _jadwalkan_ulang(data, k, benar, total, jatuh_tempo=True):
    """SM-2 versi sederhana: makin bagus skornya, makin jauh jadwal ulangnya.

    Dua aturan yang dulu dilanggar (audit 2026-10-17):

    * MONOTON. Pada percobaan pertama 7/8 dulu memberi jeda int(1*1.6)=1
      hari sementara 4/8 memberi 2: yang lebih lemah diulang lebih lambat.
      Sekarang tiap tingkat punya lantai yang lebih tinggi dari tingkat di
      bawahnya.
    * JEDA HANYA TUMBUH KALAU MEMANG SUDAH WAKTUNYA. Mengulang kuis yang sama
      tujuh kali sehari dulu mendorong jedanya sampai 120 hari, padahal
      jawabannya baru saja dilihat. Ulangan sebelum jatuh tempo yang bagus
      tidak menggeser jadwal; yang jelek tetap memendekkannya, karena
      lupa adalah informasi.
    """
    jadwal = data["jadwal_kuis"].get(k, {"interval": 1})
    rasio = (benar / total) if total else 0
    lama = max(1, int(jadwal.get("interval", 1) or 1))

    if rasio >= 0.9:
        interval = max(4, int(lama * 2.5))
    elif rasio >= 0.7:
        interval = max(3, int(lama * 1.6))
    elif rasio >= 0.5:
        interval = 2
    else:
        interval = 1

    if not jatuh_tempo and rasio >= 0.7 and jadwal.get("jatuh_tempo"):
        return  # ulangan dini yang bagus: jadwal lama tetap berlaku

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
    except (ValueError, TypeError):
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
    cek_badge_baru(data)
    save_progress(data)
    return hasil


def is_bookmarked(kategori, judul):
    return kunci(kategori, judul) in load_progress()["bookmark"]


def daftar_bookmark():
    return list(load_progress()["bookmark"])


def bersihkan_bookmark(kunci_valid):
    """Buang bookmark yang menunjuk materi yang sudah tidak ada. Return jumlahnya."""
    data = load_progress()
    sebelum = len(data["bookmark"])
    data["bookmark"] = [k for k in data["bookmark"] if k in kunci_valid]
    dibuang = sebelum - len(data["bookmark"])
    if dibuang:
        save_progress(data)
    return dibuang


# ------------------------------------------------------------------ statistik

# Kuis dihitung SELESAI kalau skor terbaiknya mencapai ambang ini. Dulu cukup
# "pernah dikerjakan": Java 3/3 kuis "selesai" dengan skor 23%, dan angka itu
# ikut menaikkan persen bahasa dan kesiapan Peta Karier. Diputuskan pemilik
# 2026-10-17. Ini SATU-SATUNYA definisi; terminal, web, dan karier membacanya
# lewat statistik_bahasa / kuis_lulus.
AMBANG_KUIS_LULUS = 0.7


def kuis_lulus(info, jumlah_soal=0):
    """True kalau satu entri kuis_skor sudah mencapai AMBANG_KUIS_LULUS.

    Entri lama (migrasi skema v1) kadang tidak punya penyebut sama sekali;
    tanpa jumlah soal, kita tidak bisa menghitung rasio, dan menghukum
    pelajar karena data lama yang tidak lengkap bukan pilihan yang adil.
    """
    if not info:
        return False
    maks = info.get("total_soal", 0) or jumlah_soal
    if not maks:
        return True
    return min(info.get("terbaik", 0), maks) / maks >= AMBANG_KUIS_LULUS


def statistik_bahasa(data, prefix, total_materi, total_kuis, total_latihan,
                     soal_per_kuis=None, latihan_tak_dinilai=0):
    """Ringkasan progres satu bahasa.

    `soal_per_kuis` (opsional) memetakan judul kuis -> jumlah soalnya. Tanpa
    itu, progres hasil migrasi skema v1 menyumbang skor tanpa penyebut sehingga
    persentase gabungan bisa melompat di atas 100%.
    """
    awalan_materi = f"{prefix}_materi::"
    awalan_kuis = f"{prefix}_kuis::"
    awalan_latihan = f"{prefix}_latihan::"

    materi = sum(1 for k in data["materi_dibaca"] if k.startswith(awalan_materi))
    sebagian = sum(1 for k in data["materi_sebagian"] if k.startswith(awalan_materi))
    dikerjakan = sum(1 for k in data["kuis_skor"] if k.startswith(awalan_kuis))
    kuis = sum(
        1 for k, info in data["kuis_skor"].items()
        if k.startswith(awalan_kuis) and kuis_lulus(
            info, (soal_per_kuis or {}).get(judul_kunci(k.split("::", 1)[1]), 0)))
    lulus = sum(1 for k in data["latihan_lulus"] if k.startswith(awalan_latihan))
    manual = sum(1 for k in data["latihan_manual"]
                 if k.startswith(awalan_latihan) and k not in data["latihan_lulus"])
    dilihat = sum(1 for k in data["latihan_dilihat"] if k.startswith(awalan_latihan))

    skor = 0
    maks = 0
    for k, info in data["kuis_skor"].items():
        if not k.startswith(awalan_kuis):
            continue
        skor += info.get("terbaik", 0)
        jumlah_soal = info.get("total_soal", 0)
        if not jumlah_soal and soal_per_kuis:
            jumlah_soal = soal_per_kuis.get(judul_kunci(k.split("::", 1)[1]), 0)
        maks += jumlah_soal
    if maks:
        skor = min(skor, maks)

    selesai = materi + kuis + lulus + manual
    target = total_materi + total_kuis + total_latihan
    return {
        "materi": materi, "materi_sebagian": sebagian, "total_materi": total_materi,
        "kuis": kuis, "kuis_dikerjakan": dikerjakan, "total_kuis": total_kuis,
        "latihan_lulus": lulus, "latihan_manual": manual,
        "latihan_dilihat": dilihat, "total_latihan": total_latihan,
        "latihan_tak_dinilai": latihan_tak_dinilai,
        "skor": skor, "skor_maks": maks,
        "persen": (min(selesai, target) / target * 100) if target else 0.0,
    }


# ------------------------------------------------------ ekspor / impor / reset

def ekspor(tujuan):
    """Salin progres ke `tujuan`. Return (berhasil, pesan/path)."""
    data = load_progress()
    try:
        tujuan = os.path.expanduser(tujuan)
        folder = os.path.dirname(tujuan)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(tujuan, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True, tujuan
    except OSError as e:
        return False, str(e)


def cadangkan():
    """Simpan salinan progres saat ini di sebelah berkas aslinya."""
    if not os.path.exists(PROGRESS_FILE):
        return ""
    tujuan = PROGRESS_FILE + ".bak"
    try:
        shutil.copy2(PROGRESS_FILE, tujuan)
        return tujuan
    except OSError:
        return ""


def impor(asal):
    """Ganti progres dengan isi `asal`, setelah mencadangkan. Return (ok, pesan)."""
    asal = os.path.expanduser(asal)
    if not os.path.exists(asal):
        return False, "berkas tidak ditemukan"
    try:
        with open(asal, "r", encoding="utf-8") as f:
            masuk = json.load(f)
        if not isinstance(masuk, dict):
            return False, "isi berkas bukan data progres"
    except (OSError, json.JSONDecodeError, ValueError) as e:
        return False, str(e)

    cadangan = cadangkan()
    if not save_progress(_migrasi(masuk)):
        return False, "gagal menulis progres"
    return True, cadangan or "tanpa cadangan"


def reset(bagian="semua"):
    """Kosongkan progres. `bagian` = 'semua' atau prefix bahasa (mis. 'java')."""
    cadangan = cadangkan()
    if bagian == "semua":
        save_progress(_default())
        return cadangan

    data = load_progress()
    for daftar in ("materi_dibaca", "materi_sebagian", "latihan_dilihat",
                   "latihan_lulus", "latihan_manual", "bookmark"):
        data[daftar] = [k for k in data[daftar] if not k.startswith(f"{bagian}_")]
    for peta in ("kuis_skor", "salah_kuis", "jadwal_kuis", "kuis_riwayat"):
        data[peta] = {k: v for k, v in data[peta].items()
                      if not k.startswith(f"{bagian}_")}
    if (data.get("terakhir") or {}).get("kategori", "").startswith(f"{bagian}_"):
        data["terakhir"] = {}
    save_progress(data)
    return cadangan
