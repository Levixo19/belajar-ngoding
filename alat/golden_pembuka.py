"""Rekaman acuan `ringkasPembuka` untuk `packages/web/uji/golden-pembuka.json`.

Kenapa ada. Panel layar Langit menampilkan paragraf pembuka sebuah materi
sebagai deskripsinya. Aturan memenggal paragraf itu ditulis DUA kali: di sini
(Python, acuan) dan di `komponen/lensa-teks.ts`. Dua tulisan dari satu aturan
menyimpang diam-diam, jadi yang satu diuji terhadap rekaman yang dibangkitkan
oleh yang lain, dan rekaman itu harus bisa dibangkitkan ULANG dari repo ini:
rekaman acuan tanpa pembangkit bukan acuan, hanya angka yang pernah benar.

Aturannya (jangan diubah satu sisi saja):

* kumpulkan blok `teks` berurutan dari awal bagian pertama; berhenti di blok
  bukan-teks atau berperan `jebakan`; blok ke-2 dan seterusnya hanya bila
  tanpa peran, >= 30 karakter, dan berakhir `. ! ?`;
* pecah kalimat di `(?<=[.!?])\\s+(?=[A-Z0-9"“(<`'])` dan sambung kembali di
  singkatan (dll dsb dst mis yg dgn tsb no vs bdk cth spt hlm ket);
* buang kalimat penutup `:`; bila SEMUANYA berakhir `:`, jadikan titik;
* ambil paling banyak 3 kalimat dan 260 karakter; kalimat pertama yang lebih
  panjang dipotong di spasi terakhir lalu diberi "…".

Pilihan kasusnya mewakili tiap CABANG aturan (dua per kombinasi cabang yang
muncul di 1.062 materi, benih tetap 20261027) ditambah 40 acak dan sembilan kasus tulis tangan, jadi sebuah
cabang yang dibuang dari TypeScript terlihat sebagai selisih, bukan lolos
karena korpusnya kebetulan tidak memuatnya.

    python3 alat/golden_pembuka.py            # periksa, tanpa menulis
    python3 alat/golden_pembuka.py --tulis    # tulis berkasnya
"""

import collections
import contextlib
import json
import os
import random
import re
import sys
import tempfile
from unittest import mock

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BERKAS = os.path.join(AKAR, "packages", "web", "uji", "golden-pembuka.json")
BENIH = 20261027
MAKS_KALIMAT = 3
MAKS_KARAKTER = 260
MIN_LANJUTAN = 30
SINGKATAN = re.compile(r"\b(?:dll|dsb|dst|mis|yg|dgn|tsb|no|vs|bdk|cth|spt|hlm|ket)\.$", re.I)
AKHIR = re.compile(r"[.!?]$")
BATAS_KALIMAT = r"(?<=[.!?])\s+(?=[A-Z0-9\"“(<`'])"

# Kasus yang tidak ada di korpus nyata tetapi menjaga satu cabang atau satu
# tepi aturan (singkatan di tengah tiga kalimat, jebakan di awal, kalimat
# tunggal > 260 karakter). Ditulis tangan; ringkasannya tetap dihitung dari
# aturan, jadi kasus ini tidak bisa menyimpang dari aturan di sisi Python.
KASUS_TULIS_TANGAN = [
    ('tulis-tangan/singkatan', [{"jenis": "teks", "teks": "Kita memakai banyak berkas, mis. HTML dan CSS. Setelah itu JavaScript menyusul.", "peran": ""}]),
    ('tulis-tangan/kalimat-panjang', [{"jenis": "teks", "teks": "Kalimat pertama ini sengaja dibuat sangat panjang sekali tanpa tanda baca penutup yang memotongnya sehingga jumlah karakternya melampaui batas dua ratus enam puluh karakter yang dipakai untuk ringkasan, lalu ia terus bersambung dengan kata kata lain yang tidak ada gunanya selain memenuhi ruang sampai akhirnya berhenti begitu saja di sini", "peran": ""}]),
    ('tulis-tangan/jebakan-di-tengah', [{"jenis": "teks", "teks": "Paragraf pembuka yang sah dan cukup panjang untuk diterima sebagai kalimat utuh.", "peran": ""}, {"jenis": "teks", "teks": "Jebakan: jangan pernah memakai ini untuk ringkasan.", "peran": "jebakan"}]),
    ('tulis-tangan/semua-pengantar', [{"jenis": "teks", "teks": "Ada tiga hal yang perlu diingat:", "peran": ""}, {"jenis": "teks", "teks": "Pertama adalah ini.", "peran": ""}]),
    ('tulis-tangan/lanjutan-diterima', [{"jenis": "teks", "teks": "Paragraf pertama berdiri sendiri dengan baik dan lengkap.", "peran": ""}, {"jenis": "teks", "teks": "Paragraf kedua cukup panjang dan berakhir dengan titik.", "peran": ""}]),
    ('tulis-tangan/singkatan-memotong-tiga-kalimat', [{"jenis": "teks", "teks": "Ada banyak hal, mis. HTML. Lalu CSS. Lalu JS. Lalu SQL.", "peran": ""}]),
    ('tulis-tangan/jebakan-di-awal', [{"jenis": "teks", "teks": "Jebakan: ini bukan pembuka yang boleh dipakai.", "peran": "jebakan"}, {"jenis": "teks", "teks": "Paragraf sesudahnya cukup panjang untuk diterima sebagai kalimat utuh.", "peran": ""}]),
    ('tulis-tangan/teks-kosong', [{"jenis": "teks", "teks": "", "peran": ""}]),
    ('tulis-tangan/teks-spasi', [{"jenis": "teks", "teks": "   ", "peran": ""}]),
]


def pecah(teks):
    mentah = [k for k in re.split(BATAS_KALIMAT, teks.strip()) if k]
    hasil, singkatan = [], False
    for k in mentah:
        if hasil and SINGKATAN.search(hasil[-1]):
            hasil[-1] += " " + k
            singkatan = True
        else:
            hasil.append(k)
    return hasil, singkatan


def rakit(kalimat, cabang):
    hasil = ""
    for k in kalimat[:MAKS_KALIMAT]:
        if hasil and len(hasil) + 1 + len(k) > MAKS_KARAKTER:
            cabang.add("potong-karakter")
            break
        hasil = (hasil + " " + k).strip()
    if len(kalimat) > MAKS_KALIMAT:
        cabang.add("potong-3-kalimat")
    if len(hasil) > MAKS_KARAKTER:
        cabang.add("kalimat-pertama-terlalu-panjang")
        hasil = hasil[:MAKS_KARAKTER].rsplit(" ", 1)[0].rstrip(",;:") + "…"
    return hasil


def ringkas(bagian0):
    """(ringkasan atau None, himpunan cabang) untuk bagian pertama sebuah materi."""
    cabang = set()
    if bagian0["jenis"] != "prosa" or not bagian0["blok"]:
        return None, {"tanpa-prosa"}
    teks = []
    for j, x in enumerate(bagian0["blok"]):
        if x["jenis"] != "teks" or x.get("peran") == "jebakan":
            cabang.add("berhenti-bukan-teks" if x["jenis"] != "teks" else "berhenti-jebakan")
            break
        t = x["teks"].strip()
        if j > 0 and not (x.get("peran", "") == "" and len(t) >= MIN_LANJUTAN and AKHIR.search(t)):
            cabang.add("lanjutan-ditolak")
            break
        if j > 0:
            cabang.add("lanjutan-diterima")
        if j == 0 and x.get("peran"):
            cabang.add("peran-aturan")
        teks.append(t)
    if not teks:
        return None, {"blok0-bukan-teks"}
    kalimat, singkatan = pecah(" ".join(teks))
    if not kalimat:
        # Blok pembuka kosong atau hanya spasi: tidak ada kalimat. Cabang ini
        # tidak ada di korpus nyata; ia dijaga dua kasus tulis tangan.
        return None, {"tanpa-kalimat"}
    if singkatan:
        cabang.add("singkatan")
    utuh = [k for k in kalimat if not k.endswith(":")]
    if utuh and len(utuh) == len(kalimat):
        cabang.add("utuh")
        hasil = rakit(kalimat, cabang)
    elif utuh:
        cabang.add("buang-pengantar")
        hasil = rakit(utuh, cabang)
    else:
        cabang.add("titikdua-jadi-titik")
        hasil = rakit([kalimat[0][:-1].rstrip() + "."], cabang)
    return hasil, cabang


@contextlib.contextmanager
def _lingkungan_sementara():
    """Lingkungan untuk mengimpor `webapp.isi` TANPA meninggalkan jejak.

    Pemanggilnya sering sebuah proses `unittest` yang masih menjalankan tes
    lain. Versi pertama menyetel `os.environ`, `sys.dont_write_bytecode`, dan
    `sys.path` begitu saja dan membuat direktori sementara yang tak pernah
    dihapus (22 direktori `golden-pembuka-*` menumpuk di `/tmp` setelah
    beberapa jalan), sehingga tes yang berjalan SESUDAHNYA membaca jalur
    sementara itu sebagai jalur bawaannya.
    """
    with tempfile.TemporaryDirectory(prefix="golden-pembuka-") as tmp:
        baru = {k: os.path.join(tmp, v) for k, v in (
            ("BELAJAR_PROGRESS_FILE", "p.json"), ("BELAJAR_CONFIG_FILE", "k.json"),
            ("BELAJAR_CATATAN_FILE", "c.json"), ("BELAJAR_WORKSPACE", "kerja"))}
        bytecode_lama = sys.dont_write_bytecode
        path_lama = list(sys.path)
        try:
            with mock.patch.dict(os.environ, baru):
                sys.dont_write_bytecode = True
                if AKAR not in sys.path:
                    sys.path.insert(0, AKAR)
                yield
        finally:
            sys.dont_write_bytecode = bytecode_lama
            sys.path[:] = path_lama


def populasi():
    """Bagian pertama SELURUH materi, seperti yang dikirim `/api/materi`."""
    with _lingkungan_sementara():
        from inti.kurikulum import LANGUAGES
        from webapp import isi

        keluar = []
        for lang in LANGUAGES:
            for i, m in enumerate(lang["materials"]):
                b0 = isi.bagian_materi(m, lang)[0]
                blok = None
                if b0["jenis"] == "prosa":
                    blok = [{"jenis": x["jenis"], "teks": x.get("teks", ""), "peran": x.get("peran", "")}
                            for x in b0.get("blok", [])]
                keluar.append({"k": f"{lang['key']}/{i}", "jenis": b0["jenis"], "blok": blok})
        return keluar


def bangun():
    pop = populasi()
    tanda = collections.defaultdict(list)
    for m in pop:
        _hasil, cabang = ringkas({"jenis": m["jenis"], "blok": m["blok"]})
        tanda[tuple(sorted(cabang))].append(m)
    acak = random.Random(BENIH)
    pilih = []
    for _tanda, ms in sorted(tanda.items(), key=lambda x: -len(x[1])):
        pilih.extend(acak.sample(ms, min(2, len(ms))))
    sisa = [m for m in pop if m not in pilih]
    pilih += acak.sample(sisa, 40)
    keluar = []
    for m in pilih:
        hasil, cabang = ringkas({"jenis": m["jenis"], "blok": m["blok"]})
        blok = [{"jenis": x["jenis"], "teks": x["teks"] if x["jenis"] == "teks" else "",
                 "peran": x["peran"]} for x in (m["blok"] or [])[:5]]
        keluar.append({"k": m["k"], "jenis": m["jenis"], "blok": blok,
                       "ringkas": hasil, "cabang": sorted(cabang)})
    for k, blok in KASUS_TULIS_TANGAN:
        hasil, cabang = ringkas({"jenis": "prosa", "blok": blok})
        keluar.append({"k": k, "jenis": "prosa", "blok": blok,
                       "ringkas": hasil, "cabang": sorted(cabang)})
    semua = set().union(*[set(t) for t in tanda])
    terlihat = set().union(*[set(k["cabang"]) for k in keluar])
    assert semua <= terlihat, f"cabang tak tercakup: {sorted(semua - terlihat)}"
    return json.dumps(keluar, ensure_ascii=False, separators=(",", ":")), len(keluar), len(pop)


def main(argv):
    teks, n, total = bangun()
    if "--tulis" in argv:
        with open(BERKAS, "w", encoding="utf-8") as f:
            f.write(teks)
        print(f"ditulis: {n} kasus dari {total} materi, {len(teks) // 1024} KB")
        return 0
    try:
        with open(BERKAS, encoding="utf-8") as f:
            ada = f.read()
    except FileNotFoundError:
        ada = None
    if ada == teks:
        print(f"cocok: {n} kasus dari {total} materi")
        return 0
    print("golden-pembuka.json tidak sama dengan hasil pembangkit; "
          "jalankan `python3 alat/golden_pembuka.py --tulis` sesudah aturan atau materi berubah",
          file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
