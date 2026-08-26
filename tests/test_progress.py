"""Tes penyimpanan progres, XP, level, streak, badge, dan penjadwalan ulang."""

import json
import os
import tempfile
import unittest
from datetime import date, timedelta

import progress


class BasisProgres(unittest.TestCase):
    """Arahkan file progres ke lokasi sementara agar data asli tidak tersentuh."""

    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.dir.name, "progress.json")
        self._asli = progress.PROGRESS_FILE
        self._asli_lama = progress.PROGRESS_FILE_LAMA
        progress.PROGRESS_FILE = self.path
        progress.PROGRESS_FILE_LAMA = os.path.join(self.dir.name, "tidak-ada.json")

    def tearDown(self):
        progress.PROGRESS_FILE = self._asli
        progress.PROGRESS_FILE_LAMA = self._asli_lama
        self.dir.cleanup()


class TestMuatSimpan(BasisProgres):
    def test_file_belum_ada_memberi_default(self):
        data = progress.load_progress()
        self.assertEqual(data["materi_dibaca"], [])
        self.assertEqual(data["xp"], 0)
        self.assertEqual(data["versi"], progress.VERSI_DATA)

    def test_bolak_balik_simpan_muat(self):
        data = progress.load_progress()
        data["xp"] = 123
        data["materi_dibaca"].append("java_materi::A")
        progress.save_progress(data)

        ulang = progress.load_progress()
        self.assertEqual(ulang["xp"], 123)
        self.assertIn("java_materi::A", ulang["materi_dibaca"])

    def test_file_rusak_tidak_bikin_crash(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write("{ini bukan json sama sekali")
        data = progress.load_progress()
        self.assertEqual(data["xp"], 0)

    def test_file_berisi_list_bukan_dict(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([1, 2, 3], f)
        self.assertEqual(progress.load_progress()["xp"], 0)

    def test_migrasi_dari_skema_lama(self):
        lama = {
            "materi_dibaca": ["java_materi::A"],
            "kuis_skor": {"java_kuis::K": {"terbaik": 3}},
            "latihan_dilihat": [],
        }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(lama, f)

        data = progress.load_progress()
        self.assertEqual(data["versi"], progress.VERSI_DATA)
        self.assertIn("bookmark", data)
        self.assertIn("latihan_lulus", data)
        self.assertEqual(data["kuis_skor"]["java_kuis::K"]["total_soal"], 0)
        self.assertEqual(data["materi_dibaca"], ["java_materi::A"])

    def test_penulisan_atomik_tidak_meninggalkan_sampah(self):
        progress.save_progress(progress.load_progress())
        sisa = [f for f in os.listdir(self.dir.name) if f.endswith(".tmp")]
        self.assertEqual(sisa, [])


class TestPencatatan(BasisProgres):
    def test_materi_dicatat_sekali_saja(self):
        progress.record_material_read("java_materi", "Topik A")
        progress.record_material_read("java_materi", "Topik A")
        data = progress.load_progress()
        self.assertEqual(data["materi_dibaca"].count("java_materi::Topik A"), 1)
        self.assertEqual(data["xp"], progress.XP_MATERI)

    def test_xp_bertambah_per_materi_baru(self):
        progress.record_material_read("java_materi", "A")
        progress.record_material_read("java_materi", "B")
        self.assertEqual(progress.load_progress()["xp"], progress.XP_MATERI * 2)

    def test_skor_kuis_menyimpan_yang_terbaik(self):
        progress.record_quiz_score("go_kuis", "K1", 5, 10)
        progress.record_quiz_score("go_kuis", "K1", 8, 10)
        progress.record_quiz_score("go_kuis", "K1", 6, 10)

        info = progress.load_progress()["kuis_skor"]["go_kuis::K1"]
        self.assertEqual(info["terbaik"], 8)
        self.assertEqual(info["percobaan"], 3)
        self.assertEqual(info["terakhir_skor"], 6)

    def test_bonus_xp_untuk_nilai_sempurna(self):
        progress.record_quiz_score("go_kuis", "K1", 10, 10)
        harapan = 10 * progress.XP_PER_JAWABAN_BENAR + progress.XP_BONUS_KUIS_SEMPURNA
        self.assertEqual(progress.load_progress()["xp"], harapan)

    def test_soal_salah_dicatat_lalu_dibersihkan(self):
        progress.record_quiz_score("go_kuis", "K1", 7, 10, salah_index=[2, 5, 9])
        self.assertEqual(progress.soal_salah_terakhir("go_kuis", "K1"), [2, 5, 9])

        progress.record_quiz_score("go_kuis", "K1", 10, 10, salah_index=[])
        self.assertEqual(progress.soal_salah_terakhir("go_kuis", "K1"), [])

    def test_latihan_lulus_dicatat_terpisah_dari_dilihat(self):
        progress.record_exercise_viewed("go_latihan", "L1")
        data = progress.load_progress()
        self.assertIn("go_latihan::L1", data["latihan_dilihat"])
        self.assertNotIn("go_latihan::L1", data["latihan_lulus"])

        progress.record_exercise_passed("go_latihan", "L1")
        data = progress.load_progress()
        self.assertIn("go_latihan::L1", data["latihan_lulus"])

    def test_riwayat_terakhir_diperbarui(self):
        progress.record_material_read("bash_materi", "Judul X")
        terakhir = progress.load_progress()["terakhir"]
        self.assertEqual(terakhir["tipe"], "materi")
        self.assertEqual(terakhir["kategori"], "bash_materi")
        self.assertEqual(terakhir["judul"], "Judul X")


class TestLevelDanXP(unittest.TestCase):
    def test_level_satu_saat_belum_ada_xp(self):
        self.assertEqual(progress.level_dari_xp(0), 1)

    def test_level_naik_seiring_xp(self):
        self.assertLess(progress.level_dari_xp(100), progress.level_dari_xp(10_000))

    def test_level_tidak_pernah_turun(self):
        sebelum = 1
        for xp in range(0, 20_000, 250):
            sekarang = progress.level_dari_xp(xp)
            self.assertGreaterEqual(sekarang, sebelum)
            sebelum = sekarang

    def test_info_level_konsisten(self):
        for xp in (0, 49, 50, 500, 5000, 50_000):
            level, di_level, butuh = progress.info_level(xp)
            with self.subTest(xp=xp):
                self.assertGreaterEqual(di_level, 0)
                self.assertGreater(butuh, 0)
                self.assertLessEqual(di_level, butuh)
                self.assertEqual(level, progress.level_dari_xp(xp))

    def test_gelar_naik_bertahap(self):
        self.assertEqual(progress.gelar_dari_level(1), "Pemula")
        self.assertEqual(progress.gelar_dari_level(100), "Mahaguru")


class TestStreak(BasisProgres):
    def test_hari_pertama_mulai_dari_satu(self):
        data = progress.catat_aktivitas(progress.load_progress())
        self.assertEqual(data["streak"]["beruntun"], 1)
        self.assertEqual(data["streak"]["total_hari"], 1)

    def test_dua_aktivitas_di_hari_sama_tidak_menambah(self):
        data = progress.catat_aktivitas(progress.load_progress())
        data = progress.catat_aktivitas(data)
        self.assertEqual(data["streak"]["beruntun"], 1)
        self.assertEqual(data["streak"]["total_hari"], 1)

    def test_hari_berurutan_menambah_streak(self):
        data = progress.load_progress()
        kemarin = (date.today() - timedelta(days=1)).isoformat()
        data["streak"] = {"tanggal_terakhir": kemarin, "beruntun": 4,
                          "terpanjang": 4, "total_hari": 4}
        data = progress.catat_aktivitas(data)
        self.assertEqual(data["streak"]["beruntun"], 5)
        self.assertEqual(data["streak"]["terpanjang"], 5)

    def test_bolong_sehari_mereset_streak(self):
        data = progress.load_progress()
        lama = (date.today() - timedelta(days=3)).isoformat()
        data["streak"] = {"tanggal_terakhir": lama, "beruntun": 9,
                          "terpanjang": 9, "total_hari": 9}
        data = progress.catat_aktivitas(data)
        self.assertEqual(data["streak"]["beruntun"], 1)
        self.assertEqual(data["streak"]["terpanjang"], 9, "rekor harus tetap tersimpan")

    def test_tanggal_rusak_tidak_bikin_crash(self):
        data = progress.load_progress()
        data["streak"]["tanggal_terakhir"] = "bukan-tanggal"
        data = progress.catat_aktivitas(data)
        self.assertEqual(data["streak"]["beruntun"], 1)


class TestBadge(BasisProgres):
    def test_badge_pertama_terbuka(self):
        baru = progress.record_material_read("java_materi", "A")
        ids = [b[0] for b in baru]
        self.assertIn("langkah_pertama", ids)

    def test_badge_tidak_diberikan_dua_kali(self):
        progress.record_material_read("java_materi", "A")
        baru = progress.record_material_read("java_materi", "B")
        self.assertNotIn("langkah_pertama", [b[0] for b in baru])

    def test_badge_poliglot_butuh_tiga_bahasa(self):
        progress.record_material_read("java_materi", "A")
        progress.record_material_read("go_materi", "B")
        self.assertNotIn("poliglot", progress.load_progress()["badge"])

        progress.record_material_read("bash_materi", "C")
        self.assertIn("poliglot", progress.load_progress()["badge"])

    def test_semua_badge_punya_pengecek_yang_jalan(self):
        data = progress.load_progress()
        for bid, nama, deskripsi, syarat in progress.DAFTAR_BADGE:
            with self.subTest(badge=bid):
                self.assertIsInstance(nama, str)
                self.assertIsInstance(deskripsi, str)
                self.assertIsInstance(syarat(data), bool)

    def test_id_badge_unik(self):
        ids = [b[0] for b in progress.DAFTAR_BADGE]
        self.assertEqual(len(ids), len(set(ids)))


class TestBookmark(BasisProgres):
    def test_toggle_menambah_lalu_menghapus(self):
        self.assertTrue(progress.toggle_bookmark("java_materi", "A"))
        self.assertTrue(progress.is_bookmarked("java_materi", "A"))

        self.assertFalse(progress.toggle_bookmark("java_materi", "A"))
        self.assertFalse(progress.is_bookmarked("java_materi", "A"))

    def test_daftar_bookmark(self):
        progress.toggle_bookmark("java_materi", "A")
        progress.toggle_bookmark("go_materi", "B")
        self.assertEqual(len(progress.daftar_bookmark()), 2)


class TestJadwalUlang(BasisProgres):
    def test_kuis_belum_dikerjakan_bukan_jatuh_tempo(self):
        data = progress.load_progress()
        self.assertFalse(progress.kuis_jatuh_tempo(data, "go_kuis", "Belum Pernah"))

    def test_skor_bagus_menjadwalkan_lebih_jauh(self):
        progress.record_quiz_score("go_kuis", "Bagus", 10, 10)
        progress.record_quiz_score("go_kuis", "Jelek", 2, 10)

        data = progress.load_progress()
        jauh = data["jadwal_kuis"]["go_kuis::Bagus"]["interval"]
        dekat = data["jadwal_kuis"]["go_kuis::Jelek"]["interval"]
        self.assertGreater(jauh, dekat)

    def test_belum_jatuh_tempo_setelah_baru_dikerjakan(self):
        progress.record_quiz_score("go_kuis", "K", 10, 10)
        data = progress.load_progress()
        self.assertFalse(progress.kuis_jatuh_tempo(data, "go_kuis", "K"))

    def test_jatuh_tempo_kalau_tanggalnya_sudah_lewat(self):
        progress.record_quiz_score("go_kuis", "K", 10, 10)
        data = progress.load_progress()
        data["jadwal_kuis"]["go_kuis::K"]["jatuh_tempo"] = (
            date.today() - timedelta(days=1)
        ).isoformat()
        progress.save_progress(data)

        data = progress.load_progress()
        self.assertTrue(progress.kuis_jatuh_tempo(data, "go_kuis", "K"))

    def test_interval_tidak_tumbuh_tanpa_batas(self):
        for _ in range(30):
            progress.record_quiz_score("go_kuis", "K", 10, 10)
        interval = progress.load_progress()["jadwal_kuis"]["go_kuis::K"]["interval"]
        self.assertLessEqual(interval, 120)


class TestStatistik(BasisProgres):
    def test_menghitung_per_bahasa(self):
        progress.record_material_read("go_materi", "A")
        progress.record_material_read("go_materi", "B")
        progress.record_material_read("java_materi", "X")
        progress.record_quiz_score("go_kuis", "K", 8, 10)
        progress.record_exercise_passed("go_latihan", "L")

        data = progress.load_progress()
        s = progress.statistik_bahasa(data, "go", 10, 5, 8)

        self.assertEqual(s["materi"], 2)
        self.assertEqual(s["kuis"], 1)
        self.assertEqual(s["latihan_lulus"], 1)
        self.assertEqual(s["skor"], 8)
        self.assertEqual(s["skor_maks"], 10)

    def test_prefix_tidak_bocor_antar_bahasa(self):
        progress.record_material_read("java_materi", "A")
        data = progress.load_progress()
        s = progress.statistik_bahasa(data, "javascript", 10, 5, 8)
        self.assertEqual(s["materi"], 0, "prefix 'java' tidak boleh cocok 'javascript'")


class TestTahanBantingTerhadapDataRusak(BasisProgres):
    """Kontrak modul: berkas rusak TIDAK BOLEH menghentikan aplikasi.

    Versi lama hanya menangkap kegagalan PARSING. Berkas yang berhasil diurai
    tapi salah tipe (entri kuis berupa angka, streak berupa string) membuat
    aplikasi melempar AttributeError di setiap peluncuran, dan pengguna tidak
    punya cara memperbaikinya dari dalam aplikasi.
    """

    RUSAK = [
        '{"versi": 2, "kuis_skor": []}',
        '{"versi": 2, "kuis_skor": {"java_kuis::A": 5}}',
        '{"versi": 2, "kuis_skor": {"java_kuis::A": null}}',
        '{"streak": "kemarin"}',
        '{"streak": null}',
        '{"streak": {"beruntun": "banyak", "tanggal_terakhir": 12345}}',
        '{"badge": "kosong"}',
        '{"materi_dibaca": "bukan list"}',
        '{"materi_dibaca": [1, 2, {"a": 1}]}',
        '{"xp": "banyak"}',
        '{"xp": -500}',
        '{"bookmark": {"a": 1}}',
        '{"jadwal_kuis": {"x": "besok"}}',
        '{"salah_kuis": {"x": "bukan list"}}',
        '{"riwayat_harian": {"2026-01-01": 5}}',
        '{"terakhir": "materi terakhir"}',
    ]

    def test_semua_bentuk_rusak_dimuat_tanpa_exception(self):
        for isi in self.RUSAK:
            with self.subTest(isi=isi[:45]):
                with open(self.path, "w", encoding="utf-8") as f:
                    f.write(isi)
                data = progress.load_progress()
                self.assertIsInstance(data, dict)
                self.assertIsInstance(data["kuis_skor"], dict)
                self.assertIsInstance(data["streak"], dict)
                self.assertIsInstance(data["badge"], list)
                self.assertIsInstance(data["xp"], int)
                self.assertGreaterEqual(data["xp"], 0)

    def test_operasi_lanjutan_tetap_aman_setelah_dimuat(self):
        for isi in self.RUSAK:
            with self.subTest(isi=isi[:45]):
                with open(self.path, "w", encoding="utf-8") as f:
                    f.write(isi)
                data = progress.load_progress()
                progress.catat_aktivitas(data)
                progress.cek_badge_baru(data)
                progress.streak_aktif(data)
                progress.riwayat_harian(data, 7)
                progress.statistik_bahasa(data, "java", 10, 5, 8)
                progress.save_progress(data)

    def test_data_sah_tidak_ikut_terbuang(self):
        with open(self.path, "w", encoding="utf-8") as f:
            f.write('{"materi_dibaca": ["java_materi::A"], "kuis_skor": [], "xp": 40}')
        data = progress.load_progress()
        self.assertEqual(data["materi_dibaca"], ["java_materi::A"])
        self.assertEqual(data["xp"], 40)


class TestSesiKuisParsial(BasisProgres):
    def test_penyebut_tidak_menyusut(self):
        progress.record_quiz_score("java_kuis", "K", 7, 10, [1, 3, 5])
        progress.record_quiz_score("java_kuis", "K", 3, 3, [], sesi_penuh=False)
        info = progress.load_progress()["kuis_skor"]["java_kuis::K"]
        self.assertEqual(info["total_soal"], 10)
        self.assertEqual(info["terbaik"], 7)

    def test_sesi_parsial_tidak_menambah_xp(self):
        progress.record_quiz_score("java_kuis", "K", 7, 10, [1, 3, 5])
        xp = progress.load_progress()["xp"]
        for _ in range(5):
            progress.record_quiz_score("java_kuis", "K", 3, 3, [], sesi_penuh=False)
        self.assertEqual(progress.load_progress()["xp"], xp)

    def test_sesi_parsial_tidak_menambah_percobaan(self):
        progress.record_quiz_score("java_kuis", "K", 7, 10)
        progress.record_quiz_score("java_kuis", "K", 3, 3, sesi_penuh=False)
        self.assertEqual(
            progress.load_progress()["kuis_skor"]["java_kuis::K"]["percobaan"], 1)

    def test_sesi_parsial_tidak_menggeser_jadwal(self):
        progress.record_quiz_score("java_kuis", "K", 10, 10)
        jadwal = dict(progress.load_progress()["jadwal_kuis"]["java_kuis::K"])
        for _ in range(5):
            progress.record_quiz_score("java_kuis", "K", 1, 1, sesi_penuh=False)
        self.assertEqual(progress.load_progress()["jadwal_kuis"]["java_kuis::K"], jadwal)

    def test_perbarui_soal_salah_hanya_menyentuh_daftar_salah(self):
        progress.record_quiz_score("java_kuis", "K", 7, 10, [1, 3, 5])
        progress.perbarui_soal_salah("java_kuis", "K", [3])
        self.assertEqual(progress.soal_salah_terakhir("java_kuis", "K"), [3])
        info = progress.load_progress()["kuis_skor"]["java_kuis::K"]
        self.assertEqual((info["terbaik"], info["total_soal"]), (7, 10))

    def test_terbaik_tidak_pernah_melebihi_total_soal(self):
        progress.record_quiz_score("go_kuis", "K", 5, 5)
        progress.record_quiz_score("go_kuis", "K", 2, 2, sesi_penuh=False)
        info = progress.load_progress()["kuis_skor"]["go_kuis::K"]
        self.assertLessEqual(info["terbaik"], info["total_soal"])


class TestStreakAktif(BasisProgres):
    def test_aktivitas_hari_ini(self):
        progress.record_material_read("java_materi", "A")
        self.assertGreaterEqual(progress.streak_aktif(progress.load_progress()), 1)

    def test_streak_lama_dilaporkan_nol(self):
        """Regresi: dashboard dulu memamerkan streak 40 hari yang sudah putus."""
        data = progress.load_progress()
        data["streak"] = {"tanggal_terakhir": "2020-01-01", "beruntun": 40,
                          "terpanjang": 40, "total_hari": 40}
        self.assertEqual(progress.streak_aktif(data), 0)

    def test_kemarin_masih_dihitung_aktif(self):
        data = progress.load_progress()
        kemarin = (date.today() - timedelta(days=1)).isoformat()
        data["streak"] = {"tanggal_terakhir": kemarin, "beruntun": 4,
                          "terpanjang": 4, "total_hari": 4}
        self.assertEqual(progress.streak_aktif(data), 4)

    def test_tanggal_rusak_dilaporkan_nol(self):
        data = progress.load_progress()
        data["streak"]["tanggal_terakhir"] = "bukan-tanggal"
        self.assertEqual(progress.streak_aktif(data), 0)

    def test_belum_pernah_belajar(self):
        self.assertEqual(progress.streak_aktif(progress.load_progress()), 0)


class TestRiwayatHarian(BasisProgres):
    def test_xp_hari_ini_bertambah(self):
        progress.record_material_read("java_materi", "A")
        self.assertEqual(progress.xp_hari_ini(progress.load_progress()),
                         progress.XP_MATERI)

    def test_panjang_riwayat_sesuai_permintaan(self):
        riwayat = progress.riwayat_harian(progress.load_progress(), 30)
        self.assertEqual(len(riwayat), 30)
        self.assertEqual(riwayat[-1][0], date.today().isoformat())

    def test_hari_kosong_tetap_muncul_dengan_nol(self):
        riwayat = progress.riwayat_harian(progress.load_progress(), 7)
        self.assertTrue(all(isinstance(x, int) for _, x in riwayat))

    def test_riwayat_tidak_tumbuh_tanpa_batas(self):
        data = progress.load_progress()
        for i in range(500):
            data["riwayat_harian"][f"2020-{(i % 12) + 1:02d}-{(i % 28) + 1:02d}"] = {"xp": 1}
        progress._catat_harian(data, "xp", 1)
        self.assertLessEqual(len(data["riwayat_harian"]), 400)


class TestLatihanManual(BasisProgres):
    def test_menandai_manual_memberi_xp_lebih_kecil(self):
        progress.tandai_latihan_manual("cpp_latihan", "L1")
        data = progress.load_progress()
        self.assertIn("cpp_latihan::L1", data["latihan_manual"])
        self.assertEqual(data["xp"], progress.XP_LATIHAN_MANUAL)

    def test_tidak_dobel_kalau_ditandai_dua_kali(self):
        progress.tandai_latihan_manual("cpp_latihan", "L1")
        progress.tandai_latihan_manual("cpp_latihan", "L1")
        data = progress.load_progress()
        self.assertEqual(data["latihan_manual"].count("cpp_latihan::L1"), 1)
        self.assertEqual(data["xp"], progress.XP_LATIHAN_MANUAL)

    def test_latihan_yang_sudah_lulus_tidak_ditandai_manual(self):
        progress.record_exercise_passed("cpp_latihan", "L1")
        progress.tandai_latihan_manual("cpp_latihan", "L1")
        self.assertEqual(progress.load_progress()["latihan_manual"], [])

    def test_bisa_dibatalkan(self):
        progress.tandai_latihan_manual("cpp_latihan", "L1")
        self.assertTrue(progress.batalkan_latihan_manual("cpp_latihan", "L1"))
        self.assertEqual(progress.load_progress()["latihan_manual"], [])

    def test_ikut_terhitung_di_statistik(self):
        progress.tandai_latihan_manual("cpp_latihan", "L1")
        s = progress.statistik_bahasa(progress.load_progress(), "cpp", 0, 0, 2)
        self.assertEqual(s["latihan_manual"], 1)
        self.assertGreater(s["persen"], 0)


class TestStatistikTahanData(BasisProgres):
    def test_persen_tidak_pernah_melebihi_seratus(self):
        data = progress.load_progress()
        for i in range(50):
            data["materi_dibaca"].append(f"java_materi::M{i}")
        s = progress.statistik_bahasa(data, "java", 5, 2, 2)
        self.assertLessEqual(s["persen"], 100.0)

    def test_penyebut_kuis_diisi_dari_data_kurikulum(self):
        """Progres v1 menyimpan total_soal 0; penyebutnya harus dipulihkan."""
        data = progress.load_progress()
        data["kuis_skor"]["java_kuis::K1"] = {"terbaik": 8, "percobaan": 1,
                                              "total_soal": 0}
        s = progress.statistik_bahasa(data, "java", 0, 1, 0,
                                      soal_per_kuis={"K1": 10})
        self.assertEqual(s["skor_maks"], 10)
        self.assertEqual(s["skor"], 8)

    def test_skor_dijepit_ke_penyebut(self):
        data = progress.load_progress()
        data["kuis_skor"]["java_kuis::K1"] = {"terbaik": 99, "percobaan": 1,
                                              "total_soal": 10}
        s = progress.statistik_bahasa(data, "java", 0, 1, 0)
        self.assertLessEqual(s["skor"], s["skor_maks"])


class TestEksporImporReset(BasisProgres):
    def test_ekspor_lalu_impor_mengembalikan_data_yang_sama(self):
        progress.record_material_read("java_materi", "A")
        progress.record_exercise_passed("go_latihan", "L")
        tujuan = os.path.join(self.dir.name, "backup.json")

        ok, _ = progress.ekspor(tujuan)
        self.assertTrue(ok)

        progress.reset("semua")
        self.assertEqual(progress.load_progress()["xp"], 0)

        ok, _ = progress.impor(tujuan)
        self.assertTrue(ok)
        data = progress.load_progress()
        self.assertIn("java_materi::A", data["materi_dibaca"])
        self.assertIn("go_latihan::L", data["latihan_lulus"])

    def test_impor_berkas_tidak_ada(self):
        ok, pesan = progress.impor(os.path.join(self.dir.name, "hantu.json"))
        self.assertFalse(ok)
        self.assertIn("tidak ditemukan", pesan)

    def test_impor_berkas_rusak_ditolak(self):
        buruk = os.path.join(self.dir.name, "buruk.json")
        with open(buruk, "w", encoding="utf-8") as f:
            f.write("{bukan json")
        ok, _ = progress.impor(buruk)
        self.assertFalse(ok)

    def test_impor_membuat_cadangan(self):
        progress.record_material_read("java_materi", "A")
        tujuan = os.path.join(self.dir.name, "b.json")
        progress.ekspor(tujuan)
        progress.impor(tujuan)
        self.assertTrue(os.path.exists(progress.PROGRESS_FILE + ".bak"))

    def test_reset_satu_bahasa_menyisakan_bahasa_lain(self):
        progress.record_material_read("java_materi", "A")
        progress.record_material_read("go_materi", "B")
        progress.record_quiz_score("java_kuis", "K", 5, 10)
        progress.reset("java")

        data = progress.load_progress()
        self.assertNotIn("java_materi::A", data["materi_dibaca"])
        self.assertIn("go_materi::B", data["materi_dibaca"])
        self.assertNotIn("java_kuis::K", data["kuis_skor"])

    def test_reset_java_tidak_menyentuh_javascript(self):
        progress.record_material_read("javascript_materi", "JS")
        progress.reset("java")
        self.assertIn("javascript_materi::JS",
                      progress.load_progress()["materi_dibaca"])


class TestSimpanGagal(BasisProgres):
    def test_berkas_sementara_dibersihkan_saat_penulisan_gagal(self):
        """Disk penuh tidak boleh meninggalkan tumpukan .progress-*.tmp di home."""
        from unittest import mock as _mock
        data = progress.load_progress()
        with _mock.patch("json.dump", side_effect=OSError(28, "No space left")):
            for _ in range(3):
                self.assertFalse(progress.save_progress(data))
        sisa = [f for f in os.listdir(self.dir.name) if f.endswith(".tmp")]
        self.assertEqual(sisa, [])

    def test_kegagalan_menulis_tidak_melempar(self):
        from unittest import mock as _mock
        data = progress.load_progress()
        with _mock.patch("os.replace", side_effect=OSError("read-only")):
            self.assertFalse(progress.save_progress(data))


class TestBerkasLama(BasisProgres):
    def test_berkas_lama_diturunkan_dari_lokasi_berkas_aktif(self):
        """Override BELAJAR_PROGRESS_FILE tidak boleh membaca progres di home."""
        self.assertTrue(
            progress.PROGRESS_FILE_LAMA.startswith(os.path.dirname(progress.PROGRESS_FILE))
            or progress.PROGRESS_FILE_LAMA == os.path.join(self.dir.name, "tidak-ada.json")
        )



if __name__ == "__main__":
    unittest.main(verbosity=2)
