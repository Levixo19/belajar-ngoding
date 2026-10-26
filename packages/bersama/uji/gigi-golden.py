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
    # Kategorinya nama JENIS gambar, diambil dari baris `JENIS BERGESER`.
    # Tiga temuan pertama yang dicetak pembanding tidak cukup: satu perubahan
    # di `s()` menyentuh ketiga belas jenis, dan jenis mana yang kebetulan
    # muncul lebih dulu tergantung urutan berkas di direktori.
    "banding-visual.mjs": (
        "banding-visual.mjs", PAKET_WEB,
        sumber_web("komponen/visual-bentuk.ts"), [
            (
                # Pemetaan `kelas` -> `class` dilepas: atributnya jadi `kelas`,
                # yang tidak berarti apa pun bagi CSS. Gambarnya tetap utuh
                # bentuknya dan tetap tergambar -- cuma kehilangan SELURUH
                # warnanya, di keempat tema, tanpa satu pun error.
                "atribut kelas tidak dipetakan ke class",
                'keluar[k === "kelas" ? "class" : k] = String(v);',
                "keluar[k] = String(v);",
                "tabel",
            ),
            (
                # `pathLength` dipasang juga pada garis putus-putus. Dasharray
                # ikut diukur dalam satuan pathLength, jadi "4 4" berubah jadi
                # satu garis utuh: garis hidup pelaku di diagram urutan
                # berhenti terlihat sebagai garis bayangan.
                "pathLength dipasang pada garis putus",
                'const putus = (kelas: string) => (/putus/.test(kelas) ? null : 1);',
                "const putus = (kelas: string) => (kelas ? 1 : 1);",
                "urutan",
            ),
            (
                # Lebar simpul pohon bergeser 2 piksel. Tidak ada yang rusak
                # dan tidak ada yang terlihat salah -- sampai dua simpul
                # bertabrakan di pohon yang paling padat.
                "lebar simpul pohon bergeser",
                "  const lebarSimpul = (n: SimpulPohon) => Math.max(46, lebarTeks(n.teks) + 22);",
                "  const lebarSimpul = (n: SimpulPohon) => Math.max(46, lebarTeks(n.teks) + 20);",
                "pohon",
            ),
            (
                # Bit dipadati spasi, bukan nol. Angka 5 pada lebar 8 jadi
                # "     101" dan lima kotak pertamanya kosong -- yang persis
                # kebalikan dari hal yang gambar ini ada untuk mengajarkan.
                "bit dipadati spasi",
                'const bit = sp.angka.toString(2).padStart(lebar, "0");',
                'const bit = sp.angka.toString(2).padStart(lebar, " ");',
                "bit",
            ),
            (
                "ketelitian titik kurva berubah",
                "p.map((v) => v.toFixed(1)).join(\",\")",
                "p.map((v) => v.toFixed(2)).join(\",\")",
                "kurva",
            ),
            (
                # Seluruh isi wadah flex bergeser 6 piksel ke atas sementara
                # wadahnya tidak. Labelnya tetap di tempatnya, jadi yang
                # terlihat kotak yang menempel ke tepi atas wadah.
                "asal wadah tata bergeser",
                "  const x0 = PAD, y0 = PAD + 36;",
                "  const x0 = PAD, y0 = PAD + 30;",
                "tata",
            ),
        ]),
    "banding-jejak.mjs": (
        "banding-jejak.mjs", PAKET_WEB,
        sumber_web("komponen/jejak-teks.ts"), [
            (
                # Dua baris sumber menyatu jadi satu. Panel menomori barisnya
                # dari hasil ini lalu menyorot baris yang dikirim pelacak
                # Python -- jadi seluruh sisa rekaman menyorot baris yang
                # salah, dan yang dipelajari orang urutan eksekusi yang tidak
                # pernah terjadi. Selnya menagih asersi penyambungan ulang,
                # yang TERPISAH dari perbandingan: kedua sisi bisa konsisten
                # salah dan hasil yang cocok tidak memberi tahu apa pun.
                "pemisah baris dilewati satu",
                "      if (i > 0) baris.push([]);",
                "      if (i > 1) baris.push([]);",
                "PENYAMBUNGAN RUSAK",
            ),
            (
                # Potongan kosong ikut jadi token. Teksnya tetap tersambung
                # benar dan jumlah barisnya tetap benar; yang berubah cuma
                # jumlah simpul yang digambar per baris.
                "potongan kosong ikut jadi token",
                "      if (p) (baris[baris.length - 1] as Token[]).push([jenis, p]);",
                "      (baris[baris.length - 1] as Token[]).push([jenis, p]);",
                "tokenPerBaris",
            ),
            (
                "nilai kembali kosong disebut null",
                "    return `${atas.nama} selesai dan mengembalikan "
                "${l.nilai ? l.nilai.r : \"None\"}.`;",
                "    return `${atas.nama} selesai dan mengembalikan "
                "${l.nilai ? l.nilai.r : \"null\"}.`;",
                "kalimat kembali",
            ),
            (
                # Kalimat penutup rekaman hilang. Tidak ada yang rusak; yang
                # hilang cuma satu-satunya tanda bahwa rekamannya memang
                # berhenti di situ, bukan macet.
                "penanda langkah terakhir dilepas",
                '    + (adaBerikut ? "" : " Ini langkah terakhir yang tercatat.");',
                '    + (adaBerikut ? "" : "");',
                "kalimat baris",
            ),
        ]),
    "banding-kerja.mjs": (
        "banding-kerja.mjs", PAKET_WEB,
        sumber_web("layar/kerja-beda.ts"), [
            (
                # Tangga "lihat jawaban" membuka dari KEPALA, bukan dari ekor.
                # Yang disajikan jadi import dan deklarasi -- bagian yang sudah
                # ada di editor pelajar sendiri -- sementara baris terakhir,
                # tempat hasilnya dicetak, baru keluar di langkah terakhir.
                "potongan solusi diambil dari kepala",
                "    potongan.push(baris.slice(n - panjang));",
                "    potongan.push(baris.slice(0, panjang));",
                "pisahRekor",
            ),
            (
                # Solusi pendek dapat tiga langkah, bukan dua: tiga klik untuk
                # empat baris, tangga yang anak-anaknya lebih banyak daripada
                # yang dinaiki. 79 dari 558 solusi berpanjang <= 12 baris.
                #
                # Sel ini MENGGANTIKAN sel yang mencabut pin langkah terakhir
                # (`i === langkah ? n : ...`). Sel itu tetap HIJAU, dan itu
                # temuan, bukan kegagalan baterai: pin tersebut tidak pernah
                # mengubah hasil untuk rumus yang sekarang. Alasannya ditulis
                # di komentar `pisahRekor`, beserta kenapa ia dipertahankan.
                "solusi pendek dapat tiga langkah",
                "  const alami = n <= AMBANG_REKOR ? 2 : LANGKAH_REKOR;",
                "  const alami = LANGKAH_REKOR;",
                "pisahRekor",
            ),
            (
                # Pemutus seri LCS dibalik. Diff-nya tetap benar sebagai diff;
                # yang berubah sisi mana yang dianggap "hilang" dan mana yang
                # "bertambah" saat keduanya sama panjang -- dan itu menentukan
                # baris mana yang dipasangkan ke baris mana sesudahnya.
                "pemutus seri diff baris dibalik",
                "    } else if ((tabel[i + 1] as Uint16Array)[j]! >= "
                "(tabel[i] as Uint16Array)[j + 1]!) {\n"
                "      keluar.push({ tanda: \"-\", teks: a[i] as string, nomor });",
                "    } else if ((tabel[i + 1] as Uint16Array)[j]! > "
                "(tabel[i] as Uint16Array)[j + 1]!) {\n"
                "      keluar.push({ tanda: \"-\", teks: a[i] as string, nomor });",
                "bedaBaris",
            ),
            (
                # Token bersebelahan yang bertanda sama berhenti dilebur. "Dua
                # kata berurutan berubah" tampil sebagai dua kotak dengan jeda
                # di antaranya, dan yang terbaca jadi dua ubahan terpisah
                # padahal cuma satu.
                "segmen bersebelahan tidak dilebur",
                "    if (akhir && akhir.tanda === tanda) akhir.teks += teks;",
                "    if (akhir && akhir.tanda === tanda && false) akhir.teks += teks;",
                "bedaKata",
            ),
            (
                # Alternatif "satu karakter apa pun" dicabut dari pemecah
                # token, jadi tanda baca HILANG. Selnya menagih kontrak
                # lossless, yang TERPISAH dari perbandingan: kedua sisi bisa
                # konsisten salah.
                "pemecah token kehilangan tanda baca",
                "const POLA_TOKEN_KATA = /\\s+|[\\p{L}\\p{N}_]+|[^\\s]/gu;",
                "const POLA_TOKEN_KATA = /\\s+|[\\p{L}\\p{N}_]+/gu;",
                "PECAH TOKEN RUSAK",
            ),
            (
                # Kelompok tangkap diganti seluruh kecocokan: `parseInt` atas
                # "jawab.py:12" memberi NaN, jadi tombol "ke baris" lahir
                # untuk baris NaN -- dan tidak ada error di mana pun.
                "nomor baris dibaca dari seluruh kecocokan",
                "  return m ? parseInt(m[1] as string, 10) : 0;",
                "  return m ? parseInt(m[0] as string, 10) : 0;",
                "nomorDiBaris",
            ),
            (
                # Salinan dangkal diganti salinan larik: butir masukannya
                # dimutasi di tempat. Hasilnya SAMA PERSIS, jadi perbandingan
                # hasil tidak bisa melihatnya -- yang menagihnya pagar
                # kemurnian yang terpisah.
                "pasangkanUbahan memutasi masukannya",
                "  const keluar: ButirBeda[] = baris.map((d) => ({ ...d }));",
                "  const keluar: ButirBeda[] = baris.slice();",
                "MENCEMARI MASUKAN",
            ),
            (
                # Satu karakter di contoh awal Java. Ruang Coba terbuka dengan
                # program yang tidak bisa dikompilasi, pada bahasa yang
                # mungkin tidak ada yang mencobanya selama berbulan-bulan --
                # dan yang pertama menemukannya pelajar, yang akan menyangka
                # dirinya salah.
                "satu karakter di contoh awal Java",
                "        System.out.println(\"Halo, dunia!\");\\n    }\\n}\\n'",
                "        System.out.printl(\"Halo, dunia!\");\\n    }\\n}\\n'",
                "contohAwal",
            ),
            (
                # Satu bahasa dicabut dari tabel contoh. Perbandingan byte-nya
                # ikut merah, TAPI kategori yang ditagih sel ini pagar yang
                # lain: daftar runner yang contohnya kosong. Tanpa pagar itu,
                # bahasa baru yang contohnya lupa ditambahkan akan tampil
                # sebagai dua string kosong yang cocok -- hijau, dan Ruang
                # Coba-nya terbuka kosong.
                "python dicabut dari tabel contoh",
                "  python: 'nama = \"dunia\"\\nprint(f\"Halo, {nama}!\")\\n',",
                "  pythonx: 'nama = \"dunia\"\\nprint(f\"Halo, {nama}!\")\\n',",
                "RUNNER TANPA CONTOH AWAL",
            ),
        ]),
    "banding-prosa.mjs": (
        "banding-prosa.mjs", PAKET_WEB,
        sumber_web("komponen/prosa-teks.ts"), [
            (
                # Backtick tidak dibuang dari isi chip. Terminal memakai
                # backtick sebagai penanda, web memakai kotak -- jadi yang
                # terbaca pelajar kotak yang MEMUAT penandanya sendiri.
                "backtick tidak dibuang dari chip",
                """      teks: cocok.charAt(0) === "`" ? cocok.slice(1, -1) : cocok,""",
                """      teks: cocok,""",
                "segmenKode",
            ),
            (
                # Kursor maju satu karakter kurang, jadi karakter terakhir
                # setiap chip muncul DUA KALI -- sekali di dalam kotaknya,
                # sekali di teks sesudahnya.
                #
                # Sel ini MENGGANTIKAN sel yang mencabut `POLA_KODE.lastIndex
                # = 0`. Sel itu tetap HIJAU, dan itu temuan: loopnya selalu
                # jalan sampai `exec` mengembalikan null, dan di situ mesin
                # regex sudah menyetel `lastIndex` kembali ke nol sendiri.
                # Alasannya ditulis di komentar `segmenKode`, beserta kenapa
                # reset itu dipertahankan.
                "kursor maju satu karakter kurang",
                "    akhir = m.index + cocok.length;",
                "    akhir = m.index + cocok.length - 1;",
                "segmenKode",
            ),
            (
                # Potongan kosong ikut didorong setiap kali chip menempel di
                # chip sebelumnya atau berdiri di awal baris. Teksnya tetap
                # tersambung benar; yang berubah cacah simpul per paragraf.
                "potongan kosong ikut didorong",
                "    if (m.index > akhir) keluar.push(teks.slice(akhir, m.index));",
                "    if (m.index >= akhir) keluar.push(teks.slice(akhir, m.index));",
                "segmenKode",
            ),
            (
                # Jalur "tidak ada chip sama sekali" mengembalikan NOL
                # potongan, bukan teksnya. 87% blok prosa lewat jalur itu --
                # artinya hampir seluruh materi tampil kosong. Selnya menagih
                # kontrak penyambungan ulang, yang TERPISAH dari perbandingan.
                "jalur tanpa chip mengembalikan kosong",
                "  if (!keluar.length) return [teks];",
                "  if (!keluar.length) return [];",
                "PENYAMBUNGAN RUSAK",
            ),
        ]),
    "banding-belajar.mjs": (
        "banding-belajar.mjs", PAKET_WEB,
        sumber_web("layar/belajar-teks.ts"), [
            (
                # Elipsis memakan satu huruf lebih sedikit, jadi judul yang
                # dipotong jadi 27 karakter di kotak yang menampung 26. Tidak
                # ada yang rusak; yang terjadi satu huruf terdorong keluar
                # kotaknya di SETIAP judul panjang di kaki pembaca.
                "elipsis meleset satu huruf",
                '  return t && t.length > n ? t.slice(0, n - 1) + "…" : t;',
                '  return t && t.length > n ? t.slice(0, n) + "…" : t;',
                "potong",
            ),
            (
                # Batas "kalimat pertama cukup pendek" DITURUNKAN dari 52 ke
                # 30: 22.564 baris pindah dari jalur "potong di kalimat" ke
                # jalur "potong di kata", jadi labelnya berhenti di tengah
                # kalimat padahal kalimatnya pendek.
                #
                # Sel ini MENGGANTIKAN sel yang MENAIKKAN ambangnya ke 62. Sel
                # itu tetap hijau atas 8.475 baris yang titiknya jatuh di
                # rentang itu -- bukan karena korpusnya kurang, melainkan
                # karena setiap nilai >= 45 berperilaku sama. Alasannya ditulis
                # di komentar `labelPeta`.
                "ambang kalimat pendek diturunkan",
                "  let awal = titik > 8 && titik < 52 ? teks.slice(0, titik) : teks;",
                "  let awal = titik > 8 && titik < 30 ? teks.slice(0, titik) : teks;",
                "labelPeta",
            ),
            (
                # Potongnya di spasi PERTAMA, bukan spasi terakhir sebelum 44.
                # Label peta jadi satu kata untuk hampir setiap bagian, dan
                # peta yang seluruh butirnya "Di" tidak menandai apa pun.
                "batas kata dicari dari depan",
                '    const batas = awal.lastIndexOf(" ", 44);',
                '    const batas = awal.indexOf(" ");',
                "labelPeta",
            ),
            (
                # Deret spasi tidak lagi diruntuhkan jadi satu. Label yang
                # datang dari baris berkolom membawa perataan tabelnya ke
                # dalam peta, tempat perataan itu tidak berarti apa-apa.
                "deret spasi tidak diruntuhkan",
                '    .replace(/\\s+/g, " ").trim();',
                '    .replace(/\\s/g, " ").trim();',
                "labelPeta",
            ),
        ]),
    "banding-ikon.mjs": (
        "banding-ikon.mjs", PAKET_WEB,
        sumber_web("komponen/ikon-bentuk.ts"), [
            (
                # Tabel jalurnya DISALIN dari `ikon.js`, dan salinan adalah hal
                # yang paling mudah melenceng tanpa tanda: satu koordinat yang
                # salah ketik menghasilkan ikon yang tetap tergambar, tetap
                # tanpa error, dan cuma terlihat sedikit aneh.
                "satu koordinat ikon materi",
                '"M12 6.5v15"',
                '"M12 6.5v14"',
                "ikon(materi",
            ),
            (
                # Penjaga `fill` berbasis INDEKS. Penjaga lama di sisi JS
                # memeriksa `d.endsWith("18Z")`, dan KEDUA jalur ikon "sedang"
                # kebetulan berakhir begitu -- jadi separuh lingkarannya tidak
                # pernah terisi dan "sedang dikerjakan" tak bisa dibedakan dari
                # "belum". Sel ini menagih keadaan sesudah perbaikan itu.
                "isi 'sedang' dari jalur pertama",
                'nama === "sedang" && i > 0',
                'nama === "sedang" && i >= 0',
                "ikon(sedang",
            ),
            (
                "tangga tingkat berhenti diisi",
                'return nama === "tingkat" || ',
                "return false || ",
                "ikon(tingkat",
            ),
            (
                "ikonTipe jatuh ke materi, bukan bagian",
                'Record<string, string>)[tipe] ?? "bagian";',
                'Record<string, string>)[tipe] ?? "materi";',
                "ikonTipe",
            ),
            (
                # `null` untuk nama tak dikenal, BUKAN daftar kosong: komponennya
                # mengembalikan `null` (tidak menggambar apa pun) hanya kalau
                # jalurnya `null`. Dengan `[]` ia menggambar `<svg>` kosong, dan
                # yang terlihat kotak 20x20 tak terjelaskan di tengah baris.
                "ikon tak dikenal jadi daftar kosong",
                "return BENTUK[nama] ?? null;",
                "return BENTUK[nama] ?? [];",
                "ikon(tidak-ada",
            ),
        ]),
    # `banding-rasi.mjs` sebelumnya TIDAK punya sel sama sekali -- ia pembanding
    # pertama yang ditulis di paket web, dan baterai ini lahir sesudahnya. Jadi
    # tiga sel pertama di bawah membuktikan bagian yang sudah lama ada
    # (`hash`/`jariBintang`/`bentukRasi`), bukan cuma tata letak yang baru.
    "banding-rasi.mjs": (
        "banding-rasi.mjs", PAKET_WEB,
        sumber_web("komponen/rasi-geometri.ts"), [
            (
                # Satu bit di `hash` menggeser SETIAP rasi. `Math.imul`
                # mengalikan sebagai int32; perkalian biasa memakai float 64
                # dan kehilangan presisi di atas 2^53.
                "hash tanpa imul",
                "x = Math.imul(x ^ (c.codePointAt(0) ?? 0), 16777619);",
                "x = (x ^ (c.codePointAt(0) ?? 0)) * 16777619;",
                "hash",
            ),
            (
                "lantai jari bintang diturunkan",
                "Math.max(1.1, 7 * Math.exp",
                "Math.max(1.0, 7 * Math.exp",
                "jariBintang",
            ),
            (
                "belokan rasi dilebarkan",
                "sudut += (acak() - 0.5) * 2.7;",
                "sudut += (acak() - 0.5) * 2.8;",
                "bentukRasi",
            ),
            (
                # Pusat tiap rasi naik-turun mengikuti sinus. Menggesernya
                # memindahkan SELURUH peta tanpa satu pun error.
                "pusat rasi digeser",
                "H * 0.46 + Math.sin",
                "H * 0.5 + Math.sin",
                "petaRasi",
            ),
            (
                # Label boleh selebar DUA rasi karena ia bergantian atas-bawah.
                # Menghitungnya dari satu rail memangkas judul bab jauh lebih
                # awal daripada yang perlu.
                "batas label dihitung dari satu rail",
                "Math.floor((lebarRasi * 2) / 6.8)",
                "Math.floor((lebarRasi * 1) / 6.8)",
                "petaRasi",
            ),
            (
                # Garis ke-j berbagi `--i` dengan bintang ke-j. Menggesernya
                # satu membuat koreografi garis-tergambar mendahului
                # bintangnya -- gerak yang salah, tanpa geometri yang salah.
                "--i garis bergeser satu",
                "            urut: urutan,",
                "            urut: urutan + 1,",
                "petaRasi",
            ),
            (
                # Jangkar label di ujung. Sel ini butuh kurikulum berBAB DUA,
                # dan kurikulum terkecil di repo ini punya enam -- jadi korpus
                # pembandingnya sengaja memuat bentuk dua dan tiga bab. Tanpa
                # keduanya sel ini hijau bukan karena tidak berakibat.
                "jangkar label berlaku untuk dua bab",
                "      bab.length > 2 && i === 0",
                "      bab.length > 1 && i === 0",
                "petaRasi",
            ),
            (
                "skala bintang peta",
                "jariBintang(magStatus(m), 0.9)",
                "jariBintang(magStatus(m), 1)",
                "petaRasi",
            ),
            (
                # Garis terang menandai "dua materi ini SAMA-SAMA sudah
                # dibaca". Dengan ATAU, separuh langit menyala untuk jalur yang
                # baru setengah ditempuh.
                "garis terang jadi ATAU",
                'terang: kiri.status === "selesai" && m.status === "selesai",',
                'terang: kiri.status === "selesai" || m.status === "selesai",',
                "petaRasi",
            ),
            (
                # Benih bentuk rasi menggabungkan kunci dan judul bab dengan
                # pemisah. Tanpa pemisah, "python" + "Bab" bisa bertabrakan
                # dengan "pytho" + "nBab" -- dan dua bab berbeda mendapat
                # bentuk yang sama.
                "benih bentuk rasi tanpa pemisah",
                'data.key + "\u00b7" + b.judul,',
                "data.key + b.judul,",
                "petaRasi",
            ),
        ]),
    "banding-bahasa.mjs": (
        "banding-bahasa.mjs", PAKET_WEB,
        sumber_web("layar/bahasa-teks.ts"), [
            (
                # `>= 100` jadi `> 100`: kurikulum yang tepat tuntas menyapa
                # dengan "Sudah 100% jalan. Lanjutkan dari tempat kamu
                # berhenti." -- padahal tidak ada lagi yang bisa dilanjutkan.
                "ambang tuntas jadi eksklusif",
                "if (s.persen >= 100) {",
                "if (s.persen > 100) {",
                "kalimatBahasa",
            ),
            (
                # `<= 0` jadi `< 0`: kurikulum yang belum disentuh menyapa
                # dengan "Sudah 0% jalan".
                "ambang belum mulai jadi eksklusif",
                "if (s.persen <= 0) {",
                "if (s.persen < 0) {",
                "kalimatBahasa",
            ),
            (
                # Tombol paling terang di halaman berujung di layar penolakan.
                "materi terkunci ikut ditawarkan",
                'b.materi.find((m) => m.status !== "selesai" && !m.terkunci)',
                'b.materi.find((m) => m.status !== "selesai")',
                "pilihLanjut",
            ),
            (
                # Urutan belajarnya terbalik: orang yang berhenti di tengah
                # kalimat diantar ke kuis, dan orang yang baru menuntaskan satu
                # blok diantar membaca blok berikutnya.
                "syarat berhenti-di-tengah dibalik",
                'materi.status !== "sebagian")',
                'materi.status === "sebagian")',
                "pilihLanjut",
            ),
            (
                "kuis jatuh tempo tidak diprioritaskan",
                "b.kuis.find((q) => q.jatuh_tempo || (!q.pernah && q.siap))",
                "b.kuis.find((q) => !q.pernah && q.siap)",
                "pilihLanjut",
            ),
            (
                # Butir keempat berhenti ditandai `.fakta-kurang`, jadi kabar
                # "toolchain belum terpasang" tampil setenang tiga angka di
                # sebelahnya.
                "penanda toolchain kurang dilepas",
                "kurang: !siap,",
                "kurang: false,",
                "faktaBahasa",
            ),
            (
                "kuis hanya ditawarkan kalau ada latihan",
                '  if (kuis) {\n    return {\n      tipe: "kuis",',
                '  if (latihan && !kuis) {\n    return {\n      tipe: "kuis",',
                "pilihLanjut",
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
