/* Penyorot sintaks sisi-klien.
 *
 * Ini PORT dari pemindai di sorot.py, bukan penyorot kedua. Bedanya cuma
 * bahasa implementasinya: algoritmanya sama langkah demi langkah, dan daftar
 * kata kuncinya tidak ada di sini sama sekali — ia dikirim server lewat
 * /api/awal, diturunkan dari sorot.ATURAN.
 *
 * Kenapa harus ada port sama sekali? Karena editor menyorot ulang setiap kali
 * pelajar menekan satu tombol. Menempuh jaringan untuk itu, meski cuma ke
 * localhost, membuat kursor terasa berat.
 *
 * Kenapa daftar kata kuncinya tetap datang dari server? Karena kalau dua
 * salinan hidup berdampingan, menambah bahasa baru di sorot.py akan
 * menyalakannya di materi tapi tidak di editor — dan tidak akan ada yang
 * menyadarinya sampai seseorang bertanya kenapa warnanya beda di dua tempat.
 *
 * Kontrak yang diuji tests/test_web.py: gabungan seluruh token WAJIB sama
 * persis dengan kode masukan, dan pemecahannya WAJIB identik dengan hasil
 * sorot.token() di Python untuk SELURUH kode di kurikulum.
 *
 * Importir: editor.js, layar-belajar.js, layar-kerja.js.
 */

import { h } from "./inti.js";

const HURUF_AWAL = /[A-Za-z_]/;
const HURUF_LANJUT = /[A-Za-z0-9_]/;
const ANGKA = /[0-9]/;
const OPERATOR = new Set("+-*/%=<>!&|^~?:;,.()[]{}@");
// Kunci di awal baris boleh memuat tanda hubung, titik, dan garis miring.
const KUNCI_LANJUT = /[A-Za-z0-9_.\-/]/;

let ATURAN = {};

/** Pasang tabel leksikal dari /api/awal. Dipanggil sekali saat aplikasi mulai. */
export function pasangAturan(tabel) {
  ATURAN = {};
  for (const [nama, a] of Object.entries(tabel || {})) {
    ATURAN[nama] = {
      ...a,
      kunci: new Set(a.kunci),
      tipe: new Set(a.tipe),
      bawaan: new Set(a.bawaan),
      kutip_mentah: new Set(a.kutip_mentah),
    };
  }
}

function aturanUntuk(bahasa) {
  const a = ATURAN[String(bahasa || "").toLowerCase()];
  if (a) return a;
  // Bahasa tak dikenal tetap tampil utuh, cuma tanpa warna. Sama seperti
  // sorot._POLOS di Python: pemindai ini tidak pernah boleh gagal.
  return {
    komentar_baris: [], komentar_blok: [], kutip: ['"', "'"],
    escape: true, praprosesor: false, variabel_dolar: false,
    tanpa_bedakan_kapital: false, pemisah_kunci: [],
    kunci: new Set(), tipe: new Set(), bawaan: new Set(),
    kutip_mentah: new Set(),
  };
}

export function bahasaDikenal(bahasa) {
  return Boolean(ATURAN[String(bahasa || "").toLowerCase()]);
}

/* --------------------------------------------------------------- pemindai */

function akhirString(kode, i, pembuka, aturan) {
  const mentah = aturan.kutip_mentah.has(pembuka) || !aturan.escape;
  let j = i + pembuka.length;
  const n = kode.length;
  // Kutip tunggal biasa tidak boleh melintasi baris; kutip tiga dan kutip
  // terbalik boleh.
  const satuBaris = pembuka.length === 1 && pembuka !== "`";

  while (j < n) {
    const c = kode[j];
    if (!mentah && c === "\\") { j += 2; continue; }
    if (kode.startsWith(pembuka, j)) return j + pembuka.length;
    if (satuBaris && c === "\n") return j;
    j += 1;
  }
  return n;
}

function akhirAngka(kode, i) {
  const n = kode.length;
  let j = i;
  if (kode[j] === "0" && j + 1 < n && "xXbBoO".includes(kode[j + 1])) {
    j += 2;
    while (j < n && HURUF_LANJUT.test(kode[j])) j += 1;
    return j;
  }
  let lihatTitik = false;
  while (j < n) {
    const c = kode[j];
    if (ANGKA.test(c) || c === "_") {
      j += 1;
    } else if (c === "." && !lihatTitik && j + 1 < n && ANGKA.test(kode[j + 1])) {
      lihatTitik = true; j += 1;
    } else if ("eE".includes(c) && j + 1 < n
               && (ANGKA.test(kode[j + 1]) || "+-".includes(kode[j + 1]))) {
      j += 2;
    } else if ("fFlLdDuU".includes(c)) {   // sufiks literal C/Java
      j += 1;
    } else {
      break;
    }
  }
  return j;
}

function diAwalBaris(kode, i) {
  let j = i - 1;
  while (j >= 0 && (kode[j] === " " || kode[j] === "\t")) j -= 1;
  return j < 0 || kode[j] === "\n";
}

/** Index sesudah KUNCI yang dimulai di `i`, atau 0 kalau bukan kunci.
 *  Padanan `_akhir_kunci` di sorot.py, langkah demi langkah. */
function akhirKunci(kode, i, pemisah) {
  let j = i - 1;
  while (j >= 0 && kode[j] !== "\n") {
    const d = kode[j];
    if (d === " " || d === "\t" || (d === "-" && (kode[j + 1] === " " || kode[j + 1] === "\t"))) j -= 1;
    else return 0;
  }
  const n = kode.length;
  let akhir = i + 1;
  while (akhir < n && KUNCI_LANJUT.test(kode[akhir])) akhir += 1;
  let k = akhir;
  while (k < n && (kode[k] === " " || kode[k] === "\t")) k += 1;
  if (k >= n || !pemisah.includes(kode[k])) return 0;
  const sesudah = k + 1 < n ? kode[k + 1] : "";
  if (kode[k] === ":" && sesudah !== "" && sesudah !== " " && sesudah !== "\t"
      && sesudah !== "\r" && sesudah !== "\n") return 0;
  if (kode[k] === "=" && sesudah === "=") return 0;
  return akhir;
}

/** Pecah kode jadi [[jenis, teks], ...]. Gabungannya = kode aslinya. */
export function token(kode, bahasa) {
  const aturan = aturanUntuk(bahasa);
  const hasil = [];
  let simpanan = [];
  let i = 0;
  const n = kode.length;

  const buang = () => {
    if (simpanan.length) {
      hasil.push(["teks", simpanan.join("")]);
      simpanan = [];
    }
  };

  while (i < n) {
    const c = kode[i];

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
    const blok = aturan.komentar_blok.find((p) => kode.startsWith(p[0], i));
    if (blok) {
      const buka = blok[0];
      const tutup = blok[1];
      let akhir = kode.indexOf(tutup, i + buka.length);
      akhir = akhir < 0 ? n : akhir + tutup.length;
      buang();
      hasil.push(["komentar", kode.slice(i, akhir)]);
      i = akhir;
      continue;
    }

    // -- komentar baris ----------------------------------------------------
    if (aturan.komentar_baris.some((p) => kode.startsWith(p, i))) {
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
    if (aturan.variabel_dolar && c === "$") {
      let j = i + 1;
      if (j < n && kode[j] === "{") {
        const tutup = kode.indexOf("}", j);
        j = tutup < 0 ? n : tutup + 1;
      } else if (j < n && kode[j] === "(") {
        j += 1;
      } else {
        while (j < n && HURUF_LANJUT.test(kode[j])) j += 1;
        if (j === i + 1 && j < n) j += 1;      // $1, $@, $?, $#
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
    if (aturan.pemisah_kunci && aturan.pemisah_kunci.length && HURUF_AWAL.test(c)) {
      const akhir = akhirKunci(kode, i, aturan.pemisah_kunci);
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
      while (j < n && HURUF_LANJUT.test(kode[j])) j += 1;
      const kata = kode.slice(i, j);
      const banding = aturan.tanpa_bedakan_kapital ? kata.toUpperCase() : kata;

      let jenis;
      if (aturan.kunci.has(banding)) jenis = "kunci";
      else if (aturan.tipe.has(banding)) jenis = "tipe";
      else if (aturan.bawaan.has(banding)) jenis = "bawaan";
      else {
        let k = j;
        while (k < n && (kode[k] === " " || kode[k] === "\t")) k += 1;
        jenis = (k < n && kode[k] === "(") ? "fungsi" : "teks";
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

/** Satukan token berdampingan yang sejenis.
 *
 *  Tanpa ini `System.out.println(` menghasilkan lima token operator terpisah,
 *  masing-masing jadi satu <span> sendiri — hasilnya berkali lipat lebih
 *  panjang dari kodenya, padahal tampilannya sama persis. */
function gabung(daftar) {
  const padat = [];
  for (const pasang of daftar) {
    const jenis = pasang[0];
    const teks = pasang[1];
    if (padat.length && padat[padat.length - 1][0] === jenis) {
      padat[padat.length - 1][1].push(teks);
    } else {
      padat.push([jenis, [teks]]);
    }
  }
  return padat.map((p) => [p[0], p[1].join("")]);
}

/* ---------------------------------------------------------------- keluaran */

/** Token -> fragment DOM ber-<span class="tk-...">. */
export function keFragmen(daftar) {
  const wadah = document.createDocumentFragment();
  for (const pasang of daftar || []) {
    const jenis = pasang[0];
    const teks = pasang[1];
    if (jenis === "teks") wadah.appendChild(document.createTextNode(teks));
    else wadah.appendChild(h("span.tk-" + jenis, {}, teks));
  }
  return wadah;
}

/** Sorot kode langsung dari string. Dipakai editor dan ruang coba. */
export function sorotKe(el, kode, bahasa) {
  el.textContent = "";
  el.appendChild(keFragmen(token(kode, bahasa)));
  return el;
}

/** <pre class="kode"> berisi kode tersorot dari token yang sudah dikirim
 *  server. Materi memakai jalur ini: token-nya dihitung sekali di Python, jadi
 *  browser tidak perlu memindai ulang ratusan blok kode saat halaman dibuka. */
export function praKode(token_, kelas = "") {
  return h("pre.kode" + (kelas ? "." + kelas : ""), {},
    h("code", {}, keFragmen(token_)));
}
