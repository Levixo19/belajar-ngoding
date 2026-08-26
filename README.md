# Belajar Ngoding

Aplikasi belajar pemrograman berbasis terminal, berbahasa Indonesia, tanpa
dependensi apa pun di luar Python 3.8+.

Bedanya dengan tutorial biasa: latihan codingnya **benar-benar dijalankan dan
dinilai otomatis** dari output programmu, bukan sekadar "intip jawaban".

```
python3 main.py
```

## Isi

| Bahasa | Materi | Kuis | Soal | Latihan | Dinilai otomatis | Butuh |
|---|---:|---:|---:|---:|---:|---|
| Java | 26 | 7 | 60 | 15 | 13 | `javac` `java` |
| SQL | 13 | 7 | 57 | 12 | 9 | `sqlite3` |
| Python | 21 | 7 | 56 | 18 | 17 | `python3` |
| JavaScript | 21 | 7 | 56 | 18 | 18 | `node` |
| C | 21 | 7 | 56 | 18 | 18 | `gcc` |
| C++ | 21 | 7 | 56 | 18 | 18 | `g++` |
| Bash | 14 | 5 | 40 | 14 | 14 | `bash` |
| Go | 16 | 6 | 48 | 14 | 14 | `go` |
| **Total** | **153** | **53** | **429** | **127** | **121** | |

Toolchain bersifat opsional. Materi dan kuis tetap jalan penuh tanpa compiler
apa pun; yang mati hanya penilaian otomatis untuk bahasa bersangkutan, dan
aplikasi memberi tahu program apa yang perlu dipasang.

## Fitur

**Latihan yang dinilai otomatis.** Tulis kode di editor favoritmu (`$EDITOR`,
atau mode ketik langsung kalau tidak ada), lalu aplikasi mengompilasi,
menjalankan, dan membandingkan outputmu dengan kunci jawaban. Statusnya jadi
`LULUS` hanya kalau outputnya benar-benar cocok.

**Kunci jawaban tidak ditulis dua kali.** Ekspektasi diturunkan dengan
menjalankan solusi contoh, jadi soal dan kunci mustahil jadi tidak sinkron.

**Kuis yang tidak bisa ditebak.** Urutan soal dan opsi diacak, ada mode timer,
review jawaban salah, dan mode "ulangi yang salah saja".

**Pengulangan terjadwal.** Kuis yang sudah dikerjakan dijadwalkan ulang dengan
interval yang melar sesuai skormu, lalu ditandai `[saatnya diulang]`.

**Navigasi.** Pencarian kata kunci lintas 8 bahasa (materi, soal kuis, dan
latihan sekaligus), bookmark, dan "lanjutkan dari terakhir".

**Gamifikasi.** XP, level bergelar, streak harian, dan 14 badge.

## Struktur

```
main.py        registry bahasa + menu utama & dashboard
utils.py       helper tampilan terminal (warna, paginasi, menu, input)
progress.py    penyimpanan progres, XP, level, streak, badge, penjadwalan
runner.py      eksekusi kode berbatas waktu/memori + pencocokan output
materials.py   pembaca materi, bookmark, pencarian dalam satu bahasa
quiz.py        mesin kuis
exercises.py   latihan coding + auto-checker
navigasi.py    pencarian global, bookmark, lanjut terakhir
data/          konten kurikulum, 3 file per bahasa
tests/         138 tes
```

## Menambah bahasa baru

1. Buat `data/<bahasa>_materials.py`, `_quizzes.py`, `_exercises.py`.
2. Ekspor ketiganya di `data/__init__.py`.
3. Tambahkan satu entri di `LANGUAGES` pada `main.py`.
4. Kalau kodenya perlu bisa dijalankan, tambahkan `Toolchain` di
   `runner.TOOLCHAINS`.

`tests/test_data.py` otomatis ikut memvalidasi konten baru itu.

### Format data latihan

```python
{
    "title": "Latihan 1: ...",       # wajib unik dalam satu bahasa
    "difficulty": "Mudah",           # Mudah | Sedang | Menengah | Sulit
    "question": ["baris soal", ...],
    "hints": ["hint 1", ...],        # dibuka bertahap oleh user
    "solution": "...",               # program lengkap yang bisa dijalankan
    "stdin": "80\n",                 # opsional: input untuk program
    "stdin_list": ["1\n", "2\n"],    # opsional: beberapa kasus uji
    "mode": "persis",                # persis|abaikan_kapital|mengandung|regex|angka
    "setup": "...",                  # opsional: kode prasyarat, ditempel di depan
    "verifikasi": "...",             # opsional: kode pemeriksa, ditempel di belakang
    "auto_check": False,             # opsional: matikan penilaian otomatis
    "alasan_tidak_dicek": "...",     # wajib kalau auto_check False
}
```

Aturan penting: **output solusi harus deterministik**. Bilangan acak, tanggal
saat ini, dan iterasi map di Go akan membuat latihan mustahil lulus.
`tests/test_solutions.py` menjalankan tiap solusi dua kali untuk memastikannya.

## Menjalankan tes

```bash
python3 -m unittest discover -s tests -t .              # semua (lambat, kompilasi ratusan program)
BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .   # lewati verifikasi solusi
BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions          # satu bahasa saja
```

Yang diperiksa:

- **test_data** struktur konten, judul unik, index jawaban valid, sebaran
  posisi jawaban merata
- **test_progress** simpan/muat, migrasi skema lama, XP, level, streak, badge,
  penjadwalan ulang
- **test_runner** eksekusi, timeout, batas output, mode pencocokan
- **test_solutions** tiap solusi contoh berjalan, mencetak output,
  deterministik, dan lolos auto-checker-nya sendiri
- **test_ui** helper tampilan + smoke test alur aplikasi lewat stdin palsu

## Lokasi data

| Apa | Di mana | Ubah lewat |
|---|---|---|
| Progres belajar | `~/.belajar_ngoding_progress.json` | `BELAJAR_PROGRESS_FILE` |
| Kode jawabanmu | `~/belajar-ngoding/kerjaanku/` | `BELAJAR_WORKSPACE` |

Progres dari versi lama (`~/.belajar_java_progress.json`) dibaca dan dimigrasi
otomatis pada peluncuran pertama.

## Catatan keamanan

Runner membatasi waktu CPU, memori, ukuran file, dan panjang output supaya kode
pemula yang keliru (misalnya loop tak berujung) tidak menggantung sistem.

Ini **bukan sandbox keamanan**. Kode berjalan dengan hak akses user yang sama
dengan aplikasi. Jangan menjalankan kode dari sumber yang tidak kamu percaya.
