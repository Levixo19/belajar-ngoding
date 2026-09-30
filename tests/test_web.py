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


_SKRIP_INTI_NODE = r"""
// Jam dibekukan SEBELUM modulnya diimpor, dan sengaja pada saat di mana tanggal
// LOKAL berbeda dari tanggal UTC. Tanpa itu `hariIniISO()` yang salah (memakai
// toISOString) akan lolos di sebagian besar jam dalam sehari, dan tes yang cuma
// lolos "biasanya" lebih buruk daripada tidak ada tes.
const ASLI = Date;
const BEKU = Number(process.argv[3]);
function Beku(...a) { return a.length ? new ASLI(...a) : new ASLI(BEKU); }
Beku.now = () => BEKU;
Beku.parse = ASLI.parse;
Beku.UTC = ASLI.UTC;
Beku.prototype = ASLI.prototype;
globalThis.Date = Beku;

// inti.js memang berbicara kepada DOM; yang diuji di sini bukan itu, jadi
// permukaannya dipalsukan seadanya supaya modulnya bisa dimuat di Node.
const boneka = () => new Proxy(function () {}, {
  get(_, k) { return k === "then" ? undefined : boneka(); },
  set() { return true; },
  apply() { return boneka(); },
  construct() { return boneka(); },
});
globalThis.window = boneka();
globalThis.document = boneka();
// localStorage sungguhan (di memori), bukan boneka yang menelan tulisan:
// `sudahPernah()` HARUS bisa membaca kembali apa yang barusan ditulisnya,
// dan boneka yang selalu mengembalikan null membuat tes itu selalu hijau.
const simpanan = new Map();
globalThis.localStorage = {
  getItem: (k) => (simpanan.has(k) ? simpanan.get(k) : null),
  setItem: (k, v) => simpanan.set(k, String(v)),
  removeItem: (k) => simpanan.delete(k),
};

const m = await import(process.argv[2]);
const hariIni = m.hariIniISO();
const geser = (n) => {
  const t = new ASLI(BEKU);
  t.setDate(t.getDate() + n);
  const dua = (x) => String(x).padStart(2, "0");
  return `${t.getFullYear()}-${dua(t.getMonth() + 1)}-${dua(t.getDate())}`;
};

console.log(JSON.stringify({
  zona: process.env.TZ,
  // Pembanding bebas: `sv-SE` memformat tanggal LOKAL sebagai YYYY-MM-DD, jadi
  // ia perhitungan kedua yang tidak memakai satu baris pun kode yang diuji.
  hariIniISO: hariIni,
  hariIniPembanding: new ASLI(BEKU).toLocaleDateString("sv-SE"),
  hariIniUTC: new ASLI(BEKU).toISOString().slice(0, 10),
  // date-only: yang dulu bergeser sehari
  tanggalDariDateOnly: m.tanggalRamah("2026-09-28"),
  // timestamp naive: TIDAK boleh bergeser satu jam maupun satu hari
  tanggalDariTimestamp: m.tanggalRamah("2026-09-28T07:15:00"),
  jamDariTimestamp: m.jamRamah("2026-09-28T07:15:00"),
  // konvensi tanda: masa depan positif, masa lalu negatif
  selisihHariIni: m.selisihHari(hariIni),
  selisihBesok: m.selisihHari(geser(1)),
  selisihKemarin: m.selisihHari(geser(-1)),
  selisihSepekanLalu: m.selisihHari(geser(-7)),
  // masukan rusak tetap tidak melempar
  selisihKosong: m.selisihHari(""),
  tanggalNgawur: m.tanggalRamah("bukan tanggal"),
  // penanda upacara: panggilan pertama harus false, kedua true
  upacaraPertama: m.sudahPernah("hijauPertama"),
  upacaraKedua: m.sudahPernah("hijauPertama"),
  upacaraLain: m.sudahPernah("upacaraLain"),
  kunciTersimpan: [...simpanan.keys()].sort(),
}));
"""


class TestKonvensiTanggalJavaScript(unittest.TestCase):
    """Satu konvensi tanggal, diadu di dua zona waktu yang berlawanan.

    Spesifikasi ECMAScript mengurai dua bentuk ISO dengan aturan berbeda:
    `"2026-09-28"` (date-only) dibaca sebagai tengah malam **UTC**, sedangkan
    `"2026-09-28T07:15:00"` (tanpa offset) dibaca sebagai tengah malam
    **lokal**. Server ini menulis keduanya dan memaksudkan keduanya waktu
    setempat, jadi hanya bentuk pertama yang perlu ditolong.

    Dua bug nyata yang melahirkan tes ini, dan keduanya diam:

      · `tanggalRamah("2026-09-28")` mengembalikan 27/9/2026 di bujur barat,
        jadi setiap tooltip sel bara salah sehari bagi sebagian dunia.
      · `new Date().toISOString().slice(0, 10)` memberi tanggal UTC, jadi sel
        "hari ini" kehilangan cincinnya sepanjang pagi di UTC+8.

    Yang dijaga bukan nilai tertentu melainkan KESAMAAN lintas zona: tanggal
    yang sama harus terbaca sama di Asia/Makassar dan Pacific/Niue. Itu
    membuatnya peka dua arah -- membuang `"T00:00:00"` memerahkannya, dan
    menempelkannya ke cap waktu (yang sudah benar) juga memerahkannya.
    """

    # Jam beku dipilih supaya tanggal lokal BERBEDA dari tanggal UTC di
    # masing-masing zona; kalau tidak, `hariIniISO()` yang salah lolos.
    ZONA = {
        # 2026-09-28T20:00Z -> 29/9 pukul 04:00 di UTC+8
        "Asia/Makassar": (1790625600000, "2026-09-29"),
        # 2026-09-28T05:00Z -> 27/9 pukul 18:00 di UTC-11
        "Pacific/Niue": (1790571600000, "2026-09-27"),
    }

    @unittest.skipUnless(shutil.which("node"), "butuh node untuk menguji inti.js")
    def test_tanggal_sama_di_dua_zona_berlawanan(self):
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        jalur = os.path.join(akar, "webapp", "statik", "js", "inti.js")

        hasil = {}
        with tempfile.TemporaryDirectory() as d:
            js = os.path.join(d, "uji-tanggal.mjs")
            with open(js, "w", encoding="utf-8") as f:
                f.write(_SKRIP_INTI_NODE)
            for zona, (beku, _) in self.ZONA.items():
                lingkungan = dict(os.environ, TZ=zona)
                jalan = subprocess.run(["node", js, jalur, str(beku)],
                                       capture_output=True, text=True,
                                       timeout=60, env=lingkungan)
                self.assertEqual(jalan.returncode, 0, jalan.stderr[-1200:])
                hasil[zona] = json.loads(jalan.stdout)

        barat, timur = hasil["Pacific/Niue"], hasil["Asia/Makassar"]

        # 1. Tanggal date-only terbaca sebagai hari yang SAMA di dua bujur.
        self.assertEqual(barat["tanggalDariDateOnly"], timur["tanggalDariDateOnly"],
                         "tanggal date-only bergeser antar zona: ISO date-only "
                         "diurai sebagai tengah malam UTC")
        self.assertIn("28", timur["tanggalDariDateOnly"])

        # 2. Cap waktu naive TIDAK boleh ikut bergeser -- tidak sehari, tidak
        #    sejam. Ia sudah benar sebelum konvensi ini ada.
        self.assertEqual(barat["jamDariTimestamp"], timur["jamDariTimestamp"],
                         "cap waktu bergeser antar zona; konvensinya menempel "
                         "'T00:00:00' pada masukan yang tidak memintanya")
        self.assertEqual(barat["tanggalDariTimestamp"], timur["tanggalDariTimestamp"])
        self.assertIn("28", timur["tanggalDariTimestamp"])
        self.assertIn("07", timur["jamDariTimestamp"],
                      "jam 07:15 berubah jam; cap waktu tidak boleh disentuh")

        # Keduanya harus benar-benar TERFORMAT. Tanpa dua baris ini, konvensi
        # yang menempelkan "T00:00:00" ke SEMUA masukan tetap lolos: cap waktu
        # jadi Invalid Date, helpernya mengembalikan string mentah apa adanya,
        # dan string mentah itu kebetulan sama di kedua zona sekaligus memuat
        # "28" dan "07". Versi pertama tes ini memang lolos untuk mutasi itu.
        for nama in ("tanggalDariTimestamp", "jamDariTimestamp", "tanggalDariDateOnly"):
            self.assertIn("Sep", timur[nama],
                          f"{nama} tidak terformat -- masukannya diurai sebagai "
                          "tanggal tidak sah dan dikembalikan mentah")
            self.assertNotIn("T", timur[nama],
                             f"{nama} masih berbentuk ISO mentah, bukan hasil format")

        # 3. "Hari ini" adalah hari menurut jam DINDING, bukan menurut UTC.
        for zona, (_, harusnya) in self.ZONA.items():
            r = hasil[zona]
            self.assertEqual(r["hariIniISO"], harusnya, f"hariIniISO salah di {zona}")
            self.assertEqual(r["hariIniISO"], r["hariIniPembanding"],
                             f"hariIniISO tidak cocok dengan tanggal lokal di {zona}")
            self.assertNotEqual(
                r["hariIniISO"], r["hariIniUTC"],
                f"jam beku di {zona} tidak lagi membedakan tanggal lokal dari "
                "UTC, jadi tes ini berhenti bisa gagal -- pilih jam lain")

    @unittest.skipUnless(shutil.which("node"), "butuh node untuk menguji inti.js")
    def test_tanda_selisih_hari_masa_lalu_negatif(self):
        """Arah `selisihHari()` adalah kontrak, bukan detail.

        `jadwalRamah()` membaca `<= 0` sebagai "sudah waktunya diulang" dan
        `celahBelajar()` membalikkannya jadi "N hari lalu". Membalik tandanya
        suatu hari nanti akan menukar kedua kalimat itu sekaligus, dan tidak
        ada satu pun tes lain di repo ini yang akan menyadarinya.
        """
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        jalur = os.path.join(akar, "webapp", "statik", "js", "inti.js")
        with tempfile.TemporaryDirectory() as d:
            js = os.path.join(d, "uji-tanggal.mjs")
            with open(js, "w", encoding="utf-8") as f:
                f.write(_SKRIP_INTI_NODE)
            for zona, (beku, _) in self.ZONA.items():
                jalan = subprocess.run(
                    ["node", js, jalur, str(beku)], capture_output=True,
                    text=True, timeout=60, env=dict(os.environ, TZ=zona))
                self.assertEqual(jalan.returncode, 0, jalan.stderr[-1200:])
                r = json.loads(jalan.stdout)
                self.assertEqual(r["selisihHariIni"], 0, zona)
                self.assertEqual(r["selisihBesok"], 1, f"{zona}: besok harus +1")
                self.assertEqual(r["selisihKemarin"], -1,
                                 f"{zona}: masa lalu harus NEGATIF")
                self.assertEqual(r["selisihSepekanLalu"], -7, zona)
                self.assertIsNone(r["selisihKosong"], zona)
                self.assertEqual(r["tanggalNgawur"], "bukan tanggal", zona)


class TestHamparanBara(unittest.TestCase):
    """Hamparan 26 pekan: konversi hari, pembagian mesin, dan kata yang dipakai.

    Tiga hal yang tidak terlihat dari membaca kodenya sepintas, dan ketiganya
    sudah pernah salah di repo ini atau di paket promptnya.
    """

    @staticmethod
    def _berkas(*bagian):
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, *bagian), encoding="utf-8") as f:
            return f.read()

    # Apa saja yang hanya bisa dijawab benar SESUDAH tata letak jadi. Semuanya
    # mengembalikan nol pada elemen yang masih lepas dari dokumen, dan nol itu
    # tidak pernah datang sebagai galat. `bawaKeTengah(` ikut masuk karena ia
    # membaca ketiganya di dalam dirinya.
    BACA_TATA_LETAK = (r"scrollWidth", r"clientWidth", r"offsetWidth",
                       r"offsetHeight", r"scrollHeight", r"clientHeight",
                       r"getBoundingClientRect", r"bawaKeTengah\(")

    @staticmethod
    def _telanjang(src):
        """Buang komentar. Tanpa ini tes menghukum penjelasannya sendiri."""
        src = re.sub(r"/\*.*?\*/", " ", src, flags=re.S)
        return re.sub(r"//[^\n]*", " ", src)

    @staticmethod
    def _kedalaman(badan):
        """[(indeks, kedalaman kurung)] relatif badan fungsi; badan = kedalaman 1."""
        dalam = 0
        peta = []
        for i, c in enumerate(badan):
            if c == "{":
                dalam += 1
            peta.append((i, dalam))
            if c == "}":
                dalam -= 1
        return peta

    @staticmethod
    def _fungsi(src, nama):
        """Badan satu fungsi tingkat-modul, dipotong dengan hitung kurung.

        Daftar parameternya dilewati dulu. Versi pertama mengambil `{` PERTAMA
        sesudah namanya, dan untuk `layarBahasa({ key }, ctx)` itu kurung
        parameter yang didekonstruksi — bukan badan fungsinya. Yang dikembalikan
        jadi potongan sepanjang `function layarBahasa({ key }`, dan asersi apa
        pun di atasnya gagal dengan alasan yang menyesatkan.
        """
        awal = src.index(f"function {nama}(")
        buka = src.index("(", awal)
        dalam = 0
        tutup = None
        for j in range(buka, len(src)):
            if src[j] == "(":
                dalam += 1
            elif src[j] == ")":
                dalam -= 1
                if dalam == 0:
                    tutup = j
                    break
        assert tutup is not None, f"daftar parameter {nama} tidak tertutup"
        i = src.index("{", tutup)
        dalam = 0
        for j in range(i, len(src)):
            if src[j] == "{":
                dalam += 1
            elif src[j] == "}":
                dalam -= 1
                if dalam == 0:
                    return src[awal:j + 1]
        raise AssertionError(f"fungsi {nama} tidak tertutup")

    def test_kolom_pertama_jatuh_di_senin(self):
        """`(getDay() + 6) % 7` adalah konversi Minggu-pertama ke Senin-pertama.

        `Date.getDay()` mengembalikan 0 untuk MINGGU. Kisi ini berbaris
        Senin..Minggu, jadi angkanya harus diputar satu. Menghapus `+ 6`
        menggeser seluruh hamparan sehari tanpa satu pun sel yang hilang --
        kesalahan yang terlihat rapi dan karena itu tidak pernah dilaporkan.
        """
        badan = self._fungsi(
            self._berkas("webapp", "statik", "js", "layar-belajar.js"), "blokBara")
        self.assertIn("(tanggalLokal(pertama.tanggal).getDay() + 6) % 7", badan,
                      "konversi Senin-pertama hilang atau berubah bentuk")

        # Adu rumusnya dengan tabel kebenaran, supaya yang dijaga artinya dan
        # bukan cuma teksnya: Senin -> 0 baris pengisi, Minggu -> 6.
        for getday, harusnya in enumerate([6, 0, 1, 2, 3, 4, 5]):   # 0=Minggu
            self.assertEqual((getday + 6) % 7, harusnya)

    def test_kisi_dibuka_pada_hari_ini(self):
        """Pin gulir harus punya BENTUK yang benar, bukan cuma ada.

        Versi pertama tes ini cuma menuntut barisnya ADA, dan dua mutasi lolos
        795 tes karenanya:

          (a) pin dipindah keluar dari callback sehingga dijalankan saat
              elemennya masih lepas dari dokumen -- `scrollWidth` nol, pin jadi
              nol, rusak di SEMUA jalur, suite hijau;
          (b) baris `geser.hidden = ...` dihapus -- penandanya melaporkan
              "tidak ada yang tersembunyi" sementara lima bulan di luar kotak,
              suite hijau.

        Terukur, empat jalur pemuatan x dua lebar, sebelum perbaikan:

          jalur = pemuatan-pertama | reload | kembali-lewat-rute | dari-bahasa
          360 px :  80 v |  80 v |   0 X |   0 X
          1100 px:  80 X | 117 v |   0 X |   0 X

        `requestAnimationFrame` polos hanya menang di pemuatan yang beruntung,
        dan di 1100 px pemuatan-pertama ia menang TERLALU CEPAT: kotaknya masih
        menyusut 299 -> 262 sesudah itu, jadi 80 mendarat di tempat yang benar
        untuk kotak yang sudah tidak ada.
        """
        js = self._berkas("webapp", "statik", "js", "layar-belajar.js")

        # 1. `blokBara` mendelegasikan, dan tidak mem-pin sendiri.
        bb = self._telanjang(self._fungsi(js, "blokBara"))
        self.assertRegex(bb, r"pinKeHariIni\(\s*petak",
                         "`blokBara` tidak lagi memanggil pin-nya")
        self.assertNotIn("scrollLeft", bb, "`blokBara` mem-pin sendiri lagi")
        self.assertNotIn("requestAnimationFrame", bb,
                         "`blokBara` memakai rAF polos; ia kalah di jalur "
                         "'kembali lewat rute' dan pin-nya jadi nol")

        badan = self._telanjang(self._fungsi(js, "pinKeHariIni"))

        # 2. TIDAK ADA pembacaan tata letak di kedalaman 1 -- yaitu langsung di
        #    badan fungsi, sebelum satu pun callback. Ini yang menangkap mutasi
        #    (a): memindahkan pin ke luar callback menaikkannya ke kedalaman 1.
        peta = dict(self._kedalaman(badan))
        for pola in self.BACA_TATA_LETAK:
            for m in re.finditer(pola, badan):
                self.assertGreaterEqual(
                    peta[m.start()], 2,
                    f"`{m.group(0)}` dibaca langsung di badan `pinKeHariIni`, "
                    "bukan di dalam callback; pada jalur pemuatan yang lambat "
                    "elemennya masih lepas dan nilainya nol")

        # 3. SATU-SATUNYA yang dijalankan langsung di badan fungsi adalah
        #    `saatSiap(...)`. Memeriksa token tata letak saja tidak cukup:
        #    mutasi (a) memindahkan PEMANGGILAN `pasang()` ke kedalaman 1, dan
        #    pemanggilan itu tidak memuat satu pun token -- versi pertama tes
        #    ini lolos untuk mutasi tersebut.
        panggil = sorted({m.group(1) for m in
                          re.finditer(r"\b([A-Za-z_$][\w$]*)\s*\(", badan)
                          if peta[m.start()] == 1})
        self.assertEqual(
            panggil, ["saatSiap"],
            "ada yang dijalankan langsung di badan `pinKeHariIni` selain "
            f"`saatSiap()`: {panggil}. Apa pun di sana berjalan sebelum "
            "elemennya punya ukuran, dan pin-nya jadi nol tanpa pesan galat")
        self.assertNotIn("requestAnimationFrame", badan,
                         "`pinKeHariIni` memakai rAF polos; `saatSiap` yang "
                         "menunggu elemennya benar-benar punya ukuran")

        # 4. Pin dan kondisi penanda di SATU blok kurung yang sama. Ini yang
        #    menangkap mutasi (b) dan juga penanda yang dihitung di tempat lain
        #    dengan kotak yang berbeda.
        i_pin = badan.index("scrollLeft")
        i_tanda = badan.index(".hidden")
        awal_blok = badan.rindex("{", 0, i_pin)
        dalam = 0
        akhir_blok = None
        for j in range(awal_blok, len(badan)):
            if badan[j] == "{":
                dalam += 1
            elif badan[j] == "}":
                dalam -= 1
                if dalam == 0:
                    akhir_blok = j
                    break
        self.assertIsNotNone(akhir_blok)
        self.assertTrue(
            awal_blok < i_tanda < akhir_blok,
            "kondisi `geser.hidden` tidak berada di blok yang sama dengan "
            "pin-nya; ia akan menjawab pertanyaan tentang kotak yang lain")

        # 5. Pengamat ukuran WAJIB bisa lepas, dan lepas karena dua sebab.
        #    Posisi gulir adalah keadaan PENGGUNA: merebutnya kembali sesudah
        #    dia menggeser sendiri lebih buruk daripada tidak mem-pin.
        for potongan, pesan in (
            ("new ResizeObserver(", "tidak ada pengamat ukuran yang dibuat; pin "
                                    "pertama salah di 1100 px karena kotaknya "
                                    "menyusut sesudahnya"),
            (".observe(", "pengamat ukuran dibuat tapi tidak pernah dipasang"),
            ("disconnect()", "pengamat ukuran tidak pernah diputus"),
            ("removeEventListener", "pendengar pelepas tidak pernah dilepas"),
            ("clearTimeout", "batas waktu pelepasan tidak pernah dibatalkan"),
        ):
            self.assertIn(potongan, badan, pesan)
        for isyarat in ("wheel", "pointerdown", "keydown"):
            self.assertIn(isyarat, js,
                          f"`{isyarat}` bukan lagi isyarat bahwa pengguna sudah "
                          "mengambil alih gulirnya")

        # 6. Larangan yang sama seperti sebelumnya.
        self.assertNotIn("scrollIntoView", badan,
                         "`scrollIntoView` menggulir seluruh leluhur dan akan "
                         "menggeser halaman -- lihat `bawaKeTengah()`")
        self.assertNotIn("scrollBehavior", badan)
        self.assertNotIn("scroll-behavior", badan)

    def test_kisi_terjangkau_papan_ketik_tanpa_mengganggu_ubin(self):
        """Wadah yang menggulir wajib bisa difokus, dan `.ubin` tidak terusik.

        Di Chrome dan Safari, wadah `overflow-x: auto` tanpa `tabindex` tidak
        bisa digulir papan ketik sama sekali. Sebelum pin, yang tak terjangkau
        adalah bulan terbaru; sesudah pin, lima bulan pertamanya -- jadi pin
        yang benar justru menaikkan harga kelalaian ini.

        Yang menjaga `.ubin` bukan urutan tab-nya melainkan sesuatu yang lebih
        kuat: `.bara-petak` lahir di `blokBara` (dipakai `dasborBerjalan`)
        sedangkan `.ubin-bahasa` di `kisiUbin` (dipakai `layarMulai`), dan
        `layarDasbor` memilih SALAH SATU lewat `d.xp === 0`. Keduanya tidak
        pernah ada di halaman yang sama. Tes ini mengunci pemisahan itu, karena
        begitu ia hilang, roving tabindex dan `tabindex="0"` biasa akan berbagi
        satu urutan tab tanpa ada yang menyadarinya.
        """
        js = self._berkas("webapp", "statik", "js", "layar-belajar.js")
        bb = self._telanjang(self._fungsi(js, "blokBara"))

        self.assertRegex(bb, r'tabindex:\s*"0"',
                         "`.bara-petak` tidak bisa difokus; pengguna papan ketik "
                         "tidak punya cara menggeser kisinya")
        self.assertRegex(bb, r'role:\s*"group"', "`.bara-petak` tanpa role")
        m = re.search(r'"aria-label":\s*"([^"]+)"', bb)
        self.assertIsNotNone(m, "`.bara-petak` tanpa nama yang diumumkan")
        self.assertRegex(m.group(1).lower(), r"geser|gulir",
                         "nama yang diumumkan tidak menyebut bahwa isinya digeser")

        # Penanda menyebut ARAH: sesudah pin, yang tersembunyi ada di KIRI.
        tanda = re.search(r'span\.bara-geser"[^)]*?,\s*\n?\s*"([^"]+)"', bb, re.S)
        self.assertIsNotNone(tanda, "teks penanda geser tidak terbaca")
        self.assertIn("kiri", tanda.group(1).lower(),
                      "penanda tidak menyebut arah; sesudah pin, yang "
                      "tersembunyi ada di kiri, dan penanda tanpa arah "
                      "menyuruh orang mencari ke tempat yang salah")

        # Pemisahan dua layar, dibaca dari pemanggilnya.
        mulai = self._telanjang(self._fungsi(js, "layarMulai"))
        berjalan = self._telanjang(self._fungsi(js, "dasborBerjalan"))
        self.assertIn("kisiUbin(", mulai)
        self.assertNotIn("blokBara(", mulai,
                         "`layarMulai` sekarang memuat hamparan bara juga; "
                         "roving tabindex `.ubin` dan `tabindex=0` milik "
                         "`.bara-petak` akan berbagi satu urutan tab")
        self.assertIn("blokBara(", berjalan)
        self.assertNotIn("kisiUbin(", berjalan,
                         "`dasborBerjalan` sekarang memuat kisi ubin juga; "
                         "lihat pesan di atas")

        # Roving tabindex `.ubin` masih satu titik masuk per kisi.
        panah = self._telanjang(self._fungsi(js, "panahAntarUbin"))
        self.assertRegex(panah, r"tabIndex\s*=\s*i === 0 \? 0 : -1",
                         "roving tabindex `.ubin` berubah bentuk; satu kisi "
                         "harus punya tepat satu titik masuk")

    def test_rAF_polos_tidak_mengukur_tata_letak(self):
        """Sapuan: `requestAnimationFrame` polos tidak boleh mengukur apa pun.

        Ini pagar untuk KELAS bug, bukan untuk satu tempat. Satu frame tidak
        cukup: layar dibangun utuh sebelum router menempelkannya, dan router
        masih menunggu animasi keluar layar sebelumnya. Jadi rAF yang mengukur
        bisa mengembalikan nol -- dan yang terjadi bukan galat melainkan diam,
        cuma di sebagian pemuatan, tergantung frame mana yang menang.

        Pembantunya sudah ada: `saatSiap()`, yang menunggu `isConnected` DAN
        `clientWidth > 0`. Yang boleh memakai rAF polos hanyalah `saatSiap`
        sendiri, dan callback yang tidak mengukur apa pun.
        """
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dirjs = os.path.join(akar, "webapp", "statik", "js")
        pelanggaran = []
        for nama in sorted(n for n in os.listdir(dirjs)
                           if n.startswith("layar-") and n.endswith(".js")):
            with open(os.path.join(dirjs, nama), encoding="utf-8") as f:
                mentah = f.read()
            src = self._telanjang(mentah)

            # Rentang badan `saatSiap` sendiri: dua rAF di dalamnya memang
            # mesinnya, bukan pemakainya.
            kebal = []
            if "function saatSiap(" in src:
                badan = self._fungsi(src, "saatSiap")
                i = src.index(badan)
                kebal.append((i, i + len(badan)))

            for m in re.finditer(r"requestAnimationFrame\s*\(", src):
                if any(a <= m.start() < b for a, b in kebal):
                    continue
                # Ambil argumennya dengan hitung kurung.
                i, dalam = m.end() - 1, 0
                arg = ""
                for j in range(i, len(src)):
                    if src[j] == "(":
                        dalam += 1
                    elif src[j] == ")":
                        dalam -= 1
                        if dalam == 0:
                            arg = src[i + 1:j]
                            break
                for pola in self.BACA_TATA_LETAK:
                    if re.search(pola, arg):
                        baris = src[:m.start()].count("\n") + 1
                        pelanggaran.append(f"{nama}:{baris} -> {pola}")
                        break

        self.assertEqual(
            pelanggaran, [],
            "requestAnimationFrame polos yang mengukur tata letak; pakai "
            "`saatSiap()` -- satu frame tidak menjamin elemennya sudah "
            "terpasang, dan nilainya nol tanpa pesan galat: "
            + "; ".join(pelanggaran))

    def test_kanal_ukuran_kontras_bertahan_di_dua_tebal_garis(self):
        """Inti berwarna tetap terbedakan berapa pun `--tebal-garis` nanti.

        Inti = 11 - 2*border - 2*cincin. Hari ini border 1 px di SEMUA tema,
        termasuk kontras: `[data-tema="kontras"] { --tebal-garis: 2px }` dan
        `:root { --tebal-garis: 1px }` sama-sama berspesifisitas 0,1,0 pada
        elemen <html> yang sama, jadi yang belakangan menang. Token itu bisa
        dihidupkan lagi kapan saja -- itu urusan S12, bukan blok bara -- dan
        begitu ia hidup, cincin 3px/1,5px membuat tingkat 1 menyusut jadi 1 px.

        Yang dikunci di sini bukan angka cincinnya melainkan SIFATNYA: langkah
        antar tingkat >= 2 px dan tingkat terkecil >= 2 px, di KEDUA nilai
        border yang mungkin.
        """
        css = re.sub(r"/\*.*?\*/", " ",
                     self._berkas("webapp", "statik", "gaya.css"), flags=re.S)
        cincin = {}
        for m in re.finditer(
                r'\[data-tema="kontras"\]\s*\.bara-([123])\s*\{[^}]*box-shadow:\s*'
                r'inset\s+0\s+0\s+0\s+([\d.]+)px', css):
            cincin[int(m.group(1))] = float(m.group(2))
        self.assertEqual(sorted(cincin), [1, 2],
                         "cincin kontras hanya boleh dipasang pada tingkat 1 dan 2; "
                         f"terbaca {sorted(cincin)}")
        cincin[3] = 0.0

        SEL = 11.0
        for border in (1.0, 2.0):
            inti = {t: SEL - 2 * border - 2 * cincin[t] for t in (1, 2, 3)}
            self.assertGreaterEqual(
                inti[1], 2.0,
                f"border {border:g}px: inti tingkat 1 tinggal {inti[1]:g}px -- "
                "kanal ukurannya hilang justru di tema yang paling membutuhkannya")
            for a, b in ((1, 2), (2, 3)):
                self.assertGreaterEqual(
                    inti[b] - inti[a], 2.0,
                    f"border {border:g}px: inti {a}->{b} cuma beda "
                    f"{inti[b] - inti[a]:g}px")

        # Cincin tidak boleh dipakai di tema lain: di sana empat tingkat sudah
        # terbedakan oleh terang-gelap, dan bentuk tambahan cuma jadi kebisingan.
        for m in re.finditer(r"([^{}]*\.bara-[123][^{}]*)\{([^{}]*)\}", css):
            if "box-shadow" in m.group(2):
                self.assertIn('[data-tema="kontras"]', m.group(1),
                              "cincin bentuk bocor ke tema selain kontras")

    def test_sel_bara_memisahkan_scale_waapi_dari_transform_css(self):
        """Satu properti satu mesin, dibuktikan dari kedua sisinya sekaligus.

        Animasi masuk tiap sel ditulis WAAPI; pembesaran hover ditulis CSS.
        Selama keduanya memakai `transform`, keduanya menulis properti yang
        sama tiap frame dan gejalanya bukan galat melainkan sel yang tersendat.
        Pemisahannya: WAAPI memakai `scale` (properti transform mandiri, yang
        disusun sebelum `transform`), CSS tetap memakai `transform`.

        Tes ini menagih kedua arah, karena memperbaiki satu sisi saja adalah
        persis bentuk regresi yang sudah terjadi tiga kali di repo ini.
        """
        js = self._berkas("webapp", "statik", "js", "layar-belajar.js")
        nyala = self._fungsi(js, "nyalakanBara")
        self.assertIn("scale:", nyala, "animasi masuk bara tidak lagi memakai `scale`")
        self.assertNotIn("transform:", nyala,
                         "`nyalakanBara` menulis `transform`, properti yang sudah "
                         "dipegang transition CSS `.bara-sel`")

        css = re.sub(r"/\*.*?\*/", " ",
                     self._berkas("webapp", "statik", "gaya.css"), flags=re.S)
        for sel, isi in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
            if not re.search(r"\.bara-(sel|1|2|3|kini|kosong)\b", sel):
                continue
            for pr in ("scale", "translate", "rotate"):
                self.assertNotRegex(
                    isi, rf"\b{pr}\s*:",
                    f"`{sel.strip()}` menyetel `{pr}` di CSS; properti itu milik "
                    "WAAPI di `nyalakanBara`")
                self.assertNotRegex(
                    isi, rf"\btransition[^;]*\b{pr}\b",
                    f"`{sel.strip()}` menaruh `{pr}` di daftar transition; itu "
                    "mesin kedua pada properti yang sudah punya mesin")

    def test_pengisi_depan_tidak_menyalin_ukuran_sel(self):
        """Ukuran sel hidup di CSS, satu kali.

        Pengisi depan dulu menulis `width/height: 11px` lewat gaya inline --
        salinan ketiga dari angka yang sudah ada di `.bara-petak` dan
        `.bara-sel`. Yang akan pecah diam-diam selalu salinan yang tidak pernah
        dilihat siapa pun.
        """
        badan = self._fungsi(
            self._berkas("webapp", "statik", "js", "layar-belajar.js"), "blokBara")
        self.assertIn("bara-kosong", badan, "pengisi depan tidak berkelas")
        self.assertNotRegex(badan, r"(width|height)\s*:\s*[\"']?\d",
                            "pengisi depan menyalin ukuran sel lewat gaya inline")

    def test_kata_di_hamparan_menyebut_xp_bukan_hari_belajar(self):
        """Invarian #11 sebagai kata, bukan cuma sebagai sumber data.

        `riwayat_harian` hanya mencatat hari yang MENGHASILKAN XP. Hari yang
        isinya bacaan setengah (`record_material_read(tuntas=False)`) menaikkan
        streak tanpa meninggalkan entri apa pun, jadi selnya bernilai nol.
        Menyebut hamparan ini "hari belajar" membuat ia membantah pil streak
        yang berdiri beberapa piksel di sebelahnya.
        """
        js = self._berkas("webapp", "statik", "js", "layar-belajar.js")
        for nama in ("blokBara", "jedaBara"):
            badan = self._fungsi(js, nama)
            # Komentar dibuang lebih dulu. Justru di komentarlah kedua kata
            # terlarang itu muncul -- untuk menjelaskan kenapa keduanya TIDAK
            # dipakai -- dan tes yang tidak membedakan penjelasan dari kalimat
            # yang muncul di layar akan menghukum dokumentasinya sendiri.
            badan = re.sub(r"/\*.*?\*/", " ", badan, flags=re.S)
            badan = re.sub(r"//[^\n]*", " ", badan)
            kutipan = re.findall(r'"([^"\\]*)"|`([^`\\]*)`', badan)
            gabung = " ".join(a + b for a, b in kutipan).lower()
            self.assertNotIn("hari belajar", gabung,
                             f"`{nama}` menyebut 'hari belajar' untuk data yang "
                             "sebenarnya mengukur XP per hari")
            self.assertNotIn("hari menyala", gabung,
                             f"`{nama}` masih memakai kata lama 'hari menyala'")
        self.assertIn("hari ber-XP", js, "penghitung legenda tidak menyebut XP")


class TestLayarBahasa(unittest.TestCase):
    """Halaman bahasa: peta bab per tingkat, penyaring FLIP, koreografi sekali.

    Layar ini tujuan paling sering dibuka di aplikasi ini dan paling mudah
    rusak oleh gerak (515 judul materi). Yang dijaga di sini adalah hal-hal
    yang tidak terlihat dari membaca kodenya sepintas.
    """

    BACA_TATA_LETAK = TestHamparanBara.BACA_TATA_LETAK

    @staticmethod
    def _berkas(*bagian):
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, *bagian), encoding="utf-8") as f:
            return f.read()

    # Pembantu yang sama, satu definisi. Menyalinnya ke sini berarti dua
    # pemotong fungsi yang harus tetap sepakat soal hitung kurung.
    _telanjang = staticmethod(TestHamparanBara._telanjang)
    _fungsi = staticmethod(TestHamparanBara._fungsi)

    # Kata tingkat menurut `bab.TINGKAT`/`bab.LABEL_TINGKAT`. Satu-satunya
    # tempat yang boleh menamainya adalah server.
    KATA_TINGKAT = ("dasar", "menengah", "mahir")

    @staticmethod
    def _literal(src):
        """Semua literal string/template di `src`, tanpa pembatasnya.

        Dipakai untuk menjawab "apakah ada kata yang DITULIS di sini", bukan
        "apakah ada nama variabel yang kebetulan lewat". Komentar sudah dibuang
        `_telanjang()` sebelum ini, jadi penjelasan di komentar tidak ikut
        tertuduh.
        """
        keluar = []
        for m in re.finditer(r'"([^"\\]*)"' + r"|'([^'\\]*)'" + r"|`([^`\\]*)`", src):
            keluar.append(next(g for g in m.groups() if g is not None))
        return keluar

    @staticmethod
    def _argumen(src, awal):
        """Argumen tingkat-atas sebuah panggilan yang dimulai di `awal`.

        `awal` menunjuk posisi nama fungsinya; kurungnya dihitung, jadi objek
        sifat dan panggilan `h()` bersarang tidak memecah pembagiannya.
        """
        buka = src.index("(", awal)
        dalam = 0
        bagian, kini = [], ""
        for j in range(buka, len(src)):
            c = src[j]
            if c in "([{":
                dalam += 1
                if dalam == 1:
                    continue
            elif c in ")]}":
                dalam -= 1
                if dalam == 0:
                    bagian.append(kini)
                    return [b.strip() for b in bagian]
            if dalam == 1 and c == ",":
                bagian.append(kini)
                kini = ""
                continue
            kini += c
        raise AssertionError("panggilan tidak tertutup")

    def _js(self):
        return self._berkas("webapp", "statik", "js", "layar-belajar.js")

    # ---------------------------------------------------------------- butir 4
    def test_koreografi_daftar_hanya_sekali_per_bahasa(self):
        """Kembali dari materi tidak mengulang reveal 44 baris.

        Jalur yang paling sering dilalui di halaman ini bukan "buka pertama
        kali" melainkan "kembali dari materi yang baru dibaca". Mengulang
        koreografinya tiap kali menunda daftar yang sudah dihafal orangnya, dan
        itu cara tercepat membuat aplikasi terasa lambat tanpa satu angka pun
        jadi jelek.
        """
        js = self._telanjang(self._js())
        self.assertRegex(js, r'const KUNCI_DIRENDER = "dirender\."',
                         "prefiks kunci ingatan hilang atau berubah")

        badan = self._telanjang(self._fungsi(js, "ungkapSekali"))
        # Penjaga harus MEMBACA dulu lalu keluar, bukan menulis lalu tetap
        # mengungkap: urutan yang terbalik membuat kunci tersimpan tapi
        # koreografinya tetap jalan setiap kali.
        i_baca = badan.index("ctx.ingat(KUNCI_DIRENDER + key)")
        i_tulis = badan.index("ctx.ingat(KUNCI_DIRENDER + key, 1)")
        i_ungkap = badan.index("ungkap(el, opsi)", i_baca)
        self.assertLess(i_baca, i_tulis, "kunci ditulis sebelum dibaca")
        self.assertLess(i_tulis, i_ungkap,
                        "koreografi dijalankan sebelum kuncinya ditandai")
        self.assertRegex(badan, r"if \(ctx\.ingat\(KUNCI_DIRENDER \+ key\)\) return el;",
                         "tidak ada jalan keluar saat sudah pernah dirender")

        # Pemanggil di luar layar bahasa (bookmark, cari) memanggil tanpa ctx dan
        # perilakunya HARUS tetap sama persis seperti sebelumnya.
        self.assertRegex(badan, r"if \(!ctx \|\| !key\) \{ ungkap\(el, opsi\); return el; \}",
                         "pemanggil tanpa ctx tidak lagi mendapat ungkap() apa adanya")

        # Cap 240 ms untuk daftar bab tidak dinaikkan.
        bb = self._telanjang(self._fungsi(js, "daftarMateri"))
        m = re.search(r"ungkapSekali\(petak, ctx, b\.key,\s*\{([^}]*)\}", bb)
        self.assertIsNotNone(m, "daftar bab tidak lagi lewat ungkapSekali")
        maks = re.search(r"maks:\s*(\d+)", m.group(1))
        self.assertIsNotNone(maks)
        self.assertLessEqual(int(maks.group(1)), 240,
                            "cap koreografi daftar bab dinaikkan di atas 240 ms")

    # ---------------------------------------------------------------- butir 5
    def test_penyaring_tingkat_flip_tanpa_menganimasikan_geometri(self):
        """Yang berpindah di-FLIP; yang muncul cuma memudar; geometri tidak pernah.

        Menganimasikan `width`/`height` saat baris hilang membayar layout tiap
        frame untuk sebelas kotak sekaligus. `tata()` sudah FLIP pada
        `transform`, dan itu satu-satunya properti yang bergerak di sini.
        """
        js = self._telanjang(self._js())
        badan = self._fungsi(js, "saringBab")
        self.assertIn("tata(tetap,", badan,
                      "perpindahan posisi tidak lagi lewat tata() (FLIP)")

        # Hanya elemen yang tampak SEBELUM dan SESUDAH yang boleh masuk tata():
        # kotak batas elemen tersembunyi nol, dan nol menghasilkan translasi
        # sebesar seluruh halaman.
        self.assertRegex(badan, r"tetap = semua\.filter\(\(el\) => !el\.hidden && setelah\.has\(el\)\)",
                         "daftar FLIP tidak lagi menyaring elemen tersembunyi")

        for pr in ("width", "height", "maxHeight", "max-height"):
            self.assertNotRegex(
                badan, rf"\b{re.escape(pr)}\s*:\s*\[",
                f"`{pr}` dianimasikan di penyaring; itu layout per frame")

        # Yang baru muncul wajib dibersihkan dari sisa `opacity` inline milik
        # ungkap(), kalau tidak animasinya berakhir di nol dan babnya tak
        # terlihat -- keadaan akhir animasi wajib keadaan alami elemennya.
        i_bersih = badan.index('el.style.opacity = ""')
        i_anim = badan.index("animasi(el, { opacity: [0, 1] }", i_bersih)
        self.assertLess(i_bersih, i_anim,
                        "sisa opacity inline tidak dibersihkan sebelum dianimasikan")

        # Gambar PERTAMA tidak boleh membaca tata letak: saat itu `petak` masih
        # lepas dari dokumen. Ini kelas bug invarian #15a, lewat jalur yang
        # bukan requestAnimationFrame -- jadi sapuan rAF tidak melihatnya.
        awal = self._fungsi(js, "gambarSaring")
        for pola in self.BACA_TATA_LETAK:
            self.assertNotRegex(
                awal, pola,
                f"`gambarSaring()` membaca `{pola}`; ia berjalan pada pohon yang "
                "belum terpasang dan angkanya nol")
        self.assertNotIn("tata(", awal,
                         "gambar pertama memanggil tata(), yang membaca "
                         "getBoundingClientRect pada elemen yang masih lepas")
        self.assertRegex(badan, r"\n  gambarSaring\(\);",
                         "gambar pertama tidak lagi lewat gambarSaring()")

    # ---------------------------------------------------------------- butir 2
    def test_cincin_bab_menyetel_keadaan_final_lebih_dulu(self):
        """Busur berangkat dari kosong, tapi keadaan diamnya sudah benar.

        Kalau gerak dimatikan, animasinya dibatalkan, atau JS tidak jalan sama
        sekali, yang tertinggal harus tetap busur dengan panjang yang benar --
        bukan lingkaran kosong (keadaan akhir = keadaan alami).
        """
        js = self._telanjang(self._js())
        badan = self._fungsi(js, "cincinBab")
        i_final = badan.index('setAttribute("stroke-dashoffset"')
        i_anim = badan.index("animasi(")
        self.assertLess(i_final, i_anim,
                        "animasi dipasang sebelum keadaan final; lingkaran akan "
                        "kosong kalau animasinya tidak pernah berjalan")
        self.assertRegex(badan, r"animasikan\b",
                         "tidak ada lagi pembeda bab mana yang beranimasi")

        # Satu angka, satu gambar: bilah di kepala bab digantikan, bukan
        # ditemani.
        kepala = self._telanjang(self._fungsi(js, "kepalaBab"))
        self.assertNotIn("bilah(", kepala,
                         "kepala bab punya cincin DAN bilah untuk angka yang sama")
        self.assertIn("cincinBab(", kepala, "kepala bab tidak lagi punya cincin")

        # Cincin baru tidak boleh menyalin `transition: stroke-dashoffset` milik
        # `.cincin` dasbor: WAAPI sudah memegang properti itu (invarian #2).
        css = re.sub(r"/\*.*?\*/", " ",
                     self._berkas("webapp", "statik", "gaya.css"), flags=re.S)
        for sel, isi in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
            if ".bab-cincin" in sel:
                self.assertNotIn("transition", isi,
                                 f"`{sel.strip()}` menambahkan transition pada "
                                 "properti yang sudah digerakkan WAAPI")

    def test_isi_bab_memakai_util_entrance_yang_sudah_ada(self):
        """Satu mesin entrance, dan bab yang sudah terbuka tidak ikut bertumpuk."""
        js = self._telanjang(self._js())
        bb = self._fungsi(js, "daftarMateri")
        self.assertRegex(
            bb, r'"div\.bab-isi" \+ \(terbuka \? "" : "\.masuk-mandiri"\)',
            "isi bab tidak lagi memakai util entrance `.masuk-mandiri`, atau ia "
            "dipasang juga pada bab yang sudah terbuka -- @starting-style menyala "
            "pada render pertama dan akan bertumpuk di atas koreografi `.bab`")
        # ::details-content sengaja TIDAK dipakai: ia Chrome-only, dan di
        # Firefox aturannya tidak menggambar apa pun.
        css = self._berkas("webapp", "statik", "gaya.css")
        self.assertNotIn("::details-content", css,
                         "`::details-content` dipakai; ia Chrome-only dan di "
                         "peramban lain jadi aturan yang tidak menggambar apa pun")

    # ---------------------------------------------------------------- butir 1
    def test_peta_bab_per_tingkat_dan_labelnya_dari_server(self):
        """Nama tingkat datang dari `bab.py`, bukan dikarang di layar (invarian #12)."""
        js = self._telanjang(self._js())
        badan = self._fungsi(js, "petaBab")
        self.assertIn("ctx.awal.aturan_bab", badan,
                      "peta bab tidak lagi membaca label tingkat dari server")
        self.assertIn("peta-tingkat", badan, "tidak ada rail per tingkat")

        js_telanjang = self._telanjang(self._js())

        # (i) BENTUK, bukan substring. Versi pertama tes ini cuma memeriksa
        #     `label_tingkat` HADIR di badan fungsi — dan satu interpolasi yang
        #     masih utuh menyembunyikan yang lain: mengarang teks pil di
        #     `kepalaBab` ATAU mengarang `title` rail di `segmenBab` sama-sama
        #     lolos 803 tes. Yang ditagih sekarang: tidak satu pun LITERAL di
        #     ketiga fungsi ini memuat kata tingkat.
        for nama in ("petaBab", "segmenBab", "kepalaBab"):
            for lit in self._literal(self._fungsi(js_telanjang, nama)):
                for kata in self.KATA_TINGKAT:
                    self.assertNotRegex(
                        lit, rf"(?i)\b{kata}\b",
                        f'`{nama}` menuliskan "{lit}" — kata tingkat dikarang di '
                        "layar. Namanya milik bab.LABEL_TINGKAT lewat "
                        "/api/awal.aturan_bab (invarian #12)")

        # (ii) Yang TERLIHAT wajib variabelnya, bukan cuma atributnya. Sebuah
        #      `title` yang benar di atas pil yang teksnya dikarang tetap
        #      salah — dan `title` tidak pernah dibaca di layar sentuh.
        kepala = self._fungsi(js_telanjang, "kepalaBab")
        i_pil = kepala.index('h("span.pil.bab-tingkat')
        arg = self._argumen(kepala, i_pil)
        self.assertGreaterEqual(len(arg), 3,
                                "pil tingkat tidak lagi punya anak teks")
        self.assertEqual(
            arg[2], "bab.label_tingkat",
            "teks yang TERLIHAT di pil tingkat bukan `bab.label_tingkat` "
            f"melainkan `{arg[2]}`")

        # Rail tetap menginterpolasikannya juga, bukan menuliskannya.
        self.assertIn("bab.label_tingkat", self._fungsi(js_telanjang, "segmenBab"),
                      "title rail tidak lagi memakai label dari server")

        # Bab terkunci tetap ditampilkan, dan alasannya ikut -- kalimatnya utuh
        # dari bab.py, tidak dirumuskan ulang di sini.
        seg = self._telanjang(self._fungsi(js, "segmenBab"))
        self.assertIn("peta-terkunci", seg, "bab terkunci tidak lagi ditampilkan")
        self.assertIn("bab.alasan", seg,
                      "segmen terkunci tidak membawa alasannya; orang harus "
                      "mengekliknya dulu untuk tahu kenapa")

        # Rail tidak memakai pemusatan gulir: diukur, ia tidak bisa pernah
        # berjalan (lima segmen terbanyak, 226 px, di rail 336 px).
        self.assertNotIn("bawaKeTengah", badan,
                         "pemusatan gulir rail kembali; ia tidak bisa pernah "
                         "berjalan dengan data repo ini -- lihat komentarnya")

    def test_kepala_bab_menjawab_tekan_lewat_pasangIsyarat(self):
        """Fisika tekan didaftarkan, tidak dipanggil dari komponennya.

        `tekan()` memakai `fill: "forwards"`, jadi siapa pun yang memanggilnya
        bertanggung jawab membatalkannya (invarian #1). `pasangIsyarat()` yang
        memegang pasangan tekan/lepas — termasuk `pointercancel` dan kursor yang
        keluar sambil ditekan — dan hanya lewat jalur itu pembatalannya dijamin.
        Presedennya `.rel-tombol`/`.rel-pemicu` dari S02.

        Papan ketik tidak butuh syarat tambahan: jalur itu cuma menumpang
        pointerdown/pointerup/pointercancel, jadi Enter pada `<summary>` — cara
        membukanya dengan papan ketik — tidak pernah memicu `tekan()`.
        """
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        dirjs = os.path.join(akar, "webapp", "statik", "js")
        with open(os.path.join(dirjs, "gerak.js"), encoding="utf-8") as f:
            gerak = f.read()

        daftar = re.search(r"const BISA_DITEKAN =(.*?);\n", gerak, re.S)
        self.assertIsNotNone(daftar, "BISA_DITEKAN tidak terbaca")
        selektor = " ".join(self._literal(self._telanjang(daftar.group(1))))
        self.assertRegex(selektor, r"\.bab-kepala\b",
                         "`.bab-kepala` tidak lagi terdaftar; kepala bab akan "
                         "diam saat ditekan padahal tetangganya menjawab")

        # Nol komponen memanggil tekan() sendiri. `lepas` TIDAK diperiksa di
        # sini: nama itu dipakai juga oleh editor.lepas() dan oleh pelepas pin
        # bara, dan menyamakan ketiganya akan membuat tes ini menuduh kode yang
        # tidak ada hubungannya.
        for nama in sorted(n for n in os.listdir(dirjs)
                           if n.endswith(".js") and n != "gerak.js"):
            with open(os.path.join(dirjs, nama), encoding="utf-8") as f:
                src = self._telanjang(f.read())
            impor = re.search(r"import \{([^}]*)\} from \"\./gerak\.js\";", src)
            if impor:
                nama_impor = [x.strip() for x in impor.group(1).split(",")]
                self.assertNotIn("tekan", nama_impor,
                                 f"{nama} mengimpor tekan() langsung; daftarkan "
                                 "selektornya di BISA_DITEKAN sebagai gantinya")
            self.assertNotRegex(
                src, r"(?<![\w.])tekan\s*\(",
                f"{nama} memanggil tekan() dari komponen; pembatalannya tidak "
                "dijamin di luar pasangIsyarat() (invarian #1)")

    def test_toolchain_belum_siap_ditandai_sebelum_diklik(self):
        """Yang tidak bisa dijalankan dikatakan SEBELUM orang sampai ke sana."""
        js = self._fungsi(self._telanjang(self._js()), "layarBahasa")
        # Bukan cukup "pipanya ada": ia harus digerakkan `b.siap`. Versi pertama
        # tes ini lolos untuk mutasi `const belumSiap = false;` — seluruh
        # penandanya mati, ketiga asersi di bawah tetap hijau.
        self.assertRegex(js, r"const belumSiap = !b\.siap;",
                         "penanda toolchain tidak lagi berasal dari `b.siap`")
        self.assertRegex(js, r'belumSiap && t === "latihan"',
                         "tab Latihan tidak ditandai saat toolchain belum ada")
        self.assertRegex(js, r"belumSiap \? capBelumSiap\(\) : null",
                         "tautan Ruang coba tidak ditandai")


class TestHiddenBenarBenarMenyembunyikan(unittest.TestCase):
    """`hidden` yang disetel JS wajib benar-benar menghilangkan elemennya.

    Aturan CSS `[hidden] { display: none }` datang dari lembar UA, dan lembar
    AUTHOR selalu menang atasnya. Jadi `.bab { display: grid }` membuat
    `el.hidden = true` tidak melakukan apa pun selain memasang atribut — dan
    tidak ada satu pun galat yang muncul.

    Itu terjadi sungguhan di S05: penyaring tingkat menyetel `hidden` pada tujuh
    dari sebelas bab, `.bab-daftar` tetap 1623 px, dan teks statusnya berbunyi
    "4 dari 11 bab ditampilkan" sementara kesebelasnya ada di layar. Verifikasi
    waktu itu membaca `el.hidden` — ATRIBUTNYA — jadi angkanya benar sebagai
    atribut dan salah sebagai tampilan. Sesudah `.bab[hidden]` dipasang:
    1623 -> 714 px, `display: none`, `offsetParent` null.

    Batas tes ini, disebut supaya tidak dianggap lebih dari yang ia lakukan:
    suite ini stdlib dan tidak punya mesin CSS, jadi yang dihitung di sini
    adalah KASKADENYA, bukan piksel yang dirender. Angka render dilaporkan dari
    peramban; yang dijaga di sini supaya tidak lahir lagi adalah bentuknya.
    """

    # Setiap penulisan `hidden` di statik/js, beserta kelas/id yang benar-benar
    # disetel. Kuncinya (berkas, fungsi penutup, teks barisnya) dan SENGAJA
    # bukan nomor baris: versi pertama registri ini berkunci nomor, dan
    # penambahan dua puluh satu baris di berkas yang sama menggeser delapan
    # entri sekaligus -- lapuk pada suntingan pertama yang tidak berhubungan.
    REGISTRI = {
        ('aplikasi.js', 'gambarKonteks',
         'el.hidden = true;'):
            ('#konteks', 'strip konteks disembunyikan router'),
        ('aplikasi.js', 'gambarKonteks',
         'el.hidden = false;'):
            ('#konteks', 'pasangannya, dibuka lagi'),
        ('aplikasi.js', 'bangunRel',
         'kotakTematik.hidden = tematik.length === 0;'):
            ('.rel-kotak-tematik', 'kotak bahasa tematik saat daftarnya kosong'),
        ('inti.js', 'jendela',
         'tirai.hidden = true;'):
            ('#tirai', 'tirai dialog'),
        ('inti.js', 'jendela',
         'tirai.hidden = false;'):
            ('#tirai', 'pasangannya'),
        ('layar-belajar.js', 'pinKeHariIni',
         'geser.hidden = petak.scrollWidth <= petak.clientWidth;'):
            ('.bara-geser', 'penanda kisi bisa digeser'),
        ('layar-belajar.js', 'blokBara',
         'const geser = h("span.bara-geser", { hidden: true },'):
            ('.bara-geser', 'lahir tersembunyi'),
        ('layar-belajar.js', 'gambarSaring',
         'for (const el of semua) el.hidden = !setelah.has(el);'):
            ('.bab', 'penyaring tingkat, gambar pertama'),
        ('layar-belajar.js', 'terapkan',
         'for (const el of semua) el.hidden = !setelah.has(el);'):
            ('.bab', 'penyaring tingkat, pembaruan beranimasi'),
        # Kartu aksi di tepi (S06 butir 2). `segarkanKunci` adalah fungsi
        # bersarang TERAKHIR yang dideklarasikan sebelum baris ini di dalam
        # `layarMateri`; pemindai memakai deklarasi terdekat, bukan lingkup
        # sebenarnya. Sasarannya `.aksi-tepi`, yang menyetel `display: flex`
        # sendiri dan karena itu WAJIB ada di daftar pemulih.
        ('layar-belajar.js', 'segarkanKunci', 'kartuAksi.hidden = true;'):
            ('.aksi-tepi', 'kartu menyingkir sesudah 4 detik diam'),
        ('layar-belajar.js', 'segarkanKunci', 'kartuAksi.hidden = false;'):
            ('.aksi-tepi', 'kartu kembali begitu ada yang menggulir'),
        ('layar-belajar.js', 'kartuKeluaran',
         'pv.el.hidden = !lihat;'):
            ('.pratinjau', 'tab pratinjau HTML/CSS'),
        ('layar-belajar.js', 'kartuKeluaran',
         'pohon.hidden = lihat;'):
            ('.pra', 'pohon struktur, pasangan tab di atas'),
        ('layar-belajar.js', 'kartuKeluaran',
         'if (ket) ket.hidden = !lihat;'):
            ('.pratinjau-ket', 'keterangan pratinjau'),
        ('layar-belajar.js', 'blokKode',
         '{ hidden: true, title: "Kembalikan ke kode aslinya" }, "Kembalikan");'):
            ('.tbl', 'tombol Kembalikan lahir tersembunyi'),
        ('layar-belajar.js', 'utakAtik',
         'tblUbah.hidden = true;'):
            ('.tbl', 'tombol Ubah'),
        ('layar-belajar.js', 'utakAtik',
         'tblPulih.hidden = false;'):
            ('.tbl', 'tombol Pulih'),
        ('layar-belajar.js', 'pulihkan',
         'tblUbah.hidden = false;'):
            ('.tbl', 'tombol Ubah, pasangannya'),
        ('layar-belajar.js', 'pulihkan',
         'tblPulih.hidden = true;'):
            ('.tbl', 'tombol Pulih, pasangannya'),
        ('layar-lain.js', 'kartuPilihan',
         'const tanda = h("span.pil.pil-nyala", { hidden: true },'):
            ('.pil', 'penanda pilihan tema/ukuran'),
        ('layar-lain.js', 'tandaiPilihan',
         'if (kt.tanda) kt.tanda.hidden = !ini;'):
            ('.pil', 'pasangannya'),
    }

    POLA_TULIS = re.compile(
        r"\.hidden\s*=|(?<![\w-])hidden\s*:\s*(?:true|false|!|[a-zA-Z])")
    POLA_FUNGSI = re.compile(r"^\s*(?:export\s+)?(?:async\s+)?function\s+(\w+)")

    @staticmethod
    def _akar():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def _situs(self):
        """{(berkas, fungsi, teks baris)} setiap penulisan `hidden` di statik/js."""
        dirjs = os.path.join(self._akar(), "webapp", "statik", "js")
        keluar = {}
        for nama in sorted(n for n in os.listdir(dirjs) if n.endswith(".js")):
            with open(os.path.join(dirjs, nama), encoding="utf-8") as f:
                baris = f.read().split("\n")
            fungsi = "(tingkat-modul)"
            for teks in baris:
                m = self.POLA_FUNGSI.match(teks)
                if m:
                    fungsi = m.group(1)
                tanpa = re.sub(r"//.*", "", teks)
                if self.POLA_TULIS.search(tanpa):
                    keluar[(nama, fungsi, teks.strip())] = True
        return set(keluar)

    def _css(self):
        with open(os.path.join(self._akar(), "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            return re.sub(r"/\*.*?\*/", " ", f.read(), flags=re.S)

    def test_registri_mencakup_setiap_penulisan_hidden(self):
        """Setiap `hidden` baru wajib mendaftar, supaya kaskadenya ikut ditanya."""
        situs = self._situs()
        daftar = set(self.REGISTRI)
        hilang = sorted(situs - daftar)
        basi = sorted(daftar - situs)
        self.assertEqual(
            hilang, [],
            "ada penulisan `hidden` yang belum terdaftar. Daftarkan di REGISTRI "
            "beserta kelas/id yang benar-benar disetel: kalau kelas itu menyetel "
            "`display` sendiri, `hidden` TIDAK akan menyembunyikannya dan tidak "
            f"ada galat yang muncul. Belum terdaftar: {hilang}")
        self.assertEqual(basi, [],
                         f"entri REGISTRI menunjuk situs yang sudah tidak ada: {basi}")

    def test_setiap_sasaran_hidden_benar_benar_jadi_display_none(self):
        """Kaskade dihitung: siapa yang menyetel display, siapa yang memulihkan."""
        css = self._css()
        pemulih, display = set(), {}
        for sel_blok, isi in re.findall(r"([^{}]+)\{([^{}]*)\}", css):
            m = re.search(r"(?<![-\w])display\s*:\s*([^;!]+)", isi)
            for sel in sel_blok.split(","):
                sel = sel.strip()
                if "[hidden]" in sel:
                    for k in re.findall(r"[.#]([A-Za-z][\w-]*)\[hidden\]", sel):
                        pemulih.add(k)
                    continue
                if not m or m.group(1).strip() == "none":
                    continue
                # Hanya penyeleksi tunggal: `.a .b` menyetel display `.b` dalam
                # konteks, bukan `.b` di mana pun.
                murni = re.fullmatch(r"([.#])([A-Za-z][\w-]*)", sel)
                if murni:
                    display.setdefault(murni.group(2), m.group(1).strip())

        gagal = []
        for (berkas, fungsi, _teks), (sasaran, alasan) in sorted(self.REGISTRI.items()):
            nama = sasaran.lstrip(".#")
            d = display.get(nama)
            if d and nama not in pemulih:
                gagal.append(f"{berkas} {fungsi}() -> {sasaran} menyetel "
                             f"`display: {d}` tanpa pemulih `{sasaran}[hidden]` "
                             f"({alasan})")
        self.assertEqual(
            gagal, [],
            "`hidden` tidak akan menyembunyikan sasaran ini: lembar author "
            "mengalahkan `[hidden]` milik UA, dan gejalanya bukan galat "
            "melainkan elemen yang tetap terlihat sementara atributnya bilang "
            "sudah hilang. Tambahkan namanya ke daftar pemulih di gaya.css. "
            + "; ".join(gagal))

    def test_penyaring_bab_masih_memakai_atribut_hidden(self):
        """Tes lama yang membaca `!el.hidden` TETAP berlaku, dan tidak cukup.

        Ia menjaga hal yang berbeda: bahwa `tata()` cuma menerima elemen yang
        tampak sebelum DAN sesudah. Yang ia tidak pernah bisa jawab adalah
        apakah `hidden` benar-benar menyembunyikan — dua tes ini bersama, bukan
        salah satunya.
        """
        with open(os.path.join(self._akar(), "webapp", "statik", "js",
                               "layar-belajar.js"), encoding="utf-8") as f:
            js = f.read()
        self.assertRegex(js, r"tetap = semua\.filter\(\(el\) => !el\.hidden",
                         "penjaga FLIP berbasis atribut hilang")
        self.assertIn(".bab[hidden]", self._css(),
                      "pemulih `.bab[hidden]` hilang dari gaya.css")


class TestVariabelDibacaDiLingkupYangSama(unittest.TestCase):
    """Variabel yang dibaca aturan di `html`/`:root` wajib diisi ulang di sana juga.

    Kelas bug ini menggigit sekali dan tidak menghasilkan satu pun galat:
    `--lengket-atas` dideklarasikan di `:root`, dibaca oleh
    `html { scroll-padding-top: calc(var(--lengket-atas) + var(--s4)) }`, lalu
    diisi ulang oleh `#panggung.berkonteks` — sebuah subtree. Leluhur tidak
    pernah bisa melihat isian ulang di dalam keturunannya, jadi pengatur
    pendaratan gulir tetap memakai nilai lama.

    Akibatnya terukur di pembaca: `scroll-padding-top` 72 px sementara dasar
    chrome yang menempel 98 px, jadi 26 px teratas setiap sasaran gulir
    mendarat DI BALIK strip — termasuk baris pertama judul bagian, persis yang
    komentar di atas aturan itu bilang tidak boleh terjadi.

    Yang dijaga: setiap `var(--x)` yang dibaca aturan pada `html`/`:root` punya
    deklarasi `--x` pada `html`/`:root` juga. Kalau sebuah variabel memang
    tidak pernah berubah, ia didaftarkan di TETAP beserta alasannya — jadi
    "tidak berubah" menjadi keputusan yang tertulis, bukan kelalaian.
    """

    # Variabel yang dibaca di lingkup html/:root dan memang TIDAK pernah diisi
    # ulang di lingkup lain mana pun. Kalau suatu hari ada yang mengisinya ulang
    # di sebuah subtree, tes di bawah akan menagihnya.
    TETAP = {
        "--ukuran-teks": "disetel JS pada <html> sendiri (layar-lain.js), bukan di subtree",
        "--s4": "tangga jarak; konstan seumur aplikasi",
        "--rel-tinggi": "tinggi navbar; konstan",
        "--konteks-tinggi": "tinggi strip konteks; konstan",
    }

    @staticmethod
    def _css():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            return re.sub(r"/\*.*?\*/", " ", f.read(), flags=re.S)

    @staticmethod
    def _lingkupAkar(sel):
        """Apakah penyeleksi ini berlaku pada elemen <html> itu sendiri?"""
        sel = sel.strip()
        if not sel or sel.startswith("@"):
            return False
        # `html`, `:root`, dan variannya dengan :has()/atribut -- tapi BUKAN
        # `html .x` atau `:root .x`, yang menyasar keturunannya.
        inti = re.sub(r":has\([^)]*\)|\[[^\]]*\]|:not\([^)]*\)", "", sel).strip()
        return inti in ("html", ":root", "html:root", ":root:root")

    def test_var_yang_dibaca_di_akar_diisi_ulang_di_akar(self):
        css = self._css()
        aturan = re.findall(r"([^{}]+)\{([^{}]*)\}", css)

        dibaca, ditulisDiAkar, ditulisDiLain = set(), set(), {}
        for sel_blok, isi in aturan:
            akar = any(self._lingkupAkar(s) for s in sel_blok.split(","))
            for nama in re.findall(r"var\((--[\w-]+)", isi):
                if akar:
                    dibaca.add(nama)
            for nama in re.findall(r"(?:^|;|\{)\s*(--[\w-]+)\s*:", isi):
                if akar:
                    ditulisDiAkar.add(nama)
                else:
                    ditulisDiLain.setdefault(nama, set()).add(sel_blok.strip()[:60])

        self.assertTrue(dibaca, "tidak ada var yang terbaca di lingkup akar")

        gagal = []
        for nama in sorted(dibaca):
            lain = ditulisDiLain.get(nama)
            if nama in ditulisDiAkar:
                continue          # diisi ulang di tempat yang bisa dilihat
            if not lain:
                if nama in self.TETAP:
                    continue      # memang konstan, dan itu tertulis
                gagal.append(f"{nama}: dibaca di akar, tidak pernah dideklarasikan "
                             "di akar, dan tidak terdaftar di TETAP")
                continue
            gagal.append(
                f"{nama}: dibaca oleh aturan di html/:root tapi diisi ulang HANYA "
                f"di {sorted(lain)} -- lingkup itu tidak pernah terlihat oleh "
                "leluhurnya, jadi pembacanya memakai nilai lama tanpa satu pun galat")
        self.assertEqual(gagal, [], "; ".join(gagal))

    def test_lengket_atas_terisi_ulang_untuk_pembaca(self):
        """Bentuk perbaikannya, bukan angkanya: dua lingkup, satu sumber angka."""
        css = self._css()
        self.assertRegex(
            css, r"#panggung\.berkonteks\s*\{\s*--lengket-atas:",
            "isian ulang untuk kolom yang menempel di dalam #panggung hilang")
        self.assertRegex(
            css, r"html:has\(#panggung\.berkonteks\)\s*\{\s*--lengket-atas:",
            "isian ulang untuk `html` hilang; `scroll-padding-top` akan kembali "
            "memakai nilai tanpa strip dan 26 px teratas tiap sasaran gulir "
            "mendarat di balik strip")
        self.assertIn("@supports selector(:has(*))", css,
                      "`:has()` tidak dipagari @supports seperti pemakai lain")
        # Jarak pendaratan TIDAK boleh disalin ke JS sebagai angka: ia dibaca
        # dari scrollPaddingTop yang sudah terhitung.
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js", "layar-belajar.js"),
                  encoding="utf-8") as f:
            js = f.read()
        badan = TestHamparanBara._fungsi(TestHamparanBara._telanjang(js), "bawaKeAtas")
        self.assertIn("scrollPaddingTop", badan,
                      "jarak pendaratan tidak dibaca dari CSS; angka kedua yang "
                      "bisa melenceng dari yang pertama")
        self.assertNotIn("scrollIntoView", badan)
        self.assertNotRegex(badan, r"\b(54|44|72|98|116)\b",
                            "angka lengket ditulis sebagai konstanta di JS")

        # Dan pemanggilnya WAJIB memakainya. Tanpa baris ini, mengembalikan
        # `petaBagian` ke `scrollIntoView` tetap hijau: `bawaKeAtas()` masih
        # benar, cuma tidak ada yang memanggilnya lagi. Mutasi itu memang lolos
        # ronde pertama.
        peta = TestHamparanBara._fungsi(TestHamparanBara._telanjang(js), "petaBagian")
        self.assertIn("bawaKeAtas(sasaran)", peta,
                      "peta bagian tidak lagi memakai `bawaKeAtas()`")
        self.assertNotIn("scrollIntoView", peta,
                         "peta bagian kembali memakai `scrollIntoView`; "
                         "pendaratannya lepas dari `scroll-padding-top` yang "
                         "sudah terhitung dan 26 px teratas kembali ke balik strip")


class TestBentukKomentar(unittest.TestCase):
    """Dua bentuk komentar yang menyesatkan pembacanya tanpa merusak apa pun.

    Keduanya sah bagi parser — dan itu justru sebabnya mereka bertahan. Yang
    rusak bukan berkasnya melainkan orang berikutnya yang membacanya.

    Kedua pagar ini dipasang HANYA karena nol positif-palsunya sudah diukur
    lebih dulu, dan cakupannya tidak sama: pola docstring disapu ke seluruh
    `webapp/statik/` (lima kasus di `0538983`, nol sesudahnya), pola komentar-dalam-
    daftar-penyeleksi hanya ke `gaya.css` (satu kasus, lalu nol). Yang terakhir bukan
    pelit cakupan melainkan struktur: JavaScript tidak punya prelude, jadi predikat itu
    kalau disapu ke `statik/js/` memberi dua puluh delapan kasus yang semuanya sah.
    Pagar yang dipasang di atas berkas yang belum bersih adalah tes merah permanen,
    dan itu bukan pagar.
    """

    @staticmethod
    def _berkas():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        statik = os.path.join(akar, "webapp", "statik")
        keluar = [os.path.join(statik, "gaya.css")]
        js = os.path.join(statik, "js")
        keluar += [os.path.join(js, n) for n in sorted(os.listdir(js))
                   if n.endswith(".js")]
        return keluar

    @staticmethod
    def _komentar_di_dalam_prelude(teks):
        """[nomor baris] setiap komentar yang berdiri di PRELUDE sesudah koma.

        Prelude = daerah antara batas sebuah aturan dan `{`-nya, tempat daftar
        penyeleksi hidup. Komentar di dalam BADAN aturan adalah bagian dari
        nilai, bukan dari daftar penyeleksi — dan di sanalah ia sah.

        Pemindaian per karakter, bukan per baris, karena predikat per baris
        ("baris berakhiran koma disusul baris berawalan /*") tidak bisa
        membedakan keduanya: `gaya.css` punya 103 baris berakhiran koma dan
        hanya sekitar 53 di antaranya daftar penyeleksi; sisanya `font-family`,
        `transition` multi-baris, dan `linear-gradient`. S07-S12 menambah CSS
        gerak, jadi predikat lama akan memerah karena alasan yang salah — dan
        tes yang memerah karena alasan yang salah adalah tes yang berhenti
        dibaca.
        """
        hasil, i, n = [], 0, len(teks)
        kedalaman, prelude, koma, baris = 0, True, 0, 1
        while i < n:
            c = teks[i]
            if c == "\n":
                baris += 1; i += 1; continue
            if teks.startswith("/*", i):
                if prelude and koma:
                    hasil.append(baris)
                j = teks.find("*/", i + 2)
                if j < 0:
                    break
                baris += teks.count("\n", i, j + 2); i = j + 2; continue
            if c in "\"'":
                q, j = c, i + 1
                while j < n and teks[j] != q:
                    if teks[j] == "\\":
                        j += 1
                    j += 1
                baris += teks.count("\n", i, min(j + 1, n)); i = j + 1; continue
            if c == "{":
                kedalaman += 1; prelude, koma = False, 0
            elif c == "}":
                kedalaman -= 1; prelude, koma = True, 0
            elif c == ";":
                prelude, koma = kedalaman == 0, 0
            elif c == "," and prelude:
                koma += 1
            i += 1
        return hasil

    def test_komentar_tidak_menyelinap_di_antara_koma_dan_penyeleksi(self):
        """`display: none` harus terlihat menempel pada penyeleksi yang mana.

        Komentar di antara sebuah koma dan penyeleksi berikutnya diperbolehkan
        parser — diuji: ketujuh belas penyeleksi daftar pemulih `[hidden]` tetap
        menghasilkan `display: none`. Yang hilang adalah kemampuan membacanya
        sebagai daftar: badan aturannya berpindah belasan baris menjauh dari
        penyeleksi pertamanya, dan penyeleksi terakhir terbaca seolah punya
        aturan sendiri. Komentar untuk satu penyeleksi = aturan sendiri.

        Cakupannya SENGAJA `gaya.css` saja. Menyapukan predikat ini ke
        `statik/js/` memberi 28 kasus yang semuanya sah: empat preset pegas di
        `gerak.js`, satu di `aplikasi.js`, dan dua puluh tiga entri path di
        `ikon.js` yang memang diberi komentar per ikon. Di JavaScript tidak ada
        "prelude", jadi predikatnya tidak punya arti di sana sama sekali.
        """
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        jalur = os.path.join(akar, "webapp", "statik", "gaya.css")
        with open(jalur, encoding="utf-8") as f:
            teks = f.read()
        gagal = [f"gaya.css:{n}" for n in self._komentar_di_dalam_prelude(teks)]
        self.assertEqual(
            gagal, [],
            "komentar berdiri di daftar penyeleksi, sesudah sebuah koma. Pecah "
            "penyeleksi itu jadi aturan sendiri dan taruh komentarnya di "
            "atasnya: " + "; ".join(gagal))

    def test_tidak_ada_docstring_yang_teryatim(self):
        """Sebuah blok `/** */` mendokumentasikan hal yang ada TEPAT di bawahnya.

        Begitu sebuah fungsi disisipkan di antara blok dan fungsinya, blok itu
        berhenti menjelaskan apa pun dan mulai salah menjelaskan tetangganya —
        dan tidak ada satu pun galat. Kelas ini ditemukan lima kali di repo ini:
        docstring `rayakan()` menganggur di atas `tingkatRayakan`, docstring
        `bawaKeTengah()` di atas `saatSiap`, docstring `ubinBahasa()` di atas
        `kisiUbin`, blok "NOMOR ADALAH ARSITEKTUR" di atas `cincinBab`, dan
        docstring `petaBagian()` di atas `bawaKeAtas`.

        Bentuk yang ditangkap: sebuah blok komentar yang berakhir TEPAT di baris
        sebelum blok `/**` berikutnya. Dua docstring yang menempel begitu berarti
        yang atas tidak mungkin menempel pada apa pun — karena yang di bawahnya
        adalah komentar, bukan kode.

        EMPAT BENTUK YATIM YANG LOLOS TES INI, dan itu disengaja. Jangan membaca
        kelas bug ini sebagai "sudah dijaga":

          (a) sebuah fungsi TANPA docstring disisipkan di antara docstring dan
              fungsi yang dijelaskannya;
          (b) komentar `//` lalu fungsi, di antara keduanya;
          (c) blok `/* */` satu bintang lalu fungsi, di antara keduanya;
          (d) dua docstring yang dipisah satu baris kosong.

        Perluasan yang jelas — "setiap `/**` wajib diikuti sebuah deklarasi" —
        diukur dan DITOLAK: ia memberi tiga positif-palsu nyata di repo hari ini,
        yaitu `aplikasi.js:100` `ingat(kunci, nilai) {` (metode objek),
        `editor.js:251` `lepas() {` (metode kelas), dan `aplikasi.js:584` (blok
        `/* */` yang memang menyusul sebuah docstring). Tes yang memerah karena
        alasan yang salah adalah tes yang berhenti dibaca, jadi pagar ini tetap
        sempit dengan sadar.

        Yang menjaga KELASNYA bukan tes ini melainkan aturan "Komentar-doc
        menempel pada fungsinya" di AGENTS.md, yang dibaca manusia.
        """
        gagal = []
        for jalur in self._berkas():
            with open(jalur, encoding="utf-8") as f:
                baris = f.read().split("\n")
            nama = os.path.basename(jalur)
            for i in range(1, len(baris)):
                if (baris[i - 1].rstrip().endswith("*/")
                        and baris[i].lstrip().startswith("/**")):
                    gagal.append(f"{nama}:{i - 1} -> :{i}")
        self.assertEqual(
            gagal, [],
            "ada blok komentar yang berakhir tepat di atas blok `/**` "
            "berikutnya, jadi ia tidak mendokumentasikan apa pun. Pindahkan ke "
            "atas fungsi yang memang dijelaskan kalimat pertamanya: "
            + "; ".join(gagal))


class TestPosisiBacaDipulihkanSetelahTerpasang(unittest.TestCase):
    """Pemulihan posisi baca wajib terjadi SESUDAH layarnya terpasang.

    Alasannya konstruktif, bukan selera. `gambarRute()` menjalankan
    `panggung.appendChild(...)` lalu `window.scrollTo({ top: 0 })` secara
    SENKRON; `saatSiap()` mem-poll lewat `requestAnimationFrame`. Jadi sebuah
    pemulihan yang dipanggil dari badan pembangun layar berjalan SEBELUM
    keduanya — nilainya nol, tidak ada galat, dan kalaupun ia berhasil ia
    langsung ditimpa `scrollTo(0)` beberapa baris kemudian. Dari dalam callback
    `saatSiap`, keduanya sudah lewat.

    CAKUPAN YANG DIUKUR: badan `layarMateri` di
    `webapp/statik/js/layar-belajar.js`, plus badan `pulihkanBaca`. Tidak
    disapukan ke berkas atau layar lain, dan tidak akan diperlebar sebelum
    positif-palsunya terukur nol di sana (doktrin pagar bentuk sejak `74df21f`).

    BENTUK YANG LOLOS TES INI, dan itu disengaja — jangan membacanya sebagai
    "kelas ini sudah dijaga":

      (a) penulisan gulir di dalam fungsi ketiga yang dipanggil `layarMateri`
          di jalur senkron; tes ini cuma mengikuti satu tingkat tak-langsung,
          yaitu `pulihkanBaca` yang disebut namanya;
      (b) `element.scrollLeft = ...` (gulir mendatar) — bukan posisi baca;
      (c) penulisan gulir di layar lain (`layarBahasa`, `layarKuis`, dst.);
      (d) penundaan lewat `setTimeout`/`queueMicrotask` alih-alih `saatSiap` —
          ia akan ditandai MERAH oleh tes ini, dan itu memang disengaja: waktu
          yang ditebak bukan pengganti tahu-kapan-terpasang.
    """

    @staticmethod
    def _js():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js",
                               "layar-belajar.js"), encoding="utf-8") as f:
            return TestHamparanBara._telanjang(f.read())

    @staticmethod
    def _rentang_panggilan(badan, nama):
        """[(mulai, selesai)] argumen tiap panggilan `nama(...)`, kurung dihitung."""
        keluar, i = [], 0
        while True:
            i = badan.find(nama + "(", i)
            if i < 0:
                return keluar
            j, dalam = badan.index("(", i), 0
            for k in range(j, len(badan)):
                if badan[k] == "(":
                    dalam += 1
                elif badan[k] == ")":
                    dalam -= 1
                    if dalam == 0:
                        keluar.append((j, k))
                        break
            i = j + 1

    TULIS_GULIR = (r"window\.scrollTo\s*\(", r"\.scrollTop\s*=",
                   r"\bpulihkanBaca\s*\(", r"\bsaatGulir\s*\(")

    def test_pemulihan_dan_pendengar_gulir_hidup_di_dalam_saatSiap(self):
        js = self._js()
        badan = TestHamparanBara._fungsi(js, "layarMateri")
        rentang = self._rentang_panggilan(badan, "saatSiap")
        self.assertTrue(rentang, "`layarMateri` tidak lagi memakai `saatSiap()`")

        gagal = []
        for pola in self.TULIS_GULIR:
            for m in re.finditer(pola, badan):
                if not any(a <= m.start() <= b for a, b in rentang):
                    baris = badan[:m.start()].count("\n") + 1
                    gagal.append(f"`{m.group(0).strip()}` di baris ke-{baris} "
                                 "badan layarMateri, DI LUAR callback saatSiap")
        self.assertEqual(
            gagal, [],
            "penulisan/pemulihan gulir berada di jalur senkron badan pembangun "
            "layar. Di sana ia berjalan sebelum `appendChild` dan sebelum "
            "`window.scrollTo({top:0})` milik gambarRute(), jadi nilainya nol "
            "dan nolnya tidak pernah datang sebagai galat: " + "; ".join(gagal))

    def test_pemulihan_tidak_mulus_dan_tidak_bertanya_ke_adaGerak(self):
        """Mengembalikan orang ke tempatnya bukan gerak yang bisa disetel.

        `behavior: "instant"`, bukan `"auto"`. CSSOM-View mendefinisikan
        `"auto"` sebagai "ikuti `scroll-behavior` kotak yang digulir", dan
        `gaya.css` memasang `html { scroll-behavior: smooth }` — jadi `"auto"`
        MULUS di tingkat gerak `penuh` dan `halus`. Versi pertama tes ini
        mengunci string `"auto"` dan lulus di atas animasi 700 px yang nyata:
        sembilan cuplikan `scrollY` yang berubah sepanjang ~650 ms.

        YANG TIDAK DIJAGA TES INI, dan jangan dibaca sebaliknya:

          · ia pagar STRING atas badan `pulihkanBaca`, BUKAN bukti render.
            Bahwa gulirnya benar-benar sinkron hanya bisa dibuktikan dengan
            mencuplik `scrollY` di peramban, dan itu bukan yang terjadi di sini;
          · ia tidak menjaga nilai `scroll-behavior` di CSS — kalau `gaya.css`
            suatu hari memasang sesuatu yang lain, tes ini tetap hijau;
          · ia tidak menjaga pemanggil `window.scrollTo` LAIN di berkas yang
            sama (`bawaKeAtas` sengaja memakai `adaGerak() ? "smooth" : "auto"`,
            dan itu sah karena ia navigasi yang diminta, bukan pemulihan).
            Sapuan seluruh pemanggil adalah pekerjaan S12.
        """
        badan = TestHamparanBara._fungsi(self._js(), "pulihkanBaca")
        self.assertRegex(badan, r'behavior:\s*"instant"',
                         "pemulihan bukan `behavior: \"instant\"`; `\"auto\"` "
                         "mewarisi `scroll-behavior: smooth` dari `html` dan "
                         "menggulir beranimasi ~650 ms")
        self.assertNotIn('"auto"', badan,
                         "`\"auto\"` kembali; ia BUKAN sinonim instan")
        self.assertNotIn("smooth", badan,
                         "pemulihan memakai gulir mulus; isi yang sudah "
                         "terpasang jadi tak terlihat hampir sedetik")
        self.assertNotIn("adaGerak", badan,
                         "pemulihan posisi ditanyakan ke tingkat gerak; ia "
                         "bukan gerak yang menyampaikan sesuatu")
        self.assertNotIn("ResizeObserver", badan,
                         "pemulihan berubah jadi pin; sekali pulih, gulir "
                         "adalah milik pengguna (invarian #15b)")

    def test_penanda_sesi_di_memori_dan_kunci_terpisah_dari_dirender(self):
        """Muat-ulang berarti mulai dari atas, dan itu bentuk bukan janji."""
        js = self._js()
        self.assertRegex(js, r"const materiPernahDigambar = new Set\(\)",
                         "penanda sesi bukan lagi Set di memori; kalau ia "
                         "pindah ke localStorage, F5 akan ikut dipulihkan")
        self.assertRegex(js, r'return `baca\.\$\{key\}\.\$\{indeks\}`',
                         "bentuk kunci berubah")
        # `dirender.` menandai "pernah dibuka", ini "sampai di mana" -- dua
        # pertanyaan berbeda yang tidak boleh berbagi satu kunci.
        badan = TestHamparanBara._fungsi(js, "kunciBaca")
        self.assertNotIn("KUNCI_DIRENDER", badan)
        self.assertNotIn("dirender", badan)
        # Nol localStorage langsung: lewat ctx.ingat, yang sudah menelan
        # kegagalan kuota di aplikasi.js.
        self.assertNotRegex(
            re.sub(r"/\*.*?\*/", " ", js, flags=re.S),
            r"localStorage\s*\.", "localStorage disentuh langsung; pakai ctx.ingat()")


class TestKartuAksiTepi(unittest.TestCase):
    """Kartu aksi materi: relokasi, penjaga lintas-layar, dan tingkat gerak.

    CAKUPAN YANG DIUKUR: badan `layarMateri` di `layar-belajar.js`, plus
    aturan `.aksi-tepi` di `gaya.css`. Tidak disapukan ke layar lain.

    YANG TIDAK DIJAGA, dan jangan dibaca sebaliknya: ini pagar STRUKTUR sumber,
    bukan bukti render. Bahwa kartunya benar-benar tidak menutupi `.kode` atau
    `#konteks`, dan bahwa ia benar-benar hilang sesudah empat detik, hanya bisa
    dibuktikan dengan mengukur `getBoundingClientRect()` dan
    `getComputedStyle().display` di peramban — dan itu bukan yang terjadi di
    sini. Ia juga tidak menjaga nilai `--lengket-atas` maupun urutan Tab.
    """

    @staticmethod
    def _js():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js",
                               "layar-belajar.js"), encoding="utf-8") as f:
            return TestHamparanBara._telanjang(f.read())

    @staticmethod
    def _css():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            return f.read()

    def test_relokasi_bukan_duplikasi(self):
        """Tiga kontrol PINDAH; tidak satu pun muncul dua kali di layar ini."""
        badan = TestHamparanBara._fungsi(self._js(), "layarMateri")
        for panggilan in ("tombolBookmark(", "tombolCatatan(", "tblSelesai,"):
            self.assertEqual(
                badan.count(panggilan), 1,
                f"`{panggilan}` muncul {badan.count(panggilan)}x di pohon "
                "layarMateri; kartu aksi adalah relokasi, bukan salinan")
        self.assertNotIn('h("div.materi-alat"', badan,
                         "`div.materi-alat` masih dibangun di layar materi "
                         "padahal isinya sudah pindah ke kartu")
        # Tombol beraksen "selesai lalu lanjut" TETAP di kaki: ia satu-satunya
        # permukaan beraksen di layar ini, dan menaikkannya membuat yang kedua.
        # Dipotong dengan HITUNG KURUNG, bukan dengan penanda teks berikutnya:
        # kartu aksinya dibangun di antara `nav.materi-kaki` dan `const el`,
        # jadi irisan sampai penanda itu ikut menelan isi kartunya sendiri --
        # dan versi pertama tes ini memang gagal karena itu.
        i = badan.index('h("nav.materi-kaki"')
        j, dalam = badan.index("(", i), 0
        for k in range(j, len(badan)):
            if badan[k] == "(":
                dalam += 1
            elif badan[k] == ")":
                dalam -= 1
                if dalam == 0:
                    break
        kaki = badan[i:k + 1]
        self.assertIn('h("button.tbl.tbl-utama"', kaki,
                      "tindakan utama ikut naik ke kartu; satu layar, satu "
                      "permukaan beraksen")
        self.assertNotIn("tblSelesai", kaki, "tblSelesai belum keluar dari kaki")

    def test_menyembunyikan_hanya_di_luar_mati_dan_lewat_tingkatGerak(self):
        """Diam-4-detik adalah perubahan yang terjadi sendiri, jadi bukan milik `mati`."""
        badan = TestHamparanBara._fungsi(self._js(), "layarMateri")
        self.assertRegex(badan, r'if \(tingkatGerak\(\) !== "mati"\)',
                         "penyembunyian tidak lagi dipagari tingkat gerak")
        self.assertNotIn("dataset.gerak", badan,
                         "tingkat gerak dibaca langsung dari DOM; `tingkatGerak()` "
                         "satu-satunya yang boleh memutuskannya")
        self.assertRegex(badan, r"const AKSI_DIAM_MS|AKSI_DIAM_MS\)",
                         "ambang diam tidak lagi konstanta bernama")
        self.assertNotIn('addEventListener("scroll"', badan,
                         "pendengar gulir mentah; pakai saatGulir()")
        # Jangan menyingkir saat sedang dipakai.
        self.assertRegex(badan, r'matches\(":hover, :focus-within"\)',
                         "kartu bisa hilang saat sedang di-hover atau difokus, "
                         "dan itu mencabut fokus dari orang yang menekan Tab")

    def test_penjaga_lintas_layar_ada_dan_pendengarnya_dilepas(self):
        """`tunda()` tidak punya gagang batal, jadi penundaannya bisa mendarat
        di layar BERIKUTNYA.

        Bedanya dengan pemulihan posisi baca: di sana callback yang terlambat
        cuma menyimpan angka milik layarnya sendiri, sedangkan di sini ia
        MENYENTUH DOM. Tanpa penjaga, sebuah penundaan yang berangkat tepat
        sebelum layar berganti akan menyembunyikan kartu layar berikutnya.
        """
        badan = TestHamparanBara._fungsi(self._js(), "layarMateri")
        i_tunda = badan.index("AKSI_DIAM_MS")
        blok = badan[badan.rindex("tunda(", 0, i_tunda):i_tunda]
        self.assertIn("if (keluarMateri) return;", blok,
                      "callback bertunda kartu aksi tidak dijaga `keluarMateri`; "
                      "ia akan menyentuh DOM layar berikutnya")
        self.assertRegex(badan, r"lepasAksi = saatGulir\(",
                         "pendengar gulir kartu tidak dipegang gagang lepas")
        self.assertRegex(badan, r"keluarMateri = true;\s*\n\s*lepasBaca\(\);"
                                r"\s*\n\s*lepasAksi\(\);",
                         "pendengar kartu tidak dilepas di saatKeluar")

    def test_materi_tata_tetap_tiga_anak_dan_kartu_bukan_salah_satunya(self):
        """`.materi-tata` adalah kisi; item keempat menggeser saudaranya.

        Kisinya dua kolom di >=1130 px dan tiga kolom di >=1380 px, dengan tepat
        tiga item tata letak: rail, kolom utama, peta bagian. Selama kartunya
        `fixed` ia tidak memakan track — tapi begitu sebuah aturan membuatnya
        `static`, ia jadi item keempat yang ditempatkan otomatis, dan yang
        terukur bukan kartunya yang salah tempat melainkan SAUDARANYA:
        `.materi-utama` menyusut dari 770 px jadi 208 px dan `.materi-peta`
        terlempar ke kolom pertama.

        Dijaga sebagai BENTUK sumber supaya tetap berlaku kalau kartunya
        dipindah lagi: yang ditagih adalah daftar anak `.materi-tata`, bukan
        posisi kartunya.
        """
        badan = TestHamparanBara._fungsi(self._js(), "layarMateri")
        i = badan.index('h("div.masuk.materi-tata"')
        j, dalam = badan.index("(", i), 0
        for k in range(j, len(badan)):
            if badan[k] == "(":
                dalam += 1
            elif badan[k] == ")":
                dalam -= 1
                if dalam == 0:
                    break
        pohon = badan[i:k + 1]
        # Anak tingkat-atas: argumen di kedalaman 1 sesudah objek sifatnya.
        dalam, bagian, kini = 0, [], ""
        for c in pohon[j - i:]:
            if c in "([{":
                dalam += 1
                if dalam == 1:
                    continue
            elif c in ")]}":
                dalam -= 1
                if dalam == 0:
                    bagian.append(kini)
                    break
            if dalam == 1 and c == ",":
                bagian.append(kini); kini = ""; continue
            kini += c
        # bagian[0] = penyeleksi, bagian[1] = objek sifat, sisanya anak.
        # Versi pertama memotong dari [1:] dan menghitung `{}` sebagai anak
        # keempat -- tesnya merah di atas kode yang benar.
        anak = [b.strip() for b in bagian[2:] if b.strip()]
        self.assertEqual(
            len(anak), 3,
            f"`.materi-tata` punya {len(anak)} anak tata letak, bukan tiga: "
            f"{[a[:40] for a in anak]}. Item keempat akan ditempatkan otomatis "
            "di kisinya dan menggeser rail/kolom utama/peta bagian")
        self.assertFalse(
            any(a.strip() == "kartuAksi" for a in anak),
            "kartu aksi kembali jadi anak `.materi-tata`; di sana ia jadi item "
            "kisi keempat begitu ada aturan yang membuatnya `static`")
        # Ia tinggal di dalam POHON kolom utama, tepat satu kali. Dipotong
        # dengan hitung kurung: irisan "sampai akhir fungsi" ikut menghitung
        # `kartuAksi.hidden = ...` di bawahnya, dan versi pertama tes ini
        # memang melaporkan lima.
        a = badan.index('h("div.materi-utama"')
        b, dalam = badan.index("(", a), 0
        for c in range(b, len(badan)):
            if badan[c] == "(":
                dalam += 1
            elif badan[c] == ")":
                dalam -= 1
                if dalam == 0:
                    break
        utama = badan[a:c + 1]
        self.assertEqual(utama.count("kartuAksi"), 1,
                         "kartu aksi bukan anak tunggal pohon `.materi-utama`")

    def test_penyembunyian_digerbang_oleh_position_bukan_oleh_ambang(self):
        """Yang static tidak boleh disembunyikan, dan gerbangnya membaca HASIL.

        Menyembunyikan kotak yang ada di ALIRAN memendekkan dokumen; scroll
        anchoring Chrome lalu menggeser gulir, dan penampil yang mendengar gulir
        memunculkannya lagi. Lingkaran itu sudah dibunuh sekali lewat `fixed` —
        keputusan "ikut aliran di tier tiga kolom" melahirkannya kembali kalau
        gerbang ini tidak ada.

        `getComputedStyle(...).position`, BUKAN angka ambang yang disalin ke JS:
        satu ambang yang hidup di dua bahasa menuntut pagarnya sendiri (preseden
        `AMBANG_PANEL`/`AMBANG_RUANG` di repo ini). Dan karena ia dibaca saat
        callback berjalan, ia tetap benar sesudah jendela diubah ukuran melintasi
        tier.

        PAGAR BENTUK, dan yang TIDAK ia jaga: posisi nyata kartu lintas tier —
        apakah ia benar-benar tidak menumpuk `.materi-peta` di 1440 px, dan
        apakah `.materi-utama` benar-benar selebar yang sama di `penuh` dan
        `mati`. Itu hanya bisa dibuktikan dengan `getBoundingClientRect()` di
        peramban, dan itu milik tabel bukti render di laporan, bukan tes ini.
        """
        badan = TestHamparanBara._fungsi(self._js(), "layarMateri")
        tulis = [m.start() for m in re.finditer(r"kartuAksi\.hidden = true;", badan)]
        self.assertTrue(tulis, "tidak ada lagi yang menyembunyikan kartu")
        for i in tulis:
            # Gerbangnya harus berdiri DI ATAS penulisan itu, di blok yang sama.
            awal = badan.rindex("{", 0, i)
            blok = badan[awal:i]
            self.assertRegex(
                blok,
                r'getComputedStyle\(kartuAksi\)\.position === "static"\) return;',
                "penulisan `kartuAksi.hidden = true` tidak digerbang "
                "`position !== \"static\"`; di tier tiga kolom kartunya ikut "
                "aliran, dan menyembunyikannya menghidupkan lagi lingkaran "
                "sembunyi-muncul lewat scroll anchoring")
        self.assertNotRegex(
            badan, r"\b1380\b",
            "ambang lebar disalin ke JS; ia sudah hidup di `@container "
            "panggung (min-width: 1380px)`, dan dua salinan satu angka menuntut "
            "pagarnya sendiri")

    def test_aturan_dasar_mendahului_blok_yang_menimpanya(self):
        """Yang menyelesaikan seri spesifisitas di berkas ini adalah URUTAN.

        `.aksi-tepi { position: fixed }` dan `@container … { .aksi-tepi {
        position: static } }` sama-sama (0,1,0). Waktu aturan dasarnya ditulis
        SESUDAH blok tier, yang menang dasarnya — dan terukur: kartu tetap
        `fixed` di 1440 px dan menumpuk `.materi-peta` 199x42 px, padahal
        aturan tiernya ada dan terbaca. Menaikkan spesifisitas untuk menang atas
        urutan yang salah adalah eskalasi tanpa ujung; itu sebabnya `@media` dan
        `@container` tinggal di kaki berkas.

        Yang dijaga: URUTAN TEKS, bukan hasil render. Sebuah aturan bisa berada
        lebih dulu dan tetap kalah kalau penimpanya lebih spesifik — dan itu
        memang sah. Karena itu:

        YANG TIDAK DIJAGA: override yang SENGAJA dibuat lebih spesifik. Kalau
        sebuah nama butuh itu, daftarkan di `SENGAJA_LEBIH_SPESIFIK` beserta
        alasannya, jangan longgarkan predikatnya. Contoh yang sudah ada dan
        TIDAK tertangkap pagar ini karena memang bukan kasusnya:
        `html[data-gerak="mati"] .aksi-tepi` (0,2,1), yang berdiri di luar blok
        mana pun dan berkata `static` juga.

        Sapuan penuh atas `gaya.css` memberi NOL kasus saat pagar ini ditulis,
        jadi cakupannya seluruh berkas — bukan satu nama.
        """
        SENGAJA_LEBIH_SPESIFIK = {}     # nama -> alasan; kosong hari ini

        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            css = f.read()
        # Komentar dibuang TAPI barisnya dipertahankan, supaya nomor baris di
        # pesan gagal masih menunjuk tempat yang benar di berkas aslinya.
        telanjang = re.sub(r"/\*.*?\*/",
                           lambda m: "\n" * m.group(0).count("\n"), css, flags=re.S)

        dalam, blok_awal = 0, None
        override, luar = {}, {}
        for i, t in enumerate(telanjang.split("\n"), start=1):
            kepala = t.strip()
            if kepala.startswith(("@media", "@container", "@supports")):
                if dalam == 0:
                    blok_awal = i
                dalam += 1
                continue
            if dalam > 0:
                m = re.match(r"^\s*([.#][\w-]+)(?:[\s,{:].*)?\{", t)
                if m:
                    override.setdefault(m.group(1), []).append(blok_awal)
                dalam += t.count("{") - t.count("}")
                if dalam < 0:
                    dalam = 0
            else:
                m = re.match(r"^([.#][\w-]+)\s*\{", t)
                if m:
                    luar.setdefault(m.group(1), i)

        gagal = []
        for nama, tempat in sorted(override.items()):
            if nama in SENGAJA_LEBIH_SPESIFIK or nama not in luar:
                continue
            for awal_blok in tempat:
                if luar[nama] > awal_blok:
                    gagal.append(f"{nama}: aturan dasar :{luar[nama]} ditulis "
                                 f"SESUDAH blok yang menimpanya :{awal_blok}")
                    break
        self.assertEqual(
            gagal, [],
            "aturan dasar berdiri sesudah blok yang menimpanya; pada "
            "spesifisitas yang sama yang belakangan menang, jadi override-nya "
            "tidak pernah berlaku dan tidak ada galat yang muncul: "
            + "; ".join(gagal))

    def test_lebar_kartu_tidak_mengikuti_keadaan_alirannya(self):
        """Satu deklarasi lebar yang benar untuk KEDUA keadaan alirannya.

        `.aksi-tepi` berpindah antara `fixed` (di luar aliran, saat melayang)
        dan `static` (di dalam aliran, di tier lebar dan di `gerak="mati"`). Di
        luar aliran kotaknya menyusut ke kontennya; di dalam aliran kotak
        block-level memenuhi induknya. Tanpa deklarasi lebar, KARTU YANG SAMA
        terukur 257 px waktu `fixed` dan 1013 px waktu `static` di jendela
        1100 px — empat kali lebih gendut, dengan tiga tombol yang saling
        berjauhan dan tidak ada galat yang muncul di mana pun. `fit-content` =
        `min(max-content, tersedia)`: menyusut seperti saat di luar aliran, dan
        tetap tidak bisa meluber di kolom sempit — yang justru tidak dijamin
        `max-content`.

        YANG DIJAGA: SUMBER KEBENARAN LEBARNYA, yaitu satu deklarasi yang benar
        untuk kedua keadaan. BUKAN HASILNYA. Bahwa lebar terukurnya benar-benar
        sama di kedua keadaan cuma bisa dibuktikan `getBoundingClientRect()` di
        peramban, dan angka itu milik tabel render di laporan, bukan tes ini.

        YANG TIDAK DIJAGA: konteks INDUKNYA. Kalau sebuah hun memindahkan kartu
        ini ke induk `display: grid` atau `flex`, `fit-content` tetap terbaca di
        sini dan tes ini tetap hijau — sementara kartunya melebar lagi karena
        alasan yang sama sekali berbeda, yaitu `stretch` yang jadi nilai awal
        perataan di sana. Jangan baca tes ini sebagai "kelasnya sudah dijaga".

        CAKUPANNYA SATU NAMA, dan itu diukur bukan ditebak. Kelas
        "persimpangan aliran" — aturan dasar `fixed|absolute` yang di-override
        jadi `static|relative` di blok tier/gerak — berpenghuni DUA nama di
        `gaya.css` hari ini: `.aksi-tepi` (`fixed` :3266 -> `static` :4298 dan
        :4436) dan `.rel-panel` (`absolute` :897 -> `static` :4471). `.rel-turun`
        BUKAN anggotanya (`relative` -> `static`; kedua-duanya di dalam aliran,
        lebarnya tidak berubah). `.rel-panel` menyelesaikan soal yang sama
        dengan cara lain yang sah: blok override-nya menyetel ulang
        `min-width: 0; padding: 0; ...` sendiri. Predikat ini disapukan ke
        keduanya akan MERAH pada `.rel-panel` hari ini — ia punya
        `min-width: 264px` dan tidak punya `width` sama sekali — dan pagar yang
        merah permanen berhenti dibaca.
        """
        # Ditelanjangi DULU. Komentar di blok ini menyebut `max-content` dengan
        # sengaja, karena itulah yang menerangkan kenapa `fit-content` yang
        # dipilih; predikat (2) yang membaca berkas mentah menghukum
        # penjelasannya sendiri.
        css = TestHamparanBara._telanjang(self._css())
        m = re.search(r"^\.aksi-tepi\s*\{", css, re.M)
        self.assertIsNotNone(
            m, "aturan dasar `.aksi-tepi` tidak ada lagi di tingkat atas "
               "berkas; kalau ia dipindahkan, pindahkan juga pagar ini")
        # Dipotong dengan HITUNG KURUNG sampai `}` padanya sendiri — bukan
        # sampai `@media` atau sampai baris berikutnya. Dua irisan salah sudah
        # terjadi di paket ini (`bagian[1:]` yang ikut menghitung objek props,
        # dan irisan "sampai akhir fungsi" yang ikut menyeret tetangganya), dan
        # keduanya ketahuan persis dengan cara ini.
        sisa = css[m.start():]
        tutup = next(i for i, d in TestHamparanBara._kedalaman(sisa)
                     if d == 1 and sisa[i] == "}")
        blok = sisa[sisa.index("{") + 1:tutup]

        self.assertRegex(
            blok, r"(?<![-\w])width:\s*fit-content\b",
            "`width: fit-content` hilang dari aturan dasar `.aksi-tepi`; tanpa "
            "ia kartunya memenuhi induknya begitu `position` jadi `static`")
        self.assertNotIn(
            "max-content", blok,
            "`max-content` tidak punya batas atas: di kolom sempit kartunya "
            "meluber keluar, dan itu tidak terlihat sampai jendelanya disempitkan")
        # `\b` di sini sengaja LONGGAR — ia ikut menangkap `min-width` dan
        # `max-width`, karena keduanya memaku lebar yang sama persis.
        px = re.search(r"\b(?:min-|max-)?width:\s*[\d.]+px", blok)
        self.assertIsNone(
            px, "lebar kartu dipaku angka piksel absolut "
                f"({px.group(0) if px else ''}); ia harus mengikuti isinya, "
                "bukan angka yang benar di satu tier saja")
        self.assertNotIn(
            "justify-self", blok,
            "`justify-self` mati di kedua keadaan aliran kartu ini (`fixed` "
            "tidak punya induk kisi; `static` induknya bukan kisi) dan sudah "
            "sekali dicabut dari sini karena itu")

    def test_sembunyi_adalah_keadaan_dan_dipulihkan_di_css(self):
        """`hidden` sebagai keadaan, dan komponennya terdaftar di pemulih."""
        badan = TestHamparanBara._fungsi(self._js(), "layarMateri")
        self.assertRegex(badan, r"kartuAksi\.hidden = (true|false);",
                         "kartu tidak lagi memakai `hidden` sebagai keadaan")
        self.assertNotIn("kartuAksi.style", badan,
                         "opacity/transform ditulis dari JS; transisinya milik "
                         "`.masuk-mandiri`, bukan komponen ini")
        css = self._css()
        self.assertIn(".aksi-tepi[hidden]", css,
                      "`.aksi-tepi` menyetel display sendiri tapi tidak ada di "
                      "daftar pemulih; `hidden` tidak akan menyembunyikan apa pun")
        self.assertIn('h("aside.aksi-tepi.masuk-mandiri"', badan,
                      "kartu tidak memakai util entrance S01")
        self.assertEqual(css.count("@starting-style {"), 4,
                         "blok @starting-style bertambah; `.masuk-mandiri` yang "
                         "sudah ada seharusnya cukup")
        self.assertRegex(css, r'html\[data-gerak="mati"\] \.aksi-tepi \{ position: static; \}',
                         "di `mati` kartu tetap sticky; kartu permanen yang "
                         "menempel akan menutupi baris kode di bawahnya")


class TestPintasanPembaca(unittest.TestCase):
    """Lapisan papan ketik halaman materi: `j`/`k`, `[`/`]`, `⏎`.

    CAKUPAN YANG DIUKUR: `pintasanPembaca`, `blokKode`, `lompat`, dan
    `layarMateri` di `layar-belajar.js`, plus array `PINTASAN` di
    `layar-lain.js`. Tidak disapukan ke layar lain dan tidak menyentuh
    `aplikasi.js` — pemilik pintasan global itu kontrak, bukan kelalaian.

    YANG TIDAK DIJAGA, dan jangan dibaca sebaliknya: ini pagar STRUKTUR sumber.
    Bahwa `j` benar-benar mendaratkan blok di dalam viewport, bahwa perhentian
    Tab benar-benar tidak bertambah, dan bahwa `⏎` benar-benar menghasilkan
    kartu keluaran yang sama dengan klik — ketiganya cuma bisa dibuktikan
    dengan `getBoundingClientRect()` dan peristiwa tombol asli di peramban, dan
    itu milik tabel render di laporan. Tes ini tidak menjalankan satu pun.
    """

    @staticmethod
    def _js():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js",
                               "layar-belajar.js"), encoding="utf-8") as f:
            return TestHamparanBara._telanjang(f.read())

    @staticmethod
    def _lain():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js",
                               "layar-lain.js"), encoding="utf-8") as f:
            return TestHamparanBara._telanjang(f.read())

    @staticmethod
    def _nilai_kunci(src, kunci):
        """Teks nilai sebuah kunci di objek literal, dipotong dengan hitung kurung.

        Tiga bentuk yang sama-sama sah dan sama-sama dipakai repo ini diterima:
        `kunci: <ekspresi>`, `kunci: () => { ... }`, dan `kunci() { ... }`.

        Irisan sampai koma pertama TIDAK cukup: untuk
        `bersihkan: () => { lepasGulir(); hentikan(); }` koma pertama yang
        ditemui ada di dalam badannya sendiri, dan yang terpotong jadi separuh
        kalimat yang kebetulan masih terbaca.
        """
        m = re.search(rf"\b{re.escape(kunci)}\s*(\(|:)", src)
        if not m:
            raise AssertionError(f"kunci `{kunci}` tidak ada di objek itu")
        mulai = m.end() - 1
        dalam = 0
        for j in range(mulai, len(src)):
            c = src[j]
            if c in "({[":
                dalam += 1
            elif c in ")}]":
                dalam -= 1
                if dalam < 0:
                    return src[mulai:j]
            elif c == "," and dalam == 0:
                return src[mulai:j]
        return src[mulai:]

    @staticmethod
    def _tabel(src, nama):
        """Kolom pertama tiap baris sebuah array literal `const <nama> = [...]`.

        Dipotong dengan hitung kurung siku, bukan sampai baris `];` pertama:
        sebuah baris yang memuat `[` di dalam teksnya membuat irisan berbasis
        baris berhenti di tempat yang salah tanpa satu pun galat.

        Dan penghitungnya WAJIB melewati literal string — bukan kehati-hatian
        berlebihan: daftar yang dibaca di sini justru MEMAKAI `"["` dan `"]"`
        sebagai nama tombol, jadi penghitung yang naif menutup arraynya di
        baris keempat dan mengembalikan tiga dari lima barisnya. Versi pertama
        tes ini melakukan persis itu, dan yang menegurnya bukan galat melainkan
        sebuah angka yang salah.
        """
        i = src.index(f"const {nama} = [")
        awal = src.index("[", i)
        dalam = 0
        j = awal
        isi = None
        while j < len(src):
            c = src[j]
            if c == '"':
                j += 1
                while j < len(src) and src[j] != '"':
                    j += 2 if src[j] == "\\" else 1
            elif c == "[":
                dalam += 1
            elif c == "]":
                dalam -= 1
                if dalam == 0:
                    isi = src[awal + 1:j]
                    break
            j += 1
        if isi is None:
            raise AssertionError(f"array {nama} tidak tertutup")
        return re.findall(r'\[\s*"((?:[^"\\]|\\.)*)"', isi)

    def test_tabel_pintasan_pembaca_sama_dengan_daftar_bantuan(self):
        """Yang DIPASANG dan yang DITAMPILKAN adalah dua definisi satu hal.

        `PINTASAN_PEMBACA` memasang tombolnya; `PINTASAN` di `layar-lain.js`
        memberitahukannya lewat `?`. Keduanya ditulis tangan, dan dua daftar
        yang tidak pernah dibandingkan adalah dua daftar yang suatu hari
        berbeda tanpa ada yang menyadarinya — kegagalannya pun senyap: tombol
        yang bekerja tapi tidak pernah diumumkan sama tidak bergunanya dengan
        tombol yang diumumkan tapi tidak bekerja.

        Perbandingannya bisa ditulis tanpa menebak karena `PINTASAN` punya
        TEPAT SATU konsumen hari ini (`tampilkanBantuan()` di berkas yang sama).

        YANG TIDAK DIJAGA: artinya. Kolom kedua kedua daftar boleh berbeda kata
        dan tes ini diam — yang dijaga cuma bahwa tombolnya diumumkan.
        """
        pembaca = self._tabel(self._js(), "PINTASAN_PEMBACA")
        bantuan = self._tabel(self._lain(), "PINTASAN")
        self.assertEqual(len(pembaca), 5,
                         f"tabel pembaca berubah jumlah barisnya: {pembaca}")
        self.assertEqual(len(set(pembaca)), len(pembaca),
                         f"ada tombol yang didaftarkan dua kali: {pembaca}")
        hilang = [t for t in pembaca if t not in bantuan]
        self.assertEqual(
            hilang, [],
            "tombol dipasang di halaman materi tapi tidak diumumkan di daftar "
            f"`?`: {hilang}. Daftar bantuan sekarang: {bantuan}")

    def test_penangan_membaca_tabel_bukan_cabang_per_tombol(self):
        """Satu tabel, satu pencarian — bukan lima cabang `if` yang tersebar.

        Cabang yang tersebar bukan soal selera: ia membuat tabel di atasnya jadi
        dokumentasi, bukan sumber. Begitu keduanya boleh berbeda, tes silang di
        atas berhenti membuktikan apa pun tentang yang benar-benar dipasang.
        """
        badan = TestHamparanBara._fungsi(self._js(), "saatTombol")
        self.assertIn("PINTASAN_PEMBACA.find(", badan,
                      "penangan tidak lagi membaca tabelnya")
        for tombol in ('"j"', '"k"', '"["', '"]"', '"Enter"'):
            self.assertNotIn(
                f"e.key === {tombol}", badan,
                f"cabang per-tombol untuk {tombol} muncul lagi di penangan; "
                "tabelnya jadi hiasan")

    def test_tiga_penjaga_berurutan_dan_pemilik_tidak_dibungkam(self):
        """Tiga penjaga, urut, dan `stopPropagation()` tidak dipakai.

        (1) `e.defaultPrevented`. Pendengar global `aplikasi.js` terdaftar di
            `mulai()`, jadi ia SELALU berjalan lebih dulu. Kasus nyatanya
            `Ctrl+J`: `e.key`-nya "j", dan tanpa penjaga ini satu penekanan
            mengganti tema sekaligus melompat satu blok kode.
        (2) Medan isian. Mengetik `jjk` di editor blok kode harus menulis tiga
            huruf.
        (3) `artikel.isConnected`. Pendengarnya di `document`; yang membatasinya
            pada layar ini cuma penjaga ini dan pelepasan di `saatKeluar`.

        `stopPropagation()` akan "menyelesaikan" (1) dari sisi yang salah: ia
        membungkam pemilik pintasan, dan pemilik yang dibungkam tidak pernah
        tahu ia dibungkam.

        Urutannya diperiksa sebagai POSISI TEKS, bukan sebagai perilaku: sebuah
        penjaga yang berdiri lebih dulu tetap bisa salah menilai. Yang dijamin
        di sini hanya bahwa tidak ada pekerjaan yang dikerjakan sebelum
        ketiganya lewat.
        """
        badan = TestHamparanBara._fungsi(self._js(), "saatTombol")
        self.assertIn(
            "if (e.defaultPrevented) return;", badan,
            "penjaga `defaultPrevented` hilang; tombol yang sudah diambil "
            "pemilik global akan dikerjakan dua kali (terukur: Ctrl+J)")
        self.assertIn(
            'e.target.matches("input, textarea, select, [contenteditable]")',
            badan,
            "penjaga medan isian hilang; mengetik j/k di editor akan "
            "memindahkan fokus alih-alih menulis huruf")
        self.assertIn(
            "if (!artikel.isConnected) return;", badan,
            "penjaga layar hilang; pendengar di `document` akan menggerakkan "
            "layar yang bukan miliknya")
        self.assertNotIn(
            "stopPropagation", badan,
            "layar ini membungkam pemilik pintasan global")

        i_cegah = badan.index("e.defaultPrevented")
        i_medan = badan.index("e.target.matches(")
        i_hidup = badan.index("artikel.isConnected")
        i_kerja = badan.index("PINTASAN_PEMBACA.find(")
        self.assertLess(i_cegah, i_medan, "urutan penjaga tertukar")
        self.assertLess(i_medan, i_hidup, "urutan penjaga tertukar")
        self.assertLess(i_hidup, i_kerja,
                        "ada pekerjaan yang dikerjakan sebelum penjaganya lewat")

    def test_pembungkus_blok_kode_difokus_tanpa_menambah_perhentian_tab(self):
        """`tabindex="-1"`: bisa `focus()`, nol perhentian Tab baru.

        Dengan `"0"` setiap contoh kode menyisipkan satu perhentian kosong di
        antara tombol-tombol yang memang berguna — di materi berisi tiga blok
        itu tiga penekanan Tab tambahan yang tidak mengantar ke mana pun.

        YANG TIDAK DIJAGA: jumlah perhentian Tab yang sebenarnya. Atribut ini
        SYARAT, bukan buktinya; hitungan nyatanya diukur di peramban dengan
        pemilih yang sama di kedua sisi hun, dan angkanya ada di laporan.
        """
        badan = TestHamparanBara._fungsi(self._js(), "blokKode")
        self.assertIn(
            'h("div.blok-kode", { tabindex: "-1" }', badan,
            "pembungkus blok kode tidak lagi `tabindex=\"-1\"`; dengan `\"0\"` "
            "ia menambah satu perhentian Tab per blok, dengan tanpa atribut "
            "`focus()` tidak menggigit dan `j`/`k` kehilangan sasarannya")
        self.assertNotIn(
            "outline", badan,
            "gaya fokus ditulis di JS; cincinnya milik `:focus-visible` global")

    def test_pendengar_keydown_dilepas_di_saatKeluar(self):
        """Pendengar di `document` yang tertinggal = dua layar, satu tombol.

        Preseden `layar-kerja.js`: yang mendaftarkan di `document` wajib
        menyimpan pelepasnya dan memanggilnya saat layarnya ditinggalkan.
        Kegagalannya senyap dan menumpuk — satu pendengar per kunjungan.
        """
        js = self._js()
        pasang = TestHamparanBara._fungsi(js, "pintasanPembaca")
        self.assertIn('document.addEventListener("keydown", saatTombol)', pasang)
        self.assertIn('document.removeEventListener("keydown", saatTombol)',
                      pasang,
                      "`pintasanPembaca` tidak mengembalikan pelepas yang nyata")

        layar = TestHamparanBara._fungsi(js, "layarMateri")
        self.assertIn("const lepasTombol = pintasanPembaca(artikel, peta);", layar,
                      "lapisan papan ketik tidak lagi dipasang di layar materi")
        keluar = layar[layar.index("saatKeluar:"):]
        self.assertIn(
            "lepasTombol();", keluar,
            "pelepas tidak dipanggil di `saatKeluar`; pendengarnya tetap hidup "
            "sesudah layar materi ditinggalkan")

    def test_ujung_daftar_dijepit_bukan_dilingkar(self):
        """Di ujung berhenti, tidak melingkar — untuk blok MAUPUN bagian.

        Melingkar berarti satu penekanan di blok terakhir memindahkan layar
        sejauh seluruh halaman. Tidak ada yang meminta perpindahan sebesar itu
        dari tombol yang artinya "berikutnya", dan yang terjadi bukan orang
        belajar polanya melainkan orang berhenti memakai tombolnya.

        Preseden bentuknya `panahAntarUbin`, yang sudah memakai jepitan yang
        sama persis untuk alasan yang sama.
        """
        js = self._js()
        blok = TestHamparanBara._fungsi(js, "pintasanPembaca")
        self.assertRegex(
            blok, r"Math\.max\(0,\s*Math\.min\(daftar\.length - 1,\s*tuju\)\)",
            "jepitan pada daftar blok kode hilang; `j` di blok terakhir "
            "melingkar ke blok pertama")
        bagian = TestHamparanBara._fungsi(js, "lompat")
        self.assertRegex(
            bagian, r"Math\.max\(0,\s*Math\.min\(butir\.length - 1,\s*i \+ arah\)\)",
            "jepitan pada daftar bagian hilang; `]` di bagian terakhir "
            "melingkar ke bagian pertama")

    def test_enter_memakai_tombol_yang_sudah_ada_bukan_definisi_kedua(self):
        """"Bisa dijalankan" tetap punya SATU definisi, dan `⏎` meminjamnya.

        Definisinya `p.bisa_dijalankan && bhs.siap` di `blokKode`, dan tombol
        Jalankan ADALAH hasil definisi itu. Menanyakannya lewat tombol berarti
        tidak ada angka atau syarat kedua yang bisa melenceng, dan `/api/coba`
        tetap disentuh dari satu tempat saja.

        Blok tanpa tombol tidak mengubah apa pun — keadaan, bukan galat.
        """
        badan = TestHamparanBara._fungsi(self._js(), "jalankanBlokFokus")
        self.assertIn('.blok-alat .tbl-utama', badan,
                      "`⏎` tidak lagi memakai tombol Jalankan yang sudah ada")
        self.assertNotIn("bisa_dijalankan", badan,
                         "definisi kedua untuk \"bisa dijalankan\" muncul di "
                         "jalur papan ketik")
        self.assertNotIn("/api/coba", badan,
                         "`/api/coba` disentuh dari tempat kedua")
        self.assertIn('classList.contains("blok-kode")', badan,
                      "`⏎` bereaksi walau fokusnya bukan pembungkus blok kode")

    def test_layar_ini_tidak_menangani_tanda_tanya(self):
        """`?` milik `aplikasi.js`, dan layar ini tidak boleh ikut memilikinya.

        Tombol yang punya dua pemilik adalah tombol yang perilakunya bergantung
        pada urutan pendaftaran pendengar — dan urutan itu tidak ditulis di mana
        pun, jadi ia berubah diam-diam setiap kali sebuah layar dipasang lebih
        awal atau lebih lambat.

        CAKUPANNYA DISEMPITKAN, dan yang menyempitkannya sebuah angka. Versi
        pertama menuntut `"?"` tidak muncul di SELURUH berkas, dan itu menghukum
        `h("span.pil", {}, "?")` — sebuah label antarmuka biasa yang tidak ada
        hubungannya dengan pintasan. Preseden yang sama sudah dua kali tercatat
        di repo ini: sapuan predikat komentar ke seluruh `statik/js/` memberi 28
        kasus yang semuanya sah, dan `.rel-panel` menyelesaikan soal lebar
        dengan cara lain yang juga sah. Pagar yang merah karena hal yang bukan
        urusannya berhenti dibaca, dan itu sudah tiga kali tercatat di paket ini.

        YANG TIDAK LAGI TERJEBAK, dan sebutkan supaya tidak dikira terjaga:
        sebuah cabang `?` yang ditulis di fungsi LAIN di berkas ini. Yang
        menjaga kelas itu paragraf ini, yang dibaca manusia — bukan tes ini.

        `tampilkanBantuan` TETAP disapu ke seluruh berkas, dan perluasannya
        tidak butuh pembelaan yang sama: token itu nama fungsi ekspor
        `layar-lain.js` dan tidak mungkin muncul di sini karena alasan lain,
        jadi positif-palsunya nol menurut konstruksi, bukan menurut selera.
        """
        js = self._js()
        for nama in ("pintasanPembaca", "saatTombol"):
            self.assertNotIn(
                '"?"', TestHamparanBara._fungsi(js, nama),
                f"`{nama}` memakai `?` sebagai tombol; pemiliknya "
                "`tampilkanBantuan()` di `aplikasi.js`")
        self.assertNotIn(
            "tampilkanBantuan", js,
            "halaman materi memanggil dialog bantuan sendiri")
        self.assertNotIn("?", self._tabel(js, "PINTASAN_PEMBACA"),
                         "`?` masuk ke tabel pintasan pembaca")

    def test_pintasan_tidak_menembus_dialog_yang_terbuka(self):
        """Dialog terbuka menahan lapisan ini, dan itu BUKAN penjaga yang sama.

        `e.defaultPrevented` menjawab "tombol ini sudah dipunyai siapa".
        `jendelaTerbuka()` menjawab "bolehkah halaman di belakang dialog
        bergerak". Dua pertanyaan berbeda, dan hanya satu yang dijawab oleh
        jawaban pertama — itu sebabnya penjaga pertama tidak menutup kasus ini.

        Terukur sebelum penjaganya ada: `?` membuka dialog bantuan (fokus di
        tombol Tutup, gulir 900), lalu satu `j` memindahkan fokus ke blok kode
        dan gulir ke 2018, lalu `]` ke 2677 — dialognya tetap menggantung di
        atas halaman yang barusan dipindahkan di belakangnya, tanpa satu pun
        galat. Jalur bermodifier tidak pernah bocor lewat sini: `Ctrl+K`
        menaruh fokus di medan isian palet, jadi ia tertahan penjaga medan.

        `jendelaTerbuka()` dipanggil dari `inti.js`, PEMILIK dialognya.
        Memanggil milik pemilik bukan menyalin keadaan siapa pun; yang dilarang
        justru dua jalan yang menghindarinya — `stopPropagation()`, yang
        membungkam pemilik pintasan, dan membaca DOM sendiri untuk menebak ada
        dialog, yang melahirkan definisi kedua dari "sedang ada jendela".

        YANG TIDAK DIJAGA: bahwa halamannya benar-benar tidak bergerak. Itu
        empat angka render (fokus tetap di dalam `.jendela`, `scrollY` tetap,
        indeks `.kini` tetap) dan tempatnya tabel di laporan, bukan tes ini.
        """
        js = self._js()
        badan = TestHamparanBara._fungsi(js, "saatTombol")
        self.assertIn(
            "if (jendelaTerbuka()) return;", badan,
            "lapisan papan ketik menembus dialog yang terbuka: halaman di "
            "belakangnya bergerak sementara dialognya menggantung di atasnya")
        self.assertRegex(
            js, r'import \{[^}]*\bjendelaTerbuka\b[^}]*\} from "\./inti\.js";',
            "`jendelaTerbuka` tidak diimpor dari pemilik dialognya")
        self.assertNotIn(
            ".jendela", badan,
            "layar ini membaca DOM sendiri untuk menebak ada dialog; itu "
            "definisi kedua dari keadaan yang sudah punya pemiliknya")

        i_cegah = badan.index("e.defaultPrevented")
        i_dialog = badan.index("jendelaTerbuka()")
        i_kerja = badan.index("PINTASAN_PEMBACA.find(")
        self.assertLess(i_cegah, i_dialog,
                        "penjaga dialog berdiri sebelum penjaga pemilik tombol")
        self.assertLess(i_dialog, i_kerja,
                        "ada pekerjaan yang dikerjakan sebelum penjaga dialog")

    def test_aturan_penanda_bagian_hanya_ada_satu_di_berkas_ini(self):
        """Satu aturan penanda, dua pemanggil — bukan dua aturan.

        "Bagian yang sedang dibaca" = bagian TERAKHIR yang tepinya sudah
        melewati sepertiga atas layar. Aturan itu hidup di `tandaiAktif()` saja.
        Dua pemanggilnya menangkap dua hal yang berbeda dan keduanya perlu:
        `IntersectionObserver` menangkap perubahan yang terjadi TANPA gulir
        (tata letak bergeser, gambar selesai dimuat, jendela diubah ukurannya),
        sedangkan langganan gulir menangkap perpindahan yang TIDAK melintasi
        ambang observer — dan yang terakhir itu bukan kasus teoretis: dari
        puncak halaman ke bagian pertama, tidak ada ambang yang dilewati sama
        sekali, jadi observernya tidak pernah dipanggil ulang.

        Yang dijaga di sini HITUNGAN, bukan perilaku: dua salinan aturan akan
        tetap memberi jawaban yang sama hari ini dan berbeda suatu hari, dan
        hari itu tidak akan ada yang menyadarinya.

        HITUNGANNYA TERNORMALISASI, dan versi pertama pagar ini membuktikan
        kenapa itu perlu. Ia menghitung potongan byte persis — `"innerHeight *
        0.34"` dan `'classList.toggle("kini"'` — jadi dua salinan penuh aturan
        ini lolos hijau hanya karena ditulis sedikit berbeda: satu memakai
        `window.innerHeight*0.34` tanpa spasi dengan kelas `'kini'` berkutip
        tunggal, satu lagi memakai `classList.add(  "kini"  )` dengan spasi
        ganda. Keduanya menggandakan seluruh aturan; suite tetap 834 hijau.
        Hitungan byte-eksak hanya membuktikan salinan yang identik byte.

        LAPANGAN BUKTINYA diuji BERPASANGAN — satu suntingan yang MENYALIN
        aturan (wajib merah) dan satu yang MENYUSUN ULANG tanpa menyalin
        (wajib hijau) — dan kedua hasilnya diukur, bukan diklaim:

          MENYALIN, merah  : ambang lewat konstanta bernama `BATAS` digabung
                             penanda lewat `className += " kini"` -> asersi
                             nilai `0.34` jatuh (2 != 1);
                             `window.innerHeight*0.34` + `'kini'` kutip tunggal
                             -> asersi operasi jatuh (2 != 1);
                             `classList.add(  "kini"  )` dengan ambang ditulis
                             terbalik -> asersi kelas jatuh (2 != 1);
                             salinan byte-identik -> asersi operasi jatuh.
          MENYUSUN ULANG, hijau : merapikan spasi di sekitar `*` pada satu-
                             satunya kemunculan ambang, mengganti kutip ganda
                             jadi tunggal pada satu-satunya `toggle("kini")`,
                             dan merapikan spasi di dalam kurung pemanggilan.

        DUA ASERSI BENTUK SAJA TIDAK CUKUP, dan itu terbukti bukan dikira:
        sebuah salinan yang menulis ambangnya lewat konstanta bernama
        (`const BATAS = 0.34; ... window.innerHeight * BATAS`) DAN penandanya
        lewat `a.className += " kini"` lolos kedua asersi bentuk sekaligus.
        Masing-masing lubangnya sudah diakui di docstring versi sebelumnya —
        dan pengakuan jujur bukan perbaikan: gabungan dua lubang yang
        sama-sama diakui tetap sebuah salinan yang hijau.

        Yang menutupnya bukan daftar bentuk yang dilarang (daftar itu selalu
        kalah dari daftar bentuk yang ADA), melainkan KUNCI NILAI: angka
        ambangnya sendiri, `0.34`, tidak bisa dipinjam sebuah salinan tanpa
        dituliskan lagi — mau lewat konstanta, mau lewat operan terbalik, mau
        lewat fungsi pembantu. Dua asersi sisanya menutup jalan menulis kelas
        yang tidak lewat `classList.<metode>("kini")`.

        Populasinya diukur hari ini di `layar-belajar.js`, bukan ditebak:
        `0.34` muncul TEPAT SATU kali, `className` NOL kali, `classList[` NOL
        kali. Ketiga asersi itu karena itu berpositif-palsu nol saat ditulis.

        YANG TIDAK DIJAGA, dan ini daftar yang tersisa sesudah lubang di atas
        ditutup: ambang yang ditulis dengan nilai yang SAMA tapi ejaan angka
        berbeda (`0.340`, `34 / 100`, `1 / 3`), dan kelas yang dipasang lewat
        `setAttribute("class", ...)`. Keduanya salinan yang masih akan lolos.
        """
        js = self._js()
        self.assertEqual(
            len(re.findall(r"innerHeight\s*\*\s*0\.34", js)), 1,
            "ambang penanda bagian muncul lebih dari sekali; salinannya akan "
            "menjawab berbeda dari aslinya suatu hari")
        self.assertEqual(
            len(re.findall(r"classList\s*[.=]\s*(?:toggle|add|remove)"
                           r"\s*\(\s*['\"]kini['\"]", js)), 1,
            "penanda `.kini` disetel dari lebih dari satu tempat")
        # KUNCI NILAI: angkanya sendiri, bukan operasinya. Sebuah salinan boleh
        # menulis ulang operasinya sesuka hati, tapi ia tidak bisa memakai
        # ambang ini tanpa menuliskan angkanya sekali lagi di suatu tempat.
        self.assertEqual(
            len(re.findall(r"\b0\.34\b", js)), 1,
            "angka ambang penanda muncul lebih dari sekali — termasuk kalau ia "
            "disembunyikan di balik konstanta bernama; salinan yang memakainya "
            "tetap harus menuliskannya, dan di situlah ia tertangkap")
        self.assertNotRegex(
            js, r"classList\s*\[",
            "kelas disetel lewat indeks terhitung (`classList[nama]`), jalan "
            "yang tidak bisa dibaca asersi metode di atas")
        self.assertNotRegex(
            js, r"className[^;]*kini",
            "penanda dipasang lewat `className`, bukan lewat `classList`; "
            "itu mesin kedua yang memakai pintu lain")
        peta = TestHamparanBara._fungsi(js, "petaBagian")
        self.assertRegex(
            peta, r"new\s+IntersectionObserver\s*\(\s*tandaiAktif\s*,",
            "observer tidak lagi memanggil aturan yang sama; ia satu-satunya "
            "yang menangkap perubahan tata letak tanpa gulir")

    def test_pemanggil_kedua_penanda_dilepas_lewat_bersihkan(self):
        """Langganan gulir kedua punya SATU pintu keluar, dan itu disengaja.

        Pelepasnya tidak dipegang `layarMateri`: ia digabung ke
        `peta.bersihkan()`, yang sudah dipanggil `saatKeluar`. Pelepas kedua
        yang dipegang terpisah adalah pelepas yang suatu hari terlupa di satu
        cabang keluar, dan pendengar gulir yang tertinggal mengukur artikel
        yang sudah tidak ada — tanpa galat, sekali per frame, selamanya.

        Didaftarkan di dalam `saatSiap`, bukan di badan pembangun: `saatGulir()`
        memanggil fungsinya SEKALI saat pendaftaran, dan panggilan pertama itu
        akan mengukur artikel yang belum terpasang (invarian #15a).

        PREDIKATNYA BENTUK, BUKAN KALIMAT BYTE. Versi pertama menuntut deretan
        karakter `"bersihkan: () => { lepasGulir(); hentikan(); }"` persis; satu
        spasi yang berubah atau satu nama pelepas yang diganti akan menjatuhkan
        pagarnya tanpa ada yang rusak. Sekarang nama pelepasnya DIBACA dari
        kode — yang menerima hasil `saatGulir(` — lalu dituntut dipanggil di
        dalam badan `bersihkan`, apa pun namanya dan apa pun spasinya.

        `bersihkan` diambil dari `return` TERAKHIR di `petaBagian`, dan itu
        bukan kerapian: cabang awal `butir.length < 2` mengembalikan objek
        dengan kunci yang sama persis, jadi pencarian dari depan akan mengukur
        peta KOSONG dan menyatakan lulus tanpa pernah menyentuh yang hidup.

        LAPANGAN BUKTINYA diuji BERPASANGAN, dan pasangan "menyusun ulang"
        di sini bukan formalitas: dua jangkar byte-murni pernah tertinggal di
        tes ini justru sementara docstring-nya sudah mengaku berpredikat
        bentuk, dan keduanya jatuh lewat galat — bukan lewat asersi — sehingga
        tidak terbaca sebagai kegagalan pagar. Terukur pada pohon yang sehat:

          `return {` ditulis `return{`  -> `rindex("return {")` lama mendarat
              di cabang peta KOSONG, badan `bersihkan` terbaca `'() {}'`,
              pagar lama MERAH; predikat regex sekarang membaca
              `': () => { lepasGulir(); hentikan(); }'` dan tetap HIJAU.
          `{` badan `saatSiap` pindah baris -> `index("saatSiap(el, () => {")`
              lama melempar ValueError, pagar lama MERAH; predikat regex
              sekarang menemukannya dan tetap HIJAU.

          MENYALIN, merah  : `bersihkan: hentikan`; `bersihkan: () => {
                             hentikan(); }` (pelepas tidak dipanggil).
          MENYUSUN ULANG, hijau : ganti nama `lepasGulir` jadi apa pun,
                             pecah badan `bersihkan` beberapa baris, pecah
                             langganan jadi tujuh baris.

        Jalur `index()`/`rindex()`/posisi yang gagal dihitung sebagai KEGAGALAN
        PAGAR, bukan galat skrip — karena itu ketiadaannya sekarang dilaporkan
        lewat `self.fail()` dengan bentuk yang diharapkan, bukan dibiarkan
        melempar.

        YANG TIDAK DIJAGA: bahwa pendengarnya benar-benar lepas. Itu jumlah
        listener hidup yang diukur di peramban, dan angkanya ada di laporan hun
        sebelumnya — bukan di tes ini.
        """
        js = self._js()
        peta = TestHamparanBara._fungsi(js, "petaBagian")
        m = re.search(r"(\w+)\s*=\s*saatGulir\s*\(", peta)
        self.assertIsNotNone(
            m, "tidak ada langganan `saatGulir(` di `petaBagian`; pemanggil "
               "kedua penanda hilang")
        pelepas = m.group(1)
        # Argumen `saatGulir(` dipotong dengan hitung kurung, bukan dengan
        # jendela sekian ratus karakter: jendela tetap adalah angka ajaib yang
        # diam-diam salah begitu badannya dipecah jadi beberapa baris.
        buka = m.end() - 1
        dalam, tutup = 0, None
        for j in range(buka, len(peta)):
            if peta[j] == "(":
                dalam += 1
            elif peta[j] == ")":
                dalam -= 1
                if dalam == 0:
                    tutup = j
                    break
        self.assertIsNotNone(tutup, "panggilan `saatGulir(` tidak tertutup")
        langganan = peta[buka + 1:tutup]
        self.assertRegex(
            langganan, r"tandaiAktif\s*\(",
            "langganan gulir kedua tidak lagi memanggil aturan yang sama; "
            f"yang terbaca: {langganan!r}")
        self.assertRegex(
            langganan, r"masihHidup\s*\(",
            "langganan gulir kedua tidak lagi menghormati penjaga keluar "
            f"layarnya; yang terbaca: {langganan!r}")

        # `return` TERAKHIR: cabang peta kosong memakai kunci yang sama persis.
        # Dicari lewat regex ternormalisasi, bukan `rindex("return {")`: spasi
        # di antara `return` dan `{` adalah bentuk murni, dan jangkar byte di
        # sini akan jatuh lewat ValueError — kegagalan yang terbaca sebagai
        # galat skrip, padahal ia kegagalan PAGAR.
        kembali = list(re.finditer(r"\breturn\s*[{(]", peta))
        if not kembali:
            self.fail("tidak ada `return` yang mengembalikan objek di "
                      "`petaBagian`; yang diharapkan sebuah `return { ... }` "
                      "berisi kunci `bersihkan`")
        akhir = kembali[-1].start()
        badan = self._nilai_kunci(peta[akhir:], "bersihkan")
        self.assertRegex(
            badan, rf"\b{re.escape(pelepas)}\s*\(\s*\)",
            f"pelepas langganan gulir (`{pelepas}`) tidak dipanggil di dalam "
            "`bersihkan()`; pendengarnya tertinggal sesudah layar materi "
            f"ditinggalkan. Badan `bersihkan` yang terbaca: {badan!r}")

        layar = TestHamparanBara._fungsi(js, "layarMateri")
        # Dua posisi ini dulu dicari dengan `index()` atas potongan byte, dan
        # keduanya jatuh lewat ValueError begitu `{` pindah baris — bentuk
        # murni yang tidak merusak apa pun. Sekarang keduanya regex
        # ternormalisasi, dan ketiadaannya dilaporkan sebagai kegagalan pagar.
        m_siap = re.search(r"saatSiap\s*\(\s*el\s*,\s*\(\s*\)\s*=>\s*\{", layar)
        if not m_siap:
            self.fail("tidak ada callback `saatSiap(el, () => { ... })` di "
                      "`layarMateri`; di situlah segala pengukuran tata letak "
                      "harus tinggal (invarian #15a)")
        m_ikut = re.search(r"peta\s*\.\s*ikutiGulir\s*\(", layar)
        if not m_ikut:
            self.fail("`layarMateri` tidak lagi mendaftarkan pemanggil kedua "
                      "penanda; yang diharapkan sebuah `peta.ikutiGulir( ... )`")
        i_siap, i_ikut = m_siap.start(), m_ikut.start()
        self.assertLess(
            i_siap, i_ikut,
            "langganan penanda didaftarkan di badan pembangun; panggilan "
            "pertama `saatGulir` akan mengukur artikel yang belum terpasang")
        self.assertRegex(
            layar, r"peta\.ikutiGulir\(\s*\(\s*\)\s*=>\s*!\s*keluarMateri\s*\)",
            "penjaga `keluarMateri` tidak dioper ke langganan penanda")

    def test_lompat_dan_penangan_tombol_tidak_menyetel_kelas(self):
        """Tripwire mesin kedua: yang MEMBACA penanda tidak boleh menulisnya.

        `lompat()` dan `saatTombol()` memindahkan gulir dan fokus; MENULIS
        penanda `.kini` bukan urusan keduanya. Begitu salah satunya menulisnya,
        ada dua mesin yang boleh menjawab "bagian mana yang sedang dibaca", dan
        jawaban yang menang jadi soal urutan waktu — yang tidak ditulis di mana
        pun dan berubah diam-diam.

        Yang dilarang MENULIS, bukan menyentuh. `lompat()` justru WAJIB membaca
        `classList.contains("kini")`: di situlah ia menanyakan jawaban
        `tandaiAktif()` alih-alih menghitungnya sendiri. Predikat versi pertama
        tes ini melarang seluruh kata `classList` dan karena itu menghukum
        pembacaan yang benar — merah pada pohon yang sehat, yang artinya
        predikatnya yang salah, bukan kodenya.
        """
        js = self._js()
        TULIS = ("classList.add", "classList.remove", "classList.toggle",
                 "className =")
        for nama in ("lompat", "saatTombol"):
            badan = TestHamparanBara._fungsi(js, nama)
            for cara in TULIS:
                self.assertNotIn(
                    cara, badan,
                    f"`{nama}` menulis kelas lewat `{cara}`; penanda bagian "
                    "jadi punya mesin kedua, dan yang menang jadi soal urutan "
                    "waktu")
        self.assertIn(
            'classList.contains("kini")', TestHamparanBara._fungsi(js, "lompat"),
            "`lompat` tidak lagi MEMBACA penanda; kalau ia menghitung sendiri "
            "bagian yang sedang dibaca, aturannya punya salinan kedua")

class TestBawaKeTengah(unittest.TestCase):
    """`bawaKeTengah()`: memusatkan butir aktif di WADAHNYA, bukan di dokumen.

    Fungsi ini lahir sebagai pengganti `scrollIntoView({block:"center"})`, dan
    penggantinya bukan soal selera: `scrollIntoView` menggulir SEMUA leluhur
    yang bisa digulir — termasuk dokumen — sehingga membuka materi ke-13 lewat
    navigasi dalam aplikasi mendaratkan pembacanya ratusan piksel di bawah
    judul, di tengah kalimat, pada halaman yang belum pernah ia lihat.

    CAKUPAN YANG DIUKUR: badan `bawaKeTengah` dan badan `kolomMateri` (satu-
    satunya pemanggilnya) di `layar-belajar.js`. Tidak disapukan ke berkas lain
    dan tidak ke `bangunRel` di layar bahasa — rail di sana memang TIDAK boleh
    memakai pemusatan ini, dan pagarnya sendiri sudah berdiri di kelas lain.

    YANG TIDAK DIJAGA, dan jangan dibaca sebaliknya: ini pagar STRUKTUR sumber.
    Bahwa `window.scrollY` benar-benar tidak bergeser, bahwa butirnya benar-
    benar masuk ruang tampil wadahnya, dan bahwa `scrollTop` benar-benar
    bergerak ke arah butir aktif — ketiganya hanya bisa dibuktikan dengan
    `getBoundingClientRect()` di peramban sesudah navigasi DALAM aplikasi, dan
    angkanya ada di tabel render di laporan, bukan di sini.
    """

    @staticmethod
    def _js():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js",
                               "layar-belajar.js"), encoding="utf-8") as f:
            return TestHamparanBara._telanjang(f.read())

    def _fungsi_unik(self, js, nama):
        """Badan satu fungsi, SESUDAH dibuktikan definisinya cuma satu.

        Tanpa pembuktian itu sebuah jangkar bisa diam-diam mendarat di situs
        yang salah dan melapor "merah" padahal matanya yang salah — dan
        kegagalan semacam itu terbaca sebagai pagar yang bekerja.
        """
        n = js.count(f"function {nama}(")
        if n != 1:
            self.fail(f"definisi `function {nama}(` muncul {n} kali, bukan satu; "
                      "jangkar tes ini tidak bisa memilih situs yang dimaksud")
        return TestHamparanBara._fungsi(js, nama)

    # Jalan-jalan yang menggulir SESUATU DI LUAR wadah yang dioper. Semuanya
    # menggeser dokumen atau leluhur lain, dan tidak satu pun menimbulkan galat
    # saat melakukannya.
    DILARANG = ("scrollIntoView", "window.scrollTo", "window.scroll",
                "documentElement.scrollTop", "documentElement.scrollLeft",
                "document.body.scrollTop")

    # `scrollTo(` TIDAK boleh dicari sebagai substring telanjang, dan alasannya
    # sebuah tuduhan yang salah: entri itu ikut menangkap
    # `wadah.scrollTo({ top: wadah.scrollTop + delta })` — yang hanya
    # menggerakkan wadah yang dioper, persis seperti yang seharusnya — lalu
    # mencetak "ia menggulir leluhur di luar wadah yang dioper, dan dokumen
    # ikut bergeser tanpa galat". Pagar yang menuduh hal yang tidak terjadi
    # mengajari pembacanya mengabaikan pesannya.
    #
    # Yang memang harus dilarang panggilan POLOS: di dalam modul ini
    # `scrollTo(` tanpa penerima adalah `window.scrollTo`. Lookbehind menolak
    # penerima apa pun (`\w`, `.`, `$`), jadi yang tersisa cuma bentuk global.
    DILARANG_POLA = (
        (r"(?<![\w.$])scrollTo\s*\(",
         "memanggil `scrollTo(` TANPA penerima; di modul ini itu "
         "`window.scrollTo`, dan yang tergulir dokumen, bukan wadahnya"),
    )

    def test_hanya_menggulir_wadahnya_bukan_dokumen(self):
        """Yang ditulis cuma `wadah.scrollTop` dan `wadah.scrollLeft`.

        Larangannya meliputi PEMANGGILNYA, bukan cuma fungsinya: mengganti
        `bawaKeTengah(daftar, kini)` dengan `daftar.scrollIntoView(...)` di
        `kolomMateri` memulihkan cacat yang sama persis tanpa menyentuh satu
        baris pun di dalam `bawaKeTengah`.

        LAPANGAN BUKTINYA, diuji berpasangan dan diukur:
          MELANGGAR, merah  : `wadah.scrollTop` jadi
              `document.documentElement.scrollTop`; pemanggil kedua diganti
              `daftar.scrollIntoView({block:"nearest", inline:"center"})`.
          MENYUSUN ULANG, hijau : merapikan spasi, menambah komentar,
              mengganti nama variabel lokal `w`/`b`.

        BATAS YANG DIPUTUS SADAR, supaya ia tidak jadi kejutan: daftar di atas
        mengunci BENTUK PROPERTI-DELTA (`wadah.scrollTop += …`). Sebuah
        peralihan ke `wadah.scrollBy({ left: … })` setara secara perilaku dan
        akan tetap MERAH — yang jatuh bukan daftar terlarang ini melainkan
        asersi bentuk/sumbu di dua tes tetangganya, dengan pesan yang benar.
        Siapa pun yang mau berpindah bentuk wajib menulis ulang pagarnya
        BERSAMA suntingannya, bukan menghapus asersinya diam-diam.

        `wadah.scrollTo({ top: wadah.scrollTop + delta })` juga tetap merah,
        tapi lewat jalur yang sama itu — BUKAN lewat daftar terlarang. Versi
        pertama daftar ini memuat substring `"scrollTo("` dan karena itu
        menuduhnya "menggulir leluhur di luar wadah yang dioper", kalimat yang
        salah untuk pemanggilan yang penerimanya justru wadah itu sendiri.
        """
        js = self._js()
        badan = self._fungsi_unik(js, "bawaKeTengah")
        pemanggil = self._fungsi_unik(js, "kolomMateri")
        for nama, teks in (("bawaKeTengah", badan), ("kolomMateri", pemanggil)):
            for jalan in self.DILARANG:
                self.assertNotIn(
                    jalan, teks,
                    f"`{nama}` memakai `{jalan}`; ia menggulir leluhur di luar "
                    "wadah yang dioper, dan dokumen ikut bergeser tanpa galat")
            for pola, sebab in self.DILARANG_POLA:
                self.assertNotRegex(teks, pola, f"`{nama}` {sebab}")
        self.assertRegex(
            badan, r"wadah\s*\.\s*scrollTop",
            "sumbu tegak tidak lagi menulis `wadah.scrollTop`")
        self.assertRegex(
            badan, r"wadah\s*\.\s*scrollLeft",
            "sumbu mendatar tidak lagi menulis `wadah.scrollLeft`")

    def test_gulirnya_delta_bukan_nilai_mutlak(self):
        """Bentuknya DELTA, dan itu yang membedakannya dari cacat aslinya.

        Nilai mutlak mengabaikan posisi wadah itu sendiri di halaman: ia benar
        hanya kalau wadahnya kebetulan mulai di titik nol. Yang terjadi
        sebelumnya persis itu — pendaratan ratusan piksel di bawah judul.

        Bentuk `wadah.scrollTop = wadah.scrollTop + …` ikut diterima: ia delta
        yang ditulis panjang, bukan nilai mutlak, dan menolaknya akan membuat
        pagar ini merah pada penyusunan ulang yang sah.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : `+=` diganti `=` dengan ruas kanan yang sama.
          MENYUSUN ULANG, hijau : ditulis panjang jadi
              `wadah.scrollTop = wadah.scrollTop + (…)`; aritmetikanya
              diekstrak ke `const tengah = (w.height - b.height) / 2`.
        """
        badan = self._fungsi_unik(self._js(), "bawaKeTengah")
        for sumbu in ("scrollTop", "scrollLeft"):
            self.assertRegex(
                badan,
                rf"wadah\s*\.\s*{sumbu}\s*(?:\+=|=\s*wadah\s*\.\s*{sumbu}\s*\+)",
                f"`wadah.{sumbu}` disetel ke nilai MUTLAK, bukan digeser. "
                "Nilai mutlak mengabaikan posisi wadahnya sendiri di halaman, "
                "dan itu cacat yang fungsi ini dibuat untuk membunuhnya")

    def test_kedua_sumbu_tetap_ada_dan_dipanggil_untuk_dua_wadah(self):
        """Dua arah, karena jalurnya memang berganti arah.

        Kolom tegak yang menggulir ke bawah di layar lebar, satu jalur yang
        menggulir ke samping di layar sempit. Menghapus salah satu cabang
        membuat salah satu dari keduanya berhenti mengikuti — tanpa galat, dan
        cuma di satu rentang lebar, jadi ia lolos dari mata yang menguji di
        satu ukuran saja.

        Pemanggilnya juga dijaga: `kolomMateri` memanggilnya DUA kali, sekali
        untuk `el` (kotak tegak) dan sekali untuk `daftar` (jalur mendatar).

        Yang dihitung SITUS PENULISAN (`scrollTop +=` / `scrollTop =`), bukan
        penyebutan namanya. Versi pertama menghitung penyebutan, dan itu
        bertabrakan dengan tes delta di atas yang sengaja menerima bentuk
        panjang `wadah.scrollTop = wadah.scrollTop + (…)` — bentuk itu
        menyebut namanya dua kali padahal menulis sekali. Yang menemukannya
        bukan penalaran melainkan kontrol negatifnya sendiri: deformasi D6
        merah padahal harus hijau, dan yang salah predikatnya.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : cabang `scrollWidth` dihapus; salah satu
              pemanggil diganti `scrollIntoView`.
          MENYUSUN ULANG, hijau : angka ambang 4 diganti 8; spasi dirapikan;
              delta ditulis panjang `= wadah.scrollTop + (…)`.
        """
        js = self._js()
        badan = self._fungsi_unik(js, "bawaKeTengah")
        for sumbu in ("scrollTop", "scrollLeft"):
            self.assertEqual(
                len(re.findall(rf"wadah\s*\.\s*{sumbu}\s*(?:\+=|=(?!=))",
                               badan)), 1,
                f"situs penulisan `wadah.{sumbu}` bukan tepat satu; salah satu "
                "sumbu hilang atau digandakan, dan jalur materi berhenti "
                "mengikuti di salah satu rentang lebar tanpa galat apa pun")

        pemanggil = self._fungsi_unik(js, "kolomMateri")
        panggil = re.findall(r"bawaKeTengah\s*\(\s*(\w+)\s*,", pemanggil)
        self.assertEqual(
            sorted(panggil), ["daftar", "el"],
            "`kolomMateri` tidak lagi memusatkan kedua wadahnya; yang "
            f"terbaca: {panggil}")

    def test_pemanggil_tidak_menyimpan_definisi_kedua(self):
        """Yang memusatkan cuma `bawaKeTengah`; pemanggilnya tidak ikut.

        Lubang yang ditutup di sini halus dan itu yang membuatnya berbahaya:
        SELURUH pagar lain di kelas ini tetap hijau selama kedua panggilan
        `bawaKeTengah(...)` masih berdiri di tempatnya — jadi sebuah salinan
        aturannya yang disisipkan DI ANTARA kedua panggilan itu lolos tanpa
        satu pun asersi berkedip. Terukur: menyisipkan lima baris
        `el.scrollTop += (kb.top - kw.top) - (kw.height - kb.height) / 2`
        beserta dua `getBoundingClientRect()`-nya di badan `kolomMateri`
        membuat suite tetap hijau di 839.

        Kenapa itu cacat dan bukan sekadar berlebihan: dua mesin yang sama-sama
        boleh memusatkan satu butir akan berbeda suatu hari — dan yang menang
        jadi soal urutan baris, yang tidak ditulis di mana pun. `bawaKeTengah`
        ada justru untuk jadi SATU-SATUNYA jawaban atas "bagaimana memusatkan
        butir aktif di wadahnya"; salinan di pemanggil adalah definisi kedua,
        dan repo ini melarang definisi kedua secara umum, bukan cuma untuk
        "lulus"/"terkunci"/aturan bab.

        TES TERSENDIRI, bukan asersi tambahan di tes tetangganya, dan itu
        pilihan sadar: tetangganya menamai kelas cacat "menggulir sesuatu di
        luar wadah yang dioper", sedangkan yang ini "pemanggil menyimpan
        salinan aturannya". Digabung, satu pesan gagal akan menyebut kelas yang
        salah untuk separuh mutasinya.

        LAPANGAN BUKTI — tujuh belas keadaan, semuanya diukur, bukan dikira.
        Angkanya `tulisan-gulir/rect` di badan `kolomMateri`:

            bersih                          0/0   HIJAU
            D1 rapikan-spasi                0/0   HIJAU
            D2 sisip-komentar               0/0   HIJAU
            D3 aritmetika-diekstrak-ke-const 0/0  HIJAU
            D4 ambang 4->8                  0/0   HIJAU
            D5 w/b di-rename                0/0   HIJAU
            D6 delta-ditulis-panjang        0/0   HIJAU
            V1 `+=` jadi `=`                0/0   HIJAU di sini (merah di tes delta)
            V2 documentElement.scrollTop    0/0   HIJAU di sini (merah di tes dokumen)
            V4 hapus cabang scrollWidth     0/0   HIJAU di sini (merah di tes dua-sumbu)
            V5 hapus guard                  0/0   HIJAU di sini (merah di tes penjaga)
            V6 guard turun                  0/0   HIJAU di sini (merah di tes penjaga)
            V7 ambang window.innerHeight    0/0   HIJAU di sini (merah di tes ambang)
            A3 wadah.scrollTo({top: delta}) 0/0   HIJAU di sini (merah di tes bentuk/sumbu)
            V3 pemanggil -> scrollIntoView  1/0   MERAH
            A2 nilai mutlak di pemanggil    1/1   MERAH
            A1 salinan aturan di pemanggil  1/2   MERAH

        Tujuh baris pertama membuktikan pagar ini tidak menyentuh penyusunan
        ulang yang sah; enam baris tengah membuktikan ia tidak ikut-ikutan
        menuduh pelanggaran yang bukan urusannya (masing-masing sudah punya
        pagarnya sendiri); tiga baris terakhir membuktikan ia punya gigi.

        YANG TIDAK DIJAGA: pemanggil yang menulis gulir lewat nama properti
        terhitung (`el["scroll" + "Top"] = …`) atau lewat fungsi pembantu di
        berkas lain. Keduanya salinan yang masih lolos.
        """
        js = self._js()
        teks = self._fungsi_unik(js, "kolomMateri")
        SEBAB = ("yang memusatkan cuma `bawaKeTengah`; pemanggilnya tidak "
                 "menulis gulir dan tidak membaca kotak apa pun")
        tulis = re.findall(
            r"scroll(?:Top|Left|IntoView|By|To)\s*(?:\+=|-=|=[^=]|\()", teks)
        self.assertEqual(
            len(tulis), 0,
            f"{SEBAB}. Tulisan gulir yang terbaca di `kolomMateri`: {tulis}")
        rect = re.findall(r"getBoundingClientRect", teks)
        self.assertEqual(
            len(rect), 0,
            f"{SEBAB}. `getBoundingClientRect` terbaca {len(rect)} kali di "
            "`kolomMateri`; membaca kotak di sana hanya berguna kalau ada yang "
            "hendak dihitung sendiri, dan itu definisi kedua")

    def test_penjaga_null_tetap_pernyataan_pertama(self):
        """Penjaganya pernyataan PERTAMA, dan posisinya bagian dari aturannya.

        Kedua pemanggil mengoper `kini` yang boleh `null` (`daftar
        .querySelector("a.kini")` pada materi yang tidak ada di jalur itu).
        Penjaga yang berdiri SESUDAH `getBoundingClientRect()` tidak menjaga
        apa pun: pembacaannya sudah melempar lebih dulu.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : penjaganya dihapus; penjaganya dipindah ke bawah
              dua pembacaan rect.
          MENYUSUN ULANG, hijau : spasi di dalamnya dirapikan; sebuah komentar
              disisipkan di atasnya.
        """
        badan = self._fungsi_unik(self._js(), "bawaKeTengah")
        # Kurung badan dicari lewat `)` penutup daftar parameter, bukan lewat
        # `{` pertama: daftar parameter yang didekonstruksi membawa `{` sendiri,
        # dan irisan itu sudah pernah salah sekali di paket ini.
        m = re.search(r"\)\s*\{", badan)
        if not m:
            self.fail("badan `bawaKeTengah` tidak ditemukan; yang diharapkan "
                      "`function bawaKeTengah(...) { ... }`")
        isi = badan[m.end():].lstrip()
        self.assertRegex(
            isi, r"^if\s*\(\s*!\s*wadah\s*\|\|\s*!\s*butir\s*\)\s*return\s*;",
            "penjaga `if (!wadah || !butir) return;` bukan lagi pernyataan "
            "pertama; penjaga yang berdiri sesudah pembacaan rect tidak "
            f"menjaga apa pun. Yang terbaca di awal badan: {isi[:70]!r}")

    def test_ambang_kemacetan_membaca_wadah_bukan_jendela(self):
        """Yang ditanya "wadah ini macet atau tidak", bukan "layarnya seberapa".

        `scrollHeight > clientHeight + N` adalah pertanyaan tentang WADAH:
        apakah isinya lebih panjang daripada ruang tampilnya. Menggantinya
        dengan ukuran jendela membuat jawabannya benar hanya kalau wadahnya
        kebetulan sebesar layar — dan di layar sempit jalur materi justru jauh
        lebih pendek daripada jendelanya.

        `N` sengaja tidak dikunci nilainya: ia toleransi pembulatan sub-piksel,
        dan 4 atau 8 sama-sama sah. Yang dikunci BENTUK pertanyaannya.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : ambangnya membaca `window.innerHeight`.
          MENYUSUN ULANG, hijau : angka 4 diganti 8; nama variabel lokal
              diganti; spasi dirapikan.
        """
        badan = self._fungsi_unik(self._js(), "bawaKeTengah")
        self.assertRegex(
            badan,
            r"wadah\s*\.\s*scrollHeight\s*>\s*wadah\s*\.\s*clientHeight\s*\+\s*\d+",
            "ambang kemacetan tegak tidak lagi membandingkan wadah dengan "
            "dirinya sendiri")
        self.assertRegex(
            badan,
            r"wadah\s*\.\s*scrollWidth\s*>\s*wadah\s*\.\s*clientWidth\s*\+\s*\d+",
            "ambang kemacetan mendatar tidak lagi membandingkan wadah dengan "
            "dirinya sendiri")
        for jendela in ("window.innerHeight", "window.innerWidth",
                        "documentElement.clientHeight",
                        "documentElement.clientWidth"):
            self.assertNotIn(
                jendela, badan,
                f"ambang kemacetan membaca `{jendela}`; ukuran jendela bukan "
                "jawaban atas pertanyaan apakah WADAH ini macet")


class TestLompatKeIsi(unittest.TestCase):
    """Tautan "Lompat ke isi" harus benar-benar bisa dicapai Tab.

    Cacatnya halus dan permukaannya lengkap, dan itu yang membuatnya bertahan
    lama: tombolnya ADA (`index.html:24`), bergaya, dan butir fokus PERTAMA
    dokumen. Yang tidak ada cuma kemungkinan mencapainya — `gambarRute()`
    memanggil `panggung.focus()` di SETIAP render yang berhasil, termasuk
    render boot, dan Chrome memulai navigasi fokus berurutan dari elemen
    TERAKHIR yang difokuskan, bukan dari kepala dokumen. Tab pertama sesudah
    memuat karena itu berangkat dari tengah dokumen: terukur 32 tekan untuk
    sampai ke tautan lompat di `#/atur`. Jumlah ini bergantung konfigurasi
    (saklar "buka semua bab", dan lebar rail pada 1100 px yang menyembunyikan
    sebagian tautan); yang TIDAK bergantung apa pun ialah angka SESUDAH:
    1 tekan, di semua rute.

    Dua nama rute yang dipakai versi pertama catatan ini SALAH dan angkanya
    ikut salah: `#/pengaturan` bukan rute — `LAYAR` menyimpan `atur`, dan
    `uraikanRute` menjatuhkan nama tak dikenal ke `dasbor` (`document.title`
    keluar "Dasbor · Belajar Ngoding"), jadi baris itu mengukur dasbor dua
    kali; dan `#/bahasa` tanpa kunci masuk cabang GALAT, bukan layar bahasa.
    Yang sah: `#/atur` dan `#/bahasa/javascript`.

    KELAS TERSENDIRI, bukan asersi tambahan di kelas yang sudah ada, dan itu
    pilihan sadar: kelas cacatnya "titik mula navigasi fokus", bukan "mesin
    gerak" maupun "bentuk pemulihan gulir". Digabung, satu pesan gagal akan
    menyebut aturan yang salah.

    YANG TIDAK DIJAGA: ini pagar STRUKTUR sumber. Bahwa Tab#1 benar-benar
    mendarat di `#lompat-isi`, bahwa `:focus-visible`-nya menyala, dan bahwa
    `scrollY` tidak bergerak saat Enter ditekan — ketiganya hanya bisa
    dibuktikan dengan mengukur di peramban, dan angkanya ada di tabel render
    di laporan, bukan di sini.
    """

    @staticmethod
    def _js(nama="aplikasi.js"):
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js", nama),
                  encoding="utf-8") as f:
            return TestHamparanBara._telanjang(f.read())

    def _fungsi_unik(self, js, nama):
        n = js.count(f"function {nama}(")
        if n != 1:
            self.fail(f"definisi `function {nama}(` muncul {n} kali, bukan satu; "
                      "jangkar tes ini tidak bisa memilih situs yang dimaksud")
        return TestHamparanBara._fungsi(js, nama)

    def _penangan(self, js, pemicu):
        """Argumen kedua `addEventListener` pada sebuah pemicu, hitung kurung.

        Irisan sampai baris berikutnya tidak cukup: badan penangan ini
        berbilang baris, dan `{ block: "start" }` di dalamnya membawa kurung
        sendiri.
        """
        m = re.search(rf'\$\(\s*["\']{re.escape(pemicu)}["\']\s*\)\s*\.\s*'
                      r'addEventListener\s*\(', js)
        if not m:
            self.fail(f"tidak ada `$(\"{pemicu}\").addEventListener(` di berkas "
                      "ini; yang diharapkan pemasangan penangan klik")
        buka = m.end() - 1
        dalam = 0
        for j in range(buka, len(js)):
            if js[j] == "(":
                dalam += 1
            elif js[j] == ")":
                dalam -= 1
                if dalam == 0:
                    return js[buka + 1:j]
        self.fail(f"pemanggilan addEventListener untuk `{pemicu}` tidak tertutup")

    def test_render_boot_tidak_memindahkan_fokus_tapi_navigasi_tetap(self):
        """Gerbangnya PARAMETER, bukan penghapusan panggilannya.

        `panggung.focus()` yang dihapus akan "memperbaiki" Tab dan sekaligus
        membunuh pengumuman pembaca layar: layar berganti tanpa ada yang
        memberi tahu. Yang benar cuma render BOOT yang tidak memindahkannya,
        dan setiap navigasi sesudahnya tetap memindahkan.

        KENAPA ASERSI CACAH DI SINI DIGANTI, dan ini aturan paket bukan selera:
        versi pertama mengunci `panggung.focus(` pada `== 1`. Yang ingin dijaga
        sebenarnya "fokusnya tidak boleh dihapus" — dan `== 1` bukan itu, ia
        keadaan hari ini yang kebetulan bernilai satu. Akibatnya terukur: saat
        gerbang yang sama dipasang di CABANG GALAT (Cacat I, perbaikan yang
        benar), cacahnya jadi 2 dan pagar ini MERAH dengan pesan "bukan lagi
        tepat satu" — ia menolak perbaikan yang benar. Jangan mengunci sebuah
        cacah kecuali cacah itu memang batasnya.

        Gantinya TIGA predikat yang batasnya benar:
          (a) SETIAP `panggung.focus(` berdiri di bawah gerbang yang menyebut
              `pindahFokus` — berapa pun situsnya;
          (b) TIDAK ADA `.focus(` lain di badan `gambarRute` selain
              `panggung.focus(` — itu yang menutup "cara kedua" memindahkan
              fokus, bukan sekadar mengganti nama;
          (c) KEDUA JALUR render — `if (galat) { … } else { … }` — sampai ke
              sebuah `panggung.focus(` yang bergerbang: di bloknya sendiri
              ATAU di ekor bersama sesudah rantai itu ditutup, asal jalur itu
              tidak `return` lebih dulu.

        (c) bukan tambahan hiasan, dan ia lahir dari pengukuran: dengan (a)+(b)
        saja, menghapus panggilan fokus dari SATU cabang tetap HIJAU, karena
        cabang yang tersisa masih memenuhi keduanya. Terukur: hapus di cabang
        sukses -> hijau; hapus di cabang galat -> hijau; hapus keduanya baru
        merah. Yang ingin dijaga "setiap jalur render mengumumkan layarnya",
        dan itu klaim PER JALUR — bukan cacah, dan bukan keberadaan di satu
        tempat mana pun.

        `return` yang dijaga adalah `return` MILIK jalur itu sendiri, diukur
        lewat `TestHamparanBara._kedalaman()` — kedalaman kurungnya DIHITUNG,
        tidak pernah ditulis sebagai angka. Sebuah `return` di dalam callback
        (`pinta(() => { if (ada) return; })`) berdiri lebih dalam, bukan
        kepunyaan jalur itu, dan tidak menghentikan apa pun. Terukur: callback
        semacam itu di ekor bersama, di blok galat, dan di blok sukses semuanya
        HIJAU, sementara `return;` sungguhan pada kedalaman blok itu sendiri
        MERAH dengan nama cabang yang benar — `['galat']`, `['sukses']`, atau
        keduanya. Dan karena kedalamannya dihitung, membungkus seluruh rantai
        `if/else` dalam `try/catch` tetap HIJAU — terukur, blok cabang di sana
        duduk di kedalaman 3, sedangkan di pohon biasa 2. Angka mana pun dari
        keduanya kalau dituliskan sebagai konstanta akan salah pada salah satu
        bentuk itu.

        EXIT DIUKUR DENGAN DUA SYARAT, dan keduanya perlu. Sebuah `return`
        boleh MILIK jalur itu dan tetap tidak MENGHENTIKANNYA: `if (sudah)
        return;` berdiri pada kedalaman yang sama tapi hanya kadang-kadang
        berjalan. Karena itu token exit dihitung hanya kalau (i) kedalamannya
        milik region yang sedang diukur, dan (ii) ia bukan konsekuensi sebuah
        syarat (`if`/`for`/`while`, dan bentuk `else`-nya). Terukur: `if
        (sudah) return;` dan `if (sudah) lewati(); else return;` di ekor
        bersama, keduanya sebelum satu-satunya gerbang, HIJAU.

        C1 TETAP MERAH SESUDAH PELONGGARAN ITU, dan kalimat ini wajib ada:
        sebuah `return;` TANPA SYARAT di tempat yang sama tetap memotong ekor
        dan membuat kedua jalur bolong (`['galat', 'sukses']`). "K2 hijau"
        bukan "penjaga exit sudah longgar" — yang dibuang cuma exit yang
        bersyarat.

        Hitungan blok DIPOTONG PADA EXIT-NYA SENDIRI, simetris dengan ekor.
        Tanpa itu, sebuah `return;` di awal blok galat sementara gerbangnya
        masih tertulis di bawahnya akan dihitung "mengumumkan" padahal gerbang
        itu tidak pernah dieksekusi — terukur MERAH `['galat']` sekarang,
        HIJAU sebelum perbaikan ini.

        `throw` ikut dihitung sebagai exit karena jalur yang melempar juga
        tidak sampai ke ekor: `throw salah;` sebagai statement pertama blok
        galat MERAH `['galat']`.

        Kedalaman sendirian tidak memisahkan region BERSAUDARA, dan itu
        ditemukan oleh kontrol negatifnya sendiri: isi `catch { throw e; }`
        duduk di kedalaman yang sama persis dengan ekor yang berdiri di dalam
        `try`-nya. Karena itu pencarian exit dibatasi pada region yang sama —
        berhenti begitu kedalamannya turun di bawah kedalaman awal. Tanpa
        batas itu, membungkus rantai `if/else` dalam `try/catch` menuduh kedua
        jalur bolong pada pohon yang sehat.

        Versi pertama (c) MENGHITUNG PER BLOK, dan itu mengadili hal yang salah
        sambil mengaku mengadili jalur. Terukur: menggabungkan dua baris
        identik jadi SATU di ekor bersama (sesudah rantai if/else ditutup,
        sebelum `segarkanUkuran()`) membuatnya merah — padahal kedua jalur
        tetap jatuh ke sana dan `preventScroll: true` membuat urutannya
        terhadap `window.scrollTo` tidak mengubah gulir apa pun. Hitungan
        sekarang: blok sendiri + ekor bersama, dengan `return` dijaga per
        jalur.

        POPULASI DI POHON BERSIH, diukur bukan dikira: `.focus(` di badan
        `gambarRute` = 1 (semuanya `panggung.focus(`), `.focus(` lain = 0,
        situs di luar gerbang = 0. Jadi (b) berpositif-palsu nol saat ditulis.

        LAPANGAN BUKTINYA, diukur berpasangan:
          MELANGGAR, merah  : `panggung.focus(...)` dihapus dari cabang
              sukses SAJA (ditangkap (c)); dihapus dari cabang galat saja
              (ditangkap (c)); dihapus seluruhnya (ditangkap (a));
              `hasil.el.focus({ preventScroll: true })` disisipkan di cabang
              sukses (cara kedua — ditangkap (b), bukan (a)).
          MENYUSUN ULANG, hijau : gerbangnya ditulis blok
              `if (pindahFokus) { ... }` di SATU atau DUA cabang sekaligus;
              spasi di dalamnya dirapikan.

        YANG TIDAK DIJAGA, dan SETIAP BARIS DI SINI SUDAH DIUKUR MERAH — bukan
        dugaan. Aturannya: sebuah pagar struktur yang akan merah pada sebuah
        refactor WAJIB mengatakannya lebih dulu; yang terlarang bukan merahnya,
        melainkan merah tanpa penjelasan, yang membuat orang mengira
        perilakunya yang rusak.

          · `if (!pindahFokus) return;` — bentuk kebalikan yang sama sahnya,
            tidak cocok dengan pola gerbang di bawah.
          · X1, `panggung.focus(` diekstrak ke fungsi pembantu
            (`umumkan(panggung, pindahFokus)`) -> MERAH lewat (a),
            `0 not greater than or equal to 1`, dengan pesan "pembaca layar
            berhenti diberi tahu" PADAHAL TIDAK berhenti. Pesan itu salah untuk
            kasus ini, dan itulah sebabnya ia didaftarkan di sini: pagarnya
            ditulis ulang BERSAMA suntingannya, bukan sesudah orang bingung.
          · D2, `if ((pindahFokus))` -> MERAH lewat (a), daftar situs di luar
            gerbang `[75]`. Perilaku identik; yang berbeda cuma ejaan.
          · D3, `if (pindahFokus === true)` -> MERAH lewat (a), daftar situs di
            luar gerbang `[75]`. Perilaku identik; yang berbeda cuma ejaan.
          · E1, `if (galat) { … return; }` tanpa `else` -> MERAH lewat
            `self.fail("cabang `else { … }` tidak menyusul `if (galat)`; pagar
            ini tidak bisa memilih jalur yang dimaksud")`. Pesan itu JUJUR — ia
            mengaku tidak bisa mengukur, bukan menuduh kodenya rusak — jadi ini
            batas yang diumumkan, bukan tuduhan palsu.

        Setiap pelonggaran pola gerbang untuk menampung D2/D3 adalah lubang
        baru: `if (pindahFokus === false)` dan `if ((!pindahFokus))` akan ikut
        lolos. Polanya sengaja dibiarkan sempit.
        """
        js = self._js()
        badan = self._fungsi_unik(js, "gambarRute")
        situs = [m.start() for m in re.finditer(r"panggung\.focus\s*\(", badan)]
        self.assertGreaterEqual(
            len(situs), 1,
            "`panggung.focus(` hilang dari `gambarRute`; tanpa itu pembaca "
            "layar berhenti diberi tahu bahwa layarnya berganti — 'perbaikan' "
            "yang menukar satu cacat dengan cacat lain yang lebih sunyi")
        diluar = []
        for i in situs:
            gerbang = None
            for g in re.finditer(r"if\s*\(\s*pindahFokus\s*\)", badan[:i]):
                gerbang = g
            # Antara gerbang dan panggilannya hanya boleh ada spasi dan paling
            # banyak satu `{` — itu yang membedakan "dipagari" dari "kebetulan
            # ada gerbang di suatu tempat di atasnya".
            antara = badan[gerbang.end():i] if gerbang else None
            if antara is None or not re.fullmatch(r"\s*\{?\s*", antara):
                diluar.append(badan[:i].count("\n") + 1)
        self.assertEqual(
            diluar, [],
            "ada `panggung.focus(` yang TIDAK berdiri di bawah gerbang "
            f"`pindahFokus` (baris relatif di badan `gambarRute`: {diluar}); "
            "render boot akan memindahkan titik mula navigasi fokus lagi dan "
            "tautan lompat kembali tak terjangkau")
        lain = re.findall(r"(?<!panggung)\.focus\s*\(", badan)
        self.assertEqual(
            len(lain), 0,
            f"ada {len(lain)} panggilan `.focus(` selain `panggung.focus(` di "
            "`gambarRute`; fokus dipindahkan lewat jalan kedua yang tidak "
            "melewati gerbang `pindahFokus`")

        # (c) PER JALUR, bukan per blok. Kedua blok dipotong dengan hitung
        # kurung, bukan dengan irisan sampai `} else {`: badan keduanya memuat
        # objek berkurung.
        #
        # Bedanya nyata dan terukur: versi pertama menuntut panggilannya ada DI
        # DALAM tiap blok, jadi ia MERAH pada penggabungan dua baris identik
        # jadi satu di ekor bersama — refactor yang justru diminta gaya repo
        # ini, dan yang tidak mengubah perilaku sedikit pun karena kedua jalur
        # tetap jatuh ke sana. Menuntut "di dalam blok" berarti mengadili
        # BENTUK dan menyebutnya JALUR; itu bentuk paling halus dari status quo
        # yang menyamar sebagai aturan, penyakit yang baru saja dibuang dari
        # asersi `== 1`.
        GERB = r"if\s*\(\s*pindahFokus\s*\)\s*\{?\s*panggung\.focus\s*\("
        # Kepemilikan dihitung, tidak ditulis. `peta[i]` = kedalaman kurung di
        # indeks `i` relatif badan fungsi — dan angkanya TIDAK pernah dibaca
        # sebagai konstanta: begitu seseorang membungkus rantai if/else dalam
        # `try`, kedalaman blok cabang naik, dan pagar yang menuliskan `== 1`
        # akan salah tanpa satu pun galat.
        peta = dict(TestHamparanBara._kedalaman(badan))

        # Sebuah jalur berhenti hanya kalau ia dilempar keluar TANPA SYARAT.
        # `throw` ikut karena jalur yang melempar juga tidak sampai ke ekor.
        BATAL = r"\b(?:return|throw)\b"

        def blok(teks, mulai):
            dalam = 0
            for j in range(mulai, len(teks)):
                if teks[j] == "{":
                    dalam += 1
                elif teks[j] == "}":
                    dalam -= 1
                    if dalam == 0:
                        return teks[mulai + 1:j], j
            return None, None

        def bersyarat(i):
            """Token di indeks `i` itu konsekuensi sebuah syarat?

            `if (sudah) return;` MILIK jalur itu dan berada di kedalaman yang
            sama, tapi ia tidak menghentikan jalurnya — hanya kadang-kadang.
            Kedalaman saja karena itu tidak cukup; bentuk `else` dari penyakit
            yang sama (`… else return;`) ikut ditangani di sini.
            """
            kiri = badan[:i].rstrip()
            if kiri.endswith("else"):
                return True
            if not kiri.endswith(")"):
                return False
            dala = 0
            for j in range(len(kiri) - 1, -1, -1):
                if kiri[j] == ")":
                    dala += 1
                elif kiri[j] == "(":
                    dala -= 1
                    if dala == 0:
                        return bool(re.search(r"\b(if|for|while)$",
                                              kiri[:j].rstrip()))
            return False

        def batas(awal, akhir, d):
            """Indeks tempat region MENINGGALKAN kedalaman `d` (atau `akhir`).

            Kedalaman sendirian tidak memisahkan region BERSAUDARA: isi sebuah
            `catch { … }` duduk di kedalaman yang sama persis dengan ekor yang
            berdiri di dalam `try`-nya, padahal ia blok lain dan tidak pernah
            dilalui jalur lurus yang sedang diukur. Terukur: tanpa batas ini,
            `} catch (e) { throw e; }` memotong ekor sebelum gerbangnya dan
            kedua jalur tertuduh bolong pada pohon yang sehat.
            """
            for j in range(awal, akhir):
                if peta[j] < d:
                    return j
            return akhir

        def keluar(awal, akhir, d):
            """Indeks exit TANPA SYARAT pertama milik kedalaman `d`, atau None.

            Tiga hal harus benar, dan ketiganya perlu: token itu masih di dalam
            region yang sama (belum melewati `batas`), kedalamannya milik
            region itu (`peta[i] == d`), DAN ia bukan konsekuensi sebuah
            syarat. Satu pembantu dipakai oleh pemotong ekor DAN penjaga per
            jalur, supaya keduanya tidak pernah bisa berbeda pendapat.
            """
            henti = batas(awal, akhir, d)
            for cm in re.finditer(BATAL, badan[awal:henti]):
                i = awal + cm.start()
                if peta[i] == d and not bersyarat(i):
                    return i
            return None

        m = re.search(r"if\s*\(\s*galat\s*\)\s*\{", badan)
        if not m:
            self.fail("cabang `if (galat) { … }` tidak ditemukan di "
                      "`gambarRute`; pagar ini tidak bisa memilih jalur yang "
                      "dimaksud")
        mulai_galat = m.end() - 1
        isi_galat, tutup1 = blok(badan, mulai_galat)
        m2 = re.match(r"\s*else\s*\{", badan[tutup1 + 1:]) if tutup1 else None
        if not m2:
            self.fail("cabang `else { … }` tidak menyusul `if (galat)`; "
                      "pagar ini tidak bisa memilih jalur yang dimaksud")
        mulai_sukses = tutup1 + 1 + m2.end() - 1
        isi_sukses, tutup2 = blok(badan, mulai_sukses)
        for nama, isi in (("galat", isi_galat), ("sukses", isi_sukses)):
            self.assertIsNotNone(
                isi, f"cabang `{nama}` tidak tertutup kurungnya")

        # EKOR BERSAMA: apa pun sesudah rantai if/else ditutup, dipotong pada
        # exit pertamanya SENDIRI. Memotong pada `return` pertama apa pun tidak
        # cukup: sebuah callback ber-`return`, dan sebuah `if (sudah) return;`,
        # keduanya tidak menghentikan siapa pun — memotong di situ membuang
        # sisa ekor yang sebenarnya masih dilalui kedua jalur.
        d_ekor = peta[tutup2 + 1]
        potong = keluar(tutup2 + 1, len(badan), d_ekor)
        ekor = badan[tutup2 + 1:] if potong is None else badan[tutup2 + 1:potong]
        n_ekor = len(re.findall(GERB, ekor))

        # PER JALUR, dan SIMETRIS dengan ekor: kalau ekor dipotong pada exit
        # pertamanya yang sah, isi blok juga. Tanpa itu, sebuah `return;` tanpa
        # syarat di awal blok yang gerbangnya masih tertulis di bawahnya akan
        # dihitung "mengumumkan" padahal gerbang itu tidak pernah dieksekusi.
        jalur = {}
        untuk = (("galat", (isi_galat, mulai_galat, tutup1)),
                 ("sukses", (isi_sukses, mulai_sukses, tutup2)))
        for nama, (isi, buka, tutup) in untuk:
            exit_blok = keluar(buka + 1, tutup, peta[buka])
            hidup = isi if exit_blok is None else isi[:exit_blok - buka - 1]
            lewat = 0 if exit_blok is not None else n_ekor
            jalur[nama] = len(re.findall(GERB, hidup)) + lewat
        bolong = sorted(n for n, v in jalur.items() if v < 1)
        self.assertEqual(
            bolong, [],
            f"jalur render {bolong} tidak sampai ke satu pun `panggung.focus(` "
            "yang bergerbang — baik di bloknya sendiri maupun di ekor bersama. "
            f"Jalur itu memasang layar tanpa mengumumkannya (hitungan: {jalur}); "
            "di cabang galat justru itulah saat orangnya paling perlu tahu apa "
            "yang terjadi")
        self.assertNotIn(
            "!pindahFokus", badan,
            "gerbangnya dibalik; artinya justru navigasi yang berhenti "
            "mengumumkan layar baru")

    def test_hanya_boot_yang_mengoper_pindahFokus_false(self):
        """Satu pemanggil mengoper `false`; sisanya memakai default `true`.

        Tiga pemanggil `gambarRute` hidup di berkas ini: render boot di
        `mulai()`, pendengar `hashchange`, dan tombol "Coba lagi" di layar
        gagal. Dua yang terakhir navigasi, jadi keduanya HARUS memindahkan
        fokus — dan keduanya memang tidak mengoper apa-apa.

        `hashchange` mengoper sebuah Event, bukan objek pilihan. Event tidak
        punya properti `pindahFokus`, jadi destrukturisasi di kepala fungsi
        membacanya `undefined` dan nilai default `true` yang berlaku. Itu
        perilaku, bukan ejaan — dan yang membuktikannya baris RUTE#2 di tabel
        render laporan (`activeElement` sesudah navigasi kedua = `layar`),
        bukan pagar string ini.

        LINGKUP KLAIMNYA DIPERLUAS KE SELURUH BERKAS, dan itu koreksi atas
        versi pertama: hitungan lamanya hanya membaca badan `mulai()`, jadi
        kalimat "sisanya memakai default `true`" lebih luas daripada yang
        benar-benar diadu — sebuah `gambarRute({ pindahFokus: false })` yang
        dipasang di tombol "Coba lagi" akan lolos sepenuhnya. Asersi ketiga di
        bawah menutup itu: `pindahFokus: false` muncul TEPAT SATU kali di
        seluruh `aplikasi.js`. Populasi hari ini: 1 (hanya di render boot),
        jadi nol positif-palsu.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : boot kembali ke `gambarRute()` polos; default di
              kepala fungsi dibalik jadi `= false`; `pindahFokus: false`
              dipasang juga di tombol "Coba lagi".
          MENYUSUN ULANG, hijau : spasi di dalam objek pilihannya dirapikan.

        TIGA MERAH YANG SENGAJA, dan bukan regresi — dicatat supaya pembaca
        laporan berikutnya tidak memanggilnya bug:
          · parameternya di-rename di tiga tempat sekaligus -> MERAH di dua
            tes. Nama `pindahFokus` memang bagian dari kontrak yang dijaga;
            menggantinya menuntut pagarnya ditulis ulang bersamanya.
          · gerbang dipindah ke baris `window.scrollTo` -> MERAH, dan pesannya
            benar: yang dipagari harus panggilan fokusnya, bukan gulirnya.
          · pemanggil `pindahFokus: false` dipindah keluar `mulai()` -> MERAH.
            Yang boot harus tetap yang boot; memindahkannya ke tempat lain
            berarti render pertama kembali memindahkan fokus.
        """
        js = self._js()
        self.assertEqual(
            len(re.findall(r"pindahFokus\s*:\s*false", js)), 1,
            "`pindahFokus: false` muncul selain tepat sekali di `aplikasi.js`; "
            "hanya render boot yang boleh menolak pindah fokus — setiap "
            "navigasi lain wajib mengumumkan layarnya")
        self.assertRegex(
            js,
            r"async\s+function\s+gambarRute\s*\(\s*\{\s*pindahFokus\s*=\s*true\s*\}"
            r"\s*=\s*\{\s*\}\s*\)",
            "kepala `gambarRute` tidak lagi mendeklarasi default `true`; "
            "`hashchange` dan tombol 'Coba lagi' akan berhenti memindahkan "
            "fokus, dan layar berganti tanpa diumumkan")
        badan = self._fungsi_unik(js, "mulai")
        boot = re.findall(
            r"gambarRute\s*\(\s*\{\s*pindahFokus\s*:\s*false\s*\}\s*\)", badan)
        self.assertEqual(
            len(boot), 1,
            "render boot di `mulai()` tidak mengoper `{ pindahFokus: false }` "
            "tepat sekali; tanpa itu Tab pertama sesudah memuat berangkat dari "
            "tengah dokumen")

    def test_lompat_ke_isi_memakai_bentuk_gerak_kondisional(self):
        """Lompatan yang DIMINTA pengguna ikut setelan gerak, tidak dipaksa.

        Bedanya dengan `pulihkanBaca` justru yang mengikat: di sana `"instant"`
        benar karena ia PEMULIHAN posisi — gerak yang tidak diminta siapa pun.
        Di sini penggunanya menekan tombol; memaksa instan berarti meniadakan
        setelan geraknya ke arah yang berlawanan. Kata-per-kata sama dengan
        `bawaKeAtas` di `layar-belajar.js`, dan itu disengaja: satu bentuk untuk
        satu kelas perpindahan.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : token jadi `"instant"`; token jadi `"auto"`
              telanjang; sebuah gulir kedua ber-`"instant"` disisipkan;
              sebuah gulir kedua ber-`"auto"` telanjang disisipkan.
          MENYUSUN ULANG, hijau : badan penangannya dipecah beberapa baris.
        """
        js = self._js()
        penangan = self._penangan(js, "#lompat-isi")
        self.assertRegex(
            penangan,
            r'behavior:\s*adaGerak\(\)\s*\?\s*"smooth"\s*:\s*"auto"',
            "penangan `#lompat-isi` tidak lagi memakai bentuk kondisional; "
            "lompatan yang diminta pengguna wajib mengikuti setelan geraknya")
        self.assertNotIn(
            '"instant"', penangan,
            "`\"instant\"` memaksa lompatan yang DIMINTA jadi tanpa gerak; itu "
            "meniadakan setelan gerak ke arah yang berlawanan")
        self.assertNotRegex(
            penangan, r'behavior:\s*"auto"',
            "`behavior: \"auto\"` telanjang: CSSOM-View membacanya sebagai "
            "'ikuti scroll-behavior kotaknya', jadi ia diam-diam mulus di "
            "`penuh` DAN di `mati` — dua keadaan, satu token, nol yang memilih")

    def test_populasi_token_behavior_tetap_tujuh_dan_dua_bentuk(self):
        r"""Tujuh situs `behavior:`, dua bentuk sah, nol telanjang.

        Dihitung SESUDAH komentar ditanggalkan, dan itu bukan kerapian:
        `grep` mentah tak berbatas memberi SEPULUH baris di pohon ini —
        tujuh situs sungguhan, satu `transition-behavior:` (komentar
        `layar-belajar.js:1140`), dan dua baris docstring `pulihkanBaca`
        (:1642 dan :1644, yang kedua menyebut `scroll-behavior:`).

        Batas `(?<![-\w])` wajib ada dan bekerja dua kali: ia menahan
        `transition-behavior:` DAN `scroll-behavior:`. Tanpanya sebuah
        `style.setProperty("transition-behavior", …)` yang sah akan ikut
        tertuduh, dan `transition-behavior: allow-discrete` adalah kosakata
        nyata repo ini — aturannya hidup di `gaya.css`.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : satu situs diganti `"auto"` telanjang; satu
              situs `behavior:` baru ditambahkan.
          MENYUSUN ULANG, hijau : sebuah komentar yang menyebut `behavior:`
              ditambahkan (komentar tidak dihitung); spasi di situs mana pun
              dirapikan.
        """
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        pola = re.compile(r"(?<![-\w])behavior:")
        SAH = (re.compile(r'(?<![-\w])behavior:\s*"instant"'),
               re.compile(r'(?<![-\w])behavior:\s*adaGerak\(\)\s*\?\s*'
                          r'"smooth"\s*:\s*"auto"'))
        # Yang diperiksa JENDELA TEKS sesudah tiap situs, bukan barisnya.
        # Versi pertama membaca per baris, dan karena itu menuduh sebuah nilai
        # kondisional yang dipecah ke beberapa baris — penyusunan ulang yang
        # sepenuhnya sah. Yang menemukannya kontrol negatifnya sendiri: sebuah
        # deformasi merah padahal harus hijau, dan yang salah predikatnya.
        situs = []
        for nama in sorted(os.listdir(os.path.join(akar, "webapp", "statik", "js"))):
            if not nama.endswith(".js"):
                continue
            with open(os.path.join(akar, "webapp", "statik", "js", nama),
                      encoding="utf-8") as f:
                src = f.read()
            tel = re.sub(r"/\*.*?\*/",
                         lambda m: "\n" * m.group(0).count("\n"), src, flags=re.S)
            tel = re.sub(r"//[^\n]*", "", tel)
            for m in pola.finditer(tel):
                baris = tel.count("\n", 0, m.start()) + 1
                jendela = " ".join(tel[m.start():m.start() + 120].split())
                situs.append((f"{nama}:{baris}", jendela))
        self.assertEqual(
            len(situs), 7,
            "jumlah situs `behavior:` berubah; setiap situs baru wajib memilih "
            "salah satu dari dua bentuk yang sudah ada, bukan bentuk ketiga. "
            f"Yang terbaca: {[s for s, _ in situs]}")
        nakal = [s for s, baris in situs
                 if not any(p.search(baris) for p in SAH)]
        self.assertEqual(
            nakal, [],
            "ada situs `behavior:` di luar dua bentuk sah "
            "(`\"instant\"` untuk pemulihan, `adaGerak() ? \"smooth\" : \"auto\"` "
            f"untuk perpindahan yang diminta): {nakal}")


class TestKuisUmpanBalik(unittest.TestCase):
    """Kuis: anggaran partikel, dan penjelasan yang berdampingan dengan kegagalannya.

    CAKUPAN YANG DIUKUR: badan `layarKuis` di `layar-kerja.js` — bukan seluruh
    berkas. Berkas itu memuat TIGA pemanggil `rayakan(` (`:315` milik kuis,
    dua lagi milik layar latihan dan ruang coba di berkas yang sama), dan
    preseden pagar `?` di S06 sudah sekali salah tuduh karena menyapu berkas.

    YANG TIDAK DIJAGA: ini pagar STRUKTUR sumber. Bahwa percikannya benar-benar
    tidak menyala per jawaban, dan bahwa penjelasannya benar-benar berdiri di
    bawah opsi yang ditekan, hanya bisa dibuktikan dengan mengukur kotak dan
    jumlah partikel di peramban — angkanya ada di tabel render di laporan.
    """

    @staticmethod
    def _js():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "js",
                               "layar-kerja.js"), encoding="utf-8") as f:
            return TestHamparanBara._telanjang(f.read())

    def _wilayah(self, nama, dalam=None):
        """Badan satu fungsi, SESUDAH dibuktikan definisinya cuma satu di sana."""
        src = dalam if dalam is not None else self._js()
        n = src.count(f"function {nama}(")
        if n != 1:
            self.fail(f"definisi `function {nama}(` muncul {n} kali di wilayah "
                      "ini, bukan satu; jangkar tes ini tidak bisa memilih "
                      "situs yang dimaksud")
        return TestHamparanBara._fungsi(src, nama)

    @staticmethod
    def _css():
        akar = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(os.path.join(akar, "webapp", "statik", "gaya.css"),
                  encoding="utf-8") as f:
            return f.read()

    def test_tombol_di_dalam_opsi_tidak_mewarisi_gaya_opsi(self):
        """`.opsi > button`, bukan `.opsi button` — dan itu bukan kerapian.

        Relokasi penjelasan menaruh `.penjelasan` BESERTA tombol tindakan
        utamanya di dalam `.opsi`. `.opsi button` berspesifisitas (0,1,1) dan
        mengalahkan `.tbl-utama` (0,1,0): `background` milik tombol utama
        ditelan sementara `color: var(--di-atas-aksen)` bertahan, jadi huruf
        yang dirancang berdiri di atas aksen berdiri di atas kartu. Terukur
        1,00-1,06:1 di keempat tema — di bawah syarat WCAG 4,5 di semuanya,
        pada tindakan yang paling sering ditekan di layar ini.

        DUA SAPUAN KELUARGA, bukan pembacaan satu blok. Menambal `color` di
        `.penjelasan .tbl` akan jadi perang spesifisitas ketiga dan kalah lagi
        nanti; yang dijaga di sini BENTUK KELUARGA selektornya.

        (a) nol selektor ber-bentuk turunan `.opsi button` di seluruh berkas,
            dan tepat 14 yang berbentuk `.opsi > button`;
        (b) setiap selektor yang menyebut sebuah wadah yang dikunci
            (`.opsi`, `.penjelasan`) DAN menjangkau tombol tindakannya lewat
            salah satu dari TIGA kata identitasnya — `button`, `.tbl`,
            `.tbl-utama`, karena `lanjut` dibuat sebagai
            `h("button.tbl.tbl-utama", …)` — dilarang; satu-satunya
            pengecualian adalah 14 aturan `.opsi > button` yang menata opsinya
            sendiri. Ini yang menutup jalan masuk kedua: `.opsi .deret >
            button { … }` dan `.opsi .tbl { padding: 0 }` tidak pernah
            berbentuk `.opsi button`, tapi keduanya menjangkau tombol `lanjut`
            yang sama dan mengembalikan cacatnya lewat pintu lain.

        Komentar ditanggalkan lebih dulu: blok komentar di atas `.opsi` MEMUAT
        potongan `.opsi button` dengan sengaja, karena itulah yang
        menerangkan kenapa bentuk turunan dibuang. Sapuan atas berkas mentah
        akan menghukum penjelasannya sendiri.

        YANG TIDAK DIJAGA, DAN ITU KEPUTUSAN: sapuan ini dikunci pada NAMA
        WADAH, jadi `.deret > button { text-align: left }` tetap HIJAU
        walaupun ia menjangkau `lanjut` juga. Sebabnya `.deret` kelas umum,
        dan angkanya bisa diadu — predikatnya `\\.deret(?![\\w-])` (BATAS
        KATA) atas baris prelude, di pohon kerja hari ini:

            gaya.css:1261  `.deret[hidden]`, di dalam daftar pemulih `[hidden]`
            gaya.css:1406  `.deret`
            gaya.css:1632  `.keadaan-isi .deret`
            gaya.css:2050  `.keluaran-kartu.deret`
            gaya.css:4633  `.deret`, di dalam daftar `#rel, #konteks, …`

        LIMA baris prelude, EMPAT selector-string berbeda — `.deret` sendirian
        muncul di dua baris. Bedakan kedua cacah itu sebelum memakainya, dan
        bedakan juga predikatnya: cacah SUBSTRING `.deret` tanpa batas kata
        memberi DELAPAN, karena `.deret-rapat` (`gaya.css:1407`) dan
        `.deret-kanan` (`:1408` dan `:4569`) adalah KELAS LAIN yang cuma
        berawalan sama. Angka tanpa predikatnya adalah klaim, bukan ukuran.

        Melarang `.deret` di SELURUH aplikasi karena itu berarti menghapus
        lima tempat gaya yang sah demi satu kasus, sementara populasi
        `.deret > button` nol hari ini — itulah kenapa jalan ini dibiarkan
        terbuka alih-alih ditutup.

        Konsekuensinya menempel pada SIAPA PUN YANG MEMINDAHKAN NODE ITU: kalau
        `lanjut` suatu hari pindah ke wadah lain, atau `.penjelasan` berhenti
        jadi wadahnya, pagar ini berhenti menjangkau tanpa memerah. Yang harus
        ditinjau saat itu adalah himpunan WADAH di sini, bukan menambah `.deret`
        ke daftar larangan.

        (v) aturan yang ditulis SATU BARIS bersama `@media`/`@supports` tidak
            terlihat PEMBACA BARIS. Sapuan wadah (b) membaca prelude dengan
            `(?m)^([^{}/@][^{}]*?)\\{`. Jangkarnya TIDAK menolak `@` sebulat
            yang terdengar: `[^{}/@]` menerima `\\n` dan `[^{}]*?` melintasi
            baris, jadi 30 prelude at-rule justru IKUT terbaca lewat baris
            kosong di depannya. Yang benar-benar tidak terbaca adalah aturan
            yang tidak MULAI di awal baris — dan itulah lubangnya, karena
            aturan dalam sebuah at-rule satu baris tidak pernah mulai di awal
            baris. Jadi
            `@media (max-width: 700px) { .penjelasan .tbl-utama { text-align: left; } }`
            LOLOS sementara bentuk multi-barisnya MERAH. Yang lolos bukan
            at-rule-nya melainkan PENULISAN SATU BARISNYA.

            KEDUA SISI ASIMETRI ITU PUNYA BARIS BATERAINYA, dan sisi hijaunya
            BENAR — jangan "diperbaiki":
              `@media (max-width: 700px) { .menipis { color: #dc2626; } }`
                satu baris -> HIJAU (pembaca aturan-per-aturan, berjangkar)
              `@media (max-width: 700px) { .opsi button { text-align: center; } }`
                satu baris -> MERAH (sapuan teks-polos `.opsi`, tanpa jangkar)

            Populasi, dengan predikat dan ruang pengukurnya:
              `@(?:media|supports)[^\\n{]*\\{[^\\n{}]*\\{[^\\n{}]*\\}`
                di pohon `_telanjang` -> NOL
                di ruang MENTAH       -> SATU, dan itu bukan aturan: contoh
                  di dalam blok komentar yang MEMBUKA dengan
                  `/* ==== @media` — hari ini `gaya.css:4436`, contohnya di
                  `:4441`. Cari teks pembukanya, bukan nomor barisnya:
                  nomornya bergeser tiap kali berkas ini tumbuh.
              predikat yang SAMA tanpa batas baris (`[^{]`, `[^{}]`)
                di pohon `_telanjang` -> EMPAT BELAS = 9 `@media` + 5
                  `@supports`, semuanya blok multi-baris normal yang memang
                  terbaca — bukan populasi lubang ini

            YANG KEBAL di tes INI, dan sebabnya ia tanpa jangkar: kedua asersi
            di atasnya berjalan atas SELURUH teks telanjang. `\\.opsi\\s+button`
            dilarang total (terbaca 0) dan `\\.opsi\\s*>\\s*button` dipatok 14,
            jadi `@media … { .opsi button { … } }` satu baris tetap MERAH.
            Yang berlubang HANYA sapuan wadah (b) di bawah.

        YANG JUGA TIDAK DIJAGA: bahwa gaya TERHITUNG `lanjut` benar-benar sama
        dengan kembarannya di luar `.opsi`. Itu `getComputedStyle` di peramban
        dan tempatnya baris R1 di tabel render, bukan tes ini — suite stdlib
        tidak punya mesin CSS.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : satu selektor dikembalikan ke bentuk turunan;
              `.opsi .deret > button { text-align: left }` ditambahkan.
          MENYUSUN ULANG, hijau : `.opsi .huruf` tetap turunan (ia memang di
              DALAM tombol, bukan anak langsung); spasi di sekitar `>`
              dirapikan; sebuah komentar yang menyebut `.opsi button`
              ditambahkan.
        """
        css = TestHamparanBara._telanjang(self._css())
        # J2: NAMA ELEMEN abai-kasus di CSS, jadi `button` di kedua sapuan ini
        # dibungkus bendera ter-scope `(?i:...)` — dan HANYA `button`. `\.opsi`
        # dibiarkan di luar bendera dengan sengaja: nama KELAS peka-kasus,
        # `.OPSI` adalah selektor mati, dan memerahkannya MERAH-palsu.
        # Bukti versi: bendera ter-scope didokumentasikan modul `re` sebagai
        # "New in version 3.6", jadi sah di lantai Python 3.8+ yang dijanjikan
        # AGENTS.md. Mesin ini menjalankan 3.14.7 dan TIDAK punya interpreter
        # 3.8/3.9/3.10, jadi klaim lantai itu bersandar pada dokumentasi, bukan
        # eksekusi — yang teruji di sini perilakunya, bukan versinya.
        self.assertEqual(
            re.findall(r"\.opsi\s+(?i:button)", css), [],
            "ada selektor ber-bentuk turunan `.opsi button`; ia (0,1,1) "
            "mengalahkan `.tbl-utama` (0,1,0) dan menelan latar tombol "
            "tindakan utama yang kini bernaung di dalam `.opsi`")
        self.assertEqual(
            len(re.findall(r"\.opsi\s*>\s*(?i:button)", css)), 14,
            "jumlah selektor `.opsi > button` bukan 14; kalau sebuah aturan "
            "opsi ditambah atau dibuang, angkanya dinaikkan BERSAMA "
            "suntingannya — jangan dilonggarkan")

        # (b) sapuan keluarga: tiap prelude yang menyebut wadah yang dikunci
        # DAN menjangkau tombol tindakannya lewat salah satu KATA
        # IDENTITASNYA.
        #
        # TIGA KATA, bukan satu. `lanjut` dibuat sebagai
        # `h("button.tbl.tbl-utama", …)` di `layar-kerja.js`, jadi tombol yang
        # sama itu terjangkau sebagai `button`, sebagai `.tbl`, DAN sebagai
        # `.tbl-utama`. Mengunci `button` sendirian meloloskan dua selektor
        # yang cacatnya SAMA PERSIS dengan yang dibunuh H1d — keduanya
        # terukur HIJAU pada versi pagar sebelum baris ini ada:
        #   `.penjelasan .tbl-utama { text-align: left }`  (0,2,0)
        #   `.opsi .tbl { padding: 0 }`                    (0,1,1)
        # Keduanya mengalahkan `.tbl-utama` (0,1,0), yang artinya wajah tombol
        # tindakan utama ditelan lewat pintu yang tidak pernah berbentuk
        # `.opsi button`.
        #
        # Keluarga `.tbl` di `gaya.css` ada SEMBILAN nama (predikat:
        # `\.tbl(?:-[\w]+)?(?![\w-])` atas berkas telanjang); DUA di dalam
        # himpunan — `.tbl` dan `.tbl-utama` — jadi TUJUH di luarnya:
        # `.tbl-bahaya`, `.tbl-besar`, `.tbl-hantu`, `.tbl-kecil`,
        # `.tbl-pergi`, `.tbl-pilih`, `.tbl-set`. Ketujuh SENGAJA di luar:
        # `lanjut` tidak memakai satu pun dari mereka, jadi mereka tidak
        # menjangkaunya.
        # Himpunan ini mengikuti kelas tombol itu; kalau kelasnya berubah,
        # himpunan ini ikut berubah, bukan dibiarkan.
        #
        # Batas kata dipasang di ketiganya. `(?<![\w-])button(?![\w-])`
        # terukur menjaring 21 selektor — sama banyak dengan substring
        # `"button"` telanjang, jadi batas itu tidak kehilangan apa pun —
        # sementara `\.tbl(?![\w-])` sengaja TIDAK menjangkau `.tbl-utama`
        # supaya keduanya terhitung sebagai kata yang berbeda.
        # K2: `button` dibungkus bendera ter-scope karena nama elemen CSS
        # abai-kasus, jadi `.penjelasan BUTTON { ... }` adalah selektor HIDUP
        # yang sebelumnya lolos sapuan ini. Bendera itu MELINGKUPI `button`
        # saja — nama wadah `.opsi`/`.penjelasan` tetap peka-kasus, karena
        # nama kelas CSS memang peka-kasus dan `.PENJELASAN` selektor mati.
        # Harga terukur NOL: fragmen yang memuat kata `button` tetap 21 di
        # pembaca satu-grup maupun dua-grup atas pohon `_telanjang`, jadi
        # tidak ada penangkapan baru hari ini.
        KATA = (r"(?<![\w-])(?i:button)(?![\w-])",
                r"\.tbl(?![\w-])",
                r"\.tbl-utama(?![\w-])")
        nakal = []
        for prelude in re.findall(r"(?m)^([^{}/@][^{}]*?)\{", css):
            for sel in prelude.split(","):
                sel = " ".join(sel.split())
                if not any(re.search(k, sel) for k in KATA):
                    continue
                # WADAH KEDUA, dan ia lebih berbahaya daripada yang pertama:
                # `lanjut` tinggal di dalam `.penjelasan`, yang merupakan ANAK
                # dari `.opsi`. `.opsi > button` karena itu tidak pernah
                # menjangkaunya — tapi `.penjelasan > .deret > button` (0,2,1)
                # mengalahkan `.tbl-utama` (0,1,0) dengan mudah. Ketiga kata
                # berpopulasi NOL di dalam `.penjelasan` hari ini, jadi bentuk
                # paling ketat gratis: BUKAN "harus kombinator anak",
                # melainkan DILARANG sama sekali.
                # NAMA WADAH DIUJI SEBAGAI TOKEN, bukan substring. `".opsi"
                # in ".opsix"` bernilai benar, jadi uji substring menuduh
                # `.opsix`/`.penjelasanx` — kelas LAIN yang cuma berawalan
                # sama — dan itu MERAH-palsu; terukur begitu kata
                # identitasnya jadi abai-kasus. Batas `(?![\w-])` menutupnya
                # tanpa menyentuh kepekaan kasusnya: `.OPSI` tetap tidak cocok,
                # karena nama kelas CSS memang peka-kasus.
                if re.search(r"\.penjelasan(?![\w-])", sel):
                    nakal.append(sel)
                    continue
                # `.opsi` menyisakan tepat satu jalan sah, dan hanya untuk
                # kata `button`: 14 aturan `.opsi > button` yang menata opsi
                # itu sendiri. `.tbl`/`.tbl-utama` berpopulasi nol di dalam
                # `.opsi` juga, jadi tidak ada pengecualian untuk keduanya.
                if (re.search(r"\.opsi(?![\w-])", sel)
                        and not re.search(r"\.opsi\s*>\s*button", sel)):
                    nakal.append(sel)
        self.assertEqual(
            nakal, [],
            "ada selektor yang menata tombol di dalam wadah opsi lewat pintu "
            f"yang salah: {nakal}. Dua pintu yang dijaga: (1) `.opsi` lewat "
            "kombinator TURUNAN — `.opsi button` (0,1,1) mengalahkan "
            "`.tbl-utama` (0,1,0); (2) `.penjelasan` lewat rantai APA PUN — "
            "`.penjelasan > .deret > button` (0,2,1) mengalahkannya lebih "
            "mudah lagi, dan `.opsi > button` tidak pernah menjangkau ke sana. "
            "Wajah tombol tindakan utama hanya boleh datang dari `.tbl`/"
            "`.tbl-utama`")

    def test_timer_tidak_panik_dan_berhenti_di_latar(self):
        """Jam yang menipis tidak berubah merah, dan berhenti saat tab di latar.

        Dua hal, satu layar. (1) Merah di detik terakhir mengubah keputusan
        jadi kecemasan — dan `--salah` di layar ini sudah berarti "jawabanmu
        keliru", jadi memakainya untuk waktu memberi satu warna dua arti.
        Tebal huruf tetap: ia menyampaikan "tinggal sedikit" tanpa merebut
        arti warna. (2) SC 2.2.2 menelan batas waktu yang berhitung sendiri:
        detik yang habis sementara tabnya tidak terlihat adalah detik yang
        tidak pernah bisa dipakai siapa pun untuk menjawab.

        Predikat warnanya menamai KELUARGA `.jam`, bukan berkas: `--salah`
        dipakai puluhan aturan lain di `gaya.css`, dan pagar yang menyapu
        berkas akan merah karena aturan yang bukan urusannya (preseden pagar
        `?` di S06).

        Dan ia menuntut HIMPUNAN NILAI, bukan nama token. `color` di keluarga
        `.jam` hanya boleh `var(--teks-2)`; `background`, `background-color`
        dan `border-color` tidak boleh muncul sama sekali. Sebabnya terukur:
        pagar yang menolak string `--salah` tetap HIJAU untuk
        `.jam { color: #dc2626 }`, yang semerah `var(--salah)` tapi tidak
        menyebut nama token apa pun.

        Dan resolusinya ikut dijaga, bukan cuma ejaannya: literal tiap token
        yang diizinkan dituntut saling lepas dari literal `--salah` di keempat
        blok tema. Tanpa itu `--teks-2: #fb7185;` di tema gelap membuat jamnya
        sungguh merah galat sementara tidak ada satu pun aturan `.jam` yang
        disentuh — terukur, dan seluruh suite tetap OK sebelum pagar itu ada.

        NORMALISASI YANG DIPAKAI, DAN YANG TIDAK. Tiap populasi di bawah
        ditulis dengan TIGA kaki — PREDIKAT, RUANG, dan PEMBACA — karena di
        kelas ini DUA pembaca aturan hidup berdampingan dan angkanya berbeda.
        Angka tanpa pembacanya bukan ukuran; ia klaim.

        DUA PEMBACA, DAN SELISIHNYA TEPAT 30.
          SATU-GRUP  `(?m)^([^{}/@][^{}]*?)\\{`  — dipakai sapuan wadah (b):
            892 fragmen tak-kosong di pohon `_telanjang`.
          DUA-GRUP   `(?m)^([^{}/@][^{}]*?)\\{([^{}]*)\\}`  — dipakai pagar
            keluarga `.jam` di bawah: 862 fragmen tak-kosong, ruang sama.
        Tiga puluh selisihnya SELURUHNYA prelude at-rule: `@media` 11,
        `@supports` 7, `@keyframes` 4, `@container` 4, `@starting-style` 4.
        Sebabnya BUKAN `@` diizinkan — `[^{}/@]` memang menolaknya — melainkan
        bahwa kelas itu MENERIMA `\\n` sementara `[^{}]*?` melintasi baris:
        sebuah baris KOSONG sebelum at-rule menjadi titik mulai yang sah, dan
        cocokannya literal `'\\n@media (max-width: 1040px) '`. Pembaca dua-grup
        tidak bisa menyelesaikannya karena badan at-rule memuat `{`.
        Karena itu 892 BUKAN "cacah selektor". Cacah selektor yang benar-benar
        dibayar pagar adalah 862 — fragmen yang punya badan kurung-kosong.

        KESIMPULAN YANG TIDAK BERGERAK di kedua pembaca, dan inilah yang
        menopang keputusan di bawah: fragmen dibuka [A-Z] = NOL, di 892 maupun
        di 862; fragmen membawa [A-Z] = EMPAT di keduanya, dan keempatnya nama
        kelas sungguhan — `.t-Mudah`, `.t-Menengah`, `.t-Lanjut`, `.t-Sulit`.

        KONTRALABEL ruang MENTAH — ini BUKAN populasi pagar, ia justru alasan
        `_telanjang` ada: satu-grup 1548 apa adanya / 1547 tak-kosong;
        dua-grup 1460 / 1459 tak-kosong; 19 fragmen dibuka [A-Z]; fragmen
        membawa [A-Z] 477 (satu-grup) dan 426 (dua-grup). Kesembilan belas dan
        ratusan itu prosa komentar yang terbaca sebagai prelude.

        DUA ASERSI `.opsi` DI ATAS BUKAN PEMBACA ATURAN: keduanya `re.findall`
        atas SELURUH teks `_telanjang`, tanpa jangkar baris. Label itu penting
        karena dari situlah asimetri di bawah berasal.

        ASIMETRI DUA BENTUK PEMBACAAN, dan SISI HIJAUNYA BENAR. Sapuan
        teks-polos (`.opsi`) tidak punya lubang "satu baris di dalam `@`",
        sementara pembaca aturan-per-aturan — sapuan wadah (b) dan pagar
        keluarga `.jam` di bawah, keduanya berjangkar `^` — punya. Dua baris
        baterai membuktikan kedua sisi:
          `@media (max-width: 700px) { .menipis { color: #dc2626; } }` satu
            baris -> HIJAU, dan itu BENAR untuk pagar ini: menutupnya menuntut
            pemindai kurung yang risikonya (`@keyframes`, `@media` bersarang,
            nilai berisi kurung) lebih besar daripada lubang berpopulasi nol.
            JANGAN "perbaiki" baris hijau ini.
          `@media (max-width: 700px) { .opsi button { text-align: center; } }`
            satu baris -> MERAH, di asersi larangan `.opsi` yang tanpa jangkar.
        Kesimpulannya: jangan menyalin harapan satu pagar ke pagar lain tanpa
        menyalin PEMBACAnya juga.

          DIPAKAI — spasi di dalam deklarasi: `" ".join(nilai.split())` plus
            spasi di tepi dalam tanda kurung, sehingga `var( --teks-2 )`
            dianggap sama dengan `var(--teks-2)`. Tanpa itu satu spasi
            menjatuhkan tes untuk kerapian yang sah (MERAH-palsu).
            PREDIKAT `var\\(\\s` · RUANG `_telanjang` · PEMBACA hitungan teks
            polos (bukan pembaca aturan): NOL dari 1347 pemanggilan `var(`
            (1362 di ruang MENTAH, juga NOL).

          DIPAKAI — kasus NAMA PROPERTI: `prop.strip().lower()`, karena nama
            properti CSS abai-kasus sementara `in IZIN_JAM` tidak. Tanpa itu
            `.jam { COLOR: #dc2626; }` tidak terbaca sama sekali (HIJAU-palsu).
            PREDIKAT `[A-Z]` pada nama properti · RUANG `_telanjang` · PEMBACA
            DUA-GRUP, badan dipecah `;` lalu `:` pertama: NOL dari 2624
            deklarasi.

          DIPAKAI — kasus BADAN ATURAN pada larangan total `color` di aturan
            ber-`.menipis`: `isi.lower()`. Tanpa itu
            `.menipis { COLOR: var(--teks-2); }` lolos larangan total dan hanya
            tertangkap asersi lain yang menjaga hal berbeda (HIJAU-palsu).
            PREDIKAT, RUANG dan PEMBACA sama dengan butir di atasnya: NOL dari
            2624 deklarasi.

          DIPAKAI — kasus NAMA ELEMEN, di TIGA tempat: dua sapuan `.opsi`
            (`(?i:button)`) dan kata identitas sapuan wadah
            (`(?<![\\w-])(?i:button)(?![\\w-])`). Nama elemen abai-kasus di CSS,
            jadi `.opsi BUTTON` dan `.penjelasan BUTTON` selektor HIDUP yang
            sebelumnya lolos (HIJAU-palsu). Nama WADAH tetap peka-kasus.
            PREDIKAT `[A-Z]` pada karakter pertama fragmen · RUANG `_telanjang`
            · PEMBACA keduanya, dan hasilnya sama: NOL dari 892 (satu-grup) dan
            NOL dari 862 (dua-grup). Harga penambalannya juga nol: fragmen yang
            memuat kata `button` tetap 21 di kedua pembaca, peka-kasus maupun
            abai-kasus.

          DIPAKAI — kasus NAMA FUNGSI: token nama yang TEPAT mendahului `(`
            dikecilkan, sehingga `VAR(--teks-2)` tidak lagi MERAH-palsu. Isi
            argumen tidak disentuh, jadi `VAR(--TEKS-2)` menjadi
            `var(--TEKS-2)` dan tetap MERAH.
            PREDIKAT `VAR\\(` · RUANG `_telanjang` dan MENTAH · PEMBACA
            hitungan teks polos: NOL di kedua ruang.

          DIPAKAI — kasus LITERAL HEKSA di pagar resolusi: heksa dikecilkan
            sebelum kedua himpunan diadu, sehingga `--teks-2: #FB7185;`
            tertangkap sebagai literal `--salah` (HIJAU-palsu).
            PREDIKAT `#[0-9a-fA-F]{6}\\b` lalu `[A-F]` · RUANG `_telanjang` dan
            MENTAH · PEMBACA hitungan teks polos: NOL dari 103 dan NOL dari 112.

          TIDAK — nama KELAS dan id, dan ini keputusan bukan kelalaian: nama
            kelas CSS peka-kasus, jadi `.OPSI` adalah selektor MATI dan
            memerahkannya MERAH-palsu. Inilah sebabnya `sel.lower()`
            bulat-bulat DILARANG di sini: EMPAT fragmen membawa [A-Z] dan
            keempatnya nama kelas sungguhan (`.t-Mudah`, `.t-Menengah`,
            `.t-Lanjut`, `.t-Sulit`) — angka yang sama di kedua pembaca.
            Mengecilkan fragmen akan menyamakan keempatnya dengan kelas yang
            tidak pernah ada.

          TIDAK — nama PROPERTI KUSTOM: `--TEKS-2` adalah properti yang BERBEDA
            dari `--teks-2` karena nama kustom CSS peka-kasus. `var(--TEKS-2)`
            MERAH bukan karena ejaan melainkan karena ia token lain yang tak
            terdefinisi, dan mengganti nama deklarasinya jadi `--TEKS-2:` MERAH
            lewat penjaga "terbaca di empat blok tema".

          TIDAK — heksa sebagai ANGGOTA `IZIN_JAM`: `#DC2626` MERAH karena
            bukan anggota himpunan, dan itu jawaban yang benar; tidak ada heksa
            apa pun yang menjadi anggota. Kanonisasi heksa di atas sengaja
            hanya menyentuh pagar resolusi.

        YANG TIDAK DIJAGA — daftar ini TIDAK ditulis dari perasaan; tiap butir
        punya baris baterainya, dan yang sudah ditutup ditandai:

        (i) `.menipis` berdiri sendiri. DITUTUP: predikat keluarga membaca
            `.jam` ATAU `.menipis`, jadi `.menipis { color: var(--salah) }`
            dan `.menipis { background: #dc2626 }` keduanya MERAH. Sebelum
            itu keduanya hijau, padahal `.menipis` cuma dipasang di satu
            tempat di seluruh aplikasi — `layar-kerja.js:177`, pada jam ini.

        (ii) selektor ber-NAMA ELEMEN telanjang yang menyetel warna. `span
            { color: var(--salah) }` HIJAU, dan itu keputusan: nama elemen
            adalah pemilik gaya dasar di berkas ini — TUJUH aturan memakainya
            untuk warna (`body`, `a`, `button, input, select, textarea`,
            `button`, `kbd`, `mark`, dan `body` lagi di blok cetak; diukur
            dengan prelude yang seluruh selektornya cocok `[a-z][a-z0-9]*`
            dan bodinya menyetel salah satu dari keempat properti). Melarang
            `span` seumur berkas berarti menghapus dasar yang sah demi satu
            kasus — alasan yang sama dengan `.deret` dan `.tbl-bahaya`.

        (iii) properti pembawa warna di luar EMPAT nama yang dibaca
            `IZIN_JAM`. Terukur HIJAU: `.jam { border-left: 2px solid red }`,
            `.jam { box-shadow: 0 0 0 3px var(--salah) }`,
            `.jam { filter: hue-rotate(320deg) }`. Yang dibaca adalah
            permukaan warna yang paling mungkin dipakai orang untuk "membuat
            jamnya merah", bukan seluruh ruang cara membuat sesuatu tampak
            merah.

        (iv) rantai `var()` DUA langkah. `--teks-2: var(--salah);` di blok
            tema HIJAU: pagar resolusi membandingkan literal, dan literal
            token itu menjadi `var(--salah)` — bukan heksa — jadi kedua
            himpunan tetap saling lepas sebagai string. Suite stdlib tidak
            punya resolver CSS; menutup ini butuh peramban.

        (v) aturan yang ditulis SATU BARIS bersama `@media`/`@supports` tidak
            terlihat PEMBACA BARIS. `aturan` di atas dibaca dengan
            `(?m)^([^{}/@][^{}]*?)\\{`. Jangkarnya TIDAK menolak `@` sebulat
            yang terdengar: `[^{}/@]` menerima `\\n`, jadi 30 prelude at-rule
            ikut terbaca lewat baris kosong di depannya (lihat "DUA PEMBACA" di
            atas). Yang benar-benar tidak terbaca adalah aturan yang tidak
            MULAI di awal baris, dan aturan dalam sebuah at-rule satu baris
            memang tidak. Akibatnya
            `@media (max-width: 700px) { .menipis { color: #dc2626; } }`
            LOLOS sementara bentuk multi-barisnya MERAH. Yang lolos bukan
            at-rule-nya — bentuk multi-baris tetap terjaga — melainkan
            PENULISAN SATU BARISNYA.

            KEDUA SISI ASIMETRI ITU PUNYA BARIS BATERAINYA, dan sisi hijaunya
            BENAR — jangan "diperbaiki":
              `@media (max-width: 700px) { .menipis { color: #dc2626; } }`
                satu baris -> HIJAU (pembaca aturan-per-aturan, berjangkar)
              `@media (max-width: 700px) { .opsi button { text-align: center; } }`
                satu baris -> MERAH (sapuan teks-polos `.opsi`, tanpa jangkar)

            Populasi, dengan predikat dan ruang pengukurnya:
              `@(?:media|supports)[^\\n{]*\\{[^\\n{}]*\\{[^\\n{}]*\\}`
                di pohon `_telanjang` -> NOL
                di ruang MENTAH       -> SATU, dan itu bukan aturan: contoh
                  di dalam blok komentar yang MEMBUKA dengan
                  `/* ==== @media` — hari ini `gaya.css:4436`, contohnya di
                  `:4441`. Cari teks pembukanya, bukan nomor barisnya:
                  nomornya bergeser tiap kali berkas ini tumbuh.
              predikat yang SAMA tanpa batas baris (`[^{]`, `[^{}]`)
                di pohon `_telanjang` -> EMPAT BELAS = 9 `@media` + 5
                  `@supports`, dan keempat belasnya blok multi-baris normal
                  yang memang terbaca. Angka itu BUKAN populasi lubang ini;
                  jangan memakainya sebagai alasan menulis ulang pembacanya
                  jadi pemindai kurung — `@keyframes`, `@media` bersarang, dan
                  nilai berisi kurung lebih mahal daripada lubang berpopulasi
                  nol.

            YANG KEBAL, dan sebabnya sederhana — ia tidak memakai jangkar:
            sapuan yang berjalan atas SELURUH teks telanjang. Di
            `test_tombol_di_dalam_opsi_tidak_mewarisi_gaya_opsi` itu
            `\\.opsi\\s+button` (dilarang total, terbaca 0) dan cacah
            `\\.opsi\\s*>\\s*button` (dipatok 14): sebuah
            `@media … { .opsi button { … } }` satu baris tetap MERAH lewat
            keduanya. Yang berlubang hanya asersi yang lewat pembaca baris —
            `blok` dan `jam_warna` di sini, dan sapuan wadah (b) di sana.

        YANG SUDAH TIDAK LOLOS, dan versi paragraf ini sebelumnya salah
        mengklaimnya lolos: `var()` yang namanya di luar himpunan. `.jam {
        color: var(--waktu-gawat) }` MERAH, karena himpunan nilai mematok
        NAMA tokennya juga — bukan cuma menolak `--salah`.

        PAGAR CABANG SEMBUNYI MENGUNCI BENTUK, BUKAN PERILAKU. Kalau jedanya
        dipindahkan ke helper (`const jedaJam = () => { clearInterval(jamId);
        jamId = 0; };`) lalu dipanggil dari cabang itu, perilakunya identik
        tapi pagar ini MERAH. Bentuk yang benar: perluas pagarnya bersama
        suntingannya — jangan balikkan bentuk kodenya cuma supaya hijau.

        Melanjutkan berarti memasang interval baru DI ATAS angka yang sama —
        `sisaDetik` hanya diikat sekali. Kalau ia dihitung ulang dari
        `sesi.durasi`, tab yang sempat disembunyikan justru memberi waktu
        gratis.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : `color: var(--salah)` dikembalikan ke blok itu;
              pelepasan `visibilitychange` dihapus dari `bersihkan`; jalur
              pembersih kedua ditambahkan; `sisaDetik` di-reset saat lanjut.
          MENYUSUN ULANG, hijau : `var(--salah)` dipakai aturan LAIN di
              `gaya.css`; spasi di blok `.jam.menipis` dirapikan.
        """
        # SAPUAN KELUARGA, bukan satu blok. Membaca `^\.jam\.menipis\s*\{`
        # saja meloloskan selektor majemuk: `.kuis-kemajuan .jam.menipis
        # { color: … }` mengembalikan merahnya lewat pintu yang tidak dibaca
        # pagarnya, dan itu terukur HIJAU pada versi pertama pagar ini.
        css = TestHamparanBara._telanjang(self._css())
        aturan = [(sel.strip(), isi) for prelude, isi
                  in re.findall(r"(?m)^([^{}/@][^{}]*?)\{([^{}]*)\}", css)
                  for sel in prelude.split(",")]
        # DUA KATA IDENTITAS, dan keduanya milik jam yang sama.
        # `jam.classList.toggle("menipis", sisaDetik <= 30)`
        # (`layar-kerja.js:177`) adalah SATU-SATUNYA pemakaian `menipis`
        # sebagai kelas di seluruh `webapp/statik/js/`, dan `.jam.menipis`
        # (`gaya.css:3780`) satu-satunya prelude yang menyebutnya. Mengunci
        # `.jam` sendirian karena itu meloloskan `.menipis { color:
        # var(--salah) }` — cacat yang persis sama dengan yang ditutup untuk
        # tombol `lanjut`, cuma di layar sebelah.
        #
        # Jangkar kiri `(^|[\s,>+~(])` DIBUANG dengan sengaja: `\.` sendiri
        # sudah batas kiri sebuah kelas, sementara jangkar itu meloloskan
        # `span.jam`, `span.jam.menipis` dan `div.menipis` — dan `tag.kelas`
        # bukan bentuk teoretis di berkas ini, 44 selektor memakainya.
        #
        # Angka 44 itu punya predikat dan ruang, dan keduanya perlu disebut
        # karena angka ini yang dipakai membenarkan pembuangan jangkar: nama
        # elemen SUNGGUHAN diikuti kelas, `(?<![#\w.-])<elemen>\.[\w-]+`
        # dengan `<elemen>` diadu ke daftar nama elemen HTML/SVG, dihitung per
        # SELEKTOR (hasil `prelude.split(",")`) di pohon `_telanjang`.
        #
        # SATU PREDIKAT PUNYA TIGA PEMBACAAN, dan ketiganya angka yang berbeda.
        # Untuk predikat longgar `[a-z0-9]\.[\w-]` di pohon `_telanjang`:
        #     95  = kemunculan DIJUMLAH per selektor
        #     91  = cacah SELEKTOR yang membawa minimal satu
        #    151  = kemunculan atas SELURUH teks
        # Yang longgar menyapu `#layar.penuh` dan
        # `#rel.pakai-tanda .rel-pemicu.kini::before` — itu id dan kelas
        # berantai, bukan `tag.kelas`.
        #
        # Untuk predikat KETAT ketiga pembacaan itu kebetulan memberi angka
        # yang SAMA: 44, 44, dan 44. Kebetulan itulah yang membuat label "per
        # selektor" bertahan tanpa pernah diuji — kalau angkanya dipakai
        # sebagai alasan, sebut pembacaannya, bukan cuma predikatnya. Pakai
        # yang ketat kalau angkanya
        # dipakai sebagai alasan.
        # Terukur: kedua bentuk menjaring selektor yang SAMA hari ini
        # (`.jam`, `.jam.menipis`), jadi bentuk yang lebih ketat gratis.
        # `(?![\w-])` tetap wajib: tanpanya `.jamu-x` dan `.menipis-x` —
        # kelas lain yang cuma berawalan sama — ikut tertuduh.
        KELUARGA_JAM = r"\.(?:jam|menipis)(?![\w-])"
        # `blok` sengaja LEBIH SEMPIT daripada keluarga: ia memilih aturan
        # yang menyebut `.menipis`, karena asersi berikutnya melarang `color`
        # di sana BERAPA PUN tokennya. Melebarkannya ke seluruh keluarga akan
        # memerahkan pekerjaan yang sah — aturan `.jam` memang menyetel
        # `color: var(--teks-2)`, dan itu justru satu-satunya nilai yang
        # diizinkan.
        blok = [(sel, isi) for sel, isi in aturan
                if re.search(r"\.menipis(?![\w-])", sel)]
        self.assertTrue(
            blok, "tidak ada satu pun aturan ber-`.menipis` di `gaya.css`; "
                  "pagar ini tidak bisa memilih aturan yang dimaksud")
        # J1: BADAN ATURAN dinormalkan sebelum uji substring. Nama properti
        # CSS abai-kasus, `"color" in isi` tidak — jadi
        # `.menipis { COLOR: var(--teks-2); }` lolos larangan TOTAL ini dan
        # hanya tertangkap asersi himpunan nilai di bawah, yang menjaga hal
        # lain. Harganya nol: pembaca yang sama melihat 2624 deklarasi di
        # pohon `_telanjang` dan nama properti ber-`[A-Z]` NOL di antaranya.
        # Yang dinormalkan HANYA badannya; `sel` tidak, karena nama kelas CSS
        # peka-kasus dan `.OPSI`/`.t-Mudah` memang selektor yang berbeda.
        berwarna = [(sel, isi.strip()) for sel, isi in blok
                    if "color" in isi.lower()]
        self.assertEqual(
            berwarna, [],
            "ada aturan `.jam.menipis` yang menyetel warna. Merah di detik "
            "terakhir mengubah keputusan jadi kecemasan, dan `--salah` di "
            f"layar ini sudah berarti 'jawabanmu keliru'. Yang terbaca: {berwarna}")
        # Asersi KEDUA, dan ia menuntut HIMPUNAN NILAI — bukan nama token.
        # Asersi di atas melarang `color` di `.jam.menipis` berapa pun
        # tokennya; yang ini menjaga SELURUH keluarga `.jam`.
        #
        # NAMA TOKEN BUKAN PAGAR. Versi sebelumnya menolak aturan `.jam` yang
        # memuat string `--salah`, dan itu terukur HIJAU dengan cacat yang
        # persis sama: `.jam { color: #dc2626 }` — merah permanen di detik
        # terakhir, tanpa menyebut nama token apa pun. Sebuah pagar yang bisa
        # dilewati dengan menuliskan warnanya sebagai heksa tidak menjaga
        # warna; ia menjaga ejaan.
        #
        # Yang dituntut karena itu adalah apa yang TERUKUR hari ini: `color`
        # di keluarga `.jam` hanya boleh `var(--teks-2)`, dan tiga properti
        # pembawa warna lainnya tidak muncul sama sekali. Kalau jam memang
        # perlu warna baru, himpunan ini DINAIKKAN bersama suntingannya —
        # bukan dilonggarkan jadi "apa pun kecuali `--salah`".
        #
        # Batas `(?![\w-])` wajib ada: `.jam` bukan awalan nama kelas lain,
        # dan tanpa batas itu sebuah `.jamu-x` ikut tertuduh.
        IZIN_JAM = {"color": {"var(--teks-2)"}, "background": set(),
                    "background-color": set(), "border-color": set()}
        jam_warna = []
        for sel, isi in aturan:
            if not re.search(KELUARGA_JAM, sel):
                continue
            for dek in isi.split(";"):
                if ":" not in dek:
                    continue
                prop, nilai = dek.split(":", 1)
                # DUA NORMALISASI, dan dua arah cacat yang berlawanan.
                #
                # (1) Nama properti CSS ABAI-KASUS; `in IZIN_JAM` tidak. Tanpa
                #     `.lower()`, `.jam { COLOR: #dc2626; }` tidak terbaca SAMA
                #     SEKALI — merah permanen di detik terakhir kembali lewat
                #     satu huruf besar, tanpa menulis nama token galat apa pun.
                #     Itu HIJAU-palsu, dan harganya nol: pembaca yang sama
                #     melihat 2624 deklarasi di pohon `_telanjang` dan
                #     `re.search(r"[A-Z]", prop)` mengenai NOL di antaranya.
                #
                # (2) Spasi di tepi dalam tanda kurung dikanonkan. `var( --teks-2 )`
                #     CSS-nya sah dan resolusinya IDENTIK dengan `var(--teks-2)`,
                #     tapi keanggotaan diuji sebagai STRING — jadi satu spasi
                #     sesudah `(` menjatuhkan tes untuk suntingan kerapian yang
                #     sah. Itu MERAH-palsu. Populasinya juga nol: `var\(\s`
                #     terbaca NOL dari 1347 pemanggilan `var(` di pohon
                #     `_telanjang` (NOL dari 1362 di ruang MENTAH), jadi kedua
                #     tambalan ini membeli ketahanan tanpa mengubah satu pun
                #     putusan hari ini.
                prop = prop.strip().lower()
                nilai = " ".join(nilai.split())
                nilai = re.sub(r"\(\s+", "(", nilai)
                nilai = re.sub(r"\s+\)", ")", nilai)
                # K3: nama FUNGSI CSS abai-kasus, jadi `VAR(--teks-2)` sah dan
                # resolusinya identik dengan `var(--teks-2)` — menolaknya
                # MERAH-palsu. Yang dikecilkan HANYA token nama yang TEPAT
                # mendahului `(`; lookbehind `(?<![\w-])` menjaga agar ekor
                # sebuah nama kustom tidak ikut tersapu, dan isi argumennya
                # tidak disentuh sama sekali — `VAR(--TEKS-2)` tetap
                # `var(--TEKS-2)` dan tetap MERAH, karena nama properti kustom
                # memang peka-kasus. Populasi `VAR(` NOL di pohon `_telanjang`
                # (dan NOL di ruang MENTAH), jadi tambalan ini nol harga.
                nilai = re.sub(r"(?<![\w-])([A-Za-z-]+)(?=\()",
                               lambda m: m.group(1).lower(), nilai)
                if prop in IZIN_JAM and nilai not in IZIN_JAM[prop]:
                    jam_warna.append((sel, prop, nilai))
        self.assertEqual(
            jam_warna, [],
            "ada aturan di keluarga `.jam`/`.menipis` yang membawa warna di "
            "luar "
            f"himpunan yang terukur. Yang diizinkan: {IZIN_JAM}. Yang "
            f"terbaca: {jam_warna}. Merah di detik terakhir mengubah "
            "keputusan jadi kecemasan, dan di layar ini merah sudah berarti "
            "'jawabanmu keliru' — jadi yang dijaga bukan nama tokennya "
            "melainkan NILAI yang benar-benar sampai ke mata: `#dc2626` "
            "sama merahnya dengan `var(--salah)`. Kalau jam memang perlu "
            "warna baru, naikkan himpunan ini bersama suntinganmu")

        # Asersi KETIGA, dan ia menutup lubang yang paling mahal dari dua di
        # atas: keduanya mengunci EJAAN nilainya, bukan RESOLUSINYA. `color:
        # var(--teks-2)` tetap diizinkan sekalipun `--teks-2` sendiri
        # didefinisikan merah di blok tema. Terukur: mengganti
        # `--teks-2: #b3a6c6;` (tema gelap) menjadi `#fb7185` — yang adalah
        # nilai `--salah` di tema yang SAMA — membuat jam kuis sungguh berubah
        # jadi warna galat sementara seluruh suite tetap OK.
        #
        # SATU LANGKAH, dan disetir oleh `IZIN_JAM` sendiri: tiap token yang
        # diizinkan di atas dibaca literalnya di keempat blok tema, lalu
        # dituntut saling lepas dari literal keluarga galat. Tidak ada nama
        # token yang dipaku di sini selain nama keluarga galatnya — kalau
        # `IZIN_JAM` nanti bertambah token, penjagaannya bertambah sendiri.
        #
        # Himpunan hari ini terukur lepas, jadi pagar ini gratis:
        #   --teks-2 = {#b3a6c6, #a297ad, #574d66, #e0d8ec}
        #   --salah  = {#fb7185, #dd8b96, #be123c, #ffa3b0}
        def literal_tema(nama):
            # J3: KASUS LITERAL HEKSA dikanonkan sebelum keanggotaan diadu.
            # `#FB7185` dan `#fb7185` warna yang SAMA di mata, tapi kedua
            # himpunan di bawah dibandingkan sebagai string — jadi
            # `--teks-2: #FB7185;` lolos padahal ia literal `--salah` persis.
            # Yang dikanonkan HANYA heksanya; nama properti kustom tidak,
            # karena `--TEKS-2` memang properti yang berbeda dari `--teks-2`.
            # Populasi heksa ber-`[A-F]` nol: 0 dari 103 heksa enam-digit di
            # pohon `_telanjang`, 0 dari 112 di ruang MENTAH.
            return {re.sub(r"#[0-9a-fA-F]{3,8}\b",
                           lambda m: m.group(0).lower(), v.strip())
                    for v in re.findall(
                        rf"(?m)^\s*{re.escape(nama)}\s*:\s*([^;]+);", css)}

        GALAT = "--salah"
        lit_galat = literal_tema(GALAT)
        # Penjaga anti-lolos-kosong: perbandingan di bawah akan lolos dengan
        # cara paling tidak berarti kalau salah satu himpunan kosong, jadi
        # cacah blok temanya dipatok. Tema kelima berarti pagar ini ditinjau
        # BERSAMA temanya, bukan angkanya dilonggarkan.
        self.assertEqual(
            len(lit_galat), 4,
            f"`{GALAT}` tidak terbaca di empat blok tema (terbaca "
            f"{len(lit_galat)}: {sorted(lit_galat)}); tanpa itu perbandingan "
            "resolusi di bawah lolos karena kosong, bukan karena warnanya "
            "aman")
        for prop, izin in sorted(IZIN_JAM.items()):
            for nilai in sorted(izin):
                tok = re.fullmatch(r"var\(\s*(--[\w-]+)\s*\)", nilai)
                if not tok:
                    continue
                nama = tok.group(1)
                lit = literal_tema(nama)
                self.assertEqual(
                    len(lit), 4,
                    f"`{nama}` — token yang diizinkan untuk `{prop}` di "
                    f"keluarga jam — tidak terbaca di empat blok tema "
                    f"(terbaca {len(lit)}: {sorted(lit)}); pagar resolusi "
                    "tidak bisa membandingkan apa pun")
                self.assertEqual(
                    lit & lit_galat, set(),
                    f"`{nama}` dan `{GALAT}` memakai literal yang SAMA di "
                    f"blok tema: {sorted(lit & lit_galat)}. Himpunan nilai di "
                    f"atas mengunci ejaan `var({nama})`, bukan warna yang "
                    "benar-benar sampai ke mata — jadi jam kuis bisa jadi "
                    "merah galat tanpa satu pun aturan `.jam` disentuh. Yang "
                    f"terbaca: {nama}={sorted(lit)}, {GALAT}="
                    f"{sorted(lit_galat)}")

        kuis = self._wilayah("layarKuis")
        self.assertIn(
            'addEventListener("visibilitychange"', kuis,
            "jam kuis tidak berhenti saat tabnya di latar; waktu habis di "
            "belakang punggung orangnya")
        self.assertEqual(
            kuis.count("bersihkan = () => {"), 1,
            "ada lebih dari satu jalur pembersih di `layarKuis`; salah satunya "
            "suatu hari terlupa di satu cabang keluar, dan pendengar yang "
            "tertinggal menyalakan jam milik kuis yang sudah ditutup")
        awal = kuis.index("bersihkan = () => {")
        dalam, tutup = 0, None
        for j in range(awal, len(kuis)):
            if kuis[j] == "{":
                dalam += 1
            elif kuis[j] == "}":
                dalam -= 1
                if dalam == 0:
                    tutup = j
                    break
        self.assertIsNotNone(tutup, "`bersihkan` tidak tertutup kurungnya")
        self.assertIn(
            'removeEventListener("visibilitychange"', kuis[awal:tutup],
            "pendengar `visibilitychange` tidak dilepas di `bersihkan` yang "
            "sudah ada; ia hidup terus sesudah layar kuis ditinggalkan")
        # JEDANYA SENDIRI, bukan perpipaannya. Pagar yang cuma membuktikan
        # "pendengar dipasang dan dilepas" tetap HIJAU walau seluruh badan
        # cabang `document.hidden` dikosongkan — terukur.
        cab = re.search(r"if\s*\(\s*document\.hidden\s*\)\s*\{([^{}]*)\}", kuis)
        if not cab:
            self.fail("tidak ada cabang `if (document.hidden) { … }` di "
                      "`layarKuis`; jamnya tidak pernah dijeda")
        self.assertIn(
            "clearInterval(jamId)", cab.group(1),
            "cabang `document.hidden` tidak mematikan pencacahnya; jam terus "
            "berjalan di belakang punggung orangnya. "
            "Pagar ini mengunci BENTUK cabang, bukan perilakunya: kalau kamu memindahkan jedanya ke helper (`const jedaJam = () => { clearInterval(jamId); jamId = 0; };`) lalu memanggilnya dari cabang itu, PERLUAS pagarnya bersama suntinganmu — jangan balikkan bentuknya cuma supaya hijau. "
            f"Isi: {cab.group(1)!r}")
        # `clearInterval` dan `jamId = 0` adalah SATU pasangan: pintu
        # `if (!jamId …)` membaca variabel yang sama, jadi membersihkan
        # pencacah tanpa menolkan gagangnya membuat jam BEKU PERMANEN sesudah
        # satu perpindahan tab — `selesai(true)` tidak pernah menyala dan mode
        # timer mati diam-diam.
        self.assertRegex(
            cab.group(1), r"jamId\s*=\s*0",
            "`jamId` tidak ditolkan di cabang sembunyi; `jalankanJam()` akan "
            "menolak memasang interval baru dan jam beku permanen sesudah "
            "satu perpindahan tab. "
            "Pagar ini mengunci BENTUK cabang, bukan perilakunya: kalau kamu memindahkan jedanya ke helper (`const jedaJam = () => { clearInterval(jamId); jamId = 0; };`) lalu memanggilnya dari cabang itu, PERLUAS pagarnya bersama suntinganmu — jangan balikkan bentuknya cuma supaya hijau. "
            f"Isi: {cab.group(1)!r}")
        self.assertRegex(
            kuis, r"jalankanJam\s*=\s*\(\)\s*=>\s*\{[^{}]*if\s*\(\s*!\s*jamId",
            "`jalankanJam` tidak lagi berpintu `!jamId`; memasang interval "
            "kedua di atas yang pertama membuat jam berjalan dua kali cepat")

        self.assertEqual(
            len(re.findall(r"sisaDetik\s*=(?!=)", kuis)), 1,
            "`sisaDetik` ditulis lebih dari sekali; melanjutkan jam harus "
            "memasang interval baru DI ATAS angka yang sama, bukan menghitung "
            "ulang dari penuh — tab yang sempat disembunyikan tidak boleh "
            "memberi waktu gratis")

    def test_partikel_dianggarkan_sekali_per_kuis_bukan_per_jawaban(self):
        """`percikBara` sekali di layar hasil, nol kali di jalur jawab.

        Satu percikan per jawaban benar terdengar murah sampai dikalikan dua
        puluh soal: yang tersisa bukan perayaan melainkan kebisingan, dan yang
        paling dihukum justru orang yang menjawab benar paling banyak.
        Ambangnya juga nyata — SC 2.3.1 menghitung <=3 pasang perubahan
        luminansi per detik di >25% medan pandang.

        LAPANGAN BUKTINYA, diukur berpasangan:
          MELANGGAR, merah  : `percikBara` dikembalikan ke jalur jawab;
              `percikBara` dihapus dari cabang `sempurna` di layar hasil.
          MENYUSUN ULANG, hijau : `jumlah` diganti angka lain; spasi dan
              pemecahan baris di kedua tempat dirapikan.
        """
        kuis = self._wilayah("layarKuis")
        jawab = self._wilayah("jawab", kuis)
        self.assertNotIn(
            "percikBara", jawab,
            "`percikBara` kembali ke jalur jawab; dua puluh soal berarti dua "
            "puluh percikan, dan yang menjawab benar paling banyak yang paling "
            "dihukum")
        hasil = self._wilayah("gambarHasil", kuis)
        self.assertRegex(
            hasil, r"percikBara\s*\(",
            "anggaran partikelnya hilang sama sekali; yang diminta bukan nol "
            "perayaan melainkan satu kali per kuis")
        self.assertRegex(
            hasil, r"if\s*\(\s*sempurna\s*\)\s*\{[^}]*percikBara\s*\(",
            "`percikBara` di layar hasil tidak lagi berdiri di bawah gerbang "
            "`sempurna`; ia akan menyala untuk skor apa pun")

    def test_penjelasan_berdampingan_dengan_opsi_yang_dipilih(self):
        """Penjelasannya disisipkan relatif ke opsi yang ditekan, bukan di kaki.

        Umpan balik yang menjelaskan hanya bekerja kalau ia berdampingan dengan
        kegagalannya. Di kaki daftar, mata harus kembali ke atas untuk
        mencocokkan "kenapa" dengan opsi mana yang tadi ditekan — pada opsi
        kelima jarak itu sudah lebih panjang daripada penjelasannya sendiri.

        LAPANGAN BUKTINYA:
          MELANGGAR, merah  : dikembalikan ke `isi.appendChild(h("div.penjelasan"`.
          MENYUSUN ULANG, hijau : nama variabel `blok`/`dipilih` diganti; spasi
              dirapikan; cabang cadangannya ditulis bentuk blok.
        """
        jawab = self._wilayah("jawab", self._wilayah("layarKuis"))
        self.assertRegex(
            jawab, r"insertBefore\s*\(",
            "penjelasan tidak lagi disisipkan relatif ke opsi mana pun")
        self.assertNotRegex(
            jawab, r'isi\s*\.\s*appendChild\s*\(\s*h\(\s*["\']div\.penjelasan',
            "penjelasan kembali di-append ke kaki daftar opsi; ia berhenti "
            "berdampingan dengan opsi yang ditekan")
        # Menuntut `tombol[pilihan]` ada DI SUATU TEMPAT di badan ini tidak
        # menjaga apa pun: token itu juga dipakai jalur `.salah` dan `getar`.
        # Yang diikat di sini SITUS SISIPANNYA — simpul acuan `insertBefore`
        # dibaca dari kode, lalu bindingnya yang dituntut. Namanya bebas, jadi
        # mengganti nama variabel tetap hijau.
        m = re.search(r"(\w+)\s*\.\s*parentNode\s*\.\s*insertBefore"
                      r"\s*\(\s*\w+\s*,\s*\1\s*\.\s*nextSibling", jawab)
        self.assertIsNotNone(
            m, "tidak ada `X.parentNode.insertBefore(blok, X.nextSibling)` di "
               "jalur jawab; penjelasan tidak disisipkan sesudah sebuah opsi")
        acuan = m.group(1)
        self.assertRegex(
            jawab, rf"\b{re.escape(acuan)}\s*=\s*tombol\s*\[\s*pilihan\s*\]",
            f"simpul acuan sisipan (`{acuan}`) tidak dibaca dari "
            "`tombol[pilihan]`; penjelasannya mendarat di bawah opsi yang "
            "BUKAN ditekan orangnya")

    def test_penjelasan_hanya_datang_dari_respons_jawab(self):
        """Muatan soal tetap bersih; penjelasan dibaca dari respons jawab.

        Ini bagian keamanannya, bukan kerapian: kalau `penjelasan` ikut di
        muatan soal "supaya lebih cepat tampil", kunci jawabannya terbaca di
        tab Network sebelum orangnya menjawab. Dua asersi pertama menjaga dua
        UJUNG kontrak field itu — pembacanya mengambil dari respons jawab, dan
        muatan soal tetap bersih.

        ASERSI KETIGA MENJAGA PENGIRIMNYA, dan itu lubang yang terukur: dengan
        dua asersi pertama saja, SELURUH fitur "kenapa" bisa dihapus dari sisi
        server tanpa satu tes pun merah. Dua probe, keduanya `Ran 847, OK`:
        hapus baris `"penjelasan": s["penjelasan"],` dari `sesi.jawab()`, dan
        paksa `"penjelasan": ""` di `_acak_soal`. Yang membuatnya senyap justru
        kemurahan hati klien: `r.penjelasan || "Jawaban yang benar disorot
        hijau."` membuat hilangnya data terasa seperti fitur yang masih hidup.

        Karena itu yang dituntut BUKAN "field-nya ada" melainkan ISINYA sama
        dengan data kurikulum untuk soal yang sama, dilacak lewat
        `obj.soal[nomor]["asli"]` (posisi ASLI sebelum pengacakan) ->
        `lang["quizzes"][indeks]["questions"][asli]["explanation"]`.
        `assertIn`/`assertIsNotNone` tidak sah di sini: keduanya hijau untuk
        string kosong, dan string kosong adalah keadaan yang sama-sama membuat
        kotak penjelasan berdiri tanpa isi. Asersi non-kosong itu jujur karena
        angkanya sudah dihitung: **928 dari 928** soal punya `explanation`.

        LAPANGAN BUKTINYA, diukur dengan satu proses per mutasi:
          MELANGGAR, merah  : baris pengirim di `sesi.jawab()` dihapus;
              `_acak_soal` memaksa `""`.
          MENYUSUN ULANG, hijau : baris pengirim dirapikan spasinya; field
              baru yang tidak berhubungan ditambahkan ke respons jawab.
        """
        jawab = self._wilayah("jawab", self._wilayah("layarKuis"))
        self.assertRegex(
            jawab, r"r\s*\.\s*penjelasan",
            "klien tidak lagi membaca penjelasan dari respons `/api/kuis/jawab`")
        # DUA JALUR, bukan satu. `sesi.buat()` punya cabang `acak=False` yang
        # TIDAK melewati `_acak_soal` sama sekali, dan pelajar sampai ke sana
        # lewat saklar yang nyata: `layar-kerja.js` membaca
        # `ctx.awal.konfigurasi.acak_bawaan` dan `api.py` meneruskannya. Menguji
        # satu jalur saja membuat jalur yang lain bisa dikosongkan tanpa satu
        # tes pun merah — itu terukur, bukan dikhawatirkan.
        #
        # `kuis_mulai`/`kuis_jawab`/`sesi.rekap` tidak menulis apa pun (keduanya
        # yang pertama hanya membaca konfigurasi dan daftar soal salah; sesinya
        # di memori), jadi kelas ini tidak perlu mengalihkan berkas. Yang
        # DILARANG di sini `api.kuis_selesai`: ia menulis progres sungguhan
        # lewat `record_quiz_score`/`perbarui_soal_salah`, dan kelas ini tidak
        # mengalihkan `~/.belajar_ngoding_progress.json` milik pemilik mesin.
        from main import LANGUAGES
        lang = next(b for b in LANGUAGES if b["key"] == "java")
        soal_kur = lang["quizzes"][0]["questions"]
        for acak in (True, False):
            jalur = f"acak={acak}"
            s = api.kuis_mulai({"key": "java", "indeks": 0, "acak": acak})
            for soal in s["soal"]:
                self.assertEqual(
                    set(soal), {"nomor", "q", "options"},
                    f"[{jalur}] muatan soal membawa field di luar "
                    f"{{nomor, q, options}}; yang terbaca: {sorted(set(soal))}. "
                    "Penjelasan dan kunci jawaban hanya boleh datang SESUDAH "
                    "orangnya menjawab")

            obj = sesi.ambil(s["sesi"])
            for nomor in range(len(s["soal"])):
                asli = obj.soal[nomor]["asli"]
                kur = soal_kur[asli]["explanation"]
                self.assertTrue(
                    kur.strip(),
                    f"[{jalur}] soal asli #{asli} tidak punya `explanation` di "
                    "kurikulum; 928 dari 928 punya, jadi ini perubahan data — "
                    "laporkan, jangan karang isinya")
                r = api.kuis_jawab({"sesi": s["sesi"], "nomor": nomor,
                                    "pilihan": 0})
                self.assertEqual(
                    r.get("penjelasan"), kur,
                    f"[{jalur}] penjelasan yang DIKIRIM untuk soal {nomor} "
                    f"(asli #{asli}) tidak sama dengan data kurikulumnya. "
                    "Klien punya teks cadangan, jadi hilangnya data ini tidak "
                    "akan terlihat di layar — kotaknya tetap berdiri, isinya "
                    "yang lenyap")

            # EXIT KEDUA: layar tinjau membaca `rincian` dari `rekap()`, bukan
            # dari respons jawab. Yang ini lebih mahal kalau bocor: blok
            # "Kenapa" ditulis `d.penjelasan ? … : null` dan `tambah()`
            # menyaring string kosong, jadi hilangnya field tidak meninggalkan
            # kotak kosong — bloknya lenyap seluruhnya, nol gejala.
            for d in sesi.rekap(s["sesi"])["rincian"]:
                self.assertEqual(
                    d.get("penjelasan"), soal_kur[d["asli"]]["explanation"],
                    f"[{jalur}] penjelasan di `rincian` untuk soal asli "
                    f"#{d['asli']} tidak sama dengan data kurikulumnya; blok "
                    "\"Kenapa\" di layar tinjau akan lenyap tanpa gejala")

class TestMesinPerayaan(unittest.TestCase):
    """Mesin upacara: penanda sekali-seumur, dan cabang `capai` yang bersyarat.

    Pemicunya bukan milik sesi ini -- ia tinggal di jalur hijau pertama
    `layar-kerja.js` dan ditagih ke S08. Justru karena itu mesinnya butuh tes:
    yang akan memasangnya adalah sesi lain yang tidak akan membaca berkas ini
    dengan hati-hati, dan satu-satunya hal yang akan menegurnya adalah tes.
    """

    @staticmethod
    def _akar():
        return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    @unittest.skipUnless(shutil.which("node"), "butuh node untuk menguji inti.js")
    def test_penanda_upacara_hanya_sekali_dan_di_localstorage(self):
        """`sudahPernah()` menjawab false sekali, lalu true selamanya.

        Penandanya di localStorage dan BUKAN di berkas progres: berkas itu
        catatan belajar orang sungguhan, dan "sudah pernah melihat animasi"
        bukan capaian belajar. Akibat yang disengaja: membersihkan data situs
        membuat perayaannya TERLEWAT -- bukan dobel, bukan galat, dan nol XP
        yang hilang.
        """
        jalur = os.path.join(self._akar(), "webapp", "statik", "js", "inti.js")
        with tempfile.TemporaryDirectory() as d:
            js = os.path.join(d, "uji-inti.mjs")
            with open(js, "w", encoding="utf-8") as f:
                f.write(_SKRIP_INTI_NODE)
            jalan = subprocess.run(
                ["node", js, jalur, "1790625600000"], capture_output=True,
                text=True, timeout=60,
                env=dict(os.environ, TZ="Asia/Makassar"))
        self.assertEqual(jalan.returncode, 0, jalan.stderr[-1200:])
        r = json.loads(jalan.stdout)

        self.assertIs(r["upacaraPertama"], False,
                      "panggilan pertama harus melaporkan BELUM pernah")
        self.assertIs(r["upacaraKedua"], True,
                      "panggilan kedua masih melaporkan belum pernah; penandanya "
                      "tidak benar-benar tertulis atau tidak terbaca kembali")
        self.assertIs(r["upacaraLain"], False,
                      "penanda satu upacara ikut menutup upacara lain")
        self.assertEqual(r["kunciTersimpan"],
                         ["belajar.upacara.hijauPertama", "belajar.upacara.upacaraLain"],
                         "kunci localStorage bukan `belajar.upacara.<kunci>`")

    def test_cabang_capai_bersyarat_dua_hal_dan_pemanggil_lama_tidak_mengoper(self):
        """Denyut + percik hanya untuk pemanggil yang menyerahkan bendanya.

        Dua syarat, bukan satu. `tingkat === "capai"` saja akan menyalakannya
        untuk keempat pemanggil hari ini -- perubahan perilaku yang tidak
        diminta siapa pun. `dari` saja akan menyalakannya juga saat naik level,
        di atas `tampilNaikLevel()` yang sudah punya partikelnya sendiri.
        """
        akar = self._akar()
        with open(os.path.join(akar, "webapp", "statik", "js", "inti.js"),
                  encoding="utf-8") as f:
            inti = f.read()

        syarat = re.search(r"if\s*\(([^)]*)\)\s*\{\s*\n\s*denyut\(", inti)
        self.assertIsNotNone(syarat, "cabang denyut+percik di rayakan() hilang")
        isi = syarat.group(1)
        self.assertIn('tingkat === "capai"', isi,
                      "cabang tidak lagi dibatasi tingkat `capai`")
        self.assertRegex(isi, r"&&\s*dari\b|dari\s*&&",
                         "cabang tidak lagi menuntut pemanggil menyerahkan `dari`; "
                         "keempat pemanggil lama akan ikut menyalakannya")

        # `dari` harus benar-benar sampai ke sana lewat parameter, bukan ditebak.
        self.assertRegex(inti, r"export function rayakan\([^)]*dari\s*=\s*null",
                         "`dari` bukan lagi parameter opsional rayakan()")

        # Tidak satu pun pemanggil lama yang mengoper `dari`.
        pemanggil = []
        for nama in ("layar-belajar.js", "layar-kerja.js", "layar-lain.js"):
            jalur = os.path.join(akar, "webapp", "statik", "js", nama)
            if not os.path.exists(jalur):
                continue
            with open(jalur, encoding="utf-8") as f:
                isi_berkas = f.read()
            for m in re.finditer(r"(?<!tingkat)(?<![A-Za-z])rayakan\(", isi_berkas):
                # potong sampai penutup kurungnya, dengan hitung kurung
                i, dalam = m.end() - 1, 0
                for j in range(i, len(isi_berkas)):
                    if isi_berkas[j] == "(":
                        dalam += 1
                    elif isi_berkas[j] == ")":
                        dalam -= 1
                        if dalam == 0:
                            pemanggil.append((nama, isi_berkas[m.start():j + 1]))
                            break
        PESAN_S08 = (
            "\n\n  KALAU KAMU S08 DAN BARU MEMASANG PEMICU DI JALUR HIJAU "
            "PERTAMA:\n"
            "  tes ini memang menagihmu. Yang benar dilakukan adalah "
            "MENDAFTARKAN\n"
            "  panggilan barumu di sini -- naikkan angkanya, dan tulis di "
            "komentar\n"
            "  panggilan mana yang kamu tambahkan beserta alasannya. JANGAN "
            "hapus\n"
            "  tesnya: ia satu-satunya yang menjaga tiga pemanggil lain tidak "
            "ikut\n"
            "  menyalakan denyut+percik yang tidak diminta siapa pun.")

        self.assertEqual(
            len(pemanggil), 4,
            f"jumlah pemanggil rayakan() berubah: {pemanggil}" + PESAN_S08)
        for nama, panggilan in pemanggil:
            self.assertNotRegex(
                panggilan, r"\bdari\b",
                f"{nama} mengoper `dari` ke rayakan(); itu perubahan perilaku "
                "pemanggil lama." + PESAN_S08)


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
    regresi kedua lolos. Sekarang KELIMA properti yang bisa diredam diperiksa:
    animation, transform, translate, scale, transition.

    `scale` masuk daftar sejak animasi masuk sel bara dipindah ke properti itu
    (S04-B). Ia belum punya satu pun pagar `[data-gerak]` hari ini -- dan itu
    benar, karena `scale` di sana ditulis WAAPI, bukan CSS, jadi pagar CSS
    untuknya justru akan jadi aturan mati. Yang dijaga daftar ini adalah
    kemungkinan berikutnya: begitu seseorang menulis `scale: none` di bawah
    `[data-gerak]`, tes ini menagih buktinya.
    """

    PROPERTI = ("animation", "transform", "translate", "scale", "transition")

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
                for pr in ("transform", "translate", "scale"):
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
