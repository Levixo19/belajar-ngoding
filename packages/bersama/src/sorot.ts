/* Pemindai sintaks: port TypeScript dari `inti/sorot.py`.
 *
 * Ini implementasi KETIGA yang sengaja dibuat, dan satu-satunya yang boleh
 * bertahan. Yang pertama `inti/sorot.py` (dipakai server untuk menghitung
 * token materi sekali saja), yang kedua `webapp/statik/js/sorot.js` (dipakai
 * editor, yang harus menyorot ulang tiap ketikan). Keduanya diadu tes
 * diferensial di `tests/test_web.py`. Begitu sisi web jadi React, tes itu
 * kehilangan lawan tandingnya -- yang menggantikannya rekaman di
 * `packages/bersama/golden/sorot.json`, dan berkas ini WAJIB mereproduksinya.
 *
 * Tiga hal yang membedakan port ini dari `sorot.js`, dan ketiganya disengaja:
 *
 * 1. NOL rujukan ke `document`. `sorot.js` mencampur pemindai dengan penulis
 *    DOM (`keFragmen`, `praKode`, `sorotKe`), jadi mengujinya di Node butuh
 *    shim DOM. Di React token digambar sebagai JSX, bukan ditempel dengan
 *    tangan, jadi bagian itu tidak ikut ke sini.
 * 2. Tabelnya DATA di paket ini, bukan suntikan dari `/api/awal`. Pemindai
 *    yang butuh server untuk tahu kata kuncinya tidak bisa diuji sendiri.
 *    Berkasnya DIHASILKAN `alat/ekspor_bersama.py` dari `sorot.ATURAN`, jadi
 *    tetap cuma ada satu tempat kata kunci dituliskan.
 * 3. `namaPenyorot()` ikut di sini. `sorot.js` tidak punya padanannya karena
 *    server selalu menerjemahkan nama bahasa lebih dulu
 *    (`inti/berkas.py:sorot_untuk`). Sisi klien yang menyorot kode dari medan
 *    `"bahasa"` sebuah materi butuh terjemahan yang SAMA; menuliskannya ulang
 *    berarti tabel kedua, dan satu-satunya gejalanya ratusan blok kode yang
 *    warnanya berbeda dari yang digambar server.
 */

// Atribut `with { type: "json" }` wajib: tanpa itu Node menolak impor JSON di
// modul ESM, dan yang terbaca bukan "tambahkan atributnya" melainkan
// "ERR_IMPORT_ATTRIBUTE_MISSING" di tengah tumpukan yang tidak menyebut
// berkas ini. Vite dan `tsc` keduanya menerimanya.
import tabel from "../data/aturan-sorot.json" with { type: "json" };

/** Jenis token. Sama persis dengan yang dipakai `inti/sorot.py`. */
export type JenisToken =
  | "teks"
  | "komentar"
  | "string"
  | "angka"
  | "kunci"
  | "tipe"
  | "bawaan"
  | "fungsi"
  | "operator"
  | "khusus";

/** Satu token: [jenis, teks]. Gabungan seluruh `teks` = kode aslinya. */
export type Token = [JenisToken, string];

/** Bentuk satu aturan seperti yang tersimpan di `aturan-sorot.json`. */
interface AturanMentah {
  komentar_baris: string[];
  komentar_blok: string[][];
  kutip: string[];
  kutip_mentah: string[];
  escape: boolean;
  kunci: string[];
  tipe: string[];
  bawaan: string[];
  praprosesor: boolean;
  variabel_dolar: boolean;
  tanpa_bedakan_kapital: boolean;
  pemisah_kunci: string[];
}

/** Aturan siap pakai: daftar kata jadi `Set` supaya pencariannya O(1). */
interface Aturan {
  komentarBaris: string[];
  komentarBlok: Array<[string, string]>;
  /** Diurutkan dari yang TERPANJANG. Urutannya bagian dari algoritma. */
  kutip: string[];
  kutipMentah: Set<string>;
  escape: boolean;
  kunci: Set<string>;
  tipe: Set<string>;
  bawaan: Set<string>;
  praprosesor: boolean;
  variabelDolar: boolean;
  tanpaBedakanKapital: boolean;
  /** Pemisah yang menandai KUNCI di awal baris (`:` YAML/HTTP, `=` ini/TOML/HCL). */
  pemisahKunci: string[];
}

const HURUF_AWAL = /[A-Za-z_]/;
const HURUF_LANJUT = /[A-Za-z0-9_]/;
const ANGKA = /[0-9]/;
const OPERATOR = new Set("+-*/%=<>!&|^~?:;,.()[]{}@");
// Kunci di awal baris boleh memuat tanda hubung, titik, dan garis miring.
const KUNCI_LANJUT = /[A-Za-z0-9_.\-/]/;

const MENTAH = tabel.aturan as unknown as Record<string, AturanMentah>;
const ALIAS = tabel.alias as Record<string, string>;
const PEMETAAN = tabel.pemetaan as Record<string, string>;

/* Aturan dibangun sekali per nama kanonik, saat pertama diminta. Membangun
 * ke-19-nya di awal berarti 19 kali tiga `Set` dari daftar kata untuk sebuah
 * halaman yang mungkin cuma memuat Python. */
const tersimpan = new Map<string, Aturan>();

function siapkan(m: AturanMentah): Aturan {
  return {
    komentarBaris: m.komentar_baris,
    komentarBlok: m.komentar_blok.map((p) => [p[0], p[1]] as [string, string]),
    kutip: m.kutip,
    kutipMentah: new Set(m.kutip_mentah),
    escape: m.escape,
    kunci: new Set(m.kunci),
    tipe: new Set(m.tipe),
    bawaan: new Set(m.bawaan),
    praprosesor: m.praprosesor,
    variabelDolar: m.variabel_dolar,
    tanpaBedakanKapital: m.tanpa_bedakan_kapital,
    pemisahKunci: m.pemisah_kunci,
  };
}

/* Bahasa tak dikenal tetap tampil UTUH, cuma tanpa warna -- sama seperti
 * `sorot._POLOS` di Python. Pemindai ini tidak pernah boleh gagal: kode yang
 * hilang dari layar jauh lebih buruk daripada kode yang tidak berwarna. */
const POLOS: Aturan = siapkan({
  komentar_baris: [],
  komentar_blok: [],
  kutip: ['"', "'"],
  kutip_mentah: [],
  escape: true,
  kunci: [],
  tipe: [],
  bawaan: [],
  praprosesor: false,
  variabel_dolar: false,
  tanpa_bedakan_kapital: false,
  pemisah_kunci: [],
});

/**
 * Nama bahasa di medan `"bahasa"` sebuah materi -> nama aturan penyorot.
 *
 * Padanan `inti/berkas.py:sorot_untuk`. Tanpa ini, `"terminal"` (194 blok),
 * `"jsx"` (25) dan `"postgresql"` (25) tampil polos di klien sementara server
 * menggambarnya sebagai bash, javascript, dan sql.
 */
export function namaPenyorot(bahasa: string): string {
  const nama = String(bahasa || "").toLowerCase();
  return PEMETAAN[nama] ?? nama;
}

function aturanUntuk(bahasa: string): Aturan {
  const nama = String(bahasa || "").toLowerCase();
  const kanonik = ALIAS[nama] ?? nama;
  const sudah = tersimpan.get(kanonik);
  if (sudah) return sudah;
  const m = MENTAH[kanonik];
  if (!m) return POLOS;
  const siap = siapkan(m);
  tersimpan.set(kanonik, siap);
  return siap;
}

/** Apakah bahasa ini punya aturan sendiri, atau akan tampil polos. */
export function bahasaDikenal(bahasa: string): boolean {
  const nama = String(bahasa || "").toLowerCase();
  return Boolean(MENTAH[ALIAS[nama] ?? nama]);
}

/** Semua nama bahasa yang dikenali, alias ikut. */
export function bahasaDidukung(): string[] {
  return [...Object.keys(MENTAH), ...Object.keys(ALIAS)].sort();
}

/* --------------------------------------------------------------- pemindai */

function akhirString(
  kode: string,
  i: number,
  pembuka: string,
  aturan: Aturan,
): number {
  const mentah = aturan.kutipMentah.has(pembuka) || !aturan.escape;
  let j = i + pembuka.length;
  const n = kode.length;
  // Kutip tunggal biasa tidak boleh melintasi baris; kutip tiga dan kutip
  // terbalik boleh.
  const satuBaris = pembuka.length === 1 && pembuka !== "`";

  while (j < n) {
    const c = kode.charAt(j);
    if (!mentah && c === "\\") {
      j += 2;
      continue;
    }
    if (kode.startsWith(pembuka, j)) return j + pembuka.length;
    if (satuBaris && c === "\n") return j;
    j += 1;
  }
  return n;
}

function akhirAngka(kode: string, i: number): number {
  const n = kode.length;
  let j = i;
  if (kode.charAt(j) === "0" && j + 1 < n && "xXbBoO".includes(kode.charAt(j + 1))) {
    j += 2;
    while (j < n && HURUF_LANJUT.test(kode.charAt(j))) j += 1;
    return j;
  }
  let lihatTitik = false;
  while (j < n) {
    const c = kode.charAt(j);
    if (ANGKA.test(c) || c === "_") {
      j += 1;
    } else if (c === "." && !lihatTitik && j + 1 < n && ANGKA.test(kode.charAt(j + 1))) {
      lihatTitik = true;
      j += 1;
    } else if (
      "eE".includes(c) &&
      j + 1 < n &&
      (ANGKA.test(kode.charAt(j + 1)) || "+-".includes(kode.charAt(j + 1)))
    ) {
      j += 2;
    } else if ("fFlLdDuU".includes(c)) {
      // sufiks literal C/Java
      j += 1;
    } else {
      break;
    }
  }
  return j;
}

function diAwalBaris(kode: string, i: number): boolean {
  let j = i - 1;
  while (j >= 0 && (kode.charAt(j) === " " || kode.charAt(j) === "\t")) j -= 1;
  return j < 0 || kode.charAt(j) === "\n";
}

/** Index sesudah KUNCI yang dimulai di `i`, atau 0 kalau bukan kunci.
 *  Padanan `_akhir_kunci` di sorot.py, langkah demi langkah. */
function akhirKunci(kode: string, i: number, pemisah: string[]): number {
  let j = i - 1;
  while (j >= 0 && kode.charAt(j) !== "\n") {
    const d = kode.charAt(j);
    const sesudahD = kode.charAt(j + 1);
    if (d === " " || d === "\t" || (d === "-" && (sesudahD === " " || sesudahD === "\t"))) j -= 1;
    else return 0;
  }
  const n = kode.length;
  let akhir = i + 1;
  while (akhir < n && KUNCI_LANJUT.test(kode.charAt(akhir))) akhir += 1;
  let k = akhir;
  while (k < n && (kode.charAt(k) === " " || kode.charAt(k) === "\t")) k += 1;
  if (k >= n || !pemisah.includes(kode.charAt(k))) return 0;
  const sesudah = kode.charAt(k + 1);
  if (kode.charAt(k) === ":" && sesudah !== "" && sesudah !== " " && sesudah !== "\t"
      && sesudah !== "\r" && sesudah !== "\n") return 0;
  if (kode.charAt(k) === "=" && sesudah === "=") return 0;
  return akhir;
}

/** Satukan token berdampingan yang sejenis.
 *
 *  Tanpa ini sebuah rantai pemanggilan metode menghasilkan lima token operator
 *  terpisah, masing-masing jadi satu elemen sendiri saat digambar -- hasilnya
 *  berkali lipat lebih panjang dari kodenya, padahal tampilannya sama persis.
 */
function gabung(daftar: Token[]): Token[] {
  const padat: Array<[JenisToken, string[]]> = [];
  for (const [jenis, teks] of daftar) {
    const akhir = padat[padat.length - 1];
    if (akhir && akhir[0] === jenis) akhir[1].push(teks);
    else padat.push([jenis, [teks]]);
  }
  return padat.map(([jenis, bagian]) => [jenis, bagian.join("")] as Token);
}

/**
 * Pecah kode jadi token. Gabungan seluruh `teks`-nya = `kode` apa adanya.
 *
 * Sifat itu bukan kenyamanan melainkan kontrak: hasilnya dipakai untuk
 * MENGGANTI kode di layar, jadi satu karakter yang hilang di sini berarti satu
 * karakter yang hilang dari mata pelajar, tanpa error di mana pun.
 */
export function token(kode: string, bahasa: string): Token[] {
  const aturan = aturanUntuk(bahasa);
  const hasil: Token[] = [];
  let simpanan: string[] = [];
  let i = 0;
  const n = kode.length;

  const buang = () => {
    if (simpanan.length) {
      hasil.push(["teks", simpanan.join("")]);
      simpanan = [];
    }
  };

  while (i < n) {
    const c = kode.charAt(i);

    // -- shebang -----------------------------------------------------------
    if (i === 0 && kode.startsWith("#!")) {
      let akhir = kode.indexOf("\n", i);
      if (akhir < 0) akhir = n;
      hasil.push(["komentar", kode.slice(i, akhir)]);
      i = akhir;
      continue;
    }

    // -- praprosesor C/C++ -------------------------------------------------
    if (aturan.praprosesor && c === "#" && diAwalBaris(kode, i)) {
      let akhir = kode.indexOf("\n", i);
      if (akhir < 0) akhir = n;
      buang();
      hasil.push(["khusus", kode.slice(i, akhir)]);
      i = akhir;
      continue;
    }

    // -- komentar blok -----------------------------------------------------
    const blok = aturan.komentarBlok.find((p) => kode.startsWith(p[0], i));
    if (blok) {
      const [buka, tutup] = blok;
      let akhir = kode.indexOf(tutup, i + buka.length);
      akhir = akhir < 0 ? n : akhir + tutup.length;
      buang();
      hasil.push(["komentar", kode.slice(i, akhir)]);
      i = akhir;
      continue;
    }

    // -- komentar baris ----------------------------------------------------
    if (aturan.komentarBaris.some((p) => kode.startsWith(p, i))) {
      let akhir = kode.indexOf("\n", i);
      if (akhir < 0) akhir = n;
      buang();
      hasil.push(["komentar", kode.slice(i, akhir)]);
      i = akhir;
      continue;
    }

    // -- string ------------------------------------------------------------
    const pembuka = aturan.kutip.find((q) => kode.startsWith(q, i));
    if (pembuka) {
      const akhir = akhirString(kode, i, pembuka, aturan);
      buang();
      hasil.push(["string", kode.slice(i, akhir)]);
      i = akhir;
      continue;
    }

    // -- variabel shell ----------------------------------------------------
    if (aturan.variabelDolar && c === "$") {
      let j = i + 1;
      if (j < n && kode.charAt(j) === "{") {
        const tutup = kode.indexOf("}", j);
        j = tutup < 0 ? n : tutup + 1;
      } else if (j < n && kode.charAt(j) === "(") {
        j += 1;
      } else {
        while (j < n && HURUF_LANJUT.test(kode.charAt(j))) j += 1;
        if (j === i + 1 && j < n) j += 1; // $1, $@, $?, $#
      }
      buang();
      hasil.push(["khusus", kode.slice(i, j)]);
      i = j;
      continue;
    }

    // -- angka -------------------------------------------------------------
    if (ANGKA.test(c)) {
      const akhir = akhirAngka(kode, i);
      buang();
      hasil.push(["angka", kode.slice(i, akhir)]);
      i = akhir;
      continue;
    }

    // -- kunci di awal baris -----------------------------------------------
    if (aturan.pemisahKunci.length > 0 && HURUF_AWAL.test(c)) {
      const akhir = akhirKunci(kode, i, aturan.pemisahKunci);
      if (akhir) {
        buang();
        hasil.push(["kunci", kode.slice(i, akhir)]);
        i = akhir;
        continue;
      }
    }

    // -- pengenal ----------------------------------------------------------
    if (HURUF_AWAL.test(c)) {
      let j = i + 1;
      while (j < n && HURUF_LANJUT.test(kode.charAt(j))) j += 1;
      const kata = kode.slice(i, j);
      const banding = aturan.tanpaBedakanKapital ? kata.toUpperCase() : kata;

      let jenis: JenisToken;
      if (aturan.kunci.has(banding)) jenis = "kunci";
      else if (aturan.tipe.has(banding)) jenis = "tipe";
      else if (aturan.bawaan.has(banding)) jenis = "bawaan";
      else {
        let k = j;
        while (k < n && (kode.charAt(k) === " " || kode.charAt(k) === "\t")) k += 1;
        jenis = k < n && kode.charAt(k) === "(" ? "fungsi" : "teks";
      }

      if (jenis === "teks") {
        simpanan.push(kata);
      } else {
        buang();
        hasil.push([jenis, kata]);
      }
      i = j;
      continue;
    }

    // -- operator & sisanya ------------------------------------------------
    if (OPERATOR.has(c)) {
      buang();
      hasil.push(["operator", c]);
      i += 1;
      continue;
    }

    simpanan.push(c);
    i += 1;
  }

  buang();
  return gabung(hasil);
}
