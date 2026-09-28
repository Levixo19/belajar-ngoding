"""Keadaan dan aturan yang melekat pada seorang pelajar.

Yang disimpan di sini milik orangnya, bukan milik aplikasi: berapa jauh ia
sudah sampai, bab mana yang terbuka, dan apa yang sebaiknya dikerjakan
berikutnya.

    progress      progres, XP, level, streak, badge, penjadwalan ulang
    bab           bab mana yang terbuka -- SATU-SATUNYA yang memutuskan penguncian
    konfigurasi   preferensi tampilan, sengaja TERPISAH dari progres
    saran         antrean "habis ini ngapain"

`konfigurasi` terpisah dari `progress` bukan karena rapi, melainkan karena
`progress.reset()` ada dan orang memakainya: preferensi yang menumpang di
berkas progres akan ikut terbakar saat seseorang mengosongkan nilainya.
"""
