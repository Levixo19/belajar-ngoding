"""Navigasi lintas bahasa: pencarian global, daftar bookmark, dan lanjut terakhir.

Importir: main.py. Tidak menulis berkas sendiri; semua status lewat progress.py.
"""

import tema
from utils import (
    C, paint, clear, ask, ask_atau_eof, ask_choice, press_enter, header, rule,
    lebar, sorot_kata,
)
from materials import render_material, teks_polos
from exercises import show_exercise
from quiz import menu_satu_kuis
from progress import load_progress, kunci, bersihkan_bookmark

WARNA_TIPE = {"materi": "aksen", "kuis": "subjudul", "latihan": "judul"}


def _potongan(teks, kata, lebar_potong=None):
    """Ambil sepotong teks di sekitar kata yang dicari, untuk pratinjau hasil."""
    lebar_potong = lebar_potong or max(30, lebar() - 12)
    posisi = teks.lower().find(kata.lower())
    if posisi < 0:
        return ""
    mulai = max(0, posisi - lebar_potong // 3)
    cuplik = teks[mulai:mulai + lebar_potong].replace("\n", " ").strip()
    awalan = "..." if mulai > 0 else ""
    akhiran = "..." if mulai + lebar_potong < len(teks) else ""
    return awalan + cuplik + akhiran


def _kumpulkan(languages, kata, tipe_diminta=None):
    """Cari `kata` di materi, kuis, dan latihan semua bahasa."""
    low = kata.lower()
    hasil = []

    for lang in languages:
        if tipe_diminta in (None, "materi"):
            for m in lang["materials"]:
                isi = teks_polos(m)
                if low in isi.lower():
                    hasil.append({
                        "tipe": "materi", "lang": lang, "obj": m,
                        "judul": m["title"], "jumlah": isi.lower().count(low),
                        "cuplikan": _potongan(isi, kata),
                    })
        if tipe_diminta in (None, "kuis"):
            for q in lang["quizzes"]:
                isi = q["title"] + "\n" + "\n".join(
                    s["q"] + " " + " ".join(s["options"]) + " " + s.get("explanation", "")
                    for s in q["questions"])
                if low in isi.lower():
                    hasil.append({
                        "tipe": "kuis", "lang": lang, "obj": q,
                        "judul": q["title"], "jumlah": isi.lower().count(low),
                        "cuplikan": _potongan(isi, kata),
                    })
        if tipe_diminta in (None, "latihan"):
            for e in lang["exercises"]:
                isi = (e["title"] + "\n" + "\n".join(e["question"]) + "\n"
                       + e.get("solution", ""))
                if low in isi.lower():
                    hasil.append({
                        "tipe": "latihan", "lang": lang, "obj": e,
                        "judul": e["title"], "jumlah": isi.lower().count(low),
                        "cuplikan": _potongan(isi, kata),
                    })

    hasil.sort(key=lambda h: -h["jumlah"])
    return hasil


def cari_global(languages):
    """Cari kata kunci di materi, kuis, dan latihan semua bahasa sekaligus."""
    clear()
    header("CARI DI SEMUA BAHASA")
    print(tema.cat("  Cari kata kunci di materi, soal kuis, dan latihan.", "redup"))
    print(tema.cat("  Contoh: 'perulangan', 'array', 'JOIN', 'pointer'", "redup"))
    print(rule("-", C.DIM, bold=False))

    kata = ask("  Kata kunci > ", "").strip()
    if len(kata) < 2:
        if kata:
            print(tema.cat("  Kata kunci minimal 2 huruf.", "galat"))
            press_enter()
        return

    tipe_diminta = None
    while True:
        semua = _kumpulkan(languages, kata, tipe_diminta)
        if not semua:
            clear()
            header("HASIL PENCARIAN", f"'{kata}'")
            saring = f" (disaring: {tipe_diminta})" if tipe_diminta else ""
            print(tema.cat(f"\n  Tidak ada yang cocok dengan '{kata}'{saring}.", "galat"))
            if tipe_diminta:
                tipe_diminta = None
                press_enter("Tekan ENTER untuk melihat semua tipe...")
                continue
            press_enter()
            return

        hasil = semua[:40]
        clear()
        judul_saring = f" - saringan: {tipe_diminta}" if tipe_diminta else ""
        header("HASIL PENCARIAN",
               f"'{kata}' - {len(hasil)} dari {len(semua)} hasil{judul_saring}")

        names = []
        for h in hasil:
            tipe = tema.cat(f"{h['tipe']:<8}", WARNA_TIPE[h["tipe"]], tema.TEBAL)
            bahasa = tema.cat(f"{h['lang']['label']:<11}", "info")
            jumlah = tema.cat(f"({h['jumlah']}x)", "redup")
            baris = f"{tipe} {bahasa} {h['judul']}  {jumlah}"
            if h["cuplikan"]:
                baris += "\n       " + sorot_kata(tema.cat(h["cuplikan"], "redup"), kata)
            names.append(baris)

        extra = {"m": "Hanya materi", "k": "Hanya kuis", "l": "Hanya latihan"}
        if tipe_diminta:
            extra["s"] = "Tampilkan semua tipe"

        pilih = ask_choice(paint("  Buka hasil nomor:", C.BLUE, C.BOLD), names, extra=extra)
        if pilih == 0:
            return
        if pilih in ("m", "k", "l"):
            tipe_diminta = {"m": "materi", "k": "kuis", "l": "latihan"}[pilih]
            continue
        if pilih == "s":
            tipe_diminta = None
            continue
        _buka(hasil[pilih - 1], kata)


def _buka(h, kata_sorot=""):
    lang = h["lang"]
    if h["tipe"] == "materi":
        render_material(h["obj"], f"{lang['key']}_materi", kata_sorot=kata_sorot,
                        daftar=lang["materials"])
    elif h["tipe"] == "kuis":
        # Lewat submenu, bukan langsung mulai: dari hasil pencarian orang
        # biasanya ingin melihat kuisnya dulu, bukan tiba-tiba diuji.
        menu_satu_kuis(h["obj"], f"{lang['key']}_kuis")
    else:
        show_exercise(h["obj"], f"{lang['key']}_latihan", lang.get("runner", lang["key"]))


def _cari_objek(languages, kategori, judul):
    """Temukan kembali materi/kuis/latihan dari kunci progres tersimpan."""
    if "_" not in kategori:
        return None
    key_bahasa, tipe = kategori.rsplit("_", 1)
    for lang in languages:
        if lang["key"] != key_bahasa:
            continue
        koleksi = {"materi": lang["materials"], "kuis": lang["quizzes"],
                   "latihan": lang["exercises"]}.get(tipe, [])
        for obj in koleksi:
            if obj["title"] == judul:
                return {"tipe": tipe, "lang": lang, "obj": obj, "judul": judul}
    return None


def _kunci_bookmark_valid(languages):
    """Semua kunci bookmark yang masih menunjuk konten yang ada."""
    sah = set()
    for lang in languages:
        for tipe, koleksi in (("materi", lang["materials"]),
                              ("kuis", lang["quizzes"]),
                              ("latihan", lang["exercises"])):
            for obj in koleksi:
                sah.add(kunci(f"{lang['key']}_{tipe}", obj["title"]))
    return sah


def menu_bookmark(languages):
    while True:
        clear()
        header("BOOKMARK", "Materi yang kamu tandai")

        data = load_progress()
        entri = []
        for k in data["bookmark"]:
            if "::" not in k:
                continue
            kategori, judul = k.split("::", 1)
            item = _cari_objek(languages, kategori, judul)
            if item:
                entri.append(item)

        basi = len(data["bookmark"]) - len(entri)

        if not entri:
            print(tema.cat("\n  Belum ada bookmark.", "redup"))
            print(tema.cat("  Buka materi apa pun, lalu tekan [b] untuk menyimpannya.",
                           "redup"))
            if basi:
                print(tema.cat(f"\n  Catatan: {basi} bookmark menunjuk materi yang "
                               "sudah tidak ada.", "peringatan"))
                if ask("  [x] bersihkan | [ENTER] kembali > ", "").lower() == "x":
                    jumlah = bersihkan_bookmark(_kunci_bookmark_valid(languages))
                    print(tema.cat(f"  {jumlah} bookmark basi dibuang.", "sukses"))
                    press_enter()
                    continue
                return
            press_enter()
            return

        if basi:
            print(tema.cat(f"  {basi} bookmark menunjuk materi yang sudah tidak ada.",
                           "peringatan"))

        names = [f"{tema.cat(e['lang']['label'] + ':', 'info')} "
                 f"{tema.cat(e['tipe'], WARNA_TIPE[e['tipe']])} {e['judul']}"
                 for e in entri]
        extra = {"x": f"Bersihkan {basi} bookmark tidak valid"} if basi else None
        pilih = ask_choice(paint("  Buka bookmark:", C.BLUE, C.BOLD), names, extra=extra)
        if pilih == 0:
            return
        if pilih == "x":
            jumlah = bersihkan_bookmark(_kunci_bookmark_valid(languages))
            print(tema.cat(f"  {jumlah} bookmark basi dibuang.", "sukses"))
            press_enter()
            continue
        _buka(entri[pilih - 1])


def lanjut_terakhir(languages):
    """Buka kembali materi/kuis/latihan yang terakhir dibuka."""
    data = load_progress()
    terakhir = data.get("terakhir") or {}
    if not terakhir.get("judul"):
        clear()
        header("LANJUTKAN BELAJAR")
        print(tema.cat("\n  Belum ada riwayat. Mulai dari menu bahasa dulu ya.", "redup"))
        press_enter()
        return

    item = _cari_objek(languages, terakhir.get("kategori", ""), terakhir["judul"])
    if not item:
        clear()
        header("LANJUTKAN BELAJAR")
        print(tema.cat("\n  Materi terakhir tidak ditemukan lagi (mungkin sudah diubah).",
                       "peringatan"))
        press_enter()
        return

    # Tawarkan juga yang BERIKUTNYA: membuka ulang item yang sama terus-menerus
    # adalah keluhan paling sering tentang tombol "lanjutkan".
    berikut = None
    if item["tipe"] == "materi":
        daftar = item["lang"]["materials"]
        try:
            posisi = daftar.index(item["obj"])
            if posisi + 1 < len(daftar):
                berikut = daftar[posisi + 1]
        except ValueError:
            berikut = None

    clear()
    header("LANJUTKAN BELAJAR")
    print(tema.cat(f"\n  Terakhir kamu buka ({item['tipe']}):", "redup"))
    print(tema.cat(f"    {item['lang']['label']} - {item['judul']}", "teks", tema.TEBAL))
    waktu = terakhir.get("waktu", "")
    if waktu:
        print(tema.cat(f"    pada {waktu.replace('T', ' ')}", "redup"))
    print()
    print(tema.cat("  [ENTER] buka lagi", "aksen"))
    if berikut:
        print(tema.cat(f"  [n] materi berikutnya: {berikut['title'][:40]}", "sukses"))
    print(tema.cat("  [0] batal", "redup"))

    pilih = ask_atau_eof("  Pilih > ")
    if pilih is None or pilih == "0":
        return
    if pilih.lower() == "n" and berikut:
        render_material(berikut, f"{item['lang']['key']}_materi",
                        daftar=item["lang"]["materials"])
        return
    _buka(item)


# Nama publik untuk pemanggil di luar modul ini.
buka = _buka
