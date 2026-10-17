"""Seluruh endpoint JSON antarmuka web.

Aturan yang dipegang berkas ini: **jangan pernah menghitung ulang apa yang
sudah dihitung modul lain.** Kelulusan latihan ditentukan `runner.periksa`,
kunci jawabannya oleh `exercises.bangun_tests`, XP dan badge oleh
`progress.record_*`, diagnosis diff oleh `beda`, terjemahan error oleh `galat`,
rekomendasi oleh `saran`. Yang ditambahkan di sini cuma bentuk keluarannya.

Kalau aturan itu dilanggar, akan ada dua definisi "lulus" di satu aplikasi --
satu di terminal, satu di web -- dan cepat atau lambat keduanya berbeda
pendapat tentang latihan yang sama.

Dua hal khas web yang memang harus ditangani di sini:

* **Penulisan progres diserialkan.** `progress` melakukan baca-ubah-tulis atas
  satu berkas JSON. Server ini melayani beberapa permintaan sekaligus (browser
  membuka banyak koneksi paralel), jadi dua permintaan yang bersamaan bisa
  saling menimpa dan menghapus XP yang baru saja dicatat. Semua mutasi lewat
  `_KUNCI_PROGRES`.

* **Kunci jawaban dipanaskan lebih dulu.** `bangun_tests` menurunkan ekspektasi
  dengan MENJALANKAN solusi contoh -- untuk Java itu kompilasi penuh, belasan
  detik. Di terminal jeda itu muncul setelah pelajar menekan "periksa". Di web
  kita tahu lebih awal: begitu halaman latihan dibuka, pemanasan dimulai di
  thread latar, sehingga saat tombolnya ditekan hasilnya biasanya sudah ada di
  cache milik `exercises`.

Importir: webapp/server.py.
"""

import os
import threading
import time

from pelajar import bab as modul_bab
from inti import beda
from inti import berkas as modul_berkas
from layar import exercises
from inti import galat as modul_galat
from inti import pustaka as modul_pustaka
from pelajar import konfigurasi
from pelajar import kuis_materi
from pelajar import simpanan
from pelajar import waktu
from pelajar import karier as modul_karier
import main as aplikasi
from pelajar import progress
from inti import runner
from pelajar import saran as modul_saran
from pelajar.progress import kunci as kunci_progres

from webapp import VERSI_WEB
from webapp import catatan as modul_catatan
from webapp import isi, sesi

LANGUAGES = aplikasi.LANGUAGES

# Semua baca-ubah-tulis progres lewat kunci ini. Lihat docstring modul.
_KUNCI_PROGRES = threading.RLock()

# Latihan yang kunci jawabannya sedang dipanaskan, supaya membuka halaman yang
# sama dua kali tidak menjalankan solusi contoh dua kali.
_SEDANG_HANGAT = set()
_KUNCI_HANGAT = threading.Lock()


class Galat(Exception):
    """Kesalahan yang boleh ditampilkan apa adanya ke pengguna."""

    def __init__(self, pesan, kode=400):
        super().__init__(pesan)
        self.pesan = pesan
        self.kode = kode


# ------------------------------------------------------------------ bantuan

def _bahasa(key):
    lang = next((l for l in LANGUAGES if l["key"] == key), None)
    if lang is None:
        raise Galat(f"Bahasa '{key}' tidak dikenal.", 404)
    return lang


def _ambil(daftar, indeks, apa):
    try:
        indeks = int(indeks)
    except (TypeError, ValueError):
        raise Galat(f"Nomor {apa} tidak sah.", 400)
    if not 0 <= indeks < len(daftar):
        raise Galat(f"{apa.capitalize()} nomor {indeks} tidak ada.", 404)
    return indeks, daftar[indeks]


def _stat(lang, data):
    """Statistik satu bahasa.

    Sengaja memanggil helper `main` alih-alih menyalinnya: di dalamnya ada
    aturan "latihan yang toolchain-nya belum terpasang dihitung tak-dinilai",
    dan dua salinan aturan itu pasti akan berbeda suatu hari nanti.
    """
    return aplikasi._stat(lang, data)


def _xp_dan_badge(sebelum, badge_baru):
    """Bungkus perubahan yang layak dirayakan di antarmuka."""
    sesudah = progress.load_progress()
    level_lama, _, _ = progress.info_level(sebelum.get("xp", 0))
    level_baru, di_level, butuh = progress.info_level(sesudah.get("xp", 0))
    return {
        "xp_tambah": sesudah.get("xp", 0) - sebelum.get("xp", 0),
        "xp": sesudah.get("xp", 0),
        "level": level_baru,
        "naik_level": level_baru > level_lama,
        "gelar": progress.gelar_dari_level(level_baru),
        # Gelar cuma berganti di beberapa ambang; layar naik level menyorotnya
        # hanya saat memang berganti, bukan di setiap level.
        "gelar_baru": (level_baru > level_lama and progress.gelar_dari_level(level_baru)
                       != progress.gelar_dari_level(level_lama)),
        "di_level": di_level,
        "butuh_level": butuh,
        "badge": [{"id": b, "nama": n, "deskripsi": d}
                  for b, n, d in (badge_baru or [])],
        "streak": progress.streak_aktif(sesudah),
        "xp_hari_ini": progress.xp_hari_ini(sesudah),
        "target_harian": konfigurasi.ambil("target_xp_harian", 60),
        # Layar jangan merayakan XP yang tidak pernah sampai ke disk.
        "simpan_gagal": progress.PROGRESS_FILE in simpanan.GAGAL,
    }


def _path_kerja(kategori, ex, bahasa, buat_folder=False):
    """Lokasi berkas jawaban pelajar -- PERSIS sama dengan yang dipakai terminal.

    Dibangun dari `exercises.DIR_KERJA` + `exercises.nama_kerja` supaya kode
    yang ditulis di web bisa dibuka di editor, dijalankan dari terminal, dan
    diperiksa lagi lewat aplikasi terminal tanpa disalin ke mana-mana.
    """
    folder = os.path.join(exercises.DIR_KERJA, kategori)
    if buat_folder:
        os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, exercises.nama_kerja(ex, bahasa))


def _baca_kerja(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


# --------------------------------------------------------------- pembungkus

def _beda_json(b):
    """`beda.Beda` -> JSON, lengkap dengan penanda spasi yang tak terlihat."""
    baris = []
    for tanda, bh, ba in b.baris:
        # Dua baris yang cuma beda spasi tidak akan pernah ditemukan mata
        # telanjang. Penandanya dihitung di sini, karakternya diambil dari
        # `beda` supaya web dan terminal memakai lambang yang sama.
        tampak = (bh is not None and ba is not None
                  and "".join(bh.split()) == "".join(ba.split()))
        baris.append({
            "tanda": tanda,
            "harapan": beda.tampakkan(bh) if (tampak and bh is not None) else bh,
            "aktual": beda.tampakkan(ba) if (tampak and ba is not None) else ba,
            "tampak": tampak,
        })
    return {
        "sama": b.sama,
        "baris": baris,
        "nomor_beda": b.nomor_beda,
        "kolom_beda": b.kolom_beda,
        "catatan": list(b.catatan),
        "ringkas": beda.ringkas(b),
    }


def _galat_json(teks, ex, bahasa):
    """Pesan error mentah -> {mentah, baris, artinya}."""
    if not teks or not teks.strip():
        return None
    rapi = modul_galat.rapikan(teks, exercises.nama_kerja(ex, bahasa),
                               exercises.baris_setup(ex))
    return {
        "mentah": rapi,
        "baris": modul_galat.ringkas(rapi, maks_baris=14),
        "artinya": modul_galat.terjemahkan(rapi),
    }


def _uji_json(h, ex, bahasa):
    keluar = {
        "nama": h.nama,
        "lulus": h.lulus,
        "harapan": h.harapan,
        "aktual": h.aktual,
        "mode": h.mode,
        "stdin": h.stdin,
        "kode_keluar": h.kode_keluar,
        "output_cocok": h.output_cocok,
        "galat": _galat_json(h.galat, ex, bahasa),
        "beda": None,
    }
    # Diff hanya bermakna kalau ada output untuk dibandingkan. Untuk kegagalan
    # kompilasi, menampilkannya cuma menambah kebisingan -- dan diagnosisnya
    # ("sudah pakai perintah cetak?") justru menyesatkan.
    if not h.lulus and h.mode not in ("regex", "mengandung"):
        if runner.normalisasi(h.aktual) or not (h.galat or "").strip():
            keluar["beda"] = _beda_json(beda.bandingkan(h.harapan, h.aktual))
    return keluar


def _jalan_json(hasil, ex=None, bahasa="", nama_berkas=""):
    if ex is not None:
        blok_galat = _galat_json(hasil.galat, ex, bahasa)
    elif hasil.galat.strip():
        # Tanpa `rapikan`, path direktori sementara ("/tmp/belajar-oykbqcmu/
        # Main.java") muncul apa adanya di ruang coba -- alamat yang tidak
        # pernah dibuka pengguna dan tidak bisa dia perbaiki.
        rapi = modul_galat.rapikan(hasil.galat, nama_berkas)
        blok_galat = {"mentah": rapi,
                      "baris": modul_galat.ringkas(rapi, 14),
                      "artinya": modul_galat.terjemahkan(rapi)}
    else:
        blok_galat = None
    return {
        "sukses": hasil.sukses,
        "keluaran": hasil.keluaran,
        "galat": blok_galat,
        "kode_keluar": hasil.kode_keluar,
        "fase": hasil.fase,
        "timeout": hasil.timeout,
        "catatan": hasil.catatan,
    }


# ---------------------------------------------------------------- bootstrap

def awal(_=None):
    """Semua yang dibutuhkan halaman untuk hidup, dalam satu permintaan."""
    data = progress.load_progress()
    return {
        # Berkas pelajar yang tidak bisa diurai dan sudah dipindah ke samping
        # (pelajar/simpanan.py). Web memberi tahu sekali per jalur.
        "karantina": list(simpanan.KARANTINA),
        "versi": aplikasi.VERSI,
        "versi_web": VERSI_WEB,
        "bahasa": [{
            "key": l["key"],
            "label": l["label"],
            "runner": l["runner"],
            "sorot": isi.bahasa_sorot(l),
            "materi": len(l["materials"]),
            "kuis": len(l["quizzes"]),
            "soal": sum(len(q["questions"]) for q in l["quizzes"]),
            "latihan": len(l["exercises"]),
            "siap": runner.tersedia(l["runner"]),
            "hilang": runner.program_hilang(l["runner"]),
            "pasang": runner.perintah_instalasi(l["runner"]),
            "cara_jalan": list(l["run_info"]),
            "persen": _stat(l, data)["persen"],
            # Kurikulum tematik (Bikin Aplikasi, CLI Fedora) bukan bahasa
            # pemrograman. Navigasi memisahkannya supaya daftar 19 butir
            # tetap terbaca; penandanya datang dari LANGUAGES, tidak
            # ditebak JavaScript dari labelnya.
            "tematik": bool(l.get("tematik")),
        } for l in LANGUAGES],
        "aturan_sorot": isi.aturan_penyorot(),
        # Kalimat aturan bab dikirim dari sini, bukan ditulis ulang di
        # JavaScript. Aturannya sudah punya satu tempat tinggal (`bab.py`);
        # rumusan yang menjelaskannya ke pelajar harus tinggal di sana juga,
        # kalau tidak keduanya melenceng diam-diam dan pelajar membaca dua
        # aturan berbeda tergantung ia sampai dari terminal atau dari browser.
        "aturan_bab": {
            "aturan": modul_bab.KALIMAT_ATURAN,
            "pintu_darurat": modul_bab.KALIMAT_PINTU_DARURAT,
            "tingkat": [{"nama": t, "label": modul_bab.LABEL_TINGKAT[t],
                         "ket": modul_bab.KETERANGAN_TINGKAT[t]}
                        for t in modul_bab.TINGKAT],
        },
        "konfigurasi": konfigurasi_baca(),
        "lokasi": {
            "progres": progress.PROGRESS_FILE,
            "konfigurasi": konfigurasi.BERKAS,
            "catatan": modul_catatan.BERKAS,
            "kerja": exercises.DIR_KERJA,
        },
        "batas": {
            "waktu": runner.BATAS_WAKTU_DETIK,
            "memori_mb": runner.BATAS_MEMORI_MB,
            "output": runner.BATAS_OUTPUT_CHAR,
        },
    }


# ------------------------------------------------------------------- dasbor

def _indeks_langkah(s):
    kolom = {"materi": "materials", "kuis": "quizzes", "latihan": "exercises"}[s.tipe]
    for i, o in enumerate(s.lang[kolom]):
        if o["title"] == s.judul:
            return i
    return 0


def _langkah_json(s):
    return {
        "tipe": s.tipe,
        "bahasa": s.lang["key"],
        "label_bahasa": s.lang["label"],
        "judul": s.judul,
        "alasan": s.alasan,
        "indeks": _indeks_langkah(s),
        "menit": waktu.menit(s.tipe, s.obj),
    }


def dasbor(_=None):
    data = progress.load_progress()
    xp = data.get("xp", 0)
    level, di_level, butuh = progress.info_level(xp)
    dimiliki = set(data.get("badge", []))

    per_bahasa = []
    total_skor = total_maks = 0
    for lang in LANGUAGES:
        s = _stat(lang, data)
        total_skor += s["skor"]
        total_maks += s["skor_maks"]
        per_bahasa.append({
            "key": lang["key"], "label": lang["label"],
            "siap": runner.tersedia(lang["runner"]),
            **{k: s[k] for k in (
                "materi", "materi_sebagian", "total_materi", "kuis", "total_kuis",
                "latihan_lulus", "latihan_manual", "latihan_dilihat",
                "total_latihan", "skor", "skor_maks", "persen")},
        })

    tantangan = modul_saran.tantangan_harian(LANGUAGES, data)

    # "Aku sudah sejauh mana?" dijawab di atas lipatan dasbor: bahasa yang
    # terakhir disentuh dan bab yang sedang berjalan. Babnya dibaca dari
    # bab.status, satu-satunya yang berhak memutuskan penguncian.
    posisi = None
    aktif = modul_saran.bahasa_terakhir(LANGUAGES, data)
    if aktif:
        semua_bab = modul_bab.status(aktif, data)
        kini = next((b for b in semua_bab if b["status"] != modul_bab.TERKUNCI
                     and b["selesai"] < b["jumlah"]), semua_bab[-1] if semua_bab else None)
        s = _stat(aktif, data)
        posisi = {"key": aktif["key"], "label": aktif["label"],
                  "bab": kini["nomor"] if kini else 0, "bab_total": len(semua_bab),
                  "bab_judul": kini["judul"] if kini else "",
                  "materi": s["materi"], "total_materi": s["total_materi"],
                  "persen": s["persen"]}

    return {
        "posisi": posisi,
        "kuis_jatuh_tempo": sum(
            progress.kuis_jatuh_tempo(data, f"{l['key']}_kuis", q["title"])
            for l in LANGUAGES for q in l["quizzes"]),
        "nama": konfigurasi.ambil("nama", ""),
        "xp": xp,
        "level": level,
        "gelar": progress.gelar_dari_level(level),
        "di_level": di_level,
        "butuh_level": butuh,
        "streak": progress.streak_aktif(data),
        "streak_rekor": data.get("streak", {}).get("terpanjang", 0),
        "streak_total": data.get("streak", {}).get("total_hari", 0),
        "xp_hari_ini": progress.xp_hari_ini(data),
        # Pembanding untuk angka hari ini. Tanpa ini "38 XP" berdiri sendiri
        # dan tidak menjawab "38 itu banyak atau sedikit bagiku".
        #
        # Dibaca, bukan dihitung: `riwayat_harian` sudah menyimpan XP per hari,
        # dan dua hari terakhir mengembalikan [(kemarin, xp), (hari ini, xp)].
        # Tidak ada definisi kedua untuk XP di sini, tidak ada tulisan ke
        # berkas progres, dan karena nol mutasi ia tidak melewati
        # _KUNCI_PROGRES.
        "xp_kemarin": progress.riwayat_harian(data, 2)[0][1],
        # Tanggal hari belajar terakhir, dibaca dari field yang SAMA yang
        # dipakai `streak_aktif()` untuk memutuskan. Menyimpulkannya dari
        # riwayat XP akan jadi definisi kedua dan langsung bertentangan:
        # `record_material_read(..., tuntas=False)` membuat streak hidup
        # sehari penuh tanpa menambah satu pun XP, jadi hari itu tidak punya
        # entri riwayat sama sekali.
        "hari_belajar_terakhir": (data.get("streak") or {}).get(
            "tanggal_terakhir", ""),
        "target_harian": konfigurasi.ambil("target_xp_harian", 60),
        "badge_dimiliki": len(dimiliki),
        "badge_total": len(progress.DAFTAR_BADGE),
        "heatmap": [{"tanggal": t, "xp": x}
                    for t, x in progress.riwayat_harian(data, 7 * 26)],
        "bahasa": per_bahasa,
        "skor_kuis": {"benar": total_skor, "maks": total_maks},
        "langkah": [_langkah_json(s)
                    for s in modul_saran.langkah_berikutnya(LANGUAGES, data, maks=6)],
        "tantangan": _langkah_json(tantangan) if tantangan else None,
        "terakhir": data.get("terakhir") or {},
        "catatan_jumlah": modul_catatan.jumlah(),
    }


def statistik(_=None):
    data = progress.load_progress()
    dimiliki = set(data.get("badge", []))
    return {
        **dasbor(),
        "semua_badge": [{"id": b, "nama": n, "deskripsi": d, "punya": b in dimiliki}
                        for b, n, d, _syarat in progress.DAFTAR_BADGE],
        "toolchain": [{
            "key": l["key"], "label": l["label"],
            "siap": runner.tersedia(l["runner"]),
            "hilang": runner.program_hilang(l["runner"]),
            "pasang": runner.perintah_instalasi(l["runner"]),
            "catatan": (runner.TOOLCHAINS[l["runner"]].catatan
                        if l["runner"] in runner.TOOLCHAINS else ""),
        } for l in LANGUAGES],
        # Namanya BUKAN "gelar": kunci itu sudah dipakai `dasbor()` untuk gelar
        # yang sedang disandang. Menimpanya membuat header statistik mencetak
        # daftar berisi objek, bukan nama gelarnya.
        "tangga_gelar": [{"level": lv, "nama": n} for lv, n in progress.GELAR],
        "xp_tarif": {
            "materi": progress.XP_MATERI,
            "latihan_dilihat": progress.XP_LATIHAN_DILIHAT,
            "latihan_lulus": progress.XP_LATIHAN_LULUS,
            "latihan_manual": progress.XP_LATIHAN_MANUAL,
            "per_jawaban_benar": progress.XP_PER_JAWABAN_BENAR,
            "bonus_kuis_sempurna": progress.XP_BONUS_KUIS_SEMPURNA,
        },
    }


# ------------------------------------------------------------------- bahasa

def bahasa(params):
    lang = _bahasa(params.get("key"))
    data = progress.load_progress()
    # Sekali hitung, lalu dipinjamkan ke daftar materinya: tiap panggilan
    # `bab.status()` membaca progres lagi.
    daftar_bab = modul_bab.status(lang, data)
    return {
        "key": lang["key"], "label": lang["label"], "runner": lang["runner"],
        "sorot": isi.bahasa_sorot(lang),
        "siap": runner.tersedia(lang["runner"]),
        "hilang": runner.program_hilang(lang["runner"]),
        "pasang": runner.perintah_instalasi(lang["runner"]),
        "cara_jalan": list(lang["run_info"]),
        "catatan": (runner.TOOLCHAINS[lang["runner"]].catatan
                    if lang["runner"] in runner.TOOLCHAINS else ""),
        "statistik": _stat(lang, data),
        "materi": isi.daftar_materi(lang, data, daftar_bab),
        "kuis": isi.daftar_kuis(lang, data),
        "latihan": isi.daftar_latihan(lang, data),
        "bab": daftar_bab,
        # Kalimat ringkasnya dirangkai bab.py, bukan di sini: kalau tidak,
        # terminal dan web akan menjelaskan keadaan yang sama dengan dua
        # kalimat berbeda. `data` yang sama diteruskan supaya berkas progres
        # tetap cuma dibaca sekali per permintaan.
        "bab_kalimat": modul_bab.kalimat_ringkas(lang, data),
        # Cuma untuk ditampilkan ("bab sedang dibuka semua"). Keputusan sebuah
        # materi terkunci atau tidak tetap sepenuhnya milik bab.py -- nilai ini
        # tidak boleh dipakai untuk memutuskan apa pun di sini.
        "buka_semua_bab": bool(konfigurasi.ambil("buka_semua_bab", False)),
        # Ringkasan bacaan dari Pustaka, dihitung inti/pustaka.py -- terminal
        # menampilkan ringkasan yang sama di menu bahasanya.
        "pustaka": modul_pustaka.ringkasan_kurikulum(lang["key"]),
    }


# ------------------------------------------------------------------ pustaka

def pustaka(params):
    """Cari dan saring tautan Pustaka; satu halaman hasil plus cacah segi.

    Label penyaring ikut dikirim dari sini supaya web tidak menyimpan daftar
    jenis atau nama kurikulum sendiri: dua salinan daftar yang sama adalah dua
    daftar yang suatu hari berbeda.
    """
    kurikulum = params.get("kurikulum") or None
    if kurikulum and not any(l["key"] == kurikulum for l in LANGUAGES):
        raise Galat("Kurikulum tidak dikenal.", 400)
    jenis = params.get("jenis") or None
    if jenis and jenis not in modul_pustaka.JENIS:
        raise Galat("Jenis tidak dikenal.", 400)
    bahasa = params.get("bahasa") or None
    if bahasa and bahasa not in modul_pustaka.BAHASA:
        raise Galat("Bahasa tidak dikenal.", 400)
    try:
        halaman = int(params.get("hal") or 1)
    except ValueError:
        raise Galat("Halaman harus angka.", 400)
    hasil = modul_pustaka.cari(
        params.get("q", ""), kurikulum=kurikulum, jenis=jenis, bahasa=bahasa,
        sumber=params.get("sumber") or None, halaman=halaman, per_halaman=40)
    hasil["label"] = {
        "jenis": modul_pustaka.JENIS,
        "bahasa": modul_pustaka.BAHASA,
        "kurikulum": {l["key"]: l["label"] for l in LANGUAGES},
    }
    hasil["sumber"] = modul_pustaka.daftar_sumber()
    hasil["semua"] = modul_pustaka.total()
    return hasil


# ------------------------------------------------------------------- karier

def karier(_=None):
    """Seluruh Peta Karier plus kesiapan pelajar, dari pelajar/karier.py.

    Kesiapan dihitung server dari progres -- browser tidak pernah menghitung
    ulang persen dari daftar materi yang dibaca.
    """
    return {**modul_karier.ringkasan(LANGUAGES, progress.load_progress()),
            "tujuan": konfigurasi.ambil("tujuan_karier", "")}


def karier_kuis(params):
    """'?pilihan=1,3,,0' -> tiga profesi teratas. Kosong = soal dilewati."""
    mentah = (params.get("pilihan") or "").split(",")
    pilihan = []
    for m in mentah[:len(modul_karier.data_karier.KUIS)]:
        m = m.strip()
        if not m:
            pilihan.append(None)
            continue
        if not m.isdigit():
            raise Galat("Pilihan kuis harus angka.", 400)
        pilihan.append(int(m))
    return {"hasil": modul_karier.skor_kuis(pilihan)}


def karier_jalur(params):
    dari, ke = params.get("dari"), params.get("ke")
    if dari not in modul_karier.PER_ID or ke not in modul_karier.PER_ID:
        raise Galat("Profesi tidak dikenal.", 400)
    langkah = modul_karier.jalur(dari, ke)
    return {"jalur": langkah or [],
            "celah": modul_karier.celah_bekal(dari, ke) if langkah else []}


# ------------------------------------------------------------------- materi

def materi(params):
    """Isi satu materi -- dan di sinilah penguncian bab ditegakkan.

    Penjagaannya sengaja ada di titik MEMBUKA, bukan di daftar: daftar tetap
    menampilkan semua judul supaya orang tahu apa yang menantinya, sedangkan
    yang benar-benar tidak boleh terjadi adalah isinya terbaca sebelum
    syaratnya terpenuhi.
    """
    lang = _bahasa(params.get("key"))
    idx, m = _ambil(lang["materials"], params.get("indeks"), "materi")
    data = progress.load_progress()
    kat = f"{lang['key']}_materi"
    k = kunci_progres(kat, m["title"])

    daftar_bab = modul_bab.status(lang, data)
    # Rentang bab dijamin menutupi seluruh materi -- pembagian yang tidak lagi
    # cocok jatuh ke satu bab berisi semuanya -- jadi materi ini pasti punya
    # babnya.
    bab_ini = next(b for b in daftar_bab if b["awal"] <= idx < b["akhir"])
    if bab_ini["status"] == modul_bab.TERKUNCI:
        # Kalimatnya diambil utuh dari bab.py: yang perlu didengar pelajar
        # bukan kata "terkunci" melainkan berapa materi lagi yang kurang.
        raise Galat(bab_ini["alasan"] or "Materi ini masih terkunci.", 403)

    # Tetangga yang babnya masih terkunci tidak ditawarkan sama sekali. Tombol
    # "Berikutnya" yang berujung penolakan lebih buruk daripada tidak adanya
    # tombol itu: yang pertama terasa seperti aplikasinya rusak.
    terbuka = {i for b in daftar_bab if b["status"] != modul_bab.TERKUNCI
               for i in b["materi"]}
    return {
        "bahasa": lang["key"], "label_bahasa": lang["label"],
        "sorot": isi.bahasa_sorot(lang),
        "indeks": idx,
        "jumlah": len(lang["materials"]),
        "judul": m["title"],
        "sebelum": (lang["materials"][idx - 1]["title"]
                    if idx > 0 and idx - 1 in terbuka else ""),
        "sesudah": (lang["materials"][idx + 1]["title"]
                    if idx + 1 < len(lang["materials"]) and idx + 1 in terbuka
                    else ""),
        "bagian": isi.bagian_materi(m, lang),
        "status": isi.status_materi(data, kat, m["title"]),
        # Sebagian bidang bab, diteruskan apa adanya: halaman materi cuma
        # perlu tahu ia sedang di bab mana dan sudah sejauh mana babnya.
        "bab": {bidang: bab_ini[bidang] for bidang in
                ("nomor", "judul", "tingkat", "label_tingkat",
                 "jumlah", "selesai")},
        "bookmark": k in data["bookmark"],
        "kunci": k,
        "catatan": modul_catatan.ambil(k),
    }


def materi_selesai(body):
    """Tandai materi tuntas atau baru-sebagian.

    `tuntas=False` sengaja tidak memberi XP: materi dihitung selesai hanya
    kalau dibaca sampai habis, dan aturan itu milik `progress`, bukan milik
    antarmuka ini.

    Penguncian bab tidak diperiksa lagi di sini. Batasnya ditegakkan sekali,
    saat materinya DIBUKA (`materi()`), dan materi yang sedang dibaca selalu
    ada di bab yang terbuka. Pemeriksaan kedua cuma menambah satu tempat lagi
    yang bisa berbeda pendapat dengan bab.py.
    """
    lang = _bahasa(body.get("key"))
    _idx, m = _ambil(lang["materials"], body.get("indeks"), "materi")
    tuntas = bool(body.get("tuntas", True))
    with _KUNCI_PROGRES:
        sebelum = progress.load_progress()
        badge = progress.record_material_read(f"{lang['key']}_materi",
                                              m["title"], tuntas=tuntas)
        sesudah = progress.load_progress()
        return {"status": "selesai" if tuntas else "sebagian",
                # Kuis yang baru saja siap karena materi ini: ditawarkan di
                # kaki materi selagi bacaannya masih segar.
                "kuis_siap": [{"indeks": i, "judul": q["title"]}
                              for i, q in kuis_materi.kuis_baru_siap(lang, sebelum, sesudah)],
                **_xp_dan_badge(sebelum, badge)}


# --------------------------------------------------------------------- kuis

def kuis_mulai(body):
    lang = _bahasa(body.get("key"))
    idx, q = _ambil(lang["quizzes"], body.get("indeks"), "kuis")
    kat = f"{lang['key']}_kuis"
    mode = body.get("mode") or "penuh"
    acak = bool(body.get("acak", konfigurasi.ambil("acak_bawaan", True)))

    durasi = 0
    if body.get("timer"):
        per_soal = konfigurasi.ambil("detik_per_soal", 30) or 30
        durasi = per_soal * len(q["questions"])

    hanya = None
    if mode == "salah":
        hanya = progress.soal_salah_terakhir(kat, q["title"])
        if not hanya:
            raise Galat("Tidak ada soal yang masih salah untuk kuis ini.", 409)

    s = sesi.buat(kat, q["title"], isi.bahasa_sorot(lang), q["questions"],
                  mode=mode, acak=acak, durasi=durasi, hanya=hanya)
    if s is None:
        raise Galat("Kuis ini tidak punya soal.", 409)
    return {**s.bersih(), "indeks": idx, "bahasa_key": lang["key"],
            "label_bahasa": lang["label"]}


def kuis_jawab(body):
    hasil = sesi.jawab(body.get("sesi"), body.get("nomor"), body.get("pilihan"))
    if hasil is None:
        raise Galat("Sesi kuis sudah tidak ada. Mulai ulang kuisnya.", 410)
    return hasil


def kuis_selesai(body):
    r = sesi.rekap(body.get("sesi"))
    if r is None:
        raise Galat("Sesi kuis sudah tidak ada.", 410)

    with _KUNCI_PROGRES:
        sebelum = progress.load_progress()
        if r["sesi_penuh"]:
            badge = progress.record_quiz_score(
                r["kategori"], r["judul"], r["benar"], r["total"],
                salah_index=r["salah_asli"], sesi_penuh=True)
        else:
            # Mode ulangan: hanya perbarui daftar soal yang masih salah.
            # Soal yang tadi berhasil dijawab dicoret dari daftar LAMA, bukan
            # menggantinya -- kalau tidak, mengulang 2 dari 5 soal salah akan
            # membuat 3 sisanya lenyap dan seolah sudah dikuasai.
            lama = set(progress.soal_salah_terakhir(r["kategori"], r["judul"]))
            dikerjakan = {d["asli"] for d in r["rincian"]}
            tersisa = sorted((lama - dikerjakan) | set(r["salah_asli"]))
            badge = progress.perbarui_soal_salah(r["kategori"], r["judul"], tersisa)
        hadiah = _xp_dan_badge(sebelum, badge)

    # Soal yang salah menunjuk materi sumbernya ("Baca lagi: ...").
    # Statusnya dibaca dari bab.py: tautan ke materi terkunci ditandai LEBIH
    # DULU, bukan berujung penolakan.
    lang_kuis = _bahasa(r["kategori"].rsplit("_", 1)[0])
    terbuka = modul_bab.indeks_terbuka(lang_kuis, progress.load_progress())
    for d in r["rincian"]:
        sumber = kuis_materi.materi_soal(lang_kuis, r["judul"], d["asli"])
        d["baca_lagi"] = ({"indeks": sumber[0], "judul": sumber[1],
                           "terkunci": sumber[0] not in terbuka} if sumber else None)
    sesudah = progress.load_progress()
    k = kunci_progres(r["kategori"], r["judul"])
    jadwal = sesudah["jadwal_kuis"].get(k, {})
    skor = sesudah["kuis_skor"].get(k, {})
    return {
        **r, **hadiah,
        "terbaik": skor.get("terbaik", 0),
        "percobaan": skor.get("percobaan", 0),
        # Skor percobaan SEBELUM usaha ini, dibaca dari potret `sebelum` yang
        # diambil di dalam `_KUNCI_PROGRES` (`:554`) -- yaitu sebelum
        # `record_quiz_score` menimpa `terakhir_skor` (`progress.py:595`).
        # Bacaan, bukan tulisan: `sebelum` sudah berupa dict di memori, jadi
        # tidak ada penguncian baru di sini.
        #
        # `None`, bukan `0`. `0` berarti "percobaan sebelumnya nol benar";
        # `None` berarti "belum pernah ada percobaan". Mencetak "naik dari
        # 0/10" kepada orang yang baru pertama menyelesaikan kuis terbaca
        # sebagai penghukuman, dan itu kalimat yang tidak boleh keluar dari
        # layar hasil. `.get("terakhir_skor")` tanpa nilai bawaan yang
        # menjaganya -- menambahkan `, 0` di situ mengembalikan cacatnya.
        #
        # `k` yang sama dipakai untuk kedua potret, jadi `kunci_progres` tetap
        # dipanggil SEKALI (`:571`).
        "terakhir_sebelum": sebelum["kuis_skor"].get(k, {}).get("terakhir_skor"),
        "jadwal": jadwal.get("jatuh_tempo", ""),
        "interval": jadwal.get("interval", 0),
        "salah_tersisa": len(progress.soal_salah_terakhir(r["kategori"], r["judul"])),
    }


def kuis_batal(body):
    sesi.hapus(body.get("sesi"))
    return {"ok": True}


# ------------------------------------------------------------------ latihan

def _hangatkan(lang, ex):
    """Turunkan kunci jawaban di latar supaya tombol Periksa tidak menunggu."""
    tanda = (lang["key"], ex["title"])
    with _KUNCI_HANGAT:
        if tanda in _SEDANG_HANGAT:
            return
        _SEDANG_HANGAT.add(tanda)

    def kerja():
        try:
            exercises.bangun_tests(ex, lang["runner"])
        except Exception:
            pass          # pemanasan gagal cuma berarti Periksa jadi lebih lama
        finally:
            with _KUNCI_HANGAT:
                _SEDANG_HANGAT.discard(tanda)

    threading.Thread(target=kerja, daemon=True,
                     name=f"hangat-{lang['key']}").start()


def latihan(params):
    lang = _bahasa(params.get("key"))
    idx, ex = _ambil(lang["exercises"], params.get("indeks"), "latihan")
    kat = f"{lang['key']}_latihan"
    bhs = lang["runner"]
    bhs_sorot = isi.bahasa_sorot(lang)

    with _KUNCI_PROGRES:
        sebelum = progress.load_progress()
        badge = progress.record_exercise_viewed(kat, ex["title"])
        hadiah = _xp_dan_badge(sebelum, badge)

    data = progress.load_progress()
    boleh, alasan = exercises.bisa_dinilai(ex, bhs)
    nama = exercises.nama_kerja(ex, bhs)
    path = _path_kerja(kat, ex, bhs)
    tersimpan = _baca_kerja(path)
    if boleh:
        _hangatkan(lang, ex)

    rumah = os.path.expanduser("~")
    folder = os.path.dirname(path)
    k = kunci_progres(kat, ex["title"])
    return {
        "bahasa": lang["key"], "label_bahasa": lang["label"],
        "runner": bhs, "sorot": bhs_sorot,
        "indeks": idx, "jumlah": len(lang["exercises"]),
        "judul": ex["title"],
        "tingkat": ex.get("difficulty", "Menengah"),
        "proyek": bool(ex.get("proyek")),
        "soal": list(ex.get("question") or []),
        # Soal latihan lewat pengurai yang SAMA dengan badan materi. Sebelum
        # ini ia dikirim sebagai satu blok teks dan digambar dengan
        # `white-space: pre-line`, yang meruntuhkan deretan spasi -- padahal
        # hampir semua soal di sini memuat contoh keluaran berkolom, dan
        # perataan kolom itulah yang menerangkan apa yang harus dicetak.
        # Yang terbaca pelajar: tabel yang kolomnya berantakan, di panel yang
        # bahkan tidak cukup lebar untuk menampungnya.
        "soal_blok": isi.blok_badan(list(ex.get("question") or [])),
        "hint": list(ex.get("hints") or []),
        "solusi": ex.get("solution", ""),
        "token_solusi": isi.token_kode(ex.get("solution", ""), bhs_sorot),
        "setup": ex.get("setup", ""),
        "token_setup": (isi.token_kode(ex["setup"], bhs_sorot)
                        if ex.get("setup", "").strip() else []),
        "stdin": ex.get("stdin", ""),
        "stdin_list": list(ex.get("stdin_list") or []),
        "mode": ex.get("mode", "persis"),
        "dinilai": boleh,
        "alasan": alasan,
        "bisa_jalan": runner.tersedia(bhs),
        "status": isi.status_latihan(data, kat, ex["title"]),
        "bookmark": k in data["bookmark"],
        "kunci": k,
        "catatan": modul_catatan.ambil(k),
        "kode": tersimpan or exercises._kerangka(bhs, ex),
        "ada_simpanan": bool(tersimpan),
        "berkas": {
            "nama": nama,
            "folder": ("~" + folder[len(rumah):]) if folder.startswith(rumah) else folder,
            "perintah": modul_berkas.perintah_jalan(bhs, nama),
        },
        "batas_waktu": runner.batas_waktu(bhs),
        "hadiah": hadiah,
    }


def latihan_simpan(body):
    """Tulis kode pelajar ke berkas kerjanya.

    Jalurnya sama persis dengan yang dipakai aplikasi terminal, jadi jawaban
    yang ditulis di browser bisa langsung dibuka di editor dan dijalankan dari
    shell -- dan sebaliknya.
    """
    lang = _bahasa(body.get("key"))
    _idx, ex = _ambil(lang["exercises"], body.get("indeks"), "latihan")
    kat = f"{lang['key']}_latihan"
    path = _path_kerja(kat, ex, lang["runner"], buat_folder=True)
    kode = body.get("kode") or ""
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(kode)
    except OSError as e:
        raise Galat(f"Gagal menyimpan berkas: {e}", 500)
    return {"ok": True, "path": path, "bita": len(kode.encode("utf-8"))}


def latihan_jalankan(body):
    lang = _bahasa(body.get("key"))
    _idx, ex = _ambil(lang["exercises"], body.get("indeks"), "latihan")
    bhs = lang["runner"]
    kode = body.get("kode") or ""

    if body.get("simpan", True):
        try:
            latihan_simpan(body)
        except Galat:
            pass          # gagal menyimpan tidak boleh menghalangi menjalankan

    stdin = body.get("stdin")
    if stdin is None:
        stdin = ex.get("stdin", "") or (ex.get("stdin_list") or [""])[0]

    mulai = time.time()
    hasil = runner.jalankan(bhs, exercises.gabung_setup(ex, kode), stdin=stdin)
    return {**_jalan_json(hasil, ex, bhs), "stdin": stdin,
            "detik": round(time.time() - mulai, 2)}


def latihan_periksa(body):
    lang = _bahasa(body.get("key"))
    _idx, ex = _ambil(lang["exercises"], body.get("indeks"), "latihan")
    kat = f"{lang['key']}_latihan"
    bhs = lang["runner"]
    kode = body.get("kode") or ""

    if body.get("simpan", True):
        try:
            latihan_simpan(body)
        except Galat:
            pass

    tests, pesan = exercises.bangun_tests(ex, bhs)
    if pesan:
        return {"bisa_dinilai": False, "alasan": pesan, "lulus": False, "uji": []}
    if not tests:
        return {"bisa_dinilai": False, "lulus": False, "uji": [],
                "alasan": "Belum ada kunci jawaban untuk latihan ini."}

    mulai = time.time()
    semua, hasil_uji, _ = runner.periksa(bhs, exercises.gabung_setup(ex, kode), tests)

    hadiah = None
    if semua:
        with _KUNCI_PROGRES:
            sebelum = progress.load_progress()
            badge = progress.record_exercise_passed(kat, ex["title"])
            hadiah = _xp_dan_badge(sebelum, badge)

    return {
        "bisa_dinilai": True,
        "lulus": semua,
        "detik": round(time.time() - mulai, 2),
        "uji": [_uji_json(h, ex, bhs) for h in hasil_uji],
        "hadiah": hadiah,
        "status": isi.status_latihan(progress.load_progress(), kat, ex["title"]),
    }


def latihan_manual(body):
    """Tandai / batalkan tanda selesai untuk latihan yang tak bisa dinilai mesin."""
    lang = _bahasa(body.get("key"))
    _idx, ex = _ambil(lang["exercises"], body.get("indeks"), "latihan")
    kat = f"{lang['key']}_latihan"
    nyalakan = bool(body.get("nyalakan", True))

    boleh, _alasan = exercises.bisa_dinilai(ex, lang["runner"])
    if boleh and nyalakan:
        raise Galat("Latihan ini bisa dinilai otomatis -- kerjakan lalu tekan "
                    "Periksa, jangan ditandai manual.", 409)

    with _KUNCI_PROGRES:
        sebelum = progress.load_progress()
        if nyalakan:
            badge = progress.tandai_latihan_manual(kat, ex["title"])
            return {"status": "manual", **_xp_dan_badge(sebelum, badge)}
        progress.batalkan_latihan_manual(kat, ex["title"])
        status = isi.status_latihan(progress.load_progress(), kat, ex["title"])
        return {"status": status, **_xp_dan_badge(sebelum, [])}


def latihan_kerangka(params):
    """Template awal, untuk tombol 'kembalikan ke kerangka'."""
    lang = _bahasa(params.get("key"))
    _idx, ex = _ambil(lang["exercises"], params.get("indeks"), "latihan")
    return {"kode": exercises._kerangka(lang["runner"], ex)}


# --------------------------------------------------------------- ruang coba

MAKS_KODE = 200_000


def coba(body):
    """Jalankan kode bebas. Bukan latihan: tidak dinilai, tidak menyentuh progres."""
    bhs = body.get("bahasa") or "python"
    if bhs not in runner.TOOLCHAINS:
        raise Galat(f"Bahasa '{bhs}' tidak bisa dijalankan.", 400)
    if not runner.tersedia(bhs):
        hilang = ", ".join(runner.program_hilang(bhs))
        pasang = runner.perintah_instalasi(bhs)
        raise Galat(f"Belum terpasang: {hilang}."
                    + (f" Pasang dengan: {pasang}" if pasang else ""), 409)

    kode = body.get("kode") or ""
    if len(kode) > MAKS_KODE:
        raise Galat("Kodenya terlalu panjang untuk dijalankan di sini.", 413)

    tc = runner.TOOLCHAINS[bhs]
    nama = tc.nama_file(kode) if tc.nama_file else ("kodemu" + tc.ekstensi)

    mulai = time.time()
    hasil = runner.jalankan(bhs, kode, stdin=body.get("stdin") or "")
    return {**_jalan_json(hasil, nama_berkas=nama),
            "detik": round(time.time() - mulai, 2),
            "bahasa": bhs, "berkas": nama}


def contoh_kode(params):
    """Ambil satu blok kode materi untuk dibuka di ruang coba.

    Blok kode ADALAH isi materi, jadi ia lewat pintu yang sama seperti
    `materi()`. Antarmuka memang tidak pernah sampai ke sini tanpa membuka
    materinya lebih dulu -- tombol "Coba jalankan" cuma ada di halaman materi
    yang sudah terbuka -- tapi endpoint yang lebih longgar daripada halaman
    yang memanggilnya adalah cara termudah sebuah pintu berhenti berarti.
    """
    lang = _bahasa(params.get("key"))
    idx, m = _ambil(lang["materials"], params.get("indeks"), "materi")
    # Keputusannya tetap sepenuhnya milik bab.py; di sini cuma dibacakan.
    bab_ini = modul_bab.bab_materi(lang, idx)
    if bab_ini and bab_ini["status"] == modul_bab.TERKUNCI:
        raise Galat(bab_ini["alasan"] or "Materi ini masih terkunci.", 403)
    try:
        nomor = int(params.get("bagian", 0))
    except (TypeError, ValueError):
        raise Galat("Nomor bagian tidak sah.", 400)
    if not 0 <= nomor < len(m["sections"]):
        raise Galat("Bagian tidak ada.", 404)
    bagian = m["sections"][nomor]
    if "code" not in bagian:
        raise Galat("Bagian ini bukan blok kode.", 409)
    return {"bahasa": lang["runner"], "kode": bagian["code"],
            "judul": bagian.get("heading") or m["title"]}


# ---------------------------------------------------------- cari & bookmark

def cari(params):
    kata = params.get("q", "")
    tipe = params.get("tipe", "semua")
    # Progres dibaca sekali di sini dan diteruskan: `isi.cari` menyisir sebelas
    # bahasa, dan membiarkannya membaca berkas progres per bahasa berarti
    # sebelas kali baca-berkas untuk tiap huruf yang diketik.
    return {"kata": kata, "tipe": tipe,
            "hasil": isi.cari(LANGUAGES, kata, tipe,
                              data=progress.load_progress())}


_KOLOM = {"materi": "materials", "kuis": "quizzes", "latihan": "exercises"}


def _uraikan_kunci(k):
    """'java_materi::Judul' -> (lang, tipe, indeks, judul), atau None kalau basi."""
    if "::" not in k:
        return None
    kategori, judul = k.split("::", 1)
    if "_" not in kategori:
        return None
    key, tipe = kategori.rsplit("_", 1)
    lang = next((l for l in LANGUAGES if l["key"] == key), None)
    if lang is None or tipe not in _KOLOM:
        return None
    for i, o in enumerate(lang[_KOLOM[tipe]]):
        # Lewat judul_kunci: kunci tersimpan sudah dibuang nomor urutnya,
        # judul di kurikulum belum. Tanpa penyamaan ini setiap bookmark dan
        # setiap catatan tampak menunjuk materi yang sudah tidak ada.
        if progress.judul_kunci(o["title"]) == progress.judul_kunci(judul):
            # Judul yang dikembalikan adalah judul KURIKULUM (lengkap dengan
            # nomornya), bukan potongan yang tersimpan di kunci. Kunci tidak
            # membawa nomor supaya tahan penyisipan materi; layar tetap
            # menampilkan nomornya, dan yang tahu nomor terbaru cuma
            # kurikulumnya.
            return lang, tipe, i, o["title"]
    return None


def bookmark_daftar(_=None):
    data = progress.load_progress()
    keluar = []
    basi = 0
    for k in data["bookmark"]:
        u = _uraikan_kunci(k)
        if u is None:
            basi += 1
            continue
        lang, tipe, i, judul = u
        keluar.append({"kunci": k, "tipe": tipe, "bahasa": lang["key"],
                       "label_bahasa": lang["label"], "indeks": i, "judul": judul})
    return {"daftar": keluar, "basi": basi}


def bookmark_ubah(body):
    lang = _bahasa(body.get("key"))
    tipe = body.get("tipe")
    if tipe not in _KOLOM:
        raise Galat("Tipe bookmark tidak dikenal.", 400)
    _idx, o = _ambil(lang[_KOLOM[tipe]], body.get("indeks"), tipe)
    with _KUNCI_PROGRES:
        aktif = progress.toggle_bookmark(f"{lang['key']}_{tipe}", o["title"])
    return {"bookmark": aktif}


def bookmark_bersihkan(_=None):
    sah = set()
    for lang in LANGUAGES:
        for tipe, kolom in _KOLOM.items():
            for o in lang[kolom]:
                sah.add(kunci_progres(f"{lang['key']}_{tipe}", o["title"]))
    with _KUNCI_PROGRES:
        dibuang = progress.bersihkan_bookmark(sah)
    return {"dibuang": dibuang}


# ------------------------------------------------------------------ catatan

def catatan_ambil(params):
    return modul_catatan.ambil(params.get("kunci", ""))


def catatan_tulis(body):
    k = body.get("kunci") or ""
    if "::" not in k:
        raise Galat("Kunci catatan tidak sah.", 400)
    return modul_catatan.tulis(k, body.get("teks", ""))


def catatan_semua(_=None):
    keluar = []
    for c in modul_catatan.semua():
        u = _uraikan_kunci(c["kunci"])
        if u is None:
            keluar.append({**c, "tipe": "", "bahasa": "", "label_bahasa": "",
                           "indeks": 0, "judul": c["kunci"], "basi": True})
            continue
        lang, tipe, i, judul = u
        keluar.append({**c, "tipe": tipe, "bahasa": lang["key"],
                       "label_bahasa": lang["label"], "indeks": i,
                       "judul": judul, "basi": False})
    return {"daftar": keluar}


# -------------------------------------------------------------- konfigurasi

def konfigurasi_baca(_=None):
    keluar = {}
    for o in konfigurasi.daftar_opsi():
        keluar[o.kunci] = {
            "label": o.label, "jenis": o.jenis,
            "nilai": konfigurasi.ambil(o.kunci),
            "bawaan": o.bawaan,
            "pilihan": [{"nilai": n, "label": l} for n, l in o.pilihan],
            "minimum": o.minimum, "maksimum": o.maksimum,
            "keterangan": o.keterangan,
        }
    return keluar


# Kunci setelan yang PENYIMPANANNYA bukan urusan browser, satu alasan per
# anggota.
#
# Dulu daftar ini sebuah set tanpa alasan, dan itu persis bentuk yang membuat
# dua kunci hilang tanpa kelihatan: `tema` dan `sorot_sintaks` ada di SKEMA,
# tidak ada di sini, dan tidak punya satu pun baris di layar Pengaturan web.
# Akibatnya `POST /api/konfigurasi {"tema": "terang"}` DITERIMA dan DITULIS ke
# berkas konfigurasi yang satu-satunya pembacanya terminal. Tidak ada galat di
# mana pun, dan yang mengirimnya tidak punya cara tahu bahwa browsernya tidak
# akan berubah sedikit pun.
#
# Sekarang alasannya menempel pada kuncinya, dan `TestPartisiKunciSetelan`
# mengadu daftar ini dengan SKEMA dan dengan baris web yang sungguhan ada.
# Menambah opsi ke SKEMA berarti memilih satu rumah dari tiga: sebuah baris di
# `layarAtur()`, satu anggota di sini, atau localStorage lewat
# `bacaTampilan()`. Tidak memilih berarti tes merah -- dan itu memang maunya.
_KONFIG_TERMINAL = {
    "lebar": "lebar kolom terminal; jendela browser mengurus lebarnya sendiri",
    "tinggi_halaman": "baris per halaman paginasi terminal; web menggulir, "
                      "tidak memaginasi",
    "warna": "kedalaman warna ANSI; di browser tidak ada terminal untuk "
             "dideteksi",
    "sorot_sintaks": "web menyalakan penyorotannya sendiri lewat sorot.js dan "
                     "tidak pernah menanyakan setelan ini",
    "tema": "tema WEB hidup di localStorage lewat bacaTampilan(), bukan di "
            "berkas konfigurasi: 'tema yang enak di terminal' dan 'tema yang "
            "enak di browser' tidak harus sama. Ruang nilainya pun sudah "
            "berbeda -- `malam` cuma ada di web, `mono` cuma di terminal -- "
            "jadi memberi kunci ini sebuah baris web akan MENGHILANGKAN satu "
            "nilai dari tiap sisi tanpa satu pun galat",
}


def konfigurasi_tulis(body):
    # `.keys()` bukan gaya: set dikurangi dict melempar TypeError, dikurangi
    # dict_keys tidak -- pandangan kunci sebuah dict memang set.
    sah = {o.kunci for o in konfigurasi.daftar_opsi()} - _KONFIG_TERMINAL.keys()
    diubah = {}
    for k, v in (body or {}).items():
        if k not in sah:
            continue
        konfigurasi.pasang(k, v)
        diubah[k] = konfigurasi.ambil(k)
    if not diubah:
        raise Galat("Tidak ada pengaturan sah yang dikirim.", 400)
    return {"diubah": diubah, "konfigurasi": konfigurasi_baca()}


def konfigurasi_bawaan(_=None):
    konfigurasi.kembalikan_bawaan()
    return {"konfigurasi": konfigurasi_baca()}


# -------------------------------------------------------------- kelola data

def laporan(_=None):
    return {"markdown": aplikasi._teks_laporan(progress.load_progress())}


def data_ekspor(_=None):
    return {"progres": progress.load_progress()}


def data_impor(body):
    masuk = body.get("progres")
    if not isinstance(masuk, dict):
        raise Galat("Isi berkas bukan data progres.", 400)
    with _KUNCI_PROGRES:
        cadangan = progress.cadangkan()
        if not progress.save_progress(progress._migrasi(dict(masuk))):
            raise Galat("Gagal menulis progres.", 500)
    return {"ok": True, "cadangan": cadangan or "tanpa cadangan"}


def data_cadangkan(_=None):
    with _KUNCI_PROGRES:
        return {"cadangan": progress.cadangkan()}


def data_reset(body):
    bagian = body.get("bagian") or "semua"
    if bagian != "semua" and not any(l["key"] == bagian for l in LANGUAGES):
        raise Galat("Bahasa tidak dikenal.", 400)
    # Reset tidak bisa dibatalkan. Kata kunci ini bukan basa-basi: ia memastikan
    # permintaan datang dari layar yang memang meminta konfirmasi, bukan dari
    # klik yang salah sasaran.
    if body.get("konfirmasi") != "HAPUS":
        raise Galat("Reset butuh konfirmasi.", 409)
    with _KUNCI_PROGRES:
        cadangan = progress.reset(bagian)
    return {"ok": True, "cadangan": cadangan or "", "bagian": bagian}
