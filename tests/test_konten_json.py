"""Pagar `packages/konten/`: JSON wajib tetap sama dengan sumber Python.

Ekspornya sekali jalan; yang mahal justru sesudahnya. Begitu ada dua salinan
konten, keduanya bisa menyimpang tanpa satu pun error muncul: seseorang
menyunting `data/python_materials.py`, lupa mengekspor ulang, dan sisi JSON
diam-diam menyajikan materi versi lama. Tes ini menutup celah itu dengan
membandingkan keduanya setiap kali suite jalan.

Tiga hal yang dijaga, masing-masing karena pernah bisa lolos:

* Kuis disimpan MENTAH. Kalau suatu hari yang tersimpan hasil rotasi, rotasi
  kedua saat pemuatan tidak akan menimbulkan error apa pun -- opsi cuma
  bergeser, dan penjelasan soal yang menyebut posisi opsi berhenti cocok.
  Sidik SHA-256 pasca-rotasi menangkapnya.
* Kunci berbentuk angka dilarang. `JSON.parse` di V8 menata ulang kunci
  seperti "0" dan "1" ke depan, jadi objek yang memakainya tidak pulih sama
  di sisi JavaScript. Hari ini tidak ada satu pun; tes ini menjaga besok.
* Nol kurikulum = lolos palsu. Populasinya ditagih eksplisit.
"""

import hashlib
import json
import os
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KONTEN = os.path.join(AKAR, "packages", "konten")

from data.bab import BAB  # noqa: E402
from data.kuis_materi import KUIS_MATERI  # noqa: E402
from data.normalisasi import seimbangkan_kuis  # noqa: E402
from inti import visual  # noqa: E402
from inti.kurikulum import LANGUAGES  # noqa: E402


def _muat(*bagian):
    with open(os.path.join(KONTEN, *bagian), encoding="utf-8") as f:
        return json.load(f)


@unittest.skipUnless(os.path.isdir(KONTEN), "packages/konten belum diekspor")
class TestKontenJsonSamaDenganPython(unittest.TestCase):

    def test_populasinya_tidak_kosong(self):
        """Tanpa ini, ekspor yang gagal total akan membuat semua tes di bawah
        lulus karena tidak membandingkan apa pun."""
        berkas = os.listdir(os.path.join(KONTEN, "kurikulum"))
        self.assertEqual(len(berkas), len(LANGUAGES))
        self.assertGreaterEqual(len(LANGUAGES), 32)

    def test_tiap_kurikulum_identik(self):
        for lang in LANGUAGES:
            with self.subTest(kurikulum=lang["key"]):
                d = _muat("kurikulum", f"{lang['key']}.json")
                self.assertEqual(d["materi"], lang["materials"])
                self.assertEqual(d["latihan"], lang["exercises"])
                self.assertEqual(d["label"], lang["label"])
                self.assertEqual(d["runner"], lang["runner"])

    def test_kuis_tersimpan_mentah_dan_memutar_jadi_yang_dipakai(self):
        for lang in LANGUAGES:
            with self.subTest(kurikulum=lang["key"]):
                mentah = _muat("kurikulum", f"{lang['key']}.json")["kuis_mentah"]
                self.assertEqual(seimbangkan_kuis(mentah), lang["quizzes"])

    def test_sidik_kuis_pasca_rotasi_tidak_bergeser(self):
        sidik = _muat("sidik.json")["kuis_pasca_rotasi"]
        self.assertEqual(sorted(sidik), sorted(l["key"] for l in LANGUAGES))
        for lang in LANGUAGES:
            with self.subTest(kurikulum=lang["key"]):
                teks = json.dumps(lang["quizzes"], ensure_ascii=False,
                                  sort_keys=True)
                nyata = hashlib.sha256(teks.encode("utf-8")).hexdigest()
                self.assertEqual(
                    nyata, sidik[lang["key"]],
                    "rotasi opsi kuis bergeser; ekspor ulang dan PERIKSA "
                    "penjelasan soal yang menyebut posisi opsi")

    def test_bab_kuis_materi_dan_gambar_identik(self):
        self.assertEqual(_muat("bab.json"), BAB)
        self.assertEqual(_muat("kuis_materi.json"), KUIS_MATERI)
        dicek = 0
        for lang in LANGUAGES:
            jalur = os.path.join(KONTEN, "visual", f"{lang['key']}.json")
            if not os.path.exists(jalur):
                continue
            with self.subTest(kurikulum=lang["key"]):
                self.assertEqual(_muat("visual", f"{lang['key']}.json"),
                                 visual.data_bahasa(lang["key"]))
            dicek += 1
        self.assertGreater(dicek, 0, "tidak ada berkas gambar yang dibandingkan")

    def test_tidak_ada_kunci_angka(self):
        """V8 menata ulang kunci berbentuk indeks saat JSON.parse."""
        temuan = []

        def sisir(obj, jalur):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if str(k).isdigit():
                        temuan.append(f"{jalur}/{k}")
                    sisir(v, f"{jalur}/{k}")
            elif isinstance(obj, list):
                for v in obj:
                    sisir(v, jalur)

        for dasar, _anak, berkas in os.walk(KONTEN):
            for nama in berkas:
                if nama.endswith(".json"):
                    penuh = os.path.join(dasar, nama)
                    with open(penuh, encoding="utf-8") as f:
                        sisir(json.load(f), os.path.relpath(penuh, KONTEN))
        self.assertEqual(temuan[:10], [])


GOLDEN = os.path.join(AKAR, "packages", "bersama", "golden")


@unittest.skipUnless(os.path.isdir(GOLDEN), "packages/bersama/golden belum dibuat")
class TestGoldenBersama(unittest.TestCase):
    """Keluaran `sorot`, `galat`, dan `beda` tidak boleh bergeser diam-diam.

    Hari ini ketiganya punya kembaran JavaScript, dan yang menjaga keduanya
    sejalan adalah tes diferensial di `test_web.py`. Begitu keduanya digabung
    jadi satu implementasi TypeScript, tes itu kehilangan lawan tandingnya.
    Rekaman ini yang menggantikannya: ia tidak mengadu dua implementasi,
    melainkan mengadu keluaran hari ini dengan keluaran yang sudah disepakati.

    Rekamannya sengaja dibuat SEBELUM versi TypeScript ada, supaya versi itu
    nanti punya angka yang harus direproduksi -- bukan angka yang ia tetapkan
    sendiri sesudah terlanjur berbeda.
    """

    def test_tidak_bergeser_dari_rekaman(self):
        import sys
        sys.path.insert(0, os.path.join(AKAR, "alat"))
        import golden_bersama

        sekarang = golden_bersama.susun()
        self.assertGreater(len(sekarang["sorot.json"]["kasus"]), 3000,
                           "korpus penyorot menyusut; pagarnya jadi tumpul")
        for nama, isi in sekarang.items():
            with self.subTest(berkas=nama):
                with open(os.path.join(GOLDEN, nama), encoding="utf-8") as f:
                    self.assertEqual(
                        json.load(f), isi,
                        f"{nama} bergeser. Kalau disengaja, jalankan "
                        "`python3 alat/golden_bersama.py --tulis`; kalau "
                        "tidak, cari penyebabnya dulu")


BERSAMA = os.path.join(AKAR, "packages", "bersama")


def _ada_node():
    import shutil
    return shutil.which("node") is not None


@unittest.skipUnless(os.path.isdir(os.path.join(BERSAMA, "src")),
                     "packages/bersama belum ada")
@unittest.skipUnless(_ada_node(), "node tidak terpasang")
class TestAlgoritmaTypeScript(unittest.TestCase):
    """Port TS wajib menghasilkan keluaran identik dengan modul `inti/`.

    Ini penerus `test_web.TestPenyorotJavaScript` untuk implementasi yang
    menggantikan `sorot.js`. Bedanya cara membuktikan: yang lama menjalankan
    dua pemindai berdampingan, yang ini mengadu satu pemindai dengan rekaman
    yang dibuat SEBELUM ia ada. Tes diferensial tetap hijau kalau kedua sisi
    diubah bersamaan; rekaman tidak.

    Yang dijalankan skrip Node-nya sendiri, bukan versi Python dari
    perbandingan yang sama. Menuliskan ulang perbandingannya di sini berarti
    dua definisi "cocok", dan yang satu bisa melonggar tanpa yang lain tahu.

    Giginya diuji terpisah dengan `python3 packages/bersama/uji/gigi-golden.py`
    (delapan mutasi, tiap sel menagih kategori keluhannya). Itu TIDAK ikut di
    sini karena ia menulis ke berkas sumber, dan tes yang menyunting pohon
    kerjanya sendiri akan merusak jalannya suite kalau ia dibunuh di tengah.
    """

    # (skrip, pola cacah populasi, lantai). Lantainya, bukan angka persisnya:
    # mematok 3315 berarti menambah satu materi memerahkan tes ini tanpa ada
    # yang rusak, dan pagar yang memerah tanpa sebab adalah pagar yang orang
    # belajar mengabaikan.
    SKRIP = (
        ("golden-sorot.ts", r"korpus: (\d+) blok kode", 3000),
        ("golden-beda.ts", r"rekaman: (\d+) pasangan", 300),
        ("golden-galat.ts", r"rekaman: (\d+) pesan", 50),
    )

    # Pembanding di `packages/web`: geometri peta rasi diadu dengan `rasi.js`,
    # bukan dengan rekaman. Bisa begitu karena keduanya JavaScript dan
    # fungsinya murni -- tidak ada sisi Python yang perlu direkam.
    SKRIP_WEB = (("banding-rasi.mjs", r"(\d+) perbandingan", 100),
                 ("banding-editor.mjs", r"(\d+) blok kode", 3000),
                 ("banding-pratinjau.mjs", r"(\d+) blok kode", 3000),
                 ("banding-visual.mjs", r"(\d+) spesifikasi gambar", 1300),
                 ("banding-jejak.mjs", r"(\d+) blok kode", 2500),
                 ("banding-kerja.mjs", r"(\d+) solusi", 500))

    def test_keluaran_identik_dengan_python(self):
        import re
        import subprocess
        WEB = os.path.join(AKAR, "packages", "web")
        tugas = [(BERSAMA, s, p, l) for s, p, l in self.SKRIP]
        if os.path.isdir(os.path.join(WEB, "uji")):
            tugas += [(WEB, s, p, l) for s, p, l in self.SKRIP_WEB]
        for paket, skrip, pola, lantai in tugas:
            with self.subTest(skrip=skrip):
                hasil = subprocess.run(
                    ["node", os.path.join(paket, "uji", skrip)],
                    cwd=paket, capture_output=True, text=True, timeout=300)
                keluaran = (hasil.stdout + hasil.stderr).strip()
                # Pesannya tidak menyebut "rekaman Python": dua dari pembanding
                # ini mengadu dengan rekaman dari Python, tapi `banding-rasi`
                # mengadu dengan `rasi.js`. Pesan gagal yang menyebut sumber
                # yang salah mengirim orang mencari di berkas yang salah.
                self.assertEqual(
                    hasil.returncode, 0,
                    f"{skrip} melaporkan ketidakcocokan.\n" + keluaran[:4000])
                # Populasi ditagih di sini juga: skrip itu memang menolak
                # populasi yang tidak sama, tapi tes yang cuma memeriksa kode
                # keluar akan lulus kalau suatu hari penolakan itu dilepas.
                cacah = re.search(pola, keluaran)
                self.assertIsNotNone(
                    cacah, f"keluaran tak terbaca:\n{keluaran[:800]}")
                self.assertGreater(int(cacah.group(1)), lantai,
                                   "korpusnya menyusut; pagarnya jadi tumpul")


if __name__ == "__main__":
    unittest.main(verbosity=2)
