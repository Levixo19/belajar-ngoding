"""Hubungan kuis dengan materi yang diujinya. Satu-satunya tempat keputusannya.

Datanya di data/kuis_materi.py: tiap soal menunjuk materi yang mengajarkan
jawabannya. Dari situ diturunkan dua hal yang dipakai terminal dan web:

* KESIAPAN: kuis "siap" kalau semua materi yang diujinya sudah dibaca
  tuntas. Ini PENANDA, bukan kunci. Kuis tetap bisa dibuka kapan saja; yang
  berubah cuma kapan ia DITAWARKAN (saran, kaki materi, daftar kuis). Aturan
  "yang mengunci hanya bacaan" (bab.py) tidak tersentuh.
* BACA LAGI: soal yang dijawab salah menunjuk materi sumbernya.

Kenapa per soal dan bukan per bab: docstring data/bab.py sudah
memperingatkan bahwa memetakan "Kuis 3" ke sebuah bab sering mengada-ada.
Soal demi soal tidak: tiap soal ditinjau terhadap materi yang benar-benar
menjelaskan jawabannya.
"""

from data.kuis_materi import KUIS_MATERI
from pelajar.progress import judul_kunci, kunci


def _indeks_materi(lang):
    """{judul tanpa nomor: indeks} untuk materi satu bahasa."""
    return {judul_kunci(m["title"]): i for i, m in enumerate(lang["materials"])}


def materi_soal(lang, judul_kuis, nomor_asli):
    """(indeks, judul lengkap) materi sumber satu soal, atau None."""
    daftar = KUIS_MATERI.get(lang["key"], {}).get(judul_kuis) or []
    if not 0 <= nomor_asli < len(daftar) or daftar[nomor_asli] is None:
        return None
    i = _indeks_materi(lang).get(daftar[nomor_asli])
    if i is None:
        return None
    return i, lang["materials"][i]["title"]


def materi_soal_key(key, judul_kuis, nomor_asli):
    """Seperti materi_soal, untuk pemanggil yang cuma memegang key bahasa.

    Antarmuka terminal menjalankan kuis dengan kategori ("python_kuis"), tanpa
    entri LANGUAGES-nya; registry itu tinggal di main.py, yang tidak boleh
    diimpor dari sini. Materinya dimuat dari paket `data`, sumber yang sama.
    """
    import importlib
    try:
        modul = importlib.import_module(f"data.{key}_materials")
    except ImportError:
        return None
    materi = next((getattr(modul, n) for n in dir(modul) if n.endswith("_MATERIALS")), None)
    if materi is None:
        return None
    return materi_soal({"key": key, "materials": materi}, judul_kuis, nomor_asli)


def materi_kuis(lang, quiz):
    """Indeks materi yang diuji sebuah kuis, urut dan unik."""
    peta = _indeks_materi(lang)
    daftar = KUIS_MATERI.get(lang["key"], {}).get(quiz["title"]) or []
    return sorted({peta[j] for j in daftar if j in peta})


def sisa_materi(lang, quiz, data):
    """Indeks materi yang diuji kuis ini tapi belum dibaca tuntas."""
    kat = f"{lang['key']}_materi"
    dibaca = set(data.get("materi_dibaca", []))
    return [i for i in materi_kuis(lang, quiz)
            if kunci(kat, lang["materials"][i]["title"]) not in dibaca]


def kuis_siap(lang, quiz, data):
    """True kalau semua materi yang diuji kuis ini sudah dibaca tuntas."""
    return bool(materi_kuis(lang, quiz)) and not sisa_materi(lang, quiz, data)


def kuis_baru_siap(lang, sebelum, sesudah):
    """Kuis yang BELUM pernah dikerjakan dan baru saja jadi siap.

    Dipakai sesudah sebuah materi tuntas: kalau materi itu yang terakhir
    ditunggu sebuah kuis, kuisnya ditawarkan saat itu juga, selagi bacaannya
    masih segar.
    """
    kat = f"{lang['key']}_kuis"
    hasil = []
    for i, q in enumerate(lang["quizzes"]):
        if kunci(kat, q["title"]) in sesudah.get("kuis_skor", {}):
            continue
        if kuis_siap(lang, q, sesudah) and not kuis_siap(lang, q, sebelum):
            hasil.append((i, q))
    return hasil
