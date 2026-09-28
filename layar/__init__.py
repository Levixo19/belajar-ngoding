"""Antarmuka terminal: yang dilihat dan ditekan orang di jendela hitam.

Satu-satunya lapisan yang boleh mencetak. Aturan belajarnya dipinjam dari
`pelajar/`, mesinnya dari `inti/` -- tidak ada keputusan "lulus" atau
"terkunci" yang lahir di sini.

    utils       primitif tampilan: paginasi, menu, input, pembungkus baris
    materials   layar materi (dua tingkat: daftar bab, lalu materinya)
    quiz        layar kuis
    exercises   layar latihan
    navigasi    pencarian, bookmark, "lanjutkan yang terakhir"

Catatan yang jujur soal `exercises.py`: ia juga dipakai `webapp/api.py` untuk
`bangun_tests` dan `DIR_KERJA`, jadi isinya belum sepenuhnya "layar". Itu
warisan, bukan rancangan -- dan memindahkannya sekarang berarti mengubah
perilaku, bukan sekadar merapikan berkas.
"""
