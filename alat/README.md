# alat/

Sebelas skrip baris perintah. Tidak satu pun diimpor aplikasi: semuanya
dijalankan dengan tangan, dan aplikasinya tetap jalan penuh tanpa folder ini.

Daftar ini ada karena folder ini sudah cukup besar untuk jadi lemari campur.
Nama berkas memberi tahu apa yang dijalankan; ia tidak memberi tahu KAPAN
harus dijalankan — dan yang paling mahal di repo ini justru alat yang lupa
dijalankan, karena lupa itu tidak menimbulkan error, cuma dua salinan data
yang mulai menyimpang.

## Yang WAJIB dijalankan ulang kalau sumbernya berubah

Keempatnya menghasilkan berkas yang ikut di-commit. Melupakannya memerahkan
`tests/test_konten_json.py` saat suite berikutnya jalan — itu disengaja.

| Alat | Menghasilkan | Jalankan ulang kalau |
|---|---|---|
| `ekspor_konten.py --tulis` | `packages/konten/` | apa pun di `data/` berubah |
| `ekspor_bersama.py --tulis` | `packages/bersama/data/` | `inti/sorot.py` atau `inti/berkas.py` berubah |
| `golden_bersama.py --tulis` | `packages/bersama/golden/` | `inti/sorot.py`, `galat.py`, atau `beda.py` berubah |
| `panen_pustaka.py` | `data/pustaka/` | repo sumbernya di `~/folder_materi` berubah |

`golden_bersama.py` tanpa `--tulis` MENOLAK kalau rekamannya bergeser, dan itu
jawaban yang benar: pergeseran yang tidak disengaja harus dicari dulu, bukan
diterima. Dengan `--tulis` ia mengganti rekamannya dan mengatakannya.

## Pemeriksa (hanya membaca, aman dijalankan kapan saja)

| Alat | Menjawab |
|---|---|
| `periksa_gaya.py [key] [judul]` | prosa materi masih bergaya ngobrol? (`panduan_gaya.md`) |
| `periksa_kuis.py` | jawaban benar tidak bisa ditebak dari bentuk opsinya? |
| `periksa_visual.py <key>` | gambar konsep lolos ke-13 pemeriksanya? |
| `uji_gigi_golden.py` | rekaman golden sisi Python bisa MERAH? |

Yang terakhir bukan tes biasa: ia merusak `sorot`/`berkas`/`isi` DI MEMORI lalu
menuntut rekamannya memerah. Pagar yang belum pernah terbukti merah belum
terbukti menjaga apa pun. Padanannya di sisi TypeScript
`packages/bersama/uji/gigi-golden.py`.

## Penulis konten (MENULIS ke `data/`, pakai hati-hati)

| Alat | Untuk |
|---|---|
| `ganti_badan.py naskah.txt --tulis` | mengganti field `body` materi, dan HANYA itu |
| `tambah_bagian.py` | menambah bagian "Di dunia nyata" di akhir materi |
| `rakit_kurikulum.py` | merakit kurikulum baru dari draf per bab |

Ketiganya menolak menulis kalau pemeriksaannya gagal — baris lebih dari 78
karakter, dash di prosa, blok `Keluaran:` yang berubah, judul yang bergeser.
Penolakan itu fiturnya: judul materi adalah bagian dari kunci progres, dan
judul yang berubah menghapus pencapaian orang tanpa satu pun tes gagal.
