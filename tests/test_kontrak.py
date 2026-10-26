"""Tes kontrak 41 endpoint: BENTUK jawaban API, bukan nilainya.

Kenapa ia ada, dan kenapa ia berbeda dari `test_web.py`.

`test_web.py` menguji APA yang dijawab server: skor kuis yang benar, materi
yang terkunci, isi yang sama di dua antarmuka. Yang TIDAK dijaganya satu hal
yang justru paling mudah rusak saat backend-nya diganti: **nama medan dan
tipenya**. Antarmuka React membaca empat puluh satu endpoint ini, dan satu
medan yang berganti nama tidak menghasilkan error di satu pun sisi -- ia
menghasilkan `undefined` yang digambar sebagai halaman kosong.

Empat hal yang membuat tes ini pagar, bukan daftar keinginan:

1. **Daftar endpointnya DITURUNKAN dari `server.RUTE`, tidak diketik.**
   Endpoint baru tanpa entri kontrak membuat tes ini MERAH dengan menyebut
   nama jalurnya. Daftar yang diketik tangan akan diam untuk endpoint ke-42,
   dan yang diam itu justru endpoint yang paling baru dan paling mungkin salah.

2. **Yang ditagih bentuk, bukan nilai.** `{"xp": 7}` dan `{"xp": 1200}`
   sama-sama sah; `{"xp": "7"}` tidak. Tes yang menagih nilai akan merah tiap
   kali kurikulumnya tumbuh, dan tes yang merah karena hal yang benar adalah
   tes yang mulai diabaikan.

3. **Kontraknya DISUSUN dari jawaban server sungguhan**, bukan dari ingatan
   siapa pun. Versi pertama tes ini ditulis dari dugaan, dan lima dari empat
   puluh satu endpointnya langsung menolak argumennya: `/api/kuis/mulai`
   memakai medan `sesi` (bukan `token`) dan mengirim SELURUH soal sekaligus,
   `/api/konfigurasi` menerima `{<kunci>: <nilai>}` langsung, dan
   `/api/data/impor` menuntut `{"progres": ...}`. Dugaan yang dipagari adalah
   dugaan yang dikukuhkan.

4. **Ia bisa diarahkan ke implementasi LAIN.** `BELAJAR_KONTRAK_URL` plus
   `BELAJAR_KONTRAK_TOKEN` membuat tes ini menembak server yang sudah berjalan
   di alamat mana pun -- dan itu seluruh gunanya untuk Tahap 2: endpoint yang
   dipindahkan ke Express bisa diadu dengan kontrak yang sama, satu per satu,
   sementara sisanya tetap dilayani Python.

Yang TIDAK diuji di sini: kode galat, pesan galat, dan penjagaan token.
Ketiganya sudah punya tempatnya di `test_web.TestPenjagaanServer`, dan dua
pagar untuk satu hal adalah dua pagar yang suatu hari berbeda pendapat.

Argumen yang butuh id nyata DICARI lewat API-nya sendiri, bukan dari modul
Python: materi mana yang punya blok kode, latihan mana yang tidak bisa dinilai
otomatis, contoh mana yang layak ditebak. Begitu tes ini diarahkan ke
implementasi lain, konteksnya pun datang dari implementasi itu.
"""

import json
import os
import tempfile
import threading
import unittest
import urllib.error
import urllib.parse
import urllib.request

from pelajar import konfigurasi
from pelajar import progress
from webapp import api, sesi
from webapp import catatan as modul_catatan
from webapp import server as modul_server


# --------------------------------------------------------------- pemeriksa

class Salah(Exception):
    """Bentuk yang tidak cocok, dengan jalur medannya di pesan."""


def _nama(t):
    if isinstance(t, tuple):
        return "|".join(_nama(x) for x in t)
    return getattr(t, "__name__", str(t))


def periksa(bentuk, nilai, jalan="hasil"):
    """Tagih `nilai` mengikuti `bentuk`. Melempar `Salah` dengan jalur medannya.

    Kosakata `bentuk` sengaja kecil -- kontrak yang butuh bahasa skema sendiri
    adalah kontrak yang berhenti dibaca:

    * tipe Python (`str`, `int`, `bool`, `dict`, `list`) atau tuple tipe
    * `dict`  -> tiap kunci WAJIB ada; kunci berakhiran `?` opsional
    * `[x]`   -> daftar yang SETIAP anggotanya mengikuti `x`
    * `None`  -> apa pun, termasuk `null`. Dipakai untuk medan yang bentuknya
                 memang bergantung isi (`galat` runner, `hadiah`, `posisi`)
    """
    if bentuk is None:
        return
    if isinstance(bentuk, dict):
        if not isinstance(nilai, dict):
            raise Salah(f"{jalan}: harus objek, dapat {type(nilai).__name__}")
        for kunci, sub in bentuk.items():
            opsional = kunci.endswith("?")
            k = kunci[:-1] if opsional else kunci
            if k not in nilai:
                if opsional:
                    continue
                raise Salah(f"{jalan}.{k}: medan HILANG")
            periksa(sub, nilai[k], f"{jalan}.{k}")
        return
    if isinstance(bentuk, list):
        if not isinstance(nilai, list):
            raise Salah(f"{jalan}: harus daftar, dapat {type(nilai).__name__}")
        # Daftar KOSONG lolos: "tidak ada bookmark" adalah keadaan sah, dan
        # menuntut satu anggota berarti tes ini cuma bisa jalan di profil yang
        # sudah dipakai. Yang dijaga bentuk tiap anggota kalau ia ada.
        for i, x in enumerate(nilai):
            periksa(bentuk[0], x, f"{jalan}[{i}]")
        return
    if isinstance(nilai, bool) and bentuk is not bool and bool not in (
            bentuk if isinstance(bentuk, tuple) else (bentuk,)):
        # `isinstance(True, int)` benar di Python, jadi tanpa penjaga ini
        # sebuah medan yang berubah dari angka jadi boolean lolos tanpa suara.
        raise Salah(f"{jalan}: harus {_nama(bentuk)}, dapat bool")
    if not isinstance(nilai, bentuk):
        raise Salah(f"{jalan}: harus {_nama(bentuk)}, "
                    f"dapat {type(nilai).__name__} ({nilai!r:.40})")


ANGKA = (int, float)

# ------------------------------------------------------------------ kontrak
#
# (metode, jalur) -> (argumen, bentuk)
#
# `argumen` boleh berupa dict tetap atau fungsi yang menerima konteks.

HADIAH = {"xp_tambah": int, "xp": int, "level": int, "naik_level": bool,
          "gelar": str, "gelar_baru": bool, "di_level": int,
          "butuh_level": int, "badge": [dict], "streak": int,
          "xp_hari_ini": int, "target_harian": int, "simpan_gagal": bool}

LANGKAH = {"tipe": str, "bahasa": str, "label_bahasa": str, "judul": str,
           "alasan": str, "indeks": int, "menit?": ANGKA}

HASIL_JALAN = {"sukses": bool, "keluaran": str, "galat": None,
               "kode_keluar": int, "fase": str, "timeout": bool,
               "catatan": str, "detik": ANGKA}

STAT_BAHASA = {"key": str, "label": str, "siap": bool, "materi": int,
               "total_materi": int, "persen": ANGKA}

OPSI_KONFIG = {"label": str, "jenis": str, "nilai": None, "bawaan": None,
               "pilihan": None, "minimum": None, "maksimum": None,
               "keterangan": str}

RINGKAS_DIRI = {"xp": int, "level": int, "gelar": str, "di_level": int,
                "butuh_level": int, "streak": int, "streak_rekor": int,
                "streak_total": int, "xp_hari_ini": int, "xp_kemarin": int,
                "hari_belajar_terakhir": None, "target_harian": int,
                "badge_dimiliki": int, "badge_total": int,
                "heatmap": [{"tanggal": str, "xp": int}],
                "bahasa": [STAT_BAHASA], "langkah": [LANGKAH],
                "tantangan": None, "kuis_jatuh_tempo": int, "posisi": None,
                "nama": str}

KONTRAK = {
    ("GET", "/api/awal"): ({}, {
        "versi": str, "versi_web": str, "karantina": [dict],
        "bahasa": [{"key": str, "label": str, "runner": str, "sorot": str,
                    "siap": bool, "materi": int, "kuis": int, "latihan": int,
                    "hilang": [str], "tematik": bool}],
        "aturan_sorot": dict,
        "aturan_bab": {"aturan": str, "pintu_darurat": str,
                       "tingkat": [{"nama": str, "label": str, "ket": str}]},
        "konfigurasi": dict,
        "lokasi": {"progres": str, "konfigurasi": str, "catatan": str,
                   "kerja": str},
        "batas": {"waktu": ANGKA, "memori_mb": ANGKA, "output": int}}),

    # Dasbor dan statistik berbagi SATU bentuk dasar, dan itu memang
    # kenyataannya: `api.statistik` mengembalikan `api.dasbor` plus medan
    # tambahan. Menuliskannya dua kali di sini akan membuat keduanya bisa
    # melenceng satu per satu.
    ("GET", "/api/dasbor"): ({}, {**RINGKAS_DIRI,
                                  "skor_kuis": {"benar": int, "maks": int},
                                  "catatan_jumlah": int}),
    ("GET", "/api/statistik"): ({}, RINGKAS_DIRI),

    ("GET", "/api/bahasa"): (lambda k: {"key": k["bahasa"]}, {
        "key": str, "label": str, "runner": str, "sorot": str, "siap": bool,
        "tebak": int, "hilang": [str], "pasang": str, "cara_jalan": [str],
        "catatan": str,
        "statistik": {"materi": int, "total_materi": int, "total_kuis": int,
                      "total_latihan": int, "persen": ANGKA},
        "materi": [{"indeks": int, "judul": str, "status": str, "bagian": int,
                    "bookmark": bool, "terkunci": bool, "tingkat": str}],
        "kuis": [{"indeks": int, "judul": str, "soal": int, "terbaik": int,
                  "percobaan": int, "total_soal": int, "pernah": bool,
                  "jatuh_tempo": bool, "bookmark": bool}],
        "latihan": [{"indeks": int, "judul": str, "tingkat": str,
                     "status": str, "dinilai": bool, "alasan": str,
                     "hint": int, "proyek": bool, "bookmark": bool}],
        "bab": [{"nomor": int, "judul": str, "tingkat": str,
                 "label_tingkat": str, "materi": [int], "selesai": int,
                 "jumlah": int, "status": str, "alasan": str,
                 "persen": ANGKA}],
        "bab_kalimat": str, "buka_semua_bab": bool,
        "pustaka": {"total": int, "per_jenis": [dict], "pembuka": [dict]}}),

    ("GET", "/api/materi"): (lambda k: {"key": k["bahasa"], "indeks": 0}, {
        "bahasa": str, "label_bahasa": str, "sorot": str, "indeks": int,
        "jumlah": int, "judul": str, "sebelum": str, "sesudah": str,
        "status": str, "bookmark": bool, "kunci": str,
        "catatan": {"teks": str, "diubah": str},
        "bab": {"nomor": int, "judul": str, "tingkat": str,
                "label_tingkat": str, "jumlah": int, "selesai": int},
        # Bagian punya DUA bentuk, dan itu kenyataan API-nya: bagian prosa
        # membawa `blok`, bagian berkode membawa `kode`/`token`/`sorot`. Yang
        # WAJIB di keduanya cuma `jenis` dan `judul`. Menuntut `blok` di
        # semuanya memerahkan materi python ke-0 di bagian kedua -- dan itu
        # memang cara tes ini menemukan bentuk yang benar.
        "bagian": [{"jenis": str, "judul": str, "blok?": [{"jenis": str}],
                    "kode?": str, "token?": list, "sorot?": str}]}),

    ("POST", "/api/materi/selesai"): (
        lambda k: {"key": k["bahasa"], "indeks": 0, "tuntas": False},
        {**HADIAH, "status": str, "kuis_siap": [dict]}),

    # Bagiannya DICARI, bukan 0: bagian pertama sebuah materi hampir selalu
    # prosa, dan endpoint ini menjawab 409 untuk bagian tanpa blok kode.
    ("GET", "/api/materi/contoh"): (
        lambda k: {"key": k["bahasa"], "indeks": k["materi_kode"][0],
                   "bagian": k["materi_kode"][1]},
        {"bahasa": str, "kode": str, "judul": str}),

    ("POST", "/api/kuis/mulai"): (
        lambda k: {"key": k["bahasa"], "indeks": 0, "mode": "biasa"},
        {"sesi": str, "judul": str, "bahasa": str, "bahasa_key": str,
         "label_bahasa": str, "indeks": int, "mode": str, "durasi": int,
         "total": int,
         # `options`, bukan `opsi`: satu-satunya medan berbahasa Inggris di
         # muatan kuis, dan ia sudah dipakai kedua antarmuka. Mengganti namanya
         # berarti dua antarmuka yang harus diubah bersamaan, jadi ia dibiarkan
         # apa adanya dan dicatat di sini.
         "soal": [{"nomor": int, "q": str, "options": [str]}]}),

    ("POST", "/api/kuis/jawab"): (
        lambda k: {"sesi": k["sesi_jawab"], "nomor": 0, "pilihan": 0},
        {"benar": bool, "jawaban_benar": int, "pilihanmu": int,
         "penjelasan": str, "terjawab": int, "total": int}),

    ("POST", "/api/kuis/selesai"): (
        lambda k: {"sesi": k["sesi_selesai"]},
        {**HADIAH, "sesi": str, "kategori": str, "judul": str, "mode": str,
         "sesi_penuh": bool, "benar": int, "total": int, "total_asli": int,
         "detik": ANGKA, "salah_asli": [int], "rincian": [dict]}),

    ("POST", "/api/kuis/batal"): (
        lambda k: {"sesi": k["sesi_batal"]}, {"ok": bool}),

    ("GET", "/api/latihan"): (lambda k: {"key": k["bahasa"], "indeks": 0}, {
        "bahasa": str, "label_bahasa": str, "runner": str, "sorot": str,
        "indeks": int, "jumlah": int, "judul": str, "tingkat": str,
        "proyek": bool, "soal": [str], "soal_blok": [{"jenis": str}],
        "hint": [str], "solusi": str, "token_solusi": [list], "setup": str,
        "token_setup": [dict], "stdin": str, "stdin_list": [str], "mode": str,
        "dinilai": bool, "alasan": str, "status": str, "kunci": str,
        "catatan": {"teks": str, "diubah": str}, "bookmark": bool}),

    ("GET", "/api/latihan/kerangka"): (
        lambda k: {"key": k["bahasa"], "indeks": 0}, {"kode": str}),

    ("POST", "/api/latihan/simpan"): (
        lambda k: {"key": k["bahasa"], "indeks": 0, "kode": "print(1)\n"},
        {"ok": bool, "path": str, "bita": int}),

    ("POST", "/api/latihan/jalankan"): (
        lambda k: {"key": k["bahasa"], "indeks": 0, "kode": "print(1)\n"},
        {**HASIL_JALAN, "stdin": str}),

    ("POST", "/api/latihan/periksa"): (
        lambda k: {"key": k["bahasa"], "indeks": 0, "kode": "print(1)\n"},
        {"bisa_dinilai": bool, "lulus": bool, "detik": ANGKA, "uji": [dict],
         "hadiah": None, "status": str}),

    # Latihannya DICARI: endpoint ini menolak 409 untuk latihan yang BISA
    # dinilai otomatis ("kerjakan lalu tekan Periksa, jangan ditandai manual").
    ("POST", "/api/latihan/manual"): (
        lambda k: {"key": k["latihan_manual"][0],
                   "indeks": k["latihan_manual"][1]},
        # Hadiahnya DITABURKAN di tingkat atas, bukan dibungkus `hadiah`
        # seperti `/api/latihan/periksa`. Dua bentuk untuk satu hal yang sama,
        # dan keduanya sudah dipakai -- jadi yang dikerjakan kontrak ini
        # mencatatnya, bukan merapikannya.
        {**HADIAH, "status": str}),

    ("POST", "/api/coba"): (
        {"bahasa": "python", "kode": "print(1)\n"},
        {**HASIL_JALAN, "bahasa": str, "berkas": str}),

    ("POST", "/api/jejak"): (
        {"kode": "x = 1\nprint(x)\n"},
        {"langkah": [dict], "galat": None, "baris_galat": None,
         "keluaran": str, "terpotong": bool, "timeout": bool}),

    ("GET", "/api/cari"): ({"q": "pointer", "tipe": "semua"}, {
        "kata": str, "tipe": str,
        "hasil": [{"tipe": str, "bahasa": str, "label_bahasa": str,
                   "indeks": int, "judul": str, "cuplikan": str,
                   # `terkunci` cuma ada di hasil bertipe materi: kuis dan
                   # latihan tidak pernah terkunci (penguncian hanya bacaan).
                   "terkunci?": bool, "skor": ANGKA}]}),

    ("GET", "/api/pustaka"): ({"q": "python"}, {
        "hasil": [{"url": str, "judul": str, "jenis": str, "bahasa": str}],
        "total": int, "semua": int, "halaman": int, "per_halaman": int,
        "segi": dict, "label": dict, "sumber": [dict]}),

    ("GET", "/api/karier"): ({}, {
        "rumpun": [dict], "jenjang": dict, "keahlian": dict,
        "profesi": [{"id": str, "nama": str, "kesiapan": ANGKA}]}),

    ("GET", "/api/karier/jalur"): (
        lambda k: {"dari": k["profesi"], "ke": k["profesi2"]},
        {"jalur": [str], "celah": [list]}),

    ("GET", "/api/karier/kuis"): ({}, {"hasil": [dict]}),

    ("GET", "/api/langit"): ({}, {
        "bahasa": [{"key": str, "label": str,
                    "materi": [{"judul": str, "status": str,
                                "terkunci": bool}]}],
        "profesi": [dict], "tujuan": None}),

    ("GET", "/api/laporan"): ({}, {"markdown": str}),

    ("GET", "/api/tebak/kartu"): (
        lambda k: {"key": k["bahasa"]},
        {"kartu": [dict], "layak": int, "siap": bool}),

    # Kodenya harus PERSIS salah satu contoh layak di materi itu; kode bebas
    # ditolak 409. Jadi kartunya diambil dari `/api/tebak/kartu` lebih dulu.
    ("POST", "/api/tebak"): (
        lambda k: k["tebakan"],
        {"benar": bool, "keluaran?": str, "galat?": None, "hadiah?": None,
         "beda?": None, "tebakanmu?": str}),

    ("GET", "/api/bookmark"): ({}, {
        "daftar": [{"tipe": str, "bahasa": str, "label_bahasa": str,
                    "indeks": int, "judul": str}],
        "basi": int}),

    ("POST", "/api/bookmark"): (
        lambda k: {"key": k["bahasa"], "tipe": "materi", "indeks": 0},
        {"bookmark": bool}),

    ("POST", "/api/bookmark/bersihkan"): ({}, {"dibuang": int}),

    ("GET", "/api/catatan"): (
        lambda k: {"kunci": k["kunci_catatan"]}, {"teks": str, "diubah": str}),

    ("POST", "/api/catatan"): (
        lambda k: {"kunci": k["kunci_catatan"], "teks": "catatan kontrak"},
        {"teks": str, "diubah": str}),

    ("GET", "/api/catatan/semua"): ({}, {
        "daftar": [{"kunci": str, "teks": str, "diubah": str, "tipe": str,
                    "bahasa": str, "label_bahasa": str, "indeks": int,
                    "judul": str, "basi": bool}]}),

    # Peta opsi, BUKAN `{opsi: [...]}`: tiap kunci setelan jadi kunci objeknya.
    ("GET", "/api/konfigurasi"): ({}, {"tema": OPSI_KONFIG,
                                       "target_xp_harian": OPSI_KONFIG}),

    # Muatannya `{<kunci>: <nilai>}` langsung, bukan `{kunci, nilai}`.
    ("POST", "/api/konfigurasi"): (
        {"target_xp_harian": 60},
        {"diubah": dict, "konfigurasi": dict}),

    ("POST", "/api/konfigurasi/bawaan"): ({}, {"konfigurasi": dict}),

    ("GET", "/api/data/ekspor"): ({}, {"progres": dict}),

    ("POST", "/api/data/cadangkan"): ({}, {"cadangan": str}),

    ("POST", "/api/data/impor"): (
        lambda k: {"progres": k["ekspor"]["progres"]},
        {"ok": bool, "cadangan": str}),

    # DIJALANKAN PALING AKHIR (lihat `_urut()`): ia menghapus progres, dan
    # endpoint lain di atas membaca progres itu.
    ("POST", "/api/data/reset"): (
        lambda k: {"bagian": k["bahasa"], "konfirmasi": "HAPUS"},
        {"ok": bool, "cadangan": str, "bagian": str}),
}


class TestKontrakApi(unittest.TestCase):
    """Empat puluh satu endpoint, satu pemeriksaan bentuk masing-masing."""

    @classmethod
    def setUpClass(cls):
        cls.dir = tempfile.TemporaryDirectory()
        d = cls.dir.name
        cls._simpan = {
            "progres": progress.PROGRESS_FILE,
            "progres_lama": progress.PROGRESS_FILE_LAMA,
            "konfig": konfigurasi.BERKAS,
            "catatan": modul_catatan.BERKAS,
            "kerja": api.exercises.DIR_KERJA,
        }
        # Keempat jalur dialihkan WALAU menembak server luar: tes ini menekan
        # `/api/data/reset` dan `/api/latihan/simpan`, dan satu jalur yang lupa
        # dialihkan menulis ke berkas pemiliknya sendiri.
        progress.PROGRESS_FILE = os.path.join(d, "progress.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(d, "tidak-ada.json")
        konfigurasi.BERKAS = os.path.join(d, "config.json")
        modul_catatan.BERKAS = os.path.join(d, "catatan.json")
        api.exercises.DIR_KERJA = os.path.join(d, "kerjaanku")
        konfigurasi.lupakan_cache()
        sesi.kosongkan()

        cls.luar = os.environ.get("BELAJAR_KONTRAK_URL")
        if cls.luar:
            cls.url = cls.luar.rstrip("/")
            cls.token = os.environ.get("BELAJAR_KONTRAK_TOKEN", "")
            cls.server = None
            return
        cls.server, cls.url = modul_server.buat(port=7802)
        cls.utas = threading.Thread(target=cls.server.serve_forever,
                                    daemon=True)
        cls.utas.start()
        cls.token = cls.server.token

    @classmethod
    def tearDownClass(cls):
        if cls.server:
            cls.server.shutdown()
            cls.server.server_close()
        progress.PROGRESS_FILE = cls._simpan["progres"]
        progress.PROGRESS_FILE_LAMA = cls._simpan["progres_lama"]
        konfigurasi.BERKAS = cls._simpan["konfig"]
        modul_catatan.BERKAS = cls._simpan["catatan"]
        api.exercises.DIR_KERJA = cls._simpan["kerja"]
        konfigurasi.lupakan_cache()
        sesi.kosongkan()
        cls.dir.cleanup()

    def minta(self, metode, jalur, arg):
        if metode == "GET":
            q = urllib.parse.urlencode(
                {k: v for k, v in arg.items() if v is not None})
            alamat = self.url + jalur + ("?" + q if q else "")
            data = None
        else:
            alamat = self.url + jalur
            data = json.dumps(arg).encode()
        kepala = {"X-Belajar-Token": self.token}
        if data is not None:
            kepala["Content-Type"] = "application/json"
        req = urllib.request.Request(alamat, data=data, headers=kepala,
                                     method=metode)
        try:
            with urllib.request.urlopen(req, timeout=120) as f:
                return f.status, json.loads(f.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            with e:
                return e.code, json.loads(e.read().decode() or "{}")

    def _wajib(self, metode, jalur, arg):
        """Panggil dan tuntut 200 -- dipakai saat MENYIAPKAN konteks.

        Kegagalan di sini bukan "kontrak bergeser" melainkan "penyiapannya
        salah", dan membedakan keduanya di pesan jauh lebih murah daripada
        membacanya dari jejak tumpukan.
        """
        kode, isi_ = self.minta(metode, jalur, arg)
        self.assertEqual(kode, 200, f"penyiapan {metode} {jalur} -> {kode}: "
                                    f"{json.dumps(isi_)[:300]}")
        return isi_

    def _konteks(self):
        """Nilai nyata untuk endpoint yang butuh id.

        Semuanya DICARI lewat API, bukan dari modul Python: materi mana yang
        punya blok kode, latihan mana yang tidak bisa dinilai otomatis, contoh
        mana yang layak ditebak. Begitu tes ini diarahkan ke implementasi lain,
        konteksnya pun datang dari implementasi itu.
        """
        kunci = "python"
        bahasa = self._wajib("GET", "/api/bahasa", {"key": kunci})

        # Materi yang punya blok kode: dicari dari bagian pertama yang
        # jawabannya 200, bukan ditebak.
        materi_kode = None
        for m in bahasa["materi"][:8]:
            if m["terkunci"]:
                continue
            for b in range(m["bagian"]):
                kode, _ = self.minta("GET", "/api/materi/contoh",
                                     {"key": kunci, "indeks": m["indeks"],
                                      "bagian": b})
                if kode == 200:
                    materi_kode = (m["indeks"], b)
                    break
            if materi_kode:
                break
        self.assertIsNotNone(materi_kode,
                             "tidak ada satu pun bagian materi berblok kode "
                             "di delapan materi pertama -- penyiapan salah, "
                             "bukan kontrak yang bergeser")

        # Latihan yang TIDAK dinilai otomatis. Ada tujuh di seluruh kurikulum
        # (Java 2, SQL 3, Python 1, JS 1), jadi beberapa bahasa disisir.
        manual = None
        for kb in (kunci, "java", "sql", "javascript"):
            b = self._wajib("GET", "/api/bahasa", {"key": kb})
            for e in b["latihan"]:
                if not e["dinilai"]:
                    manual = (kb, e["indeks"])
                    break
            if manual:
                break
        self.assertIsNotNone(manual, "tidak ada latihan tanpa nilai otomatis")

        # Kartu tebak: kodenya harus PERSIS contoh layak di materinya, DAN
        # materinya harus sudah dibaca TUNTAS -- `pelajar/tebak.py` cuma
        # menawarkan contoh dari materi yang sudah selesai. Di profil baru
        # daftarnya kosong, dan kartu kosong berarti `/api/tebak` dilewati
        # tanpa pernah diperiksa. Jadi satu materi dibaca lebih dulu, di sini,
        # dengan sengaja.
        self._wajib("POST", "/api/materi/selesai",
                    {"key": kunci, "indeks": materi_kode[0], "tuntas": True})
        kartu = self._wajib("GET", "/api/tebak/kartu", {"key": kunci})
        tebakan = None
        if kartu["kartu"]:
            k0 = kartu["kartu"][0]
            tebakan = {"key": kunci, "indeks": k0["indeks"],
                       "kode": k0["kode"], "tebakan": "tebakan kontrak"}

        profesi = [p["id"] for p in
                   self._wajib("GET", "/api/karier", {})["profesi"]]
        self.assertGreaterEqual(len(profesi), 2)

        m0 = self._wajib("GET", "/api/materi", {"key": kunci, "indeks": 0})
        ekspor = self._wajib("GET", "/api/data/ekspor", {})

        # Tiga sesi kuis: satu untuk dijawab, satu untuk diselesaikan, satu
        # untuk dibatalkan. Sesi yang dipakai dua endpoint berarti urutan
        # pemanggilan ikut jadi bagian kontrak -- dan ia bukan.
        sesi_ = {}
        for nama, indeks in (("sesi_jawab", 0), ("sesi_selesai", 1),
                             ("sesi_batal", 2)):
            m = self._wajib("POST", "/api/kuis/mulai",
                            {"key": kunci, "indeks": indeks, "mode": "biasa"})
            sesi_[nama] = m["sesi"]
            if nama == "sesi_selesai":
                # `/api/kuis/selesai` menolak sesi yang belum dijawab habis,
                # dan 400 di situ akan terbaca sebagai kontrak yang rusak.
                for soal in m["soal"]:
                    self._wajib("POST", "/api/kuis/jawab",
                                {"sesi": m["sesi"], "nomor": soal["nomor"],
                                 "pilihan": 0})
        return {"bahasa": kunci, "materi_kode": materi_kode,
                "latihan_manual": manual, "tebakan": tebakan,
                "profesi": profesi[0], "profesi2": profesi[1],
                "kunci_catatan": m0["kunci"], "ekspor": ekspor, **sesi_}

    def test_setiap_rute_punya_kontrak(self):
        """Endpoint baru tanpa entri kontrak MERAH, dengan menyebut jalurnya.

        Ini penjaga yang membuat tes di bawah berarti. Tanpa dia, endpoint
        ke-42 bisa lahir tanpa satu pun pemeriksaan bentuk -- dan ia justru
        yang paling baru dan paling mungkin salah.
        """
        rute = set(modul_server.RUTE)
        kontrak = set(KONTRAK)
        kurang = sorted(f"{m} {j}" for m, j in rute - kontrak)
        lebih = sorted(f"{m} {j}" for m, j in kontrak - rute)
        self.assertEqual(kurang, [], "rute tanpa kontrak: " + ", ".join(kurang))
        self.assertEqual(lebih, [], "kontrak tanpa rute: " + ", ".join(lebih))
        self.assertEqual(len(rute), 41,
                         f"jumlah endpoint berubah ({len(rute)}). Kalau itu "
                         "memang disengaja, perbarui angkanya DI SINI supaya "
                         "pertumbuhannya terlihat di riwayat.")

    @staticmethod
    def _urut(butir):
        """`/api/data/reset` dan `/api/data/impor` paling akhir.

        Keduanya MENGGANTI seluruh progres, dan endpoint lain membaca progres
        itu. Tanpa pengurutan ini, tesnya lulus atau gagal tergantung urutan
        iterasi dict -- dan itu urutan yang kebetulan, bukan yang dipilih.
        """
        metode, jalur = butir[0]
        akhir = jalur in ("/api/data/impor", "/api/data/reset")
        return (1 if akhir else 0, jalur, metode)

    def test_bentuk_jawaban_setiap_endpoint(self):
        k = self._konteks()
        diperiksa = 0
        for (metode, jalur), (arg, bentuk) in sorted(KONTRAK.items(),
                                                     key=self._urut):
            with self.subTest(endpoint=f"{metode} {jalur}"):
                nyata = arg(k) if callable(arg) else dict(arg)
                if nyata is None:
                    self.skipTest(f"{jalur}: tidak ada data untuk mengujinya "
                                  "di profil ini")
                kode, isi_ = self.minta(metode, jalur, nyata)
                self.assertEqual(
                    kode, 200,
                    f"{metode} {jalur} -> {kode}: {json.dumps(isi_)[:300]}")
                try:
                    periksa(bentuk, isi_)
                except Salah as e:
                    self.fail(f"{metode} {jalur} bentuknya bergeser -- {e}")
                diperiksa += 1
        # Lantai populasi: tanpa ini, sebuah bug di `_urut` atau `_konteks` yang
        # membuat seluruh perulangan dilewati tetap melapor hijau.
        self.assertGreaterEqual(diperiksa, 41,
                                f"cuma {diperiksa} endpoint yang benar-benar "
                                "diperiksa")


if __name__ == "__main__":
    unittest.main()
