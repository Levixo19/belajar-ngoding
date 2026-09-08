"""Catatan pribadi pelajar, satu per materi / kuis / latihan.

Kenapa berkas TERPISAH dari progres, bukan satu field tambahan di
`~/.belajar_ngoding_progress.json`?

Karena `progress.reset()` ada, dan orang memakainya: "ulangi Java dari nol"
adalah keinginan yang wajar. Reset itu menghapus semua kunci berawalan
`java_`. Kalau catatan ikut menumpang di sana, reset progres -- tindakan yang
di kepala penggunanya berarti "kosongkan nilaiku" -- diam-diam ikut membakar
tulisan tangannya sendiri. Progres bisa dikumpulkan lagi dengan belajar ulang;
catatan tidak bisa.

Alasan kedua: `progress._migrasi` memvalidasi tipe setiap field bawaan dan
membiarkan field asing lewat. "Membiarkan lewat" itu perilaku yang tidak
dijanjikan siapa pun, dan menggantungkan tulisan pengguna padanya sama saja
dengan berharap.

Skema berkas (~/.belajar_ngoding_catatan.json):

    {
      "versi": 1,
      "catatan": {
        "java_materi::2. Variabel & Tipe Data": {
          "teks": "...tulisan pelajar...",
          "diubah": "2026-08-27T19:04:11"
        }
      }
    }

Kuncinya memakai format `progress.kunci()` yang sudah ada, jadi catatan dan
progres selalu menunjuk hal yang sama tanpa perlu tabel penerjemah.

Importir: webapp/api.py.
"""

import json
import os
import tempfile
import threading
from datetime import datetime

from progress import judul_kunci

VERSI_CATATAN = 1

BERKAS = os.environ.get(
    "BELAJAR_CATATAN_FILE",
    os.path.join(os.path.expanduser("~"), ".belajar_ngoding_catatan.json"),
)

# Batas panjang satu catatan. Bukan soal disk -- ini menjaga muatan JSON tetap
# masuk akal kalau ada yang menempelkan seluruh berkas kode ke dalam catatan.
MAKS_PANJANG = 20_000

_KUNCI = threading.RLock()


def _kosong():
    return {"versi": VERSI_CATATAN, "catatan": {}}


def muat():
    """Baca semua catatan. Berkas rusak diperlakukan kosong, tidak fatal."""
    try:
        with open(BERKAS, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError, ValueError):
        return _kosong()

    if not isinstance(data, dict):
        return _kosong()
    isi = data.get("catatan")
    if not isinstance(isi, dict):
        return _kosong()

    bersih = {}
    for k, v in isi.items():
        if not isinstance(k, str):
            continue
        # Kuncinya dinormalkan sama seperti kunci progres: nomor urut materi
        # dibuang, karena nomor itu bergeser tiap kali kurikulum disisipi
        # materi baru. Progres yang hilang masih bisa dikumpulkan ulang dengan
        # membaca lagi; TULISAN TANGAN pemakainya tidak bisa. Justru karena
        # itulah catatan tinggal di berkasnya sendiri, dan justru karena itu
        # pula kuncinya tidak boleh ikut bergeser.
        k = _kunci_baru(k)
        if isinstance(v, str):          # bentuk lama: nilai berupa teks polos
            bersih.setdefault(k, {"teks": v, "diubah": ""})
        elif isinstance(v, dict) and isinstance(v.get("teks"), str):
            diubah = v.get("diubah")
            bersih.setdefault(k, {"teks": v["teks"],
                                  "diubah": diubah if isinstance(diubah, str)
                                  else ""})
    return {"versi": VERSI_CATATAN, "catatan": bersih}


def _kunci_baru(k):
    """'java_materi::2. Judul' -> 'java_materi::Judul'."""
    if "::" not in k:
        return k
    kategori, judul = k.split("::", 1)
    return f"{kategori}::{judul_kunci(judul)}"


def _simpan(data):
    """Tulis atomik, sama pola dengan progress.save_progress."""
    sementara = None
    try:
        folder = os.path.dirname(BERKAS) or "."
        os.makedirs(folder, exist_ok=True)
        fd, sementara = tempfile.mkstemp(dir=folder, prefix=".catatan-",
                                         suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            f.flush()
            os.fsync(f.fileno())
        os.replace(sementara, BERKAS)
        return True
    except Exception:
        if sementara:
            try:
                os.unlink(sementara)
            except OSError:
                pass
        return False


def ambil(kunci_catatan):
    """Satu catatan: {"teks": ..., "diubah": ...}. Selalu ada bentuknya.

    Kunci yang masuk dinormalkan juga, bukan cuma yang tersimpan. Pemanggilnya
    menyusun kunci dari judul materi yang MASIH bernomor; kalau cuma sisi
    simpanan yang dibuang nomornya, keduanya tidak akan pernah bertemu dan
    setiap catatan tampak kosong padahal ada di berkasnya.
    """
    isi = muat()["catatan"].get(_kunci_baru(kunci_catatan))
    return isi or {"teks": "", "diubah": ""}


def tulis(kunci_catatan, teks):
    """Simpan, atau hapus kalau teksnya kosong. Return catatan yang tersimpan."""
    teks = (teks or "")[:MAKS_PANJANG]
    kunci_catatan = _kunci_baru(kunci_catatan)
    with _KUNCI:
        data = muat()
        if teks.strip():
            entri = {"teks": teks,
                     "diubah": datetime.now().isoformat(timespec="seconds")}
            data["catatan"][kunci_catatan] = entri
        else:
            entri = {"teks": "", "diubah": ""}
            data["catatan"].pop(kunci_catatan, None)
        _simpan(data)
        return entri


def semua():
    """Semua catatan, terbaru dulu -- untuk layar 'Catatanku'."""
    daftar = [{"kunci": k, "teks": v["teks"], "diubah": v.get("diubah", "")}
              for k, v in muat()["catatan"].items()]
    daftar.sort(key=lambda c: c["diubah"], reverse=True)
    return daftar


def jumlah():
    return len(muat()["catatan"])
