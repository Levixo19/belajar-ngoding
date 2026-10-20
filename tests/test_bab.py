"""Tes pembagian bab: apa isinya, kapan terbuka, dan apa yang dikatakannya.

Yang diuji di sini KONTRAK `bab.py` dan isi `data/bab.py` — bukan antarmuka.
Terminal dan web sama-sama meminjam jawabannya dari modul ini, jadi satu aturan
yang bergeser di sini menggeser keduanya sekaligus.

Dua kelompok besar:

* **Isi datanya.** Rentang bab wajib menutupi SELURUH materi tiap bahasa tanpa
  celah maupun tumpang tindih. Rentang yang meleset tidak menghasilkan error
  apa pun — `bab.py` sengaja jatuh ke satu bab "Semua materi" supaya kurikulum
  tetap bisa dibaca — sehingga tanpa tes ini, hilangnya seluruh struktur bab
  tidak meninggalkan satu pun jejak di layar.
* **Aturan membukanya.** Bab berikutnya terbuka kalau seluruh materi bab
  sebelumnya sudah dibaca tuntas, yang sudah pernah dibuka tidak pernah
  menutup lagi, dan setiap pintu yang terkunci menyebutkan sisa pekerjaannya.

Penguncian adalah satu-satunya fitur di aplikasi ini yang MENOLAK memberi
sesuatu kepada pelajar. Kesalahan di sini tidak terasa seperti bug, melainkan
seperti progres yang hilang — karena itu ambangnya diuji dari dua sisi: yang
seharusnya terkunci, dan yang seharusnya tidak pernah terkunci lagi.
"""

import json
import os
import tempfile
import unittest

from pelajar import bab
from pelajar import konfigurasi
from pelajar import progress
from data.bab import BAB
from inti.kurikulum import LANGUAGES


def kunci_materi(lang, indeks):
    """Kunci progres materi ke-`indeks`, dibentuk persis seperti aplikasinya."""
    return progress.kunci(f"{lang['key']}_materi",
                          lang["materials"][indeks]["title"])


def progres(dibaca=(), sebagian=()):
    """Progres tiruan seperlunya; `bab.status` cuma membaca dua daftar ini."""
    return {"materi_dibaca": list(dibaca), "materi_sebagian": list(sebagian)}


def indeks_bab(lang, nomor, buka_semua=True):
    """Daftar indeks materi milik bab ke-`nomor` (1-based)."""
    return bab.status(lang, progres(), buka_semua)[nomor - 1]["materi"]


class BasisBab(unittest.TestCase):
    """Alihkan progres DAN konfigurasi ke direktori sementara.

    `bab.py` membaca keduanya: progres untuk tahu materi mana yang sudah
    dibaca, konfigurasi untuk saklar `buka_semua_bab`. Lupa mengalihkan yang
    pertama berarti menimpa catatan belajar sungguhan pemakai; lupa yang kedua
    lebih halus tapi tak kalah buruk — tesnya ikut membaca saklar milik orang
    yang menjalankannya, dan seluruh berkas ini bisa lulus karena alasan yang
    sepenuhnya salah.
    """

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self._progres_asli = progress.PROGRESS_FILE
        self._progres_lama_asli = progress.PROGRESS_FILE_LAMA
        self._konfig_asli = konfigurasi.BERKAS
        progress.PROGRESS_FILE = os.path.join(self.dir.name, "progress.json")
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name,
                                                   "tidak-ada.json")
        konfigurasi.BERKAS = os.path.join(self.dir.name, "konfig.json")
        konfigurasi.lupakan_cache()

    def tearDown(self):
        progress.PROGRESS_FILE = self._progres_asli
        progress.PROGRESS_FILE_LAMA = self._progres_lama_asli
        konfigurasi.BERKAS = self._konfig_asli
        konfigurasi.lupakan_cache()
        self.dir.cleanup()

    def tulis_konfig(self, **nilai):
        with open(konfigurasi.BERKAS, "w", encoding="utf-8") as f:
            json.dump(nilai, f)
        konfigurasi.lupakan_cache()


# --------------------------------------------------------------- isi datanya

class TestDataBab(BasisBab):
    """Yang diperiksa di sini menyangkut seluruh bahasa yang dirilis."""

    def test_setiap_bahasa_punya_pembagian_bab(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertTrue(bab.punya_bab(lang["key"]),
                                "bahasa ini belum punya entri di data/bab.py")

    def test_tidak_ada_entri_bab_untuk_bahasa_yang_tidak_ada(self):
        # Entri sisa dari bahasa yang sudah dihapus tidak pernah terlihat di
        # layar mana pun, tapi ia tetap ikut disunting orang berikutnya.
        yatim = set(BAB) - {lang["key"] for lang in LANGUAGES}
        self.assertEqual(yatim, set())

    def test_rentang_menutupi_seluruh_materi_tanpa_celah(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                tertutup = []
                for entri in BAB[lang["key"]]:
                    tertutup.extend(range(entri["awal"], entri["akhir"]))
                self.assertEqual(tertutup, list(range(len(lang["materials"]))),
                                 "rentang berlubang, tumpang tindih, atau "
                                 "tidak lagi cocok dengan jumlah materinya")

    def test_tidak_ada_bab_kosong(self):
        # Bab tanpa materi lolos dari pemeriksaan rentang di atas (ia tidak
        # menutupi apa pun), tapi akibatnya fatal: bab kosong tidak akan pernah
        # bisa "tuntas", jadi seluruh bab sesudahnya terkunci SELAMANYA.
        # Perilaku itu dikunci di TestJalurCadangan.
        for lang in LANGUAGES:
            for entri in BAB[lang["key"]]:
                with self.subTest(bahasa=lang["label"], bab=entri["judul"]):
                    self.assertGreater(entri["akhir"], entri["awal"])

    def test_jalur_cadangan_tidak_pernah_terpakai(self):
        # "Semua materi" adalah jaring pengaman, bukan hasil yang sah. Kalau ia
        # muncul, pembagian bab bahasa itu diam-diam sudah tidak berlaku.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                daftar = bab.status(lang, progres(), buka_semua=True)
                self.assertEqual(len(daftar), len(BAB[lang["key"]]))
                self.assertEqual([b["judul"] for b in daftar],
                                 [e["judul"] for e in BAB[lang["key"]]])
                self.assertNotIn("Semua materi", [b["judul"] for b in daftar])

    def test_setiap_bahasa_punya_lebih_dari_satu_bab(self):
        # Satu bab berisi semuanya = daftar panjang yang dulu ingin dipecah.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertGreater(len(BAB[lang["key"]]), 1)

    def test_tingkat_sah_dan_tidak_pernah_menurun(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                urut = []
                for entri in BAB[lang["key"]]:
                    self.assertIn(entri["tingkat"], bab.TINGKAT,
                                  f"tingkat asing: {entri['tingkat']!r}")
                    urut.append(bab.TINGKAT.index(entri["tingkat"]))
                self.assertEqual(urut, sorted(urut),
                                 "kurikulum yang naik lalu turun lagi membuat "
                                 "orang mengira ia salah membaca urutan")

    def test_bab_pertama_selalu_tingkat_dasar(self):
        # Pintu masuk sebuah bahasa tidak boleh langsung menyodorkan sesuatu
        # yang bukan untuk pemula.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertEqual(BAB[lang["key"]][0]["tingkat"], "dasar")

    def test_judul_bab_unik_dan_keterangannya_terisi(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                judul = [e["judul"] for e in BAB[lang["key"]]]
                self.assertEqual(len(judul), len(set(judul)),
                                 f"judul bab kembar: {judul}")
                for entri in BAB[lang["key"]]:
                    self.assertTrue(entri["judul"].strip())
                    self.assertTrue(entri.get("ket", "").strip(),
                                    f"{entri['judul']}: keterangannya kosong, "
                                    "jadi bab terkunci tidak bisa menjelaskan "
                                    "apa yang sedang ditunggu")

    def test_setiap_tingkat_punya_label_dan_keterangan(self):
        for tingkat in bab.TINGKAT:
            with self.subTest(tingkat=tingkat):
                self.assertTrue(bab.LABEL_TINGKAT.get(tingkat, "").strip())
                self.assertTrue(bab.KETERANGAN_TINGKAT.get(tingkat, "").strip())

    def test_label_tingkat_ikut_di_setiap_status(self):
        for lang in LANGUAGES:
            for b in bab.status(lang, progres(), buka_semua=True):
                with self.subTest(bahasa=lang["label"], bab=b["nomor"]):
                    self.assertEqual(b["label_tingkat"],
                                     bab.LABEL_TINGKAT[b["tingkat"]])

    def test_nomor_dan_rentang_berurutan_rapat(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                daftar = bab.status(lang, progres(), buka_semua=True)
                self.assertEqual([b["nomor"] for b in daftar],
                                 list(range(1, len(daftar) + 1)))
                self.assertEqual(daftar[0]["awal"], 0)
                self.assertEqual(daftar[-1]["akhir"], len(lang["materials"]))
                for sebelum, sesudah in zip(daftar, daftar[1:]):
                    self.assertEqual(sebelum["akhir"], sesudah["awal"])
                for b in daftar:
                    self.assertEqual(b["materi"],
                                     list(range(b["awal"], b["akhir"])))
                    self.assertEqual(b["jumlah"], len(b["materi"]))


# ------------------------------------------------- bentuk yang dipinjam web

class TestBentukKontrak(BasisBab):
    """Nama bidang dan nilai yang menyeberang ke sisi lain apa adanya.

    `/api/bahasa` menyalin dict dari `status()` langsung menjadi JSON, dan JS
    di seberang sana mencocokkan `status` dengan string mentahnya. Salah satu
    huruf yang bergeser di sini tidak melempar apa pun di Python — ia berubah
    jadi `undefined` di browser, dan yang terlihat pemakainya cuma bab tanpa
    keterangan atau pintu yang tidak pernah mau terbuka. Karena itu yang
    diikat di kelas ini huruf-hurufnya, bukan konstantanya: membandingkan
    `bab.TERKUNCI` dengan dirinya sendiri akan tetap hijau justru pada
    perubahan yang merusak sisi web.
    """

    BIDANG = {"nomor", "judul", "ket", "tingkat", "label_tingkat", "awal",
              "akhir", "materi", "selesai", "jumlah", "kurang", "persen",
              "status", "alasan"}

    def test_status_membawa_tepat_bidang_yang_dijanjikan(self):
        for lang in LANGUAGES:
            for b in bab.status(lang, progres(), buka_semua=False):
                with self.subTest(bahasa=lang["label"], bab=b["nomor"]):
                    self.assertEqual(set(b), self.BIDANG)

    def test_ket_diteruskan_apa_adanya_dari_data(self):
        # `ket` satu-satunya bidang yang cuma numpang lewat: tidak ada satu
        # pun perhitungan di atasnya, jadi tidak ada tes lain yang akan
        # merasakan kalau ia hilang atau tertukar di tengah jalan.
        for lang in LANGUAGES:
            daftar = bab.status(lang, progres(), buka_semua=True)
            for b, entri in zip(daftar, BAB[lang["key"]]):
                with self.subTest(bahasa=lang["label"], bab=b["nomor"]):
                    self.assertEqual(b["ket"], entri["ket"])

    def test_nilai_status_persis_seperti_di_kontrak(self):
        self.assertEqual(bab.TERKUNCI, "terkunci")
        self.assertEqual(bab.TERBUKA, "terbuka")
        self.assertEqual(bab.TUNTAS, "tuntas")

    def test_nilai_tingkat_persis_seperti_di_kontrak(self):
        self.assertEqual(bab.TINGKAT, ("dasar", "menengah", "mahir"))


# ------------------------------------------------------ aturan membuka bab

class TestMembukaBertahap(BasisBab):

    def test_bab_pertama_terbuka_bab_kedua_terkunci(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                daftar = bab.status(lang, progres(), buka_semua=False)
                self.assertEqual(daftar[0]["status"], bab.TERBUKA)
                self.assertEqual(daftar[1]["status"], bab.TERKUNCI)

    def test_progres_kosong_tidak_membuat_apa_pun_tuntas(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                for b in bab.status(lang, progres(), buka_semua=False):
                    self.assertNotEqual(b["status"], bab.TUNTAS)
                    self.assertEqual(b["selesai"], 0)
                    self.assertEqual(b["persen"], 0)
                    self.assertEqual(b["kurang"], b["jumlah"])

    def test_menuntaskan_bab_satu_membuka_bab_dua_saja(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                dibaca = [kunci_materi(lang, i)
                          for i in indeks_bab(lang, 1)]
                daftar = bab.status(lang, progres(dibaca), buka_semua=False)
                self.assertEqual(daftar[0]["status"], bab.TUNTAS)
                self.assertEqual(daftar[0]["persen"], 100)
                self.assertEqual(daftar[0]["kurang"], 0)
                self.assertEqual(daftar[1]["status"], bab.TERBUKA)
                self.assertEqual(daftar[2]["status"], bab.TERKUNCI)

    def test_kurang_satu_materi_belum_membuka_apa_apa(self):
        # Batasnya harus tepat di "seluruhnya", bukan "hampir seluruhnya".
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                dibaca = [kunci_materi(lang, i)
                          for i in indeks_bab(lang, 1)[:-1]]
                daftar = bab.status(lang, progres(dibaca), buka_semua=False)
                self.assertEqual(daftar[0]["status"], bab.TERBUKA)
                self.assertEqual(daftar[0]["kurang"], 1)
                self.assertEqual(daftar[1]["status"], bab.TERKUNCI)

    def test_membaca_sebagian_tidak_membuka_bab_berikutnya(self):
        # `materi_sebagian` = berhenti di tengah halaman. Menghitungnya sebagai
        # selesai membuat seluruh syarat bab ini kehilangan artinya.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                setengah = [kunci_materi(lang, i) for i in indeks_bab(lang, 1)]
                daftar = bab.status(lang, progres(sebagian=setengah),
                                    buka_semua=False)
                self.assertEqual(daftar[0]["selesai"], 0)
                self.assertEqual(daftar[0]["status"], bab.TERBUKA)
                self.assertEqual(daftar[1]["status"], bab.TERKUNCI)

    def test_bab_yang_pernah_disentuh_tidak_terkunci_lagi(self):
        # Skenarionya nyata: saklar "buka semua bab" pernah dinyalakan, orang
        # membaca satu materi di bab 3, lalu saklarnya dimatikan lagi. Menutup
        # kembali bab yang sudah ia buka akan terbaca sebagai progres hilang.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                satu = kunci_materi(lang, indeks_bab(lang, 3)[0])
                daftar = bab.status(lang, progres([satu]), buka_semua=False)
                self.assertEqual(daftar[2]["status"], bab.TERBUKA)
                self.assertEqual(daftar[2]["selesai"], 1)
                self.assertEqual(daftar[1]["status"], bab.TERKUNCI)

    def test_bab_terakhir_tuntas_membuat_semuanya_tuntas(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                semua = [kunci_materi(lang, i)
                         for i in range(len(lang["materials"]))]
                daftar = bab.status(lang, progres(semua), buka_semua=False)
                for b in daftar:
                    self.assertEqual(b["status"], bab.TUNTAS)
                    self.assertEqual(b["persen"], 100)
                    self.assertEqual(b["alasan"], "")

    def test_materi_bahasa_lain_tidak_ikut_membuka(self):
        # Kunci progres dibedakan oleh prefix bahasanya; kalau prefix itu
        # terlewat, membaca Python akan membuka bab Java.
        lain = LANGUAGES[1]
        dibaca = [kunci_materi(lain, i) for i in range(len(lain["materials"]))]
        daftar = bab.status(LANGUAGES[0], progres(dibaca), buka_semua=False)
        self.assertEqual(daftar[0]["selesai"], 0)
        self.assertEqual(daftar[1]["status"], bab.TERKUNCI)

    def test_progres_dibaca_sendiri_kalau_data_tidak_diberikan(self):
        # Jalur yang sebenarnya dipakai antarmuka: tanpa argumen `data`.
        lang = LANGUAGES[0]
        kategori = f"{lang['key']}_materi"
        for i in indeks_bab(lang, 1):
            progress.record_material_read(kategori,
                                          lang["materials"][i]["title"])
        daftar = bab.status(lang, buka_semua=False)
        self.assertEqual(daftar[0]["status"], bab.TUNTAS)
        self.assertEqual(daftar[1]["status"], bab.TERBUKA)

    def test_materi_dibaca_sebagian_lewat_progress_tidak_membuka(self):
        # Sisi lain dari tes di atas: `record_material_read(..., tuntas=False)`
        # menulis ke daftar yang berbeda, dan bab.py harus mengabaikannya.
        lang = LANGUAGES[0]
        kategori = f"{lang['key']}_materi"
        for i in indeks_bab(lang, 1):
            progress.record_material_read(kategori,
                                          lang["materials"][i]["title"],
                                          tuntas=False)
        daftar = bab.status(lang, buka_semua=False)
        self.assertEqual(daftar[0]["selesai"], 0)
        self.assertEqual(daftar[1]["status"], bab.TERKUNCI)


# ------------------------------------------------------- kalimat "kenapa"

class TestAlasan(BasisBab):

    def test_bab_terbuka_tidak_punya_alasan(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                for b in bab.status(lang, progres(), buka_semua=False):
                    if b["status"] != bab.TERKUNCI:
                        self.assertEqual(b["alasan"], "")

    def test_setiap_bab_terkunci_menyebut_sisa_dan_judul_pendahulunya(self):
        # "Terkunci" sendirian membuat orang menebak-nebak. Yang dibutuhkan
        # justru angkanya: berapa lagi, dan di bab yang mana.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                daftar = bab.status(lang, progres(), buka_semua=False)
                for sebelum, b in zip(daftar, daftar[1:]):
                    if b["status"] != bab.TERKUNCI:
                        continue
                    self.assertIn(str(sebelum["kurang"]), b["alasan"])
                    self.assertIn(sebelum["judul"], b["alasan"])
                    self.assertIn(f"Bab {sebelum['nomor']}", b["alasan"])

    def test_kalimat_berubah_saat_tinggal_satu_materi(self):
        # Angka "1" di kalimat jamak ("Baca 1 materi lagi") terbaca kaku;
        # bentuk tunggalnya sengaja berbeda karena inilah kalimat yang paling
        # sering dilihat orang tepat sebelum sebuah bab terbuka.
        lang = LANGUAGES[0]
        judul = bab.status(lang, progres(), buka_semua=True)[0]["judul"]

        kosong = bab.status(lang, progres(), buka_semua=False)[1]["alasan"]
        self.assertTrue(kosong.startswith("Baca "), kosong)
        self.assertIn(judul, kosong)

        hampir = [kunci_materi(lang, i) for i in indeks_bab(lang, 1)[:-1]]
        satu = bab.status(lang, progres(hampir), buka_semua=False)[1]["alasan"]
        self.assertTrue(satu.startswith("Tinggal 1 materi lagi"), satu)
        self.assertIn(judul, satu)
        self.assertNotIn("Baca 1 materi", satu)

    def test_alasan_tidak_pernah_kosong_untuk_bab_terkunci(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                dibaca = [kunci_materi(lang, i)
                          for i in indeks_bab(lang, 1)]
                for keadaan in (progres(), progres(dibaca)):
                    for b in bab.status(lang, keadaan, buka_semua=False):
                        if b["status"] == bab.TERKUNCI:
                            self.assertTrue(b["alasan"].strip())


# ------------------------------------------------------------- pintu darurat

class TestBukaSemua(BasisBab):

    def test_parameter_buka_semua_membuka_seluruh_bab(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                daftar = bab.status(lang, progres(), buka_semua=True)
                for b in daftar:
                    self.assertNotEqual(b["status"], bab.TERKUNCI)
                    self.assertEqual(b["alasan"], "")
                self.assertEqual(bab.indeks_terbuka(lang, progres(), True),
                                 set(range(len(lang["materials"]))))

    def test_buka_semua_tidak_mengaku_aku_sudah_tuntas(self):
        # Membuka pintu bukan mengerjakan isinya. Kalau saklar ini ikut
        # menandai bab tuntas, statistik belajar orang jadi bohong.
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                for b in bab.status(lang, progres(), buka_semua=True):
                    self.assertEqual(b["status"], bab.TERBUKA)
                    self.assertEqual(b["selesai"], 0)
                    self.assertEqual(b["persen"], 0)

    def test_saklar_konfigurasi_setara_dengan_parameternya(self):
        self.tulis_konfig(buka_semua_bab=True)
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertEqual(bab.status(lang),
                                 bab.status(lang, buka_semua=True))

    def test_saklar_konfigurasi_mati_tetap_mengunci(self):
        self.tulis_konfig(buka_semua_bab=False)
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                self.assertEqual(bab.status(lang)[1]["status"], bab.TERKUNCI)

    def test_tanpa_setelan_apa_pun_penguncian_berlaku(self):
        # Bawaannya harus mengunci: kurikulum bertahap yang defaultnya terbuka
        # semua sama saja dengan tidak ada.
        self.assertFalse(konfigurasi.ambil("buka_semua_bab"))
        self.assertEqual(bab.status(LANGUAGES[0])[1]["status"], bab.TERKUNCI)

    def test_parameter_menang_atas_saklar(self):
        # Pemanggil yang menulis buka_semua=False sedang menjawab pertanyaan
        # lain ("apa yang akan terjadi kalau saklarnya dimatikan?").
        self.tulis_konfig(buka_semua_bab=True)
        lang = LANGUAGES[0]
        self.assertEqual(bab.status(lang, buka_semua=False)[1]["status"],
                         bab.TERKUNCI)

    def test_saklar_terdaftar_di_skema_konfigurasi(self):
        # Kalau entrinya hilang dari SKEMA, menu Pengaturan di terminal dan web
        # ikut kehilangan satu-satunya jalan keluar dari jalur linear ini.
        opsi = konfigurasi.opsi("buka_semua_bab")
        self.assertIsNotNone(opsi)
        self.assertEqual(opsi.jenis, "sakelar")
        self.assertFalse(opsi.bawaan)


# --------------------------------------- konsistensi antar fungsi bantu

class TestKonsistensi(BasisBab):
    """Semua fungsi lain wajib menjawab hal yang sama dengan `status()`.

    Antarmuka memanggil yang paling murah untuk keperluannya masing-masing
    (`indeks_terbuka` untuk menyaring daftar, `terkunci` untuk menjaga pintu).
    Begitu dua di antaranya berbeda pendapat, materi bisa terlihat terbuka di
    daftar tapi menolak dibuka saat diklik.
    """

    def keadaan(self, lang):
        """Beberapa titik progres yang berbeda untuk bahasa yang sama."""
        semua = range(len(lang["materials"]))
        bab1 = indeks_bab(lang, 1)
        return [
            progres(),
            progres([kunci_materi(lang, i) for i in bab1[:1]]),
            progres([kunci_materi(lang, i) for i in bab1]),
            progres([kunci_materi(lang, i) for i in semua]),
        ]

    def test_indeks_terbuka_sama_dengan_gabungan_bab_terbuka(self):
        for lang in LANGUAGES:
            for data in self.keadaan(lang):
                with self.subTest(bahasa=lang["label"]):
                    daftar = bab.status(lang, data, buka_semua=False)
                    harus = set()
                    for b in daftar:
                        if b["status"] != bab.TERKUNCI:
                            harus.update(b["materi"])
                    self.assertEqual(
                        bab.indeks_terbuka(lang, data, False), harus)

    def test_terkunci_sama_dengan_status_babnya(self):
        for lang in LANGUAGES:
            for data in self.keadaan(lang):
                terbuka = bab.indeks_terbuka(lang, data, False)
                for i in range(len(lang["materials"])):
                    with self.subTest(bahasa=lang["label"], materi=i):
                        self.assertEqual(bab.terkunci(lang, i, data, False),
                                         i not in terbuka)

    def test_bab_materi_menunjuk_bab_yang_memuat_indeksnya(self):
        for lang in LANGUAGES:
            daftar = bab.status(lang, progres(), buka_semua=False)
            for b in daftar:
                for i in b["materi"]:
                    with self.subTest(bahasa=lang["label"], materi=i):
                        self.assertEqual(
                            bab.bab_materi(lang, i, progres(), False), b)

    def test_tingkat_materi_ikut_tingkat_babnya(self):
        for lang in LANGUAGES:
            for b in bab.status(lang, progres(), buka_semua=False):
                for i in b["materi"]:
                    with self.subTest(bahasa=lang["label"], materi=i):
                        self.assertEqual(
                            bab.tingkat_materi(lang, i, progres(), False),
                            b["tingkat"])

    def test_ringkas_menghitung_dari_status_yang_sama(self):
        for lang in LANGUAGES:
            for data in self.keadaan(lang):
                with self.subTest(bahasa=lang["label"]):
                    daftar = bab.status(lang, data, buka_semua=False)
                    tuntas, jumlah, kini = bab.ringkas(lang, data, False)
                    self.assertEqual(
                        tuntas,
                        sum(1 for b in daftar if b["status"] == bab.TUNTAS))
                    self.assertEqual(jumlah, len(daftar))
                    self.assertEqual(
                        kini,
                        next((b for b in daftar
                              if b["status"] == bab.TERBUKA), None))

    def test_kalimat_ringkas_menyebut_bab_yang_sedang_jalan(self):
        for lang in LANGUAGES:
            for data in self.keadaan(lang):
                with self.subTest(bahasa=lang["label"]):
                    tuntas, jumlah, kini = bab.ringkas(lang, data, False)
                    kalimat = bab.kalimat_ringkas(lang, data, False)
                    self.assertTrue(kalimat.strip())
                    if kini is None:
                        self.assertIn(str(jumlah), kalimat)
                        continue
                    self.assertIn(kini["judul"], kalimat)
                    self.assertIn(f"Bab {kini['nomor']}", kalimat)
                    self.assertIn(f"{kini['selesai']}/{kini['jumlah']}",
                                  kalimat)

    def test_kalimat_ringkas_sama_persis_dengan_contoh_di_kontrak(self):
        """BENTUK kalimatnya yang dikunci, bukan isinya.

        Versi pertama tes ini menuliskan hasilnya apa adanya
        ("Bab 2 dari 4: OOP (3/5 materi)"), dan pecah begitu kurikulumnya
        bertambah — bukan karena ada yang rusak, melainkan karena judul dan
        jumlah babnya memang berubah. Yang benar-benar disepakati bersama
        antarmuka web (kontrak "bab_kalimat") adalah SUSUNANNYA, jadi itu yang
        dirakit ulang di sini dari sumber datanya sendiri.
        """
        lang = next(l for l in LANGUAGES if l["key"] == "java")
        daftar = bab.status(lang, progres([]), False)
        dibaca = [kunci_materi(lang, i) for i in indeks_bab(lang, 1)]
        dibaca += [kunci_materi(lang, i) for i in indeks_bab(lang, 2)[:3]]

        b2 = daftar[1]
        diharap = (f"Bab 2 dari {len(daftar)}: {b2['judul']} "
                   f"(3/{b2['jumlah']} materi)")
        self.assertEqual(bab.kalimat_ringkas(lang, progres(dibaca), False),
                         diharap)

    def test_kalimat_ringkas_saat_semuanya_tuntas(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                semua = [kunci_materi(lang, i)
                         for i in range(len(lang["materials"]))]
                kalimat = bab.kalimat_ringkas(lang, progres(semua), False)
                self.assertIn("tuntas", kalimat)
                self.assertIn(str(len(BAB[lang["key"]])), kalimat)


# ---------------------------------------------------------- indeks liar

class TestBatasIndeks(BasisBab):
    """Indeks yang mustahil tetap tidak boleh menjatuhkan apa pun.

    Indeks materi datang dari URL dan dari input menu — keduanya bisa berisi
    angka apa saja, dan yang harus terjadi adalah "tidak ada", bukan traceback.
    """

    def test_indeks_di_luar_jangkauan_tidak_punya_bab(self):
        for lang in LANGUAGES:
            jumlah = len(lang["materials"])
            for i in (-1, -100, jumlah, jumlah + 50):
                with self.subTest(bahasa=lang["label"], materi=i):
                    self.assertIsNone(
                        bab.bab_materi(lang, i, progres(), False))

    def test_indeks_di_luar_jangkauan_tidak_dianggap_terkunci(self):
        # Menganggapnya terkunci akan membuat antarmuka menampilkan alasan
        # penguncian untuk materi yang bahkan tidak ada.
        lang = LANGUAGES[0]
        for i in (-1, len(lang["materials"]), 10 ** 6):
            with self.subTest(materi=i):
                self.assertFalse(bab.terkunci(lang, i, progres(), False))

    def test_tingkat_materi_di_luar_jangkauan_jatuh_ke_dasar(self):
        # Bawaannya harus yang paling tidak menakutkan. "Mahir" untuk materi
        # yang bahkan tidak ada bukan cuma salah — ia memberi label menyeramkan
        # pada sesuatu yang tidak bisa dibuka siapa pun untuk dibantah.
        lang = LANGUAGES[0]
        for i in (-1, len(lang["materials"])):
            with self.subTest(materi=i):
                self.assertEqual(bab.tingkat_materi(lang, i, progres(), False),
                                 "dasar")

    def test_indeks_terbuka_tidak_pernah_keluar_jangkauan(self):
        for lang in LANGUAGES:
            with self.subTest(bahasa=lang["label"]):
                terbuka = bab.indeks_terbuka(lang, progres(), True)
                self.assertTrue(
                    terbuka <= set(range(len(lang["materials"]))))

    def test_progres_berisi_kunci_asing_tidak_mengganggu(self):
        # Berkas progres menyimpan materi dari semua bahasa, plus sisa kunci
        # dari materi yang judulnya sudah pernah berubah.
        lang = LANGUAGES[0]
        sampah = progres(["tidak_ada::apa pun", "", "java_materi::Hantu"])
        daftar = bab.status(lang, sampah, buka_semua=False)
        self.assertEqual(daftar[0]["selesai"], 0)
        self.assertEqual(daftar[1]["status"], bab.TERKUNCI)

    def test_progres_tanpa_bidang_materi_dibaca(self):
        # Berkas progres versi lama, atau dict kosong dari pemanggil.
        daftar = bab.status(LANGUAGES[0], {}, buka_semua=False)
        self.assertEqual(daftar[0]["status"], bab.TERBUKA)


# ----------------------------------------------------------- bahasa karangan

class BasisSintetis(BasisBab):
    """Bahasa karangan, supaya bentuk dan angkanya bisa diatur persis.

    Sebagian keadaan yang harus diuji tidak ada di data yang dirilis — bab
    berlubang, bab kosong, bahasa berbab satu — dan tidak boleh dipaksa ada
    hanya demi sebuah tes. Jalan keluarnya menyisipkan kunci sendiri ke
    `bab.BAB` (objek yang SAMA dengan `data.bab.BAB`) lalu mencabutnya lagi
    lewat `addCleanup`. Inilah satu-satunya tempat di berkas ini yang
    menyentuh isi modul saat berjalan; siapa pun yang menambah tes di
    turunannya wajib ikut polanya, karena kunci yang lupa dicabut akan
    menggagalkan `test_tidak_ada_entri_bab_untuk_bahasa_yang_tidak_ada` di
    berkas ini juga.
    """

    KUNCI = "bahasa_uji_bab"

    def setUp(self):
        super().setUp()
        self.addCleanup(bab.BAB.pop, self.KUNCI, None)

    def bahasa(self, jumlah=6):
        return {"key": self.KUNCI, "label": "Uji",
                "materials": [{"title": f"Materi {i}"} for i in range(jumlah)]}

    def pasang(self, *rentang):
        bab.BAB[self.KUNCI] = [
            {"judul": f"Bab uji {n}", "ket": "keterangan",
             "tingkat": "dasar", "awal": awal, "akhir": akhir}
            for n, (awal, akhir) in enumerate(rentang, start=1)]


class TestBahasaKarangan(BasisSintetis):
    """Bentuk sah yang kebetulan belum dipakai bahasa mana pun.

    Bahasa berbab satu dan berbab dua tidak melanggar apa pun — data yang
    dirilis sekarang saja yang tidak punya. Justru di ambang itulah kalimat
    ringkasnya berhenti berbunyi, dan ambang yang tidak diuji adalah ambang
    yang bisa bergeser tanpa satu pun tanda.
    """

    def test_satu_bab_terbuka_dan_tidak_berkalimat(self):
        # Bedanya dengan jalur cadangan di bawah: pembagian ini SAH, bukan
        # jaring pengaman. Yang tidak boleh muncul cuma kalimatnya —
        # "Bab 1 dari 1" tidak memberi tahu apa pun yang belum terlihat.
        self.pasang((0, 6))
        lang = self.bahasa()
        daftar = bab.status(lang, progres(), buka_semua=False)
        self.assertEqual([b["judul"] for b in daftar], ["Bab uji 1"])
        self.assertEqual(daftar[0]["status"], bab.TERBUKA)
        self.assertEqual(bab.indeks_terbuka(lang, progres(), False),
                         set(range(len(lang["materials"]))))
        self.assertEqual(bab.kalimat_ringkas(lang, progres(), False), "")

    def test_dua_bab_tetap_berkalimat(self):
        # Ambangnya "lebih dari satu", bukan "lebih dari dua". Bahasa berbab
        # dua masih punya sesuatu untuk diberitahukan, dan kehilangan kalimat
        # itu tidak akan terlihat seperti kerusakan — cuma seperti kepala
        # halaman yang memang kosong.
        self.pasang((0, 3), (3, 6))
        lang = self.bahasa()
        self.assertEqual(bab.kalimat_ringkas(lang, progres(), False),
                         "Bab 1 dari 2: Bab uji 1 (0/3 materi)")
        habis = [kunci_materi(lang, i) for i in range(3)]
        self.assertEqual(bab.kalimat_ringkas(lang, progres(habis), False),
                         "Bab 2 dari 2: Bab uji 2 (0/3 materi)")

    def test_persen_dibulatkan_bukan_dipotong(self):
        # Angka ini dipakai apa adanya oleh bilah kemajuan di kedua antarmuka.
        # Bab berisi 7 materi dipilih karena tidak satu pun pecahannya bulat:
        # memotong (int) dan membulatkan ke atas (ceil) masing-masing meleset
        # di ujung yang berbeda, jadi dua titik ini menutup keduanya sekaligus.
        self.pasang((0, 7))
        lang = self.bahasa(jumlah=7)
        for dibaca, persen in ((1, 14), (6, 86)):
            with self.subTest(dibaca=dibaca):
                kunci = [kunci_materi(lang, i) for i in range(dibaca)]
                self.assertEqual(
                    bab.status(lang, progres(kunci), False)[0]["persen"],
                    persen)


# ------------------------------------------------------- jaring pengamannya

class TestJalurCadangan(BasisSintetis):
    """Apa yang terjadi kalau pembagian babnya sendiri yang salah.

    Kurikulum yang seluruhnya terbuka jauh lebih baik daripada kurikulum yang
    separuhnya hilang karena satu angka lupa diperbarui — jadi rentang yang
    tidak lagi cocok tidak melempar apa pun, melainkan jatuh ke satu bab berisi
    semuanya. `TestDataBab` yang menjaga supaya jalur ini tidak pernah benar-
    benar terpakai di data yang dirilis; di sini yang diperiksa jaringnya
    sendiri masih utuh.
    """

    def cadangan(self, lang):
        daftar = bab.status(lang, progres(), buka_semua=False)
        self.assertEqual(len(daftar), 1)
        self.assertEqual(daftar[0]["judul"], "Semua materi")
        self.assertEqual(daftar[0]["status"], bab.TERBUKA)
        self.assertEqual(daftar[0]["materi"],
                         list(range(len(lang["materials"]))))
        return daftar[0]

    def test_entri_tanpa_tingkat_dan_ket_tidak_menjatuhkan_apa_pun(self):
        # Bidang yang lupa diisi saat menambah bab baru. Yang benar bukan
        # melempar — yang salah menulis sedang menyunting data, bukan memakai
        # aplikasinya — melainkan memilih nilai yang paling tidak menyesatkan.
        # Keterangan kosong terbaca sebagai keterangan kosong dan selesai;
        # sedangkan tingkat yang mengarang sendiri tetap tampil sebagai label
        # yang meyakinkan, dan pelajar tidak punya cara menebak itu bohong.
        bab.BAB[self.KUNCI] = [{"judul": "Bab uji 1", "awal": 0, "akhir": 6}]
        b = bab.status(self.bahasa(), progres(), buka_semua=False)[0]
        self.assertEqual(b["tingkat"], "dasar")
        self.assertEqual(b["label_tingkat"], "Dasar")
        self.assertEqual(b["ket"], "")

    def test_bahasa_tanpa_entri_bab_tetap_terbuka_seluruhnya(self):
        lang = self.bahasa()
        self.assertFalse(bab.punya_bab(lang["key"]))
        self.cadangan(lang)
        self.assertEqual(bab.indeks_terbuka(lang, progres(), False),
                         set(range(len(lang["materials"]))))
        for i in range(len(lang["materials"])):
            self.assertFalse(bab.terkunci(lang, i, progres(), False))

    def test_satu_bab_tidak_menghasilkan_kalimat_ringkas(self):
        # "Bab 1 dari 1" bukan informasi, cuma perabot.
        self.assertEqual(
            bab.kalimat_ringkas(self.bahasa(), progres(), False), "")

    def test_rentang_berlubang_jatuh_ke_cadangan(self):
        self.pasang((0, 2), (3, 6))
        self.cadangan(self.bahasa())

    def test_rentang_tumpang_tindih_jatuh_ke_cadangan(self):
        self.pasang((0, 4), (2, 6))
        self.cadangan(self.bahasa())

    def test_materi_bertambah_tanpa_memperbarui_bab_jatuh_ke_cadangan(self):
        # Inilah kasus yang paling mungkin terjadi: materi ke-7 ditambahkan,
        # data/bab.py tidak ikut disunting.
        self.pasang((0, 3), (3, 6))
        self.cadangan(self.bahasa(jumlah=7))

    def test_materi_berkurang_tanpa_memperbarui_bab_jatuh_ke_cadangan(self):
        self.pasang((0, 3), (3, 6))
        self.cadangan(self.bahasa(jumlah=5))

    def test_pembagian_yang_cocok_tidak_memakai_cadangan(self):
        # Penyeimbang tes-tes di atas: jaringnya tidak boleh menangkap data
        # yang sebenarnya sehat.
        self.pasang((0, 3), (3, 6))
        daftar = bab.status(self.bahasa(), progres(), buka_semua=False)
        self.assertEqual([b["judul"] for b in daftar],
                         ["Bab uji 1", "Bab uji 2"])
        self.assertEqual(daftar[1]["status"], bab.TERKUNCI)

    def test_bab_kosong_mengunci_sisanya_selamanya(self):
        # Bukan perilaku yang diinginkan, melainkan bukti kenapa
        # `test_tidak_ada_bab_kosong` harus ada. Bab tanpa materi lolos dari
        # pemeriksaan rentang (ia memang tidak menutupi apa pun), tapi ia tidak
        # akan PERNAH tuntas — tidak ada yang bisa dibaca di dalamnya — jadi
        # bab sesudahnya terkunci untuk selamanya. Satu-satunya yang bisa
        # membukanya adalah membaca materi di dalam bab yang terkunci itu, dan
        # itu persis hal yang tidak bisa dilakukan dari antarmuka mana pun.
        self.pasang((0, 2), (2, 2), (2, 6))
        lang = self.bahasa()
        habis = [kunci_materi(lang, i) for i in (0, 1)]
        daftar = bab.status(lang, progres(habis), buka_semua=False)
        self.assertEqual(daftar[0]["status"], bab.TUNTAS)
        self.assertEqual(daftar[1]["jumlah"], 0)
        self.assertEqual(daftar[1]["persen"], 0)
        self.assertNotEqual(daftar[1]["status"], bab.TUNTAS)
        self.assertEqual(daftar[2]["status"], bab.TERKUNCI)
        self.assertEqual(daftar[2]["alasan"],
                         "Selesaikan Bab 2 · Bab uji 2 lebih dulu.")


if __name__ == "__main__":
    unittest.main()
