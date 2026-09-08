"""Sesi kuis yang hidup di memori server, bukan di browser.

Kenapa tidak diserahkan saja ke JavaScript? Karena kalau kunci jawaban ikut
dikirim ke browser, ia ada di tab Network dan di memori halaman sebelum soalnya
dijawab. Untuk aplikasi yang dipakai belajar sendiri itu bukan soal keamanan,
tapi soal godaan: jawaban yang bisa diintip satu klik membuat kuis berhenti
mengukur apa pun.

Jadi soal dikirim tanpa jawabannya, dan setiap jawaban diperiksa lewat satu
permintaan ke server -- yang di localhost memakan waktu di bawah satu
milidetik, jadi umpan baliknya tetap terasa seketika.

Dua hal yang gampang salah dan dijaga di sini:

* **Index jawaban wajib dipetakan ulang setelah opsi diacak.** Ini bug klasik
  yang membuat kuis menandai jawaban benar sebagai salah. Yang disimpan adalah
  posisi BARU dari opsi yang benar, dihitung sekali saat sesi dibuat.
* **Nomor soal yang dicatat sebagai "masih salah" adalah nomor ASLI**, bukan
  nomor setelah diacak. Kalau tidak, mode "ulangi yang salah saja" akan
  mengulang soal yang tidak ada hubungannya dengan yang tadi gagal.

Importir: webapp/api.py.
"""

import random
import threading
import time
import uuid

# Sesi hanya untuk satu pengguna lokal, tapi tetap dibatasi supaya tab yang
# ditinggalkan berhari-hari tidak menumpuk di memori.
MAKS_SESI = 40
UMUR_SESI_DETIK = 6 * 3600

_KUNCI = threading.RLock()
_SESI = {}


class SesiKuis:
    """Satu percobaan pengerjaan kuis."""

    __slots__ = ("id", "kategori", "judul", "bahasa", "soal", "mode",
                 "jawaban", "mulai", "durasi", "total_asli")

    def __init__(self, kategori, judul, bahasa, soal, mode, durasi, total_asli):
        self.id = uuid.uuid4().hex
        self.kategori = kategori
        self.judul = judul
        self.bahasa = bahasa
        self.soal = soal          # [{asli, q, options, jawab, penjelasan}]
        self.mode = mode          # "penuh" | "salah"
        self.jawaban = {}         # nomor_tampil -> pilihan pengguna
        self.mulai = time.time()
        self.durasi = durasi      # detik; 0 = tanpa batas waktu
        self.total_asli = total_asli

    @property
    def sesi_penuh(self):
        """Sesi ulangan TIDAK boleh menyentuh skor terbaik.

        Alasannya sama persis dengan yang tertulis di
        `progress.record_quiz_score`: subset soal yang dijawab benar semua
        pernah menimpa penyebutnya dan memicu badge "Nilai Sempurna" palsu.
        """
        return self.mode == "penuh"

    def bersih(self):
        """Bentuk yang aman dikirim ke browser: tanpa kunci jawaban."""
        return {
            "sesi": self.id,
            "judul": self.judul,
            "bahasa": self.bahasa,
            "mode": self.mode,
            "durasi": self.durasi,
            "total": len(self.soal),
            "soal": [{"nomor": i, "q": s["q"], "options": list(s["options"])}
                     for i, s in enumerate(self.soal)],
        }


def _buang_kedaluwarsa():
    batas = time.time() - UMUR_SESI_DETIK
    for k in [k for k, s in _SESI.items() if s.mulai < batas]:
        _SESI.pop(k, None)
    if len(_SESI) > MAKS_SESI:
        lama = sorted(_SESI, key=lambda x: _SESI[x].mulai)
        for k in lama[:len(_SESI) - MAKS_SESI]:
            _SESI.pop(k, None)


def _acak_soal(soal, asli, rng):
    """Acak posisi opsi dan hitung ulang di mana jawaban benarnya mendarat."""
    opsi = list(enumerate(soal["options"]))
    rng.shuffle(opsi)
    benar = soal.get("answer", 0)
    posisi_baru = next((i for i, (lama, _) in enumerate(opsi) if lama == benar), 0)
    return {
        "asli": asli,
        "q": soal["q"],
        "options": [teks for _, teks in opsi],
        "jawab": posisi_baru,
        "penjelasan": soal.get("explanation", ""),
    }


def buat(kategori, judul, bahasa, pertanyaan, mode="penuh", acak=True,
         durasi=0, hanya=None):
    """Buat sesi baru. `hanya` = daftar nomor soal ASLI yang mau dikerjakan."""
    rng = random.Random()

    pilihan = list(enumerate(pertanyaan))
    if hanya is not None:
        sah = {i for i in hanya if isinstance(i, int) and 0 <= i < len(pertanyaan)}
        pilihan = [(i, s) for i, s in pilihan if i in sah]
    if not pilihan:
        return None

    if acak:
        rng.shuffle(pilihan)
        soal = [_acak_soal(s, i, rng) for i, s in pilihan]
    else:
        soal = [{"asli": i, "q": s["q"], "options": list(s["options"]),
                 "jawab": s.get("answer", 0),
                 "penjelasan": s.get("explanation", "")} for i, s in pilihan]

    sesi = SesiKuis(kategori, judul, bahasa, soal, mode, durasi, len(pertanyaan))
    with _KUNCI:
        # Dimasukkan DULU, baru dipangkas. Urutan sebaliknya memangkas ke
        # MAKS_SESI lalu menambah satu lagi, sehingga batasnya tidak pernah
        # benar-benar MAKS_SESI melainkan selalu satu di atasnya.
        _SESI[sesi.id] = sesi
        _buang_kedaluwarsa()
    return sesi


def ambil(sesi_id):
    with _KUNCI:
        return _SESI.get(sesi_id)


def jawab(sesi_id, nomor, pilihan):
    """Catat jawaban satu soal. Return dict hasil, atau None kalau sesi hilang."""
    with _KUNCI:
        sesi = _SESI.get(sesi_id)
        if sesi is None or not isinstance(nomor, int):
            return None
        if not 0 <= nomor < len(sesi.soal):
            return None
        s = sesi.soal[nomor]
        # Jawaban PERTAMA yang dikunci; menekan tombol dua kali tidak mengubah
        # nilai, supaya klik ganda tidak diam-diam memperbaiki jawaban salah.
        if nomor not in sesi.jawaban:
            sesi.jawaban[nomor] = pilihan
        terpakai = sesi.jawaban[nomor]
        return {
            "benar": terpakai == s["jawab"],
            "jawaban_benar": s["jawab"],
            "pilihanmu": terpakai,
            "penjelasan": s["penjelasan"],
            "terjawab": len(sesi.jawaban),
            "total": len(sesi.soal),
        }


def rekap(sesi_id):
    """Ringkasan akhir sesi.

    Sesi sengaja TIDAK dihapus di sini supaya layar review masih bisa dibuka
    ulang tanpa kehilangan rinciannya.
    """
    with _KUNCI:
        sesi = _SESI.get(sesi_id)
        if sesi is None:
            return None
        rincian = []
        benar = 0
        salah_asli = []
        for i, s in enumerate(sesi.soal):
            pilih = sesi.jawaban.get(i)
            ok = pilih == s["jawab"]
            benar += 1 if ok else 0
            if not ok:
                salah_asli.append(s["asli"])
            rincian.append({
                "nomor": i,
                "asli": s["asli"],
                "q": s["q"],
                "options": list(s["options"]),
                "jawaban_benar": s["jawab"],
                "pilihanmu": pilih,
                "benar": ok,
                "penjelasan": s["penjelasan"],
            })
        return {
            "sesi": sesi.id,
            "kategori": sesi.kategori,
            "judul": sesi.judul,
            "mode": sesi.mode,
            "sesi_penuh": sesi.sesi_penuh,
            "benar": benar,
            "total": len(sesi.soal),
            "total_asli": sesi.total_asli,
            "detik": int(time.time() - sesi.mulai),
            "salah_asli": sorted(set(salah_asli)),
            "rincian": rincian,
        }


def hapus(sesi_id):
    with _KUNCI:
        _SESI.pop(sesi_id, None)


def kosongkan():
    """Dipakai tes supaya sesi tidak bocor antar kasus uji."""
    with _KUNCI:
        _SESI.clear()
