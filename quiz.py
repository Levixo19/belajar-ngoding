"""Mesin kuis: acak soal & opsi, mode timer, review jawaban salah, ulang terjadwal.

Dua cacat lama yang dibereskan di sini:

* **Mode timer bisa berputar selamanya.** `select()` melaporkan stdin "siap"
  juga saat pipe-nya sudah ditutup, jadi jawaban kosong dibaca berulang tanpa
  henti dan soal yang sama dicetak jutaan kali. Sekarang EOF dikenali sebagai
  EOF dan kuis berhenti dengan rapi.
* **Sesi "ulangi soal yang salah" merusak skor.** Sesi itu memanggil pencatat
  yang sama dengan sesi penuh, sehingga penyebutnya tertimpa jumlah subset
  ("terbaik 8/2"), badge "Nilai Sempurna" bisa dipicu palsu, dan bonus XP-nya
  bisa dipanen berulang kali. Sekarang sesi parsial hanya memperbarui daftar
  soal yang masih salah.

Importir: main.py, navigasi.py.
"""

import random

import tema
from utils import (
    C, paint, clear, press_enter, ask, ask_atau_eof, ask_choice, header, rule,
    bar, wrap, lebar, angka_pilihan, ask_timed,
)
from progress import (
    record_quiz_score, perbarui_soal_salah, soal_salah_terakhir, load_progress,
    kunci, kuis_jatuh_tempo,
)

try:
    import konfigurasi
except ImportError:
    konfigurasi = None

DETIK_PER_SOAL = 25
MAKS_SALAH_BERTURUT = 5


def _detik_per_soal():
    if konfigurasi is not None:
        try:
            return int(konfigurasi.ambil("detik_per_soal", DETIK_PER_SOAL))
        except (TypeError, ValueError):
            return DETIK_PER_SOAL
    return DETIK_PER_SOAL


def _acak_bawaan():
    if konfigurasi is not None:
        return bool(konfigurasi.ambil("acak_bawaan", True))
    return True


def _status_kuis(data, kategori, quiz):
    """Label ringkas kondisi kuis untuk ditampilkan di daftar."""
    k = kunci(kategori, quiz["title"])
    info = data["kuis_skor"].get(k)
    total = len(quiz["questions"])
    if not info:
        return tema.cat("belum dikerjakan", "redup")

    maks = info.get("total_soal", 0) or total
    terbaik = min(info.get("terbaik", 0), maks)
    pct = terbaik / maks * 100 if maks else 0
    peran = "sukses" if pct >= 80 else ("peringatan" if pct >= 50 else "galat")
    label = tema.cat(f"terbaik {terbaik}/{maks}", peran)
    if kuis_jatuh_tempo(data, kategori, quiz["title"]):
        label += tema.cat("  [saatnya diulang]", "subjudul", tema.TEBAL)
    return label


def _siapkan_soal(questions, indeks, acak_soal, acak_opsi, rng):
    """Bangun daftar soal siap tampil.

    Tiap item menyimpan `asli` = index soal di data mentah, supaya catatan
    jawaban salah tetap valid walaupun urutannya diacak.
    """
    paket = []
    for i in indeks:
        soal = questions[i]
        opsi = list(soal["options"])
        jawaban = soal["answer"]

        if acak_opsi:
            urutan = list(range(len(opsi)))
            rng.shuffle(urutan)
            opsi = [soal["options"][j] for j in urutan]
            # `urutan[posisi_baru] = posisi_lama`, jadi posisi baru jawaban
            # benar adalah index tempat posisi lamanya muncul di `urutan`.
            jawaban = urutan.index(soal["answer"])

        paket.append({
            "asli": i,
            "q": soal["q"],
            "options": opsi,
            "answer": jawaban,
            "explanation": soal.get("explanation", ""),
        })

    if acak_soal:
        rng.shuffle(paket)
    return paket


def _tampilkan_review(salah):
    """Tampilkan ulang semua soal yang dijawab keliru."""
    if not salah:
        return
    clear()
    header("REVIEW JAWABAN SALAH", f"{len(salah)} soal perlu kamu pelajari lagi")
    for n, item in enumerate(salah, start=1):
        print(tema.cat(f"\n  {n}. {item['q']}", "teks", tema.TEBAL))
        if item["dipilih"] is None:
            print(tema.cat("     Jawabanmu    : (kehabisan waktu)", "galat"))
        else:
            print(tema.cat(f"     Jawabanmu    : {item['options'][item['dipilih']]}",
                           "galat"))
        print(tema.cat(f"     Yang benar   : {item['options'][item['answer']]}", "sukses"))
        if item["explanation"]:
            print(tema.cat(wrap(item["explanation"], lebar() - 2, "     "), "redup"))
    print()
    press_enter("Tekan ENTER untuk kembali...")


def _baca_jawaban(detik_per_soal):
    """Return (teks, kehabisan_waktu, eof)."""
    if detik_per_soal:
        raw, habis = ask_timed("  Jawaban > ", detik_per_soal)
        if raw is None:
            return "", False, True
        return raw.strip().lower(), habis, False

    raw = ask_atau_eof("  Jawaban > ")
    if raw is None:
        return "", False, True
    return raw.strip().lower(), False, False


def run_quiz(quiz, kategori="kuis", indeks=None, acak_soal=True, acak_opsi=True,
             detik_per_soal=0, seed=None):
    """Jalankan satu sesi kuis. `indeks` membatasi soal (mis. hanya yang salah)."""
    questions = quiz["questions"]
    if indeks is None:
        indeks = list(range(len(questions)))
    indeks = [i for i in indeks if 0 <= i < len(questions)]
    if not indeks:
        print(tema.cat("  Tidak ada soal untuk dikerjakan.", "peringatan"))
        press_enter()
        return

    rng = random.Random(seed)
    paket = _siapkan_soal(questions, indeks, acak_soal, acak_opsi, rng)
    total = len(paket)
    sesi_penuh = len(indeks) == len(questions)

    clear()
    header("KUIS: " + quiz["title"], f"{total} soal")
    mode = []
    if acak_soal or acak_opsi:
        mode.append("acak")
    if detik_per_soal:
        mode.append(f"timer {detik_per_soal}s/soal")
    if not sesi_penuh:
        mode.append("latihan ulang (skor tidak dicatat)")
    if mode:
        print(tema.cat("  Mode: " + ", ".join(mode), "subjudul"))
    print(tema.cat("  Jawab dengan mengetik nomor. Ketik 'q' untuk berhenti.", "redup"))

    benar = 0
    salah = []
    index = 0
    salah_ketik = 0

    while index < total:
        so = paket[index]
        print(tema.cat(f"\n  Soal {index + 1}/{total}", "info", tema.TEBAL),
              "  ", bar(index, total, 16))
        print(tema.cat("  " + "-" * (lebar() - 4), "redup"))
        for baris in wrap(so["q"], lebar() - 2, "  ").splitlines():
            print(tema.cat(baris, "teks", tema.TEBAL))
        print()
        for i, opt in enumerate(so["options"]):
            print(tema.cat(f"    {i + 1}. {opt}", "teks"))
        print()

        raw, habis, eof = _baca_jawaban(detik_per_soal)

        if eof:
            print(tema.cat("\n  Masukan habis, kuis dihentikan.", "peringatan"))
            press_enter()
            return

        if habis:
            print(tema.cat("  [LEWAT] Dihitung salah.", "galat", tema.TEBAL))
            print(tema.cat(f"     Jawaban benar: {so['options'][so['answer']]}", "sukses"))
            so_salah = dict(so)
            so_salah["dipilih"] = None
            salah.append(so_salah)
            if so["explanation"]:
                print(tema.cat("  Penjelasan: " + so["explanation"], "redup"))
            index += 1
            salah_ketik = 0
            continue

        if raw == "q":
            print(tema.cat(f"\n  Kuis dihentikan. Skor sementara: {benar}/{index}",
                           "peringatan"))
            press_enter()
            return

        nomor = angka_pilihan(raw, len(so["options"]))
        if nomor is None:
            salah_ketik += 1
            if salah_ketik >= MAKS_SALAH_BERTURUT:
                print(tema.cat("\n  Terlalu banyak masukan tidak valid, kuis dihentikan.",
                               "peringatan"))
                press_enter()
                return
            print(tema.cat("  Pilihan tidak valid, coba lagi.", "galat"))
            continue

        salah_ketik = 0
        dipilih = nomor - 1
        if dipilih == so["answer"]:
            benar += 1
            print(tema.cat("  [BENAR]", "sukses", tema.TEBAL))
        else:
            print(tema.cat("  [SALAH]", "galat", tema.TEBAL))
            print(tema.cat(f"     Jawaban benar: {so['options'][so['answer']]}", "sukses"))
            so_salah = dict(so)
            so_salah["dipilih"] = dipilih
            salah.append(so_salah)

        if so["explanation"]:
            print(tema.cat("  Penjelasan: " + so["explanation"], "redup"))
        index += 1

    # ---- rekap
    lbr = lebar()
    print(tema.cat("\n  " + "=" * (lbr - 4), "garis"))
    pct = benar / total * 100
    print(tema.cat(f"  Skor akhir: {benar}/{total}  ({pct:.0f}%)", "judul", tema.TEBAL),
          " ", bar(benar, total, 20))

    if pct == 100:
        status = "Sempurna! Kamu menguasai topik ini."
    elif pct >= 80:
        status = "Bagus sekali! Sedikit lagi sempurna."
    elif pct >= 60:
        status = "Lumayan. Ulangi materi dan coba lagi."
    elif pct >= 40:
        status = "Masih kurang. Baca lagi materinya ya."
    else:
        status = "Jangan menyerah! Mulai dari materi dasar dulu."
    print(tema.cat("  " + status, "subjudul"))
    print(tema.cat("  " + "=" * (lbr - 4), "garis"))

    salah_index = sorted({s["asli"] for s in salah})

    if sesi_penuh:
        badge_baru = record_quiz_score(kategori, quiz["title"], benar, total, salah_index)
    else:
        # Sesi latihan ulang: perbarui daftar salah saja. Soal yang tadinya
        # salah dan kini benar dicoret; soal di luar sesi ini tidak disentuh.
        # Skor terbaik, penyebut, XP, dan jadwal sengaja tidak diubah.
        sisa = [i for i in soal_salah_terakhir(kategori, quiz["title"])
                if i in salah_index or i not in indeks]
        badge_baru = perbarui_soal_salah(kategori, quiz["title"], sorted(set(sisa)))
        print(tema.cat("  (Sesi latihan ulang: skor terbaik & jadwal tidak diubah.)",
                       "redup"))

    _umumkan_badge(badge_baru)

    if salah:
        print(tema.cat(f"\n  Ada {len(salah)} soal yang salah.", "peringatan"))
        pilihan = ask("  [r] review jawaban salah | [ENTER] lanjut > ", "").lower()
        if pilihan == "r":
            _tampilkan_review(salah)
            return
    press_enter()


def _umumkan_badge(badge_baru):
    if not badge_baru:
        return
    print()
    for _, nama, deskripsi in badge_baru:
        print(tema.cat(f"  [BADGE BARU] {nama} - {deskripsi}", "judul", tema.TEBAL))


def _menu_satu_kuis(quiz, kategori):
    """Submenu mode pengerjaan untuk satu kuis."""
    while True:
        clear()
        header("KUIS: " + quiz["title"], f"{len(quiz['questions'])} soal")

        data = load_progress()
        info = data["kuis_skor"].get(kunci(kategori, quiz["title"]))
        if info:
            maks = info.get("total_soal", 0) or len(quiz["questions"])
            print(tema.cat(
                f"  Skor terbaik : {min(info.get('terbaik', 0), maks)}/{maks}"
                f"   |   Percobaan: {info.get('percobaan', 0)}", "teks"))
        salah = soal_salah_terakhir(kategori, quiz["title"])
        if salah:
            print(tema.cat(f"  Soal yang masih salah: {len(salah)}", "galat"))
        print(rule("-", C.DIM, bold=False))

        detik = _detik_per_soal()
        opsi = [
            "Mulai kuis (soal & opsi diacak)",
            "Mulai kuis (urutan asli)",
            f"Mode timer ({detik} detik per soal)",
        ]
        if salah:
            opsi.append(tema.cat(f"Ulangi {len(salah)} soal yang masih salah", "subjudul"))

        pilih = ask_choice(paint("  Pilih mode:", C.BLUE, C.BOLD), opsi)
        if pilih == 0:
            return
        if pilih == 1:
            run_quiz(quiz, kategori, acak_soal=True, acak_opsi=True)
        elif pilih == 2:
            run_quiz(quiz, kategori, acak_soal=False, acak_opsi=False)
        elif pilih == 3:
            run_quiz(quiz, kategori, acak_soal=True, acak_opsi=True,
                     detik_per_soal=detik)
        elif pilih == 4:
            run_quiz(quiz, kategori, indeks=salah, acak_soal=True, acak_opsi=True)


def quiz_menu(title, quizzes, kategori="kuis"):
    while True:
        clear()
        header("KUIS: " + title)

        data = load_progress()
        perlu_ulang = [q for q in quizzes if kuis_jatuh_tempo(data, kategori, q["title"])]
        if perlu_ulang:
            print(tema.cat(
                f"  {len(perlu_ulang)} kuis sudah waktunya diulang untuk memperkuat ingatan.",
                "subjudul"))

        names = [
            f"{q['title']}  ({len(q['questions'])} soal)  {_status_kuis(data, kategori, q)}"
            for q in quizzes
        ]
        extra = {"u": "Kerjakan semua kuis yang jatuh tempo"} if perlu_ulang else None
        pilih = ask_choice(paint("  Pilih kuis:", C.BLUE, C.BOLD), names, extra=extra)

        if pilih == 0:
            return
        if pilih == "u":
            acak = _acak_bawaan()
            for q in perlu_ulang:
                run_quiz(q, kategori, acak_soal=acak, acak_opsi=acak)
            continue
        _menu_satu_kuis(quizzes[pilih - 1], kategori)


# Nama publik untuk pemanggil di luar modul ini.
menu_satu_kuis = _menu_satu_kuis
