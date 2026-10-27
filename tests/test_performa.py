"""Pagar untuk optimasi performa: ETag/304, gzip, CSP, memo Pustaka, indeks cari.

Semuanya harus TIDAK mengubah hasil -- hanya biayanya.
"""

import gzip
import http.client
import json
import threading
import time
import unittest

from inti import kurikulum as main
from inti import pustaka, runner
from webapp import isi
from webapp import server as modul_server
from tests.test_web import BasisWeb


class TestServerCacheDanCsp(BasisWeb):

    @classmethod
    def setUpClass(cls):
        cls.server, cls.url = modul_server.buat(port=7813)
        cls.utas = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.utas.start()
        cls.port = cls.server.server_address[1]
        cls.token = cls.server.token

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def ambil(self, jalur, kepala=None, token=False):
        h = dict(kepala or {})
        if token:
            h["X-Belajar-Token"] = self.token
        c = http.client.HTTPConnection("127.0.0.1", self.port, timeout=30)
        try:
            c.request("GET", jalur, headers=h)
            r = c.getresponse()
            return r.status, dict((k.lower(), v) for k, v in r.getheaders()), r.read()
        finally:
            c.close()

    def test_statik_punya_etag_dan_tetap_no_cache(self):
        kode, kepala, _ = self.ambil("/gaya.css")
        self.assertEqual(kode, 200)
        self.assertIn("etag", kepala)
        self.assertEqual(kepala["cache-control"], "no-cache")

    def test_if_none_match_menjawab_304_tanpa_badan(self):
        _, kepala, _ = self.ambil("/js/inti.js")
        kode, k2, badan = self.ambil("/js/inti.js",
                                     {"If-None-Match": kepala["etag"]})
        self.assertEqual(kode, 304)
        self.assertEqual(badan, b"")
        self.assertEqual(k2["etag"], kepala["etag"])
        self.assertEqual(k2["cache-control"], "no-cache")

    def test_etag_lain_tetap_200(self):
        kode, _, badan = self.ambil("/js/inti.js", {"If-None-Match": '"basi"'})
        self.assertEqual(kode, 200)
        self.assertGreater(len(badan), 100)

    def test_gzip_hanya_kalau_diminta_dan_isinya_sama(self):
        _, _, polos = self.ambil("/gaya.css")
        kode, kepala, mampat = self.ambil("/gaya.css",
                                          {"Accept-Encoding": "gzip"})
        self.assertEqual(kode, 200)
        self.assertEqual(kepala.get("content-encoding"), "gzip")
        self.assertEqual(kepala.get("vary"), "Accept-Encoding")
        self.assertLess(len(mampat), len(polos))
        self.assertEqual(gzip.decompress(mampat), polos)

    def test_tanpa_accept_encoding_tidak_dimampatkan(self):
        _, kepala, _ = self.ambil("/gaya.css")
        self.assertNotIn("content-encoding", kepala)

    def test_font_tidak_dimampatkan(self):
        _, kepala, _ = self.ambil("/huruf/jost.woff2", {"Accept-Encoding": "gzip"})
        self.assertNotIn("content-encoding", kepala)

    def test_json_besar_dimampatkan_dan_sama_dengan_aslinya(self):
        kepala_api = {"Accept-Encoding": "gzip"}
        kode, kepala, mampat = self.ambil("/api/awal", kepala_api, token=True)
        self.assertEqual(kode, 200)
        self.assertEqual(kepala.get("content-encoding"), "gzip")
        _, _, polos = self.ambil("/api/awal", token=True)
        self.assertEqual(json.loads(gzip.decompress(mampat)), json.loads(polos))

    def test_api_tetap_butuh_token_walau_gzip(self):
        kode, _, _ = self.ambil("/api/awal", {"Accept-Encoding": "gzip"})
        self.assertEqual(kode, 403)

    def test_halaman_membawa_csp_tanpa_cdn_dan_tanpa_eval(self):
        kode, kepala, badan = self.ambil("/")
        self.assertEqual(kode, 200)
        csp = kepala["content-security-policy"]
        for wajib in ("default-src 'self'", "connect-src 'self'",
                      "object-src 'none'", "base-uri 'none'",
                      "form-action 'none'", "img-src 'self' data:",
                      "frame-src 'self' about: data:"):
            self.assertIn(wajib, csp)
        self.assertNotIn("unsafe-eval", csp)
        # Satu-satunya asal di luar 'self': layanan pencarian catatan di
        # loopback (layar Catatanku memanggilnya dari browser). Selain itu
        # tidak boleh ada asal http mana pun, apalagi CDN.
        self.assertIn("connect-src 'self' http://127.0.0.1:7799;", csp)
        self.assertNotIn("http", csp.replace("http://127.0.0.1:7799", ""))
        self.assertEqual(kepala["cache-control"], "no-store")
        self.assertIn(self.token.encode(), badan)

    def test_csp_ketat_memasang_nonce_berbeda_tiap_respons(self):
        lama = modul_server.CSP_KETAT
        modul_server.CSP_KETAT = True
        try:
            a = self.ambil("/")
            b = self.ambil("/")
        finally:
            modul_server.CSP_KETAT = lama
        import re
        na = re.search(r"'nonce-([^']+)'", a[1]["content-security-policy"]).group(1)
        nb = re.search(r"'nonce-([^']+)'", b[1]["content-security-policy"]).group(1)
        self.assertNotEqual(na, nb)
        self.assertIn(f'<script nonce="{na}">window.TOKEN_BELAJAR'.encode(), a[2])
        skrip = a[1]["content-security-policy"].split("script-src")[1].split(";")[0]
        self.assertNotIn("unsafe-inline", skrip)


class TestMemoPustaka(unittest.TestCase):

    def test_hasil_memo_sama_dan_salinan_terpisah(self):
        a = pustaka.cari("python", kurikulum="python")
        a["hasil"].clear()
        a["segi"]["jenis"].clear()
        b = pustaka.cari("python", kurikulum="python")
        self.assertGreater(len(b["hasil"]), 0)
        self.assertGreater(len(b["segi"]["jenis"]), 0)

    def test_lupakan_cache_mengosongkan_memo(self):
        pustaka.cari("react")
        pustaka.ringkasan_kurikulum("git")
        pustaka.lupakan_cache()
        self.assertEqual(pustaka._MEMO_CARI, {})
        self.assertEqual(pustaka._MEMO_RINGKASAN, {})
        self.assertGreater(pustaka.total(), 5000)

    def test_ringkasan_salinan_terpisah(self):
        a = pustaka.ringkasan_kurikulum("javascript")
        a["pembuka"].clear()
        self.assertGreater(len(pustaka.ringkasan_kurikulum("javascript")["pembuka"]), 0)

    def test_panaskan_memuat_data(self):
        pustaka.lupakan_cache()
        pustaka.panaskan().join(timeout=30)
        self.assertIsNotNone(pustaka._CACHE)


class TestIndeksCari(unittest.TestCase):

    def test_indeks_dipakai_ulang_dan_hasil_stabil(self):
        a = isi.cari(main.LANGUAGES, "pointer", data={})
        indeks = dict(isi._INDEKS_CARI)
        b = isi.cari(main.LANGUAGES, "pointer", data={})
        self.assertEqual(a, b)
        self.assertGreater(len(a), 0)
        for k, v in isi._INDEKS_CARI.items():
            self.assertIs(v, indeks[k], "indeks dibangun ulang")

    def test_cuplik_dengan_dan_tanpa_baris_kecil_sama(self):
        baris = ["Halo Dunia", "Ada KATA Kunci di sini, cukup panjang " * 6]
        kecil = [b.lower() for b in baris]
        for kata in ("kunci", "DUNIA", "tidakada"):
            self.assertEqual(isi._cuplik(baris, kata),
                             isi._cuplik(baris, kata, rendah_list=kecil))

    def test_kata_berisi_baris_baru_tidak_melintasi_baris(self):
        # "a\nb" tidak boleh cocok hanya karena dua baris bertetangga.
        self.assertEqual(isi.cari(main.LANGUAGES, "zq\nxw", data={}), [])


class TestMemoTersedia(unittest.TestCase):

    def test_which_dipanggil_sekali_dalam_ttl(self):
        runner._MEMO_TERSEDIA.clear()
        dipanggil = []
        asli = runner.shutil.which
        runner.shutil.which = lambda p: dipanggil.append(p) or "/bin/x"
        try:
            for _ in range(5):
                self.assertTrue(runner.tersedia("python"))
            n = len(dipanggil)
            self.assertGreater(n, 0)
            # sesudah TTL lewat, ditanyakan lagi
            waktu, nilai = runner._MEMO_TERSEDIA["python"]
            runner._MEMO_TERSEDIA["python"] = (waktu - runner.TTL_TERSEDIA - 1, nilai)
            runner.tersedia("python")
            self.assertEqual(len(dipanggil), 2 * n)
        finally:
            runner.shutil.which = asli
            runner._MEMO_TERSEDIA.clear()

    def test_bahasa_tak_dikenal_tetap_false(self):
        self.assertFalse(runner.tersedia("tidak-ada-bahasa-ini"))


if __name__ == "__main__":
    unittest.main()
