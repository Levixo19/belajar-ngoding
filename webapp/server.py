"""Server HTTP untuk antarmuka web. Pustaka standar saja.

Server ini menjalankan kode yang diketik pengguna. Itu membuat satu hal jadi
penting, dan bukan karena paranoia:

    Halaman web mana pun yang sedang terbuka di browser yang sama bisa
    mengirim permintaan ke http://127.0.0.1:<port>.

"Localhost saja" bukan pengaman. Situs jahat tidak bisa MEMBACA balasannya
(same-origin policy melindungi itu), tapi tanpa penjagaan ia bisa MENGIRIM
permintaan -- dan endpoint di sini menjalankan kode. Tiga lapis penjagaan:

1. **Token per-jalannya server.** Dibuat acak saat start, ditanam ke dalam
   halaman, dan wajib disertakan sebagai header `X-Belajar-Token` di setiap
   panggilan API. Situs lain tidak bisa membaca token itu karena tidak bisa
   membaca isi halaman kita.
2. **Header khusus memicu preflight.** Permintaan lintas-asal yang membawa
   header buatan sendiri harus lewat CORS preflight dulu. Server ini tidak
   pernah mengizinkan asal lain, jadi preflight-nya gagal dan permintaan
   aslinya tidak pernah terkirim.
3. **Host dan Origin diperiksa.** Menutup DNS rebinding, di mana nama domain
   milik penyerang diarahkan ke 127.0.0.1 supaya lolos same-origin.

Alamat bind dikunci ke loopback. Menyalakannya di 0.0.0.0 berarti setiap mesin
di jaringan yang sama bisa menjalankan kode di komputer ini.

Importir: belajar-web.py, tests/test_web.py.
"""

import json
import mimetypes
import os
import secrets
import socket
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

from webapp import api

STATIK = os.path.join(os.path.dirname(os.path.abspath(__file__)), "statik")

# Muatan JSON dibatasi supaya permintaan rusak tidak menyedot memori. Kode
# pelajar paling panjang pun jauh di bawah ini.
MAKS_MUATAN = 4 * 1024 * 1024

_TIPE = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
    ".woff2": "font/woff2",
    ".woff": "font/woff",
    ".png": "image/png",
    ".ico": "image/x-icon",
}


# (metode, path) -> (fungsi, sumber_argumen)
#   "kueri"  = argumen diambil dari query string
#   "muatan" = argumen diambil dari body JSON
RUTE = {
    ("GET", "/api/awal"): (api.awal, "kueri"),
    ("GET", "/api/dasbor"): (api.dasbor, "kueri"),
    ("GET", "/api/statistik"): (api.statistik, "kueri"),
    ("GET", "/api/bahasa"): (api.bahasa, "kueri"),

    ("GET", "/api/materi"): (api.materi, "kueri"),
    ("POST", "/api/materi/selesai"): (api.materi_selesai, "muatan"),
    ("GET", "/api/materi/contoh"): (api.contoh_kode, "kueri"),

    ("POST", "/api/kuis/mulai"): (api.kuis_mulai, "muatan"),
    ("POST", "/api/kuis/jawab"): (api.kuis_jawab, "muatan"),
    ("POST", "/api/kuis/selesai"): (api.kuis_selesai, "muatan"),
    ("POST", "/api/kuis/batal"): (api.kuis_batal, "muatan"),

    ("GET", "/api/latihan"): (api.latihan, "kueri"),
    ("GET", "/api/latihan/kerangka"): (api.latihan_kerangka, "kueri"),
    ("POST", "/api/latihan/simpan"): (api.latihan_simpan, "muatan"),
    ("POST", "/api/latihan/jalankan"): (api.latihan_jalankan, "muatan"),
    ("POST", "/api/latihan/periksa"): (api.latihan_periksa, "muatan"),
    ("POST", "/api/latihan/manual"): (api.latihan_manual, "muatan"),

    ("POST", "/api/coba"): (api.coba, "muatan"),

    ("GET", "/api/cari"): (api.cari, "kueri"),
    ("GET", "/api/pustaka"): (api.pustaka, "kueri"),
    ("GET", "/api/karier"): (api.karier, "kueri"),
    ("GET", "/api/karier/kuis"): (api.karier_kuis, "kueri"),
    ("GET", "/api/karier/jalur"): (api.karier_jalur, "kueri"),

    ("GET", "/api/bookmark"): (api.bookmark_daftar, "kueri"),
    ("POST", "/api/bookmark"): (api.bookmark_ubah, "muatan"),
    ("POST", "/api/bookmark/bersihkan"): (api.bookmark_bersihkan, "muatan"),

    ("GET", "/api/catatan"): (api.catatan_ambil, "kueri"),
    ("POST", "/api/catatan"): (api.catatan_tulis, "muatan"),
    ("GET", "/api/catatan/semua"): (api.catatan_semua, "kueri"),

    ("GET", "/api/konfigurasi"): (api.konfigurasi_baca, "kueri"),
    ("POST", "/api/konfigurasi"): (api.konfigurasi_tulis, "muatan"),
    ("POST", "/api/konfigurasi/bawaan"): (api.konfigurasi_bawaan, "muatan"),

    ("GET", "/api/laporan"): (api.laporan, "kueri"),
    ("GET", "/api/data/ekspor"): (api.data_ekspor, "kueri"),
    ("POST", "/api/data/impor"): (api.data_impor, "muatan"),
    ("POST", "/api/data/cadangkan"): (api.data_cadangkan, "muatan"),
    ("POST", "/api/data/reset"): (api.data_reset, "muatan"),
}


class Penangan(BaseHTTPRequestHandler):
    server_version = "BelajarNgoding"
    sys_version = ""
    protocol_version = "HTTP/1.1"

    # ------------------------------------------------------------- keluaran

    def _kirim(self, kode, isi, tipe, tambahan=None):
        if isinstance(isi, str):
            isi = isi.encode("utf-8")
        self.send_response(kode)
        self.send_header("Content-Type", tipe)
        self.send_header("Content-Length", str(len(isi)))
        # Halaman ini tidak pernah boleh dibingkai situs lain, dan tidak boleh
        # membocorkan alamat lokalnya lewat Referer.
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        for k, v in (tambahan or {}).items():
            self.send_header(k, v)
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(isi)

    def _json(self, kode, muatan):
        self._kirim(kode, json.dumps(muatan, ensure_ascii=False),
                    "application/json; charset=utf-8",
                    {"Cache-Control": "no-store"})

    def _galat(self, kode, pesan):
        self._json(kode, {"galat": pesan})

    # ------------------------------------------------------------ penjagaan

    def _asal_sah(self):
        """Tolak permintaan yang datang atas nama host lain (DNS rebinding)."""
        host = (self.headers.get("Host") or "").rsplit(":", 1)[0].strip("[]")
        if host not in ("127.0.0.1", "localhost", "::1", ""):
            return False
        asal = self.headers.get("Origin")
        if asal:
            nama = urlparse(asal).hostname
            if nama not in ("127.0.0.1", "localhost", "::1"):
                return False
        return True

    def _token_sah(self):
        return secrets.compare_digest(
            self.headers.get("X-Belajar-Token", ""), self.server.token)

    # --------------------------------------------------------------- statik

    def _berkas_statik(self, path):
        """Sajikan berkas dari webapp/statik, tanpa bisa keluar dari sana."""
        penuh = os.path.normpath(os.path.join(STATIK, path.lstrip("/")))
        # normpath meratakan "..", jadi pemeriksaan ini menutup path traversal.
        if not penuh.startswith(STATIK + os.sep):
            return self._galat(403, "Akses ditolak.")
        if not os.path.isfile(penuh):
            return self._galat(404, "Berkas tidak ditemukan.")

        ext = os.path.splitext(penuh)[1].lower()
        tipe = (_TIPE.get(ext) or mimetypes.guess_type(penuh)[0]
                or "application/octet-stream")
        try:
            with open(penuh, "rb") as f:
                isi = f.read()
        except OSError:
            return self._galat(500, "Gagal membaca berkas.")
        # Tanpa cache: aplikasi ini dijalankan langsung dari sumbernya, dan
        # berkas yang tersangkut di cache browser setelah diperbarui adalah
        # jenis kebingungan yang paling mahal untuk didiagnosis.
        self._kirim(200, isi, tipe, {"Cache-Control": "no-cache"})

    def _halaman(self):
        try:
            with open(os.path.join(STATIK, "index.html"), "r", encoding="utf-8") as f:
                html = f.read()
        except OSError:
            return self._galat(500, "index.html tidak ditemukan.")
        # Token ditanam ke dalam halaman, bukan diletakkan di URL: URL tersimpan
        # di riwayat browser dan ikut terkirim lewat Referer.
        html = html.replace("{{TOKEN}}", self.server.token)
        self._kirim(200, html, "text/html; charset=utf-8",
                    {"Cache-Control": "no-store"})

    # ----------------------------------------------------------------- rute

    def _tangani(self, metode):
        if not self._asal_sah():
            return self._galat(403, "Permintaan ditolak: asal tidak sah.")

        url = urlparse(self.path)
        path = url.path.rstrip("/") or "/"

        if metode == "GET" and path in ("/", "/index.html"):
            return self._halaman()

        if not path.startswith("/api/"):
            if metode != "GET":
                return self._galat(405, "Metode tidak didukung.")
            return self._berkas_statik(path)

        if not self._token_sah():
            return self._galat(403, "Token tidak sah. Muat ulang halaman.")

        rute = RUTE.get((metode, path))
        if rute is None:
            return self._galat(404, f"Endpoint {path} tidak ada.")
        fungsi, sumber = rute

        try:
            if sumber == "muatan":
                argumen = self._baca_muatan()
            else:
                argumen = {k: v[0] for k, v in parse_qs(url.query).items()}
            hasil = fungsi(argumen)
        except api.Galat as e:
            return self._galat(e.kode, e.pesan)
        except json.JSONDecodeError:
            return self._galat(400, "Muatan bukan JSON yang sah.")
        except BrokenPipeError:
            return                      # tab ditutup di tengah permintaan
        except Exception:
            # Jejak lengkap ke terminal supaya bisa dilaporkan; ke browser cukup
            # pesan pendek, karena isi jejak bisa memuat path pribadi.
            traceback.print_exc()
            return self._galat(500, "Ada yang salah di dalam aplikasi. "
                                    "Jejaknya tercetak di terminal.")
        self._json(200, hasil)

    def _baca_muatan(self):
        panjang = int(self.headers.get("Content-Length") or 0)
        if panjang <= 0:
            return {}
        if panjang > MAKS_MUATAN:
            raise api.Galat("Muatan terlalu besar.", 413)
        data = json.loads(self.rfile.read(panjang).decode("utf-8"))
        if not isinstance(data, dict):
            raise api.Galat("Muatan harus berupa objek JSON.", 400)
        return data

    def do_GET(self):
        self._tangani("GET")

    def do_HEAD(self):
        self._tangani("GET")

    def do_POST(self):
        self._tangani("POST")

    def do_OPTIONS(self):
        # Sengaja tanpa header CORS: preflight dari asal lain harus gagal.
        self._kirim(204, b"", "text/plain", {"Allow": "GET, POST, HEAD"})

    def log_message(self, format, *args):
        if getattr(self.server, "berisik", False):
            super().log_message(format, *args)


class Server(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, alamat, token, berisik=False):
        super().__init__(alamat, Penangan)
        self.token = token
        self.berisik = berisik


def _port_bebas(host, mulai, coba=40):
    """Port pertama yang bisa dipakai mulai dari `mulai`.

    Menyerah dengan pesan yang jelas lebih baik daripada melempar OSError
    mentah: penyebab tersering adalah aplikasi ini sendiri yang masih hidup di
    jendela terminal lain.
    """
    for port in range(mulai, mulai + coba):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                s.bind((host, port))
                return port
            except OSError:
                continue
    return 0


def buat(host="127.0.0.1", port=7777, berisik=False):
    """Siapkan server. Return (server, url) tanpa menjalankannya."""
    if host not in ("127.0.0.1", "localhost", "::1"):
        raise ValueError(
            "Server ini menjalankan kode, jadi alamatnya harus loopback. "
            "Menyalakannya di alamat lain membuka eksekusi kode untuk seluruh "
            "jaringan.")

    terpakai = _port_bebas(host, port)
    if not terpakai:
        raise OSError(f"Tidak ada port bebas mulai dari {port}. "
                      "Mungkin aplikasinya sudah jalan di jendela lain?")

    server = Server((host, terpakai), secrets.token_urlsafe(24), berisik=berisik)
    return server, f"http://{host}:{terpakai}/"


def jalankan(host="127.0.0.1", port=7777, berisik=False, siap=None):
    """Nyalakan server sampai Ctrl+C. `siap` dipanggil dengan URL-nya."""
    server, url = buat(host, port, berisik)
    if siap:
        siap(url)
    try:
        server.serve_forever()
    finally:
        server.shutdown()
        server.server_close()
    return 0


def jalankan_di_latar(host="127.0.0.1", port=7777):
    """Nyalakan di thread terpisah. Dipakai tes. Return (server, url, thread)."""
    server, url = buat(host, port)
    utas = threading.Thread(target=server.serve_forever, daemon=True,
                            name="belajar-web")
    utas.start()
    return server, url, utas
