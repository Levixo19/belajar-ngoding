"""Buktikan rekaman golden bergigi, tanpa menyentuh satu berkas pun di disk.

Kenapa tidak dengan menyunting berkasnya. Beberapa tes di repo ini memindai
ISI `inti/*.py` dan `webapp/statik/js/*.js` dengan regex -- pajak alamat
`berkas:NNN` di `tests/test_web.py` yang paling terkenal. Menyunting sebuah
berkas untuk sepuluh detik sementara suite penuh berjalan di latar belakang
memerahkan tes yang tidak ada hubungannya dengan apa yang sedang diuji, dan
kegagalan semacam itu yang paling mahal: ia terbaca sebagai bug.

Jadi mutasinya dipasang di MEMORI, di proses ini saja.

Tiga mutasi, masing-masing mewakili satu cara rekaman ini bisa jadi tumpul:

1. `sorot_untuk` jadi identitas -- pemetaan alias dilepas, persis cacat yang
   alat ini sendiri pernah punya. Kalau rekamannya tidak memerah di sini, ia
   membekukan jalur yang aplikasinya tidak pernah tempuh.
2. Satu kata kunci dicabut dari aturan Python. Perubahan yang paling mungkin
   terjadi tanpa sengaja, dan paling tidak kelihatan di layar.
3. `bahasa_blok` mengabaikan medan `"bahasa"` per bagian. Itu mengembalikan
   perilaku sebelum kurikulum tech stack ada, dan tidak melempar error di
   mana pun.

    python3 alat/uji_gigi_golden.py
"""

import json
import os
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)
sys.path.insert(0, os.path.join(AKAR, "alat"))

from inti import berkas, sorot  # noqa: E402
from webapp import isi  # noqa: E402
import golden_bersama  # noqa: E402

GOLDEN = os.path.join(AKAR, "packages", "bersama", "golden")


def rekaman():
    with open(os.path.join(GOLDEN, "sorot.json"), encoding="utf-8") as f:
        return json.load(f)


def _beda(acuan, sekarang):
    """Berapa kasus yang sidiknya bergeser, plus pergeseran cakupannya."""
    lama = {k["nama"]: k["sha256"] for k in acuan["kasus"]}
    baru = {k["nama"]: k["sha256"] for k in sekarang["kasus"]}
    geser = sum(1 for n, s in baru.items() if lama.get(n) != s)
    return geser, (acuan["cakupan"]["tersorot"] != sekarang["cakupan"]["tersorot"])


def sel(nama, pasang, lepas, acuan):
    pasang()
    try:
        sekarang = golden_bersama.susun()["sorot.json"]
    finally:
        lepas()
    geser, cakupan_geser = _beda(acuan, sekarang)
    vonis = "MERAH" if geser else "hijau (TUMPUL)"
    tanda = "cakupan ikut bergeser" if cakupan_geser else "cakupan sama"
    print(f"  {nama:38s} {vonis:14s} {geser:5d} kasus bergeser, {tanda}")
    return geser > 0


def main():
    acuan = rekaman()

    # Pagar nol: tanpa mutasi apa pun, rekamannya WAJIB cocok. Tanpa ini,
    # sebuah alat yang selalu menghasilkan angka berbeda akan membuat ketiga
    # sel di bawah "merah" tanpa membuktikan apa pun.
    geser, _ = _beda(acuan, golden_bersama.susun()["sorot.json"])
    if geser:
        print(f"PAGAR NOL GAGAL: {geser} kasus bergeser tanpa mutasi apa pun.")
        print("  Ekspor ulang dulu (python3 alat/golden_bersama.py --tulis), "
              "lalu jalankan ini lagi.")
        return 1
    print(f"pagar nol: 0 kasus bergeser tanpa mutasi ({len(acuan['kasus'])} kasus)")
    print()

    asli_sorot_untuk = berkas.sorot_untuk
    asli_bahasa_blok = isi.bahasa_blok
    hasil = []

    hasil.append(sel(
        "sorot_untuk jadi identitas",
        lambda: setattr(berkas, "sorot_untuk", lambda b: b),
        lambda: setattr(berkas, "sorot_untuk", asli_sorot_untuk),
        acuan))

    def cabut_kunci():
        a = sorot.ATURAN["python"]
        cabut_kunci.simpan = a.kunci
        a.kunci = frozenset(k for k in a.kunci if k != "lambda")

    def pulih_kunci():
        sorot.ATURAN["python"].kunci = cabut_kunci.simpan

    hasil.append(sel("kata kunci 'lambda' dicabut dari python",
                     cabut_kunci, pulih_kunci, acuan))

    hasil.append(sel(
        "bahasa_blok mengabaikan medan 'bahasa'",
        lambda: setattr(isi, "bahasa_blok",
                        lambda bagian, lang: (lang["runner"],
                                              isi.bahasa_sorot(lang))),
        lambda: setattr(isi, "bahasa_blok", asli_bahasa_blok),
        acuan))

    print()
    if all(hasil):
        print(f"SEMUA {len(hasil)} sel MERAH: rekaman golden bergigi.")
        return 0
    print(f"{hasil.count(False)} dari {len(hasil)} sel TUMPUL. "
          "Rekamannya tidak menjaga apa yang dikiranya dijaga.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
