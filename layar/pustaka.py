"""Layar Pustaka di terminal: cari, saring, dan buka tautan belajar.

Isinya dari `inti/pustaka.py`, fungsi yang sama yang dipakai antarmuka web,
jadi urutan dan cacahnya identik di kedua tempat. Yang berbeda cuma cara
membukanya: di sini tautan dibuka lewat `webbrowser` bawaan Python, dan
alamatnya selalu ikut dicetak supaya tetap bisa disalin di mesin tanpa
browser (SSH, TTY polos).
"""

import webbrowser

from inti import pustaka
from inti import tema
from layar.utils import (
    C, paint, clear, ask, ask_choice, press_enter, header, rule,
    bungkus_baris, sorot_kata, potong, lebar_menu,
)

PER_HALAMAN = 20


def _baris_entri(e, kata=""):
    """Satu entri sebagai opsi menu dua baris: jenis + judul, lalu keterangan.

    Kedua baris dipendekkan di sini, selebar `lebar_menu()`, supaya menu
    panah tidak perlu memotongnya lagi: potongan di sana jatuh di ujung
    baris, tepat di penanda "[Indonesia]". 7 kolom untuk awalan "   nn. ".
    """
    maks = lebar_menu() - 7
    jenis = tema.cat(f"{pustaka.JENIS.get(e['jenis'], e['jenis']):<20}", "info")
    penanda = "  [Indonesia]" if e["bahasa"] == "id" else ""
    judul = potong(e["judul"], max(20, maks - 21 - len(penanda)))
    if kata:
        judul = sorot_kata(judul, kata)
    ket = e.get("catatan") or (e["topik"][0] if e["topik"] else "")
    baris = f"{jenis} {judul}{tema.cat(penanda, 'sukses') if penanda else ''}"
    if ket:
        baris += "\n       " + tema.cat(potong(ket, max(20, maks - 7)), "redup")
    return baris


def _buka_entri(e):
    clear()
    header("TAUTAN PUSTAKA", pustaka.JENIS.get(e["jenis"], e["jenis"]))
    print(tema.cat("  " + e["judul"], "teks", tema.TEBAL))
    print()
    for label, nilai in (
        ("Alamat", e["url"]),
        ("Keterangan", e.get("catatan", "")),
        ("Topik", "; ".join(e["topik"])),
        ("Bahasa", pustaka.BAHASA.get(e["bahasa"], e["bahasa"])),
        ("Sumber", e["sumber"]),
    ):
        if not nilai:
            continue
        print(tema.cat(f"  {label:<11} ", "redup") + nilai)
    print(rule("-", C.DIM, bold=False))
    pilih = ask_choice(paint("  Buka di browser?", C.BLUE, C.BOLD),
                       ["Buka di browser", "Cukup tampilkan alamatnya"])
    if pilih == 1:
        try:
            berhasil = webbrowser.open(e["url"], new=2)
        except webbrowser.Error:
            berhasil = False
        if not berhasil:
            print(tema.cat("  Browser tidak bisa dibuka dari sini. Salin "
                           "alamat di atas secara manual.", "galat"))
            press_enter()


def _pilih_dari(judul, label, segi, kini):
    """Menu satu penyaring. Mengembalikan nilai baru ("" = semua), atau None."""
    kunci = [k for k in label if segi.get(k)]
    if not kunci:
        return None
    opsi = [f"{label[k]:<24} {segi[k]:>5}" + ("  <- sekarang" if k == kini else "")
            for k in kunci]
    clear()
    header(judul)
    pilih = ask_choice(paint("  Pilih:", C.BLUE, C.BOLD), opsi,
                       extra={"s": "Semua (hapus saringan ini)"})
    if pilih == "s":
        return ""
    if isinstance(pilih, int) and 1 <= pilih <= len(kunci):
        return kunci[pilih - 1]
    return None


def _sumber_dan_lisensi():
    clear()
    header("SUMBER DAN LISENSI PUSTAKA")
    for s in pustaka.daftar_sumber():
        print(tema.cat(f"  {s['nama']}  ", "teks", tema.TEBAL)
              + tema.cat(f"[{s['lisensi']}]  {s['jumlah']} tautan", "info"))
        teks = s["atribusi"] + (f" Dipanen dari commit {s['commit']}." if s["commit"] else "")
        for b in bungkus_baris(teks, indent="    "):
            print(tema.cat(b, "redup"))
        if s["repo"]:
            print(tema.cat("    " + s["repo"], "redup"))
        print()
    press_enter()


def menu_pustaka(languages, kurikulum=None):
    """Jelajahi seluruh Pustaka; `kurikulum` = saringan awal (kunci bahasa)."""
    label_kur = {l["key"]: l["label"] for l in languages}
    saring = {"kueri": "", "kurikulum": kurikulum or "", "jenis": "",
              "bahasa": "", "sumber": ""}
    halaman = 1
    while True:
        r = pustaka.cari(saring["kueri"], kurikulum=saring["kurikulum"] or None,
                         jenis=saring["jenis"] or None, bahasa=saring["bahasa"] or None,
                         sumber=saring["sumber"] or None,
                         halaman=halaman, per_halaman=PER_HALAMAN)
        jumlah_hal = max(1, -(-r["total"] // PER_HALAMAN))
        clear()
        aktif = []
        if saring["kueri"]:
            aktif.append(f"'{saring['kueri']}'")
        if saring["kurikulum"]:
            aktif.append(label_kur.get(saring["kurikulum"], saring["kurikulum"]))
        if saring["jenis"]:
            aktif.append(pustaka.JENIS[saring["jenis"]])
        if saring["bahasa"]:
            aktif.append(pustaka.BAHASA[saring["bahasa"]])
        if saring["sumber"]:
            aktif.append(saring["sumber"])
        header("PUSTAKA", f"{r['total']} dari {pustaka.total()} tautan"
               + (" - " + ", ".join(aktif) if aktif else ""))
        for b in bungkus_baris("Buku, kursus, proyek, dan API gratis. Yang "
                               "berbahasa Indonesia tampil lebih dulu."):
            print(tema.cat(b, "redup"))
        print(rule("-", C.DIM, bold=False))

        extra = {"c": "Cari kata", "k": "Saring kurikulum", "j": "Saring jenis",
                 "b": "Saring bahasa", "r": "Saring sumber"}
        if halaman < jumlah_hal:
            extra["n"] = f"Halaman berikutnya ({halaman + 1}/{jumlah_hal})"
        if halaman > 1:
            extra["p"] = "Halaman sebelumnya"
        if aktif:
            extra["h"] = "Hapus semua saringan"
        extra["i"] = "Sumber dan lisensi"

        if r["hasil"]:
            nama = [_baris_entri(e, saring["kueri"]) for e in r["hasil"]]
            pilih = ask_choice(paint("  Buka tautan nomor:", C.BLUE, C.BOLD),
                               nama, extra=extra)
        else:
            print(tema.cat("\n  Tidak ada tautan yang cocok. Hapus salah satu "
                           "saringan atau coba kata lain.\n", "galat"))
            pilih = ask_choice(paint("  Pilih:", C.BLUE, C.BOLD),
                               ["Hapus semua saringan"], extra=extra)
            if pilih == 1:
                pilih = "h"

        if pilih == 0:
            return
        if isinstance(pilih, int):
            _buka_entri(r["hasil"][pilih - 1])
        elif pilih == "c":
            saring["kueri"] = ask("  Kata kunci (kosong = semua) > ", "").strip()
            halaman = 1
        elif pilih in ("k", "j", "b", "r"):
            nama_saring, judul, label = {
                "k": ("kurikulum", "SARING KURIKULUM", label_kur),
                "j": ("jenis", "SARING JENIS", pustaka.JENIS),
                "b": ("bahasa", "SARING BAHASA", pustaka.BAHASA),
                "r": ("sumber", "SARING SUMBER",
                      {s["kunci"]: s["nama"] for s in pustaka.daftar_sumber()}),
            }[pilih]
            baru = _pilih_dari(judul, label, r["segi"][nama_saring], saring[nama_saring])
            if baru is not None:
                saring[nama_saring] = baru
                halaman = 1
        elif pilih == "n":
            halaman += 1
        elif pilih == "p":
            halaman -= 1
        elif pilih == "h":
            saring = {k: "" for k in saring}
            halaman = 1
        elif pilih == "i":
            _sumber_dan_lisensi()


def menu_bacaan_bahasa(lang, languages):
    """Ringkasan Pustaka untuk satu bahasa: sama dengan tab Bacaan di web."""
    r = pustaka.ringkasan_kurikulum(lang["key"])
    while True:
        clear()
        header("BACAAN " + lang["label"].upper(), f"{r['total']} tautan gratis")
        if r["total"]:
            print(tema.cat("  " + ", ".join(f"{j['label']} {j['jumlah']}"
                                            for j in r["per_jenis"]), "info"))
            print(tema.cat("  Pilihan pembuka, yang berbahasa Indonesia lebih dulu.",
                           "redup"))
            print(rule("-", C.DIM, bold=False))
            pilih = ask_choice(
                paint("  Buka tautan nomor:", C.BLUE, C.BOLD),
                [_baris_entri(e) for e in r["pembuka"]],
                extra={"s": f"Semua {r['total']} bacaan {lang['label']} di Pustaka"})
        else:
            print(tema.cat("  Belum ada bacaan untuk bahasa ini di Pustaka.", "redup"))
            print(rule("-", C.DIM, bold=False))
            pilih = ask_choice(paint("  Pilih:", C.BLUE, C.BOLD), ["Buka Pustaka"])
            if pilih == 1:
                pilih = "semua"
        if pilih == 0:
            return
        if pilih == "s":
            menu_pustaka(languages, kurikulum=lang["key"])
        elif pilih == "semua":
            menu_pustaka(languages)
        elif isinstance(pilih, int):
            _buka_entri(r["pembuka"][pilih - 1])
