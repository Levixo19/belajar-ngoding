"""Gambar konsep di materi (inti/visual.py) dan pelacak "Lihat jalannya" (inti/jejak.py)."""

import os
import sys
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)
sys.path.insert(0, os.path.join(AKAR, "alat"))

from inti import jejak, runner, visual  # noqa: E402
from main import LANGUAGES  # noqa: E402
import periksa_visual  # noqa: E402

# Satu contoh sah untuk tiap jenis: pagar bahwa penggambar terminal tidak
# meledak dan muat 78 kolom, walau data kurikulum belum memakai jenis itu.
CONTOH = [
    {"setelah": 0, "jenis": "variabel", "judul": "Kotak bernama",
     "isi": [["umur", "17", "int"], ["nama", "\"Ani\""]], "sorot": ["umur"]},
    {"setelah": 0, "jenis": "larik", "judul": "Indeks", "nama": "nilai",
     "isi": ["70", "85", "90"], "sorot": [2], "penunjuk": {"i": 1}, "rentang": [1, 3]},
    {"setelah": 0, "jenis": "alur", "judul": "Lulus?", "langkah": [
        {"jenis": "mulai", "teks": "mulai"},
        {"jenis": "keputusan", "teks": "nilai >= 75?", "tidak": 3},
        {"jenis": "keluaran", "teks": "Lulus", "ke": 4},
        {"jenis": "keluaran", "teks": "Belum"},
        {"jenis": "selesai", "teks": "selesai"}]},
    {"setelah": 0, "jenis": "tumpukan", "judul": "Stack", "isi": ["main()", "f(2)"],
     "operasi": "panggil f(1)"},
    {"setelah": 0, "jenis": "tumpukan", "judul": "Antre", "mode": "antrean",
     "isi": ["Ani", "Budi"]},
    {"setelah": 0, "jenis": "pohon", "judul": "DOM", "akar": {"teks": "html", "anak": [
        {"teks": "head"}, {"teks": "body", "anak": [{"teks": "h1"}]}]}},
    {"setelah": 0, "jenis": "tabel", "judul": "JOIN", "panah": "JOIN ON id", "tabel": [
        {"nama": "siswa", "kolom": ["id", "nama"], "baris": [[1, "Ani"]], "sorot_baris": [0]},
        {"kolom": ["id", "skor"], "baris": [[1, 90]], "sorot_kolom": ["skor"]}]},
    {"setelah": 0, "jenis": "urutan", "judul": "HTTP", "pelaku": ["Browser", "Server"],
     "pesan": [[0, 1, "GET /"], [1, 0, "200 OK"], [1, 1, "catat log"]]},
    {"setelah": 0, "jenis": "kotak", "judul": "Kotak", "margin": "16px",
     "border": "2px", "padding": "12px", "isi": "200 x 80"},
    {"setelah": 0, "jenis": "tata", "judul": "Flex", "mode": "flex", "arah": "row",
     "justify": "center", "item": ["A", "B"]},
    {"setelah": 0, "jenis": "tata", "judul": "Grid", "mode": "grid", "kolom": 3,
     "item": [["kepala", 3], "menu", ["isi", 2]]},
    {"setelah": 0, "jenis": "git", "judul": "Merge", "commit": [
        {"id": "A", "cabang": "main"}, {"id": "B", "induk": ["A"], "cabang": "fitur"},
        {"id": "M", "induk": ["A", "B"], "cabang": "main", "pesan": "merge"}],
     "label": {"main": "M", "fitur": "B"}, "head": "main"},
    {"setelah": 0, "jenis": "memori", "judul": "Referensi",
     "tumpukan": [["a", "@o1"], ["n", "5"]], "heap": [{"id": "o1", "isi": "[1, 2]"}]},
    {"setelah": 0, "jenis": "bit", "judul": "Biner", "angka": 13, "lebar": 8},
    {"setelah": 0, "jenis": "kurva", "judul": "Big-O", "kurva": list(visual.KURVA),
     "sorot": "n"},
]


class TestSkemaVisual(unittest.TestCase):
    def test_tiap_jenis_punya_contoh_sah(self):
        self.assertEqual({c["jenis"] for c in CONTOH}, set(visual.JENIS))
        for c in CONTOH:
            with self.subTest(jenis=c["jenis"]):
                self.assertEqual(visual.periksa(c, 1), [])

    def test_gambar_terminal_muat_78_kolom(self):
        for c in CONTOH:
            for b in visual.baris(c, 76, 1):
                self.assertLessEqual(len("  " + b), 78, (c["jenis"], b))

    def test_pemeriksa_menolak_yang_salah(self):
        salah = [
            {"setelah": 0, "jenis": "entah", "judul": "x"},
            {"setelah": 5, "jenis": "bit", "judul": "x", "angka": 1},
            {"setelah": 0, "jenis": "bit", "judul": "x", "angka": 300, "lebar": 8},
            {"setelah": 0, "jenis": "larik", "judul": "x", "isi": ["1"], "sorot": [4]},
            {"setelah": 0, "jenis": "alur", "judul": "x", "langkah": [
                {"jenis": "keputusan", "teks": "a?"}, {"jenis": "selesai", "teks": "b"}]},
            {"setelah": 0, "jenis": "git", "judul": "x",
             "commit": [{"id": "B", "induk": ["A"], "cabang": "main"}]},
            {"setelah": 0, "jenis": "variabel", "judul": "x", "isi": [["a", "1"]],
             "medan_asing": 1},
        ]
        for s in salah:
            with self.subTest(s=s):
                self.assertNotEqual(visual.periksa(s, 2), [])


class TestDataVisualKurikulum(unittest.TestCase):
    def test_semua_data_visual_sah(self):
        keluhan = []
        for lang in LANGUAGES:
            keluhan += [f"{lang['key']}: {j}: {k}"
                        for j, k in periksa_visual.keluhan_bahasa(lang)]
        self.assertEqual(keluhan, [], "\n".join(keluhan[:20]))

    def test_berkas_visual_menunjuk_kurikulum_yang_ada(self):
        kunci = {l["key"] for l in LANGUAGES}
        d = os.path.join(AKAR, "data", "visual")
        for nama in os.listdir(d):
            if nama.endswith(".py") and nama != "__init__.py":
                self.assertIn(nama[:-3], kunci, nama)


class TestVisualSampaiKeDuaAntarmuka(unittest.TestCase):
    """Gambar yang sama terbaca di web (blok) dan di terminal (baris)."""

    def setUp(self):
        self.lang = next(l for l in LANGUAGES if l["key"] == "python")
        self.m = self.lang["materials"][0]
        self.simpan = dict(visual._singgah)
        visual._singgah["python"] = {visual.judul_tanpa_nomor(self.m["title"]): [
            dict(CONTOH[0], setelah=1), dict(CONTOH[1], setelah=0)]}

    def tearDown(self):
        visual._singgah.clear()
        visual._singgah.update(self.simpan)

    def test_web_menempelkan_gambar_ke_blok_terakhir_bagiannya(self):
        from webapp import isi
        blok = isi.bagian_materi(self.m, self.lang)
        jumlah_tanpa = len(isi.bagian_materi(self.m, {**self.lang, "key": "tanpa"}))
        self.assertEqual(len(blok), jumlah_tanpa, "gambar tidak boleh jadi blok sendiri")
        gambar = [g for b in blok for g in b.get("visual", [])]
        self.assertEqual([g["nomor"] for g in gambar], [1, 2])
        self.assertEqual([g["jenis"] for g in gambar], ["larik", "variabel"])

    def test_terminal_menampilkan_judul_dan_label_yang_sama(self):
        import re
        from layar import materials
        teks = "\n".join(materials.baris_materi(self.m, "python", "", "python"))
        polos = re.sub(r"\x1b\[[0-9;]*m", "", teks)
        self.assertIn("Gambar 1: Indeks", polos)
        self.assertIn("Gambar 2: Kotak bernama", polos)
        self.assertIn("umur", polos)


@unittest.skipUnless(runner.tersedia("python"), "python3 tidak ada")
class TestPelacakPython(unittest.TestCase):
    def test_aliasing_terlihat_lewat_nomor_objek(self):
        r = jejak.lacak("x = [1]\ny = x\ny.append(2)\nprint(x)\n")
        self.assertIsNone(r["galat"])
        self.assertEqual(r["keluaran"], "[1, 2]\n")
        akhir = r["langkah"][-1]["tumpukan"][0]["isi"]
        self.assertEqual(akhir["x"]["id"], akhir["y"]["id"])
        self.assertEqual(akhir["x"]["r"], "[1, 2]")

    def test_panggilan_dan_nilai_kembali_tercatat(self):
        r = jejak.lacak("def f(a):\n    return a * 2\n\nb = f(3)\n")
        jenis = [s["p"] for s in r["langkah"]]
        self.assertIn("panggil", jenis)
        kembali = next(s for s in r["langkah"] if s["p"] == "kembali")
        self.assertEqual(kembali["nilai"]["r"], "6")
        self.assertEqual([b["nama"] for b in kembali["tumpukan"]], ["program utama", "f"])

    def test_loop_tak_berujung_dihentikan_di_batas_langkah(self):
        r = jejak.lacak("while True:\n    pass\n", maks=50)
        self.assertTrue(r["terpotong"])
        self.assertEqual(len(r["langkah"]), 50)

    def test_galat_dan_input_dijelaskan(self):
        self.assertIn("ZeroDivisionError", jejak.lacak("print(1/0)\n")["galat"])
        self.assertIn("masukan", jejak.lacak("x = input()\n")["galat"])
        r = jejak.lacak("def f(:\n")
        self.assertTrue(r["galat"].startswith("SyntaxError"))
        self.assertEqual(r["baris_galat"], 1)

    def test_api_menolak_bahasa_lain(self):
        from webapp import api
        with self.assertRaises(api.Galat):
            api.jejak({"bahasa": "java", "kode": "x"})
        self.assertEqual(api.jejak({"kode": "a = 1\n"})["keluaran"], "")

    def test_rekaman_tidak_rusak_oleh_surrogate(self):
        r = jejak.lacak('print("\\ud800")\n')
        self.assertIsNone(r["galat"])
        self.assertEqual(r["keluaran"], "\ud800\n")

    def test_except_pelajar_tidak_menelan_batas_langkah(self):
        """Program dihentikan di batas; keluarannya cocok dengan langkahnya."""
        kode = ("def f():\n    try:\n        while True: pass\n    except:\n"
                "        print('tertangkap')\nf()\nprint('akhir')\n")
        r = jejak.lacak(kode, maks=60)
        self.assertTrue(r["terpotong"])
        self.assertFalse(r["timeout"])
        self.assertEqual(r["keluaran"], "")

    def test_nilai_besar_diringkas_tanpa_timeout(self):
        r = jejak.lacak("data = list(range(2000000))\nfor i in range(100):\n    x = i\n", maks=120)
        self.assertFalse(r["timeout"])
        self.assertLessEqual(len(r["langkah"][-1]["tumpukan"][0]["isi"]["data"]["r"]), 80)


class TestApiLangit(unittest.TestCase):
    """Peta langit memakai status dan penguncian dari jalur halaman bahasa."""

    def setUp(self):
        import tempfile
        from pelajar import progress, konfigurasi
        self.d = tempfile.mkdtemp()
        self.lama = (progress.PROGRESS_FILE, konfigurasi.BERKAS)
        progress.PROGRESS_FILE = os.path.join(self.d, "p.json")
        konfigurasi.BERKAS = os.path.join(self.d, "k.json")
        konfigurasi.lupakan_cache()

    def tearDown(self):
        from pelajar import progress, konfigurasi
        progress.PROGRESS_FILE, konfigurasi.BERKAS = self.lama
        konfigurasi.lupakan_cache()

    def test_bentuk_dan_bekal_berkelompok(self):
        from webapp import api
        r = api.langit({})
        self.assertEqual(len(r["bahasa"]), len(LANGUAGES))
        py = next(b for b in r["bahasa"] if b["key"] == "python")
        lang = next(l for l in LANGUAGES if l["key"] == "python")
        self.assertEqual(len(py["materi"]), len(lang["materials"]))
        self.assertEqual({m["status"] for m in py["materi"]}, {"baru"})
        self.assertEqual(sum(len(b["materi"]) for b in py["bab"]), len(lang["materials"]))
        # Bekal dikirim berkelompok ("salah satu dari"), bukan dipipihkan.
        for p in r["profesi"]:
            self.assertTrue(all(isinstance(g, list) for g in p["bekal"]), p["id"])


if __name__ == "__main__":
    unittest.main()
