"""Perkiraan waktu: "materi ini kira-kira berapa menit?". Satu rumus untuk dua antarmuka.

Persona audit 2026-10-17 (pekerja kantoran, 30 menit sepulang kerja) tidak
bisa memilih apa yang muat dalam waktunya: aplikasi cuma bicara XP, padahal
panjang materi Python saja berkisar 221-2121 kata. Angka di sini PERKIRAAN,
dan dibulatkan supaya tidak terbaca lebih pasti daripada kenyataannya.

Asumsinya ditulis supaya bisa dibantah:
  * prosa dibaca ~130 kata per menit (pelajar yang membaca untuk paham,
    bukan membaca sekilas);
  * tiap ~10 baris contoh kode butuh satu menit untuk dibaca dan dicoba;
  * kuis ~45 detik per soal;
  * latihan menurut tingkatnya; proyek akhir satu jam.
"""

KATA_PER_MENIT = 130
BARIS_KODE_PER_MENIT = 10
DETIK_PER_SOAL = 45
MENIT_LATIHAN = {"Mudah": 8, "Menengah": 15, "Lanjut": 25, "Sulit": 35}
MENIT_PROYEK = 60


def _bulat(menit):
    """Dibulatkan ke 5 menit di atas 10 menit: '≈23 menit' terbaca palsu teliti."""
    menit = max(2, round(menit))
    return menit if menit <= 10 else int(5 * round(menit / 5))


def menit_materi(materi):
    kata = sum(len(" ".join(s.get("body") or []).split()) for s in materi["sections"])
    kode = sum(len((s.get("code") or "").splitlines()) for s in materi["sections"])
    return _bulat(kata / KATA_PER_MENIT + kode / BARIS_KODE_PER_MENIT)


def menit_kuis(kuis):
    return _bulat(len(kuis["questions"]) * DETIK_PER_SOAL / 60)


def menit_latihan(latihan):
    if latihan.get("proyek"):
        return MENIT_PROYEK
    return MENIT_LATIHAN.get(latihan.get("difficulty"), 15)


def menit(tipe, obj):
    """Perkiraan menit untuk satu langkah ("materi" | "kuis" | "latihan")."""
    return {"materi": menit_materi, "kuis": menit_kuis,
            "latihan": menit_latihan}.get(tipe, lambda _o: 0)(obj)
