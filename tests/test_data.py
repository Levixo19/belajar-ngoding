"""Validasi struktur seluruh konten kurikulum.

Konten ditulis tangan dalam jumlah besar, jadi kesalahan kecil seperti
index jawaban meleset atau judul kembar mudah lolos. Tes ini menangkapnya.
"""

import re
import unittest

from main import LANGUAGES
from materials import teks_polos
import runner

TINGKAT_URUT = ["Mudah", "Menengah", "Lanjut", "Sulit"]
TINGKAT_VALID = set(TINGKAT_URUT)
LEBAR_MAKS_BARIS = 100


class TestRegistryBahasa(unittest.TestCase):
    def test_setiap_bahasa_punya_field_wajib(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang.get("label")):
                for field in ("key", "label", "runner", "materials",
                              "quizzes", "exercises", "run_info"):
                    self.assertIn(field, lang)
                self.assertTrue(lang["materials"], "materi kosong")
                self.assertTrue(lang["quizzes"], "kuis kosong")
                self.assertTrue(lang["exercises"], "latihan kosong")

    def test_key_bahasa_unik(self):
        keys = [l["key"] for l in LANGUAGES]
        self.assertEqual(len(keys), len(set(keys)), f"key kembar: {keys}")

    def test_key_tidak_mengandung_pemisah(self):
        # Kunci progres berbentuk "<key>_<tipe>::<judul>". Tanda :: di dalam
        # key akan merusak parsing di navigasi._cari_objek.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertNotIn("::", lang["key"])

    def test_runner_terdaftar_di_toolchain(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertIn(lang["runner"], runner.TOOLCHAINS)


class TestMateri(unittest.TestCase):
    def test_struktur_materi(self):
        for lang in LANGUAGES:
            for m in lang["materials"]:
                with self.subTest(bahasa=lang["label"], materi=m.get("title")):
                    self.assertIsInstance(m.get("title"), str)
                    self.assertTrue(m["title"].strip())
                    self.assertIsInstance(m.get("sections"), list)
                    self.assertTrue(m["sections"], "sections kosong")

                    for s in m["sections"]:
                        self.assertTrue(
                            s.get("heading") or s.get("body") or s.get("code"),
                            "section kosong tanpa heading/body/code",
                        )
                        if "body" in s:
                            self.assertIsInstance(s["body"], list)
                            for baris in s["body"]:
                                self.assertIsInstance(baris, str)
                        if "code" in s:
                            self.assertIsInstance(s["code"], str)

    def test_judul_materi_unik_per_bahasa(self):
        # Progres disimpan dengan kunci judul, judul kembar akan bertabrakan.
        for lang in LANGUAGES:
            judul = [m["title"] for m in lang["materials"]]
            with self.subTest(bahasa=lang["label"]):
                kembar = {j for j in judul if judul.count(j) > 1}
                self.assertFalse(kembar, f"judul materi kembar: {kembar}")

    def test_baris_tidak_kelewat_panjang(self):
        for lang in LANGUAGES:
            for m in lang["materials"]:
                for s in m["sections"]:
                    for baris in s.get("body") or []:
                        with self.subTest(bahasa=lang["label"], materi=m["title"]):
                            self.assertLessEqual(
                                len(baris), LEBAR_MAKS_BARIS,
                                f"baris terlalu panjang ({len(baris)}): {baris[:60]}...",
                            )

    def test_materi_punya_isi_bermakna(self):
        for lang in LANGUAGES:
            for m in lang["materials"]:
                with self.subTest(bahasa=lang["label"], materi=m["title"]):
                    self.assertGreater(len(teks_polos(m)), 200,
                                       "materi terlalu pendek")


class TestKuis(unittest.TestCase):
    def test_struktur_kuis(self):
        for lang in LANGUAGES:
            for q in lang["quizzes"]:
                with self.subTest(bahasa=lang["label"], kuis=q.get("title")):
                    self.assertIsInstance(q.get("title"), str)
                    self.assertTrue(q["title"].strip())
                    self.assertIsInstance(q.get("questions"), list)
                    self.assertTrue(q["questions"], "kuis tanpa soal")

    def test_setiap_soal_valid(self):
        for lang in LANGUAGES:
            for q in lang["quizzes"]:
                for i, so in enumerate(q["questions"]):
                    label = f"{lang['label']} / {q['title']} / soal {i + 1}"
                    with self.subTest(soal=label):
                        self.assertIsInstance(so.get("q"), str)
                        self.assertTrue(so["q"].strip(), "pertanyaan kosong")

                        opsi = so.get("options")
                        self.assertIsInstance(opsi, list)
                        self.assertGreaterEqual(len(opsi), 2,
                                                "minimal 2 pilihan jawaban")
                        for o in opsi:
                            self.assertIsInstance(o, str)
                            self.assertTrue(o.strip(), "opsi kosong")

                        self.assertEqual(len(opsi), len(set(opsi)),
                                         "ada opsi yang kembar")

                        jawaban = so.get("answer")
                        self.assertIsInstance(jawaban, int)
                        self.assertGreaterEqual(jawaban, 0)
                        self.assertLess(jawaban, len(opsi),
                                        "index jawaban di luar jangkauan opsi")

                        self.assertIsInstance(so.get("explanation"), str)
                        self.assertTrue(so["explanation"].strip(),
                                        "penjelasan kosong")

    def test_sebaran_posisi_jawaban_merata(self):
        """Kuis yang jawabannya menumpuk di satu posisi bisa ditebak.

        Setelah dinormalisasi oleh data/normalisasi.py, tidak boleh ada satu
        posisi pun yang menampung lebih dari 40% jawaban sebuah bahasa.
        """
        for lang in LANGUAGES:
            jawaban = [s["answer"]
                       for q in lang["quizzes"]
                       for s in q["questions"]]
            with self.subTest(bahasa=lang["label"]):
                for posisi in set(jawaban):
                    porsi = jawaban.count(posisi) / len(jawaban)
                    self.assertLessEqual(
                        porsi, 0.40,
                        f"{porsi:.0%} jawaban menumpuk di posisi {posisi}",
                    )

    def test_normalisasi_menjaga_jawaban_tetap_benar(self):
        """Memutar opsi tidak boleh mengubah teks jawaban yang benar."""
        from data.normalisasi import seimbangkan_kuis

        for lang in LANGUAGES:
            asli = lang["quizzes"]
            ulang = seimbangkan_kuis(asli)
            for q_asli, q_baru in zip(asli, ulang):
                for s_asli, s_baru in zip(q_asli["questions"], q_baru["questions"]):
                    with self.subTest(bahasa=lang["label"], soal=s_asli["q"][:40]):
                        self.assertEqual(
                            s_asli["options"][s_asli["answer"]],
                            s_baru["options"][s_baru["answer"]],
                            "teks jawaban benar berubah setelah diputar",
                        )
                        self.assertCountEqual(s_asli["options"], s_baru["options"])

    def test_judul_kuis_unik_per_bahasa(self):
        for lang in LANGUAGES:
            judul = [q["title"] for q in lang["quizzes"]]
            with self.subTest(bahasa=lang["label"]):
                kembar = {j for j in judul if judul.count(j) > 1}
                self.assertFalse(kembar, f"judul kuis kembar: {kembar}")


class TestLatihan(unittest.TestCase):
    def test_struktur_latihan(self):
        for lang in LANGUAGES:
            for e in lang["exercises"]:
                with self.subTest(bahasa=lang["label"], latihan=e.get("title")):
                    self.assertIsInstance(e.get("title"), str)
                    self.assertTrue(e["title"].strip())

                    self.assertIn(e.get("difficulty"), TINGKAT_VALID)

                    self.assertIsInstance(e.get("question"), list)
                    self.assertTrue(e["question"], "soal kosong")
                    for baris in e["question"]:
                        self.assertIsInstance(baris, str)

                    self.assertIsInstance(e.get("hints"), list)
                    self.assertTrue(e["hints"], "latihan tanpa hint")

                    self.assertIsInstance(e.get("solution"), str)
                    self.assertTrue(e["solution"].strip(), "solusi kosong")

    def test_judul_latihan_unik_per_bahasa(self):
        for lang in LANGUAGES:
            judul = [e["title"] for e in lang["exercises"]]
            with self.subTest(bahasa=lang["label"]):
                kembar = {j for j in judul if judul.count(j) > 1}
                self.assertFalse(kembar, f"judul latihan kembar: {kembar}")

    def test_field_opsional_bertipe_benar(self):
        for lang in LANGUAGES:
            for e in lang["exercises"]:
                with self.subTest(bahasa=lang["label"], latihan=e["title"]):
                    if "stdin" in e:
                        self.assertIsInstance(e["stdin"], str)
                    if "stdin_list" in e:
                        self.assertIsInstance(e["stdin_list"], list)
                    if "mode" in e:
                        self.assertIn(e["mode"], {
                            "persis", "abaikan_kapital", "mengandung", "regex", "angka",
                        })
                    if "tests" in e:
                        self.assertIsInstance(e["tests"], list)
                        for t in e["tests"]:
                            self.assertIn("harapan", t)

    def test_kesulitan_menanjak(self):
        # Latihan pertama tiap bahasa harus ramah pemula.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertEqual(lang["exercises"][0]["difficulty"], "Mudah")

    def test_solusi_berinput_tidak_mencetak_prompt(self):
        """Prompt di solusi contoh membuat latihan mustahil dikerjakan benar.

        Auto-checker membandingkan output. Kalau solusi mencetak
        'Masukkan nilai: ' lebih dulu, teks itu ikut jadi bagian kunci jawaban.
        Siswa yang menulis input() polos -- yang justru lebih tepat untuk
        program yang dinilai dari output -- akan selalu dianggap salah.

        Aturannya: latihan yang membaca stdin tidak boleh mencetak apa pun
        SEBELUM pembacaan pertama. Cetakan sesudahnya sah, karena itu memang
        bagian dari jawaban -- 'Isi array: 5 10 15' bukan prompt.
        """
        pola_prompt = [
            re.compile(r"""input\(\s*["'][^"']+["']\s*\)"""),               # Python
            re.compile(r"""System\.out\.print\s*\(\s*"[^"]*"\s*\)\s*;"""),  # Java
            re.compile(r"""printf\s*\(\s*"[^"\\]*[:?]\s*"\s*\)"""),         # C / C++
            re.compile(r"""cout\s*<<\s*"[^"]*[:?]\s*\""""),                 # C++
            re.compile(r"""read\s+-p\b"""),                                 # Bash
            re.compile(r"""fmt\.Print\s*\(\s*"[^"]*[:?]\s*"\s*\)"""),       # Go
        ]
        pola_baca = re.compile(
            r"""input\(|scanf\s*\(|cin\s*>>|getline\s*\(|nextInt\(|nextLine\(|"""
            r"""nextDouble\(|fmt\.Scan|bufio\.|^\s*read\s+""",
            re.MULTILINE,
        )

        for lang in LANGUAGES:
            for e in lang["exercises"]:
                if not (e.get("stdin") or e.get("stdin_list")):
                    continue
                if e.get("auto_check") is False:
                    continue

                solusi = e["solution"]
                baca = pola_baca.search(solusi)
                # Periksa bagian sebelum pembacaan pertama saja. Kalau tidak
                # ada pembacaan sama sekali, seluruh berkas diperiksa -- itu
                # sendiri sudah janggal untuk latihan yang punya stdin.
                sebelum = solusi[: baca.start()] if baca else solusi

                with self.subTest(bahasa=lang["label"], latihan=e["title"]):
                    for pola in pola_prompt:
                        cocok = pola.search(sebelum)
                        self.assertIsNone(
                            cocok,
                            "solusi mencetak teks sebelum membaca input: "
                            f"{cocok.group(0) if cocok else ''}",
                        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
