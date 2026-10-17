"""Menjawab pertanyaan "habis ini ngapain?".

Aplikasi ini menyimpan 190 materi, 67 kuis, dan 159 latihan di sebelas bahasa.
Untuk orang yang baru mulai, daftar sepanjang itu bukan kekayaan -- itu
kelumpuhan. Dulu satu-satunya penunjuk arah adalah "lanjutkan dari terakhir",
yang justru membuka ulang hal yang BARU SAJA selesai dikerjakan.

Modul ini menyusun antrean langkah berikutnya dengan urutan prioritas yang
mencerminkan cara belajar yang efektif:

0. Kalau yang terakhir dikerjakan adalah membaca: bacaan itu, atau materi
   sesudahnya -- "lanjutkan" berarti melanjutkan.
1. Kuis yang jatuh tempo diulang, paling banyak dua -- ingatan yang mau luruh
   diselamatkan dulu, tanpa menenggelamkan semua yang lain.
2. Materi yang berhenti di tengah -- tutup dulu yang menggantung.
3. Materi berikutnya di bahasa yang sedang dikerjakan -- jaga momentum.
4. Latihan yang macet (dibuka, belum lulus), atau latihan berikutnya.
5. Kuis pertama untuk materi yang sudah dibaca -- uji pemahaman.
6. Bahasa berikutnya -- menambah lebar hanya setelah ada kedalaman.

Materi yang babnya masih terkunci tidak pernah muncul di antrean ini. Saran
yang menunjuk pintu terkunci adalah kegagalan terburuk yang bisa dilakukan
fitur ini: aplikasi menyuruh mengerjakan sesuatu, lalu menolak membukanya --
dan yang membacanya tidak punya cara tahu mana dari dua kalimat itu yang
benar. Kuis dan latihan sengaja TIDAK ikut disaring; keduanya memang tidak
pernah dikunci (lihat bab.py).

Semua murni fungsi baca; tidak ada yang disimpan dari sini.

Importir: main.py. Hanya membaca dict progres dari progress.load_progress().
"""

import hashlib
from datetime import date

from inti import runner
from pelajar import bab
from pelajar import kuis_materi
from pelajar.progress import judul_kunci, kunci, kuis_jatuh_tempo, xp_hari_ini


class Langkah:
    """Satu saran konkret yang bisa langsung dibuka dari menu."""

    __slots__ = ("tipe", "lang", "obj", "judul", "alasan", "prioritas")

    def __init__(self, tipe, lang, obj, alasan, prioritas):
        self.tipe = tipe            # "materi" | "kuis" | "latihan"
        self.lang = lang
        self.obj = obj
        self.judul = obj["title"]
        self.alasan = alasan
        self.prioritas = prioritas

    def label(self):
        return f"{self.lang['label']} - {self.judul}"


def _bahasa_terakhir(languages, data):
    """Bahasa yang paling terakhir disentuh, atau None."""
    kategori = (data.get("terakhir") or {}).get("kategori", "")
    if "_" not in kategori:
        return None
    key = kategori.rsplit("_", 1)[0]
    return next((l for l in languages if l["key"] == key), None)


def _urut_bahasa(languages, data):
    """Bahasa aktif lebih dulu, sisanya mengikuti urutan aslinya."""
    aktif = _bahasa_terakhir(languages, data)
    if not aktif:
        return list(languages)
    return [aktif] + [l for l in languages if l is not aktif]


def _sudah(data, kategori, judul, bidang):
    return kunci(kategori, judul) in data.get(bidang, [])


def _materi_terbuka(lang, data, singgahan):
    """Himpunan indeks materi bahasa ini yang boleh dibuka sekarang.

    Disinggahi per bahasa karena `bab.indeks_terbuka()` menyusun ulang status
    seluruh bab tiap kali dipanggil, sedangkan satu daftar saran menyentuh
    bahasa yang sama sampai tiga kali.

    `buka_semua` sengaja tidak diisi. Setelan "buka semua bab" hanya dibaca di
    bab.py; begitu ada tempat kedua yang menafsirkannya, saran dan daftar
    materi bisa berbeda pendapat tentang materi yang sama.
    """
    key = lang["key"]
    if key not in singgahan:
        singgahan[key] = bab.indeks_terbuka(lang, data)
    return singgahan[key]


def langkah_berikutnya(languages, data, maks=6):
    """Daftar saran langkah berikutnya, paling mendesak lebih dulu."""
    if not languages:
        return []

    saran = []
    urutan = _urut_bahasa(languages, data)
    bahasa_aktif = urutan[0]
    singgahan = {}          # status bab per bahasa, dihitung sekali seperlunya

    # Kalau yang terakhir dikerjakan adalah MEMBACA, lanjutkan bacaannya dulu.
    # Persona audit 2026-10-17 menekan "Lanjutkan belajar" sesudah membaca
    # materi Python 19 dan malah dibukakan Kuis SQL 1: empat kuis ulang yang
    # jatuh tempo menyerobot di depan. Kata "lanjutkan" harus berarti
    # melanjutkan apa yang sedang dikerjakan.
    lanjut_baca = (data.get("terakhir") or {}).get("tipe") == "materi"

    # 1. Kuis jatuh tempo -- lintas bahasa, karena lupa tidak kenal bahasa.
    # Paling banyak DUA: semua kuis jatuh tempo dulu berprioritas 1 tanpa batas,
    # jadi enam di antaranya cukup untuk menghapus materi berikutnya dari
    # antrean. Bahasa yang sedang dipelajari dulu, lalu skor terburuk.
    jatuh = []
    for lang in languages:
        kat = f"{lang['key']}_kuis"
        for q in lang["quizzes"]:
            if kuis_jatuh_tempo(data, kat, q["title"]):
                info = data["kuis_skor"].get(kunci(kat, q["title"]), {})
                rasio = info.get("terbaik", 0) / max(info.get("total_soal", 0)
                                                     or len(q["questions"]), 1)
                jatuh.append((lang is not bahasa_aktif, rasio, lang, q))
    jatuh.sort(key=lambda x: (x[0], x[1]))
    for _, _, lang, q in jatuh[:2]:
        saran.append(Langkah("kuis", lang, q,
                             "sudah waktunya diulang biar tidak lupa", 1))

    # 2. Materi yang berhenti di tengah.
    for lang in urutan:
        kat = f"{lang['key']}_materi"
        boleh = _materi_terbuka(lang, data, singgahan)
        for i, m in enumerate(lang["materials"]):
            # Materi setengah jalan di bab terkunci bukan keadaan mustahil:
            # saklar "buka semua bab" dinyalakan, sebuah materi jauh di depan
            # dibuka lalu ditinggal sebelum tuntas -- sehingga babnya tetap nol
            # selesai -- lalu saklarnya dimatikan lagi. Sesudah itu antrean
            # inilah yang pertama kali menawarkannya kembali.
            if i in boleh and _sudah(data, kat, m["title"], "materi_sebagian"):
                # Bukan "kemarin": tidak ada satu pun tanggal yang diperiksa di
                # sini. Materi yang baru dibuka lima menit lalu masuk kategori
                # yang sama, dan menyebutnya "kemarin" adalah aplikasi yang
                # mengaku tahu sesuatu tentang pemakainya padahal tidak.
                terakhir = data.get("terakhir") or {}
                yang_terakhir = (lanjut_baca and terakhir.get("kategori") == kat
                                 and judul_kunci(terakhir.get("judul", "")) ==
                                 judul_kunci(m["title"]))
                saran.append(Langkah("materi", lang, m,
                                     "dibuka tapi belum tuntas dibaca",
                                     0 if yang_terakhir else 2))

    kat_m = f"{bahasa_aktif['key']}_materi"
    kat_k = f"{bahasa_aktif['key']}_kuis"
    kat_l = f"{bahasa_aktif['key']}_latihan"

    # 3. Materi berikutnya di bahasa yang sedang dikerjakan.
    boleh_aktif = _materi_terbuka(bahasa_aktif, data, singgahan)
    berikut = next((m for i, m in enumerate(bahasa_aktif["materials"])
                    if i in boleh_aktif
                    and not _sudah(data, kat_m, m["title"], "materi_dibaca")), None)
    if berikut:
        saran.append(Langkah("materi", bahasa_aktif, berikut,
                             "materi berikutnya di bahasa yang sedang kamu pelajari",
                             0 if lanjut_baca else 3))

    # 4. Latihan yang belum tuntas. Yang sudah pernah DIBUKA tapi belum lulus
    # didahulukan: itu latihan yang sedang macet, dan macet yang ditinggal
    # diam-diam paling sering jadi alasan orang berhenti.
    belum = [e for e in bahasa_aktif["exercises"]
             if not _sudah(data, kat_l, e["title"], "latihan_lulus")
             and not _sudah(data, kat_l, e["title"], "latihan_manual")]
    macet = next((e for e in belum
                  if _sudah(data, kat_l, e["title"], "latihan_dilihat")), None)
    if macet:
        saran.append(Langkah("latihan", bahasa_aktif, macet,
                             "sudah kamu buka tapi belum lulus, coba lagi", 4))
    elif belum:
        saran.append(Langkah("latihan", bahasa_aktif, belum[0],
                             "ubah yang sudah dibaca jadi kode beneran", 4))

    # 5. Kuis yang belum pernah dikerjakan DAN semua materi yang diujinya
    # sudah dibaca. Alasan lama ("uji pemahamanmu atas materi tadi") dulu
    # ditempel ke kuis pertama yang belum dikerjakan, termasuk sesudah
    # membaca satu materi saja: kalimat yang mengaku tahu sesuatu padahal
    # tidak. Kuis yang belum siap tetap bisa dibuka dari daftarnya.
    kuis = next((q for q in bahasa_aktif["quizzes"]
                 if kunci(kat_k, q["title"]) not in data.get("kuis_skor", {})
                 and kuis_materi.kuis_siap(bahasa_aktif, q, data)), None)
    if kuis:
        saran.append(Langkah("kuis", bahasa_aktif, kuis,
                             "semua materi yang diujinya sudah kamu baca", 5))

    # 6. Bahasa yang belum pernah disentuh sama sekali.
    for lang in languages:
        kat = f"{lang['key']}_materi"
        tersentuh = any(_sudah(data, kat, m["title"], "materi_dibaca")
                        or _sudah(data, kat, m["title"], "materi_sebagian")
                        for m in lang["materials"])
        if tersentuh:
            continue
        # Bab pertama selalu terbuka, jadi materi pertama praktis selalu lolos.
        # Yang disaring di sini bahasa yang belum punya materi sama sekali:
        # tanpa ini, satu-satunya slot "bahasa baru" habis untuk sesuatu yang
        # tidak bisa dibuka, dan bahasa berikutnya tidak pernah ditawarkan.
        boleh = _materi_terbuka(lang, data, singgahan)
        pertama = next(
            (m for i, m in enumerate(lang["materials"]) if i in boleh), None)
        if pertama is None:
            continue
        saran.append(Langkah("materi", lang, pertama,
                             f"mulai bahasa baru: {lang['label']}", 6))
        break

    saran.sort(key=lambda s: s.prioritas)

    # Jangan menyarankan hal yang sama dua kali lewat jalur berbeda.
    terlihat = set()
    unik = []
    for s in saran:
        tanda = (s.lang["key"], s.tipe, s.judul)
        if tanda in terlihat:
            continue
        terlihat.add(tanda)
        unik.append(s)
    return unik[:maks]


# ------------------------------------------------------------ tantangan harian

def _benih_hari(hari=None):
    """Angka yang tetap sepanjang hari tapi berubah tiap hari.

    Sengaja bukan random: tantangannya harus sama kalau aplikasi dibuka dua
    kali di hari yang sama, dan berbeda besok.
    """
    hari = hari or date.today()
    return hari.toordinal()


# Urutan tingkat latihan, dari yang paling ringan. Sama dengan TINGKAT_URUT di
# tests/test_data.py, yang menjaga bahwa hanya empat nilai ini yang dipakai.
TINGKAT = ("Mudah", "Menengah", "Lanjut", "Sulit")


def _bahasa_tersentuh(languages, data):
    """Bahasa yang materinya pernah dibuka, urut seperti di LANGUAGES."""
    hasil = []
    for lang in languages:
        awalan = f"{lang['key']}_materi::"
        if any(k.startswith(awalan) for k in data.get("materi_dibaca", [])) or \
                any(k.startswith(awalan) for k in data.get("materi_sebagian", [])):
            hasil.append(lang)
    return hasil


def _tingkat_maks(lang, data):
    """Indeks tingkat tertinggi yang boleh ditawarkan: satu di atas yang sudah lulus."""
    kat = f"{lang['key']}_latihan"
    lulus = [TINGKAT.index(e["difficulty"]) for e in lang["exercises"]
             if e.get("difficulty") in TINGKAT
             and _sudah(data, kat, e["title"], "latihan_lulus")]
    return (max(lulus) + 1) if lulus else 0


def _undian(hari, lang, ex):
    """Angka acak-tapi-tetap untuk satu latihan pada satu hari."""
    teks = f"{_benih_hari(hari)}:{lang['key']}:{ex['title']}"
    return hashlib.md5(teks.encode("utf-8")).hexdigest()


def tantangan_harian(languages, data, hari=None):
    """Satu latihan pilihan untuk hari ini, atau None kalau tidak ada yang cocok.

    Dulu kandidatnya SELURUH latihan di dua puluh kurikulum, dipilih dengan
    `hari % jumlah`. Audit 2026-10-17 (tiga agen terpisah) mengukurnya: pada
    profil baru, 54 dari 60 hari jatuh ke bahasa yang toolchain-nya tidak
    terpasang, 16 hari berupa latihan Sulit atau proyek akhir, dan pemula
    HTML di hari pertama disodori Kotlin Latihan 10. Tantangan yang mustahil
    dikerjakan merusak rasa mampu, bukan menantang.

    Sekarang kandidatnya:
      * dari bahasa yang sedang dipelajari (materinya pernah dibuka); profil
        yang belum menyentuh apa pun memakai bahasa pertama di LANGUAGES,
        pintu masuk yang memang tidak butuh pemasangan apa pun;
      * yang toolchain-nya siap di mesin ini (tombol yang berujung "belum
        terpasang" adalah tombol yang berujung penolakan);
      * paling tinggi SATU tingkat di atas latihan tersulit yang sudah lulus
        di bahasa itu; proyek akhir baru ikut kalau sisanya sudah lulus.

    Pilihannya memakai undian per latihan (hash tanggal + judul), bukan posisi
    di daftar. Daftar kandidat memang bisa berubah di tengah hari (bahasa baru
    disentuh, tingkat berikutnya terbuka); dengan undian, tantangan yang
    sedang dikerjakan hanya berganti kalau latihan itu sendiri sudah lulus.

    Latihan tidak pernah dikunci bab (lihat bab.py), jadi tidak ada penyaringan
    penguncian di sini.
    """
    bahasa = _bahasa_tersentuh(languages, data) or list(languages[:1])
    kandidat = []
    for lang in bahasa:
        if not runner.tersedia(lang["runner"]):
            continue
        kat = f"{lang['key']}_latihan"
        batas = _tingkat_maks(lang, data)
        sisa = [e for e in lang["exercises"]
                if not _sudah(data, kat, e["title"], "latihan_lulus")
                and not _sudah(data, kat, e["title"], "latihan_manual")]
        biasa = [e for e in sisa if not e.get("proyek")]
        for e in (biasa or sisa):
            if e.get("difficulty") in TINGKAT and TINGKAT.index(e["difficulty"]) > batas:
                continue
            kandidat.append((lang, e))

    if not kandidat:
        return None

    lang, ex = min(kandidat, key=lambda le: _undian(hari, *le))
    return Langkah("latihan", lang, ex, "tantangan hari ini", 0)


def ringkasan_hari_ini(data, target):
    """(xp_hari_ini, target, tercapai?) untuk bar target harian."""
    xp = xp_hari_ini(data)
    return xp, target, xp >= target
