"""Pagar Peta Karier: data yang jujur, dan kesiapan yang cuma punya satu definisi.

* Setiap rujukan di data/karier.py wajib menunjuk sesuatu yang ADA: kurikulum
  di LANGUAGES, profesi lain, keahlian di KEAHLIAN, rumpun di RUMPUN. Rujukan
  yatim tidak menimbulkan error di mana pun -- yang terjadi cuma kesiapan yang
  diam-diam salah hitung atau tombol yang tidak membuka apa-apa.
* Gaji tanpa sumber yang bisa dibuka tidak boleh ada.
* Kesiapan dihitung dari `progress.statistik_bahasa`, angka yang sama dengan
  "x% selesai" di halaman bahasa. Tesnya menyemai progres ke berkas sementara.
"""

import itertools
import os
import tempfile
import unittest

from data import karier as data_karier
from inti.kurikulum import LANGUAGES
from pelajar import karier
from pelajar import progress

KUNCI_KURIKULUM = {l["key"] for l in LANGUAGES}
ROADMAP = "/home/vi/folder_materi/materi-belajar/09-developer-roadmap/roadmaps"


class TestDataKarier(unittest.TestCase):

    def test_id_unik_dan_rumpun_dikenal(self):
        ids = [p["id"] for p in data_karier.PROFESI]
        self.assertEqual(len(ids), len(set(ids)))
        rumpun = {r["id"] for r in data_karier.RUMPUN}
        for p in data_karier.PROFESI:
            with self.subTest(profesi=p["id"]):
                self.assertIn(p["rumpun"], rumpun)
                self.assertIn(p["jenjang"], data_karier.JENJANG)

    def test_tiap_rumpun_berisi(self):
        for r in data_karier.RUMPUN:
            with self.subTest(rumpun=r["id"]):
                self.assertTrue([p for p in data_karier.PROFESI if p["rumpun"] == r["id"]])

    def test_rujukan_tidak_yatim(self):
        for p in data_karier.PROFESI:
            with self.subTest(profesi=p["id"]):
                self.assertTrue(p["bekal"], "profesi tanpa bekal selalu 0% siap")
                for grup in p["bekal"]:
                    self.assertTrue(grup)
                    self.assertTrue(set(grup) <= KUNCI_KURIKULUM, grup)
                self.assertTrue(set(p["pelengkap"]) <= KUNCI_KURIKULUM)
                self.assertTrue(set(p["keahlian"]) <= set(data_karier.KEAHLIAN))
                for q in p["naik"] + p["dekat"]:
                    self.assertIn(q, karier.PER_ID)
                    self.assertNotEqual(q, p["id"])

    def test_isi_wajib_terisi(self):
        for p in data_karier.PROFESI:
            with self.subTest(profesi=p["id"]):
                for kunci in ("ringkas", "masuk"):
                    self.assertGreater(len(p[kunci]), 30)
                self.assertGreaterEqual(len(p["harian"]), 3)
                self.assertGreaterEqual(len(p["proyek"]), 2)
                self.assertTrue(p["alat"])
                self.assertTrue(p["sumber"])
                for s in p["sertifikasi"]:
                    self.assertTrue(s["nama"] and s["penerbit"])
                    self.assertIn(s["tingkat"], data_karier.JENJANG)

    def test_gaji_selalu_bersumber(self):
        ada = 0
        for p in data_karier.PROFESI:
            g = p.get("gaji")
            if not g:
                continue
            ada += 1
            with self.subTest(profesi=p["id"]):
                self.assertTrue(g["url"].startswith("https://"))
                self.assertTrue(g["sumber"])
                self.assertRegex(g["diperiksa"], r"^\d{4}-\d{2}-\d{2}$")
                self.assertRegex(g["rentang"], r"^Rp [\d,]+ juta - Rp [\d,]+ juta per bulan$")
        self.assertGreater(ada, 0, "tabel GAJI tidak lagi tergabung ke PROFESI")
        self.assertTrue(set(data_karier.GAJI) <= set(karier.PER_ID))

    @unittest.skipUnless(os.path.isdir(ROADMAP), "folder roadmap sumber tidak ada")
    def test_slug_roadmap_benar_benar_ada(self):
        ada = set(os.listdir(ROADMAP))
        for p in data_karier.PROFESI:
            for slug in p["peta"]:
                with self.subTest(profesi=p["id"], slug=slug):
                    self.assertIn(slug, ada)

    def test_bobot_kuis_menunjuk_keahlian_yang_ada(self):
        for soal in data_karier.KUIS:
            self.assertEqual(len(soal["opsi"]), 4)
            for o in soal["opsi"]:
                self.assertTrue(set(o["bobot"]) <= set(data_karier.KEAHLIAN), o["bobot"])


class TestMesin(unittest.TestCase):

    def test_setiap_profesi_bisa_jadi_pemenang_kuis(self):
        """Profesi yang mustahil menang kuis adalah profesi yang tidak pernah
        disarankan ke siapa pun. Disapu atas semua kombinasi jawaban."""
        menang = set()
        for pilihan in itertools.product(range(4), repeat=len(data_karier.KUIS)):
            menang.add(karier.skor_kuis(list(pilihan))[0]["id"])
        self.assertEqual(menang, set(karier.PER_ID))

    def test_jalur_mengikuti_sisi_dan_deterministik(self):
        sisi = {tuple(sorted((s["a"], s["b"]))) for s in karier.sisi()}
        for dari in karier.PER_ID:
            for ke in karier.PER_ID:
                langkah = karier.jalur(dari, ke)
                with self.subTest(dari=dari, ke=ke):
                    self.assertIsNotNone(langkah, "graf profesi terputus")
                    self.assertEqual(langkah[0], dari)
                    self.assertEqual(langkah[-1], ke)
                    for a, b in zip(langkah, langkah[1:]):
                        self.assertIn(tuple(sorted((a, b))), sisi)
                    self.assertEqual(langkah, karier.jalur(dari, ke))

    def test_kuis_menolak_indeks_di_luar_rentang(self):
        self.assertEqual(karier.skor_kuis([9, -1, None]), [])


class TestKesiapan(unittest.TestCase):
    """Progres disemai ke berkas sementara -- bukan progres pemilik."""

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "progress.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")

    def tearDown(self):
        progress.PROGRESS_FILE = self._asli
        progress.PROGRESS_FILE_LAMA = self._asli_lama
        self.dir.cleanup()

    def test_profil_baru_nol_semua(self):
        siap = karier.semua_kesiapan(LANGUAGES, progress.load_progress())
        self.assertEqual(set(siap.values()), {0.0})

    def test_kesiapan_rata_rata_kelompok_dari_angka_halaman_bahasa(self):
        html = next(l for l in LANGUAGES if l["key"] == "html")
        for m in html["materials"]:
            progress.record_material_read("html_materi", m["title"])
        data = progress.load_progress()
        persen_html = progress.statistik_bahasa(
            data, "html", len(html["materials"]), len(html["quizzes"]),
            len(html["exercises"]))["persen"]
        self.assertGreater(persen_html, 0)
        fe = karier.PER_ID["frontend-developer"]
        k = karier.kesiapan(fe, karier.persen_kurikulum(LANGUAGES, data))
        self.assertAlmostEqual(k["persen"], persen_html / len(fe["bekal"]))

    def test_kelompok_salah_satu_memakai_yang_terbaik(self):
        java = next(l for l in LANGUAGES if l["key"] == "java")
        progress.record_material_read("java_materi", java["materials"][0]["title"])
        persen = karier.persen_kurikulum(LANGUAGES, progress.load_progress())
        be = karier.PER_ID["backend-developer"]
        k = karier.kesiapan(be, persen)
        self.assertEqual(k["kelompok"][0]["wakil"], "java")
        self.assertEqual(k["kelompok"][0]["persen"], persen["java"])


class TestKuisAlasan(unittest.TestCase):
    """`skor_kuis` menjelaskan JAWABAN MANA yang mendorong tiap profesi.

    Layar kuis menampilkan alasan itu dengan kata-kata pemilihnya sendiri
    ("Soal 1: Tampilan yang dilihat..."), jadi ia harus menjelaskan SELURUH
    skor: alasan yang cuma sebagian membuat orang percaya pada penjelasan yang
    tidak sama dengan penghitungnya.
    """

    PILIHAN = [None, 0, 1, 2, 3]

    def _bobot(self, pilihan):
        """Bobot keahlian tiap soal yang dijawab, dihitung ulang dari KUIS
        tanpa memanggil `skor_kuis`."""
        return {n: data_karier.KUIS[n]["opsi"][i]["bobot"]
                for n, i in enumerate(pilihan) if i is not None}

    def test_alasan_menjelaskan_seluruh_skor_di_semua_kombinasi(self):
        enam = len(data_karier.KUIS)
        for pilihan in itertools.product(self.PILIHAN, repeat=enam):
            terpilih = self._bobot(pilihan)
            for h in karier.skor_kuis(list(pilihan)):
                ada = karier.PER_ID[h["id"]]["keahlian"]
                self.assertTrue(h["dari"], (pilihan, h["id"]))
                nomor = [d["soal"] for d in h["dari"]]
                self.assertEqual(nomor, sorted(set(nomor)), (pilihan, h["id"]))
                for d in h["dari"]:
                    self.assertIn(d["soal"], terpilih, "soal yang dilewati disebut")
                    opsi = terpilih[d["soal"]]
                    self.assertTrue(d["keahlian"])
                    for k in d["keahlian"]:
                        self.assertIn(k, ada)
                        self.assertTrue(opsi.get(k), "keahlian tanpa bobot dari opsinya")
                    bobotnya = [opsi[k] for k in d["keahlian"]]
                    self.assertEqual(bobotnya, sorted(bobotnya, reverse=True))
                dari = sum(terpilih[d["soal"]][k] for d in h["dari"] for k in d["keahlian"])
                cocok = sum(o.get(k, 0) for o in terpilih.values() for k in h["cocok"])
                self.assertEqual(dari, cocok, (pilihan, h["id"]))
                self.assertEqual(h["skor"], round(dari / len(ada) ** 0.5, 3))

    def test_soal_yang_dilewati_tidak_pernah_disebut(self):
        for h in karier.skor_kuis([None, 1, None, 2, None, None]):
            self.assertLessEqual({d["soal"] for d in h["dari"]}, {1, 3})

    def test_endpoint_meneruskan_alasan(self):
        from webapp import api
        hasil = api.karier_kuis({"pilihan": "0,1,,0"})["hasil"]
        self.assertEqual(len(hasil), 3)
        for h in hasil:
            self.assertIsInstance(h["dari"], list)
            self.assertTrue(all(isinstance(d["soal"], int) and isinstance(d["keahlian"], list)
                                for d in h["dari"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
