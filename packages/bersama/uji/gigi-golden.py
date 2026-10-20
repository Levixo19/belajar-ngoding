"""Buktikan pembanding golden di paket ini bisa MERAH, bukan cuma kebetulan hijau.

Sebuah pembanding yang lulus di percobaan pertama adalah pembanding yang
paling perlu dicurigai: tidak ada satu pun bukti bahwa ia akan memberi tahu
kalau yang dibandingkannya rusak. Di sini sumber TS dirusak dengan sengaja,
satu mutasi per sel, dan tiap sel wajib merah DENGAN ALASAN YANG BENAR.

Alasan yang benar itu bedanya. Mutasi yang membuat berkasnya tidak bisa diurai
Node juga menghasilkan kode keluar 1, dan sel seperti itu tidak membuktikan
apa pun soal pembandingnya. Jadi tiap sel menagih KATEGORI keluhan yang
diharapkan muncul di keluaran, dan mutan yang cuma bikin Node gagal memuat
berkasnya dihitung sebagai sel yang GAGAL.

    python3 packages/bersama/uji/gigi-golden.py
"""

import os
import re
import subprocess
import sys

SINI = os.path.dirname(os.path.abspath(__file__))
PAKET = os.path.dirname(SINI)


def sumber(nama):
    return os.path.join(PAKET, "src", nama)


# {pembanding: (berkas sumber, [(nama, dari, ke, kategori keluhan)])}
#
# Mutan dipilih supaya masing-masing merusak LAPISAN yang berbeda, dan supaya
# hampir semuanya TIDAK menimbulkan error di mana pun -- persis jenis kerusakan
# yang cuma rekaman ini bisa menangkap.
BATERAI = {
    "golden-sorot.ts": (sumber("sorot.ts"), [
        (
            "gabung dilepas (token tidak dipadatkan)",
            "  return gabung(hasil);",
            "  return hasil;",
            "sidik token bergeser",
        ),
        (
            "kutip dicari dari yang TERPENDEK",
            "    const pembuka = aturan.kutip.find((q) => kode.startsWith(q, i));",
            "    const pembuka = [...aturan.kutip].reverse()"
            ".find((q) => kode.startsWith(q, i));",
            "sidik token bergeser",
        ),
        (
            # Jangkar ini pernah usang sekali: ia menyebut `kode[k]` sementara
            # sumbernya sudah diubah ke `charAt` saat `noUncheckedIndexedAccess`
            # dinyalakan. Baterainya melapor JANGKAR TIDAK UNIK, bukan lolos
            # diam-diam -- dan itu memang bedanya antara pagar yang berguna dan
            # pagar yang menenangkan.
            "pengenal sebelum '(' tidak jadi fungsi",
            '        jenis = k < n && kode.charAt(k) === "(" ? "fungsi" : "teks";',
            '        jenis = "teks";',
            "sidik token bergeser",
        ),
        (
            "namaPenyorot melewatkan pemetaan",
            "  return PEMETAAN[nama] ?? nama;",
            "  return nama;",
            "bahasa penyorot berbeda",
        ),
    ]),
    "golden-beda.ts": (sumber("beda.ts"), [
        (
            # Jantung penyejajarnya: tanpa akumulasi DP, setiap baris cocok
            # jadi blok sepanjang satu, dan blok "terpanjang" berhenti berarti.
            "DP j2len tidak mengakumulasi",
            "      const k = (j2len.get(j - 1) ?? 0) + 1;",
            "      const k = 1;",
            "bandingkan() berbeda",
        ),
        (
            "blok cocok tidak diurutkan",
            "  blok.sort((p, q) => p[0] - q[0] || p[1] - q[1] || p[2] - q[2]);",
            "  // blok.sort dilepas",
            "bandingkan() berbeda",
        ),
        (
            "baris kosong di AWAL tidak dibuang",
            "  while (baris.length && !baris[0]) baris.shift();",
            "  // shift dilepas",
            "bandingkan() berbeda",
        ),
        (
            "satu awalan 'nyaris' dicabut",
            '  "Hanya beda TANDA BACA",\n',
            "",
            "nyaris()",
        ),
    ]),
    "golden-galat.ts": (sumber("galat.ts"), [
        (
            # `re.IGNORECASE | re.DOTALL` di Python dipasang sekali untuk
            # SELURUH tabel. Melupakannya di TS membuat pola yang melintasi
            # baris (`cannot find symbol.*?symbol:`) berhenti cocok -- dan
            # yang terlihat cuma pesan error yang kembali mentah.
            "bendera regex dilepas",
            ").map((p) => ({ re: new RegExp(p.pola, BENDERA), ganti: p.ganti }));",
            ").map((p) => ({ re: new RegExp(p.pola), ganti: p.ganti }));",
            "terjemahkan() berbeda",
        ),
        (
            # Pengganti dikenakan pada SELURUH pesan, bukan pada teks yang
            # cocok. Hasilnya penjelasan yang membawa serta potongan pesan
            # aslinya.
            "pengganti dikenakan ke seluruh pesan",
            "    const teks = cocok[0].replace(re, ganti).trim().split(/\\s+/).join(\" \");",
            "    const teks = galat.replace(re, ganti).trim().split(/\\s+/).join(\" \");",
            "terjemahkan() berbeda",
        ),
        (
            # `re.sub` Python mengganti SEMUA kecocokan. Tanpa `g`, jalur
            # direktori sementara yang disebut dua kali cuma bersih sekali.
            "bendera g dilepas dari pola jalur",
            'const RE_PATH = new RegExp(RAPIKAN.path, "g");',
            "const RE_PATH = new RegExp(RAPIKAN.path);",
            "rapikan() berbeda",
        ),
        (
            # Traceback Python berguna di AKHIR, keluaran compiler di AWAL.
            # Memeriksa seluruh baris alih-alih tiga baris pertama membuat
            # keluaran compiler yang kebetulan menyebut kata itu dipotong dari
            # ujung yang salah.
            "deteksi Traceback melihat semua baris",
            "  if (baris.slice(0, 3).some((b) => b.includes(\"Traceback\"))) {",
            "  if (baris.some((b) => b.includes(\"Traceback\"))) {",
            "ringkas() berbeda",
        ),
    ]),
}


def jalankan(pembanding):
    hasil = subprocess.run(["node", os.path.join(SINI, pembanding)],
                           cwd=PAKET, capture_output=True, text=True)
    return hasil.returncode, hasil.stdout + hasil.stderr


def sel(pembanding, jalur, nama, dari, ke, kategori, asli):
    if asli.count(dari) != 1:
        print(f"    {nama:42s} JANGKAR TIDAK UNIK ({asli.count(dari)} kecocokan)")
        return False
    with open(jalur, "w", encoding="utf-8") as f:
        f.write(asli.replace(dari, ke))
    rc, keluaran = jalankan(pembanding)
    rusak = "SyntaxError" in keluaran or "Cannot find" in keluaran
    kena = kategori in keluaran
    ok = rc != 0 and kena and not rusak
    if rusak:
        sebab = "mutan tidak bisa dimuat Node"
    elif rc == 0:
        sebab = "pembandingnya HIJAU padahal sumbernya rusak"
    elif not kena:
        sebab = f"merah tapi BUKAN karena {kategori!r}"
    else:
        n = re.search(r"bergeser:? (\d+)", keluaran)
        sebab = f"{kategori} ({n.group(1) if n else '?'} temuan)"
    print(f"    {nama:42s} {'MERAH' if ok else 'TUMPUL':7s} {sebab}")
    return ok


def main():
    semua = []
    for pembanding, (jalur, mutan) in BATERAI.items():
        print(f"{pembanding}  (mutasi di {os.path.basename(jalur)})")
        with open(jalur, encoding="utf-8") as f:
            asli = f.read()

        # Pagar nol per baterai: tanpa mutasi apa pun, pembandingnya WAJIB
        # hijau. Tanpa ini, pembanding yang sudah merah sejak awal membuat
        # seluruh sel di bawahnya "merah" tanpa membuktikan apa pun.
        rc, keluaran = jalankan(pembanding)
        if rc != 0:
            print("    PAGAR NOL GAGAL: sudah merah sebelum dimutasi.")
            print("   ", keluaran.strip()[:400].replace("\n", "\n    "))
            semua.append(False)
            continue
        print("    pagar nol: hijau")

        try:
            for nama, dari, ke, kategori in mutan:
                semua.append(sel(pembanding, jalur, nama, dari, ke, kategori, asli))
        finally:
            with open(jalur, "w", encoding="utf-8") as f:
                f.write(asli)

        rc, _ = jalankan(pembanding)
        if rc != 0:
            print("    PEMULIHAN GAGAL: sumbernya tidak kembali seperti semula.")
            semua.append(False)
        else:
            print("    pemulihan: hijau lagi")
        print()

    if all(semua):
        print(f"SEMUA {len(semua)} sel MERAH: pembandingnya bergigi.")
        return 0
    print(f"{semua.count(False)} dari {len(semua)} sel TUMPUL.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
