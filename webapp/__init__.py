"""Antarmuka web lokal untuk aplikasi belajar pemrograman.

Paket ini TIDAK menyalin logika apa pun dari aplikasi terminal. Ia memakai
modul yang sudah ada apa adanya dan hanya menambahkan lapisan penyajian:
mengubah hasilnya jadi JSON, lalu menyajikan satu halaman web yang
memanggilnya. Yang dipinjam, beserta paketnya:

    inti/      runner, sorot, beda, galat, berkas
    pelajar/   progress, bab, konfigurasi, saran
    layar/     exercises  -- lihat catatannya di bawah
    main       registry LANGUAGES

`layar/exercises` adalah satu-satunya yang dipinjam dari lapisan TERMINAL, dan
itu bukan rancangan melainkan warisan: `bangun_tests`, `DIR_KERJA`, dan
`_kerangka` yang dipakai di sini logika latihan, bukan tampilan. Memindahkannya
berarti mengubah perilaku, bukan sekadar merapikan berkas.

Konsekuensinya disengaja: progres yang dicatat lewat web dan lewat terminal
adalah progres yang SAMA, di berkas yang sama, dengan kunci yang sama. Dua
antarmuka, satu catatan belajar.

Tetap tanpa dependensi luar -- `http.server` dari pustaka standar.
"""

VERSI_WEB = "1.0"

__all__ = ["VERSI_WEB"]
