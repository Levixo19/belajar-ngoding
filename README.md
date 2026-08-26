# Belajar Ngoding

Aplikasi belajar pemrograman berbasis terminal, berbahasa Indonesia, tanpa
dependensi apa pun di luar Python 3.8+.

Bedanya dengan tutorial biasa: latihan codingnya **benar-benar dijalankan dan
dinilai otomatis** dari output programmu, bukan sekadar "intip jawaban" — dan
kalau salah, aplikasi menunjukkan **baris dan kolom mana** yang berbeda,
lengkap dengan tebakan penyebabnya.

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
apa pun; yang mati hanya penilaian otomatis untuk bahasa bersangkutan — dan
aplikasi memberi tahu **perintah persis** untuk memasangnya di sistemmu:

```
python3 main.py --cek-toolchain
```

Latihan bahasa yang toolchain-nya belum ada tetap bisa dikerjakan dan ditandai
selesai secara manual, jadi progresnya tidak mentok di 0%.

## Fitur

**Latihan yang dinilai otomatis.** Tulis kode di editor favoritmu (`$EDITOR`,
atau mode ketik langsung kalau tidak ada), lalu aplikasi mengompilasi,
menjalankan, dan membandingkan outputmu dengan kunci jawaban. Statusnya jadi
`LULUS` hanya kalau outputnya benar-benar cocok **dan** programnya berakhir
normal.

**Umpan balik yang mengajar, bukan sekadar "GAGAL".** Kegagalan ditampilkan
sebagai diff bernomor baris dengan penunjuk kolom pertama yang berbeda, plus
diagnosis dalam bahasa manusia:

```
    1 │ Halo, namaku Andi!
    2 - Aku sedang belajar Python.   (diharapkan)
    2 + aku sedang belajar python.   (punyamu)
        ^ beda mulai kolom 1

  → Isinya sudah benar, hanya beda HURUF BESAR/KECIL.
```

Spasi tersembunyi ditampilkan sebagai `·` dan tab sebagai `→` saat dua baris
terlihat sama padahal tidak.

**Pesan error diterjemahkan.** `';' expected` jadi *"Ada baris yang lupa
diakhiri titik koma"*, path direktori sementara diganti nama berkas kerjamu,
dan nomor barisnya digeser supaya cocok dengan berkas yang benar-benar kamu
edit. Ada 50+ pola untuk delapan bahasa.

**Kunci jawaban tidak ditulis dua kali.** Ekspektasi diturunkan dengan
menjalankan solusi contoh, jadi soal dan kunci mustahil jadi tidak sinkron.
Latihan bercabang diuji dengan beberapa input sekaligus, sehingga jawaban yang
di-hardcode tidak bisa lolos.

**Contoh kode bersorot sintaks** untuk kedelapan bahasa — kata kunci, string,
komentar, angka, dan nama fungsi diwarnai berbeda, tanpa dependensi apa pun.

**Kuis yang tidak bisa ditebak.** Urutan soal dan opsi diacak, ada mode timer,
review jawaban salah, dan mode "ulangi yang salah saja" (yang tidak menyentuh
skor terbaikmu).

**Pengulangan terjadwal.** Kuis yang sudah dikerjakan dijadwalkan ulang dengan
interval yang melar sesuai skormu, lalu ditandai `[saatnya diulang]`.

**Penunjuk arah.** Menu utama menampilkan *Langkah berikutnya* yang disusun
dari progresmu sendiri — kuis yang jatuh tempo dulu, lalu materi yang berhenti
di tengah, lalu materi/latihan/kuis berikutnya di bahasa yang sedang kamu
pelajari. Ada juga **tantangan harian** yang berganti tiap hari.

**Navigasi.** Pencarian kata kunci lintas 8 bahasa dengan saringan tipe dan
kata kunci tersorot di hasilnya, bookmark, dan "lanjutkan dari terakhir" yang
juga menawarkan materi *berikutnya*.

**Gamifikasi.** XP, level bergelar, streak harian, target XP harian, heatmap
aktivitas 13 pekan, dan 22 badge.

**Bisa diatur.** Tema warna (gelap/terang/kontras tinggi/mono), kedalaman
warna, lebar layar, tinggi halaman, durasi timer, editor, dan target harian —
semua lewat menu Pengaturan, tersimpan di `~/.belajar_ngoding_config.json`.
Tampilannya mengikuti lebar terminal secara otomatis.

## Baris perintah

```
python3 main.py                    menu interaktif
python3 main.py --bantuan          daftar semua opsi
python3 main.py --cek-toolchain    compiler apa yang sudah/belum terpasang
python3 main.py --statistik        ringkasan progres, lalu keluar
python3 main.py --laporan          laporan kemajuan Markdown ke layar
python3 main.py --laporan x.md     ...atau ke berkas
python3 main.py --bahasa go        langsung buka satu bahasa
python3 main.py --tema terang      paksa tema
python3 main.py --tanpa-warna      matikan warna (juga hormati NO_COLOR)
python3 main.py --ekspor p.json    ekspor progres
python3 main.py --impor p.json     impor progres (progres lama dicadangkan)
```

## Struktur

```
main.py          registry bahasa + menu utama, dashboard, pengaturan, CLI
utils.py         helper tampilan terminal (lebar responsif, input, paginasi)
tema.py          palet warna: deteksi kemampuan terminal + 4 tema
sorot.py         penyorot sintaks 8 bahasa (pemindai token satu lintasan)
beda.py          diff output harapan vs hasil + diagnosis penyebabnya
galat.py         penerjemah pesan error compiler/runtime ke bahasa Indonesia
konfigurasi.py   preferensi pengguna yang bertahan antar sesi
progress.py      progres, XP, level, streak, badge, penjadwalan, ekspor/impor
runner.py        eksekusi kode berbatas waktu/memori + pencocokan output
materials.py     pembaca materi, bookmark, pencarian dalam satu bahasa
quiz.py          mesin kuis
exercises.py     latihan coding + auto-checker
saran.py         rekomendasi langkah berikutnya & tantangan harian
navigasi.py      pencarian global, bookmark, lanjut terakhir
data/            konten kurikulum, 3 file per bahasa
tests/           412 tes
```

## Menambah bahasa baru

1. Buat `data/<bahasa>_materials.py`, `_quizzes.py`, `_exercises.py`.
2. Ekspor ketiganya di `data/__init__.py`.
3. Tambahkan satu entri di `LANGUAGES` pada `main.py`.
4. Kalau kodenya perlu bisa dijalankan, tambahkan `Toolchain` di
   `runner.TOOLCHAINS` — termasuk field `instalasi` per sistem operasi.
5. Tambahkan aturan leksikal di `sorot.ATURAN` supaya contoh kodenya tersorot.

`tests/test_data.py`, `tests/test_sorot.py`, dan `tests/test_solutions.py`
otomatis ikut memvalidasi konten baru itu.

### Format data latihan

```python
{
    "title": "Latihan 1: ...",       # wajib unik dalam satu bahasa
    "difficulty": "Mudah",           # Mudah | Menengah | Lanjut | Sulit
    "question": ["baris soal", ...],
    "hints": ["hint 1", ...],        # dibuka bertahap; MENUNTUN, bukan jawaban
    "solution": "...",               # program lengkap yang bisa dijalankan
    "stdin": "80\n",                 # opsional: satu input untuk program
    "stdin_list": ["80\n", "60\n"],  # lebih baik: beberapa kasus uji
    "mode": "persis",                # persis|abaikan_kapital|mengandung|regex|angka
    "setup": "...",                  # opsional: kode prasyarat, ditempel di depan
    "verifikasi": "...",             # opsional: kode pemeriksa, ditempel di belakang
    "auto_check": False,             # opsional: matikan penilaian otomatis
    "alasan_tidak_dicek": "...",     # wajib kalau auto_check False
}
```

Aturan penting:

- **Output solusi harus deterministik.** Bilangan acak, tanggal saat ini, dan
  iterasi map di Go akan membuat latihan mustahil lulus.
  `tests/test_solutions.py` menjalankan tiap solusi dua kali untuk memastikannya.
- **Latihan yang membaca input tidak boleh mencetak teks ajakan** sebelum
  pembacaan pertama — teks itu akan ikut jadi bagian kunci jawaban.
- **Latihan bercabang wajib pakai `stdin_list`** dengan input yang benar-benar
  menempuh cabang berbeda. Dengan satu input saja, jawaban yang di-hardcode
  ikut dinyatakan benar.

## Menjalankan tes

```bash
python3 -m unittest discover -s tests -t .              # semua (lambat, kompilasi ratusan program)
BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .   # lewati verifikasi solusi
BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions          # satu bahasa saja
```

Yang diperiksa:

- **test_data** struktur konten, judul unik, index jawaban valid, sebaran
  posisi jawaban merata, larangan mencetak prompt sebelum membaca input
- **test_progress** simpan/muat, migrasi skema lama, ketahanan terhadap berkas
  rusak *bertipe salah*, XP, level, streak, badge, penjadwalan, ekspor/impor
- **test_runner** eksekusi, timeout, batas memori/berkas/output, pembunuhan
  proses cucu, mode aman SQLite, exit code ikut dinilai
- **test_solutions** tiap solusi contoh berjalan, mencetak output, deterministik,
  dan lolos auto-checker-nya sendiri — dengan bahasa tanpa toolchain dilaporkan
  sebagai `skipped`, bukan dilewati diam-diam
- **test_quiz** pemetaan ulang jawaban setelah opsi diacak, EOF, sesi ulang yang
  tidak merusak skor
- **test_navigasi** pencarian, bookmark basi, lanjut terakhir
- **test_sorot** keutuhan tokenizer atas SELURUH kode di kurikulum
- **test_beda** diff & diagnosis, kesepakatan dengan `runner.normalisasi`
- **test_galat** terjemahan error & penggeseran nomor baris
- **test_konfigurasi** validasi nilai ngawur, tema, kedalaman warna
- **test_saran** urutan prioritas rekomendasi & stabilitas tantangan harian
- **test_ui** helper tampilan + smoke test alur aplikasi lewat stdin palsu

## Lokasi data

| Apa | Di mana | Ubah lewat |
|---|---|---|
| Progres belajar | `~/.belajar_ngoding_progress.json` | `BELAJAR_PROGRESS_FILE` |
| Pengaturan | `~/.belajar_ngoding_config.json` | `BELAJAR_CONFIG_FILE` |
| Kode jawabanmu | `~/belajar-ngoding/kerjaanku/` | `BELAJAR_WORKSPACE` |

Progres dari versi lama (`.belajar_java_progress.json` di folder yang sama)
dibaca dan dimigrasi otomatis pada peluncuran pertama. Berkas progres yang
rusak — termasuk yang bertipe salah karena diedit tangan — tidak akan
menghentikan aplikasi; field yang rusak diganti nilai bawaan, sisanya
dipertahankan.

## Catatan keamanan

Runner membatasi waktu CPU, memori, ukuran file, dan panjang output supaya kode
pemula yang keliru (misalnya loop tak berujung) tidak menggantung sistem.
Keluaran program ditulis ke berkas di dalam direktori sementara, bukan ditampung
di memori aplikasi, dan seluruh process group dibunuh saat timeout sehingga
proses cucu tidak ada yang selamat. Latihan SQL dijalankan dengan `sqlite3 -safe`
kalau versinya mendukung, sehingga dot-command tidak bisa menulis di luar
direktori sementara.

Ini tetap **bukan sandbox keamanan**. Kode berjalan dengan hak akses user yang
sama dengan aplikasi. Jangan menjalankan kode dari sumber yang tidak kamu
percaya.
