"""Mesin aplikasi: menjalankan kode, membacanya, dan menerjemahkan hasilnya.

Tidak ada satu pun modul di sini yang tahu ada antarmuka terminal atau web.
Itu syarat yang membuat kedua antarmuka bisa memakai jawaban yang sama persis:
begitu sebuah aturan pindah ke sini, tidak ada lagi tempat kedua yang bisa
berbeda pendapat tentangnya.

    runner     eksekusi kode berbatas waktu/memori + pencocokan output
    struktur   HTML & CSS dibaca jadi pohon -- itu "keluaran" kedua bahasa itu
    sorot      penyorot sintaks 10 bahasa
    berkas     sebuah blok kode itu berkas utuh, potongan, sesi, atau ilustrasi
    galat      pesan compiler -> bahasa manusia
    beda       kenapa keluaran pelajar berbeda dari yang diharapkan
    tema       warna diminta lewat PERAN ("galat", "kode_kunci"), bukan ANSI mentah

`struktur.py` sengaja duduk BERSEBELAHAN dengan `runner.py`: runner
memanggilnya sebagai subprocess lewat `dirname(__file__)`, jadi memisahkan
keduanya diam-diam mematikan penilaian seluruh latihan HTML dan CSS.
"""
