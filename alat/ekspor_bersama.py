"""Ekspor tabel leksikal penyorot ke `packages/bersama/data/`.

Kenapa ada. `inti/sorot.py` memuat DUA hal: algoritma pemindainya dan daftar
kata kuncinya. Yang pertama diport ke TypeScript; yang kedua tidak boleh ikut
diport, karena daftar yang diketik ulang akan menyimpang dan gejalanya cuma
"warnanya beda di dua tempat" -- tidak ada error di mana pun.

Hari ini daftar itu sampai ke browser lewat `/api/awal` -> `isi.aturan_penyorot`.
Itu benar selama servernya Python. Begitu pemindainya hidup di paket TS yang
diuji sendiri, ia butuh tabelnya TANPA server yang berjalan -- jadi tabelnya
ditulis ke berkas, dihasilkan dari `sorot.ATURAN`, dan dijaga tes.

DUA hal yang sengaja berbeda dari `isi.aturan_penyorot()`:

* **Alias ikut diekspor.** `aturan_penyorot()` memakai `bahasa_didukung()`, yang
  membuang duplikat berdasarkan `id()` -- jadi `c++`, `ts`, `py`, `sh` hilang
  dari tabel yang dikirim ke browser. Itu tidak pernah jadi masalah karena
  `isi.bahasa_sorot()` kebetulan tidak pernah mengembalikan nama-nama itu.
  "Kebetulan tidak pernah" bukan jaminan, dan tabel yang lengkap menutup
  seluruh kelasnya: aturan ditulis sekali per bentuk kanonik, aliasnya jadi
  peta nama -> nama.
* **Pemetaan `sorot_untuk` ikut dibawa.** Medan `"bahasa"` di materi memakai
  nama yang BUKAN nama penyorot (`terminal`, `jsx`, `postgresql`), dan
  `inti/berkas.py` yang menerjemahkannya. Tanpa peta itu di sini, sisi TS akan
  menerjemahkannya sendiri -- tabel kedua, dan satu-satunya gejalanya 408 blok
  kode yang warnanya berbeda dari yang digambar server.

    python3 alat/ekspor_bersama.py            # periksa, tanpa menulis
    python3 alat/ekspor_bersama.py --tulis    # tulis berkasnya
"""

import argparse
import json
import os
import re
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from inti import berkas, galat, sorot  # noqa: E402

TUJUAN = os.path.join(AKAR, "packages", "bersama", "data")
NAMA = "aturan-sorot.json"
NAMA_GALAT = "pola-galat.json"


def _aturan_jadi_dict(a):
    """Satu `Aturan` jadi objek JSON. Bentuknya mengikuti `isi.aturan_penyorot`.

    `kutip` TIDAK diurutkan di sini: `Aturan.__init__` sudah mengurutkannya dari
    yang terpanjang supaya kutip tiga menang atas kutip tunggal, dan urutan itu
    BAGIAN DARI ALGORITMA -- pemindai mencari kutip pembuka dengan `find` pada
    daftar ini. Mengurutkannya alfabetis akan membuat blok kutip-tiga di Python
    terbaca sebagai string kosong lalu string kosong lagi.
    """
    return {
        "komentar_baris": list(a.komentar_baris),
        "komentar_blok": [list(p) for p in a.komentar_blok],
        "kutip": list(a.kutip),
        "kutip_mentah": sorted(a.kutip_mentah),
        "escape": a.escape,
        "kunci": sorted(a.kunci),
        "tipe": sorted(a.tipe),
        "bawaan": sorted(a.bawaan),
        "praprosesor": a.praprosesor,
        "variabel_dolar": a.variabel_dolar,
        "tanpa_bedakan_kapital": a.tanpa_bedakan_kapital,
    }


def susun():
    """{aturan, alias, pemetaan} -- tabel lengkap untuk pemindai di luar Python."""
    aturan, alias, kanonik_dari_id = {}, {}, {}

    # Nama pertama yang menunjuk sebuah objek jadi bentuk kanoniknya. Urutan
    # `ATURAN` dipertahankan Python sejak 3.7, dan di sorot.py bentuk kanonik
    # SELALU ditulis sebelum aliasnya -- baris yang membuat alias "c++" ada di
    # bawah definisi "cpp", bukan di atasnya.
    for nama, a in sorot.ATURAN.items():
        kunci_id = id(a)
        if kunci_id in kanonik_dari_id:
            alias[nama] = kanonik_dari_id[kunci_id]
        else:
            kanonik_dari_id[kunci_id] = nama
            aturan[nama] = _aturan_jadi_dict(a)

    # `sorot_untuk` untuk setiap nama yang bisa muncul di medan `"bahasa"`.
    # Yang memetakan ke dirinya sendiri dibuang: ia tidak membawa informasi,
    # dan membiarkannya membuat berkas ini terbaca seperti daftar bahasa yang
    # didukung padahal bukan.
    pemetaan = {}
    for nama in list(berkas.BAHASA_LUAR) + ["terminal", "teks"]:
        tujuan = berkas.sorot_untuk(nama)
        if tujuan != nama:
            pemetaan[nama] = tujuan

    return {
        "catatan": "DIHASILKAN alat/ekspor_bersama.py dari inti/sorot.py dan "
                   "inti/berkas.py. Jangan disunting dengan tangan.",
        "aturan": aturan,
        "alias": dict(sorted(alias.items())),
        "pemetaan": dict(sorted(pemetaan.items())),
    }


def _ganti_gaya_js(pesan):
    """Rujukan grup `\\1` gaya Python jadi `$1` gaya JavaScript.

    `$` di-escape LEBIH DULU. Tidak satu pun dari 60 pesan hari ini memuatnya,
    tapi pesan pertama yang memuat `$9,99` akan menghasilkan rujukan grup palsu
    kalau urutannya dibalik -- dan gejalanya bukan error melainkan satu kalimat
    penjelasan yang potongannya hilang.
    """
    keluar = pesan.replace("$", "$$")
    return re.sub(r"\\(\d)", r"$\1", keluar)


def susun_galat():
    """Tabel pola pesan error, untuk penerjemah di luar Python.

    Polanya DISALIN apa adanya dari `galat.POLA`. Semua ke-60-nya memakai
    konstruksi yang sama artinya di JavaScript (`(?:...)`, `\\b`, `\\s`,
    `\\w`, `\\d`, kelas karakter, escape tanda baca), jadi yang perlu
    diterjemahkan cuma rujukan grup di pesannya.

    Satu beda yang DIBIARKAN dan harus diketahui: `\\w` di Python mencakup
    huruf Unicode, di JavaScript cuma ASCII. Ke-60 pola ini memakainya untuk
    nama pengenal dan nama tag -- semuanya ASCII -- jadi hasilnya sama. Pola
    BARU yang perlu mencocokkan huruf berdiakritik tidak boleh mengandalkan
    `\\w`; pakai kelas karakter eksplisit.
    """
    pola = [{"pola": p, "ganti": _ganti_gaya_js(pesan)} for p, pesan in galat.POLA]
    return {
        "catatan": "DIHASILKAN alat/ekspor_bersama.py dari inti/galat.py. "
                   "Jangan disunting dengan tangan.",
        # Bendera `re.IGNORECASE | re.DOTALL` dipasang sekali di Python; sisi TS
        # harus memasang padanannya (`i` dan `s`) sendiri, jadi ia dicatat di
        # sini alih-alih diingat.
        "bendera": "is",
        "pola": pola,
        # Tiga pola `rapikan()` ikut, dengan alasan yang sama seperti tabel
        # kata kunci: yang diketik ulang akan menyimpang, dan menyimpangnya
        # tidak menimbulkan error -- cuma jalur direktori sementara yang bocor
        # ke layar pelajar, atau nomor baris yang berhenti digeser.
        "rapikan": {
            "path": galat._POLA_PATH.pattern,
            "baris_berkas": galat._POLA_BARIS_BERKAS.pattern,
            "kata_line": galat._POLA_KATA_LINE.pattern,
        },
    }


def buktikan(tabel):
    """Setiap nama di `sorot.ATURAN` wajib bisa dicari lewat tabel ini."""
    keluhan = []
    for nama, a in sorot.ATURAN.items():
        kanonik = tabel["alias"].get(nama, nama)
        ada = tabel["aturan"].get(kanonik)
        if ada is None:
            keluhan.append(f"{nama}: tidak ketemu (kanonik {kanonik!r})")
        elif ada != _aturan_jadi_dict(a):
            keluhan.append(f"{nama}: aturannya berbeda dari sorot.ATURAN")

    # Pemetaan tidak boleh menunjuk nama yang tidak ada aturannya: itu akan
    # menyorot polos di TS sementara Python menyorotnya penuh.
    for dari, ke in tabel["pemetaan"].items():
        if ke not in tabel["aturan"] and ke not in tabel["alias"]:
            keluhan.append(f"pemetaan {dari} -> {ke}: {ke!r} tidak punya aturan")
    return keluhan


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tulis", action="store_true")
    a = ap.parse_args()

    tabel = susun()
    keluhan = buktikan(tabel)
    teks = json.dumps(tabel, ensure_ascii=False, indent=1) + "\n"

    tabel_galat = susun_galat()
    teks_galat = json.dumps(tabel_galat, ensure_ascii=False, indent=1) + "\n"

    print(f"{len(tabel['aturan'])} aturan kanonik, {len(tabel['alias'])} alias, "
          f"{len(tabel['pemetaan'])} pemetaan bahasa, {len(teks) / 1e3:.0f} KB")
    print(f"{len(tabel_galat['pola'])} pola pesan galat, "
          f"{len(teks_galat) / 1e3:.0f} KB")
    if keluhan:
        print("DITOLAK:")
        print("\n".join("  - " + k for k in keluhan[:20]))
        return 1
    print(f"semua {len(sorot.ATURAN)} nama di sorot.ATURAN bisa dicari lewat tabel ini")

    if a.tulis:
        os.makedirs(TUJUAN, exist_ok=True)
        for nama, isi_teks in ((NAMA, teks), (NAMA_GALAT, teks_galat)):
            with open(os.path.join(TUJUAN, nama), "w", encoding="utf-8") as f:
                f.write(isi_teks)
            print(f"  ditulis packages/bersama/data/{nama}")
    else:
        print("  (belum ditulis; tambahkan --tulis)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
