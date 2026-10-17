#!/usr/bin/env python3
"""Menambahkan bagian "Di dunia nyata" di AKHIR sebuah materi, tanpa menyentuh yang lain.

    python3 alat/tambah_bagian.py naskah.txt            # periksa saja
    python3 alat/tambah_bagian.py naskah.txt --tulis    # periksa lalu tulis

Bagian ini menjawab dua pertanyaan yang tidak dijawab prosa materi: "di mana
hal ini dipakai orang sungguhan?" dan "bagaimana memecahkan masalah kecil
dengannya?". Ia selalu jadi bagian TERAKHIR, jadi indeks bagian yang sudah
ada tidak bergeser (kunci tebakan `#indeks` di pelajar/tebak.py dan rujukan
visual di data/visual/ bergantung pada indeks itu). Menjalankan ulang alat
ini pada materi yang sudah punya bagiannya MENGGANTI bagian itu, bukan
menambah yang kedua.

Bentuk naskah:

    @@ data/python_materials.py
    ## 1. Pengenalan Python & Instalasi
    baris prosa pertama
    ...
    ## 2. Variabel & Tipe Data
    ...

`@@` memilih berkas, `##` memilih materi lewat judul LENGKAP-nya. Semua baris
di bawahnya sampai penanda berikutnya adalah isi "body" bagian itu, apa
adanya, termasuk indentasi.

Pagar yang membuat alat ini MENOLAK menulis:
  * baris lebih dari LEBAR_MAKS karakter, atau em dash / en dash;
  * kepala "Keluaran:" (blok itu janji yang diuji terhadap keluaran nyata,
    dan bagian ini tidak punya kode yang bisa dijalankan);
  * tanpa label "Kasus kecil:" dan "Cara memecahkannya:" (bentuk yang sama
    di seluruh kurikulum, dan web menggambar keduanya sebagai kotak);
  * kurang dari BARIS_MIN atau lebih dari BARIS_MAKS baris;
  * sesudah ditulis, judul atau bagian LAIN berubah (dibandingkan dengan
    memuat ulang modulnya). Kalau itu terjadi, berkas dikembalikan.

Hanya stdlib.
"""

import ast
import importlib.util
import json
import os
import re
import sys
import tempfile

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JUDUL_BAGIAN = "Di dunia nyata"
LEBAR_MAKS = 78
BARIS_MIN = 8
BARIS_MAKS = 40
KEPALA_KELUARAN = re.compile(r"^keluaran(?:nya)?(?:\s*\([^)]*\))?\s*:?$", re.I)
LABEL_WAJIB = ("Kasus kecil:", "Cara memecahkannya:")


def baca_naskah(jalur):
    """{berkas: {judul: [baris]}}"""
    hasil, berkas, judul = {}, None, None
    with open(jalur, encoding="utf-8") as f:
        for mentah in f.read().split("\n"):
            if mentah.startswith("@@ "):
                berkas, judul = mentah[3:].strip(), None
                hasil.setdefault(berkas, {})
            elif mentah.startswith("## "):
                if berkas is None:
                    sys.exit("naskah: '## judul' muncul sebelum '@@ berkas'")
                judul = mentah[3:].strip()
                if judul in hasil[berkas]:
                    sys.exit(f"naskah: judul ganda {judul!r}")
                hasil[berkas][judul] = []
            elif judul is not None:
                hasil[berkas][judul].append(mentah.rstrip())
    for berkas, per in hasil.items():
        for judul, baris in per.items():
            while baris and not baris[-1].strip():
                baris.pop()
            while baris and not baris[0].strip():
                baris.pop(0)
    return hasil


def periksa_baris(judul, baris):
    keluhan = []
    if not BARIS_MIN <= len(baris) <= BARIS_MAKS:
        keluhan.append(f"{len(baris)} baris (harus {BARIS_MIN}-{BARIS_MAKS})")
    for i, b in enumerate(baris, 1):
        if len(b) > LEBAR_MAKS:
            keluhan.append(f"baris {i} {len(b)} karakter: {b[:50]}...")
        if "—" in b or "–" in b:
            keluhan.append(f"baris {i} memuat dash: {b[:50]}...")
        if KEPALA_KELUARAN.match(b.strip()):
            keluhan.append(f"baris {i} kepala Keluaran (tidak boleh di bagian ini)")
        if "\t" in b:
            keluhan.append(f"baris {i} memuat tab")
    for label in LABEL_WAJIB:
        if not any(b.startswith(label) for b in baris):
            keluhan.append(f"tidak ada baris yang diawali {label!r}")
    return [f"{judul}: {k}" for k in keluhan]


def muat_modul(jalur):
    nama = "_tambah_" + os.path.basename(jalur).replace(".py", "")
    spec = importlib.util.spec_from_file_location(nama, jalur)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    daftar = [v for k, v in vars(mod).items() if k.endswith("_MATERIALS")]
    if len(daftar) != 1:
        sys.exit(f"{jalur}: tidak menemukan tepat satu *_MATERIALS")
    return daftar[0]


def literal(baris):
    """Literal string Python berkutip dua untuk satu baris prosa."""
    return json.dumps(baris, ensure_ascii=False)


def teks_bagian(baris, indent):
    i0, i1, i2 = " " * indent, " " * (indent + 4), " " * (indent + 8)
    isi = "\n".join(f"{i2}{literal(b)}," for b in baris)
    return (f"{i0}{{\n{i1}\"heading\": {literal(JUDUL_BAGIAN)},\n"
            f"{i1}\"body\": [\n{isi}\n{i1}]\n{i0}}}")


def _ofset(teks):
    """Indeks karakter awal tiap baris (ast memakai baris 1-based, kolom byte)."""
    awal, pos = [0], 0
    for baris in teks.split("\n"):
        pos += len(baris) + 1
        awal.append(pos)
    return awal


def _posisi(teks, awal, lineno, col_byte):
    baris = teks[awal[lineno - 1]:awal[lineno]]
    return awal[lineno - 1] + len(baris.encode("utf-8")[:col_byte].decode("utf-8"))


def sunting(teks, per_judul):
    """Kembalikan teks baru dengan bagian ditambahkan/diganti di tiap materi."""
    pohon = ast.parse(teks)
    awal = _ofset(teks)
    sasaran = []  # (mulai, akhir, teks_pengganti)
    ditemukan = set()
    for simpul in ast.walk(pohon):
        if not isinstance(simpul, ast.Dict):
            continue
        kunci = [k.value if isinstance(k, ast.Constant) else None for k in simpul.keys]
        if "title" not in kunci or "sections" not in kunci:
            continue
        judul_n = simpul.values[kunci.index("title")]
        if not isinstance(judul_n, ast.Constant) or judul_n.value not in per_judul:
            continue
        daftar = simpul.values[kunci.index("sections")]
        if not isinstance(daftar, ast.List) or not daftar.elts:
            sys.exit(f"{judul_n.value}: sections bukan daftar literal")
        ditemukan.add(judul_n.value)
        terakhir = daftar.elts[-1]
        indent = terakhir.col_offset
        baru = teks_bagian(per_judul[judul_n.value], indent)
        lama = None
        if isinstance(terakhir, ast.Dict):
            kk = [k.value if isinstance(k, ast.Constant) else None for k in terakhir.keys]
            if "heading" in kk:
                h = terakhir.values[kk.index("heading")]
                if isinstance(h, ast.Constant) and h.value == JUDUL_BAGIAN:
                    lama = terakhir
        if lama is not None:
            # Ganti elemen itu sendiri, dari kurung bukanya sampai kurung tutupnya.
            mulai = _posisi(teks, awal, lama.lineno, lama.col_offset)
            akhir = _posisi(teks, awal, lama.end_lineno, lama.end_col_offset)
            sasaran.append((mulai - indent, akhir, baru))
        else:
            ujung = _posisi(teks, awal, terakhir.end_lineno, terakhir.end_col_offset)
            sasaran.append((ujung, ujung, ",\n" + baru))
    hilang = set(per_judul) - ditemukan
    if hilang:
        sys.exit("judul tidak ditemukan: " + ", ".join(sorted(hilang)))
    for mulai, akhir, pengganti in sorted(sasaran, reverse=True):
        teks = teks[:mulai] + pengganti + teks[akhir:]
    return teks


def tulis_atomik(jalur, teks):
    d = os.path.dirname(jalur)
    fd, sementara = tempfile.mkstemp(dir=d, prefix=".tambah-", suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(teks)
    os.replace(sementara, jalur)


def main(argv):
    if len(argv) < 2:
        sys.exit(__doc__)
    tulis = "--tulis" in argv
    naskah = baca_naskah(argv[1])
    keluhan = []
    for berkas, per in naskah.items():
        for judul, baris in per.items():
            keluhan += periksa_baris(judul, baris)
    if keluhan:
        print("\n".join(keluhan))
        sys.exit(f"{len(keluhan)} keluhan; tidak ada yang ditulis")
    for berkas, per in naskah.items():
        jalur = os.path.join(AKAR, berkas)
        with open(jalur, encoding="utf-8") as f:
            asli = f.read()
        sebelum = muat_modul(jalur)
        baru = sunting(asli, per)
        try:
            ast.parse(baru)
        except SyntaxError as e:
            sys.exit(f"{berkas}: hasil suntingan tidak sah ({e})")
        if not tulis:
            print(f"{berkas}: {len(per)} materi siap ditulis (pakai --tulis)")
            continue
        tulis_atomik(jalur, baru)
        try:
            sesudah = muat_modul(jalur)
            assert [m["title"] for m in sebelum] == [m["title"] for m in sesudah], "judul berubah"
            for m0, m1 in zip(sebelum, sesudah):
                s0 = [s for s in m0["sections"] if s.get("heading") != JUDUL_BAGIAN]
                s1 = [s for s in m1["sections"] if s.get("heading") != JUDUL_BAGIAN]
                assert s0 == s1, f"bagian lain berubah di {m0['title']}"
                assert sum(s.get("heading") == JUDUL_BAGIAN for s in m1["sections"]) <= 1, \
                    f"bagian ganda di {m0['title']}"
                if m1["title"] in per:
                    akhir = m1["sections"][-1]
                    assert akhir.get("heading") == JUDUL_BAGIAN, f"bukan bagian terakhir di {m1['title']}"
                    assert akhir["body"] == per[m1["title"]], f"isi tidak cocok di {m1['title']}"
        except AssertionError as e:
            tulis_atomik(jalur, asli)
            sys.exit(f"{berkas}: {e}; berkas dikembalikan")
        except BaseException:
            # Apa pun yang gagal sesudah menulis (modul tidak bisa dimuat,
            # SystemExit dari muat_modul, Ctrl-C) mengembalikan berkasnya.
            tulis_atomik(jalur, asli)
            raise
        print(f"{berkas}: {len(per)} materi ditulis")


if __name__ == "__main__":
    main(sys.argv)
