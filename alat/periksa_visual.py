#!/usr/bin/env python3
"""Periksa gambar konsep satu kurikulum, lalu tampilkan versi terminalnya.

    python3 alat/periksa_visual.py <key>            # periksa + gambar semua
    python3 alat/periksa_visual.py <key> --ringkas  # periksa saja

Yang diperiksa (sama dengan tests/test_visual.py):
  * tiap kunci di VISUAL adalah judul materi TANPA nomor yang memang ada;
  * tiap spesifikasi sah menurut inti/visual.periksa, dan `setelah` menunjuk
    bagian materi yang ada;
  * gambar terminalnya muat di 78 kolom.
Keluar dengan kode 1 kalau ada keluhan.
"""

import os
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from inti import visual  # noqa: E402
from main import LANGUAGES  # noqa: E402

LEBAR_TERMINAL = 78


def keluhan_bahasa(lang):
    """[(judul, keluhan)] untuk satu kurikulum."""
    hasil = []
    per_judul = {visual.judul_tanpa_nomor(m["title"]): m for m in lang["materials"]}
    for judul, daftar in visual.data_bahasa(lang["key"]).items():
        m = per_judul.get(judul)
        if m is None:
            hasil.append((judul, "judul ini bukan materi (tulis tanpa nomor, persis)"))
            continue
        if not isinstance(daftar, list) or not daftar:
            hasil.append((judul, "nilainya harus daftar spesifikasi yang tidak kosong"))
            continue
        for i, s in enumerate(daftar):
            for k in visual.periksa(s, len(m["sections"])):
                hasil.append((judul, f"#{i} {k}"))
            if not visual.periksa(s, len(m["sections"])):
                for b in visual.baris(s, LEBAR_TERMINAL - 2, i + 1):
                    if len("  " + b) > LEBAR_TERMINAL:
                        hasil.append((judul, f"#{i} baris terminal {len(b) + 2} kolom: {b[:40]}"))
    return hasil


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    key = argv[1]
    lang = next((l for l in LANGUAGES if l["key"] == key), None)
    if lang is None:
        sys.exit(f"kurikulum {key!r} tidak ada")
    keluhan = keluhan_bahasa(lang)
    data = visual.data_bahasa(key)
    if "--ringkas" not in argv:
        for m in lang["materials"]:
            daftar = data.get(visual.judul_tanpa_nomor(m["title"]))
            if not daftar:
                continue
            print(f"=== {m['title']}")
            for i, s in enumerate(daftar, 1):
                if visual.periksa(s, len(m["sections"])):
                    continue
                print(f"  (setelah bagian {s['setelah']})")
                for b in visual.baris(s, LEBAR_TERMINAL - 2, i):
                    print("  " + b)
                print()
    jumlah = sum(len(v) for v in data.values()) if isinstance(data, dict) else 0
    print(f"{key}: {jumlah} gambar di {len(data)} dari {len(lang['materials'])} materi; "
          f"{len(keluhan)} keluhan")
    for judul, k in keluhan:
        print(f"  {judul}: {k}")
    sys.exit(1 if keluhan else 0)


if __name__ == "__main__":
    main(sys.argv)
