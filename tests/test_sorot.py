"""Tes penyorot sintaks.

Satu properti menentukan segalanya di sini: pemindai TIDAK BOLEH kehilangan
satu karakter pun. Kalau ia menelan karakter, contoh kode yang dilihat pelajar
berbeda dari kode yang sebenarnya -- kesalahan paling berbahaya untuk sebuah
aplikasi belajar.
"""

import unittest

from inti import sorot
from inti import tema
from inti.kurikulum import LANGUAGES
from webapp import isi


def semua_potongan_kode():
    """(bahasa, judul, kode) untuk seluruh kode di kurikulum."""
    for lang in LANGUAGES:
        b = lang["runner"]
        for m in lang["materials"]:
            for s in m["sections"]:
                if s.get("code"):
                    yield b, m["title"], s["code"]
        for e in lang["exercises"]:
            yield b, e["title"], e["solution"]
            if e.get("setup"):
                yield b, e["title"] + " (setup)", e["setup"]
            if e.get("verifikasi"):
                yield b, e["title"] + " (verifikasi)", e["verifikasi"]


class TestKeutuhan(unittest.TestCase):
    def test_seluruh_kode_kurikulum_utuh_setelah_ditokenkan(self):
        jumlah = 0
        for bahasa, judul, kode in semua_potongan_kode():
            jumlah += 1
            with self.subTest(bahasa=bahasa, judul=judul):
                self.assertEqual(sorot.polos(kode, bahasa), kode)
        self.assertGreater(jumlah, 250, "kurikulum menyusut drastis?")

    def test_jumlah_baris_tidak_berubah(self):
        for bahasa, judul, kode in semua_potongan_kode():
            with self.subTest(bahasa=bahasa, judul=judul):
                self.assertEqual(len(sorot.sorot_baris(kode, bahasa)),
                                 len(kode.split("\n")))

    def test_kode_rusak_tetap_utuh(self):
        rusak = [
            'print("belum ditutup',
            "/* komentar tanpa penutup",
            "x = '''kutip tiga menggantung",
            "func main() { `raw string menggantung",
            "#include <stdio.h",
            "\\",
            "",
        ]
        for bahasa in sorot.bahasa_didukung():
            for kode in rusak:
                with self.subTest(bahasa=bahasa, kode=kode[:20]):
                    self.assertEqual(sorot.polos(kode, bahasa), kode)

    def test_bahasa_tak_dikenal_tidak_meledak(self):
        kode = "beberapa teks 123 // apa saja"
        self.assertEqual(sorot.polos(kode, "klingon"), kode)


class TestPenandaanToken(unittest.TestCase):
    def _jenis(self, kode, bahasa):
        return {teks: jenis for jenis, teks in sorot.token(kode, bahasa)}

    def test_komentar_python(self):
        jenis = dict((t, j) for j, t in sorot.token("x = 1  # catatan", "python"))
        self.assertEqual(jenis["# catatan"], "komentar")

    def test_string_kutip_tiga_python(self):
        kode = 'a = """dua\nbaris"""'
        potongan = [t for j, t in sorot.token(kode, "python") if j == "string"]
        self.assertEqual(potongan, ['"""dua\nbaris"""'])

    def test_kata_kunci_sql_tidak_bergantung_kapital(self):
        for kata in ("select", "SELECT", "SeLeCt"):
            jenis = [j for j, t in sorot.token(kata + " 1", "sql") if t == kata]
            self.assertEqual(jenis, ["kunci"], kata)

    def test_praprosesor_c_bukan_komentar(self):
        jenis = [j for j, t in sorot.token("#include <stdio.h>\nint x;", "c")
                 if t.startswith("#include")]
        self.assertEqual(jenis, ["khusus"])

    def test_shebang_bash_dianggap_komentar(self):
        jenis = [j for j, t in sorot.token("#!/usr/bin/env bash\necho hai", "bash")
                 if t.startswith("#!")]
        self.assertEqual(jenis, ["komentar"])

    def test_variabel_dolar_bash(self):
        for kode in ("echo $nama", "echo ${nama}", "echo $1", "echo $?"):
            khusus = [t for j, t in sorot.token(kode, "bash") if j == "khusus"]
            self.assertTrue(khusus, kode)

    def test_raw_string_go_boleh_lintas_baris(self):
        kode = "s := `satu\ndua`"
        potongan = [t for j, t in sorot.token(kode, "go") if j == "string"]
        self.assertEqual(potongan, ["`satu\ndua`"])

    def test_kutip_tunggal_menggantung_berhenti_di_akhir_baris(self):
        kode = "echo 'belum ditutup\necho lanjut"
        potongan = [t for j, t in sorot.token(kode, "bash") if j == "string"]
        self.assertNotIn("\n", potongan[0], "string menelan baris berikutnya")

    def test_nama_fungsi_dikenali(self):
        jenis = [j for j, t in sorot.token("hitungLuas(4)", "java") if t == "hitungLuas"]
        self.assertEqual(jenis, ["fungsi"])

    def test_angka_dalam_berbagai_bentuk(self):
        for kode in ("0xFF", "1_000", "3.14", "2e10", "10L", "1.5f"):
            angka = [t for j, t in sorot.token("x = " + kode, "java") if j == "angka"]
            self.assertEqual(angka, [kode], kode)


class TestKeluaran(unittest.TestCase):
    def test_tanpa_warna_hasilnya_sama_dengan_kode_asli(self):
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            kode = 'print("halo")  # komentar'
            self.assertEqual(sorot.sorot(kode, "python"), kode)
        finally:
            tema.pakai_kedalaman(asli)

    def test_setiap_baris_menutup_kode_warnanya_sendiri(self):
        """Kode warna yang menggantung antar baris akan bocor saat paginasi."""
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.WARNA_PENUH)
            kode = 'def f():\n    """dok\n    banyak baris"""\n    return 1'
            for baris in sorot.sorot_baris(kode, "python"):
                if "\033[" in baris:
                    self.assertTrue(baris.endswith(tema.RESET),
                                    f"warna menggantung: {baris!r}")
        finally:
            tema.pakai_kedalaman(asli)

    def test_awalan_ditempel_di_setiap_baris(self):
        asli = tema.kedalaman_aktif()
        try:
            tema.pakai_kedalaman(tema.TANPA_WARNA)
            baris = sorot.sorot_baris("a\nb\nc", "python", awalan="  ")
            self.assertEqual(baris, ["  a", "  b", "  c"])
        finally:
            tema.pakai_kedalaman(asli)


BAHASA_BARU = ("yaml", "toml", "ini", "http", "nginx", "hcl", "redis", "perl",
               "scala", "solidity", "verilog", "fsharp", "nix", "matlab", "luau")


class TestKunciDiAwalBaris(unittest.TestCase):
    """`pemisah_kunci`: kunci di awal baris untuk YAML, HTTP, ini, TOML, HCL.

    Pemindainya murni leksikal, jadi yang dijaga di sini adalah pengaman yang
    membedakan `image: nginx` dari `curl http://host`: tanpa pengaman itu
    tidak ada cara lain membedakannya. Jenisnya `kunci`, bukan `fungsi`: di
    tiga tema gelap warna `fungsi` hanya berkontras 1,16 sampai 1,53 terhadap
    teks polos, jadi kunci YAML nyaris tak terlihat bedanya.
    """

    def _kunci(self, kode, bahasa):
        return [t for j, t in sorot.token(kode, bahasa) if j == "kunci"]

    def test_yaml_kunci_bersarang_dan_butir_daftar(self):
        kode = "services:\n  web:\n    image: nginx\n    ports:\n      - uses: a/b@v1\n"
        self.assertEqual(self._kunci(kode, "yaml"),
                         ["services", "web", "image", "ports", "uses"])

    def test_kunci_boleh_memuat_hubung_titik_dan_garis_miring(self):
        for kunci in ("runs-on", "app.kubernetes.io/name", "depends_on"):
            self.assertEqual(self._kunci(f"  {kunci}: x\n", "yaml"), [kunci], kunci)

    def test_titik_dua_tanpa_spasi_bukan_kunci(self):
        kode = "- redis:7\nhttp://host/x\nurl: http://a:80/b\n"
        self.assertEqual(self._kunci(kode, "yaml"), ["url"])

    def test_titik_dua_di_akhir_baris_dan_akhir_berkas_tetap_kunci(self):
        self.assertEqual(self._kunci("a:\r\n  b: 1\r\n", "yaml"), ["a", "b"])
        self.assertEqual(self._kunci("kunci:", "yaml"), ["kunci"])

    def test_kata_di_tengah_baris_bukan_kunci(self):
        self.assertEqual(self._kunci("nama yang panjang: nilai\n", "yaml"), [])
        # `-` di tengah baris bukan penanda butir, dan `-name` bukan butir.
        self.assertEqual(self._kunci("a - b: c\n", "yaml"), [])
        self.assertEqual(self._kunci("-name: x\n", "yaml"), [])

    def test_ini_dan_toml_memakai_sama(self):
        self.assertEqual(self._kunci("spring.jpa.open-in-view=false\n", "ini"),
                         ["spring.jpa.open-in-view"])
        self.assertEqual(self._kunci('agp = "9.4.0"\n[[kv]]\nid = 1\n', "toml"),
                         ["agp", "id"])
        # Hanya kunci pertama di baris: `A=b=c` bukan dua kunci.
        self.assertEqual(self._kunci("Environment=A=b\n", "ini"), ["Environment"])

    def test_sama_dengan_ganda_bukan_penugasan(self):
        kode = 'count == 1\nregion = "x"\n  var.env == "prod" ? 1 : 0\n'
        self.assertEqual(self._kunci(kode, "hcl"), ["region"])

    def test_http_metode_header_dan_url_di_nilai(self):
        kode = "GET /x HTTP/1.1\nHost: toko.example.com\nLocation: http://x/y\n"
        jenis = sorot.token(kode, "http")
        self.assertEqual([t for j, t in jenis if j == "tipe"], ["HTTP"])
        # Metode dan nama header sama-sama kunci; URL di nilai tidak.
        self.assertEqual(self._kunci(kode, "http"), ["GET", "Host", "Location"])

    def test_nginx_nama_berkas_dan_awal_url_tidak_diwarnai(self):
        # `index` dan `http` sengaja tidak didaftarkan: `index.php` dan
        # `http://app` jauh lebih sering muncul daripada direktif `index`.
        kode = "index index.php;\nlocation / {\n  proxy_pass http://app;\n}\n"
        self.assertEqual(self._kunci(kode, "nginx"), ["location", "proxy_pass"])

    def test_bahasa_lain_tidak_terpengaruh(self):
        self.assertEqual(self._kunci("x: int = 1\nfoo: bar\n", "python"), [])
        self.assertEqual(self._kunci("const o = {\n  a: 1,\n};\n", "javascript"), ["const"])
        for nama, aturan in sorot.ATURAN.items():
            if nama not in ("yaml", "toml", "ini", "http", "hcl"):
                self.assertEqual(aturan.pemisah_kunci, (), nama)


class TestBahasaTanpaWarnaDulu(unittest.TestCase):
    """Lima belas bahasa yang dulu tampil polos (135 blok)."""

    def test_semuanya_punya_aturan_tersendiri(self):
        didukung = set(sorot.bahasa_didukung())
        for nama in BAHASA_BARU:
            self.assertIn(nama, sorot.ATURAN, nama)
            # Bukan alias: alias dibuang bahasa_didukung(), dan editor web
            # menerima daftarnya dari sana.
            self.assertIn(nama, didukung, nama)

    def test_luau_memperluas_lua_bukan_menyalinnya_mentah(self):
        lua, luau = sorot.ATURAN["lua"], sorot.ATURAN["luau"]
        self.assertIsNot(lua, luau)
        self.assertTrue(lua.kunci < luau.kunci)
        self.assertIn("continue", luau.kunci)
        self.assertNotIn("continue", lua.kunci)

    def test_porsi_karakter_berwarna_bukan_gestur(self):
        """Aturan yang terdaftar tapi nyaris tidak mewarnai apa pun tetap lolos
        sebagai "golden bergeser", jadi porsinya ditagih langsung. Terukur
        39,6 persen (nix) sampai 85,3 persen (hcl); python 63,7 persen."""
        warna, total, blok = {}, {}, {}
        for lang in LANGUAGES:
            for m in lang["materials"]:
                for s in m["sections"]:
                    if not s.get("code"):
                        continue
                    _runner, bhs = isi.bahasa_blok(s, lang)
                    if bhs not in BAHASA_BARU:
                        continue
                    blok[bhs] = blok.get(bhs, 0) + 1
                    for jenis, teks in sorot.token(s["code"], bhs):
                        n = len(teks.replace("\n", "").replace(" ", ""))
                        total[bhs] = total.get(bhs, 0) + n
                        if jenis not in ("teks", "operator"):
                            warna[bhs] = warna.get(bhs, 0) + n
        for nama in BAHASA_BARU:
            with self.subTest(bahasa=nama):
                self.assertGreater(blok.get(nama, 0), 0, "tidak ada blok di kurikulum")
                self.assertGreaterEqual(warna.get(nama, 0) / total[nama], 0.30)


if __name__ == "__main__":
    unittest.main(verbosity=2)
