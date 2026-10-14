"""Mesin Peta Karier: kesiapan, kuis kecocokan, dan jalur perpindahan.

Datanya di `data/karier.py`. Di sini cuma aturannya, dan aturan itu cuma
boleh ada di satu tempat: terminal dan web sama-sama memanggil fungsi di
modul ini, jadi angka "kesiapanmu 40%" tidak pernah berbeda di dua layar.

KESIAPAN dibangun dari angka yang SUDAH ada, bukan definisi baru. Persen tiap
kurikulum diambil dari `progress.statistik_bahasa` -- persis angka "x%
selesai" di halaman bahasa. Satu kelompok bekal ("salah satu dari Python,
Java, Go") memakai kurikulum terbaiknya; kesiapan sebuah profesi adalah
rata-rata kelompok bekalnya. Kurikulum pelengkap ditampilkan tapi tidak
dihitung, supaya profesi tidak terasa mustahil gara-gara bacaan tambahan.

Modul ini menerima `languages` sebagai argumen alih-alih mengimpor `main`:
paket `pelajar` tidak boleh mengimpor lapisan di atasnya.
"""

import heapq
import math

from data import karier as data_karier
from pelajar import progress

PROFESI = data_karier.PROFESI
PER_ID = {p["id"]: p for p in PROFESI}

# Biaya melewati profesi sebagai PERANTARA dalam jalur perpindahan. Orang
# jarang menjadi arsitek hanya supaya bisa pindah ke peran lain, jadi peran
# senior mahal sebagai batu loncatan.
_BIAYA_LEWAT = {"pemula": 0.0, "menengah": 0.4, "senior": 2.5}


def persen_kurikulum(languages, data=None):
    """{kunci kurikulum: persen 0..100}, dari definisi progres yang sama."""
    data = data if data is not None else progress.load_progress()
    keluar = {}
    for lang in languages:
        s = progress.statistik_bahasa(
            data, lang["key"], len(lang["materials"]), len(lang["quizzes"]),
            len(lang["exercises"]))
        keluar[lang["key"]] = s["persen"]
    return keluar


def kesiapan(profesi, persen):
    """Kesiapan satu profesi dari peta persen kurikulum.

    Mengembalikan persen total dan rincian per kelompok, termasuk kurikulum
    mana yang sedang menjadi wakil kelompok "salah satu".
    """
    kelompok = []
    for grup in profesi["bekal"]:
        terbaik = max(grup, key=lambda k: (persen.get(k, 0.0), -grup.index(k)))
        kelompok.append({
            "pilihan": list(grup),
            "wakil": terbaik,
            "persen": persen.get(terbaik, 0.0),
        })
    total = (sum(k["persen"] for k in kelompok) / len(kelompok)) if kelompok else 0.0
    return {"persen": total, "kelompok": kelompok}


def semua_kesiapan(languages, data=None):
    persen = persen_kurikulum(languages, data)
    return {p["id"]: kesiapan(p, persen)["persen"] for p in PROFESI}


def sisi():
    """Sisi graf tak berarah tanpa kembar; 'naik' menang atas 'dekat'."""
    keluar = {}
    for p in PROFESI:
        for daftar, jenis in ((p["naik"], "naik"), (p["dekat"], "dekat")):
            for q in daftar:
                if q not in PER_ID or q == p["id"]:
                    continue
                kunci = tuple(sorted((p["id"], q)))
                ada = keluar.get(kunci)
                if ada is None or (ada == "dekat" and jenis == "naik"):
                    keluar[kunci] = jenis
    return [{"a": a, "b": b, "jenis": j} for (a, b), j in sorted(keluar.items())]


def tetangga(pid):
    hasil = set()
    for s in sisi():
        if s["a"] == pid:
            hasil.add(s["b"])
        elif s["b"] == pid:
            hasil.add(s["a"])
    return sorted(hasil)


def jalur(dari, ke):
    """Jalur perpindahan paling realistis dari satu profesi ke profesi lain.

    Dijkstra berbobot: relasi 'naik' sedikit lebih murah daripada 'dekat',
    dan melewati peran senior sebagai perantara dikenai biaya tambahan.
    Tetangga diproses berurutan menurut id supaya hasilnya deterministik.
    """
    if dari not in PER_ID or ke not in PER_ID:
        return None
    if dari == ke:
        return [dari]
    adj = {}
    for s in sisi():
        w = 1.0 if s["jenis"] == "naik" else 1.2
        adj.setdefault(s["a"], []).append((s["b"], w))
        adj.setdefault(s["b"], []).append((s["a"], w))
    jarak = {dari: 0.0}
    asal = {}
    antre = [(0.0, dari)]
    while antre:
        d, simpul = heapq.heappop(antre)
        if d > jarak.get(simpul, math.inf):
            continue
        if simpul == ke:
            break
        for lanjut, w in sorted(adj.get(simpul, [])):
            biaya = d + w + (0.0 if lanjut == ke
                             else _BIAYA_LEWAT[PER_ID[lanjut]["jenjang"]])
            if biaya < jarak.get(lanjut, math.inf) - 1e-9:
                jarak[lanjut] = biaya
                asal[lanjut] = simpul
                heapq.heappush(antre, (biaya, lanjut))
    if ke not in jarak:
        return None
    hasil = [ke]
    while hasil[0] != dari:
        hasil.insert(0, asal[hasil[0]])
    return hasil


def celah_bekal(dari, ke):
    """Kelompok bekal profesi tujuan yang tidak tercakup bekal profesi asal."""
    punya = {k for grup in PER_ID[dari]["bekal"] for k in grup}
    return [grup for grup in PER_ID[ke]["bekal"] if not (set(grup) & punya)]


def skor_kuis(pilihan):
    """`pilihan`: daftar indeks opsi per soal (None = dilewati).

    Mengembalikan tiga profesi teratas beserta keahlian yang membuatnya cocok.
    """
    bobot = {}
    for soal, i in zip(data_karier.KUIS, pilihan):
        if i is None or not (0 <= i < len(soal["opsi"])):
            continue
        for k, v in soal["opsi"][i]["bobot"].items():
            bobot[k] = bobot.get(k, 0) + v
    peringkat = []
    for p in PROFESI:
        cocok = [k for k in p["keahlian"] if bobot.get(k)]
        skor = sum(bobot[k] for k in cocok) / math.sqrt(len(p["keahlian"]) or 1)
        if skor > 0:
            peringkat.append((-skor, p["id"], cocok))
    peringkat.sort()
    return [{"id": pid, "skor": round(-s, 3), "cocok": cocok}
            for s, pid, cocok in peringkat[:3]]


def ringkasan(languages, data=None):
    """Semua yang dibutuhkan layar karier dalam satu kali baca progres."""
    persen = persen_kurikulum(languages, data)
    label = {l["key"]: l["label"] for l in languages}
    profesi = []
    for p in PROFESI:
        k = kesiapan(p, persen)
        profesi.append(dict(p, kesiapan=k["persen"], kelompok=k["kelompok"]))
    return {
        "rumpun": data_karier.RUMPUN,
        "jenjang": data_karier.JENJANG,
        "keahlian": data_karier.KEAHLIAN,
        "kuis": [{"q": s["q"], "opsi": [o["label"] for o in s["opsi"]]}
                 for s in data_karier.KUIS],
        "profesi": profesi,
        "sisi": sisi(),
        "kurikulum": {k: {"label": label.get(k, k), "persen": v}
                      for k, v in persen.items()},
    }
