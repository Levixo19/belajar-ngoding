#!/usr/bin/env python3
"""Memberi JUDUL pada bagian prosa panjang yang belum punya, tanpa menyentuh yang lain.

    python3 alat/tambah_judul.py calon html,css naskah.txt     # tulis daftar bagian yang butuh judul
    python3 alat/tambah_judul.py terap hasil.json [lagi.json]  # periksa saja
    python3 alat/tambah_judul.py terap hasil.json --tulis      # periksa lalu tulis

Kenapa ada: 3.051 dari 8.149 bagian materi tidak berjudul, dan 612 di antaranya
prosa lebih dari 150 kata yang berdiri tanpa satu pun penanda di tengah halaman.
Peta "Di halaman ini" dan judul `h2` di layar membaca field `heading`, jadi
menambahkannya cukup; tidak ada bagian yang dipecah, disisipkan, atau digeser,
dan karena itu tiga ruang indeks yang bergantung pada urutan bagian (kunci
tebakan, `visual.setelah`, tautan Ruang Coba) tidak berubah.

Bentuk hasil (JSON):

    {"data/html_materials.py": {"3. Struktur Dokumen: head dan body": {"3": "Isi head, satu per satu"}}}

`calon` hanya memilih bagian yang BUKAN bagian pertama (pembukanya memang
mengikuti judul materi), belum berjudul, berisi prosa, dan sedikitnya
`MINIMAL_KATA` kata.

Pagar yang membuat `terap` MENOLAK menulis, semuanya per judul:
  * panjang 8 sampai 52 huruf dan 2 sampai 8 kata; diawali huruf kapital;
  * tanpa dash, emoji, atau tanda baca penutup;
  * tanpa HURUF KAPITAL untuk penekanan dan tanpa Title Case;
  * bukan kata umum kosong ("Penjelasan", "Contoh", "Lanjutan", ...) dan tanpa
    kosakata tempelan ("menyelami", "komprehensif", "tips dan trik", ...);
  * unik di dalam materinya (termasuk judul bagian yang sudah ada) dan bukan
    judul materi itu sendiri;
  * bagian sasaran memang ada, berisi prosa, dan belum berjudul.
Sesudah ditulis, modul dimuat ulang dan dibuktikan: judul materi sama, jumlah
bagian sama, dan TIAP bagian sama persis selain field `heading` yang baru.
Kalau satu saja meleset, berkas dikembalikan.

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
sys.path.insert(0, AKAR)

MINIMAL_KATA = 150
UMUM = {
    "penjelasan", "contoh", "lanjutan", "pengantar", "catatan", "ringkasan", "kesimpulan",
    "pendahuluan", "tips", "bagian", "lainnya", "selanjutnya", "detail", "rincian", "intro",
    "gambaran umum", "penjelasan lanjutan", "contoh lanjutan", "contoh penggunaan",
}
TEMPELAN = re.compile(
    r"menyelami|mendalam|komprehensif|esensial|holistik|seluk.beluk|tips dan trik|"
    r"panduan lengkap|lebih jauh|secara lengkap|revolusioner|powerful|game.?changer", re.I)
EMOJI = re.compile("[\U0001F000-\U0001FFFF☀-➿⬀-⯿]")
KATA_KAPITAL = re.compile(r"\b[A-Z][A-Z\-]{2,}\b")


def akronim():
    from alat.periksa_gaya import AKRONIM
    return AKRONIM


def keluhan_judul(judul, judul_materi, sudah):
    """Daftar keluhan untuk satu judul bagian. Kosong = lolos."""
    k = []
    j = judul.strip()
    if j != judul:
        k.append("ada spasi di ujung")
    kata = j.split()
    if not 8 <= len(j) <= 52:
        k.append(f"panjang {len(j)} huruf (harus 8 sampai 52)")
    if not 2 <= len(kata) <= 8:
        k.append(f"{len(kata)} kata (harus 2 sampai 8)")
    if j and not (j[0].isupper() or j[0] == "<"):
        k.append("tidak diawali huruf kapital")
    if re.search(r"[—–]| -- ", j):
        k.append("ada dash")
    if EMOJI.search(j):
        k.append("ada emoji")
    if j[-1:] in ".:;,!":
        k.append("diakhiri tanda baca")
    ak = akronim()
    for w in KATA_KAPITAL.findall(j):
        if w.strip("-") not in ak and re.search(r"[AIUEO]", w):
            k.append(f"huruf kapital penekanan: {w}")
    panjang = [w for w in kata[1:] if len(w) >= 3 and w.isalpha() and w.upper() not in ak]
    kapital = sum(w[0].isupper() for w in panjang)
    if kapital >= 3 and kapital >= 0.6 * len(panjang):
        k.append("Title Case")
    if j.lower() in UMUM:
        k.append("terlalu umum")
    if TEMPELAN.search(j):
        k.append("kosakata tempelan")
    if j.lower() in sudah:
        k.append("kembar dengan judul lain di materi yang sama")
    polos = re.sub(r"^\d+\.\s*", "", judul_materi).strip().lower()
    if j.lower() == polos:
        k.append("sama dengan judul materi")
    return k


def muat_modul(jalur):
    nama = "_judul_" + os.path.basename(jalur).replace(".py", "")
    spec = importlib.util.spec_from_file_location(nama, jalur)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    daftar = [v for k, v in vars(mod).items() if k.endswith("_MATERIALS")]
    if len(daftar) != 1:
        sys.exit(f"{jalur}: tidak menemukan tepat satu *_MATERIALS")
    return daftar[0]


def kata_body(s):
    return sum(len(x.split()) for x in (s.get("body") or []))


def calon(kunci_kurikulum, minimal):
    from inti.kurikulum import LANGUAGES
    per = {l["key"]: l for l in LANGUAGES}
    baris, jumlah = [], 0
    for key in kunci_kurikulum:
        l = per[key]
        berkas = f"data/{key}_materials.py"
        for m in l["materials"]:
            pilih = [(i, s) for i, s in enumerate(m["sections"])
                     if i > 0 and not s.get("heading") and s.get("body") and kata_body(s) >= minimal]
            if not pilih:
                continue
            ada = [s["heading"] for s in m["sections"] if s.get("heading")]
            baris.append(f"=== {berkas} :: {m['title']}")
            baris.append(f"judul yang sudah ada: {json.dumps(ada, ensure_ascii=False)}")
            for i, s in pilih:
                jumlah += 1
                sebelum = m["sections"][i - 1].get("heading") or "(prosa tanpa judul)"
                baris.append(f"--- bagian {i} ({kata_body(s)} kata) | sebelumnya: {sebelum}")
                baris.extend(s["body"])
            baris.append("")
    return "\n".join(baris), jumlah


def _ofset(teks):
    awal, pos = [0], 0
    for b in teks.split("\n"):
        pos += len(b) + 1
        awal.append(pos)
    return awal


def _posisi(teks, awal, lineno, col_byte):
    b = teks[awal[lineno - 1]:awal[lineno]]
    return awal[lineno - 1] + len(b.encode("utf-8")[:col_byte].decode("utf-8"))


def _kunci(d):
    return [k.value if isinstance(k, ast.Constant) else None for k in d.keys]


def sunting(teks, per_judul):
    """Teks baru dengan `"heading": ...` disisipkan sebagai kunci pertama tiap bagian sasaran."""
    pohon = ast.parse(teks)
    awal = _ofset(teks)
    sasaran, ditemukan = [], set()
    for simpul in ast.walk(pohon):
        if not isinstance(simpul, ast.Dict):
            continue
        kk = _kunci(simpul)
        if "title" not in kk or "sections" not in kk:
            continue
        jn = simpul.values[kk.index("title")]
        if not isinstance(jn, ast.Constant) or jn.value not in per_judul:
            continue
        daftar = simpul.values[kk.index("sections")]
        if not isinstance(daftar, ast.List):
            sys.exit(f"{jn.value}: sections bukan daftar literal")
        ditemukan.add(jn.value)
        for si, judul in per_judul[jn.value].items():
            si = int(si)
            if not 0 <= si < len(daftar.elts) or not isinstance(daftar.elts[si], ast.Dict):
                sys.exit(f"{jn.value}: bagian {si} tidak ada atau bukan literal dict")
            d = daftar.elts[si]
            ks = _kunci(d)
            if "heading" in ks:
                sys.exit(f"{jn.value}: bagian {si} sudah berjudul")
            if "body" not in ks:
                sys.exit(f"{jn.value}: bagian {si} tidak berisi prosa")
            pertama = d.keys[0]
            lit = json.dumps(judul, ensure_ascii=False)
            mulai = _posisi(teks, awal, pertama.lineno, pertama.col_offset)
            if pertama.lineno == d.lineno:
                sasaran.append((mulai, f'"heading": {lit}, '))
            else:
                sasaran.append((mulai, f'"heading": {lit},\n' + " " * pertama.col_offset))
    hilang = set(per_judul) - ditemukan
    if hilang:
        sys.exit("judul materi tidak ditemukan: " + ", ".join(sorted(hilang)))
    for mulai, sisip in sorted(sasaran, reverse=True):
        teks = teks[:mulai] + sisip + teks[mulai:]
    return teks


def tulis_atomik(jalur, teks):
    fd, sementara = tempfile.mkstemp(dir=os.path.dirname(jalur), prefix=".judul-", suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(teks)
    os.replace(sementara, jalur)


def gabung(jalur_hasil):
    semua = {}
    for j in jalur_hasil:
        with open(j, encoding="utf-8") as f:
            for berkas, per in json.load(f).items():
                dst = semua.setdefault(berkas, {})
                for judul, bagian in per.items():
                    ada = dst.setdefault(judul, {})
                    for si, h in bagian.items():
                        if si in ada and ada[si] != h:
                            sys.exit(f"{berkas} :: {judul} bagian {si}: dua hasil berbeda")
                        ada[si] = h
    return semua


def periksa_semua(semua):
    keluhan = []
    for berkas, per in semua.items():
        materi = {m["title"]: m for m in muat_modul(os.path.join(AKAR, berkas))}
        for judul, bagian in per.items():
            m = materi.get(judul)
            if m is None:
                keluhan.append(f"{berkas} :: {judul}: materi tidak ada")
                continue
            sudah = {s["heading"].lower() for s in m["sections"] if s.get("heading")}
            for si in sorted(bagian, key=int):
                h = bagian[si]
                i = int(si)
                if not 0 < i < len(m["sections"]):
                    keluhan.append(f"{judul} #{si}: indeks di luar jangkauan atau bagian pertama")
                    continue
                s = m["sections"][i]
                if s.get("heading"):
                    keluhan.append(f"{judul} #{si}: sudah berjudul ({s['heading']})")
                    continue
                if not s.get("body"):
                    keluhan.append(f"{judul} #{si}: bukan bagian prosa")
                    continue
                for k in keluhan_judul(h, judul, sudah):
                    keluhan.append(f"{judul} #{si} {h!r}: {k}")
                sudah.add(h.lower())
    return keluhan


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    if argv[1] == "calon":
        teks, n = calon(argv[2].split(","), MINIMAL_KATA)
        with open(argv[3], "w", encoding="utf-8") as f:
            f.write(teks)
        print(f"{n} bagian ditulis ke {argv[3]}")
        return
    if argv[1] != "terap":
        sys.exit(__doc__)
    tulis = "--tulis" in argv
    semua = gabung([a for a in argv[2:] if not a.startswith("--")])
    keluhan = periksa_semua(semua)
    if keluhan:
        print("\n".join(keluhan))
        sys.exit(f"{len(keluhan)} keluhan; tidak ada yang ditulis")
    total = sum(len(b) for per in semua.values() for b in per.values())
    for berkas, per in semua.items():
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
            print(f"{berkas}: {sum(len(b) for b in per.values())} judul siap ditulis (pakai --tulis)")
            continue
        tulis_atomik(jalur, baru)
        try:
            sesudah = muat_modul(jalur)
            assert [m["title"] for m in sebelum] == [m["title"] for m in sesudah], "judul materi berubah"
            for m0, m1 in zip(sebelum, sesudah):
                assert len(m0["sections"]) == len(m1["sections"]), f"jumlah bagian berubah di {m0['title']}"
                tambah = per.get(m0["title"], {})
                for i, (s0, s1) in enumerate(zip(m0["sections"], m1["sections"])):
                    if str(i) in tambah:
                        assert s1.get("heading") == tambah[str(i)], f"judul salah di {m0['title']} #{i}"
                        s1 = {k: v for k, v in s1.items() if k != "heading"}
                    assert s0 == s1, f"bagian berubah di {m0['title']} #{i}"
        except AssertionError as e:
            tulis_atomik(jalur, asli)
            sys.exit(f"{berkas}: {e}; berkas dikembalikan")
        except BaseException:
            tulis_atomik(jalur, asli)
            raise
        print(f"{berkas}: {sum(len(b) for b in per.values())} judul ditulis")
    print(f"total {total} judul")


if __name__ == "__main__":
    main(sys.argv)
