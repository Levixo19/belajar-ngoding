"""Menjawab pertanyaan "habis ini ngapain?".

Aplikasi ini menyimpan 190 materi, 67 kuis, dan 159 latihan di sebelas bahasa.
Untuk orang yang baru mulai, daftar sepanjang itu bukan kekayaan -- itu
kelumpuhan. Dulu satu-satunya penunjuk arah adalah "lanjutkan dari terakhir",
yang justru membuka ulang hal yang BARU SAJA selesai dikerjakan.

Modul ini menyusun antrean langkah berikutnya dengan urutan prioritas yang
mencerminkan cara belajar yang efektif:

1. Kuis yang jatuh tempo diulang -- ingatan yang mau luruh diselamatkan dulu.
2. Materi yang berhenti di tengah -- tutup dulu yang menggantung.
3. Materi berikutnya di bahasa yang sedang dikerjakan -- jaga momentum.
4. Latihan yang materinya sudah dibaca -- ubah bacaan jadi keterampilan.
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

from datetime import date

import bab
from progress import kunci, kuis_jatuh_tempo, xp_hari_ini


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

    # 1. Kuis jatuh tempo -- lintas bahasa, karena lupa tidak kenal bahasa.
    for lang in languages:
        kat = f"{lang['key']}_kuis"
        for q in lang["quizzes"]:
            if kuis_jatuh_tempo(data, kat, q["title"]):
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
                saran.append(Langkah("materi", lang, m,
                                     "dibuka tapi belum tuntas dibaca", 2))

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
                             "materi berikutnya di bahasa yang sedang kamu pelajari", 3))

    # 4. Latihan yang belum tuntas.
    latihan = next((e for e in bahasa_aktif["exercises"]
                    if not _sudah(data, kat_l, e["title"], "latihan_lulus")
                    and not _sudah(data, kat_l, e["title"], "latihan_manual")), None)
    if latihan:
        saran.append(Langkah("latihan", bahasa_aktif, latihan,
                             "ubah yang sudah dibaca jadi kode beneran", 4))

    # 5. Kuis yang belum pernah dikerjakan.
    kuis = next((q for q in bahasa_aktif["quizzes"]
                 if kunci(kat_k, q["title"]) not in data.get("kuis_skor", {})), None)
    if kuis:
        saran.append(Langkah("kuis", bahasa_aktif, kuis,
                             "uji pemahamanmu atas materi tadi", 5))

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


def tantangan_harian(languages, data, hari=None):
    """Satu latihan pilihan untuk hari ini, atau None kalau semua sudah tuntas.

    Kandidatnya hanya latihan, dan latihan tidak pernah dikunci bab (lihat
    bab.py) -- jadi tidak ada yang perlu disaring di sini. Itu bukan kebetulan
    yang boleh diubah diam-diam: pilihan hari ini diambil dari POSISI di dalam
    daftar kandidat, sehingga apa pun yang membuat daftar itu memanjang atau
    memendek di tengah hari akan mengganti tantangan yang sedang dikerjakan
    orang dengan tantangan lain. Status bab persis seperti itu -- ia berubah
    justru pada saat sebuah bab terbuka. Kalau suatu saat materi ikut jadi
    kandidat, penguncian harus diperiksa saat materinya DIBUKA, bukan dengan
    membuang kandidatnya dari daftar ini.
    """
    kandidat = []
    for lang in languages:
        kat = f"{lang['key']}_latihan"
        for e in lang["exercises"]:
            if _sudah(data, kat, e["title"], "latihan_lulus"):
                continue
            if _sudah(data, kat, e["title"], "latihan_manual"):
                continue
            kandidat.append((lang, e))

    if not kandidat:
        return None

    lang, ex = kandidat[_benih_hari(hari) % len(kandidat)]
    return Langkah("latihan", lang, ex, "tantangan hari ini", 0)


def ringkasan_hari_ini(data, target):
    """(xp_hari_ini, target, tercapai?) untuk bar target harian."""
    xp = xp_hari_ini(data)
    return xp, target, xp >= target
