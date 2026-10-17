"""Gambar konsep di materi: satu spesifikasi, dua penggambar.

Prosa bisa menceritakan "variabel itu kotak berlabel" atau "merge menyatukan
dua cabang", tapi pemula baru benar-benar menangkapnya saat MELIHAT kotak dan
cabangnya. Setiap gambar di sini ditulis sebagai data kecil (bukan berkas
gambar), lalu digambar dua kali dari data yang sama:

  * web: SVG di statik/js/visual.js, bergaya garis atlas, mengikuti tema;
  * terminal: baris teks berbingkai dari `baris()` di modul ini.

Itu yang menjaga aturan "terminal dan web menampilkan ISI yang sama": judul,
keterangan, dan semua label gambar keluar di kedua antarmuka.

Datanya di data/visual/<key>.py: `VISUAL = {"judul materi tanpa nomor":
[spesifikasi, ...]}`. Tiap spesifikasi punya `setelah` (indeks bagian materi,
mulai 0) yang menentukan di mana gambarnya muncul, `jenis`, `judul`, dan
opsional `ket`. Bagian "Di dunia nyata" yang ditambahkan belakangan selalu di
akhir, jadi indeks bagian lama tidak pernah bergeser.

Modul ini cuma membaca data; ia tidak tahu apa pun tentang pelajar.
"""

import importlib
import math
import re

JENIS = ("variabel", "larik", "alur", "tumpukan", "pohon", "tabel", "urutan",
         "kotak", "tata", "git", "memori", "bit", "kurva")

BENTUK_ALUR = ("mulai", "proses", "keputusan", "masukan", "keluaran", "selesai")
KURVA = ("1", "log n", "n", "n log n", "n^2", "2^n")
MAKS_JUDUL = 80
MAKS_KET = 220

_NOMOR = re.compile(r"^\s*\d+\.\s*")
_singgah = {}


def judul_tanpa_nomor(judul):
    """Sama dengan pelajar.progress.judul_kunci, tanpa mengimpor lapisan di atas."""
    return _NOMOR.sub("", judul or "")


def data_bahasa(key):
    """VISUAL milik satu kurikulum, atau {} kalau belum ada berkasnya."""
    if key not in _singgah:
        try:
            mod = importlib.import_module(f"data.visual.{key}")
            _singgah[key] = getattr(mod, "VISUAL", {}) or {}
        except ModuleNotFoundError as e:
            if e.name not in (f"data.visual.{key}", "data.visual"):
                raise
            _singgah[key] = {}
    return _singgah[key]


def untuk(key, judul_materi):
    """Gambar milik satu materi, urut menurut `setelah` lalu urutan tulis."""
    daftar = data_bahasa(key).get(judul_tanpa_nomor(judul_materi), [])
    return sorted(daftar, key=lambda s: s.get("setelah", 0))


def lupakan():
    _singgah.clear()


# ------------------------------------------------------------- pemeriksaan

def _teks(nilai, nama, maks, keluhan, wajib=True):
    if nilai is None and not wajib:
        return
    if isinstance(nilai, (int, float)) and not isinstance(nilai, bool):
        nilai = str(nilai)
    if not isinstance(nilai, str) or (wajib and not nilai.strip()):
        keluhan.append(f"{nama} harus teks yang tidak kosong")
    elif len(nilai) > maks:
        keluhan.append(f"{nama} {len(nilai)} karakter (maks {maks}): {nilai[:30]}")
    elif "\n" in nilai:
        keluhan.append(f"{nama} tidak boleh memuat baris baru")


def _daftar(nilai, nama, mini, maks, keluhan):
    if not isinstance(nilai, list) or not mini <= len(nilai) <= maks:
        keluhan.append(f"{nama} harus daftar {mini}-{maks} butir")
        return False
    return True


def _cek_variabel(s, k):
    if _daftar(s.get("isi"), "isi", 1, 8, k):
        for i, b in enumerate(s["isi"]):
            if not isinstance(b, list) or len(b) not in (2, 3):
                k.append(f"isi[{i}] harus [nama, nilai] atau [nama, nilai, tipe]")
                continue
            _teks(b[0], f"isi[{i}] nama", 16, k)
            _teks(b[1], f"isi[{i}] nilai", 24, k)
            if len(b) == 3:
                _teks(b[2], f"isi[{i}] tipe", 12, k)
        nama = [b[0] for b in s["isi"] if isinstance(b, list) and b]
        for x in s.get("sorot", []):
            if x not in nama:
                k.append(f"sorot {x!r} bukan nama di isi")


def _cek_larik(s, k):
    _teks(s.get("nama"), "nama", 16, k, wajib=False)
    if _daftar(s.get("isi"), "isi", 1, 12, k):
        n = len(s["isi"])
        for i, v in enumerate(s["isi"]):
            _teks(v, f"isi[{i}]", 8, k)
        for i in s.get("sorot", []):
            if not isinstance(i, int) or not 0 <= i < n:
                k.append(f"sorot {i} di luar 0..{n - 1}")
        for lbl, i in (s.get("penunjuk") or {}).items():
            _teks(lbl, "penunjuk", 8, k)
            if not isinstance(i, int) or not 0 <= i < n:
                k.append(f"penunjuk {lbl}={i} di luar 0..{n - 1}")
        r = s.get("rentang")
        if r is not None and (not isinstance(r, list) or len(r) != 2
                              or not 0 <= r[0] < r[1] <= n):
            k.append("rentang harus [awal, akhir] dengan 0 <= awal < akhir <= panjang")


def _cek_alur(s, k):
    if not _daftar(s.get("langkah"), "langkah", 2, 10, k):
        return
    n = len(s["langkah"])
    for i, l in enumerate(s["langkah"]):
        if not isinstance(l, dict):
            k.append(f"langkah[{i}] harus dict")
            continue
        if l.get("jenis") not in BENTUK_ALUR:
            k.append(f"langkah[{i}] jenis harus salah satu {BENTUK_ALUR}")
        _teks(l.get("teks"), f"langkah[{i}] teks", 34, k)
        for arah in ("ya", "tidak", "ke"):
            t = l.get(arah)
            if t is not None and (not isinstance(t, int) or not 0 <= t < n or t == i):
                k.append(f"langkah[{i}] {arah}={t} bukan indeks langkah lain")
        if l.get("jenis") == "keputusan" and l.get("tidak") is None:
            k.append(f"langkah[{i}] keputusan wajib punya 'tidak'")
        if l.get("jenis") != "keputusan" and (l.get("ya") is not None or l.get("tidak") is not None):
            k.append(f"langkah[{i}] 'ya'/'tidak' hanya untuk keputusan (pakai 'ke')")


def _cek_tumpukan(s, k):
    if s.get("mode", "tumpukan") not in ("tumpukan", "antrean"):
        k.append("mode harus 'tumpukan' atau 'antrean'")
    if _daftar(s.get("isi"), "isi", 1, 8, k):
        for i, v in enumerate(s["isi"]):
            _teks(v, f"isi[{i}]", 18, k)
    _teks(s.get("label"), "label", 30, k, wajib=False)
    _teks(s.get("operasi"), "operasi", 20, k, wajib=False)


def _simpul_pohon(n, k, jejak, kedalaman):
    if not isinstance(n, dict):
        k.append("simpul pohon harus dict {teks, anak}")
        return
    jejak.append(1)
    _teks(n.get("teks"), "teks simpul", 18, k)
    if kedalaman > 5:
        k.append("pohon lebih dalam dari 5 tingkat")
        return
    anak = n.get("anak", [])
    if not isinstance(anak, list) or len(anak) > 6:
        k.append("anak harus daftar paling banyak 6 simpul")
        return
    for a in anak:
        _simpul_pohon(a, k, jejak, kedalaman + 1)


def _cek_pohon(s, k):
    jejak = []
    _simpul_pohon(s.get("akar"), k, jejak, 1)
    if len(jejak) > 20:
        k.append(f"pohon {len(jejak)} simpul (maks 20)")


def _cek_tabel(s, k):
    if not _daftar(s.get("tabel"), "tabel", 1, 3, k):
        return
    for t, tb in enumerate(s["tabel"]):
        if not isinstance(tb, dict):
            k.append(f"tabel[{t}] harus dict")
            continue
        _teks(tb.get("nama"), f"tabel[{t}] nama", 24, k, wajib=False)
        if not _daftar(tb.get("kolom"), f"tabel[{t}] kolom", 1, 6, k):
            continue
        for c in tb["kolom"]:
            _teks(c, f"tabel[{t}] kolom", 16, k)
        if not _daftar(tb.get("baris"), f"tabel[{t}] baris", 0, 8, k):
            continue
        for r, baris_ in enumerate(tb["baris"]):
            if not isinstance(baris_, list) or len(baris_) != len(tb["kolom"]):
                k.append(f"tabel[{t}] baris[{r}] harus {len(tb['kolom'])} sel")
                continue
            for v in baris_:
                _teks("" if v is None else v, f"tabel[{t}] sel", 16, k, wajib=False)
        for r in tb.get("sorot_baris", []):
            if not isinstance(r, int) or not 0 <= r < len(tb["baris"]):
                k.append(f"tabel[{t}] sorot_baris {r} di luar jangkauan")
        for c in tb.get("sorot_kolom", []):
            if c not in tb["kolom"]:
                k.append(f"tabel[{t}] sorot_kolom {c!r} tidak ada")
    _teks(s.get("panah"), "panah", 48, k, wajib=False)


def _cek_urutan(s, k):
    if not _daftar(s.get("pelaku"), "pelaku", 2, 4, k):
        return
    for p in s["pelaku"]:
        _teks(p, "pelaku", 14, k)
    if _daftar(s.get("pesan"), "pesan", 1, 10, k):
        n = len(s["pelaku"])
        for i, m in enumerate(s["pesan"]):
            if (not isinstance(m, list) or len(m) != 3 or not isinstance(m[0], int)
                    or not isinstance(m[1], int) or not 0 <= m[0] < n or not 0 <= m[1] < n):
                k.append(f"pesan[{i}] harus [dari, ke, teks] dengan indeks pelaku")
                continue
            _teks(m[2], f"pesan[{i}] teks", 32, k)


def _cek_kotak(s, k):
    for bag in ("margin", "border", "padding", "isi"):
        _teks(s.get(bag), bag, 22, k)
    _teks(s.get("label"), "label", 24, k, wajib=False)


def _cek_tata(s, k):
    mode = s.get("mode")
    if mode not in ("flex", "grid"):
        k.append("mode harus 'flex' atau 'grid'")
        return
    if _daftar(s.get("item"), "item", 1, 9, k):
        for i, it in enumerate(s["item"]):
            if isinstance(it, list):
                if (len(it) != 2 or not isinstance(it[1], int)
                        or not 1 <= it[1] <= (s.get("kolom") or 6)):
                    k.append(f"item[{i}] bentuk [teks, rentang_kolom 1..kolom]")
                    continue
                it = it[0]
            _teks(it, f"item[{i}]", 12, k)
    if mode == "flex":
        if s.get("arah", "row") not in ("row", "column"):
            k.append("arah harus 'row' atau 'column'")
        for p in ("justify", "align"):
            _teks(s.get(p), p, 16, k, wajib=False)
    else:
        if not isinstance(s.get("kolom"), int) or not 1 <= s["kolom"] <= 6:
            k.append("grid butuh kolom 1-6")


def _cek_git(s, k):
    if not _daftar(s.get("commit"), "commit", 1, 12, k):
        return
    ada, cabang = set(), []
    for i, c in enumerate(s["commit"]):
        if not isinstance(c, dict):
            k.append(f"commit[{i}] harus dict")
            continue
        _teks(c.get("id"), f"commit[{i}] id", 4, k)
        _teks(c.get("cabang"), f"commit[{i}] cabang", 14, k)
        _teks(c.get("pesan"), f"commit[{i}] pesan", 24, k, wajib=False)
        for p in c.get("induk", []):
            if p not in ada:
                k.append(f"commit[{i}] induk {p!r} belum muncul sebelumnya")
        if c.get("id") in ada:
            k.append(f"commit id ganda {c.get('id')!r}")
        ada.add(c.get("id"))
        if c.get("cabang") not in cabang:
            cabang.append(c.get("cabang"))
    if len(cabang) > 4:
        k.append("paling banyak 4 cabang")
    for nama, cid in (s.get("label") or {}).items():
        _teks(nama, "label cabang", 14, k)
        if cid not in ada:
            k.append(f"label {nama!r} menunjuk commit yang tidak ada")
    h = s.get("head")
    if h is not None and h not in (s.get("label") or {}) and h not in ada:
        k.append("head harus nama label atau id commit")


def _cek_memori(s, k):
    ids = set()
    for i, o in enumerate(s.get("heap") or []):
        if not isinstance(o, dict):
            k.append(f"heap[{i}] harus dict")
            continue
        _teks(o.get("id"), f"heap[{i}] id", 8, k)
        _teks(o.get("isi"), f"heap[{i}] isi", 28, k)
        ids.add(o.get("id"))
    if len(s.get("heap") or []) > 5:
        k.append("heap paling banyak 5 objek")
    for nama in ("label_tumpukan", "label_heap"):
        _teks(s.get(nama), nama, 16, k, wajib=False)
    if _daftar(s.get("tumpukan"), "tumpukan", 1, 6, k):
        for i, b in enumerate(s["tumpukan"]):
            if not isinstance(b, list) or len(b) != 2:
                k.append(f"tumpukan[{i}] harus [nama, nilai]")
                continue
            _teks(b[0], f"tumpukan[{i}] nama", 12, k)
            _teks(b[1], f"tumpukan[{i}] nilai", 18, k)
            if isinstance(b[1], str) and b[1].startswith("@") and b[1][1:] not in ids:
                k.append(f"tumpukan[{i}] menunjuk {b[1]} yang tidak ada di heap")


def _cek_bit(s, k):
    lebar = s.get("lebar", 8)
    if lebar not in (4, 8, 16):
        k.append("lebar harus 4, 8, atau 16")
        return
    a = s.get("angka")
    if not isinstance(a, int) or isinstance(a, bool) or not 0 <= a < 2 ** lebar:
        k.append(f"angka harus bilangan bulat 0..{2 ** lebar - 1}")
    _teks(s.get("label"), "label", 30, k, wajib=False)


def _cek_kurva(s, k):
    if _daftar(s.get("kurva"), "kurva", 1, 6, k):
        for c in s["kurva"]:
            if c not in KURVA:
                k.append(f"kurva {c!r} bukan salah satu {KURVA}")
    if s.get("sorot") is not None and s.get("sorot") not in (s.get("kurva") or []):
        k.append("sorot harus salah satu kurva yang digambar")


_PEMERIKSA = {
    "variabel": _cek_variabel, "larik": _cek_larik, "alur": _cek_alur,
    "tumpukan": _cek_tumpukan, "pohon": _cek_pohon, "tabel": _cek_tabel,
    "urutan": _cek_urutan, "kotak": _cek_kotak, "tata": _cek_tata,
    "git": _cek_git, "memori": _cek_memori, "bit": _cek_bit, "kurva": _cek_kurva,
}

_MEDAN_UMUM = {"setelah", "jenis", "judul", "ket"}
_MEDAN = {
    "variabel": {"isi", "sorot"}, "larik": {"nama", "isi", "sorot", "penunjuk", "rentang"},
    "alur": {"langkah"}, "tumpukan": {"mode", "isi", "label", "operasi"},
    "pohon": {"akar"}, "tabel": {"tabel", "panah"}, "urutan": {"pelaku", "pesan"},
    "kotak": {"margin", "border", "padding", "isi", "label"},
    "tata": {"mode", "item", "arah", "justify", "align", "kolom"},
    "git": {"commit", "label", "head"},
    "memori": {"tumpukan", "heap", "label_tumpukan", "label_heap"},
    "bit": {"angka", "lebar", "label"}, "kurva": {"kurva", "sorot"},
}


def periksa(spes, jumlah_bagian=None):
    """Daftar keluhan untuk satu spesifikasi; kosong berarti sah."""
    k = []
    if not isinstance(spes, dict):
        return ["spesifikasi harus dict"]
    if spes.get("jenis") not in JENIS:
        return [f"jenis {spes.get('jenis')!r} bukan salah satu {JENIS}"]
    asing = set(spes) - _MEDAN_UMUM - _MEDAN[spes["jenis"]]
    if asing:
        k.append(f"medan tidak dikenal untuk {spes['jenis']}: {sorted(asing)}")
    s = spes.get("setelah")
    if not isinstance(s, int) or s < 0 or (jumlah_bagian is not None and s >= jumlah_bagian):
        k.append(f"setelah={s!r} bukan indeks bagian yang ada")
    _teks(spes.get("judul"), "judul", MAKS_JUDUL, k)
    _teks(spes.get("ket"), "ket", MAKS_KET, k, wajib=False)
    _PEMERIKSA[spes["jenis"]](spes, k)
    return k


# ----------------------------------------------------- penggambar terminal

def _s(v):
    return "" if v is None else str(v)


def _deret_sel(isi_list):
    """Satu deret sel berbingkai: (atas, tengah, bawah, lebar tiap sel)."""
    lebar = [max(3, len(_s(v)) + 2) for v in isi_list]
    atas = "┌" + "┬".join("─" * w for w in lebar) + "┐"
    tengah = "│" + "│".join(_s(v).center(w) for v, w in zip(isi_list, lebar)) + "│"
    bawah = "└" + "┴".join("─" * w for w in lebar) + "┘"
    return atas, tengah, bawah, lebar


def _g_variabel(s, lebar):
    keluar = []
    nama_w = max(len(_s(b[0])) for b in s["isi"])
    sorot = set(s.get("sorot", []))
    for b in s["isi"]:
        tipe = f"  ({b[2]})" if len(b) == 3 else ""
        tanda = "  ◀" if b[0] in sorot else ""
        keluar.append(f"{_s(b[0]).rjust(nama_w)} ─▶ [ {_s(b[1])} ]{tipe}{tanda}")
    return keluar


def _g_larik(s, lebar):
    isi = s["isi"]
    keluar = [s["nama"]] if s.get("nama") else []
    atas, tengah, bawah, lb = _deret_sel(isi)
    if len(atas) > lebar:
        keluar.append("[" + ", ".join(_s(v) for v in isi) + "]")
        keluar.append("indeks 0.." + str(len(isi) - 1))
        sorot = s.get("sorot", [])
        if sorot:
            keluar.append("disorot: indeks " + ", ".join(str(i) for i in sorot))
        for lbl, i in (s.get("penunjuk") or {}).items():
            keluar.append(f"{lbl} menunjuk indeks {i}")
        return keluar
    keluar += [atas, tengah, bawah]
    sorot = set(s.get("sorot", []))
    idx = " "
    for i, w in enumerate(lb):
        t = f"[{i}]" if i in sorot else str(i)
        idx += t.center(w) + " "
    keluar.append(idx.rstrip())
    r = s.get("rentang")
    if r:
        awal = 1 + sum(w + 1 for w in lb[:r[0]])
        akhir = sum(w + 1 for w in lb[:r[1]])
        keluar.append(" " * awal + "└" + "─" * max(0, akhir - awal - 2) + "┘ rentang"
                      f" [{r[0]}:{r[1]}]")
    for lbl, i in (s.get("penunjuk") or {}).items():
        tengah_sel = 1 + sum(w + 1 for w in lb[:i]) + lb[i] // 2
        keluar.append(" " * tengah_sel + "▲ " + lbl)
    return keluar


def _bentuk_alur(l):
    t = _s(l["teks"])
    return {"mulai": f"( {t} )", "selesai": f"( {t} )", "proses": f"[ {t} ]",
            "masukan": f"/ {t} /", "keluaran": f"/ {t} /",
            "keputusan": f"< {t} >"}.get(l["jenis"], t)


def _g_alur(s, lebar):
    langkah = s["langkah"]
    keluar = []
    for i, l in enumerate(langkah):
        baris_ = f"({i + 1}) {_bentuk_alur(l)}"
        if l["jenis"] == "keputusan":
            baris_ += f"  tidak ─▶ ({l['tidak'] + 1})"
        elif l.get("ke") is not None:
            baris_ += (f"  ─▶ ({l['ke'] + 1})" if l["ke"] > i
                       else f"  ↺ kembali ke ({l['ke'] + 1})")
        keluar.append(baris_)
        if i + 1 < len(langkah) and l["jenis"] != "selesai":
            if l["jenis"] == "keputusan":
                ya = l.get("ya")
                keluar.append("     │ ya" if ya in (None, i + 1) else f"     ya ─▶ ({ya + 1})")
            elif l.get("ke") is None:
                keluar.append("     │")
    return keluar


def _g_tumpukan(s, lebar):
    isi = [_s(v) for v in s["isi"]]
    w = max(len(v) for v in isi) + 2
    keluar = [s["label"]] if s.get("label") else []
    if s.get("mode") == "antrean":
        atas, tengah, bawah, _lb = _deret_sel(isi)
        if s.get("operasi"):
            keluar.append(s["operasi"])
        keluar += ["        " + atas, "depan ▶ " + tengah + " ◀ belakang", "        " + bawah]
        return keluar
    if s.get("operasi"):
        keluar.append(f"  {s['operasi']} ↓")
    keluar.append("┌" + "─" * w + "┐")
    for j, v in enumerate(reversed(isi)):
        keluar.append("│" + v.center(w) + "│" + ("  ◀ puncak" if j == 0 else ""))
        akhir = j == len(isi) - 1
        keluar.append(("└" if akhir else "├") + "─" * w + ("┘" if akhir else "┤"))
    return keluar


def _g_pohon(s, lebar):
    keluar = [_s(s["akar"]["teks"])]

    def turun(n, awalan):
        anak = n.get("anak", [])
        for j, a in enumerate(anak):
            akhir = j == len(anak) - 1
            keluar.append(awalan + ("└── " if akhir else "├── ") + _s(a["teks"]))
            turun(a, awalan + ("    " if akhir else "│   "))

    turun(s["akar"], "")
    return keluar


def _g_tabel(s, lebar):
    keluar = []
    for t, tb in enumerate(s["tabel"]):
        if t and s.get("panah"):
            keluar.append(f"   ↓ {s['panah']}")
        if tb.get("nama"):
            keluar.append(tb["nama"])
        kolom = [_s(c) for c in tb["kolom"]]
        isi = [[_s(v) for v in r] for r in tb["baris"]]
        w = [max([len(c)] + [len(r[i]) for r in isi]) for i, c in enumerate(kolom)]
        garis = "+" + "+".join("-" * (x + 2) for x in w) + "+"
        sorot = set(tb.get("sorot_baris", []))
        sk = set(tb.get("sorot_kolom", []))
        keluar.append(garis)
        keluar.append("|" + "|".join(
            f" {(c + '*' if c in sk else c).ljust(x)} " if c in sk and len(c) < x
            else f" {c.ljust(x)} " for c, x in zip(kolom, w)) + "|")
        keluar.append(garis)
        for r, baris_ in enumerate(isi):
            tanda = "  ◀" if r in sorot else ""
            keluar.append("|" + "|".join(f" {v.ljust(x)} " for v, x in zip(baris_, w))
                          + "|" + tanda)
        keluar.append(garis)
    return keluar


def _g_urutan(s, lebar):
    p = s["pelaku"]
    keluar = ["   ".join(f"[{x}]" for x in p)]
    for i, (a, b, teks) in enumerate(s["pesan"], 1):
        if a == b:
            keluar.append(f"{i}. {p[a]} ↺ {teks}")
        else:
            keluar.append(f"{i}. {p[a]} ──▶ {p[b]}: {teks}")
    return keluar


def _g_kotak(s, lebar):
    lapis = [("margin", s["margin"]), ("border", s["border"]),
             ("padding", s["padding"])]
    isi = f"isi: {s['isi']}"
    total = max(len(isi), max(len(f"{n} {v}") for n, v in lapis)) + 4 + 4 * len(lapis)
    keluar = [s["label"]] if s.get("label") else []
    for t, (nama, nilai) in enumerate(lapis):
        kiri, kanan = "│ " * t, " │" * t
        dalam = total - 4 * t
        keluar.append(kiri + "┌" + "─" * (dalam - 2) + "┐" + kanan)
        keluar.append(kiri + "│ " + f"{nama} {nilai}".ljust(dalam - 4) + " │" + kanan)
    t = len(lapis)
    kiri, kanan = "│ " * t, " │" * t
    dalam = total - 4 * t
    keluar.append(kiri + "┌" + "─" * (dalam - 2) + "┐" + kanan)
    keluar.append(kiri + "│ " + isi.ljust(dalam - 4) + " │" + kanan)
    keluar.append(kiri + "└" + "─" * (dalam - 2) + "┘" + kanan)
    for t in range(len(lapis) - 1, -1, -1):
        kiri, kanan = "│ " * t, " │" * t
        dalam = total - 4 * t
        keluar.append(kiri + "└" + "─" * (dalam - 2) + "┘" + kanan)
    return keluar


def _g_tata(s, lebar):
    item = [it[0] if isinstance(it, list) else it for it in s["item"]]
    if s["mode"] == "flex":
        aturan = [f"display: flex; flex-direction: {s.get('arah', 'row')}"]
        if s.get("justify"):
            aturan.append(f"justify-content: {s['justify']}")
        if s.get("align"):
            aturan.append(f"align-items: {s['align']}")
        if s.get("arah", "row") == "column":
            badan = [f"[ {x} ]" for x in item]
        else:
            badan = ["  ".join(f"[ {x} ]" for x in item)]
        return aturan + badan
    kolom = s["kolom"]
    aturan = [f"display: grid; grid-template-columns: repeat({kolom}, 1fr)"]
    deret, kini, isi_kini = [], 0, []
    for it in s["item"]:
        teks, rentang = (it[0], it[1]) if isinstance(it, list) else (it, 1)
        if kini + rentang > kolom:
            deret.append(isi_kini)
            isi_kini, kini = [], 0
        isi_kini.append((teks, rentang))
        kini += rentang
    if isi_kini:
        deret.append(isi_kini)
    sel = max(6, min(14, (lebar - 2) // kolom - 2))
    for r in deret:
        aturan.append("".join(f"[{teks.center(sel * rentang + 2 * (rentang - 1))}]"
                              for teks, rentang in r))
    return aturan


def _g_git(s, lebar):
    commit = s["commit"]
    cabang = []
    for c in commit:
        if c["cabang"] not in cabang:
            cabang.append(c["cabang"])
    lebar_nama = max(len(x) for x in cabang)
    langkah = 5
    keluar = []
    label = s.get("label") or {}
    head = s.get("head")
    for b in cabang:
        sel = [" "] * (len(commit) * langkah)
        posisi = [i for i, c in enumerate(commit) if c["cabang"] == b]
        for a, z in zip(posisi, posisi[1:]):
            for x in range(a * langkah + 1, z * langkah):
                sel[x] = "─"
        for i in posisi:
            for j, ch in enumerate(commit[i]["id"][:langkah - 1]):
                sel[i * langkah + j] = ch
        ujung = ""
        if b in label:
            ujung = f"  ◀ {b}" + (" (HEAD)" if head == b else "")
        keluar.append(f"{b.ljust(lebar_nama)} : {''.join(sel).rstrip()}{ujung}")
    for nama, cid in label.items():
        if nama not in cabang:
            keluar.append(f"label {nama} ─▶ {cid}" + (" (HEAD)" if head == nama else ""))
    if head is not None and head not in label:
        keluar.append(f"HEAD ─▶ {head}")
    for c in commit:
        induk = c.get("induk", [])
        if len(induk) > 1:
            keluar.append(f"{c['id']} menggabungkan {' dan '.join(induk)}")
        elif induk:
            asal = next(x for x in commit if x["id"] == induk[0])
            if asal["cabang"] != c["cabang"]:
                keluar.append(f"{c['id']} bercabang dari {induk[0]}")
    for c in commit:
        if c.get("pesan"):
            keluar.append(f"{c['id']}: {c['pesan']}")
    return keluar


def _dirujuk(s):
    """Id objek heap yang punya penunjuk: dari variabel ("@id") atau disebut
    di isi objek heap LAIN (node linked list, list berisi list)."""
    heap = s.get("heap") or []
    rujuk = {_s(b[1])[1:] for b in s["tumpukan"] if _s(b[1]).startswith("@")}
    for o in heap:
        for lain in heap:
            if lain is not o and re.search(r"(?<![\w])" + re.escape(o["id"]) + r"(?![\w])", lain["isi"]):
                rujuk.add(o["id"])
    return rujuk


def _g_memori(s, lebar):
    heap = {o["id"]: o["isi"] for o in s.get("heap") or []}
    keluar = [s.get("label_tumpukan") or "stack"]
    w = max(len(_s(b[0])) for b in s["tumpukan"])
    for nama, nilai in s["tumpukan"]:
        nilai = _s(nilai)
        if nilai.startswith("@"):
            keluar.append(f"  {nama.ljust(w)} │ ● ──▶ {nilai[1:]}: {heap[nilai[1:]]}")
        else:
            keluar.append(f"  {nama.ljust(w)} │ {nilai}")
    if heap:
        rujuk = _dirujuk(s)
        keluar.append(s.get("label_heap") or "heap")
        for i, isi in heap.items():
            keluar.append(f"  {i}: {isi}" + ("" if i in rujuk else "  (tanpa penunjuk)"))
    return keluar


def _g_bit(s, lebar):
    n, w = s["angka"], s.get("lebar", 8)
    bit = format(n, f"0{w}b")
    nilai = [2 ** (w - 1 - i) for i in range(w)]
    sel = len(str(nilai[0])) + 1
    keluar = [s["label"]] if s.get("label") else []
    if w * (sel + 1) > lebar:
        keluar.append(" ".join(bit[i:i + 4] for i in range(0, w, 4)))
    else:
        keluar.append(" ".join(str(v).rjust(sel) for v in nilai))
        keluar.append(" ".join(b.rjust(sel) for b in bit))
    jumlah = [str(v) for v, b in zip(nilai, bit) if b == "1"]
    keluar.append((" + ".join(jumlah) if jumlah else "0") + f" = {n}")
    return keluar


def nilai_kurva(c, n):
    """Langkah kerja kurva `c` untuk masukan berukuran n (dibulatkan)."""
    if c == "1":
        return 1
    if c == "log n":
        return round(math.log2(n)) if n > 1 else 0
    if c == "n":
        return n
    if c == "n log n":
        return round(n * math.log2(n)) if n > 1 else 0
    if c == "n^2":
        return n * n
    return 2 ** n


def _g_kurva(s, lebar):
    ns = (1, 2, 4, 8, 16, 32)
    w = 9
    keluar = ["langkah kerja untuk ukuran masukan n"]
    keluar.append("n".ljust(12) + "".join(str(n).rjust(w) for n in ns))
    for c in s["kurva"]:
        tanda = " ◀" if c == s.get("sorot") else ""
        sel = []
        for n in ns:
            v = nilai_kurva(c, n)
            sel.append((f"{v:.1e}" if v >= 10 ** 9 else str(v)).rjust(w))
        keluar.append(f"O({c})".ljust(12) + "".join(sel) + tanda)
    return keluar


_PENGGAMBAR = {
    "variabel": _g_variabel, "larik": _g_larik, "alur": _g_alur,
    "tumpukan": _g_tumpukan, "pohon": _g_pohon, "tabel": _g_tabel,
    "urutan": _g_urutan, "kotak": _g_kotak, "tata": _g_tata, "git": _g_git,
    "memori": _g_memori, "bit": _g_bit, "kurva": _g_kurva,
}


def susun(spes, lebar=76, nomor=None):
    """(kepala, gambar, keterangan): tiga daftar baris tanpa warna.

    Judul dan keterangan dibungkus ke `lebar`; gambarnya sudah menjorok dua
    spasi. Terminal mewarnai ketiganya berbeda, jadi ia butuh batasnya.
    """
    import textwrap
    kepala_teks = f"Gambar {nomor}: {spes['judul']}" if nomor else f"Gambar: {spes['judul']}"
    kepala = textwrap.wrap(kepala_teks, lebar) or [kepala_teks]
    gambar = ["  " + g for g in _PENGGAMBAR[spes["jenis"]](spes, lebar - 4)]
    ket = textwrap.wrap(spes["ket"], lebar) if spes.get("ket") else []
    return kepala, gambar, ket


def baris(spes, lebar=76, nomor=None):
    """Gambar terminal: judul, gambar menjorok dua spasi, keterangan. Tanpa warna."""
    kepala, gambar, ket = susun(spes, lebar, nomor)
    return kepala + gambar + ket
