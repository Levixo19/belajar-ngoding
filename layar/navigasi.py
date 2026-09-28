"""Navigasi lintas bahasa: pencarian global, daftar bookmark, dan lanjut terakhir.

Ketiganya jalan pintas: mereka membuka materi tanpa melewati daftar materi
bahasanya sama sekali. Karena itu penguncian bab ikut ditegakkan DI SINI --
pintu yang cuma dijaga di satu dari tiga jalan masuk bukan pintu. Yang dijaga
hanya materi; kuis dan latihan memang tidak pernah dikunci (lihat bab.py).

Yang terkunci tetap DITAMPILKAN, lengkap dengan judul dan alasannya.
Menyembunyikannya dari hasil pencarian akan membuat orang mengira kata yang
dicarinya memang tidak ada di mana-mana -- keliru, dan tidak ada cara baginya
untuk tahu bahwa ia keliru.

Importir: main.py. Tidak menulis berkas sendiri; semua status lewat
pelajar/progress.py.
"""

from pelajar import bab
from inti import tema
from layar.utils import (
    C, paint, clear, ask, ask_atau_eof, ask_choice, press_enter, header, rule,
    lebar, bungkus_baris, sorot_kata,
)
from layar.materials import render_material, teks_polos
from layar.exercises import show_exercise
from layar.quiz import menu_satu_kuis
from pelajar.progress import load_progress, kunci, judul_kunci, bersihkan_bookmark

WARNA_TIPE = {"materi": "aksen", "kuis": "subjudul", "latihan": "judul"}


def _indeks_materi(lang, obj):
    """Posisi sebuah materi di daftar bahasanya, atau -1 kalau bukan miliknya.

    Identitas diperiksa lebih dulu, bukan `==`: satu dict materi memuat seluruh
    isi bacaannya, dan `list.index()` akan membandingkan isi itu baris demi
    baris untuk tiap kandidat. Semua pemanggil di dalam modul ini memang
    mengambil objeknya dari daftar yang sama, jadi lintasan pertama ini
    hampir selalu yang menjawab.

    Judulnya jadi cadangan, dan itu bukan kemewahan: `buka()` dipanggil dari
    luar modul ini juga. Pemanggil yang menyerahkan SALINAN dict materi -- dan
    menyalin dict adalah hal paling wajar yang dilakukan lapisan lain --
    dulu membuat materinya dianggap tidak dikenal, dan yang tidak dikenal
    berarti tidak pernah terkunci. Gagal ke arah "terbuka" tepat di titik
    penegakannya bukan pilihan. Judul materi dijamin unik dalam satu bahasa
    (lihat AGENTS.md), jadi pencocokan cadangan ini tidak pernah ambigu.
    """
    for i, m in enumerate(lang["materials"]):
        if m is obj:
            return i
    judul = obj.get("title") if isinstance(obj, dict) else None
    if judul:
        for i, m in enumerate(lang["materials"]):
            if m.get("title") == judul:
                return i
    return -1


def _tandai_kunci(hasil, data=None):
    """Isi bidang "kunci" tiap hasil: bab yang menguncinya, atau None.

    Statusnya dihitung sekali per BAHASA, bukan sekali per hasil: satu layar
    pencarian bisa memuat empat puluh baris dari bahasa yang sama, dan
    `bab.status()` menyusun ulang seluruh bab tiap kali dipanggil.

    `buka_semua` tidak diteruskan dengan sengaja -- setelan "buka semua bab"
    hanya dibaca bab.py, supaya daftar di sini dan daftar materi tidak pernah
    menjawab berbeda untuk materi yang sama.
    """
    if data is None:
        data = load_progress()
    singgahan = {}
    for h in hasil:
        h["kunci"] = None
        if h["tipe"] != "materi":
            continue
        lang = h["lang"]
        if lang["key"] not in singgahan:
            singgahan[lang["key"]] = bab.status(lang, data)
        indeks = _indeks_materi(lang, h["obj"])
        if indeks < 0:
            continue
        for b in singgahan[lang["key"]]:
            if b["awal"] <= indeks < b["akhir"]:
                if b["status"] == bab.TERKUNCI:
                    h["kunci"] = b
                break
    return hasil


def _tanda_kunci(h):
    """Penanda "terkunci" untuk satu baris daftar; "" kalau boleh dibuka.

    Berupa KATA, bukan sekadar warna: tema `mono` tidak punya warna sama
    sekali, dan penanda yang lenyap di satu tema sama saja dengan tidak ada.
    """
    return ("  " + tema.cat("[terkunci]", "peringatan")) if h.get("kunci") else ""


def _layar_terkunci(h):
    """Ganti isi materi dengan penjelasan kenapa ia belum boleh dibuka.

    Bukan penolakan kosong: judul, bab, dan tingkatnya tetap terlihat, lalu
    satu kalimat yang menyebut BERAPA materi lagi yang kurang. Orang yang
    sampai ke sini datang dari pencarian atau bookmark -- ia sudah tahu materi
    ini ada, jadi yang dibutuhkannya cuma tahu apa yang harus dikerjakan dulu.

    Kalimatnya dilewatkan `bungkus_baris`, bukan dicetak apa adanya. Layar ini
    menempelkan label bahasa, nomor bab, dan judul bab dalam satu baris, dan
    versi pertamanya meluber di terminal 80 kolom -- persis pada layar yang
    tugasnya menenangkan orang yang baru saja ditolak.

    Kalimat "kenapa" yang menyebut angka datang dari `bab.py` (`alasan`),
    bukan disusun ulang di sini. Yang ditulis di layar ini hanya aturannya
    secara umum plus penunjuk ke saklarnya -- kembarannya ada di
    `materials._layar_terkunci`, jadi kalau aturan membuka bab berubah,
    KEDUA layar itu harus ikut berubah.
    """
    b = h["kunci"]
    lbr = lebar() - 2
    clear()
    header("MATERI TERKUNCI", h["judul"])
    print()
    for baris in bungkus_baris(
            f"{h['lang']['label']} - Bab {b['nomor']}: {b['judul']}", lbr, "  "):
        print(tema.cat(baris, "info", tema.TEBAL))
    if b["ket"]:
        for baris in bungkus_baris(b["ket"], lbr, "  "):
            print(tema.cat(baris, "redup"))
    print(tema.cat(f"  Tingkat {b['label_tingkat']} - {b['jumlah']} materi", "redup"))
    print()
    if b["alasan"]:
        for baris in bungkus_baris(b["alasan"], lbr, "  "):
            print(tema.cat(baris, "peringatan"))
    for baris in bungkus_baris(
            bab.KALIMAT_ATURAN + " " + bab.KALIMAT_PINTU_DARURAT,
            lbr, "  "):
        print(tema.cat(baris, "redup"))
    press_enter()


def _potongan(teks, kata, lebar_potong=None):
    """Ambil sepotong teks di sekitar kata yang dicari, untuk pratinjau hasil."""
    lebar_potong = lebar_potong or max(30, lebar() - 12)
    posisi = teks.lower().find(kata.lower())
    if posisi < 0:
        return ""
    mulai = max(0, posisi - lebar_potong // 3)
    cuplik = teks[mulai:mulai + lebar_potong].replace("\n", " ").strip()
    awalan = "..." if mulai > 0 else ""
    akhiran = "..." if mulai + lebar_potong < len(teks) else ""
    return awalan + cuplik + akhiran


def _kumpulkan(languages, kata, tipe_diminta=None):
    """Cari `kata` di materi, kuis, dan latihan semua bahasa."""
    low = kata.lower()
    hasil = []

    for lang in languages:
        if tipe_diminta in (None, "materi"):
            for m in lang["materials"]:
                isi = teks_polos(m)
                if low in isi.lower():
                    hasil.append({
                        "tipe": "materi", "lang": lang, "obj": m,
                        "judul": m["title"], "jumlah": isi.lower().count(low),
                        "cuplikan": _potongan(isi, kata),
                    })
        if tipe_diminta in (None, "kuis"):
            for q in lang["quizzes"]:
                isi = q["title"] + "\n" + "\n".join(
                    s["q"] + " " + " ".join(s["options"]) + " " + s.get("explanation", "")
                    for s in q["questions"])
                if low in isi.lower():
                    hasil.append({
                        "tipe": "kuis", "lang": lang, "obj": q,
                        "judul": q["title"], "jumlah": isi.lower().count(low),
                        "cuplikan": _potongan(isi, kata),
                    })
        if tipe_diminta in (None, "latihan"):
            for e in lang["exercises"]:
                isi = (e["title"] + "\n" + "\n".join(e["question"]) + "\n"
                       + e.get("solution", ""))
                if low in isi.lower():
                    hasil.append({
                        "tipe": "latihan", "lang": lang, "obj": e,
                        "judul": e["title"], "jumlah": isi.lower().count(low),
                        "cuplikan": _potongan(isi, kata),
                    })

    hasil.sort(key=lambda h: -h["jumlah"])
    return hasil


def cari_global(languages):
    """Cari kata kunci di materi, kuis, dan latihan semua bahasa sekaligus."""
    clear()
    header("CARI DI SEMUA BAHASA")
    print(tema.cat("  Cari kata kunci di materi, soal kuis, dan latihan.", "redup"))
    print(tema.cat("  Contoh: 'perulangan', 'array', 'JOIN', 'pointer'", "redup"))
    print(rule("-", C.DIM, bold=False))

    kata = ask("  Kata kunci > ", "").strip()
    if len(kata) < 2:
        if kata:
            print(tema.cat("  Kata kunci minimal 2 huruf.", "galat"))
            press_enter()
        return

    tipe_diminta = None
    while True:
        semua = _kumpulkan(languages, kata, tipe_diminta)
        if not semua:
            clear()
            header("HASIL PENCARIAN", f"'{kata}'")
            saring = f" (disaring: {tipe_diminta})" if tipe_diminta else ""
            print(tema.cat(f"\n  Tidak ada yang cocok dengan '{kata}'{saring}.", "galat"))
            if tipe_diminta:
                tipe_diminta = None
                press_enter("Tekan ENTER untuk melihat semua tipe...")
                continue
            press_enter()
            return

        hasil = semua[:40]
        clear()
        judul_saring = f" - saringan: {tipe_diminta}" if tipe_diminta else ""
        header("HASIL PENCARIAN",
               f"'{kata}' - {len(hasil)} dari {len(semua)} hasil{judul_saring}")

        _tandai_kunci(hasil)
        names = []
        for h in hasil:
            tipe = tema.cat(f"{h['tipe']:<8}", WARNA_TIPE[h["tipe"]], tema.TEBAL)
            bahasa = tema.cat(f"{h['lang']['label']:<11}", "info")
            jumlah = tema.cat(f"({h['jumlah']}x)", "redup")
            baris = f"{tipe} {bahasa} {h['judul']}  {jumlah}{_tanda_kunci(h)}"
            if h["cuplikan"]:
                baris += "\n       " + sorot_kata(tema.cat(h["cuplikan"], "redup"), kata)
            names.append(baris)

        extra = {"m": "Hanya materi", "k": "Hanya kuis", "l": "Hanya latihan"}
        if tipe_diminta:
            extra["s"] = "Tampilkan semua tipe"

        pilih = ask_choice(paint("  Buka hasil nomor:", C.BLUE, C.BOLD), names, extra=extra)
        if pilih == 0:
            return
        if pilih in ("m", "k", "l"):
            tipe_diminta = {"m": "materi", "k": "kuis", "l": "latihan"}[pilih]
            continue
        if pilih == "s":
            tipe_diminta = None
            continue
        _buka(hasil[pilih - 1], kata)


def _buka(h, kata_sorot=""):
    lang = h["lang"]
    if h["tipe"] == "materi":
        # Dihitung ulang di sini, BUKAN dibaca dari tanda yang sudah menempel
        # di dict-nya. Dua alasan: daftar yang menandainya bisa sudah beberapa
        # menit umurnya, dan `buka` dipanggil dari luar modul ini dengan dict
        # yang bidang "kunci"-nya cuma klaim pemanggil. Titik penegakan yang
        # mempercayai masukannya bukan titik penegakan.
        _tandai_kunci([h])
        if h["kunci"]:
            _layar_terkunci(h)
            return
        render_material(h["obj"], f"{lang['key']}_materi", kata_sorot=kata_sorot,
                        daftar=lang["materials"])
    elif h["tipe"] == "kuis":
        # Lewat submenu, bukan langsung mulai: dari hasil pencarian orang
        # biasanya ingin melihat kuisnya dulu, bukan tiba-tiba diuji.
        menu_satu_kuis(h["obj"], f"{lang['key']}_kuis")
    else:
        show_exercise(h["obj"], f"{lang['key']}_latihan", lang.get("runner", lang["key"]))


def _cari_objek(languages, kategori, judul):
    """Temukan kembali materi/kuis/latihan dari kunci progres tersimpan."""
    if "_" not in kategori:
        return None
    key_bahasa, tipe = kategori.rsplit("_", 1)
    for lang in languages:
        if lang["key"] != key_bahasa:
            continue
        koleksi = {"materi": lang["materials"], "kuis": lang["quizzes"],
                   "latihan": lang["exercises"]}.get(tipe, [])
        for obj in koleksi:
            # Dibandingkan lewat judul_kunci, bukan judul mentah: kunci yang
            # tersimpan sudah tanpa nomor urut, sedangkan judul di kurikulum
            # masih membawanya. Menyamakan keduanya apa adanya membuat SETIAP
            # bookmark tampak basi.
            if judul_kunci(obj["title"]) == judul_kunci(judul):
                # Judul yang DITAMPILKAN diambil dari kurikulum, bukan dari
                # kunci yang tersimpan. Kunci sengaja tidak membawa nomor urut
                # supaya tahan penyisipan materi; nomor itu tetap bagian dari
                # cara materi ini dikenali di layar, dan nomor yang benar
                # hanya diketahui kurikulumnya sendiri.
                return {"tipe": tipe, "lang": lang, "obj": obj,
                        "judul": obj["title"]}
    return None


def _kunci_bookmark_valid(languages):
    """Semua kunci bookmark yang masih menunjuk konten yang ada."""
    sah = set()
    for lang in languages:
        for tipe, koleksi in (("materi", lang["materials"]),
                              ("kuis", lang["quizzes"]),
                              ("latihan", lang["exercises"])):
            for obj in koleksi:
                sah.add(kunci(f"{lang['key']}_{tipe}", obj["title"]))
    return sah


def menu_bookmark(languages):
    while True:
        clear()
        header("BOOKMARK", "Materi yang kamu tandai")

        data = load_progress()
        entri = []
        for k in data["bookmark"]:
            if "::" not in k:
                continue
            kategori, judul = k.split("::", 1)
            item = _cari_objek(languages, kategori, judul)
            if item:
                entri.append(item)

        basi = len(data["bookmark"]) - len(entri)

        if not entri:
            print(tema.cat("\n  Belum ada bookmark.", "redup"))
            print(tema.cat("  Buka materi apa pun, lalu tekan [b] untuk menyimpannya.",
                           "redup"))
            if basi:
                print(tema.cat(f"\n  Catatan: {basi} bookmark menunjuk materi yang "
                               "sudah tidak ada.", "peringatan"))
                if ask("  [x] bersihkan | [ENTER] kembali > ", "").lower() == "x":
                    jumlah = bersihkan_bookmark(_kunci_bookmark_valid(languages))
                    print(tema.cat(f"  {jumlah} bookmark basi dibuang.", "sukses"))
                    press_enter()
                    continue
                return
            press_enter()
            return

        if basi:
            print(tema.cat(f"  {basi} bookmark menunjuk materi yang sudah tidak ada.",
                           "peringatan"))

        # Bookmark ke materi terkunci terdengar mustahil -- menandainya memang
        # harus membukanya lebih dulu. Jalannya lewat saklar "buka semua bab":
        # nyalakan, tandai materi jauh di depan tanpa membacanya sampai habis,
        # matikan lagi. Bookmark-nya tetap ada, babnya menutup kembali.
        _tandai_kunci(entri, data)
        names = [f"{tema.cat(e['lang']['label'] + ':', 'info')} "
                 f"{tema.cat(e['tipe'], WARNA_TIPE[e['tipe']])} {e['judul']}"
                 f"{_tanda_kunci(e)}"
                 for e in entri]
        extra = {"x": f"Bersihkan {basi} bookmark tidak valid"} if basi else None
        pilih = ask_choice(paint("  Buka bookmark:", C.BLUE, C.BOLD), names, extra=extra)
        if pilih == 0:
            return
        if pilih == "x":
            jumlah = bersihkan_bookmark(_kunci_bookmark_valid(languages))
            print(tema.cat(f"  {jumlah} bookmark basi dibuang.", "sukses"))
            press_enter()
            continue
        _buka(entri[pilih - 1])


def lanjut_terakhir(languages):
    """Buka kembali materi/kuis/latihan yang terakhir dibuka."""
    data = load_progress()
    terakhir = data.get("terakhir") or {}
    if not terakhir.get("judul"):
        clear()
        header("LANJUTKAN BELAJAR")
        print(tema.cat("\n  Belum ada riwayat. Mulai dari menu bahasa dulu ya.", "redup"))
        press_enter()
        return

    item = _cari_objek(languages, terakhir.get("kategori", ""), terakhir["judul"])
    if not item:
        clear()
        header("LANJUTKAN BELAJAR")
        print(tema.cat("\n  Materi terakhir tidak ditemukan lagi (mungkin sudah diubah).",
                       "peringatan"))
        press_enter()
        return

    _tandai_kunci([item], data)

    # Tawarkan juga yang BERIKUTNYA: membuka ulang item yang sama terus-menerus
    # adalah keluhan paling sering tentang tombol "lanjutkan".
    berikut = None
    if item["tipe"] == "materi":
        daftar = item["lang"]["materials"]
        posisi = _indeks_materi(item["lang"], item["obj"])
        if 0 <= posisi < len(daftar) - 1:
            # Disimpan sebagai hasil utuh, bukan cuma dict materinya, supaya
            # yang membukanya nanti tetap lewat `_buka` -- satu jalan masuk,
            # satu penegakan. Menawarkan pintu yang akan ditolak lebih buruk
            # daripada tidak menawarkan apa pun, jadi tandanya dibaca di sini
            # untuk memutuskan tombolnya ditawarkan atau tidak.
            berikut = {"tipe": "materi", "lang": item["lang"],
                       "obj": daftar[posisi + 1],
                       "judul": daftar[posisi + 1]["title"]}
            _tandai_kunci([berikut], data)

    clear()
    header("LANJUTKAN BELAJAR")
    print(tema.cat(f"\n  Terakhir kamu buka ({item['tipe']}):", "redup"))
    print(tema.cat(f"    {item['lang']['label']} - {item['judul']}", "teks", tema.TEBAL))
    waktu = terakhir.get("waktu", "")
    if waktu:
        print(tema.cat(f"    pada {waktu.replace('T', ' ')}", "redup"))
    print()
    if item["kunci"]:
        # Jalannya sama seperti bookmark di atas: dibuka selagi "buka semua
        # bab" menyala, ditinggal sebelum tuntas, lalu saklarnya dimatikan.
        # Tanpa cabang ini, tombol "lanjutkan" menawarkan pintu yang akan
        # ditolaknya sendiri sedetik kemudian.
        print(tema.cat(f"  {item['kunci']['alasan']}", "peringatan"))
        print(tema.cat("  [ENTER] lihat kenapa terkunci", "aksen"))
    else:
        print(tema.cat("  [ENTER] buka lagi", "aksen"))
    if berikut and not berikut["kunci"]:
        print(tema.cat(f"  [n] materi berikutnya: {berikut['judul'][:40]}", "sukses"))
    elif berikut and berikut["kunci"] and not item["kunci"]:
        # Tanpa tanda kurung siku: ini keterangan, bukan pilihan yang bisa
        # ditekan. Menuliskannya sebagai "[n]" yang lalu tidak melakukan apa-apa
        # adalah cara tercepat membuat orang mengira aplikasinya rusak.
        #
        # Dilewati kalau yang sekarang pun terkunci: keduanya biasanya ada di
        # bab yang sama, jadi alasannya akan tercetak dua kali persis sama.
        print(tema.cat("  Materi berikutnya masih terkunci - "
                       f"{berikut['kunci']['alasan']}", "redup"))
    print(tema.cat("  [0] batal", "redup"))

    pilih = ask_atau_eof("  Pilih > ")
    if pilih is None or pilih == "0":
        return
    if pilih.lower() == "n" and berikut:
        # Dilewatkan `_buka` juga ketika tombolnya tidak ditawarkan: orang yang
        # terbiasa menekan [n] tetap menekannya sesudah membaca "masih
        # terkunci". Membuka ulang materi yang sama tanpa sepatah kata terbaca
        # sebagai tombol rusak, sedangkan `_buka` menjawabnya dengan alasannya.
        _buka(berikut)
        return
    _buka(item)


# Nama publik untuk pemanggil di luar modul ini.
buka = _buka
