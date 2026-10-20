/* Bagian MURNI editor: warna kurung, pemandu indentasi, letak pita baris aktif.
 *
 * Port `pisahKurung`, `pisahInden`, dan `posisiPita` dari
 * `webapp/statik/js/editor.js`. Ketiganya tanpa DOM, dan itu yang membuat
 * keduanya bisa diadu dari Node tanpa peramban -- `TestPitaBarisAktif` dan
 * `test_invarian_slot_tiga_atas_korpus` di `tests/test_web.py` memagari versi
 * JS-nya; port ini mengikuti kontrak yang sama.
 *
 * SATU syarat yang mengikat keduanya, dan ia bukan soal warna: **GABUNGAN
 * seluruh `teks` keluaran WAJIB identik byte-per-byte dengan gabungan
 * masukannya.** Lapisan sorot ini duduk persis di bawah textarea yang
 * transparan, jadi satu karakter selisih membuat kursor mendarat di huruf yang
 * salah pada baris panjang -- tanpa satu pun error di mana pun.
 */

import type { Token } from "../../../bersama/src/sorot.ts";

/** Pasangan yang ditutup otomatis editor. */
export const PASANGAN: Record<string, string> = {
  "(": ")",
  "[": "]",
  "{": "}",
  '"': '"',
  "'": "'",
  "`": "`",
};

/** Indentasi: 4 spasi, konsisten dengan kurikulum. */
export const INDENT = "    ";

/** Penanda komentar per bahasa, untuk Ctrl+/. */
export const KOMENTAR: Record<string, string> = {
  python: "# ",
  bash: "# ",
  fedora: "# ",
  git: "# ",
  ruby: "# ",
  sql: "-- ",
  html: "<!-- ",
  css: "/* ",
  java: "// ",
  javascript: "// ",
  typescript: "// ",
  c: "// ",
  cpp: "// ",
  csharp: "// ",
  go: "// ",
  rust: "// ",
  kotlin: "// ",
  php: "// ",
  vb: "' ",
};

/* Kurung = entri `PASANGAN` yang pembuka dan penutupnya BERBEDA.
 *
 * Tiga entri lain (`"`, `'`, backtick) menutup DIRINYA SENDIRI, jadi mereka
 * tidak punya kedalaman: tidak ada cara membedakan yang membuka dari yang
 * menutup tanpa menghitung string -- dan menghitung string justru yang
 * dilarang di `pisahKurung`. Menurunkan daftarnya dari `PASANGAN` alih-alih
 * menuliskannya ulang berarti kurung yang ditutup sendiri oleh editor dan
 * kurung yang diwarnai di sini mustahil berbeda pendapat. */
const TUTUP_DARI: Record<string, string> = {};
const BUKA_DARI: Record<string, string> = {};
for (const pembuka of Object.keys(PASANGAN)) {
  const tutup = PASANGAN[pembuka] as string;
  if (tutup === pembuka) continue;
  TUTUP_DARI[pembuka] = tutup;
  BUKA_DARI[tutup] = pembuka;
}

/* Empat warna sudah cukup jauh untuk mata; kedalaman kelima memakai warna
 * pertama lagi, dan pada kedalaman itu yang menolong memang bukan warna
 * kelima melainkan indentasinya. */
const WARNA_KURUNG = 4;

/** Penanda kurung yatim: penutup tanpa pembuka, atau yang jenisnya tak cocok. */
export const YATIM = "yatim";

/** `[jenis, teks, warna]`. `warna`: `null`, `0..3`, atau `"yatim"`. */
export type Potongan = [string, string, number | string | null];

/**
 * Pecah token kurung jadi potongan yang membawa kedalamannya.
 *
 * Tiga sifat yang mengikat:
 *
 * 1. HANYA jenis `operator` yang dihitung. Di kurikulum ini ada 2.270 kurung
 *    di dalam token `string`, 981 di `komentar`, dan 83 di `khusus`; satu `(`
 *    di dalam komentar yang ikut dihitung meracuni kedalaman SELURUH kode
 *    sesudahnya, dan yang terlihat pelajar cuma warna yang terasa acak.
 * 2. Pasangannya dihitung per jenis: `]` tidak menutup `(`. Ia yatim, dan
 *    `(`-nya tetap terbuka, karena itulah yang sebenarnya terjadi pada
 *    kodenya.
 * 3. Kedalaman tidak pernah negatif -- tumpukan cuma dipangkas kalau
 *    puncaknya memang pembuka yang cocok.
 *
 * Span `operator` DIBELAH alih-alih diwarnai utuh: dari 40.287 token operator
 * ber-kurung di kurikulum ini, 9.045 rengket dengan karakter lain -- `):` di
 * ujung sebuah definisi fungsi salah satunya, dan mewarnainya utuh berarti
 * ikut mewarnai titik duanya.
 */
export function pisahKurung(daftar: Token[] | null | undefined): Potongan[] {
  const hasil: Potongan[] = [];
  const tumpukan: string[] = [];
  for (const [jenis, teks] of daftar ?? []) {
    if (jenis !== "operator") {
      hasil.push([jenis, teks, null]);
      continue;
    }

    let mulai = 0;
    for (let i = 0; i < teks.length; i++) {
      const c = teks.charAt(i);
      const buka = TUTUP_DARI[c] !== undefined;
      const tutup = BUKA_DARI[c] !== undefined;
      if (!buka && !tutup) continue;

      // Apa pun di antara dua kurung tetap satu potongan `operator` biasa.
      if (i > mulai) hasil.push([jenis, teks.slice(mulai, i), null]);
      mulai = i + 1;

      if (buka) {
        // Pembuka membaca tinggi tumpukan SEBELUM push, penutup membacanya
        // SESUDAH pop. Angka pasangan keluar sendiri dari urutan itu.
        hasil.push([jenis, c, tumpukan.length % WARNA_KURUNG]);
        tumpukan.push(c);
      } else if (tumpukan[tumpukan.length - 1] === BUKA_DARI[c]) {
        tumpukan.pop();
        hasil.push([jenis, c, tumpukan.length % WARNA_KURUNG]);
      } else {
        hasil.push([jenis, c, YATIM]);
      }
    }
    // Ekor sesudah kurung terakhir. Token tanpa kurung sama sekali lewat di
    // sini utuh, satu potongan.
    if (mulai < teks.length) hasil.push([jenis, teks.slice(mulai), null]);
  }
  return hasil;
}

/**
 * Belah deretan spasi pembuka baris jadi potongan ber-jenis `indentasi`.
 *
 * Tiga hal yang TIDAK dikerjakannya, dan ketiganya putusan:
 *
 * 1. Ia tidak tahu apa pun soal lebar, satuan `ch`, atau angka 4. Geometri
 *    tinggal di SATU tempat, dan tempat itu aturan `.tk-indentasi` di
 *    `gaya.css` -- yang sama yang sudah memegang `tab-size` dan `line-height`.
 * 2. Baris yang dibuka TAB tidak dibelah sama sekali. Lebar sebuah tab
 *    ditentukan `tab-size`, bukan jumlah karakternya, jadi pemandu yang
 *    digambar per karakter mendarat di kolom yang bukan tempat tingkatnya
 *    mulai -- penanda yang salah, bukan penanda yang kurang.
 * 3. Deret spasi yang MENGAKHIRI barisnya bukan indentasi: kalau sesudahnya
 *    cuma `\n` atau habis, ia sisa baris kosong dan tidak menandai kedalaman
 *    apa pun. Korpus kurikulum tidak punya satu pun baris seperti itu, tapi
 *    yang digambar editor ini teks PELAJAR, yang bisa memuatnya.
 */
export function pisahInden(daftar: Potongan[] | null | undefined): Potongan[] {
  // Dihitung atas teks GABUNGAN, bukan per potongan, supaya satu deret yang
  // telanjur terpotong dua token tetap terbaca sebagai satu deret. Lookahead
  // `[^ \n]`-lah yang menolak spasi sisa di baris kosong (butir 3 di atas).
  const utuh = (daftar ?? []).map((p) => p[1]).join("");
  const deret: Array<[number, number]> = [];
  const pola = /(^|\n)( +)(?=[^ \n])/g;
  for (let m: RegExpExecArray | null; (m = pola.exec(utuh)) !== null; ) {
    const mulai = m.index + (m[1] as string).length;
    deret.push([mulai, mulai + (m[2] as string).length]);
  }

  const hasil: Potongan[] = [];
  let ke = 0; // deret pertama yang belum terlewati
  let pos = 0; // offset potongan ini di dalam `utuh`
  for (const [jenis, teks, warnaMentah] of daftar ?? []) {
    const warna = warnaMentah === undefined ? null : warnaMentah;
    // Potongan berteks kosong DITERUSKAN, bukan dibuang: susun-ulang memang
    // tetap identik tanpanya, tapi penggambarnya memasangkan potongan ke-i
    // dengan simpul ke-i, dan jumlah yang berubah di tengah jalan adalah
    // kelas kegagalan yang tidak menimbulkan error di mana pun.
    if (!teks) {
      hasil.push([jenis, teks, warna]);
      continue;
    }

    const ujung = pos + teks.length;
    while (ke < deret.length && (deret[ke] as [number, number])[1] <= pos) ke++;
    let batas = pos;
    for (
      let j = ke;
      j < deret.length && (deret[j] as [number, number])[0] < ujung;
      j++
    ) {
      const d = deret[j] as [number, number];
      const a = Math.max(pos, d[0]);
      const b = Math.min(ujung, d[1]);
      if (a > batas) hasil.push([jenis, teks.slice(batas - pos, a - pos), warna]);
      hasil.push(["indentasi", teks.slice(a - pos, b - pos), null]);
      batas = b;
    }
    if (batas < ujung) hasil.push([jenis, teks.slice(batas - pos), warna]);
    pos = ujung;
  }
  return hasil;
}

/**
 * Letak pita baris aktif di dalam `.editor-lapis`, dalam piksel angka murni.
 *
 * `tinggi` SELALU `tinggiBaris` apa adanya, dan tidak pernah dikoreksi oleh
 * `baris`: pita setinggi dua baris berbohong soal di mana kursornya berdiri,
 * dan pita setinggi nol tidak menandai apa pun.
 *
 * `atas` TIDAK dijepit ke nol, dan itu syarat, bukan kelalaian. Kalau baris
 * kursor sudah tergulir keluar dari pandangan, hasilnya memang negatif, dan
 * `overflow: hidden` pada `.editor-lapis` memotongnya sampai habis -- persis
 * yang benar, karena yang tidak terlihat memang tidak boleh ditandai.
 * Menjepitnya dengan `Math.max(0, ...)` justru memarkir pita di tepi atas
 * sebagai garis macet yang mengaku "baris aktifmu di sini" padahal kursornya
 * jauh di atas layar; satu-satunya hal yang lebih buruk daripada tidak ada
 * penanda adalah penanda yang menunjuk tempat yang salah.
 */
export function posisiPita({
  baris,
  tinggiBaris,
  paddingAtas,
  scrollTop,
}: {
  baris: number;
  tinggiBaris: number;
  paddingAtas: number;
  scrollTop: number;
}): { atas: number; tinggi: number } {
  const n = Math.max(1, baris);
  return {
    atas: paddingAtas + (n - 1) * tinggiBaris - scrollTop,
    tinggi: tinggiBaris,
  };
}

function escapeRegex(s: string): string {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/** Alih komentar untuk sekumpulan baris. Mengembalikan teks penggantinya. */
export function alihKomentar(blok: string, bahasa: string): string {
  const tanda = KOMENTAR[bahasa] ?? "# ";
  const potong = tanda.trimEnd();
  const baris = blok.split("\n");
  const berisi = baris.filter((b) => b.trim());
  // Kalau SEMUA baris berisi sudah berkomentar, yang dimaksud melepasnya.
  // Menilainya per baris akan membuat blok campur jadi makin campur.
  const semuaKomentar =
    berisi.length > 0 && berisi.every((b) => b.trimStart().startsWith(potong));

  return baris
    .map((b) => {
      if (!b.trim()) return b;
      if (semuaKomentar) {
        return b.replace(new RegExp("^(\\s*)" + escapeRegex(potong) + " ?"), "$1");
      }
      const depan = (b.match(/^\s*/) ?? [""])[0] as string;
      return depan + tanda + b.slice(depan.length);
    })
    .join("\n");
}
