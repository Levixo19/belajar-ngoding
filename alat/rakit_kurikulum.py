"""Rakit kurikulum tech stack dari draf per bab, periksa, lalu tulis ke data/.

Kurikulum ranah tech stack (data/kurikulum_tech.py) ditulis banyak penulis
sekaligus. Supaya tidak ada dua penulis yang menyunting berkas data yang
sama, tiap penulis menulis DRAF satu bab di direktori draf kurikulumnya:

    <draf>/bab_01.py, bab_02.py, ...   (urut menurut nama berkas)

Isi satu draf (Python biasa, cuma empat nama ini yang dibaca):

    BAB = {"judul": "...", "ket": "...", "tingkat": "dasar"}
    MATERI = [{"title": "Judul Tanpa Nomor", "sections": [...],
               "visual": [...]}]            # visual opsional, inti/visual.py
    KUIS = {"judul": "...", "soal": [{"q": "...", "options": [4 opsi],
            "answer": 0, "explanation": "...", "materi": "Judul Tanpa Nomor"}]}
    LATIHAN = [{"title": "Judul Tanpa Nomor", "difficulty": "Mudah", ...}]

Alat ini yang memberi nomor ("3. ...", "Kuis 2: ...", "Latihan 5: ..."),
menyusun <KEY>_BAB (spesifikasi jumlah), <KEY>_KUIS_MATERI, dan VISUAL,
lalu menulis empat berkas data. Ia MENOLAK menulis kalau satu saja
pemeriksaan gagal, dan memulihkan berkas lama kalau hasil tulisnya tidak
bisa diimpor ulang persis sama.

    python3 alat/rakit_kurikulum.py <key> --draf DIR [--bab 03] [--cepat] [--tulis]

--bab    periksa satu draf saja (draf lain tetap dibaca untuk rujukan judul)
--cepat  jangan jalankan contoh kode materi dan solusi latihan
--tulis  tulis ke data/ (tanpa --bab, dan hanya kalau semua lolos)

Pemeriksaannya memakai ulang tes yang menjaga kurikulum lain
(tests/test_data.py, tests/test_mutu_soal.py, tests/test_solutions.py)
dengan LANGUAGES diganti kurikulum draf ini, ditambah aturan khusus draf:
baris prosa <= 78, tanpa dash, bagian terakhir "Di dunia nyata" berlabel,
`"bahasa"` blok yang sah, contoh PROGRAM yang benar-benar jalan dan tidak
menyentuh jaringan, kuis menautkan materi yang ada, dan gambar konsep sah.
"""

import argparse
import copy
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from data import kurikulum_tech  # noqa: E402
from data.normalisasi import seimbangkan_kuis  # noqa: E402
from inti import berkas, runner, visual  # noqa: E402

LEBAR = 78
DUNIA = "Di dunia nyata"
NOMOR = re.compile(r"^\s*\d+[.:)]\s")
DASH = re.compile("[–—]")
JARINGAN = re.compile(
    r"urlopen|urllib\.request|http\.client|\bsocket\.|\brequests\.|\bfetch\s*\("
    r"|https?\.(get|request)\s*\(|net\.connect|XMLHttpRequest|new\s+WebSocket"
    r"|serve_forever|\.listen\s*\(")
BAHASA_SAH = ((set(runner.TOOLCHAINS) - {"fedora", "git"})
              | {"terminal", "teks"} | set(berkas.BAHASA_LUAR))
KUNCI_BAGIAN = {"heading", "body", "code", "bahasa"}
TINGKAT = kurikulum_tech.TINGKAT
LIMIT_KOTAK = 3


def _info(key):
    for k in kurikulum_tech.KURIKULUM:
        if k["key"] == key:
            return k
    raise SystemExit(f"key {key!r} tidak ada di data/kurikulum_tech.KURIKULUM")


# ------------------------------------------------------------------ draf

def muat_draf(direktori):
    """[(nama, modul atau pesan galat)] urut menurut nama berkas."""
    hasil = []
    for nama in sorted(os.listdir(direktori)):
        if not re.fullmatch(r"bab_\d{2}\.py", nama):
            continue
        jalur = os.path.join(direktori, nama)
        spec = importlib.util.spec_from_file_location("draf_" + nama[:-3], jalur)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as e:  # draf rusak dilaporkan, bukan dilempar
            hasil.append((nama, f"draf tidak bisa dimuat: {type(e).__name__}: {e}"))
            continue
        hasil.append((nama, mod))
    return hasil


def _teks(nilai):
    return isinstance(nilai, str) and nilai.strip() != ""


def periksa_bentuk(nama, d, judul_sebelum, judul_semua):
    """Keluhan bentuk satu draf. judul_sebelum: judul materi sampai bab ini."""
    k = []
    tambah = lambda pesan: k.append(f"{nama}: {pesan}")  # noqa: E731

    bab = getattr(d, "BAB", None)
    if not isinstance(bab, dict) or set(bab) != {"judul", "ket", "tingkat"}:
        tambah("BAB wajib dict berkunci judul, ket, tingkat")
    else:
        if not (_teks(bab["judul"]) and _teks(bab["ket"])):
            tambah("BAB judul/ket kosong")
        if bab["tingkat"] not in TINGKAT:
            tambah(f"BAB tingkat {bab['tingkat']!r} bukan salah satu {TINGKAT}")

    materi = getattr(d, "MATERI", None)
    if not isinstance(materi, list) or not materi:
        tambah("MATERI wajib daftar yang tidak kosong")
        materi = []
    for m in materi:
        k += periksa_materi(nama, m)

    kuis = getattr(d, "KUIS", None)
    if not isinstance(kuis, dict) or set(kuis) != {"judul", "soal"}:
        tambah("KUIS wajib dict berkunci judul dan soal")
    else:
        if not _teks(kuis["judul"]) or NOMOR.match(kuis["judul"]):
            tambah("KUIS judul kosong atau masih bernomor (nomor diberi alat)")
        soal = kuis["soal"] if isinstance(kuis["soal"], list) else []
        if not 4 <= len(soal) <= 12:
            tambah(f"KUIS butuh 4-12 soal, ada {len(soal)}")
        for i, s in enumerate(soal, 1):
            if not isinstance(s, dict) or set(s) != {"q", "options", "answer",
                                                     "explanation", "materi"}:
                tambah(f"soal {i}: kunci wajib q, options, answer, explanation, materi")
                continue
            if not (isinstance(s["options"], list) and len(s["options"]) == 4
                    and all(_teks(o) for o in s["options"])):
                tambah(f"soal {i}: options wajib 4 teks")
            elif len(set(s["options"])) != 4:
                tambah(f"soal {i}: ada opsi kembar")
            if not (isinstance(s["answer"], int) and 0 <= s["answer"] < 4):
                tambah(f"soal {i}: answer wajib 0-3")
            if s["materi"] not in judul_sebelum:
                ada = "ada di bab sesudahnya" if s["materi"] in judul_semua else "tidak ada"
                tambah(f"soal {i}: materi {s['materi']!r} {ada}")

    latihan = getattr(d, "LATIHAN", None)
    if not isinstance(latihan, list):
        tambah("LATIHAN wajib daftar (boleh kosong)")
    else:
        for x in latihan:
            judul = x.get("title") if isinstance(x, dict) else None
            if not _teks(judul) or NOMOR.match(judul) or judul.startswith("Latihan"):
                tambah(f"latihan {judul!r}: title kosong atau masih bernomor")
    return k


def periksa_materi(nama, m):
    k = []
    judul = m.get("title") if isinstance(m, dict) else None
    tambah = lambda pesan: k.append(f"{nama} · {judul}: {pesan}")  # noqa: E731
    if not _teks(judul):
        return [f"{nama}: materi tanpa title"]
    if NOMOR.match(judul) or "::" in judul or len(judul) > 64:
        tambah("title bernomor, memuat '::', atau lebih dari 64 huruf")
    asing = set(m) - {"title", "sections", "visual"}
    if asing:
        tambah(f"kunci asing {sorted(asing)}")
    bagian = m.get("sections")
    if not isinstance(bagian, list) or len(bagian) < 3:
        tambah("sections wajib daftar berisi minimal 3 bagian")
        return k

    kotak = 0
    for i, s in enumerate(bagian):
        if not isinstance(s, dict) or not (set(s) <= KUNCI_BAGIAN) or not (
                "body" in s or "code" in s):
            tambah(f"bagian {i}: kunci wajib dari {sorted(KUNCI_BAGIAN)}, ada body/code")
            continue
        if "bahasa" in s:
            if "code" not in s:
                tambah(f"bagian {i}: 'bahasa' tanpa 'code'")
            elif s["bahasa"] not in BAHASA_SAH:
                tambah(f"bagian {i}: bahasa {s['bahasa']!r} tidak dikenal "
                       f"(lihat inti/berkas.BAHASA_LUAR)")
        for b in s.get("body") or []:
            if not isinstance(b, str):
                tambah(f"bagian {i}: baris body bukan teks")
                continue
            if len(b) > LEBAR:
                tambah(f"bagian {i}: baris {len(b)} > {LEBAR}: {b[:50]}...")
            if DASH.search(b):
                tambah(f"bagian {i}: dash di prosa: {b[:50]}...")
            if re.match(r"\s*(Jebakan|Ingat):", b):
                kotak += 1
        if "code" in s and not _teks(s["code"]):
            tambah(f"bagian {i}: code kosong")
    if kotak > LIMIT_KOTAK:
        tambah(f"{kotak} kotak Jebakan/Ingat, paling banyak {LIMIT_KOTAK}")

    akhir = bagian[-1]
    badan = [b.strip() for b in akhir.get("body") or []]
    if (akhir.get("heading") != DUNIA or "code" in akhir
            or not any(b.startswith("Kasus kecil:") for b in badan)
            or "Cara memecahkannya:" not in badan):
        tambah(f"bagian terakhir wajib heading {DUNIA!r} tanpa code, memuat "
               "'Kasus kecil:' dan baris 'Cara memecahkannya:'")
    if any(s.get("heading") == DUNIA for s in bagian[:-1]):
        tambah(f"{DUNIA!r} muncul sebelum bagian terakhir")

    for j, spes in enumerate(m.get("visual") or []):
        for pesan in visual.periksa(spes, len(bagian)):
            tambah(f"visual {j}: {pesan}")
        if not visual.periksa(spes, len(bagian)):
            for baris in visual.baris(spes):
                if len(baris) > LEBAR:
                    tambah(f"visual {j}: gambar terminal {len(baris)} kolom > {LEBAR}")
                    break
    return k


def periksa_kode(lang, materi, cepat):
    """Keluhan untuk blok kode yang ditawari tombol Jalankan oleh aplikasi."""
    k, cacah = [], {}
    for m in materi:
        for i, s in enumerate(m["sections"]):
            kode = s.get("code")
            if not kode:
                continue
            bhs = s.get("bahasa") or lang["runner"]
            jenis = berkas.jenis_kode(bhs, kode)
            cacah[jenis] = cacah.get(jenis, 0) + 1
            if jenis != berkas.PROGRAM:
                continue
            if JARINGAN.search(kode):
                k.append(f"{m['title']} bagian {i}: contoh PROGRAM menyentuh jaringan "
                         "atau menyalakan server; jadikan potongan (baris '...')")
                continue
            if cepat or not runner.tersedia(bhs):
                continue
            hasil = runner.jalankan(bhs, kode, timeout=60)
            if not hasil.sukses:
                galat = (hasil.galat or hasil.catatan or hasil.keluaran
                         or ("timeout" if hasil.timeout else "")).strip().splitlines()
                k.append(f"{m['title']} bagian {i}: contoh PROGRAM gagal dijalankan "
                         f"({bhs}): {(galat[-1] if galat else 'tanpa pesan')[:120]}")
    return k, cacah


# ----------------------------------------------------------------- rakit

def rakit(key, draf):
    """Struktur data lengkap dari daftar (nama, modul) yang sudah lolos bentuk."""
    materi, spek, kuis, peta, latihan, gambar = [], [], [], {}, [], {}
    for i, (_nama, d) in enumerate(draf, 1):
        spek.append({"judul": d.BAB["judul"], "ket": d.BAB["ket"],
                     "tingkat": d.BAB["tingkat"], "jumlah": len(d.MATERI)})
        for m in d.MATERI:
            materi.append({"title": f"{len(materi) + 1}. {m['title']}",
                           "sections": copy.deepcopy(m["sections"])})
            if m.get("visual"):
                gambar[m["title"]] = copy.deepcopy(m["visual"])
        judul = f"Kuis {i}: {d.KUIS['judul']}"
        kuis.append({"title": judul, "questions": [
            {k: s[k] for k in ("q", "options", "answer", "explanation")}
            for s in d.KUIS["soal"]]})
        peta[judul] = [s["materi"] for s in d.KUIS["soal"]]
        for x in d.LATIHAN:
            ex = copy.deepcopy(x)
            ex["title"] = f"Latihan {len(latihan) + 1}: {x['title']}"
            latihan.append(ex)
    return {"materi": materi, "bab": spek, "kuis": kuis, "kuis_materi": peta,
            "latihan": latihan, "visual": gambar}


def lang_dari(key, hasil):
    info = _info(key)
    return {"key": key, "label": info["label"], "runner": info["runner"],
            "tematik": True, "ranah": "tech", "materials": hasil["materi"],
            "quizzes": seimbangkan_kuis(copy.deepcopy(hasil["kuis"])),
            "exercises": hasil["latihan"], "run_info": list(info["run_info"])}


def jalankan_tes(lang, cepat, lewati=()):
    """Tes kurikulum lain, dijalankan atas kurikulum draf ini saja.

    `lewati`: nama tes yang tidak bermakna untuk potongan kurikulum, misalnya
    "latihan pertama Mudah" saat yang diperiksa bab ketujuh saja.
    """
    import tests.test_data as td
    import tests.test_mutu_soal as tm
    import tests.test_solutions as ts
    for mod in (td, tm, ts):
        mod.LANGUAGES = [lang]
    ts.LEWATI_LAMBAT = False
    kelas = [td.TestMateri, td.TestKuis, td.TestLatihan,
             tm.TestKuisTidakBisaDitebak, tm.TestPetunjukBertangga]
    if not cepat:
        kelas.append(type("TestSolusiDraf", (ts.BasisSolusi, unittest.TestCase),
                          {"lang": lang}))
    suite = unittest.TestSuite(
        t for c in kelas for t in unittest.defaultTestLoader.loadTestsFromTestCase(c)
        if t._testMethodName not in lewati)
    suite.addTest(td.TestHintSatuKalimat("test_tidak_ada_kalimat_yang_terbelah"))
    buf = io.StringIO()
    hasil = unittest.TextTestRunner(stream=buf, verbosity=0).run(suite)
    return hasil.wasSuccessful(), buf.getvalue()


def skor_gaya(materi):
    sys.argv = sys.argv[:1]
    import alat.periksa_gaya as pg
    total, kata, terburuk = 0, 0, []
    for m in materi:
        temuan, n = pg.periksa_materi(m)
        total += len(temuan)
        kata += n
        if temuan:
            terburuk.append((pg.skor(temuan, n), m["title"], sorted({t[0] for t in temuan})))
    terburuk.sort(reverse=True)
    return pg.skor([None] * total, kata), kata, terburuk[:5]


# ------------------------------------------------------------------ tulis

def _lit(v, ind=0):
    """Sumber Python yang terbaca untuk satu nilai, gaya berkas data lain."""
    if isinstance(v, str):
        if ("\n" in v and "\\" not in v and '"""' not in v and not v.endswith('"')
                and "\r" not in v):
            return '"""' + v + '"""'
        return json.dumps(v, ensure_ascii=False)
    if v is None or isinstance(v, (bool, int, float)):
        return repr(v)
    dalam = " " * (ind + 4)
    if isinstance(v, (list, tuple)):
        if not v:
            return "[]"
        if all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in v):
            return "[" + ", ".join(repr(x) for x in v) + "]"
        isi = "".join(f"{dalam}{_lit(x, ind + 4)},\n" for x in v)
        return "[\n" + isi + " " * ind + "]"
    if isinstance(v, dict):
        if not v:
            return "{}"
        isi = "".join(f"{dalam}{json.dumps(k, ensure_ascii=False)}: {_lit(x, ind + 4)},\n"
                      for k, x in v.items())
        return "{\n" + isi + " " * ind + "}"
    raise TypeError(f"tidak bisa menulis {type(v).__name__}")


def _isi_berkas(key, hasil):
    besar, info = key.upper(), _info(key)
    kepala = (f'"""Kurikulum {info["label"]}.\n\n'
              "Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).\n"
              "Sesudah dirakit, berkas ini disunting seperti kurikulum lain\n"
              "(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap\n"
              "spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.\n"
              '"""\n\n')
    berkas_ = {
        f"data/{key}_materials.py": kepala
        + f"{besar}_BAB = {_lit(hasil['bab'])}\n\n"
        + f"{besar}_MATERIALS = {_lit(hasil['materi'])}\n",
        f"data/{key}_quizzes.py": kepala
        + f"{besar}_QUIZZES = {_lit(hasil['kuis'])}\n\n"
        + "# Materi yang mengajarkan jawaban tiap soal, urut sama dengan soal\n"
        + "# di atas (lihat data/kuis_materi.py).\n"
        + f"{besar}_KUIS_MATERI = {_lit(hasil['kuis_materi'])}\n",
        f"data/{key}_exercises.py": kepala
        + f"{besar}_EXERCISES = {_lit(hasil['latihan'])}\n",
    }
    if hasil["visual"]:
        berkas_[f"data/visual/{key}.py"] = (
            f'"""Gambar konsep kurikulum {info["label"]}. Skema: inti/visual.py."""\n\n'
            f"VISUAL = {_lit(hasil['visual'])}\n")
    return berkas_


def _baca_ulang(key):
    kode = (
        "import json, main\n"
        "from data.bab import BAB\n"
        "from data.kuis_materi import KUIS_MATERI\n"
        "from inti import visual\n"
        f"l = [x for x in main.LANGUAGES if x['key'] == {key!r}]\n"
        "assert l, 'kurikulum tidak terdaftar di LANGUAGES'\n"
        "print(json.dumps({'materi': l[0]['materials'], 'latihan': l[0]['exercises'],"
        f" 'bab': BAB[{key!r}], 'kuis_materi': KUIS_MATERI.get({key!r}),"
        f" 'visual': visual.data_bahasa({key!r})}}, ensure_ascii=False, sort_keys=True))\n")
    p = subprocess.run([sys.executable, "-c", kode], cwd=AKAR, capture_output=True,
                       text=True, timeout=120)
    if p.returncode != 0:
        raise RuntimeError(p.stderr.strip().splitlines()[-1] if p.stderr else "gagal")
    return json.loads(p.stdout)


def tulis(key, hasil):
    rencana = _isi_berkas(key, hasil)
    lama = {}
    for jalur in rencana:
        penuh = os.path.join(AKAR, jalur)
        lama[penuh] = open(penuh, encoding="utf-8").read() if os.path.exists(penuh) else None
    try:
        for jalur, isi in rencana.items():
            penuh = os.path.join(AKAR, jalur)
            with open(penuh + ".baru", "w", encoding="utf-8") as f:
                f.write(isi)
            os.replace(penuh + ".baru", penuh)
        nyata = _baca_ulang(key)
        awal, bab = 0, []
        for b in hasil["bab"]:
            bab.append({"judul": b["judul"], "ket": b["ket"], "tingkat": b["tingkat"],
                        "awal": awal, "akhir": awal + b["jumlah"]})
            awal += b["jumlah"]
        harap = json.loads(json.dumps({
            "materi": hasil["materi"], "latihan": hasil["latihan"], "bab": bab,
            "kuis_materi": hasil["kuis_materi"], "visual": hasil["visual"]},
            ensure_ascii=False, sort_keys=True))
        beda = [k for k in harap if harap[k] != nyata[k]]
        if beda:
            raise RuntimeError(f"hasil impor ulang berbeda di {beda}")
    except Exception:
        for penuh, isi in lama.items():
            if isi is None:
                if os.path.exists(penuh):
                    os.remove(penuh)
            else:
                with open(penuh, "w", encoding="utf-8") as f:
                    f.write(isi)
        raise
    return sorted(rencana)


# ------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("key")
    ap.add_argument("--draf", required=True)
    ap.add_argument("--bab")
    ap.add_argument("--cepat", action="store_true")
    ap.add_argument("--tulis", action="store_true")
    a = ap.parse_args()
    _info(a.key)
    if a.tulis and a.bab:
        raise SystemExit("--tulis hanya untuk seluruh kurikulum, tanpa --bab")

    semua = muat_draf(a.draf)
    if not semua:
        raise SystemExit(f"tidak ada bab_NN.py di {a.draf}")
    keluhan = [f"{n}: {d}" for n, d in semua if isinstance(d, str)]
    draf = [(n, d) for n, d in semua if not isinstance(d, str)]

    judul_semua, urutan = set(), {}
    for n, d in draf:
        for m in getattr(d, "MATERI", None) or []:
            if isinstance(m, dict) and _teks(m.get("title")):
                if m["title"].casefold() in {j.casefold() for j in judul_semua}:
                    keluhan.append(f"{n}: judul materi kembar {m['title']!r}")
                judul_semua.add(m["title"])
                urutan.setdefault(n, []).append(m["title"])

    dipilih = [(n, d) for n, d in draf if not a.bab or n == f"bab_{a.bab}.py"]
    if a.bab and not dipilih:
        raise SystemExit(f"bab_{a.bab}.py tidak ada atau gagal dimuat")
    sebelum = set()
    for n, d in draf:
        sebelum |= set(urutan.get(n, []))
        if (n, d) in dipilih:
            keluhan += periksa_bentuk(n, d, sebelum, judul_semua)

    tingkat = [TINGKAT.index(d.BAB["tingkat"]) for _n, d in draf
               if isinstance(getattr(d, "BAB", None), dict)
               and d.BAB.get("tingkat") in TINGKAT]
    if tingkat != sorted(tingkat):
        keluhan.append("tingkat bab turun di tengah kurikulum (dasar -> menengah -> mahir)")
    judul_latihan = [x.get("title") for _n, d in draf for x in getattr(d, "LATIHAN", [])
                     if isinstance(x, dict)]
    if len(set(judul_latihan)) != len(judul_latihan):
        keluhan.append("judul latihan kembar antar bab")

    if keluhan:
        print("DITOLAK, bentuk draf belum benar:")
        print("\n".join("  - " + k for k in keluhan))
        return 1

    hasil = rakit(a.key, dipilih)
    lang = lang_dari(a.key, hasil)
    if a.tulis:
        proyek = [i for i, x in enumerate(hasil["latihan"]) if x.get("proyek")]
        if proyek != [len(hasil["latihan"]) - 1]:
            keluhan.append("tepat satu latihan proyek: True, dan itu latihan terakhir")
    k_kode, cacah = periksa_kode(lang, hasil["materi"], a.cepat)
    keluhan += k_kode
    pertama = draf and dipilih[0][0] == draf[0][0]
    lulus, laporan = jalankan_tes(
        lang, a.cepat, () if pertama else ("test_kesulitan_menanjak",))
    if not lulus:
        keluhan.append("tes kurikulum gagal:\n" + laporan)

    skor, kata, terburuk = skor_gaya(hasil["materi"])
    print(f"{a.key}: {len(dipilih)} bab, {len(hasil['materi'])} materi, "
          f"{sum(len(q['questions']) for q in hasil['kuis'])} soal, "
          f"{len(hasil['latihan'])} latihan, "
          f"{sum(len(v) for v in hasil['visual'].values())} gambar, {kata} kata prosa")
    print("  blok kode:", ", ".join(f"{j} {n}" for j, n in sorted(cacah.items())))
    print(f"  gaya: {skor} temuan per 1000 kata"
          + (" (terbanyak: " + "; ".join(f"{t[1]} {t[0]} {t[2]}" for t in terburuk) + ")"
             if terburuk else ""))
    if keluhan:
        print("DITOLAK:")
        print("\n".join("  - " + k for k in keluhan))
        return 1
    if a.tulis:
        for jalur in tulis(a.key, hasil):
            print("  ditulis", jalur)
    print("LOLOS" + ("" if a.tulis else " (belum ditulis; tambahkan --tulis)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
