"""Menjawab pertanyaan "habis ini ngapain?".

Aplikasi ini menyimpan 153 materi, 53 kuis, dan 127 latihan di delapan bahasa.
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

Semua murni fungsi baca; tidak ada yang disimpan dari sini.

Importir: main.py. Hanya membaca dict progres dari progress.load_progress().
"""

from datetime import date

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


def langkah_berikutnya(languages, data, maks=6):
    """Daftar saran langkah berikutnya, paling mendesak lebih dulu."""
    if not languages:
        return []

    saran = []
    urutan = _urut_bahasa(languages, data)
    bahasa_aktif = urutan[0]

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
        for m in lang["materials"]:
            if _sudah(data, kat, m["title"], "materi_sebagian"):
                saran.append(Langkah("materi", lang, m,
                                     "kemarin berhenti di tengah", 2))

    kat_m = f"{bahasa_aktif['key']}_materi"
    kat_k = f"{bahasa_aktif['key']}_kuis"
    kat_l = f"{bahasa_aktif['key']}_latihan"

    # 3. Materi berikutnya di bahasa yang sedang dikerjakan.
    berikut = next((m for m in bahasa_aktif["materials"]
                    if not _sudah(data, kat_m, m["title"], "materi_dibaca")), None)
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
        if not tersentuh:
            saran.append(Langkah("materi", lang, lang["materials"][0],
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
    """Satu latihan pilihan untuk hari ini, atau None kalau semua sudah tuntas."""
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
