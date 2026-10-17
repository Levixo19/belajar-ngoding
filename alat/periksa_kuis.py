#!/usr/bin/env python3
"""Mengukur seberapa bisa ditebak kuis, dan seberapa bocor petunjuk latihan.

    python3 alat/periksa_kuis.py               # ringkasan per kurikulum
    python3 alat/periksa_kuis.py rust          # soal & latihan bermasalah
    python3 alat/periksa_kuis.py rust "Kuis 2" # hanya kuis/latihan berawalan itu

Alat ukur, bukan penilai. Empat hal yang dihitung:

  terpanjang  jawaban benar adalah opsi TERPANJANG sendirian. Peluang acaknya
              25% untuk empat opsi; audit 2026-10-17 menemukan 67% (Rust 92%),
              artinya pelajar bisa lulus dengan memilih kalimat terpanjang.
  jauh        jawaban benar >= 1,5x opsi terpanjang berikutnya. Tebakan yang
              lebih gampang lagi: satu opsi yang jelas paling "lengkap".
  kapital     kata penekanan berhuruf besar (HANYA, TIDAK, BARU) yang cuma
              ada di jawaban benar. Penulisnya menekankan kebenaran, dan
              penekanan itu sendiri jadi bocoran.
  bocor       petunjuk PERTAMA sebuah latihan sudah memuat satu baris inti
              solusi apa adanya. Tangga yang diharapkan: konsep dulu, lalu
              strategi, baru potongan kode di petunjuk terakhir.

Penjaganya tests/test_mutu_soal.py; ambangnya ditulis di sana.
"""

import os
import re
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import LANGUAGES  # noqa: E402
from periksa_gaya import AKRONIM  # noqa: E402

KATA_KAPITAL = re.compile(r"\b[A-Z][A-Z]{2,}\b")
# Baris solusi yang terlalu umum untuk disebut bocoran: cetak polos, komentar,
# kurung, kerangka main. Mengutipnya di petunjuk bukan membocorkan jawaban.
BARIS_UMUM = re.compile(
    r"^(print|console\.log|System\.out|printf|echo|fmt\.Print|puts|Console\.Write"
    r"|SELECT\*FROM|#|//|--|/\*|\*|<!--|\}|\{|return$|import|using|package"
    r"|#include|defmain|publicstaticvoidmain|intmain)")


def _rapat(s):
    return re.sub(r"\s+", "", s.replace('"', "'").replace(";", "")).strip()


def kapital_penekanan(teks):
    """Kata kapital di teks yang bukan singkatan/kata kunci terdaftar."""
    return {k for k in KATA_KAPITAL.findall(teks)
            if k not in AKRONIM and re.search(r"[AIUEO]", k)}


def masalah_soal(soal):
    """Daftar nama masalah untuk satu soal kuis."""
    opsi, a = soal["options"], soal["answer"]
    panjang = [len(o) for o in opsi]
    hasil = []
    if panjang[a] == max(panjang) and panjang.count(max(panjang)) == 1:
        hasil.append("terpanjang")
        kedua = sorted(panjang)[-2]
        if kedua and panjang[a] >= 1.5 * kedua:
            hasil.append("jauh")
    di_benar = kapital_penekanan(opsi[a])
    di_lain = set().union(*(kapital_penekanan(o) for i, o in enumerate(opsi) if i != a))
    if di_benar - di_lain:
        hasil.append("kapital")
    return hasil


def baris_inti(solusi):
    keluar = []
    for b in solusi.splitlines():
        r = _rapat(b)
        if len(r) >= 10 and not BARIS_UMUM.match(r):
            keluar.append(r)
    return keluar


def petunjuk_bocor(latihan):
    """Baris inti solusi yang sudah muncul di petunjuk pertama, atau []."""
    petunjuk = latihan.get("hints") or []
    if not petunjuk:
        return []
    h1 = _rapat(petunjuk[0])
    return [b for b in baris_inti(latihan.get("solution", ""))
            if b in h1 or (len(h1) >= 10 and h1 in b)]


def ringkas(lang):
    hitung = {"soal": 0, "terpanjang": 0, "jauh": 0, "kapital": 0,
              "latihan": 0, "bocor": 0, "petunjuk_kurang": 0}
    for kuis in lang["quizzes"]:
        for s in kuis["questions"]:
            hitung["soal"] += 1
            for m in masalah_soal(s):
                hitung[m] += 1
    for ex in lang["exercises"]:
        hitung["latihan"] += 1
        if petunjuk_bocor(ex):
            hitung["bocor"] += 1
        if len(ex.get("hints") or []) < 2:
            hitung["petunjuk_kurang"] += 1
    return hitung


def main():
    args = sys.argv[1:]
    if not args:
        print(f"{'kurikulum':12} {'soal':>5} {'terpanjang':>11} {'jauh':>5} "
              f"{'kapital':>8} {'latihan':>8} {'bocor':>6} {'<2 hint':>8}")
        total = {}
        for lang in LANGUAGES:
            h = ringkas(lang)
            for k, v in h.items():
                total[k] = total.get(k, 0) + v
            print(f"{lang['key']:12} {h['soal']:5} {h['terpanjang'] / max(h['soal'], 1):10.0%} "
                  f"{h['jauh']:5} {h['kapital']:8} {h['latihan']:8} {h['bocor']:6} "
                  f"{h['petunjuk_kurang']:8}")
        print(f"{'TOTAL':12} {total['soal']:5} {total['terpanjang'] / total['soal']:10.0%} "
              f"{total['jauh']:5} {total['kapital']:8} {total['latihan']:8} "
              f"{total['bocor']:6} {total['petunjuk_kurang']:8}")
        return
    lang = next(l for l in LANGUAGES if l["key"] == args[0])
    awal = args[1] if len(args) > 1 else ""
    # Data mentah (sebelum seimbangkan_kuis) supaya nomor opsi cocok dengan
    # berkas sumber yang disunting.
    modul = __import__(f"data.{lang['key']}_quizzes", fromlist=["x"])
    mentah = next(getattr(modul, n) for n in dir(modul) if n.endswith("_QUIZZES"))
    for kuis in mentah:
        if not kuis["title"].startswith(awal):
            continue
        for i, s in enumerate(kuis["questions"]):
            m = masalah_soal(s)
            if m:
                print(f"[{kuis['title']} #{i}] {','.join(m)}: {s['q'][:70]}")
                for j, o in enumerate(s["options"]):
                    tanda = "*" if j == s["answer"] else " "
                    print(f"     {tanda} {len(o):3} {o[:90]}")
    for ex in lang["exercises"]:
        if not ex["title"].startswith(awal):
            continue
        b = petunjuk_bocor(ex)
        if b or len(ex.get("hints") or []) < 2:
            print(f"[{ex['title']}] petunjuk: {len(ex.get('hints') or [])}"
                  + (f", hint 1 bocor: {b[0][:70]}" if b else ""))


if __name__ == "__main__":
    main()
