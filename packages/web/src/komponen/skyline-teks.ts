/* Cakrawala: hamparan XP harian digambar sebagai deretan batang isometrik.
 *
 * Bagian MURNI dari `Skyline.tsx`. Terpisah supaya `uji/banding-skyline.mjs`
 * bisa mengimpornya tanpa menyeret React (Node melucuti tipe dari `.ts`, tidak
 * JSX dari `.tsx`).
 *
 * Gagasannya dari "GitHub Contribution Graph 3D" yang ditemukan waktu memindai
 * 21st.dev. Kodenya tidak disalin: komponen itu butuh Tailwind dan palet hijau
 * GitHub, sedangkan di sini datanya milik aplikasi ini (`heatmap` dari
 * `/api/dasbor`), warnanya token bara, dan aturan gerak serta aksesibilitasnya
 * aturan aplikasi ini.
 *
 * Yang dikodekan tiap bagian, supaya tidak ada ornamen yang tidak berarti:
 *  - Satu batang = satu hari. Tingginya LINEAR terhadap XP hari itu, terhadap
 *    yang terbesar antara target harian dan hari terbaik. Akar kuadrat membuat
 *    hari kecil terlihat, tapi menipu perbandingan antara dua hari.
 *  - Warna puncak batang = tingkat yang sama dengan hamparan datar
 *    (`baraPetak`), jadi dua tampilan itu tidak pernah berbeda pendapat.
 *  - Sumbu panjang = minggu, sumbu pendek = hari (Senin di belakang).
 *
 * Yang tidak diputuskan di sini: apakah tampilannya dipakai (itu pilihan
 * pelajar di kartu Bara) dan kapan digerakkan (`useGerakPenuh`).
 */

import { angka } from "../util.ts";
import { tanggalLokal, tanggalRamah } from "../waktu.ts";

/** Satu hari. Bentuknya sama dengan `SelPetak` di `layar/dasbor-teks.ts`. */
export interface HariSkyline {
  tanggal: string;
  xp: number;
  tingkat: number;
  kini: boolean;
  judul: string;
}

/** Piksel viewBox untuk satu satuan jarak antar-petak. */
export const SKALA = 34;
/** Langkah satu minggu: ke kanan, sedikit turun. */
export const MINGGU = { x: 1, y: 0.14 } as const;
/** Langkah satu hari: ke kiri bawah. Senin paling belakang, Minggu paling depan. */
export const HARI = { x: -0.34, y: 0.66 } as const;
/** Jarak batang ke tepi petaknya, supaya ada celah antar-batang. */
export const INSET = 0.1;
/** Tinggi batang puncak, dalam satuan jarak antar-petak. */
export const TINGGI_MAKS = 2.4;
/** Hari ber-XP tidak pernah serata lantai, seberapa kecil pun XP-nya. */
export const TINGGI_MIN = 0.12;
/** Ruang kosong di tepi gambar. */
export const PAD = 0.7;
/** Label bulan sedekat ini (dalam kolom) dengan tetangganya dibuang. */
export const JARAK_BULAN = 3;
/** Satu minggu = tujuh hari = tujuh indeks. */
export const HARI_PER_MINGGU = 7;
/** Tambahan ruang bawah untuk label bulan, dalam satuan. */
export const RUANG_LABEL = 0.55;
/** Baris tempat label bulan digantung (tepat di bawah baris Minggu). */
export const BARIS_LABEL = 7.35;

export const NAMA_BULAN = [
  "Jan", "Feb", "Mar", "Apr", "Mei", "Jun",
  "Jul", "Agu", "Sep", "Okt", "Nov", "Des",
] as const;
export const NAMA_HARI = [
  "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu",
] as const;

/** Kolom (minggu) dan baris (Senin = 0) hari ke-`i`, dengan `kosong` sel pembuka. */
export function kolomBaris(i: number, kosong: number): { kolom: number; baris: number } {
  const n = kosong + i;
  return { kolom: Math.floor(n / HARI_PER_MINGGU), baris: n % HARI_PER_MINGGU };
}

/** Pembagi tinggi: yang terbesar antara target harian dan hari terbaik. */
export function puncakXp(hari: ReadonlyArray<{ xp: number }>, target: number): number {
  let puncak = target > 0 ? target : 1;
  for (const h of hari) if (h.xp > puncak) puncak = h.xp;
  return puncak;
}

/** Tinggi batang dalam satuan. 0 untuk hari tanpa XP. */
export function tinggiBatang(xp: number, puncak: number): number {
  if (!(xp > 0) || !(puncak > 0)) return 0;
  return Math.max(TINGGI_MIN, Math.min(1, xp / puncak) * TINGGI_MAKS);
}

/** Titik layar (satuan, sebelum digeser dan diskalakan) untuk sudut petak. */
export function titik(kolom: number, baris: number, naik = 0): [number, number] {
  return [
    kolom * MINGGU.x + baris * HARI.x,
    kolom * MINGGU.y + baris * HARI.y - naik,
  ];
}

export interface Batang {
  /** Indeks hari di daftar masukan. */
  i: number;
  kolom: number;
  baris: number;
  tinggi: number;
  tingkat: number;
  kini: boolean;
  /** Atribut `points` tiga permukaan yang terlihat. Sisi dan muka kosong untuk hari tanpa XP. */
  atas: string;
  muka: string;
  sisi: string;
  /** Atribut `d` garis luar enam sudut, untuk sorot hari yang dipilih. */
  siluet: string;
}

export interface LabelBulan {
  kolom: number;
  teks: string;
  /** Letak sebagai pecahan 0..1 dari lebar dan tinggi gambar. */
  x: number;
  y: number;
}

export interface TataSkyline {
  lebar: number;
  tinggi: number;
  puncak: number;
  /** Sama urutannya dengan hari: minggu demi minggu, Senin dulu. Itu juga urutan gambar yang benar. */
  batang: Batang[];
  bulan: LabelBulan[];
}

/** Dibulatkan dua desimal: koordinat sependek mungkin di DOM tanpa terlihat berbeda. */
const bulat = (n: number): number => Math.round(n * 100) / 100;

/** Label bulan: bulan pertama yang terlihat plus tiap tanggal 1, tanpa yang berdesakan. */
export function labelBulan(
  hari: ReadonlyArray<{ tanggal: string }>,
  kosong: number,
): Array<{ kolom: number; teks: string }> {
  const calon: Array<{ kolom: number; teks: string }> = [];
  hari.forEach((h, i) => {
    const t = tanggalLokal(h.tanggal);
    if (!t) return;
    if (i === 0 || t.getDate() === 1) {
      calon.push({
        kolom: kolomBaris(i, kosong).kolom,
        teks: NAMA_BULAN[t.getMonth()] ?? "",
      });
    }
  });
  // Bulan pembuka yang cuma tersisa beberapa hari tidak diberi label sendiri:
  // ia akan menimpa label bulan berikutnya.
  const [awal, kedua] = calon;
  if (awal && kedua && kedua.kolom - awal.kolom < JARAK_BULAN) calon.shift();
  const hasil: Array<{ kolom: number; teks: string }> = [];
  for (const c of calon) {
    const terakhir = hasil[hasil.length - 1];
    if (!terakhir || c.kolom - terakhir.kolom >= JARAK_BULAN) hasil.push(c);
  }
  return hasil;
}

/**
 * Susun seluruh gambar: titik tiga permukaan tiap batang, garis luarnya, label
 * bulan, dan ukuran viewBox yang pas.
 *
 * Koordinat dihitung dulu dalam satuan, dicari batas kotaknya, lalu digeser
 * supaya semuanya positif dan diskalakan `SKALA`. Label bulan ikut dihitung
 * dalam batas itu, jadi tidak pernah jatuh di luar gambar.
 *
 * **Urutan `batang` adalah urutan gambar (algoritma pelukis), tanpa
 * pengurutan lagi.** Kamera ada di sisi minggu-berikutnya dan hari-berikutnya,
 * jadi batang A harus digambar sebelum B bila A tidak lebih depan dari B pada
 * kedua sumbu. Indeks hari sudah menjamin itu: minggu demi minggu, dan di dalam
 * satu minggu dari Senin. Dua batang yang saling tidak sebanding (satu lebih
 * depan di minggu, satu lebih depan di hari) tidak pernah bertumpuk di layar,
 * jadi urutan di antara keduanya bebas. Dulu ada pengurutan berkunci linear di
 * sini; baterai mutasi menunjukkan ia tidak pernah mengubah apa pun yang perlu,
 * jadi dibuang.
 */
export function bangunSkyline(
  hari: ReadonlyArray<HariSkyline>,
  kosong: number,
  target: number,
): TataSkyline {
  const puncak = puncakXp(hari, target);
  const bulan = labelBulan(hari, kosong);

  type Mentah = { h: HariSkyline; i: number; kolom: number; baris: number; tinggi: number };
  const mentah: Mentah[] = hari.map((h, i) => ({
    h,
    i,
    ...kolomBaris(i, kosong),
    tinggi: tinggiBatang(h.xp, puncak),
  }));

  let minX = Infinity;
  let maxX = -Infinity;
  let minY = Infinity;
  let maxY = -Infinity;
  const lihat = (p: [number, number]) => {
    if (p[0] < minX) minX = p[0];
    if (p[0] > maxX) maxX = p[0];
    if (p[1] < minY) minY = p[1];
    if (p[1] > maxY) maxY = p[1];
  };
  for (const m of mentah) {
    const c0 = m.kolom + INSET;
    const c1 = m.kolom + 1 - INSET;
    const r0 = m.baris + INSET;
    const r1 = m.baris + 1 - INSET;
    for (const [c, r] of [[c0, r0], [c1, r0], [c1, r1], [c0, r1]] as const) {
      lihat(titik(c, r, 0));
      lihat(titik(c, r, m.tinggi));
    }
  }
  const jangkar = bulan.map((b) => titik(b.kolom + 0.5, BARIS_LABEL, 0));
  for (const j of jangkar) {
    lihat(j);
    lihat([j[0], j[1] + RUANG_LABEL]);
  }
  if (!Number.isFinite(minX)) {
    minX = maxX = minY = maxY = 0;
  }

  const geserX = PAD - minX;
  const geserY = PAD - minY;
  const lebarSatuan = maxX - minX + 2 * PAD;
  const tinggiSatuan = maxY - minY + 2 * PAD;
  const peta = (p: [number, number]): [number, number] => [
    bulat((p[0] + geserX) * SKALA),
    bulat((p[1] + geserY) * SKALA),
  ];
  const teksTitik = (daftar: Array<[number, number]>) =>
    daftar.map((p) => `${p[0]},${p[1]}`).join(" ");

  const batang: Batang[] = mentah.map((m) => {
    const c0 = m.kolom + INSET;
    const c1 = m.kolom + 1 - INSET;
    const r0 = m.baris + INSET;
    const r1 = m.baris + 1 - INSET;
    const dasar = (c: number, r: number) => peta(titik(c, r, 0));
    const puncakTitik = (c: number, r: number) => peta(titik(c, r, m.tinggi));
    const ada = m.tinggi > 0;
    const a = puncakTitik(c0, r0);
    const b = puncakTitik(c1, r0);
    const c = puncakTitik(c1, r1);
    const d = puncakTitik(c0, r1);
    return {
      i: m.i,
      kolom: m.kolom,
      baris: m.baris,
      tinggi: bulat(m.tinggi),
      tingkat: m.h.tingkat,
      kini: m.h.kini,
      atas: teksTitik([a, b, c, d]),
      // Muka depan (menghadap hari berikutnya) dan sisi kanan (menghadap
      // minggu berikutnya): dua permukaan yang terlihat dari sudut pandang ini.
      muka: ada ? teksTitik([d, c, dasar(c1, r1), dasar(c0, r1)]) : "",
      sisi: ada ? teksTitik([b, c, dasar(c1, r1), dasar(c1, r0)]) : "",
      siluet:
        "M" + [a, b, dasar(c1, r0), dasar(c1, r1), dasar(c0, r1), d]
          .map((p) => `${p[0]},${p[1]}`).join("L") + "Z",
    };
  });

  const lebar = bulat(lebarSatuan * SKALA);
  const tinggi = bulat(tinggiSatuan * SKALA);
  return {
    lebar,
    tinggi,
    puncak,
    batang,
    bulan: bulan.map((b, j) => {
      const p = peta(jangkar[j] ?? [0, 0]);
      return {
        kolom: b.kolom,
        teks: b.teks,
        x: Math.round((p[0] / lebar) * 10000) / 10000,
        y: Math.round((p[1] / tinggi) * 10000) / 10000,
      };
    }),
  };
}

/**
 * Langkah papan ketik di hamparan. `null` bila tombolnya bukan milik hamparan,
 * supaya pemanggil tidak menelan tombol yang bukan urusannya.
 *
 * Kiri dan kanan berpindah satu minggu (tujuh indeks) dan dijepit di ujung,
 * jadi dari minggu terakhir yang belum penuh orang mendarat di hari ini, bukan
 * di tempat. Atas dan bawah berpindah satu hari tapi TIDAK menyeberang ke
 * minggu lain: dari Minggu, panah bawah tidak melompat ke Senin berikutnya.
 */
export function langkahSel(
  i: number,
  tombol: string,
  kosong: number,
  jumlah: number,
): number | null {
  if (jumlah <= 0) return null;
  const akhir = jumlah - 1;
  const baris = (kosong + i) % HARI_PER_MINGGU;
  switch (tombol) {
    case "ArrowRight":
      return Math.min(akhir, i + HARI_PER_MINGGU);
    case "ArrowLeft":
      return Math.max(0, i - HARI_PER_MINGGU);
    case "ArrowDown":
      return baris < HARI_PER_MINGGU - 1 && i < akhir ? i + 1 : i;
    case "ArrowUp":
      return baris > 0 && i > 0 ? i - 1 : i;
    case "PageDown":
      return Math.min(akhir, i + 4 * HARI_PER_MINGGU);
    case "PageUp":
      return Math.max(0, i - 4 * HARI_PER_MINGGU);
    case "Home":
      return 0;
    case "End":
      return akhir;
    default:
      return null;
  }
}

export interface RingkasSkyline {
  total: number;
  /** Hari ber-XP. Bukan "hari belajar": hari yang hanya membaca tidak tercatat di hamparan. */
  aktif: number;
  /** Hari ber-XP terbanyak; yang terbaru bila ada yang sama. */
  tersibuk: HariSkyline | null;
  /** Hari ber-XP berturutan terpanjang di dalam hamparan; yang terbaru bila sama. */
  rentetan: { panjang: number; akhir: string } | null;
}

export function ringkasSkyline(hari: ReadonlyArray<HariSkyline>): RingkasSkyline {
  let total = 0;
  let aktif = 0;
  let tersibuk: HariSkyline | null = null;
  let jalan = 0;
  let panjang = 0;
  let akhir = "";
  for (const h of hari) {
    if (h.xp > 0) {
      total += h.xp;
      aktif += 1;
      jalan += 1;
      if (jalan >= panjang) {
        panjang = jalan;
        akhir = h.tanggal;
      }
      if (!tersibuk || h.xp >= tersibuk.xp) tersibuk = h;
    } else {
      jalan = 0;
    }
  }
  return { total, aktif, tersibuk, rentetan: panjang > 0 ? { panjang, akhir } : null };
}

/** Kalimat satu hari: nama hari, tanggal, XP, dan penanda hari ini. */
export function teksHari(h: HariSkyline, baris: number): string {
  const nama = NAMA_HARI[baris] ?? "";
  return `${nama}, ${h.judul}${h.kini ? ", hari ini" : ""}`;
}

/** Nama yang dibacakan untuk seluruh hamparan, termasuk cara menjelajahinya. */
export function labelGrup(r: RingkasSkyline): string {
  const isi =
    r.aktif > 0
      ? `${angka(r.aktif)} hari ber-XP, total ${angka(r.total)} XP`
      : "belum ada hari ber-XP";
  return `Cakrawala XP harian enam bulan terakhir: ${isi}. Panah menjelajah hari, Home dan End ke ujung.`;
}

/** Tanggal hari tersibuk untuk ringkasan, atau kata pengganti bila belum ada. */
export function teksTersibuk(r: RingkasSkyline): string {
  return r.tersibuk
    ? `${tanggalRamah(r.tersibuk.tanggal)}, ${angka(r.tersibuk.xp)} XP`
    : "belum ada";
}

export function teksRentetan(r: RingkasSkyline): string {
  return r.rentetan ? `${angka(r.rentetan.panjang)} hari` : "belum ada";
}
