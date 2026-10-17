"""Melacak jalannya program Python baris demi baris ("Lihat jalannya").

Pemula paling sering tersandung bukan di sintaks, tapi di gambaran mental
tentang apa yang terjadi di dalam mesin: variabel mana berisi apa, kapan
fungsi dipanggil dan kembali, kenapa dua nama "ikut berubah" bersamaan. Prosa
cuma bisa menceritakannya; modul ini memperlihatkannya. Kode dijalankan
sungguhan dengan `sys.settrace`, dan tiap peristiwa (baris akan dijalankan,
fungsi dipanggil, fungsi kembali, galat) dicatat bersama isi seluruh tumpukan
pemanggilan dan panjang keluaran sejauh itu.

Ini BUKAN penilai. Tidak ada definisi "lulus" di sini, dan tidak ada yang
menyentuh progres; definisi lulus tetap satu, `runner.periksa`.

Pagarnya sama dengan tombol Jalankan: proses terpisah lewat `runner._proses`
(batas waktu, memori, ukuran berkas, grup proses dibunuh sesudahnya), di
direktori sementara. Jumlah langkah dibatasi MAKS_LANGKAH; program yang lebih
panjang DIHENTIKAN di situ (bukan dilanjutkan tanpa dicatat), supaya keluaran
yang ditampilkan selalu cocok dengan langkah yang terlihat.
"""

import json
import os

from inti import runner

MAKS_LANGKAH = 400
MAKS_BYTE_HASIL = 4 * 1024 * 1024

# Skrip yang dijalankan di proses anak. Ditulis sebagai teks karena ia harus
# berdiri sendiri: `python3 -I` tidak bisa mengimpor paket aplikasi ini.
_PELACAK = r'''
import builtins, io, json, os, reprlib, sys, types

NAMA = "<kode>"
MAKS_REPR = 80
MAKS_KELUAR = 20000


class _Berhenti(BaseException):
    """Bukan Exception: `except Exception` milik pelajar tidak menelannya."""


def main():
    jalur, maks, tujuan = sys.argv[1], int(sys.argv[2]), sys.argv[3]
    with open(jalur, encoding="utf-8") as f:
        sumber = f.read()
    asli = sys.stdout
    tangkap = io.StringIO()
    langkah, nomor_objek, simpan = [], {}, []
    terpotong = False
    # reprlib, bukan repr(): repr list dua juta angka dibangun utuh dulu baru
    # dipotong, di SETIAP langkah, dan pelacaknya kehabisan waktu.
    ringkasan = reprlib.Repr()
    ringkasan.maxstring = ringkasan.maxother = MAKS_REPR
    ringkasan.maxlist = ringkasan.maxtuple = ringkasan.maxset = ringkasan.maxdict = 12
    hasil = {"langkah": langkah, "galat": None, "baris_galat": None}

    def tulis(akhir_keluaran):
        teks = tangkap.getvalue()[:akhir_keluaran]
        hasil.update(keluaran=teks[:MAKS_KELUAR], terpotong=terpotong)
        # ensure_ascii: karakter yang tidak bisa dikodekan (surrogate tunggal
        # dari print pelajar) tidak boleh memotong berkas di tengah jalan.
        data = json.dumps(hasil, ensure_ascii=True)
        with open(tujuan, "w", encoding="ascii") as f:
            f.write(data)

    def ringkas(v):
        try:
            r = ringkasan.repr(v)
        except Exception:
            r = "<" + type(v).__name__ + ">"
        if len(r) > MAKS_REPR:
            r = r[:MAKS_REPR - 3] + "..."
        hasil = {"r": r, "t": type(v).__name__}
        bisa_berubah = isinstance(v, (list, dict, set, bytearray)) or (
            hasattr(v, "__dict__") and not isinstance(
                v, (types.FunctionType, types.BuiltinFunctionType, type,
                    types.ModuleType, types.MethodType)))
        if bisa_berubah:
            k = id(v)
            if k not in nomor_objek:
                nomor_objek[k] = len(nomor_objek) + 1
                simpan.append(v)   # tahan supaya id() tidak dipakai ulang
            hasil["id"] = nomor_objek[k]
        return hasil

    def isi_bingkai(frame):
        sumber_nama = frame.f_globals if frame.f_code.co_name == "<module>" else frame.f_locals
        keluar = {}
        for k, v in list(sumber_nama.items()):
            if k.startswith("__") or isinstance(v, types.ModuleType):
                continue
            if isinstance(v, types.FunctionType):
                keluar[k] = {"r": "fungsi " + v.__name__ + "()", "t": "function"}
            elif isinstance(v, type):
                keluar[k] = {"r": "class " + v.__name__, "t": "type"}
            else:
                keluar[k] = ringkas(v)
        return keluar

    def tumpukan(frame):
        rantai, f = [], frame
        while f is not None:
            if f.f_code.co_filename == NAMA:
                rantai.append(f)
            f = f.f_back
        rantai.reverse()
        return [{"nama": "program utama" if b.f_code.co_name == "<module>" else b.f_code.co_name,
                 "baris": b.f_lineno, "isi": isi_bingkai(b)} for b in rantai]

    def catat(frame, peristiwa, tambahan=None):
        nonlocal terpotong
        if len(langkah) >= maks:
            # Batas langkah: rekam lalu KELUAR saat itu juga. Melempar
            # exception tidak cukup, karena `except:` milik pelajar bisa
            # menelannya dan programnya jalan terus tanpa dicatat.
            terpotong = True
            sys.settrace(None)
            sys.stdout = asli
            tulis(tangkap.tell())
            os._exit(0)
        s = {"baris": frame.f_lineno, "p": peristiwa, "tumpukan": tumpukan(frame),
             "keluar": tangkap.tell()}
        if tambahan:
            s.update(tambahan)
        langkah.append(s)

    def lacak(frame, peristiwa, arg):
        if frame.f_code.co_filename != NAMA:
            return None
        if peristiwa == "line":
            catat(frame, "baris")
        elif peristiwa == "call":
            if frame.f_code.co_name != "<module>":
                catat(frame, "panggil")
        elif peristiwa == "return":
            if frame.f_code.co_name != "<module>":
                catat(frame, "kembali", {"nilai": ringkas(arg)})
        elif peristiwa == "exception":
            jenis, nilai, _tb = arg
            if not issubclass(jenis, _Berhenti):
                catat(frame, "galat", {"galat": jenis.__name__ + ": " + str(nilai)})
        return lacak

    try:
        kode = compile(sumber, NAMA, "exec")
    except SyntaxError as e:
        hasil.update(galat="SyntaxError: " + str(e.msg), baris_galat=e.lineno)
        kode = None
    if kode is not None:
        ruang = {"__name__": "__main__", "__builtins__": builtins}
        sys.stdout = tangkap
        sys.settrace(lacak)
        try:
            exec(kode, ruang)
        except _Berhenti:
            pass
        except SystemExit:
            pass
        except BaseException as e:
            tb, baris = e.__traceback__, None
            while tb is not None:
                if tb.tb_frame.f_code.co_filename == NAMA:
                    baris = tb.tb_lineno
                tb = tb.tb_next
            hasil.update(galat=type(e).__name__ + ": " + str(e), baris_galat=baris)
        finally:
            sys.settrace(None)
            sys.stdout = asli
    # Hasil ke BERKAS, bukan stdout: runner memotong stdout di 20.000
    # karakter, dan 400 langkah lengkap dengan tumpukannya jauh lebih besar.
    tulis(None)


main()
'''


def _terjemah_galat(galat):
    """Galat yang paling sering muncul di sini diberi kalimat manusia."""
    if not galat:
        return None
    if galat.startswith("EOFError"):
        return ("Program ini menunggu masukan (input), dan di sini tidak ada "
                "yang mengetikkannya. Coba di Ruang Coba dengan stdin.")
    return galat


def lacak(kode, maks=MAKS_LANGKAH, timeout=None):
    """Jalankan `kode` Python sambil mencatat tiap langkahnya.

    Kembalikan dict: langkah, keluaran, galat (teks atau None), baris_galat,
    terpotong (langkah melewati `maks`), timeout. `langkah[i]` berisi baris,
    peristiwa ("baris" | "panggil" | "kembali" | "galat"), tumpukan bingkai
    (nama, baris, isi variabel), dan `keluar`: panjang keluaran SEBELUM
    langkah itu, jadi layar bisa menampilkan keluaran sejauh langkah itu.
    """
    tc = runner.TOOLCHAINS["python"]
    if timeout is None:
        timeout = tc.batas_waktu
    with runner._tempdir() as d:
        pelacak = os.path.join(d, "pelacak.py")
        sumber = os.path.join(d, "kode.py")
        with open(pelacak, "w", encoding="utf-8") as f:
            f.write(_PELACAK)
        with open(sumber, "w", encoding="utf-8", errors="replace") as f:
            f.write(kode)
        tujuan = os.path.join(d, "hasil.json")
        rc, out, err, to = runner._proses(
            ["python3", "-I", pelacak, sumber, str(int(maks)), tujuan],
            d, tc, timeout)
        mentah = None
        if not to and os.path.exists(tujuan):
            with open(tujuan, "rb") as f:
                mentah = f.read(MAKS_BYTE_HASIL + 1)
    if to:
        return {"langkah": [], "keluaran": "", "galat": (
            f"Program dihentikan setelah {timeout} detik. Kemungkinan ada "
            "loop yang tidak pernah berhenti."), "baris_galat": None,
            "terpotong": False, "timeout": True}
    kosong = {"langkah": [], "keluaran": "", "baris_galat": None,
              "terpotong": False, "timeout": False}
    if mentah and len(mentah) > MAKS_BYTE_HASIL:
        return {**kosong, "galat": ("Rekamannya terlalu besar untuk ditampilkan. "
                                    "Coba dengan data yang lebih kecil.")}
    if not mentah:
        return {**kosong, "galat": (err.strip() or "Pelacak berhenti tanpa hasil.")[-800:]}
    try:
        hasil = json.loads(mentah.decode("ascii"))
    except (ValueError, UnicodeDecodeError):
        return {**kosong, "galat": (err.strip() or "Rekaman pelacak rusak di tengah jalan.")[-800:]}
    hasil["galat"] = _terjemah_galat(hasil.get("galat"))
    hasil["timeout"] = False
    return hasil
