"""Preferensi pengguna yang bertahan antar sesi.

Dipisah dari `progress.py` dengan sengaja. Progres belajar adalah CATATAN
PENCAPAIAN -- kehilangannya menyakitkan. Konfigurasi cuma preferensi tampilan;
kehilangannya paling-paling bikin warnanya balik ke bawaan. Menyimpannya di
berkas yang sama berarti satu kesalahan tulis bisa merusak keduanya sekaligus.

Setiap pengaturan dideklarasikan sekali di `SKEMA`, lengkap dengan tipe,
rentang, dan penjelasannya. Menu pengaturan dibangun otomatis dari deklarasi
itu, jadi menambah opsi baru cukup menambah satu entri -- tidak perlu menyentuh
kode antarmuka sama sekali.

Importir: utils.py (lebar & tinggi halaman), main.py (menu pengaturan),
quiz.py (detik per soal), exercises.py (editor & konfirmasi jawaban),
bab.py (saklar buka semua bab).
Berkas data: ~/.belajar_ngoding_config.json, override lewat BELAJAR_CONFIG_FILE.
"""

import json
import os
import tempfile

import tema

VERSI_KONFIG = 1

BERKAS = os.environ.get(
    "BELAJAR_CONFIG_FILE",
    os.path.join(os.path.expanduser("~"), ".belajar_ngoding_config.json"),
)


class Opsi:
    """Satu pengaturan: bawaan, cara memvalidasi, dan cara menampilkannya."""

    __slots__ = ("kunci", "label", "jenis", "bawaan", "pilihan", "minimum",
                 "maksimum", "keterangan")

    def __init__(self, kunci, label, jenis, bawaan, pilihan=None, minimum=None,
                 maksimum=None, keterangan=""):
        self.kunci = kunci
        self.label = label
        self.jenis = jenis            # "pilihan" | "angka" | "sakelar" | "teks"
        self.bawaan = bawaan
        self.pilihan = pilihan or []  # [(nilai, label_tampil)]
        self.minimum = minimum
        self.maksimum = maksimum
        self.keterangan = keterangan

    def bersihkan(self, nilai):
        """Kembalikan nilai yang pasti sah. Nilai ngawur diganti bawaan."""
        if self.jenis == "sakelar":
            return bool(nilai)
        if self.jenis == "angka":
            try:
                angka = int(nilai)
            except (TypeError, ValueError):
                return self.bawaan
            # 0 selalu berarti "otomatis" dan lolos dari batas bawah.
            if self.minimum is not None and angka != 0 and angka < self.minimum:
                return self.minimum
            if self.maksimum is not None and angka > self.maksimum:
                return self.maksimum
            return angka
        if self.jenis == "pilihan":
            sah = [n for n, _ in self.pilihan]
            return nilai if nilai in sah else self.bawaan
        return str(nilai) if nilai is not None else self.bawaan

    def tampil(self, nilai):
        if self.jenis == "sakelar":
            return "nyala" if nilai else "mati"
        if self.jenis == "pilihan":
            for n, label in self.pilihan:
                if n == nilai:
                    return label
            return str(nilai)
        if self.jenis == "angka" and nilai == 0:
            return "otomatis"
        return str(nilai) if str(nilai) else "(kosong)"


SKEMA = [
    Opsi("tema", "Tema warna", "pilihan", "gelap",
         pilihan=[(n, f"{n} - {ket}") for n, ket, _ in tema.daftar_tema()],
         keterangan="Palet warna seluruh aplikasi."),
    Opsi("warna", "Kedalaman warna", "pilihan", "auto",
         pilihan=[("auto", "auto - ikuti kemampuan terminal"),
                  ("mati", "mati - tanpa warna sama sekali"),
                  ("16", "16 warna - terminal jadul"),
                  ("256", "256 warna"),
                  ("penuh", "16 juta warna (truecolor)")],
         keterangan="Paksa kedalaman warna kalau deteksi otomatis meleset."),
    Opsi("lebar", "Lebar layar", "angka", 0, minimum=52, maksimum=140,
         keterangan="0 = ikuti lebar terminal. Isi angka untuk menguncinya."),
    Opsi("tinggi_halaman", "Baris per halaman materi", "angka", 0,
         minimum=8, maksimum=80,
         keterangan="0 = ikuti tinggi terminal."),
    Opsi("sorot_sintaks", "Sorot sintaks pada contoh kode", "sakelar", True,
         keterangan="Warnai kata kunci, string, dan komentar di contoh kode."),
    Opsi("detik_per_soal", "Detik per soal di mode timer", "angka", 25,
         minimum=5, maksimum=300,
         keterangan="Batas waktu menjawab saat kuis mode timer."),
    Opsi("acak_bawaan", "Acak soal & opsi secara bawaan", "sakelar", True,
         keterangan="Mematikannya membuat kuis selalu urut seperti di materi."),
    Opsi("target_xp_harian", "Target XP harian", "angka", 60,
         minimum=10, maksimum=1000,
         keterangan="Dipakai untuk bar target harian di dashboard."),
    Opsi("editor", "Editor teks", "teks", "",
         keterangan="Kosongkan untuk memakai $EDITOR / $VISUAL / nano."),
    Opsi("konfirmasi_jawaban", "Tanya dulu sebelum menampilkan jawaban", "sakelar", True,
         keterangan="Mencegah tidak sengaja membuka solusi."),
    Opsi("buka_semua_bab", "Buka semua bab tanpa syarat", "sakelar", False,
         keterangan="Matikan penguncian bertahap. Untuk yang sudah pernah "
                    "belajar bahasanya dan cuma ingin melompat."),
    Opsi("nama", "Nama panggilan", "teks", "",
         keterangan="Dipakai di sapaan dan laporan kemajuan."),
]

_PETA = {o.kunci: o for o in SKEMA}
_data = None


# --------------------------------------------------------------- muat/simpan

def _bawaan():
    return {o.kunci: o.bawaan for o in SKEMA}


def muat(paksa=False):
    """Baca konfigurasi (dengan cache). Selalu berhasil, apa pun isi berkasnya."""
    global _data
    if _data is not None and not paksa:
        return _data

    nilai = _bawaan()
    try:
        with open(BERKAS, "r", encoding="utf-8") as f:
            mentah = json.load(f)
        if isinstance(mentah, dict):
            for kunci, opsi_ in _PETA.items():
                if kunci in mentah:
                    nilai[kunci] = opsi_.bersihkan(mentah[kunci])
    except (OSError, json.JSONDecodeError, ValueError):
        pass  # berkas belum ada atau rusak -> pakai bawaan

    nilai["versi"] = VERSI_KONFIG
    _data = nilai
    return _data


def simpan(nilai=None):
    """Tulis konfigurasi secara atomik. Gagal menulis tidak menghentikan apa pun."""
    global _data
    if nilai is not None:
        _data = nilai
    if _data is None:
        return False
    try:
        folder = os.path.dirname(BERKAS) or "."
        os.makedirs(folder, exist_ok=True)
        fd, sementara = tempfile.mkstemp(dir=folder, prefix=".konfig-", suffix=".tmp")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(_data, f, indent=2, ensure_ascii=False, sort_keys=True)
        os.replace(sementara, BERKAS)
        return True
    except OSError:
        return False


def ambil(kunci, cadangan=None):
    nilai = muat()
    if kunci in nilai:
        return nilai[kunci]
    o = _PETA.get(kunci)
    return o.bawaan if o else cadangan


def pasang(kunci, nilai, langsung_simpan=True):
    """Ubah satu pengaturan (nilainya dibersihkan dulu) lalu terapkan."""
    o = _PETA.get(kunci)
    if o is None:
        return False
    data = muat()
    data[kunci] = o.bersihkan(nilai)
    if langsung_simpan:
        simpan(data)
    terapkan()
    return True


def kembalikan_bawaan():
    global _data
    _data = _bawaan()
    _data["versi"] = VERSI_KONFIG
    simpan(_data)
    terapkan()


def lupakan_cache():
    """Buang cache di memori. Dipakai pengujian yang mengganti lokasi berkas."""
    global _data
    _data = None


# ------------------------------------------------------------------ terapkan

_PETA_KEDALAMAN = {
    "mati": tema.TANPA_WARNA,
    "16": tema.WARNA_16,
    "256": tema.WARNA_256,
    "penuh": tema.WARNA_PENUH,
}


def terapkan():
    """Hidupkan pengaturan yang berpengaruh ke modul lain (warna & tema).

    Lebar layar TIDAK dipasang di sini: `utils.lebar()` membacanya langsung
    setiap kali dipakai supaya mengubah ukuran jendela terminal langsung terasa
    tanpa perlu keluar-masuk menu.
    """
    data = muat()
    tema.pakai_tema(data.get("tema", "gelap"))

    pilihan_warna = data.get("warna", "auto")
    if pilihan_warna == "auto":
        tema.pakai_kedalaman(tema.deteksi_kedalaman())
    else:
        tema.pakai_kedalaman(_PETA_KEDALAMAN.get(pilihan_warna, tema.deteksi_kedalaman()))


def opsi(kunci):
    return _PETA.get(kunci)


def daftar_opsi():
    return list(SKEMA)
