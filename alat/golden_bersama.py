"""Rekam keluaran `sorot`, `galat`, dan `beda` atas SELURUH kode kurikulum.

Kenapa ada. Ketiga algoritma ini hari ini hidup DUA KALI: versi Python di
`inti/` dipakai server, versi JavaScript di `webapp/statik/js/` dipakai editor.
Yang menjaga keduanya tidak menyimpang adalah tes diferensial di
`tests/test_web.py` -- ia menjalankan keduanya atas korpus yang sama lalu
mengadu hasilnya.

Begitu keduanya digabung jadi satu implementasi TypeScript, tes diferensial itu
kehilangan lawan tandingnya dan ikut mati. Yang hilang bukan sekadar sebuah
tes: tidak ada lagi yang memberi tahu kalau penyorotan berubah. Perubahan
semacam itu tidak menimbulkan error di mana pun -- warna sebuah kata kunci
bergeser, dan tidak ada yang menyadarinya sampai berbulan-bulan kemudian.

Golden hash menggantikan perannya. Ia tidak membandingkan dua implementasi,
melainkan membandingkan keluaran HARI INI dengan keluaran yang sudah
disepakati. Rekamannya dibuat SEBELUM versi TypeScript ada, dan versi
TypeScript itu nanti wajib mereproduksi angka yang sama.

Yang direkam sidiknya, bukan keluarannya: korpusnya 1.300-an blok kode, dan
menyimpan tokennya utuh berarti berkas puluhan MB yang tidak pernah dibaca
siapa pun.

    python3 alat/golden_bersama.py            # hitung dan bandingkan
    python3 alat/golden_bersama.py --tulis    # tulis packages/bersama/golden/
"""

import argparse
import collections
import hashlib
import json
import os
import sys

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, AKAR)

from inti import beda, galat, sorot  # noqa: E402
from inti.kurikulum import LANGUAGES  # noqa: E402
from webapp import isi  # noqa: E402

TUJUAN = os.path.join(AKAR, "packages", "bersama", "golden")


def _sha(nilai):
    """SHA-256 atas bentuk JSON yang bisa DIREPRODUKSI di luar Python.

    `separators=(",", ":")` bukan penghematan tempat. Bawaan `json.dumps`
    memakai `", "` dan `": "` dengan spasi, sedangkan `JSON.stringify` di
    JavaScript tidak pernah memakai spasi -- jadi sidik yang sama-sama benar
    akan selalu berbeda di kedua sisi. Gejalanya bukan "ada yang salah di
    algoritmanya" melainkan tiga ribu sidik yang tidak satu pun cocok, yang
    terbaca seperti port yang gagal total dan menghabiskan sehari untuk
    ditelusuri.

    `sort_keys` tetap dipasang untuk kasus `golden_beda`, yang menyidik sebuah
    dict. `JSON.stringify` TIDAK mengurutkan kunci, jadi sisi TS yang nanti
    mereproduksi sidik itu wajib mengurutkannya sendiri; untuk `sorot` dan
    `galat` yang disidik cuma daftar dan string, jadi di sana `JSON.stringify`
    polos sudah cukup.
    """
    teks = json.dumps(nilai, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))
    return hashlib.sha256(teks.encode("utf-8")).hexdigest()


def korpus():
    """Setiap blok kode di kurikulum, beserta bahasa penyorotnya.

    Bahasanya WAJIB datang dari `isi.bahasa_blok` dan `isi.bahasa_sorot`, bukan
    dari `lang["runner"]` mentah. Versi pertama alat ini memakai yang mentah,
    dan akibatnya 408 dari 3.315 kasus direkam untuk bahasa yang aplikasinya
    tidak pernah pakai: `"terminal"` disorot sebagai bash, `"jsx"` sebagai
    javascript, `"postgresql"` sebagai sql (seluruh tabelnya di
    `berkas.sorot_untuk`). Tiga ratus empat puluh empat di antaranya
    menghasilkan token yang BERBEDA, jadi sidiknya membekukan jalur mati --
    pagar yang tidak pernah bisa memerah untuk perubahan yang nyata, dan
    memerah untuk perubahan yang tidak pernah terlihat pelajar.
    """
    keluar = []
    for lang in LANGUAGES:
        for m in lang["materials"]:
            for i, s in enumerate(m["sections"]):
                if s.get("code"):
                    _runner, bhs = isi.bahasa_blok(s, lang)
                    keluar.append((f"{lang['key']}/materi/{m['title']}/{i}",
                                   bhs, s["code"]))
        bhs_latihan = isi.bahasa_sorot(lang)
        for x in lang["exercises"]:
            if x.get("solution"):
                keluar.append((f"{lang['key']}/latihan/{x['title']}",
                               bhs_latihan, x["solution"]))
    return keluar


def golden_sorot(blok):
    """Sidik token per blok. Gabungan teks token WAJIB sama dengan sumbernya."""
    kasus, cacat = [], []
    for nama, bhs, kode in blok:
        token = [[j, t] for j, t in sorot.token(kode, bhs)]
        if "".join(t for _, t in token) != kode:
            cacat.append(nama)
        kasus.append({"nama": nama, "bahasa": bhs, "sha256": _sha(token)})
    return kasus, cacat


# Pesan compiler yang diterjemahkan `galat.terjemahkan`. Sengaja ditulis
# tangan: yang diuji adalah penerjemahnya, dan korpus pesan error sungguhan
# tidak ada di repo. Tiap entri berbentuk seperti yang keluar di mesin ini.
PESAN = [
    ("python", 'File "/tmp/x/program.py", line 3\n    print("a"\n         ^\nSyntaxError: \'(\' was never closed'),
    ("python", 'Traceback (most recent call last):\n  File "/tmp/x/program.py", line 2, in <module>\n    print(x)\nNameError: name \'x\' is not defined'),
    ("python", 'Traceback (most recent call last):\n  File "/tmp/x/program.py", line 1, in <module>\n    1/0\nZeroDivisionError: division by zero'),
    ("java", "/tmp/x/Main.java:4: error: ';' expected\n        int a = 1\n                 ^\n1 error"),
    ("java", "Exception in thread \"main\" java.lang.NullPointerException\n\tat Main.main(Main.java:5)"),
    ("c", "/tmp/x/program.c:3:5: error: 'y' undeclared (first use in this function)\n    3 |     y = 1;\n      |     ^"),
    ("javascript", "/tmp/x/program.js:2\nconsole.log(x)\n            ^\n\nReferenceError: x is not defined\n    at Object.<anonymous> (/tmp/x/program.js:2:13)"),
    ("go", "./program.go:5:2: declared and not used: x"),
    ("rust", "error[E0425]: cannot find value `x` in this scope\n --> program.rs:2:20"),
]


# Satu pesan per pola yang TIDAK tersentuh `PESAN` di atas. Diukur, bukan
# dikira: dari 71 pola, sembilan pesan sungguhan cuma menjalani 7. Enam puluh
# empat sisanya tidak pernah dieksekusi sama sekali -- dan justru di situ beda
# regex Python-JavaScript bisa bersembunyi, karena satu pola yang tidak pernah
# cocok di sisi TS tidak menimbulkan error: pesan errornya cuma kembali tampil
# mentah kepada orang yang paling tidak bisa membacanya.
#
# Bentuknya ditulis mendekati keluaran aslinya, bukan cuma potongan yang
# kebetulan cocok, supaya pola yang terlalu longgar ikut ketahuan.
PROBE = [
    ("java", "Main.java:4: error: cannot find symbol\n  symbol:   variable jumlah\n  location: class Main"),
    ("java", "Main.java:4: error: cannot find symbol\n  symbol:   method hitung(int)\n  location: class Main"),
    ("java", "error: cannot find symbol"),
    ("java", "Main.java:5: error: incompatible types: String cannot be converted to int"),
    ("java", "Main.java:1: error: class Halo is public, should be declared in a file named Halo.java"),
    ("java", "Main.java:8: error: missing return statement"),
    ("java", "Main.java:9: error: unreachable statement"),
    ("java", "Main.java:12: error: reached end of file while parsing"),
    ("java", 'Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 3'),
    ("java", 'Exception in thread "main" java.lang.NumberFormatException: For input string: "abc"'),
    ("java", 'Exception in thread "main" java.lang.ArithmeticException: / by zero'),
    ("java", 'Exception in thread "main" java.util.NoSuchElementException'),
    ("python", '  File "program.py", line 3\n    print(x)\nIndentationError: unexpected indent'),
    ("python", '  File "program.py", line 4\nTabError: inconsistent use of tabs and spaces in indentation'),
    ("python", '  File "program.py", line 2\nSyntaxError: unmatched \')\''),
    ("python", '  File "program.py", line 1\nSyntaxError: expected \':\''),
    ("python", "SyntaxError: invalid syntax. Perhaps you forgot a comma?"),
    ("python", "SyntaxError: cannot assign to literal here."),
    ("python", '  File "program.py", line 1\nSyntaxError: invalid syntax'),
    ("python", "TypeError: 'int' object is not subscriptable"),
    ("python", "TypeError: 'str' object is not callable"),
    ("python", "TypeError: f() takes 2 positional arguments but 3 were given"),
    ("python", "SyntaxError: unterminated string literal (detected at line 1)"),
    ("python", "TypeError: unsupported operand type(s) for +: 'int' and 'str'"),
    ("python", 'TypeError: can only concatenate str (not "int") to str'),
    ("python", "ValueError: invalid literal for int() with base 10: 'abc'"),
    ("python", "IndexError: list index out of range"),
    ("python", "EOFError: EOF when reading a line"),
    ("python", "AttributeError: 'list' object has no attribute 'push'"),
    ("python", "ModuleNotFoundError: No module named 'requests'"),
    ("python", "KeyError: 'nama'"),
    ("c", "program.c:4:5: error: expected ';' before '}' token"),
    ("c", "/usr/bin/ld: undefined reference to `main'"),
    ("c", "/usr/bin/ld: program.c:5: undefined reference to `hitung'"),
    ("c", "program.c:3:5: warning: implicit declaration of function 'printf'"),
    ("c", "program.c:5:12: warning: format '%d' expects argument of type 'int', but argument 2 has type 'double'"),
    ("c", "program.c:10:1: error: expected '}' at end of input"),
    ("c", "Segmentation fault (core dumped)"),
    ("javascript", "TypeError: daftar.push is not a function"),
    ("javascript", "TypeError: Cannot read properties of undefined (reading 'nama')"),
    ("javascript", "SyntaxError: Unexpected token ')'"),
    ("javascript", "TypeError: Assignment to constant variable."),
    ("go", './program.go:4:2: "fmt" imported and not used'),
    ("go", "./program.go:6:2: x declared and not used"),
    ("go", "./program.go:7:9: undefined: hitung"),
    ("go", "./program.go:3:1: expected declaration"),
    ("go", "./program.go:8:10: invalid operation: a + b (mismatched types int and string)"),
    ("go", "panic: runtime error: index out of range [5] with length 3"),
    ("bash", "program.sh: line 10: unexpected EOF while looking for matching `\"'"),
    ("bash", "program.sh: line 4: syntax error near unexpected token `('"),
    ("bash", "program.sh: line 3: nama: command not found"),
    ("bash", "bash: kompilasi: command not found"),
    ("bash", "program.sh: line 7: [: abc: integer expression expected"),
    ("sql", 'Error: near "AUTO_INCREMENT": syntax error'),
    ("sql", "Error: no such table: siswa"),
    ("sql", "Error: no such column: nilai"),
    ("sql", "Error: UNIQUE constraint failed: siswa.id"),
    ("html", "halaman.html:3: <div> dibuka tapi tidak pernah ditutup"),
    ("html", "halaman.html:7: </span> menutup sesuatu yang tidak pernah dibuka"),
    ("html", "halaman.html:2: </br> tidak diperlukan"),
    ("css", "gaya.css:4: pemilih 'p' tidak diikuti '{'"),
    ("css", "gaya.css:9: blok dibuka dengan '{' tapi tidak pernah ditutup"),
    ("css", "gaya.css:5: 'warna merah' bukan deklarasi yang sah"),
    ("css", "gaya.css:1: blok '{ … }' tanpa pemilih"),
    # Dua di bawah bukan untuk polanya, melainkan untuk `rapikan` dan
    # `ringkas`. Baterai mutasi di `packages/bersama/uji/gigi-golden.py`
    # menemukan keduanya tidak terjaga sama sekali: melepas bendera `g` dari
    # pola jalur dan menggeser deteksi Traceback tidak memerahkan apa pun,
    # karena tidak satu pun pesan di atas menyebut jalur sementara DUA KALI
    # atau memuat kata Traceback di luar tiga baris pertama.
    ("c", "/tmp/belajar-ab12cd/program.c:3:5: error: 'y' undeclared\n"
          "/tmp/belajar-ab12cd/program.c:4:9: note: each undeclared "
          "identifier is reported only once"),
    ("python", "============ test session starts ============\n"
               "collected 1 item\n\n"
               "tes_hitung.py F                        [100%]\n\n"
               "================= FAILURES =================\n"
               "_______________ test_jumlah ________________\n"
               "Traceback (most recent call last):\n"
               '  File "tes_hitung.py", line 4, in test_jumlah\n'
               "    assert jumlah(2, 2) == 5\n"
               "AssertionError: assert 4 == 5\n"
               "========== short test summary info =========\n"
               "FAILED tes_hitung.py::test_jumlah\n"
               "FAILED tes_hitung.py::test_kurang\n"
               "FAILED tes_hitung.py::test_kali\n"
               "============= 3 failed in 0.03s ============"),
]


def cakupan_galat(pesan):
    """Indeks pola yang benar-benar dijalani korpus ini.

    Dicatat ke rekaman supaya celahnya KELIHATAN. Pola yang tidak pernah
    tersentuh bukan pola yang aman -- ia pola yang belum diuji, dan rekaman
    yang tidak menyebutkan jumlahnya membuat orang mengira sebaliknya.
    """
    kena = set()
    for _bhs, teks in pesan:
        for i, (pola, _p) in enumerate(galat._TERKOMPILASI):
            if pola.search(teks):
                kena.add(i)
    return {
        "pola": len(galat.POLA),
        "tersentuh": len(kena),
        "tidak_tersentuh": sorted(set(range(len(galat.POLA))) - kena),
    }


def golden_galat():
    # Masukannya ditulis APA ADANYA, bukan cuma sidiknya. Versi pertama cuma
    # menyimpan sidik, dan akibatnya rekaman ini tidak bisa dipakai siapa pun
    # di luar Python: sisi TS tidak punya cara menurunkan pesan compiler dari
    # SHA-256-nya, jadi ia harus menyalin daftarnya -- dan salinan kedua yang
    # menyimpang membuat kedua sisi menguji dua korpus berbeda sambil
    # sama-sama hijau. Sidiknya tetap ditulis sebagai pagar atas masukannya
    # sendiri.
    kasus = []
    for bhs, pesan in list(PESAN) + PROBE:
        kasus.append({
            "bahasa": bhs,
            "masukan": pesan,
            "masukan_sha256": _sha(pesan),
            "terjemahan_sha256": _sha(galat.terjemahkan(pesan)),
            "ringkas_sha256": _sha(galat.ringkas(pesan)),
            "rapikan_sha256": _sha(galat.rapikan(pesan, "program")),
        })
    return kasus


# Pasangan (harapan, aktual) yang mewakili bentuk kegagalan nyata: beda satu
# huruf, beda spasi di ujung, baris hilang, baris tertukar, beda angka.
PASANGAN = [
    ("Halo, Dunia!", "Halo, dunia!"),
    ("12\n7\n", "12\n8\n"),
    ("a\nb\nc\n", "a\nc\n"),
    ("a\nb\nc\n", "a\nc\nb\n"),
    ("total: 1.500", "total: 1500"),
    ("baris  berkolom   rapi", "baris berkolom rapi"),
    ("selesai", "selesai "),
    ("", "ada isinya"),
    ("ada isinya", ""),
    # Tiga di bawah menutup cabang diagnosis yang tidak pernah terpicu korpus
    # hasilan. Bentuknya tidak realistis, dan memang bukan itu gunanya:
    # `uji/gigi-golden.py` menemukan bahwa mencabut sebuah awalan dari
    # `_AWALAN_NYARIS` tidak memerahkan apa pun, karena tidak satu pun dari
    # 309 pasangan menghasilkan kalimat itu. Cabang yang tidak pernah dijalani
    # adalah cabang yang bebas menyimpang saat diport.
    ("Halo.", "Halo"),                 # -> "Hanya beda TANDA BACA"
    ("Selesai.", "selesai"),           # -> beda kapital + tanda baca
    ("nilai  akhir", "Nilai Akhir"),   # -> beda spasi + kapital
]


def pasangan_hasilan(jumlah=300):
    """Pasangan keluaran yang DIHASILKAN, untuk menguji penyejajar barisnya.

    Sembilan pasangan di `PASANGAN` ditulis tangan untuk heuristik
    DIAGNOSISNYA, dan tidak satu pun darinya memicu rekursi
    `SequenceMatcher`: semuanya satu blok beda di satu tempat. Padahal justru
    penyejajar itu bagian yang paling mungkin menyimpang saat diport, karena
    ia bukan Myers diff dan pemenang-seri-blok-terpanjangnya halus.

    Jadi di sini keluaran berbilah banyak dirusak dengan cara-cara yang
    memaksa rekursinya: baris disisipkan, dibuang, ditukar tempat, dan
    diduplikasi. Duplikasi yang paling tajam -- baris yang sama muncul
    beberapa kali membuat beberapa blok cocok berukuran sama, dan di situlah
    dua implementasi bisa memilih yang berbeda tanpa salah satunya salah.

    SEED-nya bagian dari rekaman. Mengubahnya berarti mengganti seluruh
    korpus, dan rekaman yang korpusnya berubah tidak membuktikan apa pun soal
    perubahan yang sedang diperiksa. Kalau korpusnya perlu diperluas, TAMBAH
    kasus di ujung; jangan sentuh seed-nya.
    """
    import random
    rng = random.Random(20261020)
    kata = ["total", "nama", "skor", "Budi", "Ani", "lulus", "gagal",
            "0", "1", "10", "3.0", "3", "-5", "OK", "selesai", ""]

    def baris_acak():
        n = rng.randint(1, 4)
        return " ".join(rng.choice(kata) for _ in range(n)).strip()

    keluar = []
    for _ in range(jumlah):
        n = rng.randint(1, 9)
        asal = [baris_acak() for _ in range(n)]
        # Baris duplikat disuntikkan dengan sengaja: tanpa itu hampir setiap
        # baris unik, dan blok cocok terpanjangnya selalu tunggal.
        if n >= 2 and rng.random() < 0.5:
            asal[rng.randrange(n)] = asal[rng.randrange(n)]
        rusak = list(asal)
        for _ in range(rng.randint(1, 3)):
            aksi = rng.choice(("sisip", "buang", "ubah", "tukar"))
            if aksi == "sisip":
                rusak.insert(rng.randint(0, len(rusak)), baris_acak())
            elif aksi == "buang" and rusak:
                rusak.pop(rng.randrange(len(rusak)))
            elif aksi == "ubah" and rusak:
                rusak[rng.randrange(len(rusak))] = baris_acak()
            elif aksi == "tukar" and len(rusak) >= 2:
                i, j = rng.randrange(len(rusak)), rng.randrange(len(rusak))
                rusak[i], rusak[j] = rusak[j], rusak[i]
        keluar.append(("\n".join(asal), "\n".join(rusak)))
    return keluar


def golden_beda():
    kasus = []
    for harap, aktual in list(PASANGAN) + pasangan_hasilan():
        hasil = beda.bandingkan(harap, aktual)
        # `Beda` objek biasa tanpa __dict__, jadi medannya diambil eksplisit.
        # Menyebutnya satu per satu juga membuat medan BARU yang ditambahkan
        # nanti tidak diam-diam lolos dari rekaman ini.
        bentuk = {m: getattr(hasil, m) for m in
                  ("sama", "nomor_beda", "kolom_beda", "catatan",
                   "harapan", "aktual")}
        bentuk["baris"] = [list(b) if isinstance(b, tuple) else b
                           for b in (hasil.baris or [])]
        kasus.append({
            # Apa adanya, dengan alasan yang sama seperti di `golden_galat`.
            "harap": harap,
            "aktual": aktual,
            "harap_sha256": _sha(harap),
            "aktual_sha256": _sha(aktual),
            "bandingkan_sha256": _sha(bentuk),
            "nyaris": beda.nyaris(hasil),
            "kolom_pertama_beda": beda.kolom_pertama_beda(harap, aktual),
        })
    return kasus


def cakupan(blok):
    """Berapa blok yang benar-benar tersorot, dan bahasa apa yang tidak.

    Ini yang membuat rekaman di bawah bisa menyebut PENYEBAB, bukan cuma
    melaporkan sidik yang bergeser. Sebuah pemetaan yang hilang di
    `berkas.sorot_untuk` menggeser ratusan sidik sekaligus, dan daftar sidik
    tidak memberi tahu apa pun soal mana yang hilang -- sedangkan satu nama
    bahasa yang pindah dari "tersorot" ke "polos" langsung menunjuknya.
    """
    # `sorot.ATURAN`, bukan `sorot.bahasa_didukung()`. Yang kedua membuang
    # duplikat berdasarkan `id()`, jadi ia menjawab "ada berapa SET aturan
    # yang berbeda" -- bukan "nama apa saja yang dikenali". Memakainya di sini
    # menggolongkan setiap alias sebagai tidak tersorot, dan `aplikasi` (68
    # blok, alias Java) langsung muncul di puncak daftar sebagai bukti.
    punya = set(sorot.ATURAN)
    polos = collections.Counter(b[1] for b in blok if b[1] not in punya)
    return {
        "tersorot": sum(1 for b in blok if b[1] in punya),
        "polos": sum(polos.values()),
        # Bahasa tanpa aturan penyorotan. Angkanya ikut dicatat supaya
        # menambah aturan baru untuk salah satunya terlihat sebagai
        # perbaikan yang terukur, bukan sebagai "golden bergeser".
        "bahasa_polos": dict(sorted(polos.items())),
    }


def susun():
    blok = korpus()
    kasus_sorot, cacat = golden_sorot(blok)
    if cacat:
        raise ValueError("token tidak merekonstruksi sumbernya: "
                         + ", ".join(cacat[:3]))
    return {
        "sorot.json": {
            "fungsi": "sorot.token(kode, bahasa) -> [[jenis, teks]]",
            "catatan": "Gabungan teks token WAJIB sama persis dengan kodenya.",
            "bahasa_didukung": sorot.bahasa_didukung(),
            "cakupan": cakupan(blok),
            "kasus": kasus_sorot,
        },
        "galat.json": {
            "fungsi": "galat.terjemahkan(pesan), ringkas(pesan), rapikan(pesan, nama)",
            "cakupan": cakupan_galat(list(PESAN) + PROBE),
            "kasus": golden_galat(),
        },
        "beda.json": {
            "fungsi": "beda.bandingkan(harap, aktual), nyaris, kolom_pertama_beda",
            "kasus": golden_beda(),
        },
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--tulis", action="store_true")
    a = ap.parse_args()

    berkas = susun()
    n = len(berkas["sorot.json"]["kasus"])
    print(f"sorot: {n} blok kode di {len(LANGUAGES)} kurikulum")
    print(f"galat: {len(berkas['galat.json']['kasus'])} pesan compiler")
    print(f"beda : {len(berkas['beda.json']['kasus'])} pasangan keluaran")

    lama = {}
    for nama in berkas:
        jalur = os.path.join(TUJUAN, nama)
        if os.path.exists(jalur):
            with open(jalur, encoding="utf-8") as f:
                lama[nama] = json.load(f)
    # `isi` sengaja TIDAK dipakai sebagai nama di sini: modul `webapp.isi`
    # sudah memakai nama itu di berkas ini, dan loop yang menimpanya pernah
    # jadi bug yang cuma muncul kalau cabangnya diambil.
    if lama:
        geser = [n for n, rekaman in lama.items() if rekaman != berkas[n]]
        if geser:
            print("BERGESER dari rekaman sebelumnya:", ", ".join(geser))
            if not a.tulis:
                # Menolak di sini TANPA --tulis saja. Versi sebelumnya menolak
                # keduanya sekaligus sambil mencetak "kalau ini disengaja,
                # tulis ulang" -- saran yang mustahil diikuti, karena jalurnya
                # sendiri yang ditutup. Pagar yang tidak bisa dilewati dengan
                # sengaja bukan pagar; ia cuma alat yang rusak.
                print("  Kalau ini disengaja, jalankan ulang dengan --tulis. "
                      "Kalau tidak, cari perubahan yang menyebabkannya "
                      "SEBELUM menerimanya.")
                return 1
            print("  --tulis diberikan: rekaman DIGANTI dengan yang sekarang.")
        else:
            print("cocok dengan rekaman sebelumnya")

    if a.tulis:
        os.makedirs(TUJUAN, exist_ok=True)
        for nama, isi in berkas.items():
            with open(os.path.join(TUJUAN, nama), "w", encoding="utf-8") as f:
                json.dump(isi, f, ensure_ascii=False, indent=1)
                f.write("\n")
        print(f"  ditulis {len(berkas)} berkas ke packages/bersama/golden/")
    else:
        print("  (belum ditulis; tambahkan --tulis)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
