"""Tebak keluarannya: latihan membaca kode dari contoh materi yang sudah dibaca.

Audit 2026-10-17: 0 dari 968 soal kuis memuat kode multi-baris, dan tidak ada
satu pun latihan "baca kode". Padahal kemampuan melacak kode mendahului
kemampuan menulisnya, dan materi sudah memuat ratusan contoh program utuh.

Bentuknya: pelajar mengetik perkiraan keluaran sebuah contoh, lalu contoh itu
dijalankan sungguhan. Kuncinya keluaran nyata dari runner, jadi tidak bisa
salah tulis. Ini BUKAN latihan: tidak menyentuh latihan_lulus atau definisi
"lulus" (runner.periksa). Yang dicatat cuma riwayat tebakan per blok.

Blok yang layak:
  * berkas.jenis_kode == PROGRAM dan boleh dijalankan aplikasi (pagar SESI
    Fedora/Git ikut dari sana, jadi perintah sungguhan tidak pernah lolos);
  * bukan HTML/CSS (keluarannya pohon struktur, bukan sesuatu yang ditebak);
  * tidak membaca masukan (tombol Jalankan di materi tidak punya stdin, jadi
    program yang menunggu input berhenti dengan EOF).
"""

import re

from inti import berkas, runner
from pelajar.progress import judul_kunci

BUKAN_TEBAKAN = {"html", "css", "fedora", "git"}
_BACA_MASUKAN = re.compile(
    r"\binput\s*\(|Scanner|scanf|\bgets\b|readline|ReadLine|readLine|"
    r"\bread\s+-|\bread\s+[a-z_]|STDIN|stdin|fgets|cin\s*>>|bufio\.NewReader|"
    r"Console\.Read|io::stdin|fgetc|getchar")


def blok_layak(lang):
    """[(indeks_materi, indeks_bagian, kode)] contoh yang bisa ditebak."""
    bhs = lang["runner"]
    if bhs in BUKAN_TEBAKAN:
        return []
    hasil = []
    for i, m in enumerate(lang["materials"]):
        for j, s in enumerate(m["sections"]):
            kode = s.get("code")
            if s.get("bahasa") not in (None, bhs):
                continue   # contoh berbahasa lain: runner kurikulum ini salah alat
            if not kode or _BACA_MASUKAN.search(kode):
                continue
            jenis = berkas.jenis_kode(bhs, kode)
            if jenis != berkas.PROGRAM or not berkas.boleh_dijalankan_aplikasi(bhs, jenis):
                continue
            hasil.append((i, j, kode))
    return hasil


def kunci_blok(lang, indeks_materi, indeks_bagian):
    """Kunci progres satu blok: kategori materi + judul tanpa nomor + bagian."""
    judul = judul_kunci(lang["materials"][indeks_materi]["title"])
    return f"{lang['key']}_materi::{judul}#{indeks_bagian}"


def cari_blok(lang, indeks_materi, kode):
    """Indeks bagian sebuah contoh di materi itu, atau None kalau bukan contoh layak."""
    for i, j, k in blok_layak(lang):
        if i == indeks_materi and k == kode:
            return j
    return None


def pilih_kartu(lang, data, maks=5):
    """Contoh dari materi yang SUDAH dibaca, yang paling perlu dilatih dulu.

    Urutan: yang terakhir kali salah ditebak, lalu yang belum pernah dicoba,
    lalu yang paling lama tidak dicoba. Toolchain yang tidak terpasang = kosong:
    kartu yang tidak bisa diperiksa adalah tombol yang berujung penolakan.
    """
    if not runner.tersedia(lang["runner"]):
        return []
    dibaca = set(data.get("materi_dibaca", []))
    tebakan = data.get("tebakan", {})
    calon = []
    for i, j, kode in blok_layak(lang):
        m = lang["materials"][i]
        if f"{lang['key']}_materi::{judul_kunci(m['title'])}" not in dibaca:
            continue
        info = tebakan.get(kunci_blok(lang, i, j)) or {}
        urutan = (0 if info.get("salah_terakhir") else 1 if not info else 2,
                  info.get("terakhir", ""), i, j)
        calon.append((urutan, i, j, kode))
    calon.sort()
    return [(i, j, kode) for _, i, j, kode in calon[:maks]]
