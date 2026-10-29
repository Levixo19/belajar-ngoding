"""Pagar `packages/konten/`: JSON wajib tetap sama dengan sumber Python.

Ekspornya sekali jalan; yang mahal justru sesudahnya. Begitu ada dua salinan
konten, keduanya bisa menyimpang tanpa satu pun error muncul: seseorang
menyunting `data/python_materials.py`, lupa mengekspor ulang, dan sisi JSON
diam-diam menyajikan materi versi lama. Tes ini menutup celah itu dengan
membandingkan keduanya setiap kali suite jalan.

Tiga hal yang dijaga, masing-masing karena pernah bisa lolos:

* Kuis disimpan MENTAH. Kalau suatu hari yang tersimpan hasil rotasi, rotasi
  kedua saat pemuatan tidak akan menimbulkan error apa pun -- opsi cuma
  bergeser, dan penjelasan soal yang menyebut posisi opsi berhenti cocok.
  Sidik SHA-256 pasca-rotasi menangkapnya.
* Kunci berbentuk angka dilarang. `JSON.parse` di V8 menata ulang kunci
  seperti "0" dan "1" ke depan, jadi objek yang memakainya tidak pulih sama
  di sisi JavaScript. Hari ini tidak ada satu pun; tes ini menjaga besok.
* Nol kurikulum = lolos palsu. Populasinya ditagih eksplisit.
"""

import hashlib
import glob
import json
import os
import unittest

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KONTEN = os.path.join(AKAR, "packages", "konten")

from data.bab import BAB  # noqa: E402
from data.kuis_materi import KUIS_MATERI  # noqa: E402
from data.normalisasi import seimbangkan_kuis  # noqa: E402
from inti import visual  # noqa: E402
from inti.kurikulum import LANGUAGES  # noqa: E402


def _muat(*bagian):
    with open(os.path.join(KONTEN, *bagian), encoding="utf-8") as f:
        return json.load(f)


@unittest.skipUnless(os.path.isdir(KONTEN), "packages/konten belum diekspor")
class TestKontenJsonSamaDenganPython(unittest.TestCase):

    def test_populasinya_tidak_kosong(self):
        """Tanpa ini, ekspor yang gagal total akan membuat semua tes di bawah
        lulus karena tidak membandingkan apa pun."""
        berkas = os.listdir(os.path.join(KONTEN, "kurikulum"))
        self.assertEqual(len(berkas), len(LANGUAGES))
        self.assertGreaterEqual(len(LANGUAGES), 32)

    def test_tiap_kurikulum_identik(self):
        for lang in LANGUAGES:
            with self.subTest(kurikulum=lang["key"]):
                d = _muat("kurikulum", f"{lang['key']}.json")
                self.assertEqual(d["materi"], lang["materials"])
                self.assertEqual(d["latihan"], lang["exercises"])
                self.assertEqual(d["label"], lang["label"])
                self.assertEqual(d["runner"], lang["runner"])

    def test_kuis_tersimpan_mentah_dan_memutar_jadi_yang_dipakai(self):
        for lang in LANGUAGES:
            with self.subTest(kurikulum=lang["key"]):
                mentah = _muat("kurikulum", f"{lang['key']}.json")["kuis_mentah"]
                self.assertEqual(seimbangkan_kuis(mentah), lang["quizzes"])

    def test_sidik_kuis_pasca_rotasi_tidak_bergeser(self):
        sidik = _muat("sidik.json")["kuis_pasca_rotasi"]
        self.assertEqual(sorted(sidik), sorted(l["key"] for l in LANGUAGES))
        for lang in LANGUAGES:
            with self.subTest(kurikulum=lang["key"]):
                teks = json.dumps(lang["quizzes"], ensure_ascii=False,
                                  sort_keys=True)
                nyata = hashlib.sha256(teks.encode("utf-8")).hexdigest()
                self.assertEqual(
                    nyata, sidik[lang["key"]],
                    "rotasi opsi kuis bergeser; ekspor ulang dan PERIKSA "
                    "penjelasan soal yang menyebut posisi opsi")

    def test_bab_kuis_materi_dan_gambar_identik(self):
        self.assertEqual(_muat("bab.json"), BAB)
        self.assertEqual(_muat("kuis_materi.json"), KUIS_MATERI)
        dicek = 0
        for lang in LANGUAGES:
            jalur = os.path.join(KONTEN, "visual", f"{lang['key']}.json")
            if not os.path.exists(jalur):
                continue
            with self.subTest(kurikulum=lang["key"]):
                self.assertEqual(_muat("visual", f"{lang['key']}.json"),
                                 visual.data_bahasa(lang["key"]))
            dicek += 1
        self.assertGreater(dicek, 0, "tidak ada berkas gambar yang dibandingkan")

    def test_tidak_ada_kunci_angka(self):
        """V8 menata ulang kunci berbentuk indeks saat JSON.parse."""
        temuan = []

        def sisir(obj, jalur):
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if str(k).isdigit():
                        temuan.append(f"{jalur}/{k}")
                    sisir(v, f"{jalur}/{k}")
            elif isinstance(obj, list):
                for v in obj:
                    sisir(v, jalur)

        for dasar, _anak, berkas in os.walk(KONTEN):
            for nama in berkas:
                if nama.endswith(".json"):
                    penuh = os.path.join(dasar, nama)
                    with open(penuh, encoding="utf-8") as f:
                        sisir(json.load(f), os.path.relpath(penuh, KONTEN))
        self.assertEqual(temuan[:10], [])


GOLDEN = os.path.join(AKAR, "packages", "bersama", "golden")


@unittest.skipUnless(os.path.isdir(GOLDEN), "packages/bersama/golden belum dibuat")
class TestGoldenBersama(unittest.TestCase):
    """Keluaran `sorot`, `galat`, dan `beda` tidak boleh bergeser diam-diam.

    Hari ini ketiganya punya kembaran JavaScript, dan yang menjaga keduanya
    sejalan adalah tes diferensial di `test_web.py`. Begitu keduanya digabung
    jadi satu implementasi TypeScript, tes itu kehilangan lawan tandingnya.
    Rekaman ini yang menggantikannya: ia tidak mengadu dua implementasi,
    melainkan mengadu keluaran hari ini dengan keluaran yang sudah disepakati.

    Rekamannya sengaja dibuat SEBELUM versi TypeScript ada, supaya versi itu
    nanti punya angka yang harus direproduksi -- bukan angka yang ia tetapkan
    sendiri sesudah terlanjur berbeda.
    """

    def test_tidak_bergeser_dari_rekaman(self):
        import sys
        sys.path.insert(0, os.path.join(AKAR, "alat"))
        import golden_bersama

        sekarang = golden_bersama.susun()
        self.assertGreater(len(sekarang["sorot.json"]["kasus"]), 3000,
                           "korpus penyorot menyusut; pagarnya jadi tumpul")
        for nama, isi in sekarang.items():
            with self.subTest(berkas=nama):
                with open(os.path.join(GOLDEN, nama), encoding="utf-8") as f:
                    self.assertEqual(
                        json.load(f), isi,
                        f"{nama} bergeser. Kalau disengaja, jalankan "
                        "`python3 alat/golden_bersama.py --tulis`; kalau "
                        "tidak, cari penyebabnya dulu")


BERSAMA = os.path.join(AKAR, "packages", "bersama")


# `--experimental-strip-types` DIBERIKAN eksplisit, dan ia bukan sisa dari masa
# lalu. Pelucutan tipe baru tanpa-flag sejak Node 23.6 (dan 22.18 di jalur LTS);
# di bawah itu SELURUH pembanding di bawah gagal dengan
# `ERR_UNKNOWN_FILE_EXTENSION` -- empat belas tes merah karena alasan yang tidak
# ada hubungannya dengan isinya, dan tes yang merah begitu adalah tes yang
# berhenti dibaca. Terukur: flagnya diterima apa adanya oleh 22.11 maupun 24.21,
# jadi memberikannya selalu lebih murah daripada mendeteksi versinya -- dan jauh
# lebih murah daripada melewatkan tesnya diam-diam.
def _ada_node():
    import shutil
    return shutil.which("node") is not None


@unittest.skipUnless(os.path.isdir(os.path.join(BERSAMA, "src")),
                     "packages/bersama belum ada")
@unittest.skipUnless(_ada_node(), "node tidak terpasang")
class TestAlgoritmaTypeScript(unittest.TestCase):
    """Port TS wajib menghasilkan keluaran identik dengan modul `inti/`.

    Ini penerus `test_web.TestPenyorotJavaScript` untuk implementasi yang
    menggantikan `sorot.js`. Bedanya cara membuktikan: yang lama menjalankan
    dua pemindai berdampingan, yang ini mengadu satu pemindai dengan rekaman
    yang dibuat SEBELUM ia ada. Tes diferensial tetap hijau kalau kedua sisi
    diubah bersamaan; rekaman tidak.

    Yang dijalankan skrip Node-nya sendiri, bukan versi Python dari
    perbandingan yang sama. Menuliskan ulang perbandingannya di sini berarti
    dua definisi "cocok", dan yang satu bisa melonggar tanpa yang lain tahu.

    Giginya diuji terpisah dengan `python3 packages/bersama/uji/gigi-golden.py`
    (delapan mutasi, tiap sel menagih kategori keluhannya). Itu TIDAK ikut di
    sini karena ia menulis ke berkas sumber, dan tes yang menyunting pohon
    kerjanya sendiri akan merusak jalannya suite kalau ia dibunuh di tengah.
    """

    # (skrip, pola cacah populasi, lantai). Lantainya, bukan angka persisnya:
    # mematok 3315 berarti menambah satu materi memerahkan tes ini tanpa ada
    # yang rusak, dan pagar yang memerah tanpa sebab adalah pagar yang orang
    # belajar mengabaikan.
    SKRIP = (
        ("golden-sorot.ts", r"korpus: (\d+) blok kode", 3000),
        ("golden-beda.ts", r"rekaman: (\d+) pasangan", 300),
        ("golden-galat.ts", r"rekaman: (\d+) pesan", 50),
    )

    # Pembanding di `packages/web`: geometri peta rasi diadu dengan `rasi.js`,
    # bukan dengan rekaman. Bisa begitu karena keduanya JavaScript dan
    # fungsinya murni -- tidak ada sisi Python yang perlu direkam.
    SKRIP_WEB = (("banding-ikon.mjs", r"(\d+) perbandingan", 100),
                 ("banding-rasi.mjs", r"(\d+) perbandingan", 400),
                 ("banding-editor.mjs", r"(\d+) blok kode", 3000),
                 ("banding-pratinjau.mjs", r"(\d+) blok kode", 3000),
                 ("banding-visual.mjs", r"(\d+) spesifikasi gambar", 1300),
                 ("banding-jejak.mjs", r"(\d+) blok kode", 2500),
                 ("banding-kerja.mjs", r"(\d+) solusi", 500),
                 ("banding-prosa.mjs", r"(\d+) baris prosa", 100000),
                 ("banding-belajar.mjs", r"(\d+) baris prosa", 100000),
                 ("banding-bahasa.mjs", r"(\d+) perbandingan", 1000),
                 ("banding-dasbor.mjs", r"(\d+) perbandingan", 2000),
                 ("banding-palet.mjs", r"(\d+) perbandingan", 10000),
                 ("banding-langit.mjs", r"(\d+) perbandingan", 30),
                 ("banding-sampul.mjs", r"(\d+) perbandingan", 700),
                 ("banding-gerak.mjs", r"(\d+) perbandingan", 150),
                 ("banding-lensa.mjs", r"(\d+) perbandingan", 100000),
                 ("banding-hero.mjs", r"(\d+) perbandingan", 1000),
                 ("banding-orbit.mjs", r"(\d+) perbandingan", 3000),
                 ("banding-skyline.mjs", r"(\d+) perbandingan", 8000),
                 ("banding-pohon.mjs", r"(\d+) perbandingan", 20000),
                 ("banding-tetes.mjs", r"(\d+) perbandingan", 150000),
                 ("banding-penutup.mjs", r"(\d+) perbandingan", 3000),
                 ("banding-dasbor-hidup.mjs", r"(\d+) perbandingan", 6000))

    def test_layanan_catatan(self):
        """Uji `packages/catatan` -- lapisan murninya selalu, Mongo kalau ada.

        Dijalankan dari suite ini supaya ia tidak jadi tes yang cuma diingat
        orang yang menulisnya. Lapisan MongoDB-nya MELEWATI diri sendiri kalau
        containernya tidak jalan, dan pesannya menyebut perintah untuk
        menyalakannya -- jadi "dilewati" di sini tidak pernah berarti "lulus
        diam-diam", dan suite tidak pernah merah cuma karena sebuah container
        sedang dimatikan.

        Paketnya juga dilewati kalau `node_modules`-nya belum ada: `express`
        dan `mongodb` adalah SATU-SATUNYA dependensi runtime di seluruh repo
        ini, dan aplikasi utamanya memang harus tetap jalan tanpa `npm
        install`.
        """
        import re
        import subprocess
        paket = os.path.join(AKAR, "packages", "catatan")
        if not os.path.isdir(paket):
            self.skipTest("packages/catatan tidak ada")
        if not os.path.isdir(os.path.join(AKAR, "node_modules", "mongodb")):
            self.skipTest("dependensi @belajar/catatan belum dipasang "
                          "(npm install --workspace @belajar/catatan)")
        hasil = subprocess.run(
            ["node", "--experimental-strip-types",
             os.path.join(paket, "uji", "uji-cari.ts")],
            cwd=paket, capture_output=True, text=True, timeout=300)
        keluaran = (hasil.stdout + hasil.stderr).strip()
        self.assertEqual(hasil.returncode, 0,
                         "uji layanan catatan gagal.\n" + keluaran[:4000])
        # Lantai populasi: lapisan murninya lima pemeriksaan dan ia TIDAK
        # pernah dilewati. Tanpa tagihan ini, berkas uji yang jadi kosong
        # tetap melapor kode keluar nol.
        cocok = re.search(r"(\d+) pemeriksaan lulus", keluaran)
        self.assertIsNotNone(cocok, f"keluaran tak terbaca:\n{keluaran[:800]}")
        # Lantainya 12: lima pemeriksaan lapisan murni plus tujuh penjagaan
        # HTTP, dan KEDUANYA tidak pernah dilewati -- ketiga penjagaan itu
        # menolak sebelum satu pun panggilan Mongo. Lantai 5 yang lama tetap
        # hijau untuk berkas uji yang kehilangan seluruh lapisan HTTP-nya.
        self.assertGreaterEqual(int(cocok.group(1)), 12, keluaran[:800])

    def test_setiap_pembanding_terdaftar_di_tiga_tempat(self):
        """Pembanding yang ditulis tapi tidak didaftarkan = pembanding yang mati.

        Ia kelas cacat yang sudah terjadi di repo ini dengan bentuk lain:
        `komponen/Tanda.tsx` selesai ditulis satu ronde penuh lebih awal dan
        tidak pernah disambung ke satu layar pun, jadi dua layar yang
        bergantung padanya mustahil terisi -- tanpa satu pun error yang
        menjelaskannya.

        Sebuah berkas `banding-*.mjs` punya TIGA pendaftaran, dan masing-masing
        membeli hal yang berbeda:

        * `SKRIP_WEB` di bawah -- ia ikut suite, jadi ia benar-benar dijalankan;
        * skrip `banding` di `packages/web/package.json` -- ia bisa dijalankan
          sekaligus tanpa menghafal dua belas nama;
        * `BATERAI` di `gigi-golden.py` -- ada bukti ia bisa MERAH.

        Yang paling mahal kalau terlupa yang ketiga: pembanding tanpa sel
        mutasi adalah pembanding yang hijaunya tidak berarti apa pun.
        """
        import json
        import re
        WEB = os.path.join(AKAR, "packages", "web")
        dir_uji = os.path.join(WEB, "uji")
        if not os.path.isdir(dir_uji):
            self.skipTest("packages/web/uji tidak ada")
        ada = {n for n in os.listdir(dir_uji)
               if n.startswith("banding-") and n.endswith(".mjs")}
        self.assertGreaterEqual(len(ada), 12, f"cuma {len(ada)} pembanding?")

        di_suite = {s for s, _p, _l in self.SKRIP_WEB}
        self.assertEqual(sorted(ada - di_suite), [],
                         "pembanding tidak ikut suite")

        with open(os.path.join(WEB, "package.json"), encoding="utf-8") as f:
            skrip = json.load(f)["scripts"].get("banding", "")
        # `[a-z-]`, bukan `[a-z]`: nama dua kata (`banding-dasbor-hidup.mjs`) tidak tertangkap
        # `[a-z]+`, dan pembanding yang sah dilaporkan "tidak ada di skrip npm".
        di_npm = set(re.findall(r"banding-[a-z-]+\.mjs", skrip))
        self.assertEqual(sorted(ada - di_npm), [],
                         "pembanding tidak ada di skrip npm `banding`")
        # Dan skripnya harus benar-benar BISA DIJALANKAN. Versi pertama
        # `banding` memanggil `node uji/banding-*.mjs` telanjang, dan karena
        # tiap pembanding mengimpor `.ts`, kedua belasnya mati dengan
        # ERR_UNKNOWN_FILE_EXTENSION di Node < 23.6 -- termasuk node 22.11 di
        # PATH mesin ini. Daftar yang lengkap tapi tidak bisa dijalankan
        # adalah daftar yang tidak pernah dijalankan siapa pun.
        #
        # Diperiksa untuk SELURUH paket, bukan cuma `web`: cacat yang sama
        # ternyata juga ada di skrip `golden` milik `packages/bersama`, satu
        # paket di sebelahnya, dan ia luput justru karena pagar pertama
        # menyebut satu skrip dengan namanya. Yang menular bukan skripnya
        # melainkan kebiasaan memanggil `node` begitu saja.
        tanpa_flag = []
        for pkg in sorted(glob.glob(os.path.join(AKAR, "packages", "*",
                                                 "package.json"))):
            with open(pkg, encoding="utf-8") as f:
                skrip_pkg = json.load(f).get("scripts") or {}
            paket = os.path.basename(os.path.dirname(pkg))
            for nama, perintah in skrip_pkg.items():
                if not re.search(r"\bnode\s+\S+\.(ts|mjs)", perintah):
                    continue
                if "--experimental-strip-types" not in perintah:
                    tanpa_flag.append(f"{paket}:{nama}")
        self.assertEqual(tanpa_flag, [],
                         "skrip npm memanggil node tanpa pelucut tipe -- "
                         "yang dijalankannya mengimpor `.ts`, jadi ia mati "
                         "dengan ERR_UNKNOWN_FILE_EXTENSION di Node < 23.6")

        # Tabel baterainya DIIMPOR, tidak di-grep. Versi pertama memakai
        # `re.findall` atas teks berkasnya, dan mutan yang membuktikannya
        # lemah: mengganti nama entri jadi `"banding-palet-X.mjs"` sekaligus
        # merusak pembandingnya jadi `"banding-palet.mjs-X"` TETAP lolos,
        # karena regexnya menemukan `banding-palet.mjs` di dalam string yang
        # sudah rusak itu. Nama di sebuah KOMENTAR pun akan memuaskannya.
        # Yang diimpor pendaftaran yang sungguhan dipakai.
        import importlib.util
        jalur_baterai = os.path.join(AKAR, "packages", "bersama", "uji",
                                     "gigi-golden.py")
        spek = importlib.util.spec_from_file_location("gigi_golden",
                                                      jalur_baterai)
        modul = importlib.util.module_from_spec(spek)
        spek.loader.exec_module(modul)
        di_baterai = {p for p, _akar, _sumber, _mutan in modul.BATERAI.values()}
        self.assertEqual(sorted(ada - di_baterai), [],
                         "pembanding tanpa satu pun sel mutasi -- hijaunya "
                         "tidak membuktikan apa pun")
        # Dan tiap entri wajib punya mutan: entri berdaftar KOSONG mendaftarkan
        # sebuah pembanding tanpa membuktikan apa pun tentangnya.
        kosong = sorted(label for label, (_p, _a, _s, mutan)
                        in modul.BATERAI.items() if not mutan)
        self.assertEqual(kosong, [], "entri baterai tanpa satu pun mutan")

    def test_kelas_css_react_ada_di_gaya_css(self):
        """Kelas yang dipakai React harus benar-benar ADA di `gaya.css`.

        Kelas karangan tidak menimbulkan error apa pun: elemennya tetap
        tergambar, `tsc` tetap hijau, dan yang hilang cuma gayanya. Sudah
        terjadi DUA kali, dan yang kedua merusak seluruh cangkang --
        `nav` diberi `className="pil-atas"`, nama yang dipakai KOMENTAR blok
        di `gaya.css`, bukan selektornya; selektornya `#rel`. Dua puluh lima
        aturan tidak pernah berlaku, dan navigasinya tampil sebagai teks
        telanjang berdempetan di pojok. Bersama `.rel-deret` dan `.rel-butir`
        yang juga karangan, sekitar lima puluh aturan diam.

        Yang diperiksa cuma kelas yang `gaya.css` memang PUNYA pendapat
        tentangnya. Kelas yang tidak muncul di sana belum tentu salah -- ia
        bisa penanda untuk JS atau untuk tes -- tapi kelas yang dipakai untuk
        MENATA dan tidak ada di stylesheet selalu salah, dan satu-satunya cara
        membedakannya adalah daftar putih yang ditulis sadar.
        """
        import re
        src = os.path.join(AKAR, "packages", "web", "src")
        css = os.path.join(AKAR, "webapp", "statik", "gaya.css")
        if not os.path.isdir(src) or not os.path.isfile(css):
            self.skipTest("sumber React atau gaya.css tidak ada")
        with open(css, encoding="utf-8") as f:
            teks_css = f.read()
        ada_di_css = set(re.findall(r"\.(-?[_a-zA-Z][\w-]*)", teks_css))

        # Penanda yang memang BUKAN urusan gaya. Tiap entri harus bisa
        # disebutkan alasannya; daftar yang tumbuh tanpa alasan adalah daftar
        # yang membatalkan pagarnya sendiri.
        DIKECUALIKAN = {
            "kini",            # keadaan, dipakai sebagai `a.kini`
            "buka", "tampak", "menyala", "mati",   # keadaan, dirangkai induk
        }

        # DAFTAR DASAR. Kelas di bawah dipakai React dan nol aturan di
        # `gaya.css`, dan masing-masing sudah DIPERIKSA: semuanya kait tanpa
        # gaya -- penanda untuk JS, untuk tes, atau sisa yang berdiri di
        # samping kelas yang memang bergaya (`bab-saring` dipakai bersama
        # `tbl` + `tbl-pilih`/`tbl-hantu`, dan ketiganya ada). Tata letaknya
        # terbukti benar di browser pada 1440 px.
        #
        # Daftar ini RATCHET: ia tidak boleh tumbuh. Kelas BARU yang tidak
        # punya aturan memerahkan tes ini, dan itu tujuannya -- `pil-atas`,
        # `rel-deret`, dan `rel-butir` lolos justru karena pagar ini belum
        # ada, dan ketiganya mematikan sekitar lima puluh aturan sekaligus.
        # Menambah entri di sini berarti menyatakan "sudah diperiksa, memang
        # bukan urusan gaya", bukan "biar hijau".
        DASAR = {
            "bab-judul", "bab-saring", "diff-kata", "keluaran-isi",
            "kr-lapis-garis", "medan-judul", "medan-ket", "mulai-pilih",
            "pratinjau-lebar", "tanda-angka", "tbl-pintu",
        }

        dipakai = {}
        for akar, _dir, berkas in os.walk(src):
            for n in sorted(berkas):
                if not n.endswith(".tsx"):
                    continue
                jalur = os.path.join(akar, n)
                with open(jalur, encoding="utf-8") as f:
                    isi = f.read()
                isi = re.sub(r"/\*.*?\*/", "", isi, flags=re.S)
                for m in re.finditer(r'className=(?:"([^"]*)"|\{"([^"]*)")', isi):
                    for k in (m.group(1) or m.group(2) or "").split():
                        # Potongan yang diakhiri `-` itu AWALAN rangkaian
                        # string (`"tk-" + jenis`), bukan kelas. Menghitungnya
                        # sebagai kelas memberi sebelas positif-palsu yang
                        # memaksa daftar dasar ini jadi tempat sampah.
                        if k.endswith("-"):
                            continue
                        if k and k not in DIKECUALIKAN and k not in DASAR:
                            dipakai.setdefault(k, os.path.relpath(jalur, src))

        karangan = sorted((k, v) for k, v in dipakai.items()
                          if k not in ada_di_css)
        self.assertGreaterEqual(
            len(dipakai), 60,
            f"cuma {len(dipakai)} kelas yang terbaca -- polanya yang salah")
        self.assertEqual(
            [f"{k} ({v})" for k, v in karangan], [],
            "kelas dipakai React tapi NOL aturan di gaya.css")

    def test_jalur_api_tanpa_awalan_ganda(self):
        """`ambil`/`kirim` menambahkan `/api/`, jadi jalurnya telanjang.

        Jalur yang sudah membawa awalannya menghasilkan `/api//api/...` -- 404
        yang HANYA browser bisa memberitahu, karena bagi `tsc` ia cuma sebuah
        string yang sah. Sudah terjadi dua kali: sekali di ronde port layar,
        sekali lagi di `BlokData`.

        Pagar di tingkat tipe sudah dicoba dan diukur TUMPUL -- dengan
        `<T, J extends string = string>`, pemanggil yang menulis
        `ambil<Hasil>(...)` membuat `J` jatuh ke bawaannya `string`, dan
        `string` tidak diawali `/` sehingga apa pun lolos. Jadi yang menjaga
        sapuan ini, plus pemeriksaan runtime di `api.ts`.
        """
        import re
        src = os.path.join(AKAR, "packages", "web", "src")
        if not os.path.isdir(src):
            self.skipTest("packages/web/src tidak ada")
        pola = re.compile(
            r"\b(?:api\.)?(?:ambil|kirim)\s*(?:<[^()]*?>)?\s*\(\s*"
            r"[\"'`]([^\"'`]+)")
        salah, diperiksa = [], 0
        for akar, _dir, berkas in os.walk(src):
            for n in sorted(berkas):
                if not n.endswith((".ts", ".tsx")):
                    continue
                jalur = os.path.join(akar, n)
                with open(jalur, encoding="utf-8") as f:
                    isi = f.read()
                for m in pola.finditer(isi):
                    diperiksa += 1
                    j = m.group(1)
                    if j.startswith("/") or j.startswith("api/"):
                        salah.append(f"{os.path.relpath(jalur, AKAR)}: {j!r}")
        # Lantai populasi: sapuan yang nol panggilan hijau tanpa arti.
        self.assertGreaterEqual(diperiksa, 20,
                                f"cuma {diperiksa} panggilan api yang terbaca "
                                "-- polanya yang salah, bukan sumbernya")
        self.assertEqual(salah, [],
                         "jalur api berawalan ganda: `ambil`/`kirim` sudah "
                         "menambahkan `/api/` sendiri")

    def test_layar_tidak_memanggil_isyarat_langsung(self):
        """`isyarat()` diekspor, tapi bukan untuk layar.

        Di antarmuka lama `inti.js` berdiri di tengah dan sengaja TIDAK
        meneruskan fungsi ini: layar yang bisa memanggilnya langsung adalah
        layar yang bisa mengarang bunyi barunya sendiri, dan pada saat itu
        "tiga tingkat" berhenti menggambarkan apa yang sebenarnya terdengar.
        Di React tidak ada perantara semacam itu, jadi kebijakannya dijaga di
        sini -- bukan oleh ketiadaan ekspornya, karena ekspornya DITUNTUT
        driver uji yang menagih permukaan modul ini sama dengan `suara.js`.

        Pintu yang sah dua: `mainkanContoh()` untuk peragaan di Pengaturan,
        dan `rasakanPerayaan()` yang menempel pada satu keputusan di
        `rayakan()`.
        """
        import re
        src = os.path.join(AKAR, "packages", "web", "src")
        if not os.path.isdir(src):
            self.skipTest("packages/web/src tidak ada")
        pola = re.compile(r"\bisyarat\s*\(")
        salah, diperiksa = [], 0
        for akar, _dir, berkas in os.walk(src):
            for n in sorted(berkas):
                if not n.endswith((".ts", ".tsx")):
                    continue
                jalur = os.path.join(akar, n)
                rel = os.path.relpath(jalur, src)
                with open(jalur, encoding="utf-8") as f:
                    isi = f.read()
                diperiksa += 1
                if rel == "suara.ts":
                    continue          # pemiliknya
                # Komentar dibuang lebih dulu: paragraf yang MENJELASKAN
                # kebijakan ini menyebut `isyarat()` beberapa kali, dan sapuan
                # yang menghitungnya memaksa penjelasannya dihapus supaya
                # pagarnya hijau -- persis kebalikan dari yang diinginkan.
                tanpa_komentar = re.sub(r"/\*.*?\*/", "", isi, flags=re.S)
                tanpa_komentar = re.sub(r"//[^\n]*", "", tanpa_komentar)
                if pola.search(tanpa_komentar):
                    salah.append(rel)
        self.assertGreaterEqual(diperiksa, 20,
                                f"cuma {diperiksa} berkas TS yang disapu")
        self.assertEqual(salah, [],
                         "layar/komponen memanggil `isyarat()` langsung; "
                         "pintunya `mainkanContoh()` atau `rasakanPerayaan()`")

    def test_keluaran_identik_dengan_python(self):
        import re
        import subprocess
        WEB = os.path.join(AKAR, "packages", "web")
        tugas = [(BERSAMA, s, p, l) for s, p, l in self.SKRIP]
        if os.path.isdir(os.path.join(WEB, "uji")):
            tugas += [(WEB, s, p, l) for s, p, l in self.SKRIP_WEB]
        for paket, skrip, pola, lantai in tugas:
            with self.subTest(skrip=skrip):
                hasil = subprocess.run(
                    ["node", "--experimental-strip-types",
                     os.path.join(paket, "uji", skrip)],
                    cwd=paket, capture_output=True, text=True, timeout=300)
                keluaran = (hasil.stdout + hasil.stderr).strip()
                # Pesannya tidak menyebut "rekaman Python": dua dari pembanding
                # ini mengadu dengan rekaman dari Python, tapi `banding-rasi`
                # mengadu dengan `rasi.js`. Pesan gagal yang menyebut sumber
                # yang salah mengirim orang mencari di berkas yang salah.
                self.assertEqual(
                    hasil.returncode, 0,
                    f"{skrip} melaporkan ketidakcocokan.\n" + keluaran[:4000])
                # Populasi ditagih di sini juga: skrip itu memang menolak
                # populasi yang tidak sama, tapi tes yang cuma memeriksa kode
                # keluar akan lulus kalau suatu hari penolakan itu dilepas.
                cacah = re.search(pola, keluaran)
                self.assertIsNotNone(
                    cacah, f"keluaran tak terbaca:\n{keluaran[:800]}")
                self.assertGreater(int(cacah.group(1)), lantai,
                                   "korpusnya menyusut; pagarnya jadi tumpul")


class TestGoldenPembuka(unittest.TestCase):
    """Rekaman acuan `ringkasPembuka` harus bisa dibangkitkan ULANG dari repo.

    Panel layar Langit memenggal paragraf pembuka sebuah materi di dua tempat:
    `alat/golden_pembuka.py` (acuan) dan `komponen/lensa-teks.ts`. Pembanding
    TypeScript menagih keluarannya terhadap `golden-pembuka.json`; tanpa tes
    ini rekaman itu cuma angka yang pernah benar, dan materi baru yang
    mengubah salah satu cabang aturan tidak akan terlihat sebagai selisih.
    """

    def test_rekaman_sama_dengan_pembangkitnya(self):
        import sys
        sys.path.insert(0, os.path.join(AKAR, "alat"))
        import golden_pembuka

        teks, kasus, total = golden_pembuka.bangun()
        self.assertGreaterEqual(total, 1062, "korpus materi menyusut")
        self.assertGreaterEqual(kasus, 100, "rekaman menyusut; pagarnya tumpul")
        with open(golden_pembuka.BERKAS, encoding="utf-8") as f:
            self.assertEqual(
                f.read(), teks,
                "golden-pembuka.json bergeser. Kalau disengaja, jalankan "
                "`python3 alat/golden_pembuka.py --tulis`")


if __name__ == "__main__":
    unittest.main(verbosity=2)
