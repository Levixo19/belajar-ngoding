"""Membaca dan menulis berkas JSON milik pelajar tanpa pernah menghapusnya diam-diam.

Tiga berkas memakai modul ini: progres, konfigurasi, dan catatan pribadi.
Ketiganya dulu punya salinan kode tulis-atomiknya sendiri, dan ketiganya punya
lubang yang sama: berkas yang RUSAK (satu koma salah, laptop mati di tengah
penulisan oleh program lain, sinkronisasi awan yang setengah jadi) dibaca
sebagai "kosong", lalu penyimpanan berikutnya menimpanya. Audit 2026-10-17
mengulanginya di direktori sementara: XP 500 jadi 10, materi lama hilang, dan
tidak ada cadangan apa pun. Untuk catatan itu permanen; tulisan tangan tidak
bisa dikumpulkan ulang.

Aturan di sini:

* Berkas yang tidak bisa diurai DIPINDAH ke samping (``<nama>.rusak-<waktu>``)
  sebelum pemanggil diberi data bawaan. Penyimpanan berikutnya lalu menulis
  berkas baru tanpa menyentuh yang rusak, dan isinya masih bisa diselamatkan
  dengan tangan. Jalurnya dicatat di ``KARANTINA`` supaya antarmuka bisa
  memberi tahu pemakainya, sekali.
* Sebelum menimpa berkas yang sehat, salinannya disimpan sebagai
  ``<nama>.bak``. Satu cadangan bergulir, cukup untuk membatalkan satu
  penyimpanan yang salah.
* Penulisan tetap atomik (berkas sementara + ``os.replace``), dan gagal
  menulis TIDAK melempar: sesi belajar tidak boleh berhenti karena disk
  penuh. Tapi kegagalannya dicatat di ``GAGAL`` supaya layar bisa jujur,
  alih-alih merayakan "+10 XP" yang tidak pernah tersimpan.
"""

import json
import os
import shutil
import tempfile
from datetime import datetime

# Jalur berkas yang dikarantina selama proses ini hidup, urut kejadian.
KARANTINA = []
# Jalur berkas yang penyimpanan TERAKHIRNYA gagal. Dihapus lagi begitu
# penyimpanan berikutnya ke berkas itu berhasil.
GAGAL = set()


def karantina(jalur):
    """Pindahkan berkas rusak ke samping. Mengembalikan jalur barunya, atau None."""
    cap = datetime.now().strftime("%Y%m%d-%H%M%S")
    tujuan = f"{jalur}.rusak-{cap}"
    n = 1
    while os.path.exists(tujuan):
        n += 1
        tujuan = f"{jalur}.rusak-{cap}-{n}"
    try:
        os.replace(jalur, tujuan)
    except OSError:
        return None
    KARANTINA.append(tujuan)
    return tujuan


def baca_json(jalur):
    """Isi berkas JSON, atau None kalau berkas tidak ada atau rusak.

    Berkas yang ADA tapi tidak bisa diurai dikarantina lebih dulu, jadi
    pemanggil boleh langsung memakai data bawaan tanpa takut menimpa apa pun.
    Berkas yang tidak bisa DIBACA (izin, I/O) dibiarkan di tempatnya: itu
    bukan bukti isinya rusak.
    """
    try:
        with open(jalur, "r", encoding="utf-8") as f:
            teks = f.read()
    except FileNotFoundError:
        return None
    except (OSError, UnicodeDecodeError):
        return None
    try:
        return json.loads(teks)
    except ValueError:
        karantina(jalur)
        return None


def tulis_json(jalur, data, awalan=".simpan-", urut_kunci=False):
    """Tulis atomik dengan satu cadangan ``.bak``. True kalau berhasil."""
    sementara = None
    try:
        folder = os.path.dirname(jalur) or "."
        os.makedirs(folder, exist_ok=True)
        fd, sementara = tempfile.mkstemp(dir=folder, prefix=awalan, suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, sort_keys=urut_kunci)
            f.flush()
            os.fsync(f.fileno())
        if os.path.isfile(jalur):
            try:
                shutil.copy2(jalur, jalur + ".bak")
            except OSError:
                pass  # cadangan gagal bukan alasan membatalkan penyimpanan
        os.replace(sementara, jalur)
        GAGAL.discard(jalur)
        return True
    except Exception:
        if sementara:
            try:
                os.unlink(sementara)
            except OSError:
                pass
        GAGAL.add(jalur)
        return False
