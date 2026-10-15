# Panduan gaya menulis materi

Untuk siapa pun yang menulis atau menulis ulang prosa materi di `data/*_materials.py`.
Ukur hasilnya dengan `python3 alat/periksa_gaya.py`, tulis lewat
`python3 alat/ganti_badan.py naskah.txt --tulis`.

Pemiliknya bilang terus terang: kalau materinya terasa ditulis AI dan
membingungkan, ia lebih baik belajar di situs berbayar. Panduan ini ada supaya
itu tidak terjadi.

## Pembacanya

Orang Indonesia yang baru belajar pemrograman. Ia belum tahu istilahnya, belum
punya gambaran mesinnya, dan sering belajar sendirian malam hari sesudah kerja
atau kuliah. Ia tidak butuh dikagumi; ia butuh mengerti, lalu bisa mencoba.

Bayangkan kamu duduk di sebelahnya dan menjelaskan dengan sabar, seperti
teman yang sudah lebih dulu bisa.

## Nadanya: ngobrol (dipilih pemilik, 2026-10-15)

Pemilik membandingkan tiga nada (baku, ngobrol, ringkas) dan memilih
NGOBROL. Patokannya kalimat ini:

    Kenapa tag harus ditutup? Gampangnya, tag pembuka itu cuma bilang
    "mulai dari sini". Kalau nggak ada penutupnya, browser bingung
    elemennya selesai di mana, jadi dia nebak sendiri.

    Masalahnya, browser nggak pernah protes. Halamannya tetap tampil,
    kelihatan hampir benar, dan kamu nggak dikasih tahu salahnya di mana.

Ciri-cirinya:

- **"nggak" untuk tidak, di seluruh prosa.** Konsisten; jangan dicampur
  "tidak" dan "nggak" di paragraf yang sama. Pengecualian: label aturan dan
  isi tabel/contoh boleh tetap "tidak".
- **Kata sehari-hari yang wajar:** cuma, aja, bikin, kasih, pakai, gampangnya,
  intinya, masalahnya, ternyata, biasanya, misalnya. Kata kerja bentuk lisan
  boleh (nebak, ngecek, nyimpen) asal tidak tiap kalimat.
- **Browser, program, atau komputer boleh disebut "dia"** kalau bikin kalimat
  lebih enak dibaca.
- **Partikel "sih", "kok", "lho", "kan" paling banyak sekali-dua per materi.**
  Lebih dari itu terdengar dibuat-buat.
- **Tetap jelas dan benar.** Santai bukan berarti asal: istilah teknis tetap
  disebut dengan nama aslinya dan dijelaskan, angka tetap persis, dan setiap
  fakta tetap ada.
- **Jangan:** "gaes", "bro", "wkwk", emoji, singkatan chat (yg, gmn, bgt),
  candaan yang memotong penjelasan, atau sok akrab ("Nah, sobat ngoding!").

## Aturan menulis

1. **Satu gagasan per kalimat.** Kalimat rata-rata 10 sampai 20 kata. Kalau
   sebuah kalimat butuh dua koma dan satu "yang" untuk dipahami, pecah jadi dua.
2. **Urutan menjelaskan:** apa itu (satu kalimat polos), lalu contoh nyata atau
   perumpamaan sehari-hari, lalu kodenya, lalu apa yang terjadi saat dijalankan,
   lalu kesalahan yang sering terjadi. Tidak harus kaku, tapi jangan pernah
   menyodorkan kode sebelum pembaca tahu kode itu untuk apa.
3. **Istilah baru dijelaskan saat pertama muncul**, dengan kata sehari-hari:
   "iterable, yaitu sesuatu yang isinya bisa diambil satu per satu, seperti
   list atau string". Sesudah itu pakai istilah yang SAMA terus; jangan
   berganti-ganti sinonim supaya terdengar bervariasi.
4. **Sapa pembaca dengan "kamu"**, kalimat aktif: "browser menebak", bukan
   "tebakan dilakukan oleh browser".
5. **Tunjukkan, jangan menyuruh kagum.** Daripada "ini sangat penting", tulis
   apa yang rusak kalau hal itu dilupakan.
6. **Jangan merujuk ke materi yang belum dibaca** kecuali benar-benar perlu.
   Kalau perlu, sebut judulnya dan katakan terus terang bahwa belum perlu
   dipahami sekarang.
7. **Perumpamaan boleh, asal sederhana dan sekali saja per konsep.** Satu
   perumpamaan yang pas lebih menolong daripada tiga yang ditumpuk.
8. **Kata asing secukupnya.** Kata yang memang dipakai programmer (browser,
   error, loop) boleh tetap; jangan dipaksakan diterjemahkan, jangan juga
   dijejali bahasa Inggris yang ada padanannya ("berkas" untuk file sudah
   dipakai di seluruh aplikasi, pertahankan).

## Yang dilarang (dihitung `periksa_gaya.py`)

| Pola | Contoh dari materi lama | Gantinya |
|---|---|---|
| Em dash, en dash | "...namanya DOM — singkatan dari..." | titik, koma, titik dua, atau kurung |
| HURUF KAPITAL untuk penekanan | "HTML BUKAN bahasa pemrograman", "jadi ia MENEBAK" | tulis biasa; kalau perlu penekanan, susun kalimatnya supaya kata itu di akhir |
| "bukan X, melainkan Y" sebagai gaya | "DOM BUKAN berkas yang kamu ketik. DOM adalah hasil TEBAKAN" | katakan Y langsung: "DOM adalah isi berkasmu menurut tebakan browser" |
| Penguat kosong | sangat, benar-benar, sebenarnya, pada dasarnya, tentu saja | buang, atau ganti dengan fakta |
| Pembuka kosong | "Satu hal yang perlu dicatat", "Perlu diingat bahwa", "Inilah", "Itulah sebabnya", "Mari kita" | langsung ke isinya |
| Tanya-jawab retoris | "Kenapa begitu? Karena..." | "Alasannya: ..." atau langsung jelaskan |
| Pepatah dan kalimat penutup "bijak" | "konsistensi lebih berharga daripada selera", "yang menang selalu DOM" | buang; akhiri pada fakta terakhir yang berguna |
| Drama | "kamu akan mencari penyebabnya selama satu jam", "Python yang langsung berteriak" | sebut akibatnya dengan datar |
| Daftar tiga yang dipaksakan | "dokumentasi, pesan error, dan artikel JavaScript di luar sana" | sebut yang memang perlu |
| Catatan telegrafis | "BEDA dari Java/C, for Python TIDAK memakai (awal; kondisi; update)" | kalimat utuh |

Pertanyaan pembuka paragraf yang memang ditanyakan pemula ("Kenapa tag harus
ditutup?") boleh, asal jawabannya langsung, tanpa "Karena" yang dramatis
di kalimat berikutnya, dan tidak dipakai di setiap paragraf.

Label di AWAL paragraf seperti `Jebakan:`, `Ingat:`, `Catatan:`,
`Perhatikan:` BUKAN pelanggaran. Aplikasi memakai label itu untuk menggambar
kotak peringatan (lihat `_PERAN` di `webapp/isi.py`). Pakai seperlunya, paling
banyak dua atau tiga per materi, dan tulis `Jebakan:`, bukan `JEBAKAN:`.

## Yang tidak boleh berubah

- **Judul materi.** Ia bagian dari kunci progres pelajar.
- **Kode** (field `code`) dan **blok `Keluaran:`** sesudahnya. Blok itu janji
  yang diuji terhadap keluaran sungguhan. `ganti_badan.py` menolak menulis
  kalau blok itu berubah.
- **Fakta.** Setiap fakta, angka, nama fungsi, dan contoh di prosa lama harus
  tetap ada di prosa baru, kecuali memang salah (kalau salah, catat). Jangan
  menambah fakta yang tidak bisa kamu pastikan benar.
- **Contoh kode kecil dan diagram ASCII di dalam prosa** (baris yang
  menjorok). Boleh dirapikan labelnya, isinya jangan.

## Bentuk teks di sumber

Badan materi adalah daftar baris. Pengurainya (`isi.blok_badan`) membaca
bentuknya, jadi bentuk itu punya arti:

- Paragraf biasa: baris tanpa indentasi, dibungkus manual sekitar 70 karakter
  (maksimal 78). Baris kosong memisahkan paragraf.
- Daftar: `  - butir` (dua spasi, tanda hubung, SATU spasi). Lanjutan butir
  menjorok sejajar dengan teks butirnya.
- Contoh kode atau tabel: menjorok dua spasi atau lebih, kolom disejajarkan
  dengan spasi.
- Jangan memecah kata di ujung baris dengan tanda hubung.

## Contoh: sebelum dan sesudah

Sebelum:

    KENAPA TAG HARUS DITUTUP:
      Tag pembuka cuma berkata "mulai dari sini". Tanpa penutup,
      browser tidak tahu di mana elemennya berakhir, jadi ia MENEBAK.

      Dan browser tidak pernah memberi pesan error. Ia menebak diam-
      diam lalu tetap menampilkan halamannya. ... Itu sebabnya
      kesalahan HTML lebih sulit dicari daripada kesalahan Python
      yang langsung berteriak.

Sesudah:

    Kenapa tag harus ditutup? Gampangnya, tag pembuka itu cuma bilang
    "mulai dari sini". Kalau nggak ada penutupnya, browser bingung
    elemennya selesai di mana, jadi dia nebak sendiri.

    Masalahnya, browser nggak pernah protes. Halamannya tetap tampil,
    kelihatan hampir benar, dan kamu nggak dikasih tahu salahnya di
    mana. Makanya kesalahan HTML lebih susah dicari daripada kesalahan
    Python, yang langsung nunjukin baris mana yang salah.

Yang berubah: nggak ada huruf kapital untuk penekanan, nggak ada "diam-diam"
dan "berteriak", kalimatnya lebih pendek, dan alasannya disebut dengan fakta
("nunjukin baris mana yang salah"), bukan dengan gaya.

Contoh lengkap yang sudah memakai nada ini: bab 1 HTML (materi 1 sampai 4
di `data/html_materials.py`). Baca dulu sebelum mulai menulis.
