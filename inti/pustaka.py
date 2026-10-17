"""Pustaka: ribuan tautan belajar dari repo kurasi, bisa dicari dan disaring.

Datanya DIHASILKAN `alat/panen_pustaka.py` ke `data/pustaka/*.json`, satu
berkas per sumber, lengkap dengan lisensi dan atribusinya. Modul ini cuma
membaca, memetakan topik ke kurikulum, dan mencari. Ia tidak tahu ada
terminal atau web: `layar/pustaka.py` dan `webapp/api.py` sama-sama memanggil
`cari()` dan `ringkasan_kurikulum()` di sini, jadi kedua antarmuka menampilkan
isi yang sama persis.

Pemetaan ke kurikulum dihitung SAAT DIMUAT dari jalur topik tiap entri, bukan
disimpan di JSON. Alasannya: daftar kurikulum milik aplikasi ini, sedangkan
data pustaka milik repo sumbernya. Menambah kurikulum baru cukup menambah satu
baris di `TOPIK_KURIKULUM`, tanpa memanen ulang.
"""

import copy
import json
import os
import re
import threading

FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                      "data", "pustaka")

# Urutan di sini adalah urutan tampil penyaring "jenis".
JENIS = {
    "buku": "Buku",
    "kursus": "Kursus",
    "tutorial": "Tutorial interaktif",
    "proyek": "Proyek praktik",
    "soal": "Kumpulan soal",
    "contekan": "Contekan",
    "playground": "Playground",
    "podcast": "Podcast & screencast",
    "bacaan": "Bacaan",
    "peta": "Peta belajar",
    "pustaka": "Pustaka Python",
    "api": "API publik",
    "daftar": "Daftar kurasi",
}

BAHASA = {"id": "Indonesia", "en": "Inggris"}

# Ruas topik (huruf kecil) -> kunci kurikulum. Satu ruas boleh ke beberapa
# kurikulum: buku "C/C++" berguna untuk keduanya.
TOPIK_KURIKULUM = {
    "html": ["html"], "html and css": ["html", "css"], "html5": ["html"],
    "css": ["css"], "bootstrap": ["css"], "sass": ["css"],
    "tailwind css": ["css"], "web performance": ["css", "javascript"],
    "java": ["java"], "spring": ["java", "aplikasi"], "spring boot": ["java", "aplikasi"],
    "jvm": ["java"], "maven": ["java"], "gradle": ["java", "kotlin"],
    "sql": ["sql"], "mysql": ["sql"], "postgresql": ["sql"], "sqlite": ["sql"],
    "sql server": ["sql"], "sql (implementation agnostic)": ["sql"],
    "databases": ["sql"], "database": ["sql"], "dbms": ["sql"],
    "relational database management system (rdbms)": ["sql"],
    "python": ["python"], "django": ["python"], "flask": ["python"],
    "fastapi": ["python"], "jupyter": ["python"], "pytorch": ["python"],
    "javascript": ["javascript"], "node.js": ["javascript"], "nodejs": ["javascript"],
    "node": ["javascript"], "react": ["javascript"], "react.js": ["javascript"],
    "vue.js": ["javascript"], "angular": ["javascript", "typescript"],
    "angularjs": ["javascript"], "svelte": ["javascript"], "next.js": ["javascript"],
    "jquery": ["javascript"], "deno": ["javascript", "typescript"],
    "redux": ["javascript"], "nest.js": ["javascript", "typescript"],
    "d3.js": ["javascript"], "electron": ["javascript"], "webpack": ["javascript"],
    "ember.js": ["javascript"], "backbone.js": ["javascript"],
    "typescript": ["typescript"],
    "c": ["c"], "c/c++": ["c", "cpp"], "c / c++": ["c", "cpp"], "c++": ["cpp"],
    "go": ["go"], "golang": ["go"],
    "bash": ["bash"], "bash / shell": ["bash"], "shell scripting": ["bash"],
    "shell": ["bash"], "awk": ["bash"], "command line": ["bash"],
    "regular expressions": ["bash", "python", "javascript"],
    "linux": ["fedora", "bash"], "unix": ["fedora", "bash"],
    "operating systems": ["fedora"],
    "git": ["git"], "version control systems": ["git"], "version control": ["git"],
    "c#": ["csharp"], ".net framework": ["csharp", "vb"], ".net core / .net": ["csharp"],
    "asp.net": ["csharp"], "asp.net core": ["csharp"], "blazor": ["csharp"],
    "visual basic": ["vb"], "vb.net": ["vb"],
    "rust": ["rust"],
    "php": ["php"], "laravel": ["php"], "codeigniter": ["php"], "symfony": ["php"],
    "yii": ["php"], "wordpress": ["php"],
    "ruby": ["ruby"], "ruby on rails": ["ruby"], "rails": ["ruby"],
    "kotlin": ["kotlin"], "android": ["kotlin", "java"],
    "software architecture": ["aplikasi"], "design patterns": ["aplikasi"],
    "software engineering": ["aplikasi"], "testing": ["aplikasi"],
    "unit testing": ["aplikasi"], "system design": ["aplikasi"],
    "system design, scalability, data handling": ["aplikasi"],
}

# Sumber yang seluruh isinya milik satu kurikulum, apa pun topiknya.
SUMBER_KURIKULUM = {"python": ["python"]}

# Peta roadmap.sh -> kurikulum, lewat slug alamatnya.
PETA_KURIKULUM = {
    "html": ["html"], "css": ["css"], "java": ["java"], "spring-boot": ["java", "aplikasi"],
    "sql": ["sql"], "postgresql-dba": ["sql"], "python": ["python"],
    "javascript": ["javascript"], "nodejs": ["javascript"], "react": ["javascript"],
    "vue": ["javascript"], "angular": ["javascript", "typescript"],
    "typescript": ["typescript"], "cpp": ["cpp"], "golang": ["go"],
    "shell-bash": ["bash"], "linux": ["fedora", "bash"], "git-github": ["git"],
    "aspnet-core": ["csharp"], "rust": ["rust"], "php": ["php"], "laravel": ["php"],
    "ruby": ["ruby"], "kotlin": ["kotlin"], "android": ["kotlin", "java"],
    "software-design-architecture": ["aplikasi"], "system-design": ["aplikasi"],
    "backend": ["aplikasi"], "frontend": ["html", "css", "javascript"],
    "full-stack": ["html", "css", "javascript", "aplikasi"],
}

_CACHE = None
_KUNCI = threading.Lock()

# Datanya statis selama proses hidup, jadi hasil `cari()` dan
# `ringkasan_kurikulum()` dimemo. Isinya SALINAN yang dikembalikan, supaya
# pemanggil yang menyunting hasilnya tidak meracuni pemanggil berikutnya.
_MEMO_CARI = {}
_MEMO_RINGKASAN = {}
_MAKS_MEMO = 512


def _kurikulum_entri(e, sumber):
    if sumber in SUMBER_KURIKULUM:
        # Topik "Testing" di awesome-python berarti pustaka uji PYTHON, bukan
        # bacaan untuk kurikulum Bikin Aplikasi yang berbahasa Java.
        return list(SUMBER_KURIKULUM[sumber])
    keluar = []
    if e["jenis"] == "peta":
        slug = e["url"].rstrip("/").rsplit("/", 1)[-1]
        keluar += PETA_KURIKULUM.get(slug, [])
    for jalur in e["topik"]:
        for ruas in jalur.split(" › "):
            keluar += TOPIK_KURIKULUM.get(ruas.strip().lower(), [])
    return sorted(set(keluar))


def _muat():
    global _CACHE
    if _CACHE is not None:
        return _CACHE
    with _KUNCI:
        if _CACHE is None:
            _CACHE = _muat_dari_berkas()
    return _CACHE


def panaskan():
    """Muat data di thread latar supaya permintaan pertama tidak membayarnya."""
    utas = threading.Thread(target=_muat, daemon=True, name="pustaka-panas")
    utas.start()
    return utas


def _muat_dari_berkas():
    sumber = {}
    entri = []
    if os.path.isdir(FOLDER):
        for nama in sorted(os.listdir(FOLDER)):
            if not nama.endswith(".json"):
                continue
            with open(os.path.join(FOLDER, nama), encoding="utf-8") as f:
                isi = json.load(f)
            meta = isi["sumber"]
            sumber[meta["kunci"]] = meta
            for i, e in enumerate(isi["entri"]):
                e = dict(e)
                e["id"] = f"{meta['kunci']}-{i}"
                e["sumber"] = meta["kunci"]
                e["kurikulum"] = _kurikulum_entri(e, meta["kunci"])
                # Teks yang dicari, dikecilkan sekali saja di sini.
                e["_judul"] = e["judul"].lower()
                e["_semua"] = " ".join([e["judul"], " ".join(e["topik"]),
                                        e.get("catatan", "")]).lower()
                entri.append(e)
    return {"sumber": sumber, "entri": entri}


def lupakan_cache():
    """Untuk tes yang mengganti FOLDER."""
    global _CACHE
    with _KUNCI:
        _CACHE = None
        _MEMO_CARI.clear()
        _MEMO_RINGKASAN.clear()


def daftar_sumber():
    """Semua sumber beserta lisensi, atribusi, dan jumlah entrinya."""
    data = _muat()
    jumlah = {}
    for e in data["entri"]:
        jumlah[e["sumber"]] = jumlah.get(e["sumber"], 0) + 1
    return [dict(m, jumlah=jumlah.get(k, 0)) for k, m in data["sumber"].items()]


def total():
    return len(_muat()["entri"])


def _publik(e):
    return {k: v for k, v in e.items() if not k.startswith("_")}


def _skor(e, kata):
    """Skor relevansi; None kalau ada kata kueri yang tidak ditemukan."""
    skor = 0
    for k in kata:
        if k in e["_judul"]:
            skor += 3 if re.search(r"\b" + re.escape(k), e["_judul"]) else 2
        elif k in e["_semua"]:
            skor += 1
        else:
            return None
    return skor


def cari(kueri="", kurikulum=None, jenis=None, bahasa=None, sumber=None,
         halaman=1, per_halaman=40):
    """Cari dan saring (dimemo; lihat `_cari_hitung` untuk aturannya)."""
    kunci = (kueri or "", kurikulum or None, jenis or None, bahasa or None,
             sumber or None, halaman, per_halaman)
    try:
        hasil = _MEMO_CARI.get(kunci)
    except TypeError:               # argumen tak bisa di-hash: hitung saja
        return _cari_hitung(kueri, kurikulum, jenis, bahasa, sumber,
                            halaman, per_halaman)
    if hasil is None:
        hasil = _cari_hitung(kueri, kurikulum, jenis, bahasa, sumber,
                             halaman, per_halaman)
        if len(_MEMO_CARI) >= _MAKS_MEMO:
            _MEMO_CARI.clear()
        _MEMO_CARI[kunci] = hasil
    return copy.deepcopy(hasil)


def _cari_hitung(kueri, kurikulum, jenis, bahasa, sumber, halaman, per_halaman):
    """Cari dan saring. Semua penyaring opsional; kueri kosong = jelajah.

    Mengembalikan hasil SATU halaman plus `segi`: cacah tiap nilai penyaring
    untuk himpunan yang sudah tersaring oleh penyaring LAIN. Dengan begitu
    angka di samping "Buku (120)" selalu jujur terhadap pilihan yang lain.
    """
    kata = [k for k in re.split(r"\s+", (kueri or "").lower().strip()) if k]
    saring = {"kurikulum": kurikulum or None, "jenis": jenis or None,
              "bahasa": bahasa or None, "sumber": sumber or None}

    def cocok(e, kecuali=None):
        for nama, nilai in saring.items():
            if nama == kecuali or nilai is None:
                continue
            if nama == "kurikulum":
                if nilai not in e["kurikulum"]:
                    return False
            elif e[nama] != nilai:
                return False
        return True

    hasil = []
    segi = {"kurikulum": {}, "jenis": {}, "bahasa": {}, "sumber": {}}
    for e in _muat()["entri"]:
        if kata:
            s = _skor(e, kata)
            if s is None:
                continue
        else:
            s = 0
        for nama in segi:
            if cocok(e, kecuali=nama):
                nilai = e["kurikulum"] if nama == "kurikulum" else [e[nama]]
                for n in nilai:
                    segi[nama][n] = segi[nama].get(n, 0) + 1
        if cocok(e):
            hasil.append((s, e))

    # Bahasa Indonesia lebih dulu: hanya sedikit, dan itulah yang paling
    # mungkin dibaca sampai habis oleh pelajar aplikasi ini.
    urutan_jenis = list(JENIS)
    peringkat = {j: n for n, j in enumerate(urutan_jenis)}
    hasil.sort(key=lambda p: (-p[0], p[1]["bahasa"] != "id",
                              peringkat.get(p[1]["jenis"], 99),
                              p[1]["_judul"]))
    halaman = max(1, int(halaman or 1))
    per_halaman = max(1, min(int(per_halaman or 40), 200))
    awal = (halaman - 1) * per_halaman
    return {
        "total": len(hasil),
        "halaman": halaman,
        "per_halaman": per_halaman,
        "hasil": [_publik(e) for _, e in hasil[awal:awal + per_halaman]],
        "segi": segi,
    }


def ringkasan_kurikulum(kunci, pilihan=6):
    """Dimemo; lihat `_ringkasan_hitung`."""
    k = (kunci, pilihan)
    hasil = _MEMO_RINGKASAN.get(k)
    if hasil is None:
        hasil = _ringkasan_hitung(kunci, pilihan)
        _MEMO_RINGKASAN[k] = hasil
    return copy.deepcopy(hasil)


def _ringkasan_hitung(kunci, pilihan):
    """Cacah per jenis untuk satu kurikulum, plus beberapa tautan pembuka.

    Pembukanya dipilih tetap (bukan acak) supaya terminal dan web
    menampilkan tautan yang sama: berbahasa Indonesia dulu, lalu buku dan
    kursus, lalu yang lain, tiap jenis paling banyak dua.
    """
    data = [e for e in _muat()["entri"] if kunci in e["kurikulum"]]
    per_jenis = {}
    for e in data:
        per_jenis[e["jenis"]] = per_jenis.get(e["jenis"], 0) + 1
    urutan_jenis = list(JENIS)
    calon = sorted(data, key=lambda e: (e["bahasa"] != "id",
                                        urutan_jenis.index(e["jenis"]),
                                        e["_judul"]))
    pembuka = []
    dipakai = {}
    for e in calon:
        if dipakai.get(e["jenis"], 0) >= 2:
            continue
        dipakai[e["jenis"]] = dipakai.get(e["jenis"], 0) + 1
        pembuka.append(_publik(e))
        if len(pembuka) >= pilihan:
            break
    return {
        "total": len(data),
        "per_jenis": [{"jenis": j, "label": JENIS[j], "jumlah": per_jenis[j]}
                      for j in urutan_jenis if per_jenis.get(j)],
        "pembuka": pembuka,
    }
