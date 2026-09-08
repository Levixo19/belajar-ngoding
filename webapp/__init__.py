"""Antarmuka web lokal untuk aplikasi belajar pemrograman.

Paket ini TIDAK menyalin logika apa pun dari aplikasi terminal. Ia memakai
modul yang sudah ada (`progress`, `runner`, `exercises`, `sorot`, `beda`,
`galat`, `berkas`, `saran`, `konfigurasi`) apa adanya dan hanya menambahkan
lapisan penyajian: mengubah hasilnya jadi JSON, lalu menyajikan satu halaman
web yang memanggilnya.

Konsekuensinya disengaja: progres yang dicatat lewat web dan lewat terminal
adalah progres yang SAMA, di berkas yang sama, dengan kunci yang sama. Dua
antarmuka, satu catatan belajar.

Tetap tanpa dependensi luar -- `http.server` dari pustaka standar.
"""

VERSI_WEB = "1.0"

__all__ = ["VERSI_WEB"]
