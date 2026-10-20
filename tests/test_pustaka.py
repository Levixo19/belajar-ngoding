"""Pagar Pustaka: datanya sah, berlisensi jelas, dan pencariannya jujur.

Yang dijaga di sini terbagi tiga:

  * BENTUK data: tiap entri punya judul, alamat http(s), jenis dan bahasa
    yang dikenal, dan tiap berkas sumber membawa lisensi serta atribusinya.
  * LISENSI: sumber yang hanya boleh DITAUTKAN (repo tanpa lisensi,
    roadmap.sh, freeCodeCamp) tidak boleh diam-diam berisi salinan daftar
    orang lain. Ini pagar hukum, bukan kosmetik: CC BY dan MIT mewajibkan
    atribusi, dan repo tanpa lisensi tidak boleh disalin sama sekali.
  * PENCARIAN: cacah segi cocok dengan hasilnya, halaman tidak tumpang-tindih,
    dan yang berbahasa Indonesia benar-benar tampil lebih dulu.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import urlsplit

from inti import pustaka
from inti.kurikulum import LANGUAGES

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MATERI = "/home/vi/folder_materi/materi-belajar"

# Sumber yang isinya cuma boleh ditautkan, beserta domain yang boleh dituju.
HANYA_TAUTAN = {
    "peta": {"roadmap.sh"},
    "fcc": {"www.freecodecamp.org"},
    "rujukan": {"github.com"},
}


def _berkas_sumber():
    for nama in sorted(os.listdir(pustaka.FOLDER)):
        if nama.endswith(".json"):
            with open(os.path.join(pustaka.FOLDER, nama), encoding="utf-8") as f:
                yield nama, json.load(f)


class TestBentukData(unittest.TestCase):

    def test_ada_isinya(self):
        self.assertGreater(pustaka.total(), 5000, "data Pustaka kosong atau terpotong")

    def test_tiap_sumber_membawa_lisensi_dan_atribusi(self):
        for nama, isi in _berkas_sumber():
            with self.subTest(berkas=nama):
                s = isi["sumber"]
                self.assertEqual(s["kunci"] + ".json", nama)
                self.assertTrue(s["lisensi"].strip())
                self.assertGreater(len(s["atribusi"]), 20,
                                   "atribusi wajib ada: CC BY dan MIT memintanya")

    def test_tiap_entri_berbentuk_benar(self):
        for nama, isi in _berkas_sumber():
            for i, e in enumerate(isi["entri"]):
                with self.subTest(berkas=nama, entri=i):
                    self.assertTrue(e["judul"].strip())
                    u = urlsplit(e["url"])
                    self.assertIn(u.scheme, ("http", "https"),
                                  "skema selain http(s) tidak boleh jadi tautan")
                    self.assertTrue(u.netloc)
                    self.assertIn(e["jenis"], pustaka.JENIS)
                    self.assertIn(e["bahasa"], pustaka.BAHASA)
                    self.assertIsInstance(e["topik"], list)

    def test_tidak_ada_url_kembar_dalam_satu_sumber(self):
        for nama, isi in _berkas_sumber():
            with self.subTest(berkas=nama):
                urls = [e["url"].rstrip("/").lower() for e in isi["entri"]]
                kembar = {u for u in urls if urls.count(u) > 1}
                self.assertFalse(kembar)

    def test_tidak_ada_sisa_markdown_di_judul(self):
        for nama, isi in _berkas_sumber():
            for e in isi["entri"]:
                with self.subTest(berkas=nama, judul=e["judul"][:40]):
                    self.assertNotIn("**", e["judul"])
                    self.assertNotIn("](", e["judul"])
                    self.assertNotIn("`", e["judul"])

    def test_setiap_kurikulum_punya_bacaan(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["key"]):
                self.assertGreater(pustaka.ringkasan_kurikulum(lang["key"])["total"], 0,
                                   "kurikulum tanpa satu pun bacaan: periksa "
                                   "TOPIK_KURIKULUM di inti/pustaka.py")

    def test_pemetaan_hanya_menunjuk_kurikulum_yang_ada(self):
        kunci = {l["key"] for l in LANGUAGES}
        for tabel in (pustaka.TOPIK_KURIKULUM, pustaka.SUMBER_KURIKULUM,
                      pustaka.PETA_KURIKULUM):
            for asal, tujuan in tabel.items():
                with self.subTest(asal=asal):
                    self.assertTrue(set(tujuan) <= kunci, tujuan)


class TestLisensi(unittest.TestCase):

    def test_sumber_hanya_tautan_tidak_menyalin_daftar_orang_lain(self):
        for nama, isi in _berkas_sumber():
            kunci = isi["sumber"]["kunci"]
            if kunci not in HANYA_TAUTAN:
                continue
            for e in isi["entri"]:
                with self.subTest(sumber=kunci, url=e["url"]):
                    self.assertIn(urlsplit(e["url"]).netloc, HANYA_TAUTAN[kunci])
        rujukan = {e["url"] for _, isi in _berkas_sumber()
                   if isi["sumber"]["kunci"] == "rujukan" for e in isi["entri"]}
        self.assertEqual(len(rujukan), 2,
                         "repo tanpa lisensi cuma boleh dirujuk lewat tautan ke "
                         "repo itu sendiri, satu entri masing-masing")

    def test_turunan_cc_by_sa_berlisensi_sama(self):
        isi = dict(_berkas_sumber())["ciu.json"]
        self.assertEqual(isi["sumber"]["lisensi"], "CC BY-SA 4.0")
        self.assertIn("CC BY-SA 4.0", isi["sumber"]["atribusi"])

    def test_bahasa_selain_indonesia_dan_inggris_tidak_dipanen(self):
        for _, isi in _berkas_sumber():
            for e in isi["entri"]:
                self.assertIn(e["bahasa"], ("id", "en"))


class TestPencarian(unittest.TestCase):

    def test_segi_jujur_terhadap_hasil(self):
        r = pustaka.cari("", kurikulum="python")
        self.assertEqual(sum(r["segi"]["jenis"].values()), r["total"],
                         "cacah tombol jenis tidak sama dengan jumlah hasil")
        self.assertEqual(sum(r["segi"]["bahasa"].values()), r["total"])

    def test_penyaring_benar_benar_menyaring(self):
        r = pustaka.cari("", kurikulum="git", jenis="buku", per_halaman=200)
        self.assertTrue(r["hasil"])
        for e in r["hasil"]:
            self.assertIn("git", e["kurikulum"])
            self.assertEqual(e["jenis"], "buku")

    def test_indonesia_lebih_dulu(self):
        r = pustaka.cari("", kurikulum="python", per_halaman=200)
        bahasa = [e["bahasa"] for e in r["hasil"]]
        self.assertIn("id", bahasa)
        pertama_en = bahasa.index("en")
        self.assertNotIn("id", bahasa[pertama_en:],
                         "entri berbahasa Indonesia tertimbun di bawah yang Inggris")

    def test_halaman_tidak_tumpang_tindih(self):
        a = pustaka.cari("", halaman=1, per_halaman=30)
        b = pustaka.cari("", halaman=2, per_halaman=30)
        self.assertFalse({e["id"] for e in a["hasil"]} & {e["id"] for e in b["hasil"]})

    def test_kueri_menuntut_semua_kata(self):
        r = pustaka.cari("react hooks", per_halaman=200)
        self.assertGreater(r["total"], 0)
        for e in r["hasil"]:
            teks = (e["judul"] + " ".join(e["topik"]) + e["catatan"]).lower()
            self.assertIn("react", teks)
            self.assertIn("hooks", teks)

    def test_ringkasan_deterministik_dan_berbatas(self):
        a = pustaka.ringkasan_kurikulum("javascript")
        b = pustaka.ringkasan_kurikulum("javascript")
        self.assertEqual(a, b, "terminal dan web harus melihat pembuka yang sama")
        self.assertLessEqual(len(a["pembuka"]), 6)
        self.assertEqual(sum(j["jumlah"] for j in a["per_jenis"]), a["total"])

    def test_tidak_ada_kolom_internal_yang_bocor(self):
        r = pustaka.cari("python", per_halaman=5)
        for e in r["hasil"]:
            self.assertFalse([k for k in e if k.startswith("_")])


class TestApiPustaka(unittest.TestCase):

    def test_menolak_penyaring_yang_tidak_dikenal(self):
        from webapp import api
        for params in ({"kurikulum": "cobol"}, {"jenis": "video"},
                       {"bahasa": "jw"}, {"hal": "dua"}):
            with self.subTest(params=params):
                with self.assertRaises(api.Galat):
                    api.pustaka(params)

    def test_label_datang_dari_server(self):
        from webapp import api
        r = api.pustaka({})
        self.assertEqual(r["label"]["jenis"], pustaka.JENIS)
        self.assertEqual(set(r["label"]["kurikulum"]), {l["key"] for l in LANGUAGES})
        self.assertEqual(r["semua"], pustaka.total())


@unittest.skipUnless(os.path.isdir(MATERI), "folder materi sumber tidak ada di mesin ini")
class TestDataHasilPemanen(unittest.TestCase):
    """data/pustaka/ wajib persis hasil alat/panen_pustaka.py.

    Berkas yang disunting tangan akan tertimpa diam-diam pada panen berikutnya,
    dan perbaikan yang seharusnya masuk ke pengurai hilang tanpa jejak."""

    def test_panen_ulang_menghasilkan_berkas_yang_sama(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, os.path.join(AKAR, "alat", "panen_pustaka.py"),
                            MATERI, tmp], check=True, capture_output=True)
            for nama in sorted(os.listdir(pustaka.FOLDER)):
                with self.subTest(berkas=nama):
                    with open(os.path.join(tmp, nama), encoding="utf-8") as a, \
                         open(os.path.join(pustaka.FOLDER, nama), encoding="utf-8") as b:
                        self.assertEqual(a.read(), b.read())


class TestTautanBerskemaAman(unittest.TestCase):
    """Semua tautan Pustaka & Karier http(s). Web juga menyaringnya (urlAman di
    inti.js), tapi data yang dipanen ulang dengan skema lain sebaiknya merah
    di sini lebih dulu, bukan diam-diam jadi tautan mati."""

    def test_url_pustaka_http_atau_kosong(self):
        from inti import pustaka
        entri = pustaka._muat()["entri"]
        self.assertGreater(len(entri), 9000, "tes ini harus benar-benar menyapu Pustaka")
        for e in entri:
            for medan in ("url", "repo"):
                u = (e.get(medan) or "").strip()
                if u:
                    with self.subTest(url=u[:60]):
                        self.assertRegex(u, r"^https?://")

    def test_url_karier_http(self):
        from data.karier import PROFESI
        for p in PROFESI:
            gaji = p.get("gaji") or {}
            if isinstance(gaji, dict) and gaji.get("url"):
                self.assertRegex(gaji["url"], r"^https?://")


if __name__ == "__main__":
    unittest.main(verbosity=2)
