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


PAKET_WEB = os.path.join(os.path.dirname(PAKET), "web")


def sumber(nama):
    return os.path.join(PAKET, "src", nama)


def sumber_web(nama):
    return os.path.join(PAKET_WEB, "src", nama)


# {label: (pembanding, paket, berkas sumber, [(nama, dari, ke, kategori)])}
#
# `paket` ada karena baterai ini tidak lagi hanya menguji `packages/bersama`:
# pembanding editor tinggal di `packages/web/uji`, dan sumber yang dimutasinya
# `packages/web/src`. Menurunkannya dari ekstensi berkas -- `.ts` berarti
# bersama, `.mjs` berarti web -- memang lebih singkat, tapi ia benar hanya
# selama kebetulan itu bertahan, dan pembanding berikutnya yang memakai
# ekstensi "salah" akan dijalankan dari direktori yang salah dengan pesan
# "Cannot find module" yang menyalahkan impornya.
#
# Dan `label` terpisah dari `pembanding` karena satu pembanding bisa punya DUA
# berkas sumber: `banding-pratinjau` mengadu logika di `pratinjau-css.ts` DAN
# identitas byte pelapor tinggi di `Pratinjau.tsx`. Satu mutasi cuma bisa
# menyentuh satu berkas, jadi keduanya butuh entri sendiri.
#
# Mutan dipilih supaya masing-masing merusak LAPISAN yang berbeda, dan supaya
# hampir semuanya TIDAK menimbulkan error di mana pun -- persis jenis kerusakan
# yang cuma rekaman ini bisa menangkap.
BATERAI = {
    "golden-sorot.ts": ("golden-sorot.ts", PAKET, sumber("sorot.ts"), [
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
    "golden-beda.ts": ("golden-beda.ts", PAKET, sumber("beda.ts"), [
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
    "golden-galat.ts": ("golden-galat.ts", PAKET, sumber("galat.ts"), [
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
    # Pembanding ini beda jenis dari tiga di atasnya: ia tidak mengadu dengan
    # rekaman Python melainkan dengan `editor.js` yang masih berjalan di
    # aplikasi lama, potongan demi potongan, atas seluruh kode kurikulum.
    # Mutan terakhirnya menagih asersi yang TERPISAH dari perbandingan itu --
    # identitas byte, satu-satunya sifat yang dua sisi bisa langgar bersamaan
    # tanpa pernah berbeda satu sama lain.
    "banding-editor.mjs": ("banding-editor.mjs", PAKET_WEB,
                           sumber_web("komponen/editor-teks.ts"), [
        (
            # Pembuka membaca tinggi tumpukan SEBELUM push. Menukarnya menggeser
            # seluruh warna satu tingkat, dan pasangan pembuka-penutup berhenti
            # berwarna sama -- satu-satunya hal yang membuat fitur ini berguna.
            "pembuka membaca tumpukan sesudah push",
            "        hasil.push([jenis, c, tumpukan.length % WARNA_KURUNG]);\n"
            "        tumpukan.push(c);",
            "        tumpukan.push(c);\n"
            "        hasil.push([jenis, c, tumpukan.length % WARNA_KURUNG]);",
            "pisahKurung",
        ),
        (
            # Kurung di dalam string dan komentar ikut dihitung: 2.270 + 981 di
            # kurikulum ini, dan satu saja meracuni kedalaman SELURUH kode
            # sesudahnya.
            "jenis token tidak lagi disaring",
            '    if (jenis !== "operator") {',
            '    if (jenis === "jenis-yang-tidak-ada") {',
            "pisahKurung",
        ),
        (
            # Spasi pembuka baris tetap dibelah di tempat yang benar, cuma
            # berhenti mengaku indentasi. Tidak ada byte yang bergeser, tidak
            # ada potongan yang hilang -- yang hilang cuma pemandunya.
            "potongan indentasi memakai jenis induknya",
            '      hasil.push(["indentasi", teks.slice(a - pos, b - pos), null]);',
            "      hasil.push([jenis, teks.slice(a - pos, b - pos), null]);",
            "pisahInden",
        ),
        (
            # `atas` sengaja TIDAK dijepit ke nol: baris yang tergulir keluar
            # pandangan memang bernilai negatif, dan dijepit ia jadi garis macet
            # di tepi atas yang mengaku "baris aktifmu di sini".
            "posisi pita dijepit ke nol",
            "    atas: paddingAtas + (n - 1) * tinggiBaris - scrollTop,",
            "    atas: Math.max(0, paddingAtas + (n - 1) * tinggiBaris - scrollTop),",
            "posisiPita",
        ),
        (
            # Kurungnya ikut lagi di potongan sesudahnya, jadi gabungan teksnya
            # lebih panjang daripada masukannya. Warnanya tetap masuk akal dan
            # tidak ada error di mana pun; yang terjadi cuma kursor mendarat di
            # huruf yang salah, makin jauh makin melenceng.
            "kurung tidak dilewati sesudah dipotong",
            "      mulai = i + 1;",
            "      mulai = i;",
            "IDENTITAS BYTE RUSAK",
        ),
    ]),
    "banding-pratinjau.mjs (logika)": (
        "banding-pratinjau.mjs", PAKET_WEB,
        sumber_web("komponen/pratinjau-css.ts"), [
            (
                # Pemilih di dalam @media hilang seluruhnya: cabang at-rule
                # yang tidak dikenali MELEWATI badannya. Halaman contohnya
                # tetap terbentuk dan tetap masuk akal -- cuma kehilangan
                # justru elemen yang aturan responsifnya mau ditunjukkan.
                "@media berhenti dianggap memuat pemilih",
                "        if (/^@(media|supports|layer|container|scope)\\b/.test(kepala)) {",
                "        if (/^@(supports|layer|container|scope)\\b/.test(kepala)) {",
                "halamanDariCss",
            ),
            (
                # `.menu > li` jadi <div class="menu"><li> tanpa <ul>. Browser
                # menampilkan butirnya sebagai teks polos tanpa bulatan, dan
                # pelajar menyimpulkan aturannya tidak berlaku.
                "induk wajib tidak pernah disisipkan",
                '    butuh = INDUK_WAJIB[nama] || "";',
                '    butuh = "";',
                "halamanDariCss",
            ),
            (
                # Batas jumlah contoh dipotong. Aturan ke-5 dan sesudahnya
                # tidak punya elemen untuk dikenai, jadi pelajar melihat
                # separuh lembar gayanya seolah tidak berpengaruh apa pun.
                "batas contoh dipangkas",
                "const MAKS_CONTOH = 14;",
                "const MAKS_CONTOH = 4;",
                "halamanDariCss",
            ),
            (
                # Blok yang SUDAH memuat markup berhenti dikenali, jadi ia
                # dikarang ulang -- dan 11 dari 40 blok CSS di kurikulum
                # berbentuk halaman utuh. Label "dibuatkan" ikut berbohong.
                "markup yang sudah ada tidak dikenali",
                "    .test(kode);",
                "    .test(kode) && false;",
                "adaMarkup",
            ),
        ]),
    "banding-pratinjau.mjs (pelapor)": (
        "banding-pratinjau.mjs", PAKET_WEB,
        sumber_web("komponen/Pratinjau.tsx"), [
            (
                # Satu-satunya pagar untuk skrip yang jalan di dalam bingkai
                # ber-asal buram. Mutasi ini justru yang paling mungkin terjadi
                # sungguhan: seseorang "merapikan" satu sisi dan lupa sisi
                # lainnya, dan tinggi bingkai mulai berbeda antara dua
                # antarmuka tanpa satu pun error.
                "pelapor tinggi memakai scrollHeight",
                "      bawah = b.getBoundingClientRect().bottom;",
                "      bawah = document.documentElement.scrollHeight;",
                "PELAPOR BERBEDA",
            ),
        ]),
}


def jalankan(pembanding, akar):
    hasil = subprocess.run(["node", os.path.join(akar, "uji", pembanding)],
                           cwd=akar, capture_output=True, text=True)
    return hasil.returncode, hasil.stdout + hasil.stderr


def sel(pembanding, akar, jalur, nama, dari, ke, kategori, asli):
    if asli.count(dari) != 1:
        print(f"    {nama:42s} JANGKAR TIDAK UNIK ({asli.count(dari)} kecocokan)")
        return False
    with open(jalur, "w", encoding="utf-8") as f:
        f.write(asli.replace(dari, ke))
    rc, keluaran = jalankan(pembanding, akar)
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
        n = re.search(r"(?i:bergeser):? (\d+)", keluaran)
        sebab = f"{kategori} ({n.group(1) if n else '?'} temuan)"
    print(f"    {nama:42s} {'MERAH' if ok else 'TUMPUL':7s} {sebab}")
    return ok


def main():
    semua = []
    for label, (pembanding, akar, jalur, mutan) in BATERAI.items():
        print(f"{label}  (mutasi di {os.path.basename(jalur)})")
        with open(jalur, encoding="utf-8") as f:
            asli = f.read()

        # Pagar nol per baterai: tanpa mutasi apa pun, pembandingnya WAJIB
        # hijau. Tanpa ini, pembanding yang sudah merah sejak awal membuat
        # seluruh sel di bawahnya "merah" tanpa membuktikan apa pun.
        rc, keluaran = jalankan(pembanding, akar)
        if rc != 0:
            print("    PAGAR NOL GAGAL: sudah merah sebelum dimutasi.")
            print("   ", keluaran.strip()[:400].replace("\n", "\n    "))
            semua.append(False)
            continue
        print("    pagar nol: hijau")

        try:
            for nama, dari, ke, kategori in mutan:
                semua.append(
                    sel(pembanding, akar, jalur, nama, dari, ke, kategori, asli))
        finally:
            with open(jalur, "w", encoding="utf-8") as f:
                f.write(asli)

        rc, _ = jalankan(pembanding, akar)
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
