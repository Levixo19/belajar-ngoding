"""Tampilan materi: baca, tandai, bookmark, dan cari di dalam satu bahasa.

Tiga perubahan perilaku yang disengaja:

* **Materi baru dihitung "dibaca" kalau benar-benar dibaca sampai habis.**
  Dulu XP dan tanda [v] diberikan sebelum halaman pertama muncul, jadi membuka
  lalu langsung menekan [q] tetap menaikkan progres. Sekarang berhenti di
  tengah dicatat sebagai [~] "dibaca sebagian", tanpa XP.
* **Paragraf dibungkus mengikuti lebar terminal** dan contoh kode disorot per
  token, bukan dicetak satu warna hijau datar.
* **Daftarnya dua tingkat: bab dulu, baru materi di dalamnya.** Bab yang masih
  terkunci tetap terlihat lengkap dengan judul, tingkat, jumlah materi, dan
  alasannya. Menyembunyikannya justru menghapus alasan bab ini ada — orang
  perlu tahu apa yang menanti, bukan cuma apa yang sudah lewat.

Aturan "bab mana yang boleh dibuka" TIDAK ditulis ulang di sini; seluruhnya
dipinjam dari `bab.py`. Begitu ada tempat kedua yang memutuskannya, terminal
dan web akan berbeda pendapat tentang materi yang sama.

Penjagaannya duduk di `render_material`, bukan di menunya, karena itulah
SATU-SATUNYA pintu masuk materi di antarmuka terminal: menu bab, pencarian
lokal, pencarian global, bookmark, "lanjutkan yang terakhir", dan antrean saran
semuanya berakhir di fungsi itu.

Importir: main.py, layar/navigasi.py, tests/test_data.py (memakai `teks_polos`).
"""

from pelajar import bab
from pelajar import kuis_materi
from pelajar import waktu
from inti import berkas
from inti import sorot
from inti import tema
from layar.utils import (
    C, paint, clear, paginate, ask, ask_atau_eof, ask_choice, header, rule,
    lebar, bungkus_baris, sorot_kata, tinggi_halaman, press_enter, potong,
)
from pelajar.progress import (
    record_material_read, load_progress, kunci, toggle_bookmark, is_bookmarked,
)

try:
    from pelajar import konfigurasi
except ImportError:
    konfigurasi = None


# Tingkat bab memakai tangga peran yang sama dengan tingkat kesulitan latihan
# (lihat exercises.PERAN_TINGKAT) supaya "makin panas warnanya, makin berat
# isinya" berlaku di seluruh aplikasi, bukan cuma di satu layar.
PERAN_TINGKAT = {
    "dasar": "tingkat_mudah",
    "menengah": "tingkat_sedang",
    "mahir": "tingkat_sulit",
}


def _bahasa_dari_kategori(kategori):
    """'java_materi' -> 'java'. Dipakai untuk memilih aturan penyorot."""
    return kategori.rsplit("_", 1)[0] if "_" in kategori else ""


def _entri_bahasa(kategori, materials, lang=None):
    """Entri bahasa seperlunya untuk `bab.py`: cuma `key` dan `materials`.

    Pemanggil lama (navigasi.py, antrean saran) tidak memegang entri LANGUAGES,
    cuma kategori progres dan daftar materinya — dan dari keduanya entri itu
    bisa disusun ulang tanpa mengimpor main.py, yang akan jadi impor melingkar.

    Kalau daftar yang diberikan ternyata BUKAN daftar utuh bahasanya, rentang
    bab tidak akan cocok dan `bab.py` jatuh ke satu bab berisi semuanya, alias
    semua terbuka. Itu arah yang benar untuk gagal: salah membuka cuma berarti
    seseorang membaca lebih cepat dari rencana, sedangkan salah mengunci
    menghentikan orang di depan pintu yang seharusnya sudah terbuka.
    """
    if lang is not None:
        return lang
    return {"key": _bahasa_dari_kategori(kategori), "materials": materials or []}


def _indeks_materi(entri, topic):
    """Posisi `topic` di daftar materi bahasanya; -1 kalau tidak dikenali."""
    try:
        return entri["materials"].index(topic)
    except (AttributeError, KeyError, ValueError):
        return -1


def _bab_dari(entri, topic, data=None):
    """Bab yang memuat `topic`, atau None kalau materinya tidak dikenali."""
    posisi = _indeks_materi(entri, topic)
    return bab.bab_materi(entri, posisi, data) if posisi >= 0 else None


def _garis_label(teks, lbr, peran="redup"):
    """Garis pembatas kotak kode yang sekaligus memuat keterangan.

    Bentuknya:  ── Buat berkas: hello.py ───────────────────
    Keterangan ditaruh DI GARIS, bukan di baris terpisah, supaya tidak
    memakan tinggi layar yang sudah sempit untuk isi materinya sendiri.
    """
    isi = "  ── " + teks + " "
    sisa = lbr - 2 - len(isi)
    if sisa < 2:
        # Terminal sempit: potong keterangannya, jangan sampai garis membungkus.
        maks = max(0, lbr - 12)
        isi = "  ── " + teks[:maks] + " "
        sisa = 2
    return tema.cat(isi + "─" * sisa, peran)


def _kotak_kode(kode, bahasa, konteks, lbr, sorot_nyala):
    """Blok kode lengkap dengan instruksi di garis atas dan bawah."""
    p = berkas.petunjuk_kode(bahasa, kode, konteks)

    peran_atas = {
        berkas.PROGRAM: "sukses",
        berkas.MULTI: "sukses",
        berkas.SESI: "info",
    }.get(p.jenis, "redup")

    baris = [_garis_label(p.instruksi, lbr, peran_atas)]

    if sorot_nyala and bahasa:
        baris.extend(sorot.sorot_baris(kode, bahasa, awalan="  "))
    else:
        for cl in kode.splitlines():
            baris.append(tema.cat("  " + cl, "kode_string"))

    if p.perintah:
        bawah = "Jalankan: " + "  lalu  ".join(p.perintah)
        baris.append(_garis_label(bawah, lbr, "aksen"))
    elif p.keterangan:
        baris.append(_garis_label(p.keterangan, lbr, "redup"))
    else:
        baris.append(tema.cat("  " + "─" * (lbr - 6), "redup"))

    return baris


def baris_materi(topic, bahasa="", kata_sorot=""):
    """Ubah satu topik jadi daftar baris siap tampil."""
    lbr = lebar()
    sorot_nyala = konfigurasi is None or konfigurasi.ambil("sorot_sintaks", True)
    lines = []

    for i, section in enumerate(topic["sections"]):
        if i > 0:
            lines.append("")
        if section.get("heading"):
            lines.append(tema.cat("  ### " + section["heading"], "subjudul", tema.TEBAL))

        for paragraph in section.get("body") or []:
            for baris in bungkus_baris(paragraph, lbr - 2, "  "):
                if kata_sorot:
                    baris = sorot_kata(baris, kata_sorot)
                lines.append(baris)

        if section.get("code"):
            konteks = section.get("heading") or topic["title"]
            lines.extend(_kotak_kode(section["code"], bahasa, konteks,
                                     lbr, sorot_nyala))

    return lines


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


def _layar_terkunci(b, materi_judul=""):
    """Kenapa sesuatu belum bisa dibuka, dan apa persisnya yang membukanya.

    Layar ini menyebut sisa pekerjaannya dalam angka lalu menunjuk saklar di
    Pengaturan — tapi tidak pernah menyalakannya sendiri. Menawarkan pintu
    darurat berbeda dengan mendorong orang melewatinya, dan setelan yang
    berubah tanpa diminta adalah cara tercepat membuat orang berhenti percaya
    pada layar pengaturannya.
    """
    clear()
    header(f"BAB {b['nomor']} MASIH TERKUNCI", b["judul"])

    if b["ket"]:
        for baris in bungkus_baris(b["ket"], lebar() - 2, "  "):
            print(tema.cat(baris, "teks"))
        print()
    print(tema.cat(f"  Tingkat : {b['label_tingkat']} — "
                   + bab.KETERANGAN_TINGKAT.get(b["tingkat"], ""),
                   PERAN_TINGKAT.get(b["tingkat"], "teks")))
    print(tema.cat(f"  Isinya  : {b['jumlah']} materi", "teks"))
    if materi_judul:
        print(tema.cat(f"  Diminta : {materi_judul}", "redup"))
    print()

    if b["alasan"]:
        print(tema.cat("  " + b["alasan"], "peringatan", tema.TEBAL))
    for baris in bungkus_baris(
            bab.KALIMAT_ATURAN, lebar() - 2, "  "):
        print(tema.cat(baris, "teks"))
    print()
    for baris in bungkus_baris(
            'Sudah pernah belajar bahasa ini dan cuma ingin melompat? Di '
            'Pengaturan ada saklar "Buka semua bab tanpa syarat" yang membuka '
            'semuanya sekaligus.', lebar() - 2, "  "):
        print(tema.cat(baris, "redup"))
    press_enter()


def _baca(topic, kategori, bahasa, kata_sorot, entri):
    """Tampilkan isinya, catat hasilnya, dan laporkan indeks yang baru terbuka.

    Himpunan indeks terbuka dihitung DUA KALI — sebelum halaman pertama dan
    sesudah halaman terakhir — karena materi penutup sebuah bab membuka bab
    berikutnya tepat pada saat ini. Memakai angka yang dihitung sebelum
    materinya dibaca berarti pintu yang baru saja terbuka baru kelihatan pada
    kunjungan menu berikutnya, dan momen itu justru satu-satunya alasan
    penguncian bertahap ini ada.
    """
    sebelum = bab.indeks_terbuka(entri, load_progress())
    tuntas = paginate(topic["title"],
                      baris_materi(topic, bahasa, kata_sorot),
                      chunk_size=tinggi_halaman(sisa=9))
    # Dicatat SESUDAH dibaca: berhenti di tengah tidak boleh dihitung selesai.
    record_material_read(kategori, topic["title"], tuntas=tuntas)
    return tuntas, bab.indeks_terbuka(entri, load_progress()) - sebelum


def _sesudah(entri, daftar, topic, data):
    """(materi berikutnya menurut daftar, babnya). (None, None) kalau di ujung.

    Babnya ikut dikembalikan karena pemanggilnya butuh dua hal dari sana:
    menolak melompat ke bab yang masih terkunci, dan memberi tahu kalau materi
    berikutnya ternyata sudah pindah bab.
    """
    if not daftar:
        return None, None
    try:
        posisi = daftar.index(topic)
    except ValueError:
        return None, None
    if posisi + 1 >= len(daftar):
        return None, None

    calon = daftar[posisi + 1]
    indeks = _indeks_materi(entri, calon)
    return calon, (bab.bab_materi(entri, indeks, data) if indeks >= 0 else None)


def _bab_baru(entri, indeks_baru, data):
    """Bab-bab yang materinya baru saja masuk daftar terbuka."""
    if not indeks_baru:
        return []
    return [b for b in bab.status(entri, data)
            if set(b["materi"]) & indeks_baru]


def render_material(topic, kategori="materi", kata_sorot="", daftar=None, lang=None):
    """Tampilkan satu materi. `daftar` (opsional) memungkinkan lompat ke berikutnya.

    `lang` adalah entri LANGUAGES; dipakai untuk memeriksa penguncian bab.
    Pemanggil yang tidak memegangnya tetap terjaga — entrinya disusun dari
    `kategori` dan `daftar` (lihat `_entri_bahasa`).
    """
    bahasa = _bahasa_dari_kategori(kategori)
    entri = _entri_bahasa(kategori, daftar, lang)

    bab_ini = _bab_dari(entri, topic)
    if bab_ini and bab_ini["status"] == bab.TERKUNCI:
        _layar_terkunci(bab_ini, topic["title"])
        return

    data_awal = load_progress()
    tuntas, baru_terbuka = _baca(topic, kategori, bahasa, kata_sorot, entri)
    # Kuis yang baru saja siap karena materi ini (pelajar/kuis_materi.py):
    # kalimatnya sama dengan tombol di kaki materi versi web.
    kuis_baru = (kuis_materi.kuis_baru_siap(lang, data_awal, load_progress())
                 if lang and lang.get("quizzes") else [])

    while True:
        # Dihitung ulang tiap putaran, bukan sekali di awal: membaca materi ini
        # bisa saja BARU SAJA membuka bab berikutnya, dan [n] harus tahu itu.
        data = load_progress()
        bab_ini = _bab_dari(entri, topic, data)
        calon, bab_calon = _sesudah(entri, daftar, topic, data)
        berikut_terkunci = bool(bab_calon and bab_calon["status"] == bab.TERKUNCI)
        berikut = None if berikut_terkunci else calon
        pindah_bab = bool(berikut and bab_calon and bab_ini
                          and bab_calon["nomor"] != bab_ini["nomor"])

        clear()
        header(topic["title"], "selesai dibaca" if tuntas else "dihentikan di tengah")
        ditandai = is_bookmarked(kategori, topic["title"])
        print(tema.cat("  Status bookmark: "
                       + ("TERSIMPAN" if ditandai else "belum disimpan"),
                       "judul" if ditandai else "redup"))
        if not tuntas:
            print(tema.cat("  Materi ini ditandai [~] dibaca sebagian. "
                           "Baca sampai habis untuk mendapat XP.", "peringatan"))
        for b in _bab_baru(entri, baru_terbuka, data):
            print(tema.cat(f"  Bab {b['nomor']} · {b['judul']} baru terbuka: "
                           f"{b['jumlah']} materi tingkat {b['label_tingkat']}.",
                           "sukses", tema.TEBAL))
        for _, q in kuis_baru:
            print(tema.cat(f"  {q['title']} siap: semua materinya sudah kamu baca.",
                           "sukses"))
        print()
        print(tema.cat("  [b] " + ("Hapus bookmark" if ditandai else "Simpan ke bookmark"),
                       "aksen"))
        print(tema.cat("  [u] Baca ulang materi ini", "aksen"))
        if berikut and pindah_bab:
            print(tema.cat(f"  [n] Mulai Bab {bab_calon['nomor']} · "
                           f"{bab_calon['judul']}: {berikut['title'][:34]}",
                           "sukses", tema.TEBAL))
        elif berikut:
            print(tema.cat(f"  [n] Lanjut ke materi berikutnya: {berikut['title'][:38]}",
                           "sukses"))
        elif berikut_terkunci:
            # Tanpa kalimat ini, hilangnya [n] terbaca sebagai "materinya habis".
            print(tema.cat(f"  Materi berikutnya ada di Bab {bab_calon['nomor']} · "
                           f"{bab_calon['judul']} yang masih terkunci.", "redup"))
            if bab_calon["alasan"]:
                print(tema.cat("  " + bab_calon["alasan"], "redup"))
        print(tema.cat("  [0] Kembali ke daftar", "redup"))

        pilih = ask_atau_eof("  Pilih > ")
        if pilih is None:
            return
        pilih = pilih.lower()
        if pilih == "b":
            toggle_bookmark(kategori, topic["title"])
        elif pilih == "u":
            tuntas, baru_terbuka = _baca(topic, kategori, bahasa, kata_sorot, entri)
        elif pilih == "n" and berikut:
            render_material(berikut, kategori, kata_sorot, daftar, lang)
            return
        else:
            return


def _label(topic, kategori, data):
    k = kunci(kategori, topic["title"])
    if k in data["materi_dibaca"]:
        tanda = tema.cat("[v]", "sukses", tema.TEBAL)
    elif k in data["materi_sebagian"]:
        tanda = tema.cat("[~]", "peringatan")
    else:
        tanda = tema.cat("[ ]", "redup")
    bintang = tema.cat(" *", "judul", tema.TEBAL) if k in data["bookmark"] else ""
    # Perkiraan menit yang sama dengan daftar materi versi web (pelajar/waktu.py).
    menit = tema.cat(f"  ≈{waktu.menit_materi(topic)} mnt", "redup")
    return f"{tanda} {topic['title']}{bintang}{menit}"


def _cari_lokal(title, materials, kategori, entri=None):
    """Cari kata kunci di SELURUH materi bahasa ini, bab terkunci sekalipun.

    Pencarian sengaja tidak menghormati bab: orang mencari karena sedang
    kebingungan pada satu kata, dan hasil yang disembunyikan cuma menambah
    kebingungan itu. Yang dijaga tetap pintunya — `render_material` yang
    memutuskan boleh atau tidaknya materi itu dibuka.
    """
    kata = ask("  Kata kunci > ", "").strip()
    if not kata:
        return
    kunci_cari = kata.lower()

    cocok = []
    for m in materials:
        isi = teks_polos(m).lower()
        if kunci_cari in isi:
            cocok.append((m, isi.count(kunci_cari)))
    cocok.sort(key=lambda x: -x[1])

    if not cocok:
        print(tema.cat(f"  Tidak ada materi yang memuat '{kata}'.", "galat"))
        ask("  Tekan ENTER untuk kembali...", "")
        return

    while True:
        clear()
        header("HASIL PENCARIAN", f"{title} - '{kata}' - {len(cocok)} materi")
        # Ditandai, bukan disembunyikan — dan dihitung ulang tiap putaran layar
        # karena membaca satu hasil bisa saja membuka bab tempat hasil
        # berikutnya berada. Daftar yang lupa dihitung ulang akan berbohong
        # justru pada saat pintunya baru terbuka.
        terbuka = (bab.indeks_terbuka(entri, load_progress())
                   if entri is not None else None)
        names = []
        for m, n in cocok:
            baris = f"{m['title']}  ({n}x)"
            if terbuka is not None:
                posisi = _indeks_materi(entri, m)
                if posisi >= 0 and posisi not in terbuka:
                    # Berupa KATA, bukan sekadar warna: tema `mono` tidak punya
                    # warna sama sekali, dan penanda yang lenyap di satu tema
                    # sama saja dengan tidak ada. Sama persis dengan penanda di
                    # pencarian global supaya dua layar pencarian tidak
                    # menjawab berbeda untuk materi yang sama.
                    baris += "  " + tema.cat("[terkunci]", "peringatan")
            names.append(baris)
        pilih = ask_choice(paint("  Pilih materi:", C.BLUE, C.BOLD), names)
        if pilih == 0:
            return
        render_material(cocok[pilih - 1][0], kategori, kata_sorot=kata,
                        daftar=materials, lang=entri)


def _hitung(isi, kategori, data):
    """(berapa yang tuntas, berapa yang baru dibaca sebagian) dari sederet materi."""
    dibaca = sum(1 for m in isi
                 if kunci(kategori, m["title"]) in data["materi_dibaca"])
    sebagian = sum(1 for m in isi
                   if kunci(kategori, m["title"]) in data["materi_sebagian"])
    return dibaca, sebagian


def _baris_bab(b, lebar_judul):
    """Satu baris daftar bab: penanda, judul, tingkat, dan kemajuannya.

    SATU baris, selalu. `ask_choice` menggambar ulang menunya dengan menghitung
    jumlah baris yang tercetak, jadi opsi yang melipat membuat kursornya naik
    ke tempat yang salah dan menu ikut berantakan.
    """
    if b["status"] == bab.TUNTAS:
        tanda = tema.cat("[v]", "sukses", tema.TEBAL)
    elif b["status"] == bab.TERKUNCI:
        tanda = tema.cat("[x]", "redup")
    elif b["selesai"]:
        tanda = tema.cat("[~]", "peringatan")
    else:
        tanda = tema.cat("[ ]", "redup")

    judul = potong(f"Bab {b['nomor']}: {b['judul']}", lebar_judul).ljust(lebar_judul)
    tingkat = tema.cat(b["label_tingkat"].ljust(8),
                       PERAN_TINGKAT.get(b["tingkat"], "teks"))
    maju = f"{b['selesai']}/{b['jumlah']}".rjust(5)
    baris = f"{tanda} {judul}  {tingkat}  {maju}"
    if b["status"] == bab.TERKUNCI:
        baris += tema.cat("  terkunci", "redup")
    return baris


def _menu_isi_bab(title, materials, kategori, entri, b, tunggal=False):
    """Daftar materi DI DALAM satu bab.

    `daftar` yang dibawa ke `render_material` tetap seluruh materi bahasa ini,
    bukan cuma isi babnya: pintasan [n] harus bisa menyeberang ke bab berikutnya
    tepat pada saat bab itu terbuka.

    `tunggal` menandai bahasa yang cuma punya satu bab — layar ini otomatis
    jadi layar pertamanya, jadi judul babnya tidak perlu diulang.
    """
    while True:
        clear()
        header("MATERI: " + title,
               "" if tunggal else f"Bab {b['nomor']}: {b['judul']}")

        data = load_progress()
        isi = [materials[i] for i in b["materi"]]
        dibaca, sebagian = _hitung(isi, kategori, data)
        ringkasan = f"  Sudah dibaca {dibaca}/{len(isi)} materi"
        if sebagian:
            ringkasan += f"  ({sebagian} dibaca sebagian)"
        print(tema.cat(ringkasan, "teks"))
        if not tunggal:
            if b["ket"]:
                print(tema.cat("  " + b["ket"], "redup"))
            print(tema.cat(f"  Tingkat {b['label_tingkat']} — "
                           + bab.KETERANGAN_TINGKAT.get(b["tingkat"], ""),
                           PERAN_TINGKAT.get(b["tingkat"], "teks")))
        print(tema.cat("  [v] selesai   [~] sebagian   * di-bookmark", "redup"))
        print(rule("-", C.DIM, bold=False))

        names = [_label(m, kategori, data) for m in isi]
        extra = {"c": "Cari kata kunci di materi ini"}
        # Loncat ke materi pertama yang belum tuntas: jalan pintas paling sering
        # dipakai orang yang belajar berurutan.
        belum = next((n for n, m in enumerate(isi, start=1)
                      if kunci(kategori, m["title"]) not in data["materi_dibaca"]), None)
        if belum:
            extra["l"] = f"Lanjutkan: {isi[belum - 1]['title'][:40]}"

        pilih = ask_choice(paint("  Pilih materi:", C.BLUE, C.BOLD), names, extra=extra)

        if pilih == 0:
            return
        if pilih == "c":
            _cari_lokal(title, materials, kategori, entri)
            continue
        if pilih == "l" and belum:
            render_material(isi[belum - 1], kategori, daftar=materials, lang=entri)
            continue
        if isinstance(pilih, int):
            render_material(isi[pilih - 1], kategori, daftar=materials, lang=entri)


def materials_menu(title, materials, kategori="materi", lang=None):
    """Layar materi dua tingkat: pilih bab dulu, baru materi di dalamnya.

    Bahasa yang cuma punya satu bab melewati layar bab sama sekali. Layar
    berisi satu pilihan bukan navigasi — ia cuma satu tombol tambahan sebelum
    tempat yang sudah pasti dituju.
    """
    entri = _entri_bahasa(kategori, materials, lang)

    while True:
        clear()
        data = load_progress()
        daftar_bab = bab.status(entri, data)

        if len(daftar_bab) <= 1:
            _menu_isi_bab(title, materials, kategori, entri, daftar_bab[0],
                          tunggal=True)
            return

        header("MATERI: " + title, bab.kalimat_ringkas(entri, data))

        dibaca, sebagian = _hitung(materials, kategori, data)
        tuntas = sum(1 for b in daftar_bab if b["status"] == bab.TUNTAS)
        ringkasan = (f"  Sudah dibaca {dibaca}/{len(materials)} materi"
                     f"   {tuntas}/{len(daftar_bab)} bab tuntas")
        if sebagian:
            ringkasan += f"   ({sebagian} dibaca sebagian)"
        print(tema.cat(ringkasan, "teks"))

        # Alasan bab terkunci PERTAMA saja yang ditulis di sini: cuma itu yang
        # bisa dikerjakan sekarang. Alasan bab-bab sesudahnya menunggu di layar
        # penjelasannya masing-masing.
        menunggu = next((b for b in daftar_bab if b["status"] == bab.TERKUNCI), None)
        if menunggu and menunggu["alasan"]:
            for baris in bungkus_baris(
                    f"Bab {menunggu['nomor']} terkunci — {menunggu['alasan']}",
                    lebar() - 2, "  "):
                print(tema.cat(baris, "peringatan"))
        keterangan = "  [v] tuntas   [~] sedang jalan   [ ] belum"
        if menunggu:
            # Saklar "Buka semua bab" membuat [x] tidak pernah muncul. Menyebut
            # penanda yang mustahil ada cuma menyuruh mata mencari sesuatu yang
            # tidak di sana.
            keterangan += "   [x] terkunci"
        print(tema.cat(keterangan, "redup"))
        print(rule("-", C.DIM, bold=False))

        # Kolom tetap baris bab mengambil jatahnya lebih dulu, judul kebagian
        # sisanya. Tanpa batas ini `utils.potong` yang memangkas barisnya di
        # terminal sempit, dan potongannya membuang SELURUH warna baris itu —
        # termasuk warna tingkat, satu-satunya alasan kolom tingkat ada.
        # 7 = awalan "   N. " yang digambar `ask_choice`; 4 = penanda + spasi;
        # 8 = kolom tingkat; 5 = kolom kemajuan; 10 = kata "terkunci" di ekor.
        tetap = 7 + 4 + 2 + 8 + 2 + 5 + (10 if menunggu else 0)
        lebar_judul = min(
            max(len(f"Bab {b['nomor']}: {b['judul']}") for b in daftar_bab),
            max(12, lebar() - tetap))
        names = [_baris_bab(b, lebar_judul) for b in daftar_bab]

        extra = {"c": "Cari kata kunci di materi ini"}
        # "Lanjutkan" hanya boleh menunjuk materi yang BOLEH dibuka; mengirim
        # orang ke pintu terkunci lewat pintasan yang menjanjikan kelanjutan
        # adalah cara paling cepat membuat fitur ini terasa seperti gangguan.
        terbuka = bab.indeks_terbuka(entri, data)
        belum = next((i for i in range(len(materials))
                      if i in terbuka and kunci(kategori, materials[i]["title"])
                      not in data["materi_dibaca"]), None)
        if belum is not None:
            extra["l"] = f"Lanjutkan: {materials[belum]['title'][:40]}"

        pilih = ask_choice(paint("  Pilih bab:", C.BLUE, C.BOLD), names, extra=extra)

        if pilih == 0:
            return
        if pilih == "c":
            _cari_lokal(title, materials, kategori, entri)
            continue
        if pilih == "l" and belum is not None:
            render_material(materials[belum], kategori, daftar=materials, lang=entri)
            continue
        if isinstance(pilih, int):
            b = daftar_bab[pilih - 1]
            if b["status"] == bab.TERKUNCI:
                _layar_terkunci(b)
            else:
                _menu_isi_bab(title, materials, kategori, entri, b)
