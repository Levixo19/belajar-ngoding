#!/usr/bin/env python3
"""Menuliskan blok "Keluaran yang diharapkan" ke soal latihan, dari keluaran
SUNGGUHAN solusinya.

    python3 alat/tambah_keluaran.py                 # laporan: mana yang kurang
    python3 alat/tambah_keluaran.py rust            # periksa satu kurikulum
    python3 alat/tambah_keluaran.py rust --tulis    # periksa lalu tulis

Kenapa alat ini ada. Latihan yang dinilai `persis` dicocokkan karakter demi
karakter, jadi soal yang tidak menuliskan keluarannya meminta pelajar menebak
sesuatu yang tidak pernah disebutkan -- termasuk lebar kolom dan jumlah
desimalnya. Tujuh puluh delapan latihan seperti itu tertinggal, 16 dari 16 di
Rust dan 16 dari 16 di C#, karena toolchain keduanya dulu tidak terpasang di
mesin ini. Janjinya karena itu TIDAK ditulis tangan: ia dijalankan.

Pengurainya dipinjam dari `inti/latihan.py` (`blok_janji`, `input_untuk`),
pengurai yang SAMA dengan yang dipakai
`test_solutions.test_janji_keluaran_di_soal_sesuai_kenyataan` untuk mengadu
janji itu dengan kenyataan. Dua pengurai untuk satu bentuk berarti blok yang
ditulis rapi di sini lalu tidak pernah dibaca pagarnya.

Pagar yang membuat alat ini MENOLAK menulis:
  * solusinya gagal jalan, atau keluarannya kosong;
  * dua kali jalan memberi keluaran BERBEDA -- janji yang tidak deterministik
    adalah latihan yang mustahil lulus, dan menuliskannya memindahkan bug itu
    ke dalam kurikulum;
  * ada baris yang melewati LEBAR_MAKS setelah dijorokkan (janji dipotong
    adalah janji yang salah, jadi yang ditolak latihannya, bukan barisnya);
  * sesudah ditulis, `blok_janji` membaca balik sesuatu yang TIDAK sama
    dengan keluaran yang baru dijalankan, atau medan lain latihan itu
    berubah. Kalau itu terjadi berkasnya dikembalikan ke isi semula.

Satu utang yang DIUKUR dan sengaja dibiarkan: dari 548 janji di seluruh
kurikulum, 19 isinya sudah muncul utuh di prosa tepat di atasnya, jadi
pelajar membacanya dua kali. Gaya rumahnya memang membolehkan sketsa format
di prosa lalu janji penuh di bawahnya -- 529 latihan begitu, dan sketsanya
biasanya bermarka `...` sehingga bukan duplikat. Yang 19 ini sketsanya
kebetulan lengkap. Memangkas prosanya akan membuatnya mengalir, tapi itu
suntingan EDITORIAL atas teks kurikulum, dan alat yang menambah janji tidak
boleh sekaligus jadi alat yang memangkas prosa: sekali ia boleh, tidak ada
lagi yang menjaga mana yang berubah karena diputuskan dan mana karena
kebetulan cocok pola. Kalau mau ditutup, jalurnya `alat/ganti_badan.py`
dengan pagarnya sendiri.

Hanya stdlib.
"""

import ast
import importlib.util
import json
import os
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from inti import runner                                        # noqa: E402
from inti.kurikulum import LANGUAGES                           # noqa: E402
from inti.latihan import blok_janji, gabung_setup, input_untuk  # noqa: E402

LEBAR_MAKS = 100
# Cuplikan diterima pagar (`janji in nyata`), jadi keluaran panjang dipotong
# di batas baris dari ATAS -- tetap bersambung, tetap benar.
BARIS_MAKS = 16
JOROK = "    "
TIMEOUT = 20


def perlu_blok(ex):
    """Latihan ini dinilai persis, punya solusi, dan belum punya janji?"""
    return (ex.get("auto_check", True)
            and ex.get("mode", "persis") == "persis"
            and ex.get("solution")
            and not blok_janji(ex))


def _muat_daftar(jalur):
    spec = importlib.util.spec_from_file_location("_latihan_sementara", jalur)
    modul = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modul)
    nama = [n for n in dir(modul) if n.endswith("_EXERCISES")]
    if not nama:
        raise SystemExit(f"{jalur}: tidak ada *_EXERCISES")
    return getattr(modul, nama[0])


def _nilai(simpul, kunci):
    for k, v in zip(simpul.keys, simpul.values):
        if isinstance(k, ast.Constant) and k.value == kunci:
            return v
    return None


def cari_rentang(sumber, judul):
    """Rentang teks daftar `question` milik latihan berjudul itu."""
    for simpul in ast.walk(ast.parse(sumber)):
        if not isinstance(simpul, ast.Dict):
            continue
        t = _nilai(simpul, "title")
        if not (isinstance(t, ast.Constant) and t.value == judul):
            continue
        q = _nilai(simpul, "question")
        if not isinstance(q, ast.List):
            raise SystemExit(f"{judul!r}: question bukan daftar literal")
        return q
    raise SystemExit(f"latihan tidak ditemukan: {judul!r}")


def format_daftar(baris, indent):
    dalam = " " * (indent + 4)
    isi = "".join(f"{dalam}{json.dumps(b, ensure_ascii=False)},\n" for b in baris)
    return "[\n" + isi + " " * indent + "]"


def jalankan_dua_kali(lang, ex):
    """(keluaran, keluhan). Keluhan tidak kosong berarti JANGAN tulis."""
    masukan = input_untuk(ex, None)
    kode = gabung_setup(ex, ex["solution"])
    hasil = []
    for _ in range(2):
        r = runner.jalankan(lang["runner"], kode, stdin=masukan, timeout=TIMEOUT)
        if not r.sukses:
            return None, f"solusinya gagal jalan: {(r.galat or '')[:120]}"
        hasil.append(runner.normalisasi(r.keluaran))
    if hasil[0] != hasil[1]:
        return None, "dua kali jalan beda -- keluarannya tidak deterministik"
    if not hasil[0].strip():
        return None, "keluarannya kosong"
    return hasil[0], ""


def susun_blok(ex, keluaran):
    """(baris_baru, keluhan) -- blok yang akan ditempelkan ke soal."""
    baris = [b.rstrip() for b in keluaran.rstrip("\n").split("\n")]
    dipotong = len(baris) > BARIS_MAKS
    if dipotong:
        baris = baris[:BARIS_MAKS]
    panjang = [b for b in baris if len(JOROK + b) > LEBAR_MAKS]
    if panjang:
        return None, (f"ada baris {len(JOROK + panjang[0])} karakter setelah "
                      f"dijorokkan: {panjang[0][:48]}...")

    masukan = ex.get("stdin_list") or ([ex["stdin"]] if ex.get("stdin") else [])
    satu_baris = masukan and len(masukan[0].strip().split("\n")) == 1
    if satu_baris:
        kepala = f"Untuk input {masukan[0].strip()}, keluarannya:"
    else:
        kepala = "Keluaran yang diharapkan:"

    blok = [""] + [kepala] + [JOROK + b if b else "" for b in baris]
    # Baris kosong di TENGAH keluaran memutus bloknya bagi `blok_janji`, yang
    # berhenti di baris kosong pertama sesudah isinya mulai. Jadi yang
    # dijanjikan cuma sampai sebelum baris kosong itu -- bukan bug, tapi harus
    # dipotong DI SINI supaya yang ditulis sama dengan yang dibaca balik.
    for i, b in enumerate(blok[2:], start=2):
        if not b.strip():
            blok = blok[:i]
            dipotong = True
            break
    if len(blok) <= 2:
        return None, "keluarannya mulai dengan baris kosong"
    return blok, ""


def proses(kunci, tulis):
    lang = next((l for l in LANGUAGES if l["key"] == kunci), None)
    if lang is None:
        raise SystemExit(f"kurikulum tidak ada: {kunci}")
    if not runner.tersedia(lang["runner"]):
        print(f"  {kunci}: toolchain `{lang['runner']}` tidak terpasang -- "
              "janji tidak boleh ditulis dari tebakan")
        return 0, 0
    jalur = os.path.join(AKAR, "data", f"{kunci}_exercises.py")
    if not os.path.exists(jalur):
        raise SystemExit(f"tidak ada {jalur}")

    sasaran = [e for e in lang["exercises"] if perlu_blok(e)]
    if not sasaran:
        print(f"  {kunci}: semua latihan sudah punya janji")
        return 0, 0

    with open(jalur, encoding="utf-8") as f:
        sumber_awal = f.read()
    sumber = sumber_awal
    ditulis, ditolak = 0, 0
    rencana = []
    for ex in sasaran:
        keluaran, keluhan = jalankan_dua_kali(lang, ex)
        if keluhan:
            print(f"    TOLAK {ex['title'][:46]:<48}{keluhan}")
            ditolak += 1
            continue
        blok, keluhan = susun_blok(ex, keluaran)
        if keluhan:
            print(f"    TOLAK {ex['title'][:46]:<48}{keluhan}")
            ditolak += 1
            continue
        rencana.append((ex, blok))
        print(f"    ok    {ex['title'][:46]:<48}{len(blok) - 2} baris")

    if not tulis or not rencana:
        return 0, ditolak

    # Disunting dari BELAKANG supaya rentang yang di depannya tidak bergeser.
    for ex, blok in sorted(rencana, key=lambda r: -cari_rentang(
            sumber_awal, r[0]["title"]).lineno):
        q = cari_rentang(sumber, ex["title"])
        garis = sumber.split("\n")
        awal = sum(len(g) + 1 for g in garis[:q.lineno - 1]) + q.col_offset
        akhir = sum(len(g) + 1 for g in garis[:q.end_lineno - 1]) + q.end_col_offset
        # Indentasinya diambil dari AWAL BARIS, bukan dari `col_offset`.
        # `col_offset` menunjuk kolom `[`, yang ada SESUDAH `"question": ` --
        # memakainya langsung menjorokkan butirnya 24 spasi alih-alih 12, dan
        # yang rusak bukan isi string-nya (pagar tetap hijau) melainkan
        # selisih git yang jadi mustahil dibaca manusia.
        baris_kunci = garis[q.lineno - 1]
        indent = len(baris_kunci) - len(baris_kunci.lstrip())
        sumber = (sumber[:awal]
                  + format_daftar(list(ex["question"]) + blok, indent)
                  + sumber[akhir:])

    with open(jalur, "w", encoding="utf-8") as f:
        f.write(sumber)

    # Verifikasi: yang dibaca balik pengurai yang SAMA harus sama dengan yang
    # baru dijalankan, dan medan lain tidak boleh bergeser.
    salah = []
    baru = {e["title"]: e for e in _muat_daftar(jalur)}
    lama = {e["title"]: e for e in lang["exercises"]}
    if set(baru) != set(lama):
        salah.append("daftar latihannya berubah")
    for judul, e_lama in lama.items():
        e_baru = baru.get(judul)
        if e_baru is None:
            continue
        for medan in e_lama:
            if medan != "question" and e_baru.get(medan) != e_lama[medan]:
                salah.append(f"{judul}: medan {medan} ikut berubah")
    for ex, blok in rencana:
        e_baru = baru.get(ex["title"])
        janji = blok_janji(e_baru) if e_baru else []
        if not janji:
            salah.append(f"{ex['title']}: blok yang ditulis tidak terbaca "
                         "balik oleh blok_janji")
            continue
        # `blok_janji` mengembalikan baris BESERTA indentasinya -- ia cuma
        # me-rstrip. Pagar di test_solutions yang melakukan dedent, saat
        # membandingkan. Jadi yang diadu di sini harus ikut berindentasi;
        # melepasnya di satu sisi saja membuat ke-11 janji bash terbaca
        # "beda" padahal yang ditulis sudah benar.
        teks = janji[-1][1]
        harap = "\n".join(blok[2:])
        if teks != harap:
            salah.append(f"{ex['title']}: yang dibaca balik beda dengan yang "
                         f"ditulis\n      baca: {teks[:90]!r}\n"
                         f"      tulis: {harap[:90]!r}")
    if salah:
        with open(jalur, "w", encoding="utf-8") as f:
            f.write(sumber_awal)
        for s in salah:
            print("    GAGAL", s)
        raise SystemExit(f"{kunci}: verifikasi gagal, berkas DIKEMBALIKAN")

    ditulis = len(rencana)
    print(f"  {kunci}: {ditulis} janji ditulis, {ditolak} ditolak")
    return ditulis, ditolak


def laporan():
    print(f"{'kurikulum':<14}{'tanpa janji':>12}{'total':>7}  toolchain")
    total = 0
    for l in LANGUAGES:
        ex = l.get("exercises") or []
        n = sum(1 for e in ex if perlu_blok(e))
        if not n:
            continue
        total += n
        siap = "ada" if runner.tersedia(l["runner"]) else "TIDAK ADA"
        print(f"{l['key']:<14}{n:>12}{len(ex):>7}  {siap}")
    print(f"{'TOTAL':<14}{total:>12}")


def main():
    arg = [a for a in sys.argv[1:] if not a.startswith("--")]
    tulis = "--tulis" in sys.argv[1:]
    if not arg:
        laporan()
        return 0
    ditulis = ditolak = 0
    for kunci in arg:
        a, b = proses(kunci, tulis)
        ditulis += a
        ditolak += b
    print(f"\nringkas: {ditulis} ditulis, {ditolak} ditolak"
          + ("" if tulis else "  (tanpa --tulis: tidak ada yang ditulis)"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
