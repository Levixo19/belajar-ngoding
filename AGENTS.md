# Catatan untuk agen

Aplikasi belajar pemrograman berbasis terminal, berbahasa Indonesia, **tanpa
dependensi eksternal**. Python 3.8+ dan stdlib saja. Jangan tambahkan paket
pihak ketiga — seluruh arsitektur mengandalkan ini (runner, penyorot sintaks,
diff, tema warna, semuanya ditulis tangan).

Semua nama fungsi, variabel, komentar, docstring, dan teks antarmuka memakai
**Bahasa Indonesia**. Ikuti gaya yang sudah ada.

Status: 9 bahasa, 166 materi, 57 kuis / 452 soal, 135 latihan (128 dinilai
otomatis), 464 tes.

## Menjalankan

```bash
python3 main.py

python3 -m unittest discover -s tests -t .                        # semua (~6 menit)
BELAJAR_SKIP_LAMBAT=1 python3 -m unittest discover -s tests -t .  # ~16 detik
BELAJAR_BAHASA=go python3 -m unittest tests.test_solutions        # satu bahasa
```

Tes lambat mengompilasi ratusan program latihan. Jalankan versi penuh sebelum
commit apa pun yang menyentuh `data/`, `runner.py`, atau `exercises.py`.

## Peta modul

| Modul | Tanggung jawab |
|---|---|
| `main.py` | Registry `LANGUAGES` + menu utama & dashboard |
| `utils.py` | Primitif tampilan: paginasi, menu, input, pembungkus baris |
| `tema.py` | Warna diminta lewat PERAN (`"galat"`, `"kode_kunci"`), bukan ANSI mentah |
| `sorot.py` | Penyorot sintaks 8 bahasa, pemindai token satu lintasan |
| `berkas.py` | Menentukan sebuah blok kode itu berkas, potongan, sesi, multi, atau ilustrasi |
| `runner.py` | Eksekusi kode berbatas waktu/memori + pencocokan output |
| `galat.py` | Menerjemahkan pesan compiler ke bahasa manusia |
| `beda.py` | Menjelaskan kenapa output pelajar berbeda |
| `progress.py` | Progres, XP, level, streak, badge, penjadwalan ulang |
| `konfigurasi.py` | Preferensi tampilan, sengaja TERPISAH dari progres |
| `saran.py` | Antrean "habis ini ngapain" |
| `materials.py` `quiz.py` `exercises.py` `navigasi.py` | Layar-layar aplikasi |

`utils.C` menyimpan ANSI mentah dan masih dipakai di beberapa tempat lama.
Untuk kode baru pakai `tema.cat(teks, "peran")`.

## Invarian yang gampang dilanggar

Semuanya dijaga tes. Kalau salah satu gagal, itu bukan tes yang cerewet —
itu bug yang akan menyakiti pelajar.

**Solusi latihan harus deterministik.** Auto-checker menurunkan kunci jawaban
dengan menjalankan solusi contoh. Bilangan acak, tanggal saat ini, iterasi map
Go, dan panggilan jaringan membuat latihan mustahil lulus. `test_solutions`
menjalankan tiap solusi dua kali dan membandingkannya.

**Latihan ber-`stdin` tidak boleh mencetak prompt.** Kalau solusi mencetak
`"Masukkan nilai: "`, teks itu ikut jadi bagian kunci jawaban, dan pelajar yang
menulis `input()` polos — yang justru lebih tepat — selalu dianggap salah.

**Latihan yang dinilai otomatis tidak boleh mengakses jaringan.** Pernah ada
solusi memanggil `fetch("https://api.contoh.com")`; yang sebenarnya diuji jadi
perilaku DNS mesin penilai. Tandai `auto_check: False`.

**Judul materi/kuis/latihan wajib unik dalam satu bahasa.** Kunci progres
berbentuk `"<key>_<tipe>::<judul>"`. Judul kembar berarti progres bertabrakan.

**`key` bahasa tidak boleh diubah setelah rilis.** Mengubahnya menghapus seluruh
progres pengguna untuk bahasa itu.

**Solusi harus mencetak sesuatu.** Kalau output kosong, kode kosong pun lolos.
Pakai field `verifikasi` untuk menampilkan kondisi akhir (lihat SQL Latihan 2).

**Nama berkas Java = nama kelas public.** Dijaga `berkas.py` dan diuji di
`test_berkas.py`.

## Menambah bahasa

1. Buat `data/<key>_materials.py`, `_quizzes.py`, `_exercises.py`.
2. Ekspor di `data/__init__.py`. Kuis WAJIB dibungkus `seimbangkan_kuis()`.
3. Tambah satu entri di `LANGUAGES` (`main.py`).
4. Kalau kodenya perlu dijalankan, tambah `Toolchain` di `runner.TOOLCHAINS`.
5. Kalau perlu penyorotan, tambah aturan di `sorot.py`.

`test_data.py` otomatis ikut memvalidasi konten baru.

### Field latihan

```python
{
    "title": "Latihan 1: ...",       # unik dalam satu bahasa
    "difficulty": "Mudah",           # Mudah | Sedang | Menengah | Sulit
    "question": ["baris soal", ...],
    "hints": ["hint 1", ...],
    "solution": "...",               # program lengkap, deterministik
    "stdin": "80\n",                 # opsional
    "stdin_list": ["1\n", "2\n"],    # opsional, beberapa kasus uji
    "mode": "persis",                # persis|abaikan_kapital|mengandung|regex|angka
    "setup": "...",                  # ditempel SEBELUM kode pelajar
    "verifikasi": "...",             # ditempel SESUDAH kode pelajar
    "auto_check": False,             # matikan penilaian otomatis
    "alasan_tidak_dicek": "...",     # wajib kalau auto_check False
}
```

## Keputusan yang mudah disalahpahami

**Posisi jawaban kuis dinormalisasi saat data dimuat** (`data/normalisasi.py`).
Konten aslinya sangat bias — pada C++ 55 dari 56 jawaban ada di opsi kedua.
Opsi DIPUTAR (bukan diacak) supaya urutannya tetap terbaca wajar. Jangan hapus
langkah ini; jangan pula menulis ulang 452 soal di source.

**SQL dijalankan dengan SQLite, bukan MySQL.** Materinya mengajarkan MySQL.
Latihan yang memakai `AUTO_INCREMENT`, `DELIMITER`, `TRIGGER`, atau
`START TRANSACTION` ditandai `auto_check: False`. Latihan lain memakai `setup`
karena tiap eksekusi memakai database kosong.

**7 latihan tidak dinilai otomatis** (Java 2, SQL 3, Python 1, JS 1). Ini
disengaja: butuh JUnit, JDBC, pytest, fitur khas MySQL, atau jaringan.
`test_solutions` menjaga rasionya tetap di bawah 10%.

**Materi dihitung selesai hanya kalau dibaca sampai habis.** Berhenti di tengah
ditandai `[~]` tanpa XP.

**`runner` bukan sandbox keamanan.** Ada batas CPU, memori, ukuran berkas, dan
panjang output supaya loop tak berujung tidak menggantung sistem, tapi kode
berjalan dengan hak akses user yang sama.

## Lingkungan mesin ini

Terpasang: `python3` `node` `javac/java` `gcc` `g++` `sqlite3` `bash`.
**Belum ada: `go`.** Latihan Go tetap ada tapi tidak terverifikasi kecuali Go
dipasang. Kalau perlu memverifikasi konten Go, pasang sementara:

```bash
curl -sL -o /tmp/go.tar.gz https://go.dev/dl/go1.23.4.linux-amd64.tar.gz
mkdir -p /tmp/goroot && tar -xzf /tmp/go.tar.gz -C /tmp/goroot --strip-components=1
PATH=/tmp/goroot/bin:$PATH GOCACHE=/tmp/gocache python3 -m unittest tests.test_solutions
```

Ekstrak ke direktori BERSIH. Mengekstrak ke atas instalasi Go lain akan
mencampur berkas antar versi dan menghasilkan error kompilasi yang menyesatkan
di dalam standard library.

## Lokasi data pengguna

| Apa | Di mana | Override |
|---|---|---|
| Progres | `~/.belajar_ngoding_progress.json` | `BELAJAR_PROGRESS_FILE` |
| Konfigurasi | `~/.belajar_ngoding_config.json` | `BELAJAR_CONFIG_FILE` |
| Kode jawaban | `~/belajar-ngoding/kerjaanku/` | `BELAJAR_WORKSPACE` |

Tes WAJIB mengarahkan `progress.PROGRESS_FILE` ke direktori sementara. Lihat
`tests/test_progress.py` kelas `BasisProgres`.
