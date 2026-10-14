/* Ikon garis, digambar sendiri.
 *
 * Sebelum berkas ini ada, jenis isi ditandai dengan karakter Unicode: ◆ untuk
 * materi, ◇ untuk kuis, ▶ untuk latihan. Itu bekerja, tapi tiga masalahnya
 * nyata. Bentuknya ditentukan font yang kebetulan terpasang, jadi berat dan
 * ukurannya berbeda-beda di tiap mesin dan tidak pernah sejajar dengan teks di
 * sebelahnya. Ia tidak bisa dibedakan sekilas — belah ketupat penuh dan belah
 * ketupat kosong terlalu mirip. Dan ia tidak pernah bisa terlihat seperti
 * bagian dari satu keluarga yang sama.
 *
 * Yang di bawah ini semuanya digambar pada kisi 24×24 dengan ketebalan garis
 * yang sama (1,7), ujung membulat, dan tanpa isi. Konsistensi itulah seluruh
 * gunanya: dua puluh ikon yang jelas berasal dari satu tangan terbaca sebagai
 * sistem, sementara dua puluh ikon yang masing-masing "bagus sendiri" terbaca
 * sebagai kebisingan.
 *
 * Semuanya mewarisi `currentColor`, jadi ikon otomatis ikut warna teks di
 * sekitarnya di keempat tema tanpa satu baris CSS tambahan.
 *
 * Importir: aplikasi.js, layar-belajar.js, layar-kerja.js.
 */

const NS = "http://www.w3.org/2000/svg";

/* Tiap entri adalah daftar <path d="..."> — bagian yang benar-benar berbeda
   antar ikon. Sisanya (viewBox, stroke, ketebalan, ujung) sama untuk semua dan
   dipasang di satu tempat, di bawah. */
const BENTUK = {
  /* Materi: buku terbuka. */
  materi: ["M12 6.5C10.5 5.2 8.6 4.5 6.5 4.5H4v13h2.5c2.1 0 4 .7 5.5 2",
           "M12 6.5c1.5-1.3 3.4-2 5.5-2H20v13h-2.5c-2.1 0-4 .7-5.5 2",
           "M12 6.5v15"],
  /* Kuis: tanda tanya di dalam lingkaran. */
  kuis: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z",
         "M9.6 9.4a2.5 2.5 0 0 1 4.9.6c0 1.7-2.5 2.5-2.5 2.5",
         "M12 16.6h.01"],
  /* Latihan: kurung siku dan garis miring — lambang menulis kode. */
  latihan: ["M8.5 8 5 12l3.5 4", "M15.5 8 19 12l-3.5 4", "M13.5 6.5l-3 11"],
  /* Ruang coba: tombol putar. */
  jalankan: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z", "M10.2 8.6 15.5 12l-5.3 3.4V8.6Z"],
  /* Dasbor: lingkaran dengan titik di tengah. */
  dasbor: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z", "M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6Z"],
  /* Catatan: pena. */
  catatan: ["M4 20h4L19.5 8.5a2.1 2.1 0 0 0-3-3L5 17v3Z", "M14.5 7 17 9.5"],
  /* Bookmark: pita. */
  bookmark: ["M7 4h10a1 1 0 0 1 1 1v15l-6-4-6 4V5a1 1 0 0 1 1-1Z"],
  /* Statistik: tiga batang. */
  statistik: ["M5 20V13", "M12 20V5", "M19 20v-4"],
  /* Pengaturan: geser. */
  atur: ["M4 8h10", "M18 8h2", "M4 16h4", "M12 16h8",
         "M16 8a2 2 0 1 0-4 0 2 2 0 0 0 4 0Z", "M10 16a2 2 0 1 0-4 0 2 2 0 0 0 4 0Z"],
  /* Cari: kaca pembesar. */
  cari: ["M11 18a7 7 0 1 0 0-14 7 7 0 0 0 0 14Z", "M16.2 16.2 20 20"],
  /* Waktu: jam. */
  waktu: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z", "M12 7.5V12l3 1.8"],
  /* Tingkat kesulitan: tangga tiga anak. */
  tingkat: ["M4 19h4v-5H4z", "M10 19h4V9h-4z", "M16 19h4V5h-4z"],
  /* Api: streak harian. */
  api: ["M12 21c3.5 0 6-2.4 6-5.6 0-3.7-3-5.4-3.6-9.4-2 1.2-2.9 3-2.9 4.6 0 1-.6 1.6-1.2 1.6-.7 0-1.2-.6-1.2-1.6-1.9 1.3-3.1 3.3-3.1 5.4C6 18.6 8.5 21 12 21Z"],
  /* Selesai: centang dalam lingkaran. */
  selesai: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z", "M8.5 12.3l2.4 2.4 4.6-4.9"],
  /* Terkunci / belum. */
  belum: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z"],
  /* Sedang berjalan: lingkaran separuh terisi. */
  sedang: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z", "M12 3a9 9 0 0 1 0 18Z"],
  /* Panah kanan: lanjut. */
  lanjut: ["M5 12h13", "M13 6.5 18.5 12 13 17.5"],
  /* Panah kiri: kembali. */
  kembali: ["M19 12H6", "M11 6.5 5.5 12 11 17.5"],
  /* Panel: sembunyikan/tampilkan rel. */
  panel: ["M4.5 5.5h15v13h-15z", "M10 5.5v13"],
  /* Bintang: badge. */
  bintang: ["M12 4.5l2.3 4.9 5.2.7-3.8 3.7.9 5.2-4.6-2.5-4.6 2.5.9-5.2L4.5 10l5.2-.7z"],
  /* Bantuan. */
  bantuan: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z",
            "M9.6 9.4a2.5 2.5 0 0 1 4.9.6c0 1.7-2.5 2.5-2.5 2.5", "M12 16.6h.01"],
  /* Tema: separuh terang separuh gelap. */
  tema: ["M12 21a9 9 0 1 0 0-18 9 9 0 0 0 0 18Z", "M12 3v18"],
  /* Berkas kode. */
  berkas: ["M13 3.5H7a1.5 1.5 0 0 0-1.5 1.5v14A1.5 1.5 0 0 0 7 20.5h10a1.5 1.5 0 0 0 1.5-1.5V9z",
           "M13 3.5V9h5.5"],
  /* Bagian / daftar. */
  bagian: ["M5 7h14", "M5 12h14", "M5 17h9"],
  /* Rak Pustaka: tiga punggung buku, satu miring. */
  pustaka: ["M5 4.5h3v15H5z", "M10 4.5h3v15h-3z", "M15.2 5.6l2.9-.8 2.4 14.4-2.9.8z"],
  /* Peta Karier: dua titik dan jalan berkelok di antaranya. */
  karier: ["M6 20.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z",
           "M18 8.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5Z",
           "M8.4 17.2c3.8-.6 2.6-6.4 7.2-7.6"],
};

/** Bangun satu ikon.
 *
 *  @param nama    kunci di BENTUK
 *  @param opsi    { ukuran = 20, tebal = 1.7, kelas }
 *  @returns SVGElement, atau null kalau namanya tidak dikenal — bukan
 *           melempar: sebuah ikon yang hilang tidak boleh menjatuhkan seluruh
 *           layar yang memuatnya.
 */
export function ikon(nama, opsi = {}) {
  const jalur = BENTUK[nama];
  if (!jalur) return null;

  const { ukuran = 20, tebal = 1.7, kelas = "" } = opsi;
  const svg = document.createElementNS(NS, "svg");
  svg.setAttribute("viewBox", "0 0 24 24");
  svg.setAttribute("width", String(ukuran));
  svg.setAttribute("height", String(ukuran));
  svg.setAttribute("fill", "none");
  svg.setAttribute("stroke", "currentColor");
  svg.setAttribute("stroke-width", String(tebal));
  svg.setAttribute("stroke-linecap", "round");
  svg.setAttribute("stroke-linejoin", "round");
  // Ikon di sini SELALU mendampingi teks yang sudah menyampaikan artinya.
  // Membiarkannya terbaca pembaca layar cuma menghasilkan pengumuman ganda.
  svg.setAttribute("aria-hidden", "true");
  svg.setAttribute("focusable", "false");
  if (kelas) svg.setAttribute("class", kelas);
  svg.style.flex = "none";

  jalur.forEach((d, i) => {
    const p = document.createElementNS(NS, "path");
    p.setAttribute("d", d);
    // Bentuk yang ditandai isi memakai currentColor sebagai isian, bukan
    // garis. Penjaganya berbasis INDEKS, bukan bentuk jalurnya: penjaga lama
    // memeriksa `d.endsWith("18Z")`, dan kedua jalur ikon "sedang" kebetulan
    // berakhir begitu — jadi separuh lingkarannya tidak pernah sekali pun
    // terisi, dan ikon "sedang dikerjakan" tak bisa dibedakan dari "belum".
    if (nama === "tingkat" || (nama === "sedang" && i > 0)) {
      p.setAttribute("fill", "currentColor");
    }
    svg.appendChild(p);
  });
  return svg;
}

/** Nama ikon untuk sebuah tipe isi. Satu tempat, supaya materi selalu buku
 *  dan latihan selalu kurung siku di mana pun ia muncul. */
export function ikonTipe(tipe) {
  return { materi: "materi", kuis: "kuis", latihan: "latihan" }[tipe] || "bagian";
}

/* Dipakai tes untuk memastikan tiap ikon benar-benar bisa dibangun. */
export const NAMA_IKON = Object.keys(BENTUK);
