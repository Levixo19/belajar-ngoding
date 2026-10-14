"""Peta Karier di terminal: daftar profesi, rincian, kuis, dan jalur pindah.

Semua angka datang dari `pelajar/karier.py`, sama dengan layar web. Yang
tidak ikut ke terminal cuma gambar kisinya; isinya (profesi, kesiapan, bekal,
gaji bersumber, jalur) utuh.
"""

from data import karier as data_karier
from inti import tema
from pelajar import karier
from pelajar.progress import load_progress
from layar.utils import (
    C, paint, clear, ask_choice, press_enter, header, rule, bar, bungkus_baris,
)


def _persen(p):
    return f"{p:3.0f}%"


def _cetak_blok(judul, baris):
    print(tema.cat("  " + judul.upper(), "redup", tema.TEBAL))
    for b in baris:
        for i, potong in enumerate(bungkus_baris(b, indent="      ")):
            print(("    - " + potong.lstrip()) if i == 0 else potong)
    print()


def _rincian(p, ringkas):
    kur = ringkas["kurikulum"]
    clear()
    rumpun = next(r["label"] for r in data_karier.RUMPUN if r["id"] == p["rumpun"])
    header(p["nama"].upper(), f"{rumpun} - {data_karier.JENJANG[p['jenjang']]}")
    print("  " + bar(p["kesiapan"], 100, 30)
          + tema.cat(f"  {_persen(p['kesiapan'])} siap", "teks", tema.TEBAL))
    print()
    for b in bungkus_baris(p["ringkas"]):
        print(tema.cat(b, "teks"))
    print()
    print(tema.cat("  BEKAL DARI APLIKASI INI", "redup", tema.TEBAL))
    for k in p["kelompok"]:
        nama = (" / ".join(kur[x]["label"] for x in k["pilihan"])
                if len(k["pilihan"]) > 1 else kur[k["wakil"]]["label"])
        awal = "salah satu: " if len(k["pilihan"]) > 1 else ""
        print(f"    {bar(k['persen'], 100, 12)} {_persen(k['persen'])}  {awal}{nama}")
    if p["pelengkap"]:
        print(tema.cat("    pelengkap: " + ", ".join(kur[x]["label"] for x in p["pelengkap"]),
                       "redup"))
    print()
    _cetak_blok("Sehari-hari", p["harian"])
    _cetak_blok("Keahlian", [", ".join(data_karier.KEAHLIAN[k] for k in p["keahlian"])])
    _cetak_blok("Alat", [", ".join(p["alat"])])
    if p.get("gaji"):
        g = p["gaji"]
        _cetak_blok("Gaji di Indonesia", [
            g["rentang"], f"{g['konteks']} Sumber: {g['sumber']}, diperiksa {g['diperiksa']}.",
            g["url"]])
    else:
        _cetak_blok("Gaji di Indonesia", [
            "Belum ada sumber publik yang angkanya bisa diperiksa, jadi sengaja tidak ditebak."])
    _cetak_blok("Sertifikasi", [f"{s['nama']} ({s['penerbit']}, {s['tingkat']})"
                                for s in p["sertifikasi"]]
                or ["Tidak ada sertifikasi yang diakui luas; portofolio yang berbicara."])
    _cetak_blok("Jalan masuk", [p["masuk"]])
    _cetak_blok("Proyek untuk portofolio", p["proyek"])
    nama = {q["id"]: q["nama"] for q in ringkas["profesi"]}
    if p["naik"]:
        _cetak_blok("Langkah berikutnya", [", ".join(nama[x] for x in p["naik"])])
    _cetak_blok("Profesi yang dekat", [", ".join(nama[x] for x in p["dekat"])])
    _cetak_blok("Bacaan lanjut", ["https://roadmap.sh/" + s for s in p["peta"]]
                + [f"{x['judul']}: {x['url']}" for x in p["sumber"]])
    press_enter()


def _kuis(ringkas):
    pilihan = []
    for i, soal in enumerate(data_karier.KUIS, 1):
        clear()
        header("KUIS KECOCOKAN", f"soal {i} dari {len(data_karier.KUIS)}")
        pilih = ask_choice(paint("  " + soal["q"], C.BLUE, C.BOLD),
                           [o["label"] for o in soal["opsi"]],
                           back_label="Lewati soal ini")
        pilihan.append(pilih - 1 if isinstance(pilih, int) and pilih > 0 else None)
    hasil = karier.skor_kuis(pilihan)
    per_id = {p["id"]: p for p in ringkas["profesi"]}
    clear()
    header("HASIL KUIS KECOCOKAN")
    if not hasil:
        print(tema.cat("  Jawabanmu belum cukup condong ke satu arah.", "redup"))
        press_enter()
        return
    for i, h in enumerate(hasil, 1):
        print(tema.cat(f"  {i}. {per_id[h['id']]['nama']}", "teks", tema.TEBAL))
        print(tema.cat("     cocok karena: " + ", ".join(
            data_karier.KEAHLIAN[k] for k in h["cocok"]), "redup"))
    print()
    pilih = ask_choice(paint("  Buka rinciannya:", C.BLUE, C.BOLD),
                       [per_id[h["id"]]["nama"] for h in hasil])
    if isinstance(pilih, int) and pilih > 0:
        _rincian(per_id[hasil[pilih - 1]["id"]], ringkas)


def _pilih_profesi(judul, ringkas):
    clear()
    header(judul)
    daftar = ringkas["profesi"]
    pilih = ask_choice(paint("  Pilih profesi:", C.BLUE, C.BOLD),
                       [p["nama"] for p in daftar])
    return daftar[pilih - 1]["id"] if isinstance(pilih, int) and pilih > 0 else None


def _jalur(ringkas):
    dari = _pilih_profesi("PERENCANA PERPINDAHAN - PROFESIMU SEKARANG", ringkas)
    if not dari:
        return
    ke = _pilih_profesi("PERENCANA PERPINDAHAN - PROFESI TUJUAN", ringkas)
    if not ke:
        return
    nama = {p["id"]: p["nama"] for p in ringkas["profesi"]}
    kur = ringkas["kurikulum"]
    clear()
    header("PERENCANA PERPINDAHAN", f"{nama[dari]} -> {nama[ke]}")
    langkah = karier.jalur(dari, ke) or []
    if not langkah:
        print(tema.cat("  Belum ada jalur yang tercatat di antara keduanya.", "redup"))
    else:
        print("  " + tema.cat("  ->  ".join(nama[x] for x in langkah), "teks", tema.TEBAL))
        celah = karier.celah_bekal(dari, ke)
        print()
        if celah:
            print(tema.cat("  Bekal yang perlu ditambah:", "redup", tema.TEBAL))
            for grup in celah:
                print("    - " + " atau ".join(
                    f"{kur[k]['label']} ({kur[k]['persen']:.0f}%)" for k in grup))
        else:
            print(tema.cat("  Bekal profesi tujuan sudah tercakup bekal profesi asal.", "redup"))
    print()
    press_enter()


def menu_karier(languages):
    while True:
        ringkas = karier.ringkasan(languages, load_progress())
        clear()
        header("PETA KARIER", f"{len(ringkas['profesi'])} profesi dari kurikulum aplikasi ini")
        print(tema.cat("  Kesiapan dihitung dari kurikulum yang sudah kamu kerjakan.",
                       "redup"))
        print(rule("-", C.DIM, bold=False))
        urut = []
        opsi = []
        for r in data_karier.RUMPUN:
            for p in ringkas["profesi"]:
                if p["rumpun"] != r["id"]:
                    continue
                urut.append(p)
                opsi.append(f"{_persen(p['kesiapan'])}  {p['nama']:<34} "
                            + tema.cat(r["label"], "redup"))
        pilih = ask_choice(paint("  Buka rincian profesi:", C.BLUE, C.BOLD), opsi,
                           extra={"q": "Kuis kecocokan", "j": "Perencana perpindahan"})
        if pilih == 0:
            return
        if pilih == "q":
            _kuis(ringkas)
        elif pilih == "j":
            _jalur(ringkas)
        elif isinstance(pilih, int):
            _rincian(urut[pilih - 1], ringkas)
