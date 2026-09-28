"""Tes antarmuka web: keamanan server, endpoint JSON, sesi kuis, dan catatan.

Tiga hal dijaga paling ketat di sini, dan ketiganya adalah hal yang kalau rusak
tidak akan terlihat sampai terlambat:

1. **Penjagaan server.** Endpoint di sini MENJALANKAN KODE. Begitu penjagaan
   tokennya bocor, halaman web mana pun yang kebetulan terbuka di browser yang
   sama bisa memanggilnya. Tesnya menembak dari sudut penyerang, bukan dari
   sudut pemakai.

2. **Pemetaan ulang jawaban kuis.** Opsi diacak sebelum dikirim ke browser.
   Kalau index jawaban benarnya tidak ikut dipetakan, kuis akan menandai
   jawaban benar sebagai salah -- bug yang membuat pelajar meragukan dirinya
   sendiri, bukan aplikasinya. Diuji dengan mengerjakan SELURUH kuis di SEMUA
   bahasa memakai jawaban yang benar, lalu menuntut skornya sempurna.

3. **Penyorot JavaScript identik dengan Python.** Ada dua implementasi pemindai
   token: sorot.py dan statik/js/sorot.js. Keduanya diadu memakai seluruh kode
   di kurikulum. Kalau Node tidak terpasang, tesnya dilaporkan sebagai skipped
   -- bukan lulus diam-diam.

4. **Mesin gerak.** statik/js/gerak.js memuat solver pegas: matematika murni
   yang menentukan berapa lama SETIAP animasi di aplikasi ini berjalan. Salah
   satu tanda kurang di situ tidak menghasilkan error apa pun -- ia cuma
   menghasilkan animasi yang salah, dan "terasa aneh" bukan sesuatu yang bisa
   dilacak balik ke sebuah rumus enam bulan kemudian. Karena itu solvernya
   diadu dengan sifat-sifat yang HARUS berlaku, bukan dengan angka yang
   kebetulan keluar hari ini.
"""

import datetime
import json
import os
import re
import shutil
import subprocess
import tempfile
import threading
import unittest
import urllib.error
import urllib.request
from datetime import date

from pelajar import bab
from pelajar import konfigurasi
from pelajar import progress
from webapp import api, isi, sesi
from webapp import catatan as modul_catatan
from webapp import server as modul_server

LEWATI_LAMBAT = os.environ.get("BELAJAR_SKIP_LAMBAT") == "1"


def _bahasa(key):
    """Entri LANGUAGES berdasarkan KEY, bukan berdasarkan posisinya.

    Tes-tes di bawah mengirim `{"key": "java"}` ke API lalu memeriksa judul
    yang diambil dari daftar bahasa. Selama Java kebetulan berdiri paling
    depan, `LANGUAGES[0]` memberi jawaban yang benar — dan begitu urutan
    daftarnya berubah, tesnya bukan cuma gagal melainkan gagal dengan pesan
    yang menyesatkan: "kunci java_kuis::Kuis 1: Dasar HTML tidak ditemukan".
    Memilih berdasarkan key membuat tesnya menguji apa yang memang
    dimaksudkan, apa pun urutan daftarnya nanti.
    """
    for lang in api.LANGUAGES:
        if lang["key"] == key:
            return lang
    raise AssertionError(f"bahasa '{key}' tidak ada di LANGUAGES")


def _urai(badan):
    """Balasan JSON jadi objek; balasan lain (CSS, JS, HTML) jadi teks apa adanya."""
    try:
        return json.loads(badan or b"null")
    except (json.JSONDecodeError, UnicodeDecodeError):
        return badan.decode("utf-8", errors="replace")


class BasisWeb(unittest.TestCase):
    """Arahkan SEMUA berkas pengguna ke direktori sementara.

    Termasuk direktori kerja: tanpa itu, tes yang menekan "simpan" akan menulis
    ke ~/belajar-ngoding/kerjaanku milik pengguna sungguhan dan menimpa
    jawabannya sendiri.
    """

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        d = self.dir.name

        self._simpan = {
            "progres": progress.PROGRESS_FILE,
            "progres_lama": progress.PROGRESS_FILE_LAMA,
            "konfig": konfigurasi.BERKAS,
            "catatan": modul_catatan.BERKAS,
            "kerja": api.exercises.DIR_KERJA,
        }
        progress.PROGRESS_FILE = os.path.join(d, "progress.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(d, "tidak-ada.json")
        konfigurasi.BERKAS = os.path.join(d, "config.json")
        modul_catatan.BERKAS = os.path.join(d, "catatan.json")
        api.exercises.DIR_KERJA = os.path.join(d, "kerjaanku")
        konfigurasi.lupakan_cache()
        sesi.kosongkan()

    def tearDown(self):
        progress.PROGRESS_FILE = self._simpan["progres"]
        progress.PROGRESS_FILE_LAMA = self._simpan["progres_lama"]
        konfigurasi.BERKAS = self._simpan["konfig"]
        modul_catatan.BERKAS = self._simpan["catatan"]
        api.exercises.DIR_KERJA = self._simpan["kerja"]
        konfigurasi.lupakan_cache()
        sesi.kosongkan()
        self.dir.cleanup()


# -------------------------------------------------------------------- server

class TestPenjagaanServer(BasisWeb):
    """Setiap tes di sini adalah satu cara menyusup yang harus gagal."""

    @classmethod
    def setUpClass(cls):
        cls.server, cls.url = modul_server.buat(port=7801)
        cls.utas = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.utas.start()
        cls.token = cls.server.token

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def minta(self, jalur, token=None, metode="GET", muatan=None, kepala=None):
        data = json.dumps(muatan).encode() if muatan is not None else None
        h = dict(kepala or {})
        if token:
            h["X-Belajar-Token"] = token
        if data is not None:
            h["Content-Type"] = "application/json"
        req = urllib.request.Request(self.url.rstrip("/") + jalur, data=data,
                                     headers=h, method=metode)
        try:
            with urllib.request.urlopen(req, timeout=30) as f:
                return f.status, _urai(f.read())
        except urllib.error.HTTPError as e:
            # HTTPError memegang soket; tanpa close() Python meneriakkan
            # ResourceWarning di tengah keluaran tes.
            with e:
                return e.code, _urai(e.read())

    def test_api_tanpa_token_ditolak(self):
        kode, isi_ = self.minta("/api/dasbor")
        self.assertEqual(kode, 403)
        self.assertIn("Token", isi_["galat"])

    def test_api_dengan_token_salah_ditolak(self):
        kode, _ = self.minta("/api/dasbor", token="salah-sekali")
        self.assertEqual(kode, 403)

    def test_endpoint_yang_menjalankan_kode_juga_dijaga(self):
        """Yang paling penting: tanpa token, kode tidak boleh bisa dijalankan."""
        kode, _ = self.minta("/api/coba", metode="POST",
                             muatan={"bahasa": "python", "kode": "print(1)"})
        self.assertEqual(kode, 403)

    def test_origin_asing_ditolak(self):
        """Situs lain di browser yang sama tidak boleh bisa memanggil API."""
        kode, _ = self.minta("/api/dasbor", token=self.token,
                             kepala={"Origin": "https://situs-jahat.example"})
        self.assertEqual(kode, 403)

    def test_host_asing_ditolak(self):
        """Penutup serangan DNS rebinding."""
        kode, _ = self.minta("/api/dasbor", token=self.token,
                             kepala={"Host": "rebind.example.com"})
        self.assertEqual(kode, 403)

    def test_origin_localhost_diterima(self):
        kode, _ = self.minta("/api/dasbor", token=self.token,
                             kepala={"Origin": "http://127.0.0.1:7801"})
        self.assertEqual(kode, 200)

    def test_halaman_utama_tidak_butuh_token(self):
        """Kalau halamannya sendiri butuh token, tidak ada cara memulai."""
        with urllib.request.urlopen(self.url, timeout=10) as f:
            self.assertEqual(f.status, 200)
            self.assertIn("Belajar Ngoding", f.read().decode())

    def test_token_ditanam_ke_halaman(self):
        with urllib.request.urlopen(self.url, timeout=10) as f:
            html = f.read().decode()
        self.assertIn(self.token, html)
        self.assertNotIn("{{TOKEN}}", html)

    def test_path_traversal_ditolak(self):
        for jahat in ["/../../etc/passwd", "/js/../../../etc/passwd",
                      "/%2e%2e/%2e%2e/etc/passwd"]:
            kode, _ = self.minta(jahat)
            self.assertIn(kode, (403, 404), f"{jahat} tidak ditolak")

    def test_berkas_statik_tersaji(self):
        for jalur in ["/gaya.css", "/js/aplikasi.js", "/js/sorot.js"]:
            kode, _ = self.minta(jalur)
            self.assertEqual(kode, 200, jalur)

    def test_endpoint_tak_dikenal_404(self):
        kode, _ = self.minta("/api/tidak-ada", token=self.token)
        self.assertEqual(kode, 404)

    def test_post_ke_berkas_statik_ditolak(self):
        kode, _ = self.minta("/gaya.css", metode="POST", muatan={})
        self.assertEqual(kode, 405)

    def test_muatan_bukan_json_ditolak_dengan_rapi(self):
        req = urllib.request.Request(
            self.url.rstrip("/") + "/api/coba", data=b"bukan json",
            headers={"X-Belajar-Token": self.token,
                     "Content-Type": "application/json"}, method="POST")
        try:
            urllib.request.urlopen(req, timeout=10).close()
            self.fail("muatan rusak seharusnya ditolak")
        except urllib.error.HTTPError as e:
            with e:
                self.assertEqual(e.code, 400)

    def test_bind_selain_loopback_ditolak(self):
        """Menyalakan di 0.0.0.0 membuka eksekusi kode ke seluruh jaringan."""
        with self.assertRaises(ValueError):
            modul_server.buat(host="0.0.0.0", port=7802)


# ------------------------------------------------------------------ endpoint

class TestEndpoint(BasisWeb):
    def test_awal_memuat_semua_yang_dibutuhkan_halaman(self):
        a = api.awal()
        self.assertEqual(len(a["bahasa"]), len(api.LANGUAGES))
        self.assertIn("java", a["aturan_sorot"])
        self.assertIn("progres", a["lokasi"])
        for b in a["bahasa"]:
            for kunci in ("key", "label", "runner", "sorot", "siap", "persen"):
                self.assertIn(kunci, b)

    def test_dasbor_konsisten_dengan_progres_kosong(self):
        d = api.dasbor()
        self.assertEqual(d["xp"], 0)
        self.assertEqual(d["level"], 1)
        self.assertEqual(len(d["heatmap"]), 7 * 26)
        self.assertEqual(d["heatmap"][-1]["tanggal"], date.today().isoformat())

    def test_statistik_memisahkan_gelar_kini_dari_tangga_gelar(self):
        """Dua arti berbeda tidak boleh berbagi satu kunci JSON."""
        s = api.statistik()
        self.assertIsInstance(s["gelar"], str)
        self.assertIsInstance(s["tangga_gelar"], list)
        self.assertEqual(len(s["semua_badge"]), len(progress.DAFTAR_BADGE))

    def test_bahasa_tidak_dikenal_404(self):
        with self.assertRaises(api.Galat) as c:
            api.bahasa({"key": "kobol"})
        self.assertEqual(c.exception.kode, 404)

    def test_indeks_di_luar_jangkauan_404(self):
        with self.assertRaises(api.Galat) as c:
            api.materi({"key": "java", "indeks": "9999"})
        self.assertEqual(c.exception.kode, 404)

    def test_indeks_bukan_angka_400(self):
        with self.assertRaises(api.Galat) as c:
            api.materi({"key": "java", "indeks": "abc"})
        self.assertEqual(c.exception.kode, 400)

    def test_materi_memuat_token_dan_petunjuk_berkas(self):
        m = api.materi({"key": "java", "indeks": "0"})
        kode = [b for b in m["bagian"] if b["jenis"] == "kode"]
        self.assertTrue(kode, "materi Java pertama seharusnya punya contoh kode")
        for b in kode:
            self.assertEqual("".join(t[1] for t in b["token"]), b["kode"])
            self.assertIn(b["petunjuk"]["jenis"],
                          ("program", "potongan", "sesi", "multi", "ilustrasi"))

    def test_materi_selesai_memberi_xp_sekali_saja(self):
        r1 = api.materi_selesai({"key": "java", "indeks": 0, "tuntas": True})
        self.assertEqual(r1["xp_tambah"], progress.XP_MATERI)
        r2 = api.materi_selesai({"key": "java", "indeks": 0, "tuntas": True})
        self.assertEqual(r2["xp_tambah"], 0)

    def test_materi_sebagian_tidak_memberi_xp(self):
        r = api.materi_selesai({"key": "java", "indeks": 1, "tuntas": False})
        self.assertEqual(r["xp_tambah"], 0)
        self.assertEqual(r["status"], "sebagian")
        judul = _bahasa("java")["materials"][1]["title"]
        self.assertIn(progress.kunci("java_materi", judul),
                      progress.load_progress()["materi_sebagian"])

    def test_bookmark_bolak_balik(self):
        r1 = api.bookmark_ubah({"key": "java", "tipe": "materi", "indeks": 0})
        self.assertTrue(r1["bookmark"])
        self.assertEqual(len(api.bookmark_daftar()["daftar"]), 1)
        r2 = api.bookmark_ubah({"key": "java", "tipe": "materi", "indeks": 0})
        self.assertFalse(r2["bookmark"])
        self.assertEqual(api.bookmark_daftar()["daftar"], [])

    def test_bookmark_tipe_ngawur_ditolak(self):
        with self.assertRaises(api.Galat):
            api.bookmark_ubah({"key": "java", "tipe": "resep", "indeks": 0})

    def test_bookmark_basi_dilaporkan_dan_bisa_dibersihkan(self):
        d = progress.load_progress()
        d["bookmark"].append("java_materi::Materi Yang Sudah Dihapus")
        progress.save_progress(d)
        self.assertEqual(api.bookmark_daftar()["basi"], 1)
        self.assertEqual(api.bookmark_bersihkan()["dibuang"], 1)
        self.assertEqual(api.bookmark_daftar()["basi"], 0)

    def test_cari_menemukan_dan_membawa_cuplikan(self):
        h = api.cari({"q": "variabel"})["hasil"]
        self.assertTrue(h)
        self.assertTrue(any(x["cuplikan"] for x in h))
        for x in h:
            self.assertIn(x["tipe"], ("materi", "kuis", "latihan"))

    def test_cari_satu_huruf_tidak_membanjiri(self):
        self.assertEqual(api.cari({"q": "a"})["hasil"], [])

    def test_reset_butuh_konfirmasi(self):
        with self.assertRaises(api.Galat) as c:
            api.data_reset({"bagian": "semua"})
        self.assertEqual(c.exception.kode, 409)

    def test_reset_bahasa_tidak_menyentuh_bahasa_lain(self):
        api.materi_selesai({"key": "java", "indeks": 0, "tuntas": True})
        api.materi_selesai({"key": "python", "indeks": 0, "tuntas": True})
        api.data_reset({"bagian": "java", "konfirmasi": "HAPUS"})
        d = progress.load_progress()
        self.assertFalse([k for k in d["materi_dibaca"] if k.startswith("java_")])
        self.assertTrue([k for k in d["materi_dibaca"] if k.startswith("python_")])

    def test_konfigurasi_menolak_opsi_khusus_terminal(self):
        """Mengubah lebar terminal dari browser tidak berefek apa pun."""
        with self.assertRaises(api.Galat):
            api.konfigurasi_tulis({"lebar": 200})

    def test_konfigurasi_menyimpan_nilai_sah(self):
        api.konfigurasi_tulis({"target_xp_harian": 90})
        self.assertEqual(konfigurasi.ambil("target_xp_harian"), 90)

    def test_laporan_berbentuk_markdown(self):
        teks = api.laporan()["markdown"]
        self.assertIn("# Laporan Kemajuan", teks)
        self.assertIn("| Bahasa |", teks)

    def test_ekspor_impor_bolak_balik(self):
        api.materi_selesai({"key": "java", "indeks": 0, "tuntas": True})
        cadangan = api.data_ekspor()["progres"]
        api.data_reset({"bagian": "semua", "konfirmasi": "HAPUS"})
        self.assertEqual(progress.load_progress()["xp"], 0)
        api.data_impor({"progres": cadangan})
        self.assertEqual(progress.load_progress()["xp"], progress.XP_MATERI)

    def test_impor_isi_ngawur_ditolak(self):
        with self.assertRaises(api.Galat):
            api.data_impor({"progres": "bukan dict"})


# ------------------------------------------------------------------- catatan

class TestFieldPembandingDasbor(BasisWeb):
    """Dua field read-only di `/api/dasbor`, dan semantik "kemarin" milik server.

    Keduanya menjawab satu pertanyaan tampilan ("38 XP itu banyak atau sedikit
    bagiku", "kapan terakhir aku belajar") tanpa memindahkan satu pun keputusan
    ke JavaScript. Yang dijaga di sini justru batasnya:

      · `xp_kemarin` dan `hari_belajar_terakhir` punya nilai netral yang jelas
        untuk profil yang masih kosong, jadi layar tidak perlu menebak.
      · `riwayat_harian(d, 2)[0]` benar-benar hari KEMARIN. Kalau urutannya
        terbalik suatu hari, "naik 26" berubah jadi "turun 26" tanpa satu pun
        tes lain yang merah -- dan itu angka yang dibaca pelajar tiap hari.
    """

    def test_profil_kosong_memberi_nilai_netral(self):
        d = api.dasbor()
        self.assertEqual(d["xp_kemarin"], 0)
        self.assertEqual(d["hari_belajar_terakhir"], "")

    def test_riwayat_indeks_nol_adalah_kemarin(self):
        data = progress.load_progress()
        kemarin = (datetime.date.today() - datetime.timedelta(days=1)).isoformat()
        self.assertEqual(progress.riwayat_harian(data, 2)[0][0], kemarin)

    def test_xp_kemarin_benar_benar_mengambil_hari_kemarin(self):
        """Bukan cuma semantik riwayatnya -- indeks yang DIPAKAI api.dasbor().

        Menguji `riwayat_harian` saja tidak cukup: indeks yang tertukar di
        api.py membuat "naik 26" berubah jadi "turun 26" tanpa satu pun tes
        lain merah. Dua hari diberi nilai yang berbeda supaya tertukarnya
        ketahuan.
        """
        hari = datetime.date.today()
        kemarin = (hari - datetime.timedelta(days=1)).isoformat()
        # Profil uji masih kosong dan berkasnya belum ada, jadi ditulis dari
        # nol; load_progress() yang menormalkan sisanya.
        with open(progress.PROGRESS_FILE, "w", encoding="utf-8") as f:
            json.dump({"riwayat_harian": {kemarin: {"xp": 12},
                                          hari.isoformat(): {"xp": 38}}}, f)

        d = api.dasbor()
        self.assertEqual(d["xp_kemarin"], 12, "xp_kemarin mengambil hari yang salah")
        self.assertEqual(d["xp_hari_ini"], 38)

    def test_hari_belajar_terakhir_ikut_streak_bukan_xp(self):
        """Membaca materi tanpa menuntaskannya: streak hidup, XP tetap nol.

        Inilah kasus yang membuat kesimpulan "hari ber-XP terakhir" salah:
        harinya tidak punya entri riwayat sama sekali, jadi tebakan dari
        heatmap akan bilang "belum pernah belajar" sementara streak-nya hidup.
        """
        progress.record_material_read("python_materi", "Contoh Uji", tuntas=False)
        data = progress.load_progress()
        hari_ini = datetime.date.today().isoformat()

        self.assertEqual(progress.streak_aktif(data), 1)
        self.assertEqual(progress.xp_hari_ini(data), 0)
        self.assertEqual(api.dasbor()["hari_belajar_terakhir"], hari_ini)


class TestCatatan(BasisWeb):
    def test_tulis_lalu_baca(self):
        api.catatan_tulis({"kunci": "java_materi::A", "teks": "ingat: ini penting"})
        self.assertEqual(api.catatan_ambil({"kunci": "java_materi::A"})["teks"],
                         "ingat: ini penting")

    def test_mengosongkan_menghapus_entrinya(self):
        api.catatan_tulis({"kunci": "java_materi::A", "teks": "x"})
        api.catatan_tulis({"kunci": "java_materi::A", "teks": "   "})
        self.assertEqual(modul_catatan.jumlah(), 0)

    def test_kunci_tanpa_pemisah_ditolak(self):
        with self.assertRaises(api.Galat):
            api.catatan_tulis({"kunci": "tanpa-pemisah", "teks": "x"})

    def test_reset_progres_TIDAK_menghapus_catatan(self):
        """Ini alasan utama catatan tinggal di berkasnya sendiri."""
        judul = _bahasa("java")["materials"][0]["title"]
        api.catatan_tulis({"kunci": f"java_materi::{judul}", "teks": "tulisanku"})
        api.materi_selesai({"key": "java", "indeks": 0, "tuntas": True})
        api.data_reset({"bagian": "semua", "konfirmasi": "HAPUS"})
        self.assertEqual(progress.load_progress()["xp"], 0)
        self.assertEqual(modul_catatan.jumlah(), 1)

    def test_berkas_rusak_tidak_menjatuhkan_aplikasi(self):
        with open(modul_catatan.BERKAS, "w", encoding="utf-8") as f:
            f.write("{ini bukan json")
        self.assertEqual(modul_catatan.semua(), [])

    def test_catatan_terlalu_panjang_dipotong(self):
        hasil = modul_catatan.tulis("a::b", "x" * 50_000)
        self.assertEqual(len(hasil["teks"]), modul_catatan.MAKS_PANJANG)

    def test_bentuk_lama_berupa_teks_polos_tetap_terbaca(self):
        with open(modul_catatan.BERKAS, "w", encoding="utf-8") as f:
            json.dump({"versi": 1, "catatan": {"a::b": "tulisan lama"}}, f)
        self.assertEqual(modul_catatan.ambil("a::b")["teks"], "tulisan lama")


# ---------------------------------------------------------------------- kuis

class TestSesiKuis(BasisWeb):
    def test_jawaban_benar_dinilai_benar_di_seluruh_kurikulum(self):
        """Pertahanan utama terhadap bug pemetaan-ulang index jawaban.

        Setiap kuis di setiap bahasa dikerjakan dengan jawaban yang benar.
        Skornya wajib sempurna. Kalau pengacakan opsi pernah lupa memetakan
        ulang index jawabannya, tes ini gagal di kuis pertama.
        """
        for lang in api.LANGUAGES:
            for i, q in enumerate(lang["quizzes"]):
                s = api.kuis_mulai({"key": lang["key"], "indeks": i, "acak": True})
                obj = sesi.ambil(s["sesi"])
                for nomor, soal in enumerate(obj.soal):
                    hasil = api.kuis_jawab({"sesi": s["sesi"], "nomor": nomor,
                                            "pilihan": soal["jawab"]})
                    self.assertTrue(hasil["benar"],
                                    f"{lang['key']} kuis {i} soal {nomor}")
                akhir = api.kuis_selesai({"sesi": s["sesi"]})
                self.assertEqual(akhir["benar"], akhir["total"],
                                 f"{lang['key']} / {q['title']}")

    def test_opsi_teracak_tetap_memuat_semua_pilihan(self):
        lang = _bahasa("java")
        s = api.kuis_mulai({"key": lang["key"], "indeks": 0, "acak": True})
        obj = sesi.ambil(s["sesi"])
        asli = {soal["q"]: sorted(soal["options"])
                for soal in lang["quizzes"][0]["questions"]}
        for soal in obj.soal:
            self.assertEqual(sorted(soal["options"]), asli[soal["q"]])

    def test_soal_yang_dikirim_tidak_memuat_kunci_jawaban(self):
        s = api.kuis_mulai({"key": "java", "indeks": 0})
        mentah = json.dumps(s)
        self.assertNotIn("jawab", mentah)
        self.assertNotIn("penjelasan", mentah)
        for soal in s["soal"]:
            self.assertEqual(set(soal), {"nomor", "q", "options"})

    def test_jawaban_pertama_yang_dikunci(self):
        """Klik dua kali tidak boleh diam-diam memperbaiki jawaban salah."""
        s = api.kuis_mulai({"key": "java", "indeks": 0, "acak": False})
        obj = sesi.ambil(s["sesi"])
        benar = obj.soal[0]["jawab"]
        salah = (benar + 1) % len(obj.soal[0]["options"])
        api.kuis_jawab({"sesi": s["sesi"], "nomor": 0, "pilihan": salah})
        kedua = api.kuis_jawab({"sesi": s["sesi"], "nomor": 0, "pilihan": benar})
        self.assertFalse(kedua["benar"])

    def test_skor_dan_jadwal_ulang_tercatat(self):
        s = api.kuis_mulai({"key": "java", "indeks": 0, "acak": False})
        obj = sesi.ambil(s["sesi"])
        for nomor, soal in enumerate(obj.soal):
            api.kuis_jawab({"sesi": s["sesi"], "nomor": nomor,
                            "pilihan": soal["jawab"]})
        r = api.kuis_selesai({"sesi": s["sesi"]})
        self.assertEqual(r["terbaik"], r["total"])
        self.assertTrue(r["jadwal"], "kuis sempurna tetap harus dijadwalkan ulang")
        self.assertEqual(r["salah_tersisa"], 0)
        self.assertGreater(r["xp_tambah"], progress.XP_BONUS_KUIS_SEMPURNA)

    def test_mode_ulangan_tidak_menyentuh_skor_terbaik(self):
        lang = _bahasa("java")
        judul = lang["quizzes"][0]["title"]
        s = api.kuis_mulai({"key": "java", "indeks": 0, "acak": False})
        obj = sesi.ambil(s["sesi"])
        for nomor, soal in enumerate(obj.soal):
            api.kuis_jawab({"sesi": s["sesi"], "nomor": nomor,
                            "pilihan": soal["jawab"]})
        api.kuis_selesai({"sesi": s["sesi"]})
        k = progress.kunci("java_kuis", judul)
        terbaik = progress.load_progress()["kuis_skor"][k]["terbaik"]

        # Buat satu soal jadi "masih salah" supaya ada bahan untuk diulang.
        progress.perbarui_soal_salah("java_kuis", judul, [0])
        u = api.kuis_mulai({"key": "java", "indeks": 0, "mode": "salah"})
        self.assertEqual(u["total"], 1)
        objU = sesi.ambil(u["sesi"])
        api.kuis_jawab({"sesi": u["sesi"], "nomor": 0,
                        "pilihan": objU.soal[0]["jawab"]})
        r = api.kuis_selesai({"sesi": u["sesi"]})

        sesudah = progress.load_progress()["kuis_skor"][k]
        self.assertEqual(sesudah["terbaik"], terbaik)
        self.assertEqual(sesudah["total_soal"], len(obj.soal))
        self.assertFalse(r["sesi_penuh"])
        self.assertEqual(r["salah_tersisa"], 0)

    def test_ulangan_sebagian_tidak_menghapus_sisa_daftar_salah(self):
        """Mengulang 3 dari 3 soal salah dan hanya benar 2: 1 harus tersisa."""
        lang = _bahasa("java")
        judul = lang["quizzes"][0]["title"]
        progress.perbarui_soal_salah("java_kuis", judul, [0, 1, 2])
        u = api.kuis_mulai({"key": "java", "indeks": 0, "mode": "salah",
                            "acak": False})
        obj = sesi.ambil(u["sesi"])
        api.kuis_jawab({"sesi": u["sesi"], "nomor": 0,
                        "pilihan": obj.soal[0]["jawab"]})
        salah = (obj.soal[1]["jawab"] + 1) % len(obj.soal[1]["options"])
        api.kuis_jawab({"sesi": u["sesi"], "nomor": 1, "pilihan": salah})
        api.kuis_jawab({"sesi": u["sesi"], "nomor": 2,
                        "pilihan": obj.soal[2]["jawab"]})
        r = api.kuis_selesai({"sesi": u["sesi"]})
        self.assertEqual(r["salah_tersisa"], 1)

    def test_mode_salah_tanpa_soal_salah_ditolak_dengan_jelas(self):
        with self.assertRaises(api.Galat) as c:
            api.kuis_mulai({"key": "java", "indeks": 0, "mode": "salah"})
        self.assertEqual(c.exception.kode, 409)

    def test_sesi_hilang_memberi_pesan_yang_bisa_ditindaklanjuti(self):
        with self.assertRaises(api.Galat) as c:
            api.kuis_jawab({"sesi": "tidak-ada", "nomor": 0, "pilihan": 0})
        self.assertEqual(c.exception.kode, 410)
        self.assertIn("Mulai ulang", c.exception.pesan)

    def test_sesi_lama_dibuang_supaya_tidak_menumpuk(self):
        for i in range(sesi.MAKS_SESI + 6):
            sesi.buat("k", f"judul {i}", "java",
                      [{"q": "?", "options": ["a", "b"], "answer": 0}])
        self.assertLessEqual(len(sesi._SESI), sesi.MAKS_SESI)


# ------------------------------------------------------------------- latihan

class TestLatihan(BasisWeb):
    def test_membuka_latihan_mencatat_dan_menyiapkan_berkas(self):
        x = api.latihan({"key": "python", "indeks": "0"})
        self.assertEqual(x["hadiah"]["xp_tambah"], progress.XP_LATIHAN_DILIHAT)
        self.assertTrue(x["berkas"]["nama"].endswith(".py"))
        self.assertTrue(x["kode"].strip(), "kerangka awal tidak boleh kosong")

    def test_nama_berkas_java_sama_dengan_nama_kelas(self):
        x = api.latihan({"key": "java", "indeks": "0"})
        nama = x["berkas"]["nama"]
        self.assertTrue(nama.endswith(".java"))
        self.assertIn(f"public class {nama[:-5]}", x["kode"])

    def test_simpan_menulis_ke_jalur_yang_sama_dengan_terminal(self):
        api.latihan_simpan({"key": "python", "indeks": 0, "kode": "print(1)"})
        lang = next(l for l in api.LANGUAGES if l["key"] == "python")
        path = api._path_kerja("python_latihan", lang["exercises"][0], "python")
        with open(path, encoding="utf-8") as f:
            self.assertEqual(f.read(), "print(1)")

    def test_manual_ditolak_untuk_latihan_yang_bisa_dinilai(self):
        with self.assertRaises(api.Galat) as c:
            api.latihan_manual({"key": "python", "indeks": 0, "nyalakan": True})
        self.assertEqual(c.exception.kode, 409)

    def test_kerangka_bisa_diambil_ulang(self):
        r = api.latihan_kerangka({"key": "java", "indeks": "0"})
        self.assertIn("public class", r["kode"])

    def test_ruang_coba_menolak_bahasa_tak_dikenal(self):
        with self.assertRaises(api.Galat):
            api.coba({"bahasa": "kobol", "kode": "x"})

    def test_ruang_coba_menolak_kode_raksasa(self):
        with self.assertRaises(api.Galat) as c:
            api.coba({"bahasa": "python", "kode": "x" * (api.MAKS_KODE + 1)})
        self.assertEqual(c.exception.kode, 413)

    @unittest.skipIf(LEWATI_LAMBAT, "menjalankan kode; BELAJAR_SKIP_LAMBAT=1")
    @unittest.skipUnless(shutil.which("python3"), "butuh python3")
    def test_jawaban_benar_lulus_dan_memberi_xp(self):
        lang = next(l for l in api.LANGUAGES if l["key"] == "python")
        ex = lang["exercises"][0]
        r = api.latihan_periksa({"key": "python", "indeks": 0,
                                 "kode": ex["solution"]})
        self.assertTrue(r["lulus"], r.get("alasan"))
        self.assertEqual(r["status"], "lulus")
        self.assertEqual(r["hadiah"]["xp_tambah"], progress.XP_LATIHAN_LULUS)

    @unittest.skipIf(LEWATI_LAMBAT, "menjalankan kode; BELAJAR_SKIP_LAMBAT=1")
    @unittest.skipUnless(shutil.which("python3"), "butuh python3")
    def test_jawaban_salah_membawa_diff_dan_diagnosis(self):
        r = api.latihan_periksa({
            "key": "python", "indeks": 0,
            "kode": 'print("halo, namaku andi!")\nprint("aku sedang belajar python.")',
        })
        self.assertFalse(r["lulus"])
        beda = r["uji"][0]["beda"]
        self.assertIsNotNone(beda, "kegagalan beda-output wajib membawa diff")
        self.assertTrue(beda["catatan"], "diff wajib disertai diagnosis")
        self.assertTrue(any("BESAR/KECIL" in c for c in beda["catatan"]))
        self.assertEqual(beda["kolom_beda"], 1)

    @unittest.skipIf(LEWATI_LAMBAT, "menjalankan kode; BELAJAR_SKIP_LAMBAT=1")
    @unittest.skipUnless(shutil.which("python3"), "butuh python3")
    def test_error_sintaks_diterjemahkan_dan_pathnya_disembunyikan(self):
        r = api.latihan_periksa({"key": "python", "indeks": 0,
                                 "kode": 'print("halo"'})
        self.assertFalse(r["lulus"])
        g = r["uji"][0]["galat"]
        self.assertIsNotNone(g)
        self.assertTrue(g["artinya"], "error sintaks Python wajib diterjemahkan")
        self.assertNotIn("/tmp/belajar-", g["mentah"])

    @unittest.skipIf(LEWATI_LAMBAT, "menjalankan kode; BELAJAR_SKIP_LAMBAT=1")
    @unittest.skipUnless(shutil.which("python3"), "butuh python3")
    def test_ruang_coba_tidak_menyentuh_progres(self):
        sebelum = progress.load_progress()["xp"]
        r = api.coba({"bahasa": "python", "kode": 'print("halo")'})
        self.assertEqual(r["keluaran"].strip(), "halo")
        self.assertEqual(progress.load_progress()["xp"], sebelum)

    @unittest.skipIf(LEWATI_LAMBAT, "menjalankan kode; BELAJAR_SKIP_LAMBAT=1")
    @unittest.skipUnless(shutil.which("python3"), "butuh python3")
    def test_path_sementara_tidak_bocor_ke_ruang_coba(self):
        r = api.coba({"bahasa": "python", "kode": "print(1/0)"})
        self.assertIsNotNone(r["galat"])
        self.assertNotIn("/tmp/belajar-", r["galat"]["mentah"])
        self.assertTrue(r["galat"]["artinya"])


# --------------------------------------------------------------- penyajian isi

class TestBerkasStatik(unittest.TestCase):
    """Penjagaan yang bentuknya berkas, bukan perilaku."""

    AKAR_JS = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "webapp", "statik", "js")

    def test_tidak_ada_replaceChildren_di_luar_inti(self):
        """`replaceChildren` mengubah `null` jadi kata "null" di layar.

        Seluruh berkas ini memakai pola `syarat ? h(...) : null`. Di dalam
        `h()` pola itu aman -- `tambah()` menyaringnya. Dipasang langsung
        sebagai argumen `replaceChildren`, `null` berubah jadi simpul teks dan
        kata "null" muncul di halaman, tanpa satu pun error di konsol. Sudah
        pernah terjadi di layar kuis (dua kali) dan bookmark.

        Penggantinya `isikan()` di inti.js, yang lewat `tambah()` yang sama.
        """
        pelanggar = []
        for nama in sorted(os.listdir(self.AKAR_JS)):
            if not nama.endswith(".js") or nama == "inti.js":
                continue
            with open(os.path.join(self.AKAR_JS, nama), encoding="utf-8") as f:
                for nomor, baris in enumerate(f, 1):
                    if "replaceChildren(" in baris:
                        pelanggar.append(f"{nama}:{nomor}")
        self.assertEqual(pelanggar, [],
                         "pakai isikan() dari inti.js, bukan replaceChildren")

    def test_penanda_modul_es_ada(self):
        """Tanpa berkas ini, dua tes yang menjalankan JS-nya GAGAL, bukan skip.

        Node membaca *.js sebagai CommonJS kecuali package.json terdekat
        menyatakan sebaliknya, dan tes yang merah karena alasan yang tidak ada
        hubungannya dengan isinya adalah tes yang berhenti dibaca orang.
        """
        jalur = os.path.join(self.AKAR_JS, "package.json")
        self.assertTrue(os.path.exists(jalur), "webapp/statik/js/package.json hilang")
        with open(jalur, encoding="utf-8") as f:
            self.assertEqual(json.load(f).get("type"), "module")


class TestPenyajianIsi(unittest.TestCase):
    def test_blok_badan_memisahkan_prosa_pra_dan_daftar(self):
        blok = isi.blok_badan([
            "Kalimat biasa.", "",
            "  Tipe   Ukuran", "  int    4 byte", "",
            "- butir satu", "- butir dua", "",
            "1. langkah satu", "2. langkah dua",
        ])
        self.assertEqual([b["jenis"] for b in blok],
                         ["teks", "pra", "daftar", "daftar"])
        self.assertFalse(blok[2]["urut"])
        self.assertTrue(blok[3]["urut"])
        self.assertEqual([x["teks"] for x in blok[2]["butir"]],
                         ["butir satu", "butir dua"])

    def test_blok_pra_mempertahankan_indentasi_relatif(self):
        """Tabel ASCII hanya terbaca kalau kolomnya tetap sejajar."""
        blok = isi.blok_badan(["  induk", "      anak"])
        self.assertEqual(blok[0]["teks"], "induk\n    anak")

    def test_daftar_menjorok_tetap_daftar(self):
        """Regresi: daftar yang ditulis menjorok jadi blok monospace.

        Ini bentuk yang dipakai HAMPIR SELURUH kurikulum -- 664 dari 885
        daftar. Karena indentasi diperiksa sebelum penanda, semuanya dulu
        mendarat sebagai `pra`, dan halaman materi kehilangan satu-satunya
        pembeda visual antara penjelasan dan contoh kode.
        """
        blok = isi.blok_badan(["  - butir satu", "  - butir dua"])
        self.assertEqual([b["jenis"] for b in blok], ["daftar"])
        self.assertEqual([x["teks"] for x in blok[0]["butir"]],
                         ["butir satu", "butir dua"])

    def test_baris_lanjutan_menyambung_kalimat_butirnya(self):
        """Satu kalimat tidak boleh pecah jadi beberapa bulatan."""
        blok = isi.blok_badan([
            "  - Kalau kamu datang dari Python, lupakan dulu alur",
            "    program. Di sini kamu menjelaskan sebuah dokumen.",
        ])
        self.assertEqual(len(blok[0]["butir"]), 1)
        self.assertEqual(
            blok[0]["butir"][0]["teks"],
            "Kalau kamu datang dari Python, lupakan dulu alur program. "
            "Di sini kamu menjelaskan sebuah dokumen.")

    def test_contoh_milik_butir_tidak_diratakan_jadi_kalimat(self):
        """Perataan kolom ADALAH isinya; menyambungnya menghapus artinya."""
        blok = isi.blok_badan([
            "  - Generic hanya bisa menampung objek:",
            "      List<int> daftar;       // ERROR",
            "      List<Integer> daftar;   // benar",
        ])
        butir = blok[0]["butir"][0]
        self.assertEqual(butir["teks"], "Generic hanya bisa menampung objek:")
        self.assertEqual([x["jenis"] for x in butir["blok"]], ["pra"])
        self.assertEqual(butir["blok"][0]["teks"],
                         "List<int> daftar;       // ERROR\n"
                         "List<Integer> daftar;   // benar")

    def test_urutan_prosa_dan_contoh_di_dalam_butir_dipertahankan(self):
        """Prosa penutup sering MENUNJUK contoh di atasnya."""
        blok = isi.blok_badan([
            "1. INLINE - atribut style langsung di elemennya.",
            "     <h1 style=\"color: darkred\">",
            "   Hanya mengenai satu elemen itu.",
        ])
        butir = blok[0]["butir"][0]
        self.assertEqual(butir["teks"],
                         "INLINE - atribut style langsung di elemennya.")
        self.assertEqual([x["jenis"] for x in butir["blok"]], ["pra", "teks"])

    def test_tabel_berkolom_bintang_bukan_daftar(self):
        """"  *  perkalian        a * b" adalah tabel, bukan butir.

        Pembedanya jumlah spasi sesudah penanda: 446 dari 449 daftar sungguhan
        memakai tepat satu, dan ketiga sisanya justru tabel seperti ini.
        """
        blok = isi.blok_badan([
            "  *  perkalian        a * b",
            "  /  pembagian        a / b",
        ])
        self.assertEqual([b["jenis"] for b in blok], ["pra"])

    def test_paragraf_disambung_bukan_dipatahkan_ulang(self):
        """Patahan baris di sumber cuma jejak lebar berkasnya, bukan isi."""
        blok = isi.blok_badan([
            "Materi ini hanya tentang yang pertama. Jangan campur dulu.",
            "Halaman yang HTML-nya benar tapi belum diberi CSS tetap bisa",
            "dibaca orang.",
        ])
        self.assertEqual(blok[0]["jenis"], "teks")
        self.assertNotIn("\n", blok[0]["teks"])

    def test_kata_terpenggal_disambung_tanpa_spasi(self):
        """"diam-" + "diam" = "diam-diam", bukan "diam- diam".

        Semua 18 pemenggalan di kurikulum adalah kata ulang, jadi tanda
        hubungnya bagian dari katanya dan yang salah cuma spasinya.
        """
        blok = isi.blok_badan(["Ia menebak diam-",
                               "diam lalu tetap menampilkan halamannya."])
        self.assertEqual(blok[0]["teks"],
                         "Ia menebak diam-diam lalu tetap menampilkan "
                         "halamannya.")

    def test_tanda_hubung_sebagai_jeda_tetap_berspasi(self):
        """Hubung yang didahului spasi itu tanda baca, bukan penggalan kata."""
        blok = isi.blok_badan(["Pakai tanda hubung -",
                               "lalu lanjut ke berikutnya."])
        self.assertEqual(blok[0]["teks"],
                         "Pakai tanda hubung - lalu lanjut ke berikutnya.")

    def test_paragraf_berkolom_mempertahankan_barisnya(self):
        """"printf() -> ..." / "scanf()  -> ..." adalah dua entri, bukan satu."""
        blok = isi.blok_badan([
            "printf() -> menampilkan output ke layar.",
            "scanf()  -> membaca input dari keyboard.",
        ])
        self.assertIn("\n", blok[0]["teks"])

    def test_prosa_menjorok_bukan_blok_monospace(self):
        """181 paragraf biasa dulu tampil sebagai kotak berhuruf mesin ketik."""
        blok = isi.blok_badan([
            "  Tag pembuka cuma berkata \"mulai dari sini\". Tanpa penutup,",
            "  browser tidak tahu di mana elemennya berakhir, jadi ia menebak",
            "  diam-diam lalu tetap menampilkan halamannya.",
        ])
        self.assertEqual([b["jenis"] for b in blok], ["catatan"])
        self.assertNotIn("\n", blok[0]["teks"])

    def test_kode_menjorok_tetap_monospace(self):
        """Sisi salah yang dipilih: ragu berarti TETAP kode.

        Menyangka prosa sebagai kode cuma mempertahankan keadaan lama;
        menyangka kode sebagai prosa menghapus perataan yang jadi isinya.
        """
        for contoh in (
            ["  bash --version"],                                # satu baris
            ["  grep 'a\\+' berkas", "  grep -E 'a+' berkas"],    # tanpa titik
            ["  module github.com/andi/tokoku", "  go 1.21"],
            ["  Tipe   Ukuran", "  int    4 byte"],             # kolom sejajar
        ):
            with self.subTest(contoh=contoh[0]):
                self.assertEqual(
                    [b["jenis"] for b in isi.blok_badan(contoh)], ["pra"])

    def test_blok_berperan_dikenali(self):
        """"Jebakan:" dan "Aturan ..." dibaca berbeda, jadi harus TAMPIL beda.

        Kurikulum sudah menulisnya sejak awal; yang hilang cuma penandanya di
        layar, sehingga peringatan berhuruf kapital punya bobot visual yang
        sama dengan kalimat penghubung di sebelahnya.
        """
        contoh = [
            ("JEBAKAN: gambar pertama halaman justru tidak boleh lazy.",
             "jebakan"),
            ("Jangan pakai <br><br> untuk membuat jarak antar paragraf.",
             "jebakan"),
            ("Aturan yang menyelamatkanmu dari banyak kebingungan:", "aturan"),
            ("Perhatikan letak daftar bersarang di contoh:", "aturan"),
            ("Dua paragraf pertama isinya sama persis.", ""),
        ]
        for teks, harap in contoh:
            with self.subTest(teks=teks[:30]):
                blok = isi.blok_badan([teks])
                self.assertEqual(blok[0].get("peran"), harap)

    def test_peran_tetap_jarang(self):
        """Kalau semuanya ditandai, tidak ada yang tertandai.

        Ambangnya bukan selera: kotak berwarna yang muncul di tiap dua
        paragraf berhenti dibaca sebagai penanda dan mulai dibaca sebagai
        latar belakang. 6% sekarang; kalau sebuah pola baru ditambahkan dan
        angkanya melewati 15%, yang hilang bukan kerapian melainkan seluruh
        gunanya.
        """
        berperan = biasa = 0
        for lang in api.LANGUAGES:
            for m in lang["materials"]:
                for bagian in m["sections"]:
                    for b in isi.blok_badan(bagian.get("body") or []):
                        if b["jenis"] not in ("teks", "catatan"):
                            continue
                        if b.get("peran"):
                            berperan += 1
                        else:
                            biasa += 1
        total = berperan + biasa
        self.assertGreater(berperan, 100, "terlalu sedikit untuk memberi irama")
        self.assertLess(berperan / total, 0.15,
                        "terlalu sering; penandanya berhenti menandai apa pun")

    def test_daftar_bersarang_tidak_diratakan(self):
        blok = isi.blok_badan([
            "  - Alasannya:",
            "    - Satu berkas menata semua halaman.",
            "    - Browser menyimpannya di cache.",
        ])
        butir = blok[0]["butir"]
        self.assertEqual(len(butir), 1)
        self.assertEqual(butir[0]["teks"], "Alasannya:")
        self.assertEqual([x["teks"] for x in butir[0]["anak"]["butir"]],
                         ["Satu berkas menata semua halaman.",
                          "Browser menyimpannya di cache."])

    def test_token_semua_kode_kurikulum_utuh(self):
        """Tidak boleh ada satu karakter pun yang hilang saat kode dipecah."""
        for lang in api.LANGUAGES:
            b = isi.bahasa_sorot(lang)
            for m in lang["materials"]:
                for bagian in m["sections"]:
                    if "code" not in bagian:
                        continue
                    ulang = "".join(t[1] for t in isi.token_kode(bagian["code"], b))
                    self.assertEqual(ulang, bagian["code"],
                                     f"{lang['key']} / {m['title']}")

    def test_aturan_penyorot_lengkap_untuk_semua_bahasa(self):
        aturan = isi.aturan_penyorot()
        for lang in api.LANGUAGES:
            self.assertIn(isi.bahasa_sorot(lang), aturan, lang["key"])

    def test_pencarian_menghormati_saringan_tipe(self):
        for tipe in ("materi", "kuis", "latihan"):
            for h in isi.cari(api.LANGUAGES, "data", tipe):
                self.assertEqual(h["tipe"], tipe)


# ---------------------------------------------------- kesepadanan penyorot JS

_SKRIP_BANDING = r"""
globalThis.window = { TOKEN_BELAJAR: "x" };
globalThis.document = {
  createElement: () => ({ style: {}, appendChild() {}, setAttribute() {} }),
  createTextNode: () => ({}),
  createDocumentFragment: () => ({ appendChild() {} }),
  querySelector: () => null, addEventListener() {},
};
const fs = await import("node:fs");
const { pasangAturan, token } = await import(process.argv[2]);
const kasus = JSON.parse(fs.readFileSync(process.argv[3], "utf8"));
pasangAturan(kasus.aturan);
const beda = [];
for (const k of kasus.kasus) {
  if (JSON.stringify(token(k.kode, k.bahasa)) !== JSON.stringify(k.harapan)) {
    beda.push(k.label);
  }
}
console.log(JSON.stringify({ total: kasus.kasus.length,
                             jumlahBeda: beda.length, beda: beda.slice(0, 5) }));
"""

# Kode yang sengaja rusak atau menjengkelkan. Pemindainya tidak boleh gagal,
# dan KEDUA implementasinya harus gagal dengan cara yang sama persis.
_KASUS_SULIT = [
    ("python", 'x = "kutip belum ditutup\nprint(1)'),
    ("python", 'a = """tiga\nbaris"""'),
    ("python", "n = 1_000 + 3.14e-2 + 0b1010"),
    ("python", "émoji = 'héllo → 日本'  # unicode"),
    ("java", "char c = '\\''; // kutip di dalam kutip"),
    ("bash", "#!/usr/bin/env bash\necho '$mentah' \"$ekspansi\" ${a} $1 $@"),
    ("go", "x := `mentah\nmulti`"),
    ("c", "#include <stdio.h>\nint a[] = {1,2}; /* tak ditutup"),
    ("sql", "select COUNT(*) from t where x like '%a%'"),
    ("javascript", "const s = `halo ${n}`; /* blok\ntak ditutup"),
    ("python", ""),
    ("java", "   "),
]


# ---------------------------------------------------------------- gerak.js

_SKRIP_GERAK = r"""
const g = await import(process.argv[2]);

const hasil = { lolos: [], gagal: [] };
const cek = (nama, syarat, ket = "") => {
  (syarat ? hasil.lolos : hasil.gagal).push(nama + (syarat ? "" : " -- " + ket));
};

// 1. Tanpa DOM, mesinnya harus tetap bisa diimpor dan menjawab "mati".
cek("tingkatGerak tanpa DOM = mati", g.tingkatGerak() === "mati",
    "dapat " + g.tingkatGerak());
cek("adaGerak tanpa DOM = false", g.adaGerak() === false);
cek("skala tanpa DOM = 0", g.skala() === 0);
// Fungsi ber-DOM tidak boleh melempar walau dipanggil di tempat tanpa DOM.
try {
  g.animasi(null, {}, {});
  g.masuk(null);
  g.tata(null, () => {});
  g.percikBara(null);
  g.saatTampak(null, () => {})();
  cek("fungsi ber-DOM aman dipanggil tanpa DOM", true);
} catch (e) {
  cek("fungsi ber-DOM aman dipanggil tanpa DOM", false, e.message);
}

// 2. Pembantu angka.
cek("jepit", g.jepit(5, 0, 1) === 1 && g.jepit(-2, 0, 1) === 0
             && g.jepit(0.4, 0, 1) === 0.4);
cek("antara", g.antara(10, 20, 0.5) === 15);
cek("petakan naik", g.petakan(50, [0, 100], [0, 360]) === 180);
cek("petakan menjepit", g.petakan(200, [0, 100], [0, 360]) === 360);
cek("petakan turun", g.petakan(50, [0, 100], [1, 0]) === 0.5);
cek("petakan rentang nol tidak NaN",
    Number.isFinite(g.petakan(5, [3, 3], [0, 1])));

// 3. durasiTampak harus benar-benar mengendalikan gerakannya. Ini sifat yang
//    pernah SALAH: dengan definisi "waktu pertama menyentuh sasaran", pegas
//    tak berpantul sudah 99,5% sampai jauh sebelum waktu yang diminta, dan
//    dua durasiTampak yang berbeda menghasilkan animasi yang sama persis.
//    Toleransinya sengaja ketat (0.004). Dengan definisi lama, f(durasiTampak)
//    keluar tepat 1.0 alih-alih 0.99 -- selisih yang lolos begitu saja dari
//    toleransi longgar, padahal ia menandai definisi yang salah.
for (const [dt, pantul] of [[0.2, 0], [0.3, 0], [0.5, 0], [0.25, 0.3],
                            [0.4, 0.5]]) {
  const p = g.paramPegas({ durasiTampak: dt, pantul });
  const f = g.jalurPegas(p);
  const di = f(dt);
  cek(`f(durasiTampak=${dt}, pantul=${pantul}) tepat 0.99`,
      Math.abs(di - 0.99) < 0.004, "dapat " + di.toFixed(5));
}

// Dua durasiTampak berbeda WAJIB menghasilkan durasi yang berbeda.
const cepat = g.kurvaPegas({ durasiTampak: 0.18, pantul: 0 }).durasi;
const lambat = g.kurvaPegas({ durasiTampak: 0.45, pantul: 0 }).durasi;
cek("durasiTampak lebih besar = durasi lebih panjang", lambat > cepat * 1.5,
    `${cepat} vs ${lambat}`);

// Animasinya tidak boleh SELESAI sebelum ia "terlihat selesai": durasi total
// wajib >= durasiTampak, berapa pun pantulnya. Ini penjaga untuk kesalahan
// yang paling gampang terjadi di sini -- rumus yang memakai
// 1/sqrt(1 - zeta^2) meledak begitu pantul mendekati nol, dan "sampai dalam
// 0,3 detik" diam-diam berubah jadi animasi 100 md.
const perPantul = [0, 0.1, 0.3, 0.5]
  .map((pantul) => g.kurvaPegas({ durasiTampak: 0.3, pantul }).durasi);
cek("durasi total tidak lebih pendek dari durasiTampak",
    perPantul.every((d) => d >= 300), perPantul.join(" / "));
// Pantul yang lebih besar memang membeli ekor yang lebih panjang -- itu
// fisikanya, dan itu justru alasan preset `lentur` menahan pantulnya di 0.26.
cek("pantul besar = ekor lebih panjang",
    perPantul[3] > perPantul[0], perPantul.join(" / "));

// 4. Bentuk kurvanya.
for (const [nama, p] of Object.entries(g.PEGAS)) {
  const k = g.kurvaPegas(p);
  const t = k.titik;
  cek(`${nama}: mulai 0`, t[0] === 0);
  cek(`${nama}: berakhir 1`, t[t.length - 1] === 1);
  cek(`${nama}: durasi wajar`, k.durasi > 40 && k.durasi < 1200,
      k.durasi + "ms");
  cek(`${nama}: easing berbentuk linear()`,
      /^linear\([-\d.,]+\)$/.test(k.easing), k.easing.slice(0, 40));
  cek(`${nama}: tidak ada NaN`, t.every(Number.isFinite));
  // Tidak ada satu pun animasi yang berkedip: kurvanya tidak boleh turun
  // balik ke bawah nol atau melonjak jauh di atas sasaran.
  cek(`${nama}: tidak menembus jauh di bawah nol`, Math.min(...t) > -0.12,
      String(Math.min(...t)));
  cek(`${nama}: puncak wajar`, Math.max(...t) < 1.25,
      String(Math.max(...t)));
}

// pantul 0 harus benar-benar tidak berpantul; pantul besar harus berpantul.
const tanpaPantul = g.kurvaPegas({ durasiTampak: 0.3, pantul: 0 }).titik;
cek("pantul 0 tidak melewati sasaran", Math.max(...tanpaPantul) <= 1.0001,
    String(Math.max(...tanpaPantul)));
const berpantul = g.kurvaPegas({ durasiTampak: 0.3, pantul: 0.4 }).titik;
cek("pantul 0.4 melewati sasaran", Math.max(...berpantul) > 1.01,
    String(Math.max(...berpantul)));

// pantul 0 juga harus MONOTON naik -- sekali turun di tengah, itu kedipan.
let monoton = true;
for (let i = 1; i < tanpaPantul.length; i++) {
  if (tanpaPantul[i] < tanpaPantul[i - 1] - 1e-9) monoton = false;
}
cek("pantul 0 naik monoton", monoton);

// 5. Kekakuan/redaman mentah tetap diterima apa adanya.
const mentah = g.paramPegas({ kekakuan: 200, redaman: 20, massa: 2 });
cek("parameter mentah dipakai apa adanya",
    mentah.kekakuan === 200 && mentah.redaman === 20 && mentah.massa === 2);

// Ketiga rezim redaman harus punya penyelesaian, bukan NaN.
for (const [nama, redaman] of [["kurang", 10], ["kritis", 20], ["lebih", 60]]) {
  const f = g.jalurPegas({ kekakuan: 100, redaman, massa: 1, kecepatan: 0 });
  cek(`teredam ${nama}: berhingga`,
      Number.isFinite(f(0)) && Number.isFinite(f(0.5)) && Number.isFinite(f(5)));
  cek(`teredam ${nama}: mulai di 0`, Math.abs(f(0)) < 1e-9, String(f(0)));
  cek(`teredam ${nama}: berakhir di 1`, Math.abs(f(30) - 1) < 1e-6,
      String(f(30)));
}

// 6. Urutan (stagger).
const b = g.berurut(60, { per: 34, maks: 300 });
cek("berurut: item pertama tanpa tunggu", b(0) === 0);
cek("berurut: daftar panjang tidak melewati batas", b(59) <= 300.0001,
    String(b(59)));
const b2 = g.berurut(5, { per: 30, maks: 1000 });
cek("berurut: daftar pendek memakai jarak penuh", Math.abs(b2(4) - 120) < 1e-9,
    String(b2(4)));
const bt = g.berurut(5, { dari: "tengah", per: 20, maks: 1000 });
cek("berurut dari tengah: pusatnya nol", bt(2) === 0);
cek("berurut dari tengah: simetris", Math.abs(bt(0) - bt(4)) < 1e-9);
const ba = g.berurut(5, { dari: "akhir", per: 20, maks: 1000 });
cek("berurut dari akhir: item terakhir nol", ba(4) === 0);
cek("berurut: mulai digeser", g.berurut(3, { mulai: 50, per: 10 })(0) === 50);
cek("berurut: jumlah nol tidak meledak", Number.isFinite(g.berurut(0)(0)));

console.log(JSON.stringify(hasil));
"""


class TestMesinGerak(unittest.TestCase):
    """Adu solver pegas di statik/js/gerak.js dengan sifat yang harus berlaku.

    Yang diuji bukan angka hasilnya melainkan SIFATNYA: kurva mulai di 0 dan
    berakhir di 1, pegas tanpa pantul tidak pernah melewati sasaran dan tidak
    pernah turun di tengah, `durasiTampak` benar-benar mengendalikan lamanya,
    dan urutan tidak pernah membuat daftar panjang menunggu lebih lama dari
    batasnya. Menguji angka persisnya akan membuat tes ini pecah setiap kali
    sebuah preset disetel ulang -- padahal menyetel preset justru pekerjaan
    yang wajar.

    Separuh atas gerak.js sengaja ditulis tanpa menyentuh DOM sama sekali
    supaya bisa dijalankan langsung di Node seperti ini.
    """

    @unittest.skipUnless(shutil.which("node"), "butuh node untuk menguji gerak.js")
    def test_solver_pegas_dan_urutan(self):
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        jalur = os.path.join(akar, "webapp", "statik", "js", "gerak.js")
        with tempfile.TemporaryDirectory() as d:
            js = os.path.join(d, "uji-gerak.mjs")
            with open(js, "w", encoding="utf-8") as f:
                f.write(_SKRIP_GERAK)
            hasil = subprocess.run(["node", js, jalur],
                                   capture_output=True, text=True, timeout=60)

        self.assertEqual(hasil.returncode, 0, hasil.stderr[-1200:])
        laporan = json.loads(hasil.stdout)
        self.assertEqual(laporan["gagal"], [], "sifat pegas yang dilanggar")
        self.assertGreater(len(laporan["lolos"]), 40,
                           "terlalu sedikit sifat yang benar-benar diuji")


_SKRIP_TANPA_DOM = r"""
// Perangkap: apa pun yang menyentuh `document` atau `window` SAAT IMPOR akan
// melempar dengan pesan yang menyebut jalurnya. Node memang tidak punya
// keduanya, tapi tanpa perangkap ini sebuah `document.documentElement` di
// tingkat modul cuma menghasilkan ReferenceError yang terbaca sama seperti
// kesalahan ketik biasa -- dan yang ingin dijaga bukan "tidak melempar",
// melainkan "tidak menyentuh".
const jejak = [];
const jebak = (nama) => new Proxy({}, {
  get(_, k) { jejak.push(nama + "." + String(k)); return undefined; },
  set(_, k) { jejak.push(nama + "." + String(k) + " ="); return true; },
});
globalThis.document = jebak("document");
globalThis.window = jebak("window");

const g = await import(process.argv[2]);
// Potret DI SINI, sebelum satu pun fungsi dipanggil: yang diuji adalah apa
// yang disentuh IMPOR, bukan apa yang disentuh pemakaian sesudahnya. vt()
// memang menanyakan matchMedia -- itu justru tugasnya.
const jejakImpor = jejak.slice();

const wajib = ["terbitkanKurva", "vt", "TOKEN_PEGAS", "PEGAS", "kurvaPegas"];
const hilang = wajib.filter((n) => g[n] === undefined);

// vt() harus memanggil fungsinya TEPAT SEKALI di dua jalur: platform tanpa
// startViewTransition, dan gerak yang dimatikan.
let n = 0;
await g.vt(() => { n++; });
delete globalThis.document.startViewTransition;
await g.vt(() => { n++; });

console.log(JSON.stringify({
  jejakSaatImpor: jejakImpor,
  eksporHilang: hilang,
  vtDipanggil: n,
  tokenPegas: Object.values(g.TOKEN_PEGAS),
  terbitTanpaAkar: g.terbitkanKurva(null),
}));
"""


class TestJembatanPlatform(unittest.TestCase):
    """Lapisan platform gerak: token pegas, `vt()`, dan janji bebas-DOM.

    Dua hal yang dijaga di sini, dan keduanya sudah pernah hampir dilanggar:

    1. `gerak.js` diimpor langsung di Node oleh TestMesinGerak. Janji itu
       bertahan hanya kalau kode ber-DOM tidak pernah berjalan saat impor --
       satu `document.documentElement` di tingkat modul cukup untuk
       merobohkannya, dan gejalanya di Node terbaca seperti salah ketik.
    2. Nama token pegas ditulis DUA KALI: sebagai `TOKEN_PEGAS` di gerak.js
       dan sebagai daftar yang dibaca manusia di blok ATURAN GERAK di kepala
       gaya.css. Dua salinan yang tidak diadu akan melenceng; prompt layar
       berikutnya membaca yang di CSS, sedangkan yang berlaku yang di JS.
    """

    @staticmethod
    def _akar():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @unittest.skipUnless(shutil.which("node"), "butuh node untuk menguji gerak.js")
    def test_impor_gerak_tidak_menyentuh_dom(self):
        jalur = os.path.join(self._akar(), "webapp", "statik", "js", "gerak.js")
        with tempfile.TemporaryDirectory() as d:
            js = os.path.join(d, "uji-tanpa-dom.mjs")
            with open(js, "w", encoding="utf-8") as f:
                f.write(_SKRIP_TANPA_DOM)
            hasil = subprocess.run(["node", js, jalur],
                                   capture_output=True, text=True, timeout=60)

        self.assertEqual(hasil.returncode, 0, hasil.stderr[-1200:])
        lap = json.loads(hasil.stdout)

        # Yang dilarang bukan "menyentuh" melainkan "menyentuh tanpa pagar".
        # gerak.js sengaja men-cache dua MediaQueryList di tingkat modul, dan
        # keduanya berdiri di belakang ADA_DOM (`typeof document`/`typeof
        # window`) sehingga di Node sungguhan tidak pernah dijalankan. Yang
        # tidak boleh adalah menyentuh STRUKTUR dokumen atau MENULIS apa pun
        # saat impor -- itulah yang akan merobohkan TestMesinGerak.
        BOLEH_SAAT_IMPOR = {"window.matchMedia"}
        terlarang = [j for j in lap["jejakSaatImpor"] if j not in BOLEH_SAAT_IMPOR]
        self.assertEqual(terlarang, [],
                         "gerak.js menyentuh DOM di luar deteksi fitur "
                         "berpagar saat diimpor; TestMesinGerak mengimpornya "
                         "di Node dan akan ikut mati")
        self.assertFalse([j for j in lap["jejakSaatImpor"] if j.endswith(" =")],
                         "ada penulisan ke DOM saat impor")
        self.assertEqual(lap["eksporHilang"], [], "ekspor lapisan platform hilang")
        self.assertEqual(lap["vtDipanggil"], 2,
                         "vt() wajib memanggil fungsinya tepat sekali di tiap "
                         "jalur, termasuk saat transisinya tidak terjadi")
        self.assertFalse(lap["terbitTanpaAkar"],
                         "terbitkanKurva() tanpa elemen akar harus menolak "
                         "diam-diam, bukan melempar")

    @unittest.skipUnless(shutil.which("node"), "butuh node")
    def test_impor_di_node_asli_tidak_melempar(self):
        """Tanpa global palsu apa pun -- ini yang benar-benar dijalankan CI."""
        jalur = os.path.join(self._akar(), "webapp", "statik", "js", "gerak.js")
        hasil = subprocess.run(
            ["node", "--input-type=module", "-e",
             'const g = await import(process.argv[1]);'
             'if (typeof document !== "undefined") throw new Error("document bocor");'
             'g.terbitkanKurva(); await g.vt(() => {});'
             'console.log(g.tingkatGerak());',
             jalur],
            capture_output=True, text=True, timeout=60)
        self.assertEqual(hasil.returncode, 0, hasil.stderr[-1200:])
        self.assertEqual(hasil.stdout.strip(), "mati")

    @unittest.skipUnless(shutil.which("node"), "butuh node untuk membaca TOKEN_PEGAS")
    def test_daftar_token_pegas_sama_di_js_dan_css(self):
        akar = self._akar()
        jalur_js = os.path.join(akar, "webapp", "statik", "js", "gerak.js")
        hasil = subprocess.run(
            ["node", "--input-type=module", "-e",
             'const g = await import(process.argv[1]);'
             'console.log(JSON.stringify(Object.values(g.TOKEN_PEGAS)));',
             jalur_js],
            capture_output=True, text=True, timeout=60)
        self.assertEqual(hasil.returncode, 0, hasil.stderr[-800:])
        dari_js = sorted(json.loads(hasil.stdout))

        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            css = f.read()

        kepala = css[:css.index("*/", css.index("ATURAN GERAK"))]
        disebut = sorted(set(re.findall(r"--pegas-[a-z]+", kepala)))
        self.assertEqual(disebut, dari_js,
                         "daftar token pegas di blok ATURAN GERAK (gaya.css) "
                         "tidak sama dengan TOKEN_PEGAS (gerak.js)")

        # Tiap kurva WAJIB punya pasangan -ms-nya, di :root maupun di JS.
        for token in dari_js:
            self.assertIn(token + ":", css,
                          f"{token} tidak punya cadangan di :root")
            self.assertIn(token + "-ms:", css,
                          f"{token} tidak berpasangan dengan {token}-ms")


class TestSatuMesinPerProperti(unittest.TestCase):
    """`#maju-baca` boleh digerakkan CSS ATAU JS, tidak pernah dua-duanya.

    Bilah kemajuan baca punya dua jalur: scroll-timeline milik CSS di browser
    yang mendukungnya, dan pendengar gulir milik JS di browser yang tidak.
    Keduanya menulis `transform` pada elemen yang sama, jadi menghidupkan
    keduanya berarti dua mesin pada satu properti -- dan gejalanya bukan error
    melainkan bilah yang tersendat karena dua penulis berebut tiap frame.

    `data-mesin` ditulis supaya keadaan itu bisa DIBUKTIKAN dari luar. Tes ini
    menjaga dua hal yang tidak terlihat dari membaca kodenya sepintas:
    nilainya tidak pernah selain "css"/"js", dan cabang CSS benar-benar
    berhenti sebelum sampai ke cabang JS.
    """

    @staticmethod
    def _sumber():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js", "aplikasi.js"),
                  encoding="utf-8") as f:
            return f.read()

    def test_nilai_data_mesin_hanya_css_atau_js(self):
        nilai = re.findall(r'dataset\.mesin\s*=\s*"([^"]*)"', self._sumber())
        self.assertTrue(nilai, "tidak ada yang menulis data-mesin lagi")
        self.assertEqual(sorted(set(nilai)), ["css", "js"],
                         f"nilai data-mesin di luar css/js: {sorted(set(nilai))}")

    def test_cabang_css_berhenti_sebelum_cabang_js(self):
        src = self._sumber()
        i_css = src.index('dataset.mesin = "css"')
        i_js = src.index('dataset.mesin = "js"')
        self.assertLess(i_css, i_js, "urutan cabang berubah; tes ini perlu ditulis ulang")
        antara = src[i_css:i_js]
        self.assertIn("return", antara,
                      "cabang CSS tidak berhenti sebelum cabang JS: kedua mesin "
                      "akan hidup bersamaan di browser yang mendukung "
                      "scroll-timeline")

    def test_hanya_satu_elemen_yang_membawa_data_mesin(self):
        src = self._sumber()
        # Keduanya harus menulis ke variabel yang sama, dan variabel itu harus
        # berasal dari satu pencarian #maju-baca.
        pemilik = set(re.findall(r'(\w+)\.dataset\.mesin\s*=', src))
        self.assertEqual(len(pemilik), 1,
                         f"data-mesin ditulis ke lebih dari satu elemen: {pemilik}")
        nama = pemilik.pop()
        self.assertRegex(src, rf'const {nama}\s*=\s*\$\("#maju-baca"\)',
                         f"{nama} bukan #maju-baca")


class TestPagarTingkatGerak(unittest.TestCase):
    """Pagar `[data-gerak]` harus meredam properti yang MEMANG disetel sasarannya.

    Bug yang melahirkan tes ini terjadi dua kali, dengan bentuk yang sama:
    sebuah gerakan dipindah ke tempat lain, pagarnya tidak ikut, dan aturannya
    berhenti mengenai sasaran tanpa satu pun pesan galat.

      · sapuan skeleton pindah dari `.denyut` ke `.denyut::after`;
        pagarnya tetap di `.denyut`.
      · geser hover pindah dari `transform` ke `translate` pada `.baris` dan
        `.opsi button`; pagarnya tetap meredam `transform`.

    Versi pertama tes ini hanya menutup `animation`, dan justru karena itulah
    regresi kedua lolos. Sekarang keempat properti yang bisa diredam diperiksa:
    animation, transform, translate, transition.
    """

    PROPERTI = ("animation", "transform", "translate", "transition")

    @staticmethod
    def _css():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            return re.sub(r"/\*.*?\*/", " ", f.read(), flags=re.S)

    @staticmethod
    def _aturan(css):
        for m in re.finditer(r"([^{}]+)\{([^{}]*)\}", css):
            yield m.group(1).strip(), m.group(2)

    def test_pagar_gerak_menyasar_properti_yang_memang_disetel(self):
        css = self._css()

        # 1. Apa yang diredam tiap pagar [data-gerak].
        pagar = []
        for sel_blok, isi in self._aturan(css):
            if "[data-gerak=" not in sel_blok:
                continue
            diredam = [pr for pr in self.PROPERTI
                       if re.search(rf"\b{pr}\s*:\s*none\b", isi)]
            if not diredam:
                continue
            for sel in sel_blok.split(","):
                sel = sel.strip()
                if "[data-gerak=" not in sel:
                    continue
                sisa = re.sub(r'\[data-gerak="[^"]+"\]', "", sel).strip()
                # Selector universal memang menyapu semuanya; ia tidak menunjuk
                # sasaran tertentu, jadi tidak bisa -- dan tidak perlu -- diadu.
                if not sisa or sisa.startswith("*"):
                    continue
                for pr in diredam:
                    pagar.append((sisa, pr))

        self.assertTrue(pagar, "tidak ada pagar [data-gerak] yang terbaca")

        # 2. Properti apa yang benar-benar disetel tiap selector.
        disetel = {}
        for sel_blok, isi in self._aturan(css):
            if "[data-gerak=" in sel_blok:
                continue
            punya = set()
            for pr in self.PROPERTI:
                m = re.search(rf"\b{pr}(-property)?\s*:\s*([^;]+)", isi)
                if m and m.group(2).strip() != "none":
                    punya.add(pr)
            # `transition: ... transform ...` juga berarti transform disetel
            # di sini: ia yang membuat perpindahannya terlihat bergerak.
            mt = re.search(r"\btransition(-property)?\s*:\s*([^;]+)", isi)
            if mt:
                for pr in ("transform", "translate"):
                    if re.search(rf"\b{pr}\b", mt.group(2)):
                        punya.add(pr)
            if not punya:
                continue
            for sel in sel_blok.split(","):
                disetel.setdefault(sel.strip(), set()).update(punya)

        # 3. Adu keduanya.
        #
        # Normalisasi membuang pseudo-class dan pseudo fungsional TAPI menjaga
        # struktur keturunannya. Versi pertama memotong di titik dua pertama,
        # sehingga `.baris:hover .baris-panah` runtuh jadi `.baris` -- dan pagar
        # `.baris:hover` yang sudah mati terlihat hidup karena ANAKNYA yang
        # punya transform. Yang diadu harus elemen yang sama, bukan kerabatnya.
        # Pseudo-KELAS (:hover, :active, :not(...)) adalah KEADAAN elemen yang
        # sama, jadi dibuang. Pseudo-ELEMEN (::after, ::before) adalah elemen
        # LAIN, jadi dipertahankan -- justru di situ letak regresi S03: pagar
        # menunjuk `.denyut` sementara yang beranimasi `.denyut::after`.
        PSEUDO_ELEMEN = ("::after", "::before", "::marker", "::placeholder",
                         "::selection", "::backdrop", "::first-line",
                         "::first-letter")

        def pokok(sel):
            simpan = [pe for pe in PSEUDO_ELEMEN if pe in sel]
            for pe in simpan:
                sel = sel.replace(pe, "\x00")
            sel = re.sub(r":[a-z-]+\([^)]*\)", "", sel)
            sel = re.sub(r":[a-z-]+", "", sel)
            for pe in simpan:
                sel = sel.replace("\x00", pe, 1)
            return " ".join(sel.split())

        peta = {}
        for s_sel, props in disetel.items():
            peta.setdefault(pokok(s_sel), set()).update(props)

        mati = []
        for sasaran, pr in sorted(set(pagar)):
            if pr not in peta.get(pokok(sasaran), set()):
                mati.append(f"{sasaran} -> {pr}")

        self.assertEqual(mati, [],
                         "pagar [data-gerak] meredam properti yang tidak pernah "
                         "disetel sasarannya; aturannya mati tanpa pesan galat: "
                         + "; ".join(mati))


class TestBerkasWebLengkap(unittest.TestCase):
    """Setiap modul JS yang diimpor harus ada dan bisa disajikan server.

    Aplikasi web ini memuat modul ES langsung dari sumbernya, tanpa langkah
    build. Enaknya: tidak ada yang bisa basi. Bahayanya: sebuah `import` yang
    salah ketik tidak ketahuan sampai halaman dibuka dan layar tinggal putih --
    dan tidak ada satu pun tes Python yang akan menangkapnya.
    """

    def setUp(self):
        self.akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.js = os.path.join(self.akar, "webapp", "statik", "js")

    def _berkas_js(self):
        return sorted(n for n in os.listdir(self.js) if n.endswith(".js"))

    def test_semua_import_menunjuk_berkas_yang_ada(self):
        import re
        pola = re.compile(r"""from\s+["'](\./[^"']+)["']""")
        diperiksa = 0
        for nama in self._berkas_js():
            with open(os.path.join(self.js, nama), encoding="utf-8") as f:
                teks = f.read()
            for m in pola.finditer(teks):
                tujuan = os.path.join(self.js, m.group(1))
                self.assertTrue(os.path.isfile(tujuan),
                                f"{nama} mengimpor {m.group(1)} yang tidak ada")
                diperiksa += 1
        self.assertGreater(diperiksa, 8, "impor terlalu sedikit untuk dipercaya")

    def test_gerak_js_ada_dan_diimpor_di_mana_mana(self):
        self.assertIn("gerak.js", self._berkas_js())
        pemakai = []
        for nama in self._berkas_js():
            if nama == "gerak.js":
                continue
            with open(os.path.join(self.js, nama), encoding="utf-8") as f:
                if "./gerak.js" in f.read():
                    pemakai.append(nama)
        self.assertIn("inti.js", pemakai)
        self.assertIn("aplikasi.js", pemakai)

    def test_halaman_memuat_sarana_yang_dipakai_gerak(self):
        with open(os.path.join(self.akar, "webapp", "statik", "index.html"),
                  encoding="utf-8") as f:
            html = f.read()
        # Keduanya dicari lewat querySelector oleh aplikasi.js. Kalau salah
        # satunya hilang dari halaman, penandanya diam-diam berhenti bekerja.
        self.assertIn('class="rel-tanda"', html)
        self.assertIn('id="maju-baca"', html)

    def test_gaya_css_kurungnya_seimbang(self):
        """Satu kurung tutup yang hilang membuat SISA berkas gaya diam-diam
        tidak berlaku.

        Ini bukan kekhawatiran teoretis: pernah terjadi persis begitu di sini.
        Sebuah blok dihapus bersama kurung tutup tetangganya, dan browser
        berhenti mengurai tepat di situ -- 60 aturan sesudahnya lenyap tanpa
        satu pun error di konsol, tanpa halaman yang gagal dimuat, dan tanpa
        satu tes pun yang gagal. Yang terlihat cuma "kok tampilannya jadi
        aneh". Perhitungan kurung menangkapnya dalam sepersekian detik.
        """
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            css = f.read()

        # Komentar dan string dibuang lebih dulu: kurung di dalamnya bukan
        # kurung blok, dan berkas ini penuh komentar panjang.
        import re
        bersih = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        bersih = re.sub(r'"[^"\n]*"|\'[^\'\n]*\'', '""', bersih)

        buka = bersih.count("{")
        tutup = bersih.count("}")
        self.assertEqual(
            buka, tutup,
            f"kurung gaya.css tidak seimbang: {buka} '{{' lawan {tutup} '}}'. "
            "Satu blok tidak ditutup, dan semua aturan sesudahnya tidak akan "
            "berlaku.")

        # Kedalaman tidak boleh pernah negatif -- itu tanda '}' yang berlebih,
        # yang gejalanya sama merusaknya tapi arahnya berlawanan.
        dalam = 0
        for i, c in enumerate(bersih):
            if c == "{":
                dalam += 1
            elif c == "}":
                dalam -= 1
                self.assertGreaterEqual(
                    dalam, 0,
                    "ada '}' berlebih di gaya.css sekitar: "
                    + bersih[max(0, i - 90):i + 10].strip()[-110:])

    def test_gaya_css_memuat_kelas_yang_dipakai_javascript(self):
        """Kelas tata letak inti harus benar-benar punya aturan.

        Kelas yang dipakai JS tapi tidak pernah didefinisikan di CSS tidak
        menghasilkan error apa pun -- elemennya cuma tampil tanpa gaya. Yang
        didaftar di sini adalah kelas yang kalau hilang membuat sebuah halaman
        kehilangan bentuknya sama sekali, bukan sekadar terlihat berbeda.
        """
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            css = f.read()

        wajib = [
            "lanjutkan", "lanjutkan-tbl", "lanjutkan-nomor",
            "kepala-besar", "kepala-sub",
            "fakta", "fakta-butir", "tab-jumlah",
            "materi-tata", "materi-rel", "materi-peta", "materi-utama",
            "materi-alat",
            "kerja", "kerja-tata", "kerja-soal", "kerja-kode", "kerja-bawah",
            "kerja-tindakan", "kerja-utama", "kerja-hasil",
            "tbl-pilih", "tbl-set", "sambut", "kartu-level",
            # Dasbor dua kolom, dan layar "mulai" untuk profil yang masih
            # kosong. Tanpa aturannya, dasbor kembali jadi satu kolom
            # bertumpuk dan tiga pintu masuk di layar pertama kehilangan
            # bentuknya sama sekali.
            # "pintu" TELANJANG tidak pernah dipancarkan JS: yang ada
            # `pintu-tenang` (pintunya) dan `pintu-isi` (isinya). Entri lama
            # itu lolos selama bertahun-tahun karena satu-satunya `.pintu`
            # di gaya.css adalah pagar [data-gerak="halus"] .pintu:hover --
            # aturan yang tidak pernah mengenai apa pun. Begitu pagar mati
            # itu dibuang, tes ini merah dan menunjuk dirinya sendiri.
            "dasbor", "dasbor-utama", "dasbor-sisi", "mulai",
            "pintu-tenang", "pintu-isi",
            # Keadaan: SATU komponen untuk kosong/berhasil/gagal/terkunci.
            # Kalau aturannya hilang, keempatnya sekaligus jadi teks telanjang
            # di tengah halaman — termasuk layar penolakan bab terkunci.
            "keadaan", "keadaan-tuntas", "keadaan-kosong", "keadaan-kunci",
            # Strip konteks: pengganti remah roti sekaligus pembawa posisi.
            # Tanpa gayanya ia jadi setumpuk teks tak berjarak di bawah navbar.
            "konteks-balik", "konteks-tengah", "konteks-maju", "konteks-langkah",
            # Peta bab menggantikan gulungan lima ribu piksel sebagai jawaban
            # atas "ada berapa bab dan aku di mana"; panel bantuan yang
            # menjauhkan "lihat jawaban" dari "periksa jawaban".
            "peta-bab", "bantuan", "bantuan-kepala", "bantuan-isi",
            "bantuan-akhir",
            # Bab: tanpa aturan-aturan ini daftar materi kembali jadi satu
            # senarai rata tanpa pengelompokan, dan bab yang terkunci tampak
            # persis sama dengan yang terbuka — kegagalan diam yang justru
            # jadi alasan tes ini ada.
            "bab", "bab-daftar", "bab-kepala", "bab-nomor", "bab-ket",
            "bab-maju", "bab-kunci", "bab-terkunci", "bab-lipat", "bab-isi",
            "baris-terkunci", "pil-kunci", "materi-rel-bab",
        ]
        # Dua hal harus dibereskan dulu, dan keduanya pernah membuat tes ini
        # tidak pernah bisa gagal:
        #   1. KOMENTAR dibuang. Berkas ini penuh komentar panjang yang
        #      menyebut nama kelas ("Kartu .lanjutkan adalah..."), jadi
        #      mencarinya di teks mentah selalu ketemu walau aturannya hilang.
        #   2. Batas kata, bukan substring — tanpa itu ".lanjutkan" dianggap
        #      ada hanya karena ".lanjutkan-tbl" kebetulan memuatnya.
        import re
        tanpa_komentar = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
        hilang = [k for k in wajib
                  if not re.search(r"\." + re.escape(k) + r"(?![\w-])",
                                   tanpa_komentar)]
        self.assertEqual(hilang, [],
                         f"kelas tata letak tanpa aturan di gaya.css: {hilang}")

    def test_tiga_tingkat_gerak_dikenali_gaya_dan_skrip(self):
        with open(os.path.join(self.akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            css = f.read()
        with open(os.path.join(self.js, "gerak.js"), encoding="utf-8") as f:
            gerak = f.read()
        for tingkat in ("halus", "mati"):
            self.assertIn(f'[data-gerak="{tingkat}"]', css,
                          f"gaya.css tidak mengurus tingkat {tingkat}")
            self.assertIn(f'"{tingkat}"', gerak)
        # prefers-reduced-motion wajib dihormati di KEDUA tempat: CSS untuk
        # animasi yang ditulis di sana, JS untuk yang dijalankan WAAPI.
        self.assertIn("prefers-reduced-motion", css)
        self.assertIn("prefers-reduced-motion", gerak)

class TestPenyorotJavaScript(unittest.TestCase):
    """Adu sorot.py melawan statik/js/sorot.js atas seluruh kode kurikulum.

    Dua implementasi pemindai yang sama artinya dua kesempatan untuk berbeda
    pendapat. Tes ini menutup celah itu -- dan kalau Node tidak ada, ia
    dilaporkan sebagai skipped, bukan lulus diam-diam.
    """

    @unittest.skipUnless(shutil.which("node"), "butuh node untuk mengadu penyorot")
    def test_hasil_js_identik_dengan_python(self):
        kasus = []
        for lang in api.LANGUAGES:
            b = isi.bahasa_sorot(lang)
            for m in lang["materials"]:
                for bagian in m["sections"]:
                    if "code" in bagian:
                        kasus.append({"bahasa": b, "kode": bagian["code"],
                                      "harapan": isi.token_kode(bagian["code"], b),
                                      "label": f"{lang['key']}/{m['title']}"})
            for e in lang["exercises"]:
                kasus.append({"bahasa": b, "kode": e["solution"],
                              "harapan": isi.token_kode(e["solution"], b),
                              "label": f"{lang['key']}/{e['title']}"})
        for b, kode in _KASUS_SULIT:
            kasus.append({"bahasa": b, "kode": kode,
                          "harapan": isi.token_kode(kode, b),
                          "label": f"rusak/{b}"})

        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with tempfile.TemporaryDirectory() as d:
            js = os.path.join(d, "banding.mjs")
            data = os.path.join(d, "kasus.json")
            with open(js, "w", encoding="utf-8") as f:
                f.write(_SKRIP_BANDING)
            with open(data, "w", encoding="utf-8") as f:
                json.dump({"aturan": isi.aturan_penyorot(), "kasus": kasus}, f)
            hasil = subprocess.run(
                ["node", js,
                 os.path.join(akar, "webapp", "statik", "js", "sorot.js"), data],
                capture_output=True, text=True, timeout=180)

        self.assertEqual(hasil.returncode, 0, hasil.stderr[-800:])
        laporan = json.loads(hasil.stdout)
        self.assertGreater(laporan["total"], 200, "kasus uji terlalu sedikit")
        self.assertEqual(laporan["jumlahBeda"], 0,
                         f"penyorot JS berbeda dari Python di: {laporan['beda']}")


# ----------------------------------------------------------------------- bab

class TestBabWeb(BasisWeb):
    """Kontrak JSON fitur bab, diadu dari sisi yang memakainya.

    Tes di sini sengaja menyebut NAMA BIDANG satu per satu, bukan sekadar
    memeriksa "ada babnya". Bidang yang meleset satu huruf tidak menimbulkan
    error di mana pun -- ia diam-diam menjadi `undefined` di JavaScript, dan
    yang terlihat pemakainya cuma bab yang kemajuannya selalu nol.
    """

    def _baca_tuntas(self, key, sampai):
        """Tandai materi 0..sampai-1 sebuah bahasa sudah dibaca tuntas."""
        materi = _bahasa(key)["materials"]
        for i in range(sampai):
            progress.record_material_read(f"{key}_materi", materi[i]["title"],
                                          tuntas=True)

    def test_bahasa_membawa_bab_lengkap_dengan_bidangnya(self):
        b = api.bahasa({"key": "java"})
        self.assertIn("bab", b)
        self.assertIn("bab_kalimat", b)
        self.assertIn("buka_semua_bab", b)
        self.assertGreater(len(b["bab"]), 1)
        for x in b["bab"]:
            for k in ("nomor", "judul", "ket", "tingkat", "label_tingkat",
                      "awal", "akhir", "materi", "selesai", "jumlah",
                      "kurang", "persen", "status", "alasan"):
                self.assertIn(k, x, f"bidang '{k}' hilang dari bab")

    def test_bab_menutupi_seluruh_materi_tanpa_celah(self):
        for lang in api.LANGUAGES:
            b = api.bahasa({"key": lang["key"]})
            tertutup = [i for x in b["bab"] for i in x["materi"]]
            self.assertEqual(tertutup, list(range(len(lang["materials"]))),
                             f"bab {lang['key']} tidak menutupi materinya")

    def test_tiap_materi_tahu_bab_tingkat_dan_kuncinya(self):
        b = api.bahasa({"key": "python"})
        for m in b["materi"]:
            self.assertIn("bab", m)
            self.assertIn("terkunci", m)
            self.assertIn("tingkat", m)
            self.assertIn(m["tingkat"], bab.TINGKAT)
        self.assertFalse(b["materi"][0]["terkunci"],
                         "materi pertama tidak boleh pernah terkunci")
        self.assertTrue(b["materi"][-1]["terkunci"],
                        "pada progres kosong, materi terakhir harus terkunci")

    def test_materi_terkunci_ditolak_403_dengan_alasan(self):
        b = api.bahasa({"key": "java"})
        terkunci = next(m for m in b["materi"] if m["terkunci"])
        with self.assertRaises(api.Galat) as c:
            api.materi({"key": "java", "indeks": str(terkunci["indeks"])})
        self.assertEqual(c.exception.kode, 403)
        # Pesannya harus memberi tahu apa yang kurang, bukan cuma melarang.
        self.assertTrue(str(c.exception).strip())
        self.assertNotEqual(str(c.exception).lower(), "terkunci")

    def test_materi_terbuka_membawa_babnya(self):
        m = api.materi({"key": "java", "indeks": "0"})
        self.assertIn("bab", m)
        for k in ("nomor", "judul", "tingkat", "label_tingkat", "jumlah",
                  "selesai"):
            self.assertIn(k, m["bab"])

    def test_sesudah_tidak_menunjuk_materi_terkunci(self):
        """Materi terakhir sebuah bab yang belum tuntas tidak punya "berikutnya".

        Kalau ia tetap menunjuk ke depan, tombol "lanjut" mengantar orang ke
        pintu yang dikunci oleh aplikasi yang sama -- salah satu cara tercepat
        membuat sebuah fitur terasa rusak, bukan terasa membimbing.
        """
        b = api.bahasa({"key": "java"})
        bab1 = b["bab"][0]
        self._baca_tuntas("java", bab1["jumlah"] - 1)
        m = api.materi({"key": "java", "indeks": str(bab1["akhir"] - 1)})
        self.assertEqual(m["sesudah"], "")

    def test_menuntaskan_bab_membuka_bab_berikutnya(self):
        b = api.bahasa({"key": "java"})
        bab1, bab2 = b["bab"][0], b["bab"][1]
        self.assertEqual(bab2["status"], bab.TERKUNCI)

        self._baca_tuntas("java", bab1["jumlah"])

        b2 = api.bahasa({"key": "java"})
        self.assertEqual(b2["bab"][0]["status"], bab.TUNTAS)
        self.assertEqual(b2["bab"][1]["status"], bab.TERBUKA)
        # Yang ketiga TETAP terkunci: membuka satu pintu tidak membuka semuanya.
        if len(b2["bab"]) > 2:
            self.assertEqual(b2["bab"][2]["status"], bab.TERKUNCI)
        api.materi({"key": "java", "indeks": str(bab2["awal"])})

    def test_membaca_sebagian_tidak_membuka_bab_berikutnya(self):
        b = api.bahasa({"key": "java"})
        materi = _bahasa("java")["materials"]
        for i in range(b["bab"][0]["jumlah"]):
            progress.record_material_read("java_materi", materi[i]["title"],
                                          tuntas=False)
        self.assertEqual(api.bahasa({"key": "java"})["bab"][1]["status"],
                         bab.TERKUNCI)

    def test_saklar_buka_semua_membuka_semua_bab(self):
        konfigurasi.pasang("buka_semua_bab", True)
        try:
            b = api.bahasa({"key": "java"})
            self.assertTrue(b["buka_semua_bab"])
            for x in b["bab"]:
                self.assertNotEqual(x["status"], bab.TERKUNCI)
            for m in b["materi"]:
                self.assertFalse(m["terkunci"])
            # Dan materinya benar-benar bisa dibuka, bukan cuma tampak terbuka.
            api.materi({"key": "java", "indeks": str(b["bab"][-1]["awal"])})
        finally:
            konfigurasi.pasang("buka_semua_bab", False)

    def test_saklar_bisa_dinyalakan_dari_web(self):
        r = api.konfigurasi_tulis({"buka_semua_bab": True})
        try:
            self.assertTrue(r["diubah"]["buka_semua_bab"])
            self.assertTrue(api.bahasa({"key": "css"})["buka_semua_bab"])
        finally:
            konfigurasi.pasang("buka_semua_bab", False)

    def test_langkah_berikutnya_tidak_pernah_menunjuk_materi_terkunci(self):
        """Saran yang mengantar ke pintu terkunci adalah bug, bukan sekadar
        ketidakrapian: aplikasi menyuruh mengerjakan sesuatu lalu menolaknya."""
        self._baca_tuntas("java", 3)
        d = api.dasbor()
        for s in d.get("langkah", []):
            if s.get("tipe") != "materi":
                continue
            lang = _bahasa(s["bahasa"])
            judul = [m["title"] for m in lang["materials"]]
            self.assertIn(s["judul"], judul)
            idx = judul.index(s["judul"])
            self.assertFalse(bab.terkunci(lang, idx),
                             f"langkah menunjuk materi terkunci: {s['judul']}")


def _panen_butir(butir, keluar):
    """Kumpulkan SELURUH teks di dalam pohon butir, termasuk sarang dan contoh.

    Sebuah butir menyimpan kalimat pertamanya di `teks`, sisanya di `blok`, dan
    daftar anaknya di `anak`. Melupakan salah satunya membuat tes kesamaan isi
    lolos untuk kalimat yang sebenarnya tidak pernah sampai ke layar.
    """
    for x in butir:
        keluar.append(x.get("teks") or "")
        for sub in x.get("blok") or []:
            keluar.append(sub.get("teks") or "")
        if x.get("anak"):
            _panen_butir(x["anak"]["butir"], keluar)


class TestIsiSamaDenganTerminal(BasisWeb):
    """Web dan terminal harus menampilkan ISI yang sama untuk materi yang sama.

    Bukan tata letak yang sama — itu memang sengaja berbeda — melainkan tidak
    ada kalimat yang muncul di satu antarmuka lalu hilang di antarmuka lain.
    Kegagalan seperti itu tidak menimbulkan error di mana pun, dan orang yang
    membaca di browser tidak punya cara tahu ada yang tidak ia lihat.
    """

    def _prosa_web(self, materi, lang):
        keluar = []
        for b in isi.bagian_materi(materi, lang):
            if b["jenis"] != "prosa":
                continue
            for blok in b["blok"]:
                keluar.append(blok.get("teks") or "")
                _panen_butir(blok.get("butir") or [], keluar)
        return " ".join(keluar)

    def test_bagian_bercode_tidak_membuang_prosanya(self):
        """Regresi: `if "code" in bagian: ... else: ...` membuang body-nya.

        Nol dari materi yang ada mencampur body dan code dalam satu bagian,
        jadi bug ini tidak pernah terlihat — ia menunggu materi baru pertama
        yang menulisnya untuk mulai menyembunyikan penjelasan.
        """
        lang = _bahasa("java")
        materi = {"title": "Uji", "sections": [
            {"heading": "Campur", "body": ["kalimat yang wajib terlihat"],
             "code": "int x = 1;"},
        ]}
        jenis = [b["jenis"] for b in isi.bagian_materi(materi, lang)]
        self.assertEqual(jenis, ["prosa", "kode"])
        self.assertIn("kalimat yang wajib terlihat",
                      self._prosa_web(materi, lang))

    def test_judul_bagian_tidak_tercetak_dua_kali(self):
        lang = _bahasa("java")
        materi = {"title": "Uji", "sections": [
            {"heading": "Sekali saja", "body": ["prosa"], "code": "int x;"},
        ]}
        judul = [b["judul"] for b in isi.bagian_materi(materi, lang)]
        self.assertEqual(judul.count("Sekali saja"), 1)

    @staticmethod
    def _huruf(teks):
        """Hanya huruf dan angka, dikecilkan.

        `blok_badan` memang MERAPIKAN prosa untuk web: penanda daftar ("- ",
        "3. ") dipindahkan jadi struktur, indentasi dibuang, baris disambung.
        Membandingkan teks mentah karena itu akan menuduh perapian sebagai
        kehilangan. Yang diuji di sini cuma satu: apakah HURUF-HURUFNYA masih
        ada di sisi web, atau ada kalimat yang benar-benar lenyap.
        """
        return "".join(c.lower() for c in teks if c.isalnum())

    def test_seluruh_kurikulum_tampil_utuh_di_kedua_antarmuka(self):
        """Setiap baris body di SETIAP materi harus sampai ke sisi web."""
        from layar import materials
        for lang in api.LANGUAGES:
            for m in lang["materials"]:
                web = self._huruf(self._prosa_web(m, lang))
                for bagian in m["sections"]:
                    for baris in bagian.get("body") or []:
                        # Penanda daftar di awal baris ("- ", "3. ") memang
                        # dipindahkan jadi struktur oleh blok_badan, jadi
                        # angkanya sengaja dibuang dari kedua sisi sebelum
                        # dibandingkan.
                        inti = self._huruf(
                            re.sub(r"^\s*(?:[-*\u2022]|\d+[.)])\s+", "", baris))
                        if len(inti) < 12:
                            continue     # baris kosong atau garis hias
                        with self.subTest(bahasa=lang["key"],
                                          materi=m["title"], baris=baris[:50]):
                            self.assertIn(inti, web,
                                          "baris ini terbaca di terminal tapi "
                                          "tidak pernah sampai ke web")
                self.assertIn(m["title"], materials.teks_polos(m))


if __name__ == "__main__":
    unittest.main()
