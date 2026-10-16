#!/usr/bin/env python3
"""Mengganti PROSA (field "body") sebuah materi tanpa menyentuh apa pun lagi.

    python3 alat/ganti_badan.py naskah.txt            # periksa saja
    python3 alat/ganti_badan.py naskah.txt --tulis    # periksa lalu tulis

Dipakai saat menulis ulang bahasa materi (lihat alat/panduan_gaya.md). Yang
diganti cuma daftar "body" pada bagian yang disebut; judul, kode, heading,
dan urutan bagian dibiarkan persis. Berkas data diubah di tempat, hanya pada
rentang teks daftar itu, jadi selisih git-nya cuma prosa yang memang ditulis
ulang.

Bentuk naskah:

    @@ data/html_materials.py
    ## 1. Apa Itu HTML & Halaman Pertamamu
    -- 0
    baris prosa pertama
    baris prosa kedua
    -- 1
    ...

`@@` memilih berkas, `##` memilih materi lewat judul LENGKAP-nya, `-- N`
memilih bagian ke-N (mulai dari 0) yang sudah punya "body". Semua yang ada
di bawahnya sampai penanda berikutnya adalah isi baru bagian itu, apa
adanya, termasuk indentasi (yang punya arti bagi pengurai, lihat
"Membaca badan materi" di AGENTS.md).

Pagar yang membuat alat ini MENOLAK menulis:
  * baris baru lebih dari LEBAR_MAKS karakter (baris yang disalin persis
    dari prosa asli dibebaskan, karena blok Keluaran wajib identik);
  * em dash atau en dash di mana pun (panduan gaya melarangnya);
  * blok "Keluaran:" yang tidak sama persis dengan aslinya. Blok itu janji
    yang diuji test_solutions.test_janji_keluaran_di_materi_sesuai_kenyataan
    terhadap keluaran sungguhan, jadi isinya bukan prosa yang boleh digubah;
  * sesudah ditulis, judul, kode, heading, atau body bagian LAIN berubah
    (dibandingkan dengan memuat ulang modulnya). Kalau itu terjadi berkas
    dikembalikan ke isi semula.

Hanya stdlib.
"""

import ast
import importlib.util
import json
import os
import re
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from periksa_gaya import teks_prosa  # noqa: E402  (pengurai prosa yang sama)

LEBAR_MAKS = 78
KEPALA_KELUARAN = re.compile(r"^keluaran(?:nya)?(?:\s*\([^)]*\))?\s*:?$", re.I)


def blok_keluaran(body):
    """Salinan pengurai di tests/test_solutions.py (_blok_keluaran)."""
    hasil = []
    for j, baris in enumerate(body):
        if not KEPALA_KELUARAN.match(baris.strip()):
            continue
        keluar, mulai = [], False
        for x in body[j + 1:]:
            if not x.strip():
                if mulai:
                    break
                continue
            mulai = True
            keluar.append(x.rstrip())
        if keluar:
            hasil.append("\n".join(keluar))
    return hasil


def baca_naskah(jalur):
    """{berkas: {judul: {indeks: [baris]}}}"""
    hasil = {}
    berkas = judul = indeks = None
    with open(jalur, encoding="utf-8") as f:
        for baris in f.read().split("\n"):
            if baris.startswith("@@ "):
                berkas, judul, indeks = baris[3:].strip(), None, None
                hasil.setdefault(berkas, {})
            elif baris.startswith("## "):
                judul, indeks = baris[3:].strip(), None
                hasil[berkas].setdefault(judul, {})
            elif re.match(r"^-- \d+\s*$", baris):
                indeks = int(baris[3:])
                hasil[berkas][judul][indeks] = []
            elif indeks is not None:
                hasil[berkas][judul][indeks].append(baris.rstrip())
    for berkas in hasil.values():
        for bagian in berkas.values():
            for i, isi in bagian.items():
                while isi and not isi[-1].strip():
                    isi.pop()
                while isi and not isi[0].strip():
                    isi.pop(0)
    return hasil


def muat(jalur):
    spec = importlib.util.spec_from_file_location("_materi_sementara", jalur)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    nama = [n for n in dir(modul) if n.endswith("_MATERIALS")]
    return getattr(modul, nama[0])


def _nilai(dict_node, kunci):
    for k, v in zip(dict_node.keys, dict_node.values):
        if isinstance(k, ast.Constant) and k.value == kunci:
            return v
    return None


def cari_rentang(sumber, judul, indeks):
    """(baris_awal, kolom_awal, baris_akhir, kolom_akhir) daftar body."""
    pohon = ast.parse(sumber)
    for simpul in ast.walk(pohon):
        if not isinstance(simpul, ast.Dict):
            continue
        t = _nilai(simpul, "title")
        if not (isinstance(t, ast.Constant) and t.value == judul):
            continue
        bagian = _nilai(simpul, "sections")
        if not isinstance(bagian, ast.List) or indeks >= len(bagian.elts):
            raise SystemExit(f"bagian {indeks} tidak ada di {judul!r}")
        body = _nilai(bagian.elts[indeks], "body")
        if not isinstance(body, ast.List):
            raise SystemExit(f"bagian {indeks} di {judul!r} tidak punya body")
        return body.lineno, body.col_offset, body.end_lineno, body.end_col_offset
    raise SystemExit(f"materi tidak ditemukan: {judul!r}")


def format_daftar(baris_baru, indent):
    dalam = " " * (indent + 4)
    isi = "".join(f"{dalam}{json.dumps(b, ensure_ascii=False)},\n" for b in baris_baru)
    return "[\n" + isi + " " * indent + "]"


def periksa_baris(baris_baru, label, asli=()):
    salah = []
    # Baris yang disalin PERSIS dari prosa asli dibebaskan dari batas lebar:
    # blok Keluaran wajib identik, dan beberapa di antaranya memang memuat
    # baris 80-an karakter. Batas 78 untuk tulisan baru; batas proyek yang
    # dijaga test_data tetap 100.
    asli = set(asli)
    for b in baris_baru:
        if len(b) > LEBAR_MAKS and b not in asli:
            salah.append(f"{label}: baris {len(b)} karakter: {b[:50]}...")
    # Dash hanya dilarang di PROSA. Contoh yang menjorok boleh memuatnya:
    # materi HTML mengajarkan entitas &mdash; dan menampilkan karakternya.
    for p in teks_prosa(baris_baru):
        if "—" in p or "–" in p:
            salah.append(f"{label}: em/en dash di prosa: {p[:60]}")
    return salah


def proses(jalur_berkas, naskah_berkas, tulis):
    jalur = os.path.join(AKAR, jalur_berkas)
    with open(jalur, encoding="utf-8") as f:
        sumber = f.read()
    lama = muat(jalur)
    per_judul = {m["title"]: m for m in lama}
    salah, ganti = [], []
    for judul, bagian in naskah_berkas.items():
        if judul not in per_judul:
            salah.append(f"judul tidak ada: {judul!r}")
            continue
        for indeks, baru in bagian.items():
            label = f"{judul} [{indeks}]"
            asli = per_judul[judul]["sections"][indeks].get("body") or []
            salah += periksa_baris(baru, label, asli)
            if blok_keluaran(asli) != blok_keluaran(baru):
                salah.append(f"{label}: blok Keluaran berubah atau hilang")
            ganti.append((cari_rentang(sumber, judul, indeks), baru))
    if salah:
        print("DITOLAK:\n  " + "\n  ".join(salah))
        return False
    baris = sumber.split("\n")
    # Dari bawah ke atas supaya rentang yang belum diganti tidak bergeser.
    for (l1, c1, l2, c2), baru in sorted(ganti, key=lambda x: -x[0][0]):
        indent = len(baris[l1 - 1]) - len(baris[l1 - 1].lstrip())
        awal = baris[l1 - 1][:c1]
        akhir = baris[l2 - 1][c2:]
        teks = awal + format_daftar(baru, indent) + akhir
        baris[l1 - 1:l2] = teks.split("\n")
    hasil = "\n".join(baris)
    print(f"{jalur_berkas}: {len(ganti)} bagian siap diganti")
    if not tulis:
        return True
    with open(jalur, "w", encoding="utf-8") as f:
        f.write(hasil)
    # Pagar sesudah tulis: selain body yang diminta, semuanya harus identik.
    try:
        kini = muat(jalur)
        diminta = {(j, i) for j, b in naskah_berkas.items() for i in b}
        assert [m["title"] for m in kini] == [m["title"] for m in lama], "judul"
        for m_lama, m_kini in zip(lama, kini):
            assert len(m_lama["sections"]) == len(m_kini["sections"]), m_lama["title"]
            for i, (a, b) in enumerate(zip(m_lama["sections"], m_kini["sections"])):
                for kunci in set(a) | set(b):
                    if kunci == "body" and (m_lama["title"], i) in diminta:
                        continue
                    assert a.get(kunci) == b.get(kunci), f"{m_lama['title']} [{i}] {kunci}"
            for i, s in enumerate(m_kini["sections"]):
                if (m_kini["title"], i) in diminta:
                    assert s.get("body") == naskah_berkas[m_kini["title"]][i], "isi"
    except AssertionError as e:
        with open(jalur, "w", encoding="utf-8") as f:
            f.write(sumber)
        print(f"DIKEMBALIKAN: penulisan mengubah hal lain ({e})")
        return False
    print(f"{jalur_berkas}: ditulis")
    return True


def main():
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    tulis = "--tulis" in sys.argv
    naskah = baca_naskah(sys.argv[1])
    oke = all(proses(b, isi, tulis) for b, isi in naskah.items())
    sys.exit(0 if oke else 1)


if __name__ == "__main__":
    main()
