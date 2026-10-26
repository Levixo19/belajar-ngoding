/* Pencocok dan pengelompok palet perintah. Bagian MURNI dari blok `palet` di
 * `webapp/statik/js/aplikasi.js`.
 *
 * Semuanya fungsi tanpa DOM, dan itu bukan kebetulan: yang dikerjakan palet
 * adalah MENGURUTKAN, dan urutan yang salah tidak pernah menimbulkan error --
 * ia cuma menaruh hal yang dicari orang di baris kedua belas. Karena murni,
 * seluruhnya diadu dengan `aplikasi.js` di `uji/banding-palet.mjs`.
 */

import { labelPintasan } from "./pintasan-tabel.ts";

/** Satu butir palet. `tipe` kosong berarti ia sebuah perintah. */
export interface ButirPalet {
  label: string;
  ket?: string;
  href: string;
  tipe?: string;
  /** Label `<kbd>` kalau tujuan ini punya pintasan `G lalu <huruf>`. */
  pintasan?: string | null;
}

/** Entri riwayat: alamat dan kapan ia dipakai. */
export interface ButirRiwayat {
  k: string;
  u: number;
}

/* Skor yang tidak mungkin dicapai sebuah kecocokan, dipakai sebagai "tidak
 * cocok". Ia -1 dan bukan 0 karena kueri yang seluruh hurufnya mendarat di
 * tengah kata memang berskor rendah tapi SAH, dan menyamakan "nol" dengan
 * "tidak ada" membuang justru kecocokan yang paling perlu bantuan. */
export const SKOR_GAGAL = -1;
const BOBOT_HURUF = 2;
const BONUS_BATAS = 8;
const BONUS_AWAL = 4;
/* Tambahan untuk baris yang pernah dibuka dari palet, dan ia WAJIB lebih kecil
 * daripada `BONUS_AWAL` di atas -- itu sebabnya keduanya ditulis bersebelahan,
 * supaya perbandingannya terbaca tanpa mencari. Kalau ia menang, satu
 * kunjungan lama mengalahkan huruf yang SUNGGUH ada di awal kata, dan
 * pencocoknya berhenti menjawab apa yang sedang diketik: ia mulai menjawab apa
 * yang kebetulan dibuka minggu lalu. Yang dibeli riwayat cuma pemecah seri
 * antara kandidat yang sama-sama cocok -- bukan hak veto atas kuerinya. */
const BONUS_RIWAYAT = 3;

/**
 * Apakah `teks[i]` memulai sebuah kata?
 *
 * Yang dibaca di sini teks ASLI, bukan bentuk kecilnya, dan itu bukan
 * kelalaian: sebagian batas kata di aplikasi ini TIDAK punya pemisah sama
 * sekali -- ia cuma transisi kecil->besar (`scrollTop`, `tipeData`). Mengukur
 * batas pada teks yang sudah dikecilkan menghapus seluruh kelas itu, dan yang
 * hilang justru bentuk nama yang paling sering dicari di kurikulum ini.
 */
export function diBatasKata(teks: string, i: number): boolean {
  if (i === 0) return true;
  const sblm = teks.charAt(i - 1);
  if (sblm === "_" || sblm === "-" || sblm === "/" || sblm === " ") return true;
  const kini = teks.charAt(i);
  return (
    sblm === sblm.toLowerCase() &&
    sblm !== sblm.toUpperCase() &&
    kini === kini.toUpperCase() &&
    kini !== kini.toLowerCase()
  );
}

/**
 * Skor kecocokan BERURUTAN `kata` di dalam `teks`, atau `SKOR_GAGAL`.
 *
 * "Berurutan" berarti huruf kueri wajib muncul dalam urut yang sama tapi boleh
 * berjarak: "stk" menemukan "Statistik", sedangkan "kts" tidak, karena sesudah
 * "t" di situ tidak ada lagi "s". Pencocokan yang cuma mengenali potongan
 * BERDEKATAN membuat dua kueri paling alami untuk sebuah palet -- singkatan
 * ("stk") dan huruf awal kata ("bh" untuk "Bahasa") -- tidak pernah menemukan
 * apa pun, dan yang dialami pemakainya bukan "kueriku kurang tepat" melainkan
 * "barangnya tidak ada di sini".
 *
 * Pencariannya RAKUS dari kiri (`indexOf` dari kursor), dan itu dipilih bukan
 * karena termurah melainkan karena deterministik: satu lintasan, tanpa tabel,
 * tanpa cabang yang bergantung pada apa pun di luar kedua argumennya. Skor
 * yang lahir dari satu lintasan itulah yang membuat baris berskor sama
 * benar-benar sama -- dan dengan itu urutan daftar asal selamat.
 */
export function skorBerurutan(teks: string, kata: string): number {
  const t = teks.toLowerCase();
  const k = kata.toLowerCase();
  let skor = 0;
  let dari = 0;
  let mulai = -1;
  for (let n = 0; n < k.length; n++) {
    const pos = t.indexOf(k.charAt(n), dari);
    if (pos < 0) return SKOR_GAGAL;
    if (mulai < 0) mulai = pos;
    skor += BOBOT_HURUF;
    // Huruf yang mendarat di AWAL kata jauh lebih mungkin yang dimaksud
    // pengetiknya daripada huruf yang kebetulan ada di tengah kata.
    if (diBatasKata(teks, pos)) skor += BONUS_BATAS;
    dari = pos + 1;
  }
  // Dan kecocokan yang dimulai di huruf pertama teksnya mengalahkan yang mulai
  // di tengah, kalau sisa skornya sama.
  if (mulai === 0) skor += BONUS_AWAL;
  return skor;
}

/**
 * Saring dan urutkan daftar perintah menurut `kata`.
 *
 * Kueri KOSONG berarti "belum ada yang dipersempit": daftar dikembalikan apa
 * adanya, objek yang sama dalam urutan yang sama. Palet lahir dengan medan
 * kosong, jadi inilah keadaan yang paling sering terlihat -- dan urutan
 * aslinya sendiri sudah berarti: perintah lebih dulu, bahasa sesudahnya.
 * Riwayat sengaja TIDAK mengurutkan ulang keadaan ini: menatanya dari ingatan
 * yang bisa berubah berarti daftar yang sama menyambut orangnya dengan susunan
 * berbeda tiap kali Ctrl+K ditekan, tepat di layar yang ia pakai untuk
 * menghafal letak sesuatu.
 */
export function saringPerintah(
  daftar: ButirPalet[],
  kata: string,
  riwayat: ButirRiwayat[] = [],
): ButirPalet[] {
  if (!kata) return daftar;
  // Keanggotaannya dihitung SEKALI jadi himpunan, dengan alasan yang sama
  // dengan skor di bawah -- `riwayat.some()` di dalam perulangan mengubah
  // ongkosnya jadi n*m pada SETIAP ketukan papan ketik.
  const pernah = new Set(riwayat.map((r) => r.k));
  // Skor dihitung SEKALI per baris lalu dibawa di samping barisnya. Memanggil
  // pencocoknya dari dalam pembanding `sort` berarti ia berjalan O(n log n)
  // kali alih-alih n, dan yang lebih mahal daripada ongkosnya: dua baris yang
  // skornya dihitung di dua pemanggilan berbeda tidak dijamin dibandingkan
  // atas angka yang sama.
  const bernilai: Array<{ d: ButirPalet; skor: number }> = [];
  for (const d of daftar) {
    // Dua medan, dua pencocokan, skor terbaik yang dipakai. Menggabungnya jadi
    // satu string (`label + " " + ket`) membuat batas antar-medan jadi batas
    // kata yang sah, sehingga huruf yang MELOMPAT dari judul ke keterangan
    // terbaca sebagai kecocokan -- padahal tidak ada seorang pun yang mengetik
    // "ab" untuk mencari "Alpha" yang keterangannya "Beta".
    const skor = Math.max(
      skorBerurutan(d.label || "", kata),
      skorBerurutan(d.ket || "", kata),
    );
    // Riwayat MENAIKKAN kecocokan yang sudah ada, ia tidak pernah
    // menciptakannya: baris yang hurufnya tidak muncul tetap gugur walau pernah
    // dibuka. Kebalikannya -- membawa masuk baris yang tidak cocok karena
    // pernah dipakai -- membuat kueri berhenti berarti apa pun.
    if (skor > SKOR_GAGAL) {
      bernilai.push({ d, skor: skor + (pernah.has(d.href) ? BONUS_RIWAYAT : 0) });
    }
  }
  // Tanpa pemecah-seri buatan. `Array.prototype.sort` dijamin stabil sejak
  // ES2019, jadi baris berskor sama keluar dalam urutan daftar asalnya.
  // Menambah `|| indeks` apa pun di sini bukan "memastikan" -- ia justru
  // satu-satunya cara urutan itu bisa rusak.
  bernilai.sort((a, b) => b.skor - a.skor);
  return bernilai.map((x) => x.d);
}

/* Umur ingatan palet diukur dalam HARI, dan panjang satu hari ditulis sekali
 * di sini. Angka 86400000 yang ditebar di beberapa tempat adalah angka yang
 * suatu hari ditulis salah satu digit di salah satu tempat, dan gejalanya
 * bukan error melainkan ingatan yang dibuang pada umur yang bukan 14 hari. */
const HARI_MS = 86400000;

/**
 * Butir riwayat yang masih cukup baru, dalam urutan yang sama.
 *
 * `sekarang` masuk sebagai ARGUMEN, bukan dibaca dari jam di dalam sini, dan
 * itu bukan soal gaya: fungsi yang membaca jamnya sendiri memberi jawaban
 * berbeda untuk masukan yang sama, dan sebuah baris yang sedang berada tepat
 * di tepi 14 hari akan muncul-hilang di antara dua huruf yang diketik. Yang
 * mengambil jam tinggal di komponennya, satu kali per palet yang dibuka -- dan
 * dengan itu pencocok di atas tetap bisa diadu per urutan oleh pembanding,
 * yang mustahil kalau jawabannya bergantung pada kapan ia dijalankan.
 *
 * Yang dikembalikan daftar BARU dan yang masuk tidak disentuh: pemanggilnya
 * memakai lagi daftar yang sama nanti untuk mencatat butir berikutnya.
 */
export function riwayatPotong(
  riwayat: ButirRiwayat[],
  sekarang: number,
  batasHari = 14,
): ButirRiwayat[] {
  const batas = sekarang - batasHari * HARI_MS;
  return riwayat.filter((r) => r.u >= batas);
}

/**
 * Riwayat BARU dengan `k` di depan dan waktunya disetel `sekarang`.
 *
 * Satu alamat satu butir: kalau `k` sudah ada di dalam, yang lama DIBUANG --
 * tidak dibiarkan tinggal di posisi lamanya. Membiarkannya membuat satu tujuan
 * yang sering dibuka menumpuk jadi belasan butir yang isinya sama, dan
 * pemotongan umur kemudian membaca tumpukan itu sebagai belasan kunjungan
 * berbeda -- sehingga ingatan yang paling sering dipakai justru yang paling
 * cepat memenuhi dirinya sendiri.
 */
export function riwayatNaikkan(
  riwayat: ButirRiwayat[],
  k: string,
  sekarang: number,
): ButirRiwayat[] {
  return [{ k, u: sekarang }, ...riwayat.filter((r) => r.k !== k)];
}

/**
 * Rombongan palet. Predikatnya DIURUT dan itu mengikat: sebuah butir masuk ke
 * rombongan PERTAMA yang mengakuinya, jadi `() => true` di ekor bukan
 * kemalasan melainkan satu-satunya bentuk yang membuat butir MUSTAHIL hilang
 * dari daftar. Predikat ketiga yang menyebut tipenya satu per satu ("materi",
 * "kuis", "latihan") akan menelan tipe KEEMPAT yang ditambahkan `/api/cari`
 * suatu hari -- tanpa error, tanpa baris di layar, tanpa satu pun tes merah.
 *
 * Yang sengaja TIDAK dipecah: ketiga tipe isi tinggal dalam SATU rombongan.
 * Server sudah mengurutkan hasilnya menurut relevansi, dan memecahnya jadi
 * tiga berarti mendorong materi berperingkat rendah di atas kuis berperingkat
 * tinggi -- persis cacat yang penanda ini ada untuk mencegah, kali ini tanpa
 * satu pun alasan yang terbaca di layar.
 */
export const GRUP_PALET: Array<{
  label: string;
  punya: (d: ButirPalet) => boolean;
}> = [
  { label: "Perintah", punya: (d) => !d.tipe },
  { label: "Bahasa", punya: (d) => d.tipe === "bahasa" },
  { label: "Isi", punya: () => true },
];

export interface Rombongan {
  label: string;
  isi: ButirPalet[];
}

/**
 * Partisi, BUKAN pengurutan ulang: urutan DI DALAM tiap rombongan
 * dipertahankan apa adanya, jadi skor `saringPerintah()` dan peringkat
 * relevansi `/api/cari` tetap berarti. Batas antar-rombongannya sendiri sudah
 * berlaku sebelum penanda ada -- daftar perintah menaruh perintah lebih dulu,
 * hasil pencarian menyambung di belakang -- jadi yang ditambahkan di sini
 * TANDANYA, bukan susunannya.
 *
 * Rombongan KOSONG tidak menghasilkan penanda. Sebuah label di atas nol butir
 * menjanjikan sesuatu yang tidak ada di bawahnya, dan satu-satunya cara
 * pembacanya tahu janji itu bohong adalah dengan mencarinya dulu.
 */
export function kelompokkan(daftar: ButirPalet[]): Rombongan[] {
  const isiGrup: ButirPalet[][] = GRUP_PALET.map(() => []);
  for (const d of daftar) {
    const i = GRUP_PALET.findIndex((g) => g.punya(d));
    (isiGrup[i] as ButirPalet[]).push(d);
  }
  return GRUP_PALET.map((g, i) => ({
    label: g.label,
    isi: isiGrup[i] as ButirPalet[],
  })).filter((r) => r.isi.length > 0);
}

/** Bahasa seperti yang dikirim `/api/awal`, medan yang dipakai palet. */
export interface BahasaPalet {
  key: string;
  label: string;
  materi: number;
  kuis: number;
  latihan: number;
}

/**
 * Enam perintah tetap, tiga tujuan tambahan, lalu satu butir per kurikulum.
 *
 * Urutan enam yang pertama adalah KONTRAK: `TestPaletCombobox` di
 * `tests/test_web.py` membaca indeksnya, jadi tujuan baru disisipkan SESUDAH
 * keenamnya, bukan di antaranya.
 */
export function daftarPerintah(bahasa: BahasaPalet[]): ButirPalet[] {
  const daftar: ButirPalet[] = [
    { label: "Dasbor", ket: "Ringkasan dan langkah berikutnya", href: "#/dasbor" },
    { label: "Ruang Coba", ket: "Jalankan kode apa saja", href: "#/coba" },
    { label: "Catatanku", ket: "Semua catatan pribadimu", href: "#/catatan" },
    { label: "Bookmark", ket: "Halaman yang kamu tandai", href: "#/bookmark" },
    { label: "Statistik", ket: "XP, badge, toolchain", href: "#/statistik" },
    { label: "Pengaturan", ket: "Tema, target harian, data", href: "#/atur" },
    { label: "Pustaka", ket: "Buku, kursus, proyek, dan API gratis", href: "#/pustaka" },
    { label: "Peta Karier", ket: "21 profesi, kesiapan, dan jalur pindah", href: "#/karier" },
    { label: "Langit", ket: "Seluruh kurikulum sebagai peta bintang", href: "#/langit" },
    { label: "Cari", ket: "Cari di seluruh isi kurikulum", href: "#/cari" },
  ];
  for (const b of bahasa) {
    daftar.push({
      label: b.label,
      ket: `${b.materi} materi · ${b.kuis} kuis · ${b.latihan} latihan`,
      href: "#/bahasa/" + b.key,
      tipe: "bahasa",
    });
  }
  return daftar.map((d) => ({ ...d, pintasan: labelPintasan(d.href) }));
}
