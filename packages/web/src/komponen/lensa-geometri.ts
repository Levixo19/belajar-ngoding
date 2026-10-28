/* Geometri layar Langit: ikhtisar (peta 32 rasi) dan lensa (satu rasi
 * diperbesar). Bagian MURNI: nol rujukan ke `document` atau React, supaya
 * pembandingnya (`uji/banding-lensa.mjs`) bisa mengimpornya langsung lewat
 * pelucut tipe Node.
 *
 * Tiga keputusan yang dikunci di sini, masing-masing dengan sebabnya:
 *
 * 1. Semua koordinat dalam PIKSEL layar, bukan satuan viewBox. Jari-jari,
 *    tebal garis, dan sasaran klik adalah angka piksel (bintang 3,7 px,
 *    jangkauan sasaran 14 dan 40 px). Kalau yang dipakai satuan viewBox,
 *    tiap angka itu harus dibagi skala di setiap pemakaiannya, dan satu
 *    pembagian yang terlupa tidak menimbulkan error -- cuma bintang yang
 *    kebesaran di satu lebar jendela saja.
 * 2. Bentuk rasi TIDAK ditulis ulang. `bentukRasi` dari `rasi-geometri.ts`
 *    dipakai dengan benih yang sama ("langit·<key>"); lensa hanya
 *    memanggilnya dengan kotak yang lebih besar. Karena `bentukRasi`
 *    menormalkan ke kotak w x h tanpa mengubah perbandingan, rasi di lensa
 *    adalah rasi yang SAMA dengan di ikhtisar, cuma lebih besar: pelajar yang
 *    mengenali bentuk "HTML" tetap mengenalinya.
 * 3. Satu penentu sasaran untuk kedua tampilan: `terdekat()`. Di versi lama
 *    tiap bintang membawa lingkaran sasaran r=10 yang saling tumpang, dan
 *    66 persen klik tepat di pusat sebuah bintang mengenai bintang TETANGGA.
 *    Sekarang satu pencari bintang terdekat, dan yang ditekan selalu yang
 *    paling dekat dengan kursor.
 */

import { bentukRasi, berikutDari, ROMAWI, type MateriBintang, type Titik } from "./rasi-geometri.ts";

export type StatusBintang = "selesai" | "sebagian" | "baru" | "terkunci";

/** Status gabungan. `terkunci` selalu memenangkan `baru`: server menjamin
 *  `terkunci: true` hanya berpasangan dengan `status: "baru"`. */
export function statusBintang(m: MateriBintang): StatusBintang {
  if (m.terkunci) return "terkunci";
  if (m.status === "selesai") return "selesai";
  if (m.status === "sebagian") return "sebagian";
  return "baru";
}

/** Kata status untuk label dan panel. Satu sumber, supaya legenda, tip, dan
 *  `aria-label` tidak berpendapat berbeda. */
export const KATA_STATUS_BINTANG: Record<StatusBintang, string> = {
  selesai: "sudah dibaca",
  sebagian: "dibaca sebagian",
  baru: "belum dibaca",
  terkunci: "masih terkunci",
};

/** Urutan "makin jauh makin redup": dipakai legenda dan uji monotonitas. */
export const URUTAN_STATUS: StatusBintang[] = [
  "selesai", "sebagian", "baru", "terkunci",
];

/* ------------------------------------------------------------- grid ruang */

export interface TitikRuang {
  x: number;
  y: number;
}

export interface Grid<T extends TitikRuang> {
  sel: number;
  kolom: number;
  baris: number;
  isi: T[][];
}

const jepit = (n: number, a: number, b: number): number =>
  n < a ? a : n > b ? b : n;

/** Grid seragam. Satu sel = `sel` piksel; pencarian terdekat cuma membuka
 *  sel-sel di sekitar kursor, jadi ongkosnya tidak tumbuh dengan jumlah
 *  bintang (1.062 di ikhtisar, <= 60 di lensa). */
export function bangunGrid<T extends TitikRuang>(
  titik: readonly T[],
  lebar: number,
  tinggi: number,
  sel = 24,
): Grid<T> {
  const kolom = Math.max(1, Math.ceil(lebar / sel));
  const baris = Math.max(1, Math.ceil(tinggi / sel));
  const isi: T[][] = Array.from({ length: kolom * baris }, () => []);
  for (const t of titik) {
    const c = jepit(Math.floor(t.x / sel), 0, kolom - 1);
    const b = jepit(Math.floor(t.y / sel), 0, baris - 1);
    (isi[b * kolom + c] as T[]).push(t);
  }
  return { sel, kolom, baris, isi };
}

/** Titik terdekat dalam jarak `maks`, atau `null`. Jarak sama persis dimenangkan
 *  titik yang lebih dulu dimasukkan ke grid (urutan sel, lalu urutan masuk). */
export function terdekat<T extends TitikRuang>(
  g: Grid<T>,
  x: number,
  y: number,
  maks: number,
): { t: T; jarak: number } | null {
  const c0 = jepit(Math.floor(x / g.sel), 0, g.kolom - 1);
  const b0 = jepit(Math.floor(y / g.sel), 0, g.baris - 1);
  // Titik di luar kotak grid dijepit ke sel tepi; cincin diperlebar sebesar
  // selisihnya supaya pencarian tidak melewatkan titik yang sebenarnya dekat.
  const lebarGrid = g.kolom * g.sel;
  const tinggiGrid = g.baris * g.sel;
  const lewat = Math.max(
    0, -x, x - lebarGrid, -y, y - tinggiGrid,
  );
  const cincin = Math.ceil((maks + lewat) / g.sel);
  let terbaik: T | null = null;
  let d2 = maks * maks;
  for (let b = Math.max(0, b0 - cincin); b <= Math.min(g.baris - 1, b0 + cincin); b++) {
    for (let c = Math.max(0, c0 - cincin); c <= Math.min(g.kolom - 1, c0 + cincin); c++) {
      for (const t of g.isi[b * g.kolom + c] as T[]) {
        const dd = (t.x - x) * (t.x - x) + (t.y - y) * (t.y - y);
        if (dd < d2 || (terbaik === null && dd <= d2)) {
          d2 = dd;
          terbaik = t;
        }
      }
    }
  }
  return terbaik ? { t: terbaik, jarak: Math.sqrt(d2) } : null;
}

/** Jarak ke tetangga terdekat untuk tiap titik (brute force; dipakai tiap
 *  kali peta dibangun ulang, 1.062 titik = 0,56 juta pasangan). Yang
 *  dibandingkan jarak kuadrat, akarnya satu kali per titik: `Math.hypot` per
 *  pasangan diukur 37 ms untuk 1.062 titik, versi ini 2,3 ms, selisih 1e-14. */
export function jarakTetangga(titik: readonly TitikRuang[]): number[] {
  return titik.map((p, i) => {
    let d2 = Infinity;
    for (let j = 0; j < titik.length; j++) {
      if (j === i) continue;
      const q = titik[j] as TitikRuang;
      const dx = p.x - q.x;
      const dy = p.y - q.y;
      const dd = dx * dx + dy * dy;
      if (dd < d2) d2 = dd;
    }
    return Math.sqrt(d2);
  });
}

/* --------------------------------------------------------------- ikhtisar */

/** Ukuran dasar peta ikhtisar, sama dengan `viewBox` layar Langit lama. Pusat
 *  32 rasi (`TATA`) tidak berubah: pelajar yang hafal letak "HTML" di pojok
 *  kiri atas tetap menemukannya di sana. */
export const LEBAR_PETA = 1400;
export const TINGGI_PETA = 1420;

/** Kotak tiap rasi di ikhtisar, satuan dasar. Sama dengan yang dipakai
 *  `Langit.tsx` lama (`bentukRasi(n, "langit·" + key, 150, 112)`). */
export const KOTAK_RASI: [number, number] = [150, 112];

export interface BabLangit {
  nomor: number;
  judul: string;
  materi: number[];
}

export interface BahasaLangit {
  key: string;
  label: string;
  persen?: number;
  materi: MateriBintang[];
  bab?: BabLangit[];
}

export type TataRasi = Record<string, [number, number, string]>;

export interface BintangPeta extends TitikRuang {
  rasi: number;
  i: number;
  status: StatusBintang;
  /** Jarak ke tetangga terdekat, piksel. */
  nn: number;
  /** Jari-jari gambar, piksel (sudah dibatasi tetangga). */
  r: number;
}

export interface RasiPeta {
  key: string;
  label: string;
  /** Pusat rasi, piksel. */
  cx: number;
  cy: number;
  keluarga: string;
  jumlah: number;
  selesai: number;
  bintang: BintangPeta[];
  /** Indeks materi yang memulai sebuah bab (tidak ada garis menuju mereka). */
  awalBab: Set<number>;
  /** Poligon wilayah (piksel): yang disorot, dan batas klik rasi. */
  wilayah: Titik[];
}

export interface Ikhtisar {
  skala: number;
  lebar: number;
  tinggi: number;
  rasi: RasiPeta[];
  semua: BintangPeta[];
  grid: Grid<BintangPeta>;
}

/** Jari-jari sasaran gambar per status, piksel. Urutan ukurannya adalah
 *  "terang bintang": selesai > sebagian > baru > terkunci (magnitudo, bukan
 *  hiasan). Angkanya diukur terhadap jarak tetangga: median 8,65 px di 1905,
 *  jadi 3,7 px (diameter 7,4) muat untuk bintang yang bisa dibuka, yang justru
 *  gugus terdekatnya renggang. */
export const JARI_PX: Record<StatusBintang, number> = {
  selesai: 4.6,
  sebagian: 4.0,
  baru: 3.7,
  terkunci: 2.4,
};

/** Jari-jari akhir: batas status, dibatasi 46 persen jarak ke tetangga
 *  supaya dua bintang tidak pernah bersentuhan, dan tidak pernah di bawah
 *  lantai 1,25 px (di bawah itu titik tidak lagi terlihat di DPR 1). */
export function jariIkhtisar(status: StatusBintang, nnPx: number): number {
  return Math.min(JARI_PX[status], Math.max(1.25, 0.46 * nnPx));
}

/**
 * Ujung-ujung garis rasi di ikhtisar: dari tepi glif ke tepi glif, tanpa
 * celah. `ruasAntara` (rasi-geometri.ts, milik peta lama dan Bahasa) menolak
 * ruas yang celah tepinya di bawah 4 satuan dan berhenti 3 satuan sebelum
 * glif; di satuan viewBox itu wajar, tetapi di sini jari-jarinya piksel dan
 * jarak tetangga cuma 6 sampai 9 px, sehingga garisnya tergambar 35, 53, dan
 * 69 persen di akar 1156, 1440, dan 1905 px (peta lama 76). Glif digambar di
 * atas garis, jadi ujung di tepinya tidak meninggalkan celah dan tidak
 * mencoret bagian dalam cincin "baru". `null` hanya bila kedua glif saling
 * bersentuhan: tidak ada garis yang bisa terlihat di antaranya.
 */
export function ruasIkhtisar(
  a: Titik,
  b: Titik,
  ra: number,
  rb: number,
): { x1: number; y1: number; x2: number; y2: number } | null {
  const dx = b[0] - a[0];
  const dy = b[1] - a[1];
  const d = Math.hypot(dx, dy);
  if (d <= ra + rb) return null;
  const ux = dx / d;
  const uy = dy / d;
  return {
    x1: a[0] + ux * ra,
    y1: a[1] + uy * ra,
    x2: b[0] - ux * rb,
    y2: b[1] - uy * rb,
  };
}

/** Pengembangan wilayah rasi, piksel. */
export const padWilayah = (skala: number): number => 16 + 8 * skala;

/**
 * Seluruh peta ikhtisar untuk lebar tertentu. `skala` = piksel per satuan
 * dasar (lebar wadah / 1400).
 *
 * Rasi yang belum terdaftar di `tata` tetap digambar di baris cadangan paling
 * bawah, jalur yang sama dengan versi lama: menambah kurikulum tidak boleh
 * membuat sebuah kurikulum hilang dari peta.
 */
export function bangunIkhtisar(
  bahasa: readonly BahasaLangit[],
  tata: TataRasi,
  skala: number,
): Ikhtisar {
  let cadangan = 0;
  const semua: BintangPeta[] = [];
  const rasi: RasiPeta[] = bahasa.map((b, urut) => {
    const letak = tata[b.key] ?? [140 + cadangan++ * 180, 820, "tech"];
    const cx = (letak[0] as number) * skala;
    const cy = (letak[1] as number) * skala;
    const titik = bentukRasi(
      b.materi.length, "langit·" + b.key, KOTAK_RASI[0], KOTAK_RASI[1],
    );
    const bintang: BintangPeta[] = b.materi.map((m, i) => {
      const p = titik[i] as Titik;
      return {
        rasi: urut, i, x: cx + p[0] * skala, y: cy + p[1] * skala,
        status: statusBintang(m), nn: 0, r: 0,
      };
    });
    semua.push(...bintang);
    return {
      key: b.key,
      label: b.label,
      cx, cy,
      keluarga: letak[2] as string,
      jumlah: b.materi.length,
      selesai: b.materi.filter((m) => m.status === "selesai").length,
      bintang,
      awalBab: new Set((b.bab ?? []).map((x) => x.materi[0] as number)),
      wilayah: wilayahPoligon(bintang.map((t) => [t.x, t.y] as Titik), padWilayah(skala)),
    };
  });
  const nn = jarakTetangga(semua);
  semua.forEach((s, k) => {
    s.nn = nn[k] as number;
    s.r = jariIkhtisar(s.status, s.nn);
  });
  const lebar = LEBAR_PETA * skala;
  const tinggi = TINGGI_PETA * skala;
  return { skala, lebar, tinggi, rasi, semua, grid: bangunGrid(semua, lebar, tinggi, 24) };
}

/** Jarak (piksel) dari kursor yang masih dianggap "mengenai rasi". Di atas
 *  ini, klik di ruang kosong tidak membuka apa pun. */
export const JANGKAU_RASI_PX = 40;
/** Jarak yang masih dianggap "mengenai bintang itu sendiri" (memilih bintang
 *  terdekat sebagai bintang awal lensa, dan memunculkan tip judulnya). */
export const JANGKAU_BINTANG_PX = 14;

export interface Sasaran {
  bintang: BintangPeta;
  jarak: number;
  /** `true` kalau cukup dekat untuk dianggap menunjuk bintang itu sendiri. */
  tepat: boolean;
}

/** Sasaran untuk satu titik kursor, atau `null` kalau di ruang kosong.
 *  Urutannya: bintang dalam jangkauan, lalu wilayah rasi. Wilayah itu yang
 *  membuat celah di antara bintang yang renggang tetap milik rasinya. */
export function sasaranIkhtisar(ik: Ikhtisar, x: number, y: number): Sasaran | null {
  const h = terdekat(ik.grid, x, y, JANGKAU_RASI_PX);
  if (h) return { bintang: h.t, jarak: h.jarak, tepat: h.jarak <= JANGKAU_BINTANG_PX };
  let terbaik: Sasaran | null = null;
  for (const r of ik.rasi) {
    if (!titikDiPoligon(r.wilayah, x, y)) continue;
    for (const b of r.bintang) {
      const d = Math.hypot(b.x - x, b.y - y);
      if (!terbaik || d < terbaik.jarak) terbaik = { bintang: b, jarak: d, tepat: false };
    }
  }
  return terbaik;
}


/* ------------------------------------------------------------------ glif */

const f2 = (n: number): string => n.toFixed(2);

/**
 * Bentuk bintang per status. SEMUANYA path berkoordinat MUTLAK, bukan
 * `<g transform>`: CSS `transform` pada simpul yang posisinya ditulis lewat
 * atribut `transform` memarkirnya di titik asal (cacat Peta Karier yang sudah
 * pernah terjadi). Satu-satunya `transform` di layar ini adalah cincin
 * terpilih lensa (`.lt-ln-terpilih`), dan ia tidak punya atribut `transform`.
 *
 * Silhuetnya berbeda, bukan cuma warnanya: percik empat sudut (selesai),
 * cakram setengah terisi (sebagian), cincin (baru), belah ketupat (terkunci).
 * `isi` digambar dengan fill, `tepi` dengan stroke.
 */
export function bagianGlif(
  status: StatusBintang,
  x: number,
  y: number,
  r: number,
): { isi?: string; tepi?: string } {
  switch (status) {
    case "selesai": {
      // Percik: ujung di jarak r, pinggang di 0,27 r pada diagonal.
      const k = r * 0.27;
      return {
        isi:
          `M${f2(x)},${f2(y - r)}L${f2(x + k)},${f2(y - k)}L${f2(x + r)},${f2(y)}` +
          `L${f2(x + k)},${f2(y + k)}L${f2(x)},${f2(y + r)}L${f2(x - k)},${f2(y + k)}` +
          `L${f2(x - r)},${f2(y)}L${f2(x - k)},${f2(y - k)}Z`,
      };
    }
    case "sebagian":
      return {
        // Separuh kiri terisi: "dikerjakan, belum tuntas".
        isi: `M${f2(x)},${f2(y - r)}A${f2(r)},${f2(r)} 0 0 0 ${f2(x)},${f2(y + r)}Z`,
        tepi: lingkaran(x, y, r),
      };
    case "baru":
      return { tepi: lingkaran(x, y, r) };
    case "terkunci": {
      const s = r * 0.86;
      return {
        isi:
          `M${f2(x)},${f2(y - r)}L${f2(x + s)},${f2(y)}` +
          `L${f2(x)},${f2(y + r)}L${f2(x - s)},${f2(y)}Z`,
      };
    }
  }
}

/** Lingkaran sebagai path (dua busur), supaya banyak lingkaran bisa digabung
 *  jadi SATU atribut `d`. */
export function lingkaran(x: number, y: number, r: number): string {
  return `M${f2(x - r)},${f2(y)}a${f2(r)},${f2(r)} 0 1 0 ${f2(2 * r)},0a${f2(r)},${f2(r)} 0 1 0 ${f2(-2 * r)},0`;
}

/** Empat sudut braket di sekeliling sebuah titik: "ini sasaranmu". Statis;
 *  versi lama memutarnya selamanya dan satu putaran tak berhingga per
 *  kurikulum adalah hampir seluruh biaya CPU layar ini. */
export function pathBraket(x: number, y: number, R: number, panjang = 5): string {
  const a = x - R, b = x + R, c = y - R, d = y + R, p = panjang;
  return (
    `M${f2(a)},${f2(c + p)}V${f2(c)}H${f2(a + p)}` +
    `M${f2(b - p)},${f2(c)}H${f2(b)}V${f2(c + p)}` +
    `M${f2(b)},${f2(d - p)}V${f2(d)}H${f2(b - p)}` +
    `M${f2(a + p)},${f2(d)}H${f2(a)}V${f2(d - p)}`
  );
}

/* ----------------------------------------------------------------- wilayah */

/** Selubung cembung (monotone chain). Hasil berlawanan arah jarum jam dalam
 *  koordinat layar (y ke bawah). */
export function selubungCembung(titik: readonly Titik[]): Titik[] {
  const p = [...titik].sort((a, b) => a[0] - b[0] || a[1] - b[1]);
  if (p.length <= 2) return p;
  const silang = (o: Titik, a: Titik, b: Titik) =>
    (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0]);
  const bawah: Titik[] = [];
  for (const t of p) {
    while (bawah.length >= 2 &&
           silang(bawah[bawah.length - 2] as Titik, bawah[bawah.length - 1] as Titik, t) <= 0) bawah.pop();
    bawah.push(t);
  }
  const atas: Titik[] = [];
  for (let i = p.length - 1; i >= 0; i--) {
    const t = p[i] as Titik;
    while (atas.length >= 2 &&
           silang(atas[atas.length - 2] as Titik, atas[atas.length - 1] as Titik, t) <= 0) atas.pop();
    atas.push(t);
  }
  bawah.pop();
  atas.pop();
  return bawah.concat(atas);
}

/** Titik-titik poligon wilayah: selubung cembung yang dikembangkan `pad` piksel
 *  menjauhi pusatnya. Bentuk rasi tipis memanjang, jadi pembagian rata ke semua
 *  arah cukup (tidak butuh offset poligon yang sebenarnya). Ini BATAS SASARAN
 *  (`sasaranIkhtisar`): celah di antara bintang yang renggang tetap milik
 *  rasinya. Garis putus yang digambar saat rasi disorot BUKAN ini: selubung
 *  cembung melompati setiap lekukan rasi, jadi garisnya menggembung jauh dari
 *  bintang (sampai 69 px di SQL pada skala 1,286). Gambarnya dari `pathWilayah`. */
export function wilayahPoligon(titik: readonly Titik[], pad: number): Titik[] {
  const h = selubungCembung(titik);
  if (h.length < 3) return h;
  let cx = 0, cy = 0;
  for (const [x, y] of h) { cx += x; cy += y; }
  cx /= h.length; cy /= h.length;
  return h.map(([x, y]) => {
    const dx = x - cx, dy = y - cy;
    const d = Math.hypot(dx, dy) || 1;
    return [x + (dx / d) * pad, y + (dy / d) * pad] as Titik;
  });
}

/** Bantalan garis wilayah yang DIGAMBAR, piksel: jarak garis putus dari rangka
 *  rasi. Lebih ketat daripada `padWilayah` karena dihitung dari rangka, bukan
 *  dari selubung, jadi di mana pun garisnya sama jauh dari bintang atau ruas
 *  terdekat. Lantainya (14,9 px pada skala 0,571) masih di luar cincin sorot
 *  bintang (jari-jari 4,6 + 5) dan braket "berikutnya" (4,6 + 7). */
export const padKontur = (skala: number): number => 12 + 5 * skala;

/** Jarak titik (px, py) ke ruas a-b; a sama dengan b berarti ke satu titik. */
function jarakKeRuas(px: number, py: number, ax: number, ay: number, bx: number, by: number): number {
  const dx = bx - ax, dy = by - ay;
  const l2 = dx * dx + dy * dy;
  const t = l2 === 0 ? 0 : Math.max(0, Math.min(1, ((px - ax) * dx + (py - ay) * dy) / l2));
  return Math.hypot(px - (ax + t * dx), py - (ay + t * dy));
}

/** Tepi sel marching squares yang dipotong kontur, per kode sudut-di-dalam
 *  (kiri-atas 8, kanan-atas 4, kanan-bawah 2, kiri-bawah 1). Tepi: 0 atas,
 *  1 kanan, 2 bawah, 3 kiri. Kode 5 dan 10 pelana, dipilih di pemakainya. */
const POTONG: readonly (readonly (readonly [number, number])[])[] = [
  [], [[3, 2]], [[2, 1]], [[3, 1]], [[0, 1]], [], [[0, 2]], [[0, 3]],
  [[0, 3]], [[0, 2]], [], [[0, 1]], [[3, 1]], [[1, 2]], [[3, 2]], [],
];

/**
 * Lingkar-lingkar tertutup tempat jarak ke RANGKA rasi tepat `pad` piksel.
 * Rangka = tiap bintang ditambah ruas antara bintang BERURUTAN, termasuk ruas
 * yang tidak digambar di batas bab: tanpa jembatan itu celah antar-bab yang
 * lebih lebar dari 2 x `pad` memecah satu rasi jadi beberapa pulau.
 *
 * Ini kontur jarak (marching squares atas grid sel `pad / 6`), bukan selubung
 * cembung: garisnya mengikuti lekukan rasi dan tidak pernah lebih jauh dari
 * `pad` (ditambah galat interpolasi sub-piksel) dari bintang atau garisnya.
 * Medan jarak hanya dihitung di sekitar tiap ruas, jadi ongkosnya sebanding
 * dengan jumlah bintang, bukan luas kotak. Rongga yang cukup besar muncul
 * sebagai lingkar tersendiri, jadi gambarnya wajib memakai `fill-rule: evenodd`.
 * Rongga yang lebih kecil dari separuh cakram bantalan (pi x pad^2 / 2) tidak
 * digambar: di dalam rangka yang rapat ia terbaca sebagai noktah putus-putus,
 * bukan sebagai bentuk rasi.
 */
export function lingkarWilayah(titik: readonly Titik[], pad: number): Titik[][] {
  if (titik.length === 0 || !(pad > 0)) return [];
  const h = Math.max(1.5, pad / 6);
  const jangkau = pad + 2 * h;
  let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
  for (const [x, y] of titik) {
    x0 = Math.min(x0, x); x1 = Math.max(x1, x);
    y0 = Math.min(y0, y); y1 = Math.max(y1, y);
  }
  // Tepi grid selalu di luar kontur (jarak >= jangkau + h > pad): lingkarnya tertutup.
  const ox = x0 - jangkau - h, oy = y0 - jangkau - h;
  const kol = Math.ceil((x1 - ox + jangkau + h) / h) + 1;
  const bar = Math.ceil((y1 - oy + jangkau + h) / h) + 1;
  const f = new Float32Array(kol * bar).fill(pad + 4 * h);
  const cap = (ax: number, ay: number, bx: number, by: number) => {
    const i0 = Math.max(0, Math.floor((Math.min(ax, bx) - jangkau - ox) / h));
    const i1 = Math.min(kol - 1, Math.ceil((Math.max(ax, bx) + jangkau - ox) / h));
    const j0 = Math.max(0, Math.floor((Math.min(ay, by) - jangkau - oy) / h));
    const j1 = Math.min(bar - 1, Math.ceil((Math.max(ay, by) + jangkau - oy) / h));
    for (let j = j0; j <= j1; j++) {
      for (let i = i0; i <= i1; i++) {
        const d = jarakKeRuas(ox + i * h, oy + j * h, ax, ay, bx, by);
        const k = j * kol + i;
        if (d < (f[k] as number)) f[k] = d;
      }
    }
  };
  for (let i = 0; i < titik.length; i++) {
    const [ax, ay] = titik[i] as Titik;
    cap(ax, ay, ax, ay);
    if (i > 0) {
      const [px, py] = titik[i - 1] as Titik;
      cap(px, py, ax, ay);
    }
  }

  const dalam = (k: number): boolean => (f[k] as number) <= pad;
  const posisi = new Map<number, Titik>();
  const sambung = new Map<number, number[]>();
  /** Id tepi sel (i, j); `tepi` 0 atas, 1 kanan, 2 bawah, 3 kiri. Titik potongnya
   *  diinterpolasi linear di antara dua node yang statusnya berbeda. */
  const tepi = (i: number, j: number, sisi: number): number => {
    const jj = sisi === 2 ? j + 1 : j;
    const ii = sisi === 1 ? i + 1 : i;
    const tegak = sisi === 1 || sisi === 3;
    const id = (jj * kol + ii) * 2 + (tegak ? 1 : 0);
    if (!posisi.has(id)) {
      const ka = jj * kol + ii;
      const fa = f[ka] as number;
      const fb = f[tegak ? ka + kol : ka + 1] as number;
      const t = (pad - fa) / (fb - fa);
      posisi.set(id, [ox + ii * h + (tegak ? 0 : t * h), oy + jj * h + (tegak ? t * h : 0)]);
    }
    return id;
  };
  const hubung = (a: number, b: number) => {
    const sa = sambung.get(a);
    if (sa) sa.push(b); else sambung.set(a, [b]);
    const sb = sambung.get(b);
    if (sb) sb.push(a); else sambung.set(b, [a]);
  };
  for (let j = 0; j < bar - 1; j++) {
    for (let i = 0; i < kol - 1; i++) {
      const kk = j * kol + i;
      const kode = (dalam(kk) ? 8 : 0) | (dalam(kk + 1) ? 4 : 0) |
        (dalam(kk + kol + 1) ? 2 : 0) | (dalam(kk + kol) ? 1 : 0);
      if (kode === 0 || kode === 15) continue;
      let pasang = POTONG[kode] as readonly (readonly [number, number])[];
      if (kode === 5 || kode === 10) {
        const tengah =
          ((f[kk] as number) + (f[kk + 1] as number) + (f[kk + kol] as number) + (f[kk + kol + 1] as number)) / 4 <= pad;
        // 5 (kanan-atas + kiri-bawah di dalam) dan 10 (kiri-atas + kanan-bawah):
        // tengah di dalam menyambung dua sudut di dalam, jadi yang dipotong dua sudut luar.
        // Cabang ini tercapai 8 kali di korpus (8 dari 128 kombinasi rasi dan skala)
        // dan membaliknya hanya mengubah satu leher atau rongga selebar satu sel
        // (sekitar 3 px). Tidak ada pagar yang membedakannya: raster 1 px independen
        // sendiri berselisih dengan kontur di 14 dari 128 kasus, jadi bukan penagih
        // yang adil. Pagar mati yang disadari, bukan yang lupa dibuat.
        const sambungDalam: readonly (readonly [number, number])[] = kode === 5 ? [[0, 3], [1, 2]] : [[0, 1], [3, 2]];
        const pisahDalam: readonly (readonly [number, number])[] = kode === 5 ? [[0, 1], [3, 2]] : [[0, 3], [1, 2]];
        pasang = tengah ? sambungDalam : pisahDalam;
      }
      for (const [a, b] of pasang) hubung(tepi(i, j, a), tepi(i, j, b));
    }
  }

  const lingkar: Titik[][] = [];
  const sudah = new Set<number>();
  for (const awal of sambung.keys()) {
    if (sudah.has(awal)) continue;
    const jalan: Titik[] = [];
    let kini = awal, lalu = -1;
    for (;;) {
      sudah.add(kini);
      jalan.push(posisi.get(kini) as Titik);
      const tetangga = sambung.get(kini) as number[];
      const lanjut = tetangga[0] !== lalu ? tetangga[0] : tetangga[1];
      if (lanjut === undefined || lanjut === awal || sudah.has(lanjut)) break;
      lalu = kini;
      kini = lanjut;
    }
    if (jalan.length < 3) continue;
    // Luas lingkar (rumus tali sepatu). Lingkar luar selalu memuat cakram
    // berjari-jari `pad` di tiap bintang, jadi tidak pernah di bawah ambang.
    let luas = 0;
    for (let i = 0, j = jalan.length - 1; i < jalan.length; j = i++) {
      const [xi, yi] = jalan[i] as Titik;
      const [xj, yj] = jalan[j] as Titik;
      luas += xj * yi - xi * yj;
    }
    if (Math.abs(luas) / 2 >= (Math.PI * pad * pad) / 2) lingkar.push(jalan);
  }
  return lingkar;
}

/** Path garis wilayah yang digambar saat rasi disorot: satu `M...Z` per lingkar
 *  (`lingkarWilayah`). Kosong untuk rasi tanpa bintang. Penggambarnya wajib
 *  memasang `fill-rule: evenodd` supaya rongga tidak ikut terisi. */
export function pathWilayah(titik: readonly Titik[], pad: number): string {
  let d = "";
  for (const l of lingkarWilayah(titik, pad)) {
    d += `M${f2((l[0] as Titik)[0])},${f2((l[0] as Titik)[1])}`;
    for (let i = 1; i < l.length; i++) d += `L${f2((l[i] as Titik)[0])},${f2((l[i] as Titik)[1])}`;
    d += "Z";
  }
  return d;
}

/** Titik di dalam poligon? (ray casting; poligon cembung maupun tidak.) */
export function titikDiPoligon(poli: readonly Titik[], x: number, y: number): boolean {
  let dalam = false;
  for (let i = 0, j = poli.length - 1; i < poli.length; j = i++) {
    const [xi, yi] = poli[i] as Titik;
    const [xj, yj] = poli[j] as Titik;
    if (yi > y !== yj > y && x < ((xj - xi) * (y - yi)) / (yj - yi) + xi) dalam = !dalam;
  }
  return dalam;
}

/* ------------------------------------------------------------------ lensa */

export interface OpsiLensa {
  /** Ukuran kanvas lensa, piksel. */
  lebar: number;
  tinggi: number;
  /** Ruang kosong di tepi kanvas untuk label dan lencana bab. */
  tepiX: number;
  tepiY: number;
  /** Faktor pelebaran maksimum per sumbu (default 1,5). Rasi tinggi di kanvas
   *  lebar hanya memakai sepertiga lebarnya kalau diskalakan seragam, dan
   *  gugus padatnya menumpuk label. Pelebaran sampai 1,5 kali memberi
   *  median jarak tetangga +17 persen dan bintang yang muat glif 7 px naik dari
   *  95,8 ke 97,2 persen (1905 px); urutan bintang dan topologi garis tidak
   *  berubah. 1 = skala seragam persis seperti ikhtisar. */
  tarik?: number;
  /** Faktor ukuran huruf (>= 1, paling besar 2): setelan "Ukuran huruf" di
   *  Pengaturan menaikkan `rem` tetapi tidak piksel, jadi lebar dan tinggi
   *  lencana serta kotak nomor yang dipakai penata label ikut dikalikan.
   *  1 = persis lensa lama (lebar teks 12 px). */
  skalaTeks?: number;
}

export interface LabelLensa {
  x: number;
  y: number;
  jangkar: "start" | "middle" | "end";
}

export interface BintangLensa extends TitikRuang {
  i: number;
  status: StatusBintang;
  /** Indeks bab (posisi di `bab`), atau -1 kalau kurikulum tanpa bab. */
  bab: number;
  nn: number;
  r: number;
  label: LabelLensa;
}

export interface GarisLensa {
  bab: number;
  dari: number;
  ke: number;
  x1: number;
  y1: number;
  x2: number;
  y2: number;
}

export interface LencanaBab {
  nomor: number;
  judul: string;
  /** Indeks bintang pertama dan terakhir bab ini. */
  awal: number;
  akhir: number;
  x: number;
  y: number;
  /** Ukuran perkiraan (piksel) untuk penempatan, bukan untuk gambar. */
  w: number;
  h: number;
}

/** Lencana teks "berikutnya": bentuk (braket) + warna (kuning) + KATA. Braket
 *  saja tidak cukup: reticle papan ketik global juga braket. */
export interface LencanaBerikut {
  i: number;
  x: number;
  y: number;
  w: number;
  h: number;
}

export interface Lensa {
  lebar: number;
  tinggi: number;
  berikut: LencanaBerikut | null;
  /** Label yang akhirnya menimpa sesuatu (bukan jaminan, ukuran mutu). */
  tumpang: { bintang: number; garis: number; keluar: number };
  bintang: BintangLensa[];
  garis: GarisLensa[];
  bab: LencanaBab[];
  grid: Grid<BintangLensa>;
}

/** Jari-jari glif lensa per status, piksel. Dibatasi 46 persen jarak ke
 *  tetangga, dengan lantai 3,2 px (di bawah itu silhuetnya tidak terbaca). */
export const JARI_LENSA_PX: Record<StatusBintang, number> = {
  selesai: 10,
  sebagian: 8,
  baru: 7.5,
  terkunci: 6,
};

export function jariLensa(status: StatusBintang, nnPx: number): number {
  return Math.min(JARI_LENSA_PX[status], Math.max(3.2, 0.46 * nnPx));
}

/** Angka Romawi untuk lencana bab: tabel `ROMAWI` milik `rasi-geometri.ts`,
 *  dan angka di atas 20 jatuh ke angka biasa seperti `tataPetaRasi`. */
export const romawi = (n: number): string => ROMAWI[n] || String(n);

interface Kotak {
  x0: number;
  y0: number;
  x1: number;
  y1: number;
}

const beririsan = (a: Kotak, b: Kotak): boolean =>
  a.x0 < b.x1 && a.x1 > b.x0 && a.y0 < b.y1 && a.y1 > b.y0;

/** Segmen memotong kotak? (uji tepi + titik ujung di dalam). */
function segmenMasukKotak(
  x1: number, y1: number, x2: number, y2: number, k: Kotak,
): boolean {
  const di = (x: number, y: number) => x > k.x0 && x < k.x1 && y > k.y0 && y < k.y1;
  if (di(x1, y1) || di(x2, y2)) return true;
  const potong = (ax: number, ay: number, bx: number, by: number,
                  cx: number, cy: number, dx: number, dy: number) => {
    const d = (bx - ax) * (dy - cy) - (by - ay) * (dx - cx);
    if (d === 0) return false;
    const t = ((cx - ax) * (dy - cy) - (cy - ay) * (dx - cx)) / d;
    const u = ((cx - ax) * (by - ay) - (cy - ay) * (bx - ax)) / d;
    return t >= 0 && t <= 1 && u >= 0 && u <= 1;
  };
  return (
    potong(x1, y1, x2, y2, k.x0, k.y0, k.x1, k.y0) ||
    potong(x1, y1, x2, y2, k.x1, k.y0, k.x1, k.y1) ||
    potong(x1, y1, x2, y2, k.x1, k.y1, k.x0, k.y1) ||
    potong(x1, y1, x2, y2, k.x0, k.y1, k.x0, k.y0)
  );
}

/** Enam belas arah, urutan kesukaan: serong kanan-atas lebih dulu (tempat
 *  mata mencari nomor), lalu kanan, lalu sisanya berselang-seling. */
const SUDUT_KANDIDAT: number[] = [
  -Math.PI / 4, 0, Math.PI / 4, -Math.PI / 2, Math.PI / 2,
  (-3 * Math.PI) / 4, Math.PI, (3 * Math.PI) / 4,
  -Math.PI / 8, Math.PI / 8, (-3 * Math.PI) / 8, (3 * Math.PI) / 8,
  (-5 * Math.PI) / 8, (5 * Math.PI) / 8, (-7 * Math.PI) / 8, (7 * Math.PI) / 8,
];
const JARAK_KANDIDAT = [0, 7, 15];
/** Lencana (bab, "berikutnya") lebih penting daripada nomor dan lebih lebar:
 *  kalau tiga jarak dekat semuanya menimpa sesuatu, dua jarak lagi dicoba
 *  sebelum menerima tumpang tindih. */
const JARAK_LENCANA = [0, 7, 15, 26, 40];

/**
 * Lensa sebuah rasi: bentuk yang SAMA dengan ikhtisar, diperbesar sampai
 * mengisi kanvas.
 *
 * Label nomor dan lencana bab ditempatkan serakus mungkin tanpa bertabrakan:
 * tiap label mencoba enam belas arah dan memilih yang paling sedikit memotong
 * bintang, garis, atau label lain. Ini bukan penataan optimal, cuma cukup
 * untuk 60 bintang; yang dijamin uji adalah TIDAK ADA label yang keluar
 * kanvas dan jarak antarbintang tidak pernah kurang dari dua kali jari-jari
 * yang dipakai.
 */
export function bangunLensa(
  materi: readonly MateriBintang[],
  bab: readonly BabLangit[],
  key: string,
  opsi: OpsiLensa,
): Lensa {
  const { lebar, tinggi, tepiX, tepiY } = opsi;
  const sk = Math.min(2, Math.max(1, opsi.skalaTeks ?? 1));
  const n = materi.length;
  const kotakW = Math.max(40, lebar - 2 * tepiX);
  const kotakH = Math.max(40, tinggi - 2 * tepiY);
  const dasar = bentukRasi(n, "langit·" + key, kotakW, kotakH);
  const tarik = Math.max(1, opsi.tarik ?? 1.5);
  const bw = Math.max(1e-6, Math.max(...dasar.map((p) => p[0])) - Math.min(...dasar.map((p) => p[0])));
  const bh = Math.max(1e-6, Math.max(...dasar.map((p) => p[1])) - Math.min(...dasar.map((p) => p[1])));
  const sx = n > 1 ? Math.min(kotakW / bw, tarik) : 1;
  const sy = n > 1 ? Math.min(kotakH / bh, tarik) : 1;
  const titik = dasar.map(([x, y]) => [x * sx, y * sy] as Titik);

  const babDari: number[] = Array.from({ length: n }, () => -1);
  bab.forEach((b, k) => b.materi.forEach((i) => { babDari[i] = k; }));

  const bintang: BintangLensa[] = materi.map((m, i) => {
    const p = titik[i] as Titik;
    return {
      i, x: lebar / 2 + p[0], y: tinggi / 2 + p[1],
      status: statusBintang(m), bab: babDari[i] as number,
      nn: 0, r: 0, label: { x: 0, y: 0, jangkar: "start" },
    };
  });
  const nn = jarakTetangga(bintang);
  bintang.forEach((s, k) => {
    s.nn = Number.isFinite(nn[k]) ? (nn[k] as number) : 1e6;
    s.r = jariLensa(s.status, s.nn);
  });

  // Garis di dalam satu bab saja; batas bab sengaja tanpa garis, seperti
  // peta lama: tiap bab adalah rasi kecil di dalam rasi besar.
  const garis: GarisLensa[] = [];
  for (let i = 1; i < n; i++) {
    const a = bintang[i - 1] as BintangLensa;
    const b = bintang[i] as BintangLensa;
    if (a.bab !== b.bab) continue;
    const dx = b.x - a.x, dy = b.y - a.y;
    const d = Math.hypot(dx, dy);
    const ra = a.r + 4, rb = b.r + 4;
    if (d < ra + rb + 4) continue;
    garis.push({
      bab: a.bab, dari: i - 1, ke: i,
      x1: a.x + (dx / d) * ra, y1: a.y + (dy / d) * ra,
      x2: b.x - (dx / d) * rb, y2: b.y - (dy / d) * rb,
    });
  }

  // Kotak terlarang: bintang (dengan celah) dan segmen garis.
  const terisi: Kotak[] = bintang.map((s) => ({
    x0: s.x - s.r - 2, y0: s.y - s.r - 2, x1: s.x + s.r + 2, y1: s.y + s.r + 2,
  }));
  const dalam = (k: Kotak) =>
    k.x0 >= 2 && k.y0 >= 2 && k.x1 <= lebar - 2 && k.y1 <= tinggi - 2;

  const tumpang = { bintang: 0, garis: 0, keluar: 0 };
  const tempatkan = (
    px: number, py: number, pr: number, w: number, h: number, abaikan: number,
    jarakCalon: readonly number[] = JARAK_KANDIDAT,
  ): { x: number; y: number; jangkar: "start" | "middle" | "end"; kotak: Kotak } => {
    type Calon = {
      skor: number; x: number; y: number; jangkar: "start" | "middle" | "end"; kotak: Kotak;
      nb: number; ng: number; kl: number;
    };
    let terbaik: Calon | null = null;
    for (const jarakExtra of jarakCalon) {
      for (const [si, sudut] of SUDUT_KANDIDAT.entries()) {
        const cx = px + Math.cos(sudut) * (pr + 5 + jarakExtra + w / 2 * Math.abs(Math.cos(sudut)));
        const cy = py + Math.sin(sudut) * (pr + 5 + jarakExtra + h / 2 * Math.abs(Math.sin(sudut)));
        const k: Kotak = { x0: cx - w / 2, y0: cy - h / 2, x1: cx + w / 2, y1: cy + h / 2 };
        let skor = si * 0.01 + jarakExtra * 0.05;
        const kl = dalam(k) ? 0 : 1;
        let nb = 0, ng = 0;
        terisi.forEach((o, idx) => { if (idx !== abaikan && beririsan(k, o)) nb += 1; });
        for (const g of garis) {
          if (segmenMasukKotak(g.x1, g.y1, g.x2, g.y2, k)) ng += 1;
        }
        skor += kl * 1000 + nb * 10 + ng * 4;
        if (!terbaik || skor < terbaik.skor) {
          const jangkar = Math.cos(sudut) > 0.4 ? "start" : Math.cos(sudut) < -0.4 ? "end" : "middle";
          terbaik = {
            skor,
            x: jangkar === "start" ? k.x0 : jangkar === "end" ? k.x1 : cx,
            y: cy, jangkar, kotak: k, nb, ng, kl,
          };
        }
      }
    }
    const t = terbaik as NonNullable<typeof terbaik>;
    if (t.nb) tumpang.bintang += 1;
    if (t.ng) tumpang.garis += 1;
    if (t.kl) tumpang.keluar += 1;
    return { x: t.x, y: t.y, jangkar: t.jangkar, kotak: t.kotak };
  };

  // Braket "berikutnya" (r + 9) adalah penanda terpenting di lensa: ia ikut
  // jadi kotak terlarang SEBELUM lencana bab ditempatkan.
  const ib = berikutDari(materi as MateriBintang[]);
  if (ib !== null) {
    const sb = bintang[ib] as BintangLensa;
    terisi.push({ x0: sb.x - sb.r - 11, y0: sb.y - sb.r - 11, x1: sb.x + sb.r + 11, y1: sb.y + sb.r + 11 });
  }

  // Lencana bab lebih dulu (lebih penting), lalu nomor tiap bintang.
  const lencana: LencanaBab[] = bab.map((b, k) => {
    const anggota = bintang.filter((s) => s.bab === k);
    const awal = anggota[0] as BintangLensa | undefined;
    const akhir = anggota[anggota.length - 1] as BintangLensa | undefined;
    const teks = romawi(b.nomor);
    const w = (teks.length * 9 + 16) * sk;
    const h = 22 * sk;
    if (!awal || !akhir) {
      return { nomor: b.nomor, judul: b.judul, awal: -1, akhir: -1, x: 0, y: 0, w, h };
    }
    const t = tempatkan(awal.x, awal.y, awal.r + 6, w, h, awal.i, JARAK_LENCANA);
    terisi.push(t.kotak);
    return {
      nomor: b.nomor, judul: b.judul, awal: awal.i, akhir: akhir.i,
      x: (t.kotak.x0 + t.kotak.x1) / 2, y: (t.kotak.y0 + t.kotak.y1) / 2, w, h,
    };
  });

  // Lencana "berikutnya": sebelum nomor, karena ia lebih penting dan lebih lebar.
  let berikut: LencanaBerikut | null = null;
  if (ib !== null) {
    const sb = bintang[ib] as BintangLensa;
    const w = 82 * sk;
    const h = 22 * sk;
    const t = tempatkan(sb.x, sb.y, sb.r + 12, w, h, sb.i, JARAK_LENCANA);
    terisi.push(t.kotak);
    berikut = { i: sb.i, x: (t.kotak.x0 + t.kotak.x1) / 2, y: (t.kotak.y0 + t.kotak.y1) / 2, w, h };
  }

  // Bintang yang paling terhimpit dilayani lebih dulu: ia punya paling sedikit
  // tempat kosong, dan yang longgar hampir selalu menemukan tempat.
  const urutLabel = [...bintang].sort((a, b) => a.nn - b.nn);
  for (const s of urutLabel) {
    const teks = String(s.i + 1);
    const w = (teks.length * 6.8 + 3) * sk;
    const h = 14 * sk;
    const t = tempatkan(s.x, s.y, s.r, w, h, s.i);
    terisi.push(t.kotak);
    s.label = { x: t.x, y: t.y, jangkar: t.jangkar };
  }

  return {
    lebar, tinggi, berikut, tumpang, bintang, garis, bab: lencana,
    grid: bangunGrid(bintang, lebar, tinggi, 24),
  };
}

/** Jari-jari pencarian bintang di lensa: bintang terdekat yang masih dalam
 *  jarak ini dianggap ditunjuk. Sama dengan separuh sasaran 44 px, dan
 *  sengaja lebih besar daripada glif terbesar (10 px). */
export const JANGKAU_LENSA_PX = 22;

export function sasaranLensa(l: Lensa, x: number, y: number): BintangLensa | null {
  const h = terdekat(l.grid, x, y, JANGKAU_LENSA_PX);
  return h ? h.t : null;
}

/** Kartu judul hover lensa (WCAG 1.4.13): boleh dilayangi dan tidak menimpa
 *  bintangnya. Lebar 260 = `max-width` `.lt-ln-tip` di CSS. Tinggi 64 adalah
 *  tinggi penempatan (bintang 32 px dari tepi atas), bukan batas CSS: kartu
 *  terukur 57, 76, dan 94 px untuk satu, dua, dan tiga baris judul, dan
 *  ketiganya tetap melingkupi bintangnya. */
export const LEBAR_TIP_MAKS = 260;
export const TINGGI_TIP_MAKS = 64;
/** Jarak antara tepi glif dan tepi kartu. Cukup kecil supaya jalan dari
 *  bintang ke kartu tetap di dalam `JARAK_TAHAN_PX`. */
export const CELAH_TIP = 4;
/** Kanvas yang lebih sempit tidak punya tempat untuk kartu di samping bintang
 *  (260 + dua kali jarak + tepi); di sana tidak ada kartu hover, dan isinya
 *  ada di panel. Itu juga lebar sentuh, yang tidak punya hover. */
export const LEBAR_KANVAS_TIP_MIN = 560;
/** Lebar koridor (setengah tinggi, px) dari bintang ke kartunya. */
export const KORIDOR_TIP_PX = 8;

/**
 * Letak kartu judul: di KANAN bintang kalau muat, kalau tidak di kiri; secara
 * tegak dipusatkan pada bintang lalu dijepit ke kanvas, jadi bintangnya
 * selalu berada di antara tepi atas dan bawah kartu. Hasilnya `kiri`/`atas`
 * adalah pojok kartu berukuran maksimum; kartu yang lebih kecil menempel di
 * sisi dekat bintang (`sisi` memberi tahu CSS sisi mana). `null` di kanvas
 * yang lebih sempit dari `LEBAR_KANVAS_TIP_MIN`.
 */
export function tempatTip(
  b: { x: number; y: number; r: number },
  lebar: number,
  tinggi: number,
  w: number = LEBAR_TIP_MAKS,
  h: number = TINGGI_TIP_MAKS,
): { kiri: number; atas: number; sisi: "kanan" | "kiri" } | null {
  if (lebar < LEBAR_KANVAS_TIP_MIN) return null;
  const kanan = b.x + b.r + CELAH_TIP;
  const muat = kanan + w <= lebar - 4;
  const kiri = muat ? kanan : Math.max(4, b.x - b.r - CELAH_TIP - w);
  const atas = Math.min(Math.max(4, b.y - h / 2), Math.max(4, tinggi - h - 4));
  return { kiri, atas, sisi: muat ? "kanan" : "kiri" };
}

/**
 * Sorot mana yang berlaku: `kini` (hasil `sasaranLensa`) atau bintang yang
 * SEDANG disorot (`lama`)? Penunjuk yang berjalan dari bintang ke kartunya
 * melewati sel tetangga, dan tanpa tahanan kartunya berganti di tengah jalan
 * (WCAG 1.4.13 "hoverable"). Tahanan hanya berlaku di KORIDOR: persegi
 * panjang dari pusat bintang sampai tepi dekat kartu, selebar
 * `KORIDOR_TIP_PX` ke atas dan ke bawah (atau jari-jari glif, mana yang lebih
 * besar). Penunjuk yang berada di atas glif bintang lain (jari-jari + 3 px)
 * tidak pernah ditahan: bintang yang terhimpit tetap bisa dicapai.
 */
export function pilihSorotLensa(
  lama: BintangLensa | null,
  kini: BintangLensa | null,
  px: number,
  py: number,
  lebar: number,
  tinggi: number,
): BintangLensa | null {
  if (!lama || !kini || lama.i === kini.i) return kini;
  if (Math.hypot(kini.x - px, kini.y - py) <= kini.r + 3) return kini;
  const t = tempatTip(lama, lebar, tinggi);
  if (!t) return kini;
  const tepi = t.sisi === "kanan" ? t.kiri : t.kiri + LEBAR_TIP_MAKS;
  const x0 = Math.min(lama.x, tepi), x1 = Math.max(lama.x, tepi);
  const lebarKor = Math.max(lama.r, KORIDOR_TIP_PX);
  return px >= x0 && px <= x1 && Math.abs(py - lama.y) <= lebarKor ? lama : kini;
}

/**
 * Bintang lain yang pusatnya tertutup kartu judul bintang yang sedang
 * disorot, ditunjuk penunjuk yang berada di atas kartu itu. Kartu hover
 * menangkap penunjuk supaya bisa dilayangi (WCAG 1.4.13), dan itu membuat 21
 * sampai 28 persen perpindahan alami dari satu bintang ke tetangganya tidak
 * pernah sampai ke svg: hover dan klik mendarat di kartu. Kartu meneruskannya:
 * bintang lain yang glifnya (jari-jari + 3 px, ukuran yang sama dengan
 * `pilihSorotLensa`) ada di bawah penunjuk mengambil sorot, yang terdekat
 * menang. `null` = penunjuk tidak di atas glif mana pun, dan kartu ini tetap.
 */
export function bintangDiBawahKartu(
  l: Lensa,
  lamaI: number,
  px: number,
  py: number,
): BintangLensa | null {
  let terbaik: BintangLensa | null = null;
  let jarak = Infinity;
  for (const s of l.bintang) {
    if (s.i === lamaI) continue;
    const d = Math.hypot(s.x - px, s.y - py);
    if (d <= s.r + 3 && d < jarak) {
      jarak = d;
      terbaik = s;
    }
  }
  return terbaik;
}

/**
 * Garis penunjuk dari bintang terpilih ke tepi kanvas tempat panel menempel.
 * Mode "kanan": mendatar ke tepi kanan. Mode "bawah": tegak ke tepi bawah
 * (panel ditumpuk di bawah kanvas di lebar sempit). Mengembalikan path
 * mutlak dan koordinat ujungnya, yang juga dipakai CSS untuk menjajarkan takik
 * panel.
 */
export function jalurPenunjuk(
  b: { x: number; y: number; r: number },
  lebar: number,
  tinggi: number,
  mode: "kanan" | "bawah",
): { d: string; ujungX: number; ujungY: number } {
  const jarak = b.r + 10;
  if (mode === "kanan") {
    return {
      d: `M${f2(b.x + jarak)},${f2(b.y)}H${f2(lebar)}`,
      ujungX: lebar, ujungY: b.y,
    };
  }
  return {
    d: `M${f2(b.x)},${f2(b.y + jarak)}V${f2(tinggi)}`,
    ujungX: b.x, ujungY: tinggi,
  };
}

/** Tombol pengubah yang MENGEMBALIKAN sebuah tombol ke peramban: Alt+Panah =
 *  Mundur/Maju (Linux, Windows), Ctrl+Home/End = gulir dokumen, Meta+Panah =
 *  Mundur/Maju (macOS). Shift tidak termasuk: tidak ada tindakan peramban untuk
 *  Shift+Panah di luar kolom teks. */
export interface Pengubah {
  alt?: boolean;
  ctrl?: boolean;
  meta?: boolean;
}

/** Langkah papan ketik: ke bintang berikutnya/sebelumnya dalam urutan baca
 *  (= urutan indeks = garis rasi), ke awal/akhir, atau antar-bab. Mengembalikan
 *  indeks bintang tujuan, atau `null` kalau tombolnya bukan milik pohon ini
 *  (termasuk SEMUA tombol yang dipegang bersama Alt, Ctrl, atau Meta). */
export function langkahTombol(
  kunci: string,
  kini: number,
  jumlah: number,
  babDari: readonly number[],
  awalBab: readonly number[],
  mod?: Pengubah,
): number | null {
  if (mod && (mod.alt || mod.ctrl || mod.meta)) return null;
  const jepitI = (i: number) => Math.max(0, Math.min(jumlah - 1, i));
  switch (kunci) {
    case "ArrowRight":
    case "ArrowDown":
      return jepitI(kini + 1);
    case "ArrowLeft":
    case "ArrowUp":
      return jepitI(kini - 1);
    case "Home":
      return 0;
    case "End":
      return jumlah - 1;
    case "PageDown": {
      const b = babDari[kini] ?? -1;
      const tujuan = awalBab.find((a, k) => k > b && a >= 0);
      return tujuan === undefined ? jepitI(jumlah - 1) : tujuan;
    }
    case "PageUp": {
      const b = babDari[kini] ?? -1;
      const awalIni = awalBab[b] ?? 0;
      if (kini > awalIni) return awalIni;
      for (let k = b - 1; k >= 0; k--) {
        const a = awalBab[k];
        if (a !== undefined && a >= 0) return a;
      }
      return 0;
    }
    default:
      return null;
  }
}

/* ------------------------------------------------------------------- gulir */

/** Napas antara tepi layar (atau bawah pil atas) dan benda yang digulir tampak. */
export const CELAH_GULIR = 8;
/** Letak tepi atas panel di layar sesudah menggulir ke sana (mode panel di
 *  bawah kanvas): 40 persen dari tinggi layar menyisakan 60 persen untuk
 *  panel, dan sisanya masih menunjukkan bawah kanvas tempat bintang dipilih. */
export const LETAK_PANEL = 0.4;

/**
 * Berapa piksel jendela harus digulir (positif = ke bawah) supaya sebuah benda
 * `[atas, bawah]` (koordinat layar saat ini) tampak penuh di antara
 * `batasAtas + celah` (bawah pil atas yang melayang) dan `tinggiLayar - celah`.
 * 0 bila sudah tampak. Benda yang lebih tinggi daripada ruang yang ada
 * disejajarkan tepi atasnya. `focus({ preventScroll: true })` dipakai di lensa
 * supaya peramban tidak melompat sendiri, jadi inilah satu-satunya yang
 * menjaga bintang berfokus tetap terlihat pada zum 125 persen ke atas dan
 * jendela pendek.
 */
export function deltaGulirTampak(
  atas: number,
  bawah: number,
  tinggiLayar: number,
  batasAtas: number,
  celah: number = CELAH_GULIR,
): number {
  const lo = batasAtas + celah;
  const hi = tinggiLayar - celah;
  if (bawah - atas > hi - lo) return atas - lo;
  if (atas < lo) return atas - lo;
  if (bawah > hi) return bawah - hi;
  return 0;
}

/** Jarak (px) dari pusat bintang terpilih ke tepi luar penanda pilihannya
 *  (`.lt-ln-terpilih-isi`): dipakai penggambar dan `deltaGulirPanel`. */
export const RUANG_TERPILIH = 9;

/**
 * Gulir sesudah sebuah bintang DIPILIH di mode panel-di-bawah: bila judul
 * panel (`[panelAtas, judulBawah]`) belum tampak penuh, jendela digulir sampai
 * tepi atas panel berada di `LETAK_PANEL` tinggi layar (tidak lebih tinggi
 * daripada bawah pil atas + celah). 0 bila judulnya sudah tampak.
 *
 * `bintangAtas` (tepi atas penanda bintang terpilih, koordinat layar saat ini)
 * membatasi gulir ke bawah: kanvas ada di atas panel, jadi menggulir ke judul
 * panel mendorong bintang di bagian atas kanvas ke bawah pil atas tepat saat
 * ia dipilih (terukur: 4 dari 12 klik di 320x568 sampai 952x600). Bintang
 * yang tetap tampak lebih penting daripada judul yang tampak penuh.
 */
export function deltaGulirPanel(
  panelAtas: number,
  judulBawah: number,
  tinggiLayar: number,
  batasAtas: number,
  celah: number = CELAH_GULIR,
  bintangAtas?: number,
): number {
  const tampak = panelAtas >= batasAtas + celah && judulBawah <= tinggiLayar - celah;
  if (tampak) return 0;
  const ke = panelAtas - Math.max(batasAtas + celah, LETAK_PANEL * tinggiLayar);
  return bintangAtas === undefined ? ke : Math.min(ke, bintangAtas - (batasAtas + celah));
}
