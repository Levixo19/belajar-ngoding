"""Ekspor kurikulum dari literal Python ke JSON, lalu BUKTIKAN tidak ada yang hilang.

Kenapa ada: isi kurikulum (1.062 materi, 2.159 soal, 558 latihan, 1.356 gambar)
adalah satu-satunya bagian repo ini yang tidak bisa ditulis ulang. Selama ia
berupa literal Python, ia cuma bisa dibaca Python. JSON membuatnya bisa dibaca
apa pun, dan itu yang membuat migrasi ke stack lain tidak mempertaruhkannya.

CARA MEMBUKTIKANNYA, dan kenapa bukan dengan menjalankan tes.
`tests/test_data.py` adalah tes SKEMA: field wajib ada, judul unik, baris tidak
kepanjangan. Semuanya tetap hijau walau sebuah nilai berubah, asal bentuknya
masih sah. Jadi yang dipakai di sini pembanding langsung: ekspor, impor balik,
lalu `==` terhadap objek Python aslinya. Itu menangkap urutan kunci, tuple yang
berubah jadi list, dan nilai yang bergeser -- hal-hal yang lolos dari tes skema.

TIGA JEBAKAN yang ditutup sengaja:

* Kuis diekspor MENTAH, sebelum `normalisasi.seimbangkan_kuis` memutarnya.
  Kalau yang diekspor hasil putaran lalu pembacanya memutar lagi, opsi berputar
  dua kali -- dan `test_normalisasi_menjaga_jawaban_tetap_benar` TETAP HIJAU,
  karena rotasi memang menjaga korelasi opsi dengan jawabannya. Yang rusak diam
  diam cuma penjelasan soal yang menyebut posisi opsi tertentu. Karena itu
  rotasi tetap tinggal di satu tempat, dan sidik SHA-256 hasil pasca-rotasi
  ikut ditulis supaya pergeserannya ketahuan.
* `data/karier.py` memutasi `PROFESI` saat diimpor (menyuntik `gaji`), dan
  `GAJI` adalah satu-satunya sarang tuple di seluruh `data/`. Yang diekspor
  `PROFESI` SESUDAH impor, dan `GAJI` tidak diekspor terpisah.
* Validator yang hari ini jalan saat impor (`kurikulum_tech.bab()` menolak
  jumlah bab yang tidak cocok, 13 pemeriksa `inti/visual.py`) akan berhenti
  jalan begitu JSON jadi sumber. Keduanya dijalankan di sini sebagai GERBANG:
  ekspor ditolak kalau salah satu mengeluh.

    python3 alat/ekspor_konten.py            # periksa + buktikan, tanpa menulis
    python3 alat/ekspor_konten.py --tulis    # tulis packages/konten/
"""

import argparse
import hashlib
import importlib
import json
import os
import shutil
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from data.normalisasi import seimbangkan_kuis  # noqa: E402
from inti import visual  # noqa: E402
from inti.kurikulum import LANGUAGES  # noqa: E402

TUJUAN = os.path.join(AKAR, "packages", "konten")

# Medan entri LANGUAGES yang bukan konten; `materials`/`quizzes`/`exercises`
# ditulis terpisah supaya berkasnya terbaca.
META = ("key", "label", "runner", "tematik", "ranah", "run_info")


def kuis_mentah(key):
    """Kuis SEBELUM diputar `seimbangkan_kuis`, dari modulnya langsung."""
    modul = importlib.import_module(f"data.{key}_quizzes")
    return getattr(modul, f"{key.upper()}_QUIZZES")


def sidik(obj):
    """SHA-256 atas bentuk JSON yang stabil."""
    teks = json.dumps(obj, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(teks.encode("utf-8")).hexdigest()


def susun():
    """{jalur relatif: objek} untuk seluruh konten, plus sidik pasca-rotasi."""
    berkas, sidik_kuis = {}, {}

    for lang in LANGUAGES:
        key = lang["key"]
        mentah = kuis_mentah(key)
        # Pagar: yang mentah harus memutar jadi persis yang dipakai aplikasi.
        if seimbangkan_kuis(mentah) != lang["quizzes"]:
            raise ValueError(f"{key}: kuis mentah tidak memutar jadi yang dipakai")
        sidik_kuis[key] = sidik(lang["quizzes"])
        berkas[f"kurikulum/{key}.json"] = {
            **{k: lang[k] for k in META if k in lang},
            "materi": lang["materials"],
            "kuis_mentah": mentah,
            "latihan": lang["exercises"],
        }

    from data.bab import BAB
    from data.karier import PROFESI, RUMPUN
    from data.kuis_materi import KUIS_MATERI

    berkas["bab.json"] = BAB
    berkas["kuis_materi.json"] = KUIS_MATERI
    berkas["karier.json"] = {"rumpun": RUMPUN, "profesi": PROFESI}

    for lang in LANGUAGES:
        g = visual.data_bahasa(lang["key"])
        if g:
            berkas[f"visual/{lang['key']}.json"] = g

    berkas["sidik.json"] = {
        "catatan": "SHA-256 kuis SESUDAH seimbangkan_kuis. Berubah = rotasi "
                   "bergeser; periksa sebelum menerima.",
        "kuis_pasca_rotasi": sidik_kuis,
    }
    return berkas


def gerbang_validator():
    """Jalankan validator yang hari ini cuma hidup saat impor Python."""
    keluhan = []

    from data import kurikulum_tech
    try:
        kurikulum_tech.bab()          # menolak jumlah bab != jumlah materi
    except ValueError as e:
        keluhan.append(f"kurikulum_tech.bab(): {e}")

    for lang in LANGUAGES:
        key = lang["key"]
        per_judul = {visual.judul_tanpa_nomor(m["title"]): m
                     for m in lang["materials"]}
        for judul, daftar in visual.data_bahasa(key).items():
            m = per_judul.get(judul)
            if m is None:
                keluhan.append(f"{key}: gambar untuk materi tak dikenal {judul!r}")
                continue
            for i, spes in enumerate(daftar):
                for pesan in visual.periksa(spes, len(m["sections"])):
                    keluhan.append(f"{key}/{judul} gambar {i}: {pesan}")
    return keluhan


def buktikan(berkas):
    """Impor balik hasil ekspor dan adu dengan objek Python aslinya."""
    keluhan = []
    pulang = {j: json.loads(json.dumps(o, ensure_ascii=False))
              for j, o in berkas.items()}

    for lang in LANGUAGES:
        key = lang["key"]
        d = pulang[f"kurikulum/{key}.json"]
        if d["materi"] != lang["materials"]:
            keluhan.append(f"{key}: materi berubah setelah roundtrip")
        if d["latihan"] != lang["exercises"]:
            keluhan.append(f"{key}: latihan berubah setelah roundtrip")
        if seimbangkan_kuis(d["kuis_mentah"]) != lang["quizzes"]:
            keluhan.append(f"{key}: kuis tidak pulih setelah roundtrip")
        for k in META:
            if k in lang and d.get(k) != lang[k]:
                keluhan.append(f"{key}: meta {k} berubah")

    from data.bab import BAB
    from data.karier import PROFESI, RUMPUN
    from data.kuis_materi import KUIS_MATERI
    if pulang["bab.json"] != BAB:
        keluhan.append("bab berubah setelah roundtrip")
    if pulang["kuis_materi.json"] != KUIS_MATERI:
        keluhan.append("kuis_materi berubah setelah roundtrip")
    # PROFESI memuat tuple di `gaji`; JSON mengubahnya jadi list. Yang
    # dibandingkan karena itu bentuk JSON-nya, bukan objek Python-nya.
    asli = json.loads(json.dumps({"rumpun": RUMPUN, "profesi": PROFESI},
                                 ensure_ascii=False))
    if pulang["karier.json"] != asli:
        keluhan.append("karier berubah setelah roundtrip")

    for lang in LANGUAGES:
        j = f"visual/{lang['key']}.json"
        if j in pulang and pulang[j] != visual.data_bahasa(lang["key"]):
            keluhan.append(f"{lang['key']}: gambar berubah setelah roundtrip")

    # Kunci angka ditolak: V8 menata ulang kunci berbentuk indeks saat
    # JSON.parse, jadi "0"/"1" sebagai kunci objek tidak aman dibawa ke JS.
    def angka(o, jalur=""):
        if isinstance(o, dict):
            for k, v in o.items():
                if str(k).isdigit():
                    keluhan.append(f"kunci angka {k!r} di {jalur}")
                angka(v, f"{jalur}/{k}")
        elif isinstance(o, list):
            for v in o:
                angka(v, jalur)
    for j, o in pulang.items():
        angka(o, j)
    return keluhan


def tulis(berkas):
    if os.path.isdir(TUJUAN):
        shutil.rmtree(TUJUAN)
    for jalur, obj in berkas.items():
        penuh = os.path.join(TUJUAN, jalur)
        os.makedirs(os.path.dirname(penuh), exist_ok=True)
        with open(penuh, "w", encoding="utf-8") as f:
            json.dump(obj, f, ensure_ascii=False, indent=1)
            f.write("\n")
    asal = os.path.join(AKAR, "data", "pustaka")
    shutil.copytree(asal, os.path.join(TUJUAN, "pustaka"))
    return len(berkas) + len(os.listdir(asal))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tulis", action="store_true")
    a = ap.parse_args()

    keluhan = gerbang_validator()
    if keluhan:
        print("DITOLAK, validator mengeluh:")
        print("\n".join("  - " + k for k in keluhan[:20]))
        return 1

    berkas = susun()
    keluhan = buktikan(berkas)

    byte = sum(len(json.dumps(o, ensure_ascii=False)) for o in berkas.values())
    print(f"{len(berkas)} berkas, {byte / 1e6:.1f} MB JSON")
    print(f"  kurikulum: {sum(1 for j in berkas if j.startswith('kurikulum/'))}")
    print(f"  gambar   : {sum(1 for j in berkas if j.startswith('visual/'))}")

    if keluhan:
        print("DITOLAK, roundtrip tidak lossless:")
        print("\n".join("  - " + k for k in keluhan[:20]))
        return 1
    print("roundtrip LOSSLESS: materi, kuis, latihan, bab, kuis_materi, "
          "karier, gambar semuanya pulih utuh")

    if a.tulis:
        print(f"  ditulis {tulis(berkas)} berkas ke packages/konten/")
    else:
        print("  (belum ditulis; tambahkan --tulis)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
