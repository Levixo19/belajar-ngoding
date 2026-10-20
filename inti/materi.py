"""Membaca isi materi sebagai teks biasa.

Dipakai pencarian (terminal maupun web) dan beberapa tes yang menghitung
panjang prosa. Tidak ada hubungannya dengan cara materi DIGAMBAR, jadi ia
tidak lagi tinggal di lapisan tampilan.
"""


def teks_polos(topic):
    """Seluruh isi materi sebagai teks biasa. Dipakai fitur pencarian."""
    bagian = [topic["title"]]
    for section in topic["sections"]:
        if section.get("heading"):
            bagian.append(section["heading"])
        bagian.extend(section.get("body") or [])
        if section.get("code"):
            bagian.append(section["code"])
    return "\n".join(bagian)
