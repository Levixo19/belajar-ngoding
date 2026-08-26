"""Navigasi lintas bahasa: pencarian global, daftar bookmark, dan lanjut terakhir."""

from utils import C, paint, clear, ask, ask_choice, press_enter, header, rule, WIDTH
from materials import render_material, teks_polos
from exercises import show_exercise
from quiz import run_quiz
from progress import load_progress, kunci


def _potongan(teks, kata, lebar=54):
    """Ambil sepotong teks di sekitar kata yang dicari, untuk pratinjau hasil."""
    posisi = teks.lower().find(kata.lower())
    if posisi < 0:
        return ""
    mulai = max(0, posisi - lebar // 3)
    cuplik = teks[mulai:mulai + lebar].replace("\n", " ").strip()
    awalan = "..." if mulai > 0 else ""
    akhiran = "..." if mulai + lebar < len(teks) else ""
    return awalan + cuplik + akhiran


def cari_global(languages):
    """Cari kata kunci di materi, kuis, dan latihan semua bahasa sekaligus."""
    clear()
    header("CARI DI SEMUA BAHASA")
    print(paint("  Cari kata kunci di materi, soal kuis, dan latihan.", C.DIM))
    print(paint("  Contoh: 'perulangan', 'array', 'JOIN', 'pointer'", C.DIM))
    print(rule("-", C.DIM, bold=False))

    kata = ask("  Kata kunci > ", "").strip()
    if len(kata) < 2:
        if kata:
            print(paint("  Kata kunci minimal 2 huruf.", C.RED))
            press_enter()
        return

    low = kata.lower()
    hasil = []

    for lang in languages:
        for m in lang["materials"]:
            isi = teks_polos(m)
            if low in isi.lower():
                hasil.append({
                    "tipe": "materi", "lang": lang, "obj": m,
                    "judul": m["title"], "jumlah": isi.lower().count(low),
                    "cuplikan": _potongan(isi, kata),
                })
        for q in lang["quizzes"]:
            isi = q["title"] + "\n" + "\n".join(
                s["q"] + " " + " ".join(s["options"]) + " " + s.get("explanation", "")
                for s in q["questions"]
            )
            if low in isi.lower():
                hasil.append({
                    "tipe": "kuis", "lang": lang, "obj": q,
                    "judul": q["title"], "jumlah": isi.lower().count(low),
                    "cuplikan": _potongan(isi, kata),
                })
        for e in lang["exercises"]:
            isi = e["title"] + "\n" + "\n".join(e["question"]) + "\n" + e.get("solution", "")
            if low in isi.lower():
                hasil.append({
                    "tipe": "latihan", "lang": lang, "obj": e,
                    "judul": e["title"], "jumlah": isi.lower().count(low),
                    "cuplikan": _potongan(isi, kata),
                })

    if not hasil:
        print(paint(f"\n  Tidak ada yang cocok dengan '{kata}'.", C.RED))
        press_enter()
        return

    hasil.sort(key=lambda h: -h["jumlah"])
    hasil = hasil[:40]

    while True:
        clear()
        header("HASIL PENCARIAN", f"'{kata}' - {len(hasil)} hasil teratas")
        warna_tipe = {"materi": C.CYAN, "kuis": C.MAGENTA, "latihan": C.YELLOW}
        names = []
        for h in hasil:
            tipe = paint(f"{h['tipe']:<8}", warna_tipe[h["tipe"]], C.BOLD)
            bahasa = paint(f"{h['lang']['label']:<11}", C.BLUE)
            jumlah = paint(f"({h['jumlah']}x)", C.DIM)
            baris = f"{tipe} {bahasa} {h['judul']}  {jumlah}"
            if h["cuplikan"]:
                baris += "\n       " + paint(h["cuplikan"], C.DIM)
            names.append(baris)

        pilih = ask_choice(paint("  Buka hasil nomor:", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        _buka(hasil[pilih - 1])


def _buka(h):
    lang = h["lang"]
    if h["tipe"] == "materi":
        render_material(h["obj"], f"{lang['key']}_materi")
    elif h["tipe"] == "kuis":
        run_quiz(h["obj"], f"{lang['key']}_kuis")
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

        if not entri:
            print(paint("\n  Belum ada bookmark.", C.DIM))
            print(paint("  Buka materi apa pun, lalu tekan [b] untuk menyimpannya.", C.DIM))
            press_enter()
            return

        names = [f"{paint(e['lang']['label'] + ':', C.BLUE)} {e['judul']}" for e in entri]
        pilih = ask_choice(paint("  Buka bookmark:", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        _buka(entri[pilih - 1])


def lanjut_terakhir(languages):
    """Buka kembali materi/kuis/latihan yang terakhir dibuka."""
    data = load_progress()
    terakhir = data.get("terakhir") or {}
    if not terakhir.get("judul"):
        clear()
        header("LANJUTKAN BELAJAR")
        print(paint("\n  Belum ada riwayat. Mulai dari menu bahasa dulu ya.", C.DIM))
        press_enter()
        return

    item = _cari_objek(languages, terakhir.get("kategori", ""), terakhir["judul"])
    if not item:
        clear()
        header("LANJUTKAN BELAJAR")
        print(paint("\n  Materi terakhir tidak ditemukan lagi (mungkin sudah diubah).", C.YELLOW))
        press_enter()
        return

    clear()
    header("LANJUTKAN BELAJAR")
    print(paint(f"\n  Terakhir kamu buka ({item['tipe']}):", C.DIM))
    print(paint(f"    {item['lang']['label']} - {item['judul']}", C.WHITE, C.BOLD))
    waktu = terakhir.get("waktu", "")
    if waktu:
        print(paint(f"    pada {waktu.replace('T', ' ')}", C.DIM))
    print()
    if ask("  [ENTER] buka | [0] batal > ", "0") == "0":
        return
    _buka(item)
