/* Menjelaskan kenapa keluaran pelajar berbeda. Port dari `inti/beda.py`.
 *
 * Yang TIDAK ikut diport: `render()` dan `_potong()`. Keduanya menggambar diff
 * berdampingan untuk terminal 76 kolom beserta kode warna ANSI, dan antarmuka
 * terminal sudah dibuang. React menggambar `Beda` sendiri sebagai elemen, jadi
 * memport `render` berarti memindahkan penulis teks yang tidak akan pernah
 * dipanggil -- dan kode yang tidak dipanggil adalah kode yang diam-diam salah.
 *
 * `tampakkan()` IKUT, meski terdengar seperti tampilan: ia yang mengubah spasi
 * jadi titik tengah saat dua baris terlihat identik padahal tidak, dan tanpa
 * itu umpan baliknya berbunyi "baris 3 berbeda" di atas dua baris yang bagi
 * mata pelajar sama persis.
 */

/** Karakter pengganti untuk hal yang tak terlihat. */
export const SPASI_TAMPAK = "·";
export const TAB_TAMPAK = "→";

/** Tanda penyejajaran satu baris: sama, berubah, kurang, atau berlebih. */
export type Tanda = "=" | "~" | "-" | "+";

/** Satu baris hasil penyejajaran: [tanda, teks harapan, teks aktual]. */
export type BarisBeda = [Tanda, string | null, string | null];

/** Hasil perbandingan satu keluaran harapan dengan satu keluaran nyata. */
export interface Beda {
  sama: boolean;
  harapan: string[];
  aktual: string[];
  baris: BarisBeda[];
  /** Nomor baris 1-basis, `null` kalau sama. */
  nomorBeda: number | null;
  /** Kolom 1-basis pada baris itu, `null` kalau bukan soal kolom. */
  kolomBeda: number | null;
  /** Diagnosis berbahasa manusia. Kosong kalau tidak ada yang cocok. */
  catatan: string[];
}

/* --------------------------------------------- penyejajar ala SequenceMatcher
 *
 * Port `difflib.SequenceMatcher(autojunk=False).get_opcodes()`.
 *
 * Kenapa diport dan bukan diganti pustaka npm. `SequenceMatcher` BUKAN Myers
 * diff seperti `diff` atau `fast-diff`: ia Ratcliff/Obershelp -- cari blok
 * cocok TERPANJANG, lalu rekursi ke kiri dan kanannya. Untuk dua keluaran yang
 * bedanya satu baris di tengah keduanya setuju; untuk baris yang berpindah
 * tempat penyejajarannya berbeda, dan yang pelajar lihat bukan "diff-nya lain"
 * melainkan penjelasan yang menunjuk baris yang salah.
 *
 * `autojunk=False` penting: dengan bawaannya, elemen yang muncul di lebih dari
 * 1% baris b dianggap "sampah" dan dilewati -- pada keluaran panjang yang
 * banyak baris kosongnya, itu membuang justru baris yang menandai strukturnya.
 */

type Blok = [number, number, number]; // [i di a, j di b, panjang]
type Opcode = [string, number, number, number, number];

function petaIndeks(b: string[]): Map<string, number[]> {
  const b2j = new Map<string, number[]>();
  b.forEach((nilai, j) => {
    const ada = b2j.get(nilai);
    if (ada) ada.push(j);
    else b2j.set(nilai, [j]);
  });
  return b2j;
}

function blokTerpanjang(
  a: string[],
  b: string[],
  b2j: Map<string, number[]>,
  alo: number,
  ahi: number,
  blo: number,
  bhi: number,
): Blok {
  let besti = alo;
  let bestj = blo;
  let bestsize = 0;
  let j2len = new Map<number, number>();

  for (let i = alo; i < ahi; i += 1) {
    const baruJ2len = new Map<number, number>();
    for (const j of b2j.get(a[i] as string) ?? []) {
      if (j < blo) continue;
      if (j >= bhi) break;
      const k = (j2len.get(j - 1) ?? 0) + 1;
      baruJ2len.set(j, k);
      if (k > bestsize) {
        besti = i - k + 1;
        bestj = j - k + 1;
        bestsize = k;
      }
    }
    j2len = baruJ2len;
  }

  /* CPython punya DUA loop perluasan di sini, satu ke belakang dan satu ke
   * depan, keduanya di balik `not isbjunk(...)`. Keduanya SENGAJA TIDAK
   * diport, dan itu bukan penyederhanaan.
   *
   * Gunanya melebarkan blok melewati elemen yang ditandai "sampah". Dengan
   * `isjunk=None` dan `autojunk=False` tidak ada yang ditandai sampah, jadi
   * `b2j` memuat semua elemen -- dan DP `j2len` di atas sudah menghitung
   * panjang run cocok yang berakhir di SETIAP `(i, j)`. Maksimumnya karena itu
   * sudah blok cocok terpanjang; tidak ada sisa yang bisa diperluas.
   *
   * Diukur, bukan ditalar: dengan kedua loop dicabut, `uji/golden-beda.ts`
   * tetap cocok untuk ke-309 pasangannya. Menyalinnya ke sini berarti
   * menyimpan belasan baris yang tidak bisa dibuat merah oleh tes apa pun,
   * dan baris yang tidak bisa diuji adalah baris yang diam-diam salah.
   *
   * Yang membatalkan alasan ini cuma satu: menyalakan junk (`isjunk` atau
   * `autojunk=True`) di `inti/beda.py`. Kalau itu terjadi, kedua loop WAJIB
   * ikut diport, karena saat itu barulah ia berefek. */
  return [besti, bestj, bestsize];
}

function blokCocok(a: string[], b: string[]): Blok[] {
  const b2j = petaIndeks(b);
  const la = a.length;
  const lb = b.length;
  const antre: Array<[number, number, number, number]> = [[0, la, 0, lb]];
  const blok: Blok[] = [];

  while (antre.length) {
    const [alo, ahi, blo, bhi] = antre.pop() as [number, number, number, number];
    const [i, j, k] = blokTerpanjang(a, b, b2j, alo, ahi, blo, bhi);
    if (k) {
      blok.push([i, j, k]);
      if (alo < i && blo < j) antre.push([alo, i, blo, j]);
      if (i + k < ahi && j + k < bhi) antre.push([i + k, ahi, j + k, bhi]);
    }
  }

  // `list.sort()` Python mengurutkan tuple leksikografis per elemen.
  blok.sort((p, q) => p[0] - q[0] || p[1] - q[1] || p[2] - q[2]);

  // Satukan blok yang sebenarnya bersebelahan.
  let i1 = 0;
  let j1 = 0;
  let k1 = 0;
  const rapat: Blok[] = [];
  for (const [i2, j2, k2] of blok) {
    if (i1 + k1 === i2 && j1 + k1 === j2) {
      k1 += k2;
    } else {
      if (k1) rapat.push([i1, j1, k1]);
      i1 = i2;
      j1 = j2;
      k1 = k2;
    }
  }
  if (k1) rapat.push([i1, j1, k1]);
  rapat.push([la, lb, 0]);
  return rapat;
}

function opcodes(a: string[], b: string[]): Opcode[] {
  let i = 0;
  let j = 0;
  const jawab: Opcode[] = [];
  for (const [ai, bj, ukuran] of blokCocok(a, b)) {
    let tag = "";
    if (i < ai && j < bj) tag = "replace";
    else if (i < ai) tag = "delete";
    else if (j < bj) tag = "insert";
    if (tag) jawab.push([tag, i, ai, j, bj]);
    i = ai + ukuran;
    j = bj + ukuran;
    if (ukuran) jawab.push(["equal", ai, i, bj, j]);
  }
  return jawab;
}

/* ------------------------------------------------------------------ bantuan */

/**
 * Pecah jadi baris, samakan akhiran, buang baris kosong di ujung.
 *
 * Harus sepadan dengan `runner.normalisasi`: kalau modul ini menganggap dua
 * keluaran berbeda padahal penilai menganggapnya sama, pelajar akan melihat
 * "GAGAL" berdampingan dengan diff yang bilang "sudah sama".
 */
export function pecahBaris(teks: string | null | undefined): string[] {
  const rapi = (teks ?? "").replace(/\r\n/g, "\n").replace(/\r/g, "\n");
  // `str.rstrip()` Python membuang SEMUA spasi-putih di ujung, termasuk tab dan
  // form feed -- bukan cuma spasi. `\s` di JS mencakup itu plus beberapa spasi
  // Unicode yang `rstrip` juga buang, jadi keduanya sepadan untuk keluaran
  // program.
  const baris = rapi.split("\n").map((b) => b.replace(/\s+$/, ""));
  while (baris.length && !baris[baris.length - 1]) baris.pop();
  while (baris.length && !baris[0]) baris.shift();
  return baris;
}

function rapatkan(s: string): string {
  return s.replace(/\s+/g, " ").trim();
}

function angka(s: string): string[] {
  return s.match(/-?\d+(?:[.,]\d+)?/g) ?? [];
}

/** Kolom 1-basis pertama yang berbeda antara dua baris. `null` kalau sama. */
export function kolomPertamaBeda(a: string, b: string): number | null {
  const batas = Math.min(a.length, b.length);
  for (let i = 0; i < batas; i += 1) {
    if (a[i] !== b[i]) return i + 1;
  }
  if (a.length !== b.length) return batas + 1;
  return null;
}

/**
 * Ganti spasi & tab jadi karakter kasatmata.
 *
 * Hanya dipakai kalau dua baris terlihat sama tapi sebenarnya beda, supaya
 * pelajar bisa melihat spasi ganda atau tab yang tersembunyi.
 */
export function tampakkan(teks: string): string {
  return teks.split("\t").join(TAB_TAMPAK).split(" ").join(SPASI_TAMPAK);
}

/* ----------------------------------------------------------------- diagnosa */

/* `str.rstrip("0").rstrip(".")` Python membuang SEKUMPULAN karakter dari
 * ujung, bukan sebuah akhiran. Tidak ada padanannya di JS, dan `replace`
 * dengan regex `/0+$/` kebetulan sama untuk kasus ini -- tapi cuma kebetulan,
 * jadi ditulis eksplisit supaya tidak ada yang "merapikannya" nanti. */
function buangNolDesimal(x: string): string {
  let s = x.replace(/,/g, ".");
  let akhir = s.length;
  while (akhir > 0 && s[akhir - 1] === "0") akhir -= 1;
  s = s.slice(0, akhir);
  akhir = s.length;
  while (akhir > 0 && s[akhir - 1] === ".") akhir -= 1;
  return s.slice(0, akhir);
}

/* Python membandingkan string per CODE POINT; `<` di JS membandingkan per unit
 * UTF-16. Keduanya sepakat untuk seluruh BMP, dan keluaran program di
 * kurikulum ini tidak pernah memuat karakter di luar itu. Kalau suatu hari
 * ada, urutannya bisa berbeda -- dan gejalanya cuma kalimat "URUTANNYA
 * tertukar" yang muncul atau hilang, bukan error. */
function samaSetelahDiurut(h: string[], a: string[]): boolean {
  if (h.length !== a.length) return false;
  const uh = [...h].sort();
  const ua = [...a].sort();
  return uh.every((v, i) => v === ua[i]);
}

function sama(h: string[], a: string[]): boolean {
  return h.length === a.length && h.every((v, i) => v === a[i]);
}

/** Tebak kenapa keluaran berbeda. Daftar kalimat penjelas, boleh kosong. */
function diagnosa(h: string[], a: string[]): string[] {
  const catatan: string[] = [];

  if (!a.length) {
    catatan.push("Programmu tidak mencetak apa pun. Sudah pakai perintah cetak?");
    return catatan;
  }
  if (sama(h, a)) return catatan;

  const gabungH = h.join("\n");
  const gabungA = a.join("\n");

  if (gabungH.toLowerCase() === gabungA.toLowerCase()) {
    catatan.push("Isinya sudah benar, hanya beda HURUF BESAR/KECIL.");
    return catatan;
  }
  if (rapatkan(gabungH) === rapatkan(gabungA)) {
    catatan.push("Isinya sudah benar, hanya beda JUMLAH SPASI atau indentasi.");
    return catatan;
  }
  if (rapatkan(gabungH).toLowerCase() === rapatkan(gabungA).toLowerCase()) {
    catatan.push("Isinya sudah benar, hanya beda spasi dan huruf besar/kecil.");
    return catatan;
  }
  if (samaSetelahDiurut(h, a) && !sama(h, a)) {
    catatan.push("Semua barisnya benar, tapi URUTANNYA tertukar.");
    return catatan;
  }

  if (a.length > h.length && h.every((b) => a.includes(b))) {
    catatan.push(
      `Semua baris yang diminta sudah ada, tapi ada ${a.length - h.length} ` +
        "baris TAMBAHAN yang tidak diminta.",
    );
  }

  const hilang = h.filter((b) => !a.includes(b));
  if (hilang.length && hilang.length < h.length) {
    catatan.push(
      `${hilang.length} baris belum tercetak, mulai dari: ` +
        `${kutipPython((hilang[0] as string).slice(0, 48))}`,
    );
  }

  // Pelajar mencetak teks ajakan sebelum jawabannya.
  const batas = Math.min(h.length, a.length);
  for (let i = 0; i < batas; i += 1) {
    const bh = h[i] as string;
    const ba = a[i] as string;
    if (bh && ba.endsWith(bh) && ba.length > bh.length) {
      const awalan = ba.slice(0, ba.length - bh.length);
      if (awalan.trim()) {
        catatan.push(
          `Sepertinya kamu ikut mencetak teks ajakan ` +
            `${kutipPython(awalan.trim().slice(0, 32))} sebelum jawabannya. ` +
            "Latihan ini dinilai dari output, jadi jangan cetak prompt apa pun.",
        );
        break;
      }
    }
  }

  const angkaH = angka(gabungH);
  const angkaA = angka(gabungA);
  const daftarSama = (x: string[], y: string[]) =>
    x.length === y.length && x.every((v, i) => v === y[i]);

  if (angkaH.length && daftarSama(angkaH, angkaA)) {
    catatan.push("Semua ANGKANYA sudah benar; yang beda cuma teks di sekitarnya.");
  } else {
    const rapiH = angkaH.map(buangNolDesimal);
    const rapiA = angkaA.map(buangNolDesimal);
    if (rapiH.length && daftarSama(rapiH, rapiA)) {
      catatan.push(
        "Nilainya sudah benar, yang beda FORMAT desimalnya " +
          "(misal 3 vs 3.0). Perhatikan tipe data pembagiannya.",
      );
    }
  }

  if (!catatan.length) {
    const tanpaBaca = (b: string) => b.replace(/[.!?,;:]+$/, "");
    const tbH = h.map(tanpaBaca);
    const tbA = a.map(tanpaBaca);
    if (daftarSama(tbH, tbA)) {
      catatan.push("Hanya beda TANDA BACA di akhir baris.");
    } else if (
      daftarSama(
        tbH.map((b) => b.toLowerCase()),
        tbA.map((b) => b.toLowerCase()),
      )
    ) {
      catatan.push(
        "Isinya sudah benar, yang beda cuma huruf besar/kecil " +
          "dan tanda baca di akhir baris.",
      );
    }
  }

  if (!catatan.length) {
    if (a.length < h.length) {
      catatan.push(
        `Outputmu ${h.length - a.length} baris lebih pendek dari yang diminta.`,
      );
    } else if (a.length > h.length) {
      catatan.push(
        `Outputmu ${a.length - h.length} baris lebih panjang dari yang diminta.`,
      );
    }
  }

  return catatan;
}

/* `{!r}` Python pada sebuah str memilih kutip tunggal, dan baru memakai kutip
 * ganda kalau teksnya memuat kutip tunggal tapi tidak memuat kutip ganda.
 * Dua kalimat diagnosis memakainya, dan kalimat yang kutipnya berbeda dari
 * yang digambar server adalah kalimat yang sama-sama benar tapi tidak bisa
 * diadu -- jadi aturannya ditiru, bukan diperkirakan. */
function kutipPython(s: string): string {
  const lolos = s
    .replace(/\\/g, "\\\\")
    .replace(/\n/g, "\\n")
    .replace(/\r/g, "\\r")
    .replace(/\t/g, "\\t");
  if (lolos.includes("'") && !lolos.includes('"')) return `"${lolos}"`;
  return `'${lolos.replace(/'/g, "\\'")}'`;
}

/* ---------------------------------------------------------------- pembanding */

/** Sejajarkan dua keluaran dan jelaskan bedanya. Selalu mengembalikan `Beda`. */
export function bandingkan(
  harapan: string | null | undefined,
  aktual: string | null | undefined,
): Beda {
  const h = pecahBaris(harapan);
  const a = pecahBaris(aktual);

  const baris: BarisBeda[] = [];
  let nomorBeda: number | null = null;
  let kolomBeda: number | null = null;
  let nomor = 0;

  for (const [tag, h1, h2, a1, a2] of opcodes(h, a)) {
    if (tag === "equal") {
      for (let o = 0; o < h2 - h1; o += 1) {
        nomor += 1;
        baris.push(["=", h[h1 + o] as string, a[a1 + o] as string]);
      }
    } else if (tag === "replace") {
      // Sejajarkan berpasangan supaya kolom bedanya bisa ditunjuk.
      const panjang = Math.max(h2 - h1, a2 - a1);
      for (let o = 0; o < panjang; o += 1) {
        nomor += 1;
        const bh = h1 + o < h2 ? (h[h1 + o] as string) : null;
        const ba = a1 + o < a2 ? (a[a1 + o] as string) : null;
        if (bh !== null && ba !== null) {
          baris.push(["~", bh, ba]);
          if (nomorBeda === null) {
            nomorBeda = nomor;
            kolomBeda = kolomPertamaBeda(bh, ba);
          }
        } else if (bh !== null) {
          baris.push(["-", bh, null]);
          if (nomorBeda === null) {
            nomorBeda = nomor;
            kolomBeda = null;
          }
        } else {
          baris.push(["+", null, ba]);
          if (nomorBeda === null) {
            nomorBeda = nomor;
            kolomBeda = null;
          }
        }
      }
    } else if (tag === "delete") {
      for (let o = 0; o < h2 - h1; o += 1) {
        nomor += 1;
        baris.push(["-", h[h1 + o] as string, null]);
        if (nomorBeda === null) {
          nomorBeda = nomor;
          kolomBeda = null;
        }
      }
    } else if (tag === "insert") {
      for (let o = 0; o < a2 - a1; o += 1) {
        nomor += 1;
        baris.push(["+", null, a[a1 + o] as string]);
        if (nomorBeda === null) {
          nomorBeda = nomor;
          kolomBeda = null;
        }
      }
    }
  }

  return {
    sama: sama(h, a),
    harapan: h,
    aktual: a,
    baris,
    nomorBeda,
    kolomBeda,
    catatan: diagnosa(h, a),
  };
}

/* Diagnosis yang berarti "isinya sudah benar, tinggal bentuknya". Layar latihan
 * memakainya untuk berkata "Hampir" alih-alih vonis gagal berwarna merah: kalau
 * kemajuan sebagian tidak terlihat, mencoba lagi terasa seperti mulai dari nol. */
const AWALAN_NYARIS = [
  "Isinya sudah benar",
  "Semua barisnya benar",
  "Semua ANGKANYA",
  "Nilainya sudah benar",
  "Hanya beda TANDA BACA",
  "Semua baris yang diminta sudah ada",
];

/** True kalau keluaran pelajar hampir benar menurut diagnosis di atas. */
export function nyaris(beda: Beda): boolean {
  return beda.catatan.some((c) => AWALAN_NYARIS.some((p) => c.startsWith(p)));
}

/** Satu kalimat rangkuman, untuk daftar hasil uji. */
export function ringkas(beda: Beda): string {
  if (beda.sama) return "output sama persis";
  if (beda.catatan.length) return beda.catatan[0] as string;
  if (beda.nomorBeda) {
    const kolom = beda.kolomBeda ? ` kolom ${beda.kolomBeda}` : "";
    return `beda mulai baris ${beda.nomorBeda}${kolom}`;
  }
  return "output berbeda";
}
