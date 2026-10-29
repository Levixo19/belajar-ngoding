"""Judul bagian: tiap prosa panjang punya penanda, dan judulnya tidak berbau tempelan.

Audit 2026-10-29 menemukan 612 bagian prosa lebih dari 150 kata yang berdiri tanpa satu
pun judul di tengah halaman, dan 37 judul yang sudah ada berhuruf kapital penekanan
("pojok KIRI ATAS", "kapan async TIDAK perlu") atau memakai em dash. `alat/periksa_gaya.py`
dulu hanya membaca badan materi, jadi keduanya tidak pernah terhitung.

Pagar yang dijaga di sini:
  * tidak ada bagian prosa (bukan bagian pertama) sedikitnya 150 kata tanpa judul;
  * judul bagian tidak berhuruf kapital penekanan, ber-dash, ber-emoji, bertempelan, atau kembar
    di dalam satu materi;
  * gerbang `alat/tambah_judul.py` sendiri bisa merah (dan penyisipannya tidak menyentuh apa
    pun selain field `heading`).
Rumusannya ada di AGENTS.md, bagian "Lembar baca".
"""

import ast
import os
import sys
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(AKAR, "alat"))
sys.path.insert(0, AKAR)

import tambah_judul  # noqa: E402
from inti.kurikulum import LANGUAGES  # noqa: E402
from periksa_gaya import keluhan_judul_bagian  # noqa: E402


class TestSetiapProsaPanjangBerjudul(unittest.TestCase):
    def test_tidak_ada_bagian_prosa_panjang_tanpa_judul(self):
        sisa = []
        for l in LANGUAGES:
            for m in l["materials"]:
                for i, s in enumerate(m["sections"]):
                    if i > 0 and not s.get("heading") and s.get("body") and tambah_judul.kata_body(s) >= tambah_judul.MINIMAL_KATA:
                        sisa.append((l["key"], m["title"], i, tambah_judul.kata_body(s)))
        self.assertEqual(sisa, [], "bagian prosa panjang tanpa judul; beri judul lewat "
                         "`python3 alat/tambah_judul.py calon <kurikulum> naskah.txt` lalu `terap`")


class TestJudulBagianBersih(unittest.TestCase):
    def test_judul_bagian_lolos_pemeriksa_gaya(self):
        self.assertEqual(keluhan_judul_bagian(), [])

    def test_tidak_ada_judul_kembar_di_satu_materi(self):
        kembar = []
        for l in LANGUAGES:
            for m in l["materials"]:
                lihat = {}
                for i, s in enumerate(m["sections"]):
                    h = s.get("heading")
                    if h and h.lower() in lihat:
                        kembar.append((l["key"], m["title"], lihat[h.lower()], i, h))
                    if h:
                        lihat[h.lower()] = i
        self.assertEqual(kembar, [])


class TestGerbangTambahJudul(unittest.TestCase):
    def keluhan(self, h, sudah=()):
        return tambah_judul.keluhan_judul(h, "3. Struktur Dokumen", set(sudah))

    def test_judul_baik_lolos(self):
        for h in ("Isi head, satu per satu", "Kenapa tag harus ditutup?", "Cascade dan spesifisitas pemilih",
                  "Tipe size_t dan bedanya dengan int", "<head> dan <body> tidak boleh tertukar"):
            self.assertEqual(self.keluhan(h), [], h)

    def test_setiap_pelanggaran_ketahuan(self):
        kasus = {
            "Penjelasan": "terlalu umum",
            "Head": "kata",
            "Menyelami isi head": "tempelan",
            "Pojok KIRI ATAS": "kapital",
            "Cara Kerja Tag Penutup Di HTML": "Title Case",
            "head — isi halaman": "dash",
            "isi head dan body.": "diakhiri",
            "isi head dan body": "kapital",
            "Struktur dokumen": "sama dengan judul materi",
            "Judul yang kepanjangan sampai melewati lima puluh dua huruf sungguhan": "panjang",
        }
        for h, kata in kasus.items():
            hasil = " ".join(self.keluhan(h))
            self.assertTrue(kata.lower() in hasil.lower(), f"{h!r} tidak ditolak karena {kata!r}: {hasil!r}")
        self.assertIn("kembar", " ".join(self.keluhan("Isi head, satu per satu", sudah={"isi head, satu per satu"})))


class TestPenyisipanJudul(unittest.TestCase):
    SUMBER = (
        "X_MATERIALS = [\n"
        "    {\n"
        '        "title": "1. Satu",\n'
        '        "sections": [\n'
        "            {\n"
        '                "body": ["pembuka"]\n'
        "            },\n"
        "            {\n"
        '                "body": ["isi panjang", "lagi"]\n'
        "            },\n"
        '            {"body": ["satu baris"], "code": "x = 1"},\n'
        "        ],\n"
        "    },\n"
        "]\n"
    )

    def muat(self, teks):
        ruang = {}
        exec(compile(teks, "x", "exec"), ruang)
        return ruang["X_MATERIALS"]

    def test_hanya_field_heading_yang_bertambah(self):
        sebelum = self.muat(self.SUMBER)
        baru = tambah_judul.sunting(self.SUMBER, {"1. Satu": {"1": "Isi yang panjang", "2": "Contoh satu baris"}})
        ast.parse(baru)
        sesudah = self.muat(baru)
        self.assertEqual(len(sebelum[0]["sections"]), len(sesudah[0]["sections"]))
        for i, (a, b) in enumerate(zip(sebelum[0]["sections"], sesudah[0]["sections"])):
            if i == 0:
                self.assertEqual(a, b)
                continue
            self.assertEqual({k: v for k, v in b.items() if k != "heading"}, a)
        self.assertEqual(sesudah[0]["sections"][1]["heading"], "Isi yang panjang")
        self.assertEqual(sesudah[0]["sections"][2]["heading"], "Contoh satu baris")
        self.assertEqual(list(sesudah[0]["sections"][1])[0], "heading")

    def test_bagian_yang_sudah_berjudul_ditolak(self):
        sumber = self.SUMBER.replace('"body": ["isi panjang", "lagi"]', '"heading": "Ada", "body": ["isi"]')
        with self.assertRaises(SystemExit):
            tambah_judul.sunting(sumber, {"1. Satu": {"1": "Judul baru"}})


if __name__ == "__main__":
    unittest.main()
