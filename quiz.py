"""Mesin kuis: acak soal & opsi, mode timer, review jawaban salah, ulang terjadwal."""

import random

from utils import (
    C, paint, clear, press_enter, ask, ask_choice, header, rule, bar, wrap, WIDTH,
    ask_timed,
)
from progress import (
    record_quiz_score, soal_salah_terakhir, load_progress, kunci, kuis_jatuh_tempo,
)

DETIK_PER_SOAL = 25


def _status_kuis(data, kategori, quiz):
    """Label ringkas kondisi kuis untuk ditampilkan di daftar."""
    k = kunci(kategori, quiz["title"])
    info = data["kuis_skor"].get(k)
    total = len(quiz["questions"])
    if not info:
        return paint("belum dikerjakan", C.DIM)

    terbaik = info.get("terbaik", 0)
    maks = info.get("total_soal", total) or total
    pct = terbaik / maks * 100 if maks else 0
    warna = C.GREEN if pct >= 80 else (C.YELLOW if pct >= 50 else C.RED)
    label = paint(f"terbaik {terbaik}/{maks}", warna)
    if kuis_jatuh_tempo(data, kategori, quiz["title"]):
        label += paint("  [saatnya diulang]", C.MAGENTA, C.BOLD)
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
        print(paint(f"\n  {n}. {item['q']}", C.WHITE, C.BOLD))
        if item["dipilih"] is None:
            print(paint("     Jawabanmu    : (kehabisan waktu)", C.RED))
        else:
            print(paint(f"     Jawabanmu    : {item['options'][item['dipilih']]}", C.RED))
        print(paint(f"     Yang benar   : {item['options'][item['answer']]}", C.GREEN))
        if item["explanation"]:
            print(paint(wrap("     " + item["explanation"], WIDTH + 6, "     "), C.DIM))
    print()
    press_enter("Tekan ENTER untuk kembali...")


def run_quiz(quiz, kategori="kuis", indeks=None, acak_soal=True, acak_opsi=True,
             detik_per_soal=0, seed=None):
    """Jalankan satu sesi kuis. `indeks` membatasi soal (mis. hanya yang salah)."""
    questions = quiz["questions"]
    if indeks is None:
        indeks = list(range(len(questions)))
    indeks = [i for i in indeks if 0 <= i < len(questions)]
    if not indeks:
        print(paint("  Tidak ada soal untuk dikerjakan.", C.YELLOW))
        press_enter()
        return

    rng = random.Random(seed)
    paket = _siapkan_soal(questions, indeks, acak_soal, acak_opsi, rng)
    total = len(paket)

    clear()
    header("KUIS: " + quiz["title"], f"{total} soal")
    mode = []
    if acak_soal or acak_opsi:
        mode.append("acak")
    if detik_per_soal:
        mode.append(f"timer {detik_per_soal}s/soal")
    if mode:
        print(paint("  Mode: " + ", ".join(mode), C.MAGENTA))
    print(paint("  Jawab dengan mengetik nomor. Ketik 'q' untuk berhenti.", C.DIM))

    benar = 0
    salah = []
    index = 0

    while index < total:
        so = paket[index]
        print(paint(f"\n  Soal {index + 1}/{total}", C.BLUE, C.BOLD),
              "  ", bar(index, total, 16))
        print(paint("  " + "-" * (WIDTH - 4), C.DIM))
        print(paint("  " + so["q"], C.WHITE, C.BOLD))
        print()
        for i, opt in enumerate(so["options"]):
            print(paint(f"    {i + 1}. {opt}", C.WHITE))
        print()

        if detik_per_soal:
            raw, habis = ask_timed("  Jawaban > ", detik_per_soal)
        else:
            raw, habis = ask("  Jawaban > ", "q"), False
        raw = raw.strip().lower()

        if habis:
            print(paint("  [LEWAT] Dihitung salah.", C.RED, C.BOLD))
            print(paint(f"     Jawaban benar: {so['options'][so['answer']]}", C.GREEN))
            so_salah = dict(so)
            so_salah["dipilih"] = None
            salah.append(so_salah)
            if so["explanation"]:
                print(paint("  Penjelasan: " + so["explanation"], C.DIM))
            index += 1
            continue

        if raw == "q":
            print(paint(f"\n  Kuis dihentikan. Skor sementara: {benar}/{index}", C.YELLOW))
            press_enter()
            return

        if not raw.isdigit() or not (1 <= int(raw) <= len(so["options"])):
            print(paint("  Pilihan tidak valid, coba lagi.", C.RED))
            continue

        dipilih = int(raw) - 1
        if dipilih == so["answer"]:
            benar += 1
            print(paint("  [BENAR]", C.GREEN, C.BOLD))
        else:
            print(paint("  [SALAH]", C.RED, C.BOLD))
            print(paint(f"     Jawaban benar: {so['options'][so['answer']]}", C.GREEN))
            so_salah = dict(so)
            so_salah["dipilih"] = dipilih
            salah.append(so_salah)

        if so["explanation"]:
            print(paint("  Penjelasan: " + so["explanation"], C.DIM))
        index += 1

    # ---- rekap
    print(paint("\n  " + "=" * (WIDTH - 4), C.CYAN))
    pct = benar / total * 100
    print(paint(f"  Skor akhir: {benar}/{total}  ({pct:.0f}%)", C.YELLOW, C.BOLD),
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
    print(paint("  " + status, C.MAGENTA))
    print(paint("  " + "=" * (WIDTH - 4), C.CYAN))

    # Hanya catat skor resmi kalau seluruh soal dikerjakan, bukan sesi "ulang yang salah".
    sesi_penuh = len(indeks) == len(questions)
    salah_index = sorted({s["asli"] for s in salah})

    if sesi_penuh:
        badge_baru = record_quiz_score(kategori, quiz["title"], benar, total, salah_index)
    else:
        # Sesi latihan ulang: perbarui daftar salah saja, tanpa merusak skor terbaik.
        sisa = [i for i in soal_salah_terakhir(kategori, quiz["title"])
                if i in salah_index or i not in indeks]
        badge_baru = record_quiz_score(kategori, quiz["title"], benar, total, sorted(set(sisa)))

    _umumkan_badge(badge_baru)

    if salah:
        print(paint(f"\n  Ada {len(salah)} soal yang salah.", C.YELLOW))
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
        print(paint(f"  [BADGE BARU] {nama} - {deskripsi}", C.YELLOW, C.BOLD))


def _menu_satu_kuis(quiz, kategori):
    """Submenu mode pengerjaan untuk satu kuis."""
    while True:
        clear()
        header("KUIS: " + quiz["title"], f"{len(quiz['questions'])} soal")

        data = load_progress()
        info = data["kuis_skor"].get(kunci(kategori, quiz["title"]))
        if info:
            print(paint(
                f"  Skor terbaik : {info.get('terbaik', 0)}/{info.get('total_soal', 0)}"
                f"   |   Percobaan: {info.get('percobaan', 0)}",
                C.WHITE,
            ))
        salah = soal_salah_terakhir(kategori, quiz["title"])
        if salah:
            print(paint(f"  Soal yang masih salah: {len(salah)}", C.RED))
        print(rule("-", C.DIM, bold=False))

        opsi = [
            "Mulai kuis (soal & opsi diacak)",
            "Mulai kuis (urutan asli)",
            f"Mode timer ({DETIK_PER_SOAL} detik per soal)",
        ]
        if salah:
            opsi.append(paint(f"Ulangi {len(salah)} soal yang masih salah", C.MAGENTA))

        pilih = ask_choice(paint("  Pilih mode:", C.BLUE, C.BOLD), opsi)
        if pilih == 0:
            return
        if pilih == 1:
            run_quiz(quiz, kategori, acak_soal=True, acak_opsi=True)
        elif pilih == 2:
            run_quiz(quiz, kategori, acak_soal=False, acak_opsi=False)
        elif pilih == 3:
            run_quiz(quiz, kategori, acak_soal=True, acak_opsi=True,
                     detik_per_soal=DETIK_PER_SOAL)
        elif pilih == 4:
            run_quiz(quiz, kategori, indeks=salah, acak_soal=True, acak_opsi=True)


def quiz_menu(title, quizzes, kategori="kuis"):
    while True:
        clear()
        header("KUIS: " + title)

        data = load_progress()
        perlu_ulang = [q for q in quizzes if kuis_jatuh_tempo(data, kategori, q["title"])]
        if perlu_ulang:
            print(paint(
                f"  {len(perlu_ulang)} kuis sudah waktunya diulang untuk memperkuat ingatan.",
                C.MAGENTA,
            ))

        names = [
            f"{q['title']}  ({len(q['questions'])} soal)  {_status_kuis(data, kategori, q)}"
            for q in quizzes
        ]
        extra = {"u": "Kerjakan semua kuis yang jatuh tempo"} if perlu_ulang else None
        pilih = ask_choice(paint("  Pilih kuis:", C.BLUE, C.BOLD), names, extra=extra)

        if pilih == 0:
            return
        if pilih == "u":
            for q in perlu_ulang:
                run_quiz(q, kategori, acak_soal=True, acak_opsi=True)
            continue
        _menu_satu_kuis(quizzes[pilih - 1], kategori)
