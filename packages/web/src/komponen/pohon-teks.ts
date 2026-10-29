/* Pohon berkas untuk blok kode yang memuat BEBERAPA berkas sekaligus.
 *
 * Bagian MURNI dari `PohonBerkas.tsx`, terpisah supaya `uji/banding-pohon.mjs`
 * bisa mengimpornya tanpa menyeret React. Tiga bagian: pemecah (teks blok jadi
 * berkas), pembangun (daftar nama jadi pohon bertingkat), dan navigator (baris
 * yang tampak ditambah tombol jadi aksi, mengikuti pola WAI-ARIA "tree").
 *
 * Gagasannya dari "Tree Code Viewer" yang ditemukan waktu memindai 21st.dev
 * (pohon folder di kiri, kode berkas yang dipilih di kanan). Kodenya tidak
 * disalin; datanya milik aplikasi ini: 25 blok `multi` di kurikulum, yang kini
 * tampil sebagai satu blok panjang berisi komentar penanda.
 *
 * Penandanya sama dengan yang dikenali server (`_PENANDA_BERKAS` di
 * `inti/berkas.py`): `# File: a.py`, `// ==== file: a/b.go ====`,
 * `/* ===== File: a.h ===== *\/`, `-- file: a.sql`. Server menganggap blok itu
 * multi bila ada paling sedikit DUA nama berbeda; pemecah ini memakai syarat
 * yang sama, jadi keduanya tidak pernah berbeda pendapat tentang satu blok.
 *
 * Satu sifat yang dijaga atas seluruh blok nyata: TIDAK ADA BARIS YANG HILANG.
 * Baris tak kosong yang bukan penanda di blok asli, berurutan, sama persis
 * dengan gabungan catatan dan isi semua berkas.
 */

/** Penanda berkas di AWAL baris. Server mencarinya di mana saja; di data nyata keduanya selalu sama. */
export const POLA_PENANDA = /^\s*(?:\/\*|\/\/|#|--)\s*=*\s*[Ff]ile\s*:\s*([\w./-]+)/;
const POLA_KOMENTAR = /^\s*(?:\/\/|#|--|\/\*|\*)/;

export interface BerkasPecah {
  /** Jalur berkas, tanpa "./" di depan. */
  nama: string;
  /** Isi tanpa baris kosong di ujung-ujungnya; kosong bila berkasnya memang kosong. */
  isi: string;
  /** Jumlah baris di `isi`; 0 untuk berkas kosong. */
  baris: number;
}

export interface HasilPecah {
  /** Komentar sebelum penanda pertama (mis. langkah menyiapkan folder), kosong bila tidak ada. */
  catatan: string;
  berkas: BerkasPecah[];
}

/** Buang "." dan segmen kosong: "./a//b.py" menjadi "a/b.py". */
const bersihkan = (nama: string): string =>
  nama.split("/").filter((s) => s !== "" && s !== ".").join("/");

/** Pangkas baris kosong di awal dan akhir (pemisah antar-berkas), isinya tidak disentuh. */
function pangkas(baris: string[]): string[] {
  let a = 0;
  let b = baris.length;
  while (a < b && (baris[a] ?? "").trim() === "") a++;
  while (b > a && (baris[b - 1] ?? "").trim() === "") b--;
  return baris.slice(a, b);
}

/**
 * Pecah satu blok jadi berkas. `null` bila namanya kurang dari dua.
 *
 * Isi sebelum penanda pertama diperlakukan menurut jenisnya, dan dua kasus
 * nyata menentukan aturannya. Kalau seluruhnya komentar ("// Siapkan dulu:
 * mkdir ..." di materi Go), ia CATATAN di atas penampil. Kalau bukan
 * (`<?php` di materi PHPUnit, yang penandanya jatuh sesudahnya), ia bagian dari
 * berkas pertama dan menempel di depannya: tanpa itu `<?php` hilang atau
 * berdiri sendirian seperti kesalahan.
 *
 * Nama yang muncul dua kali digabung ke satu berkas, dipisah satu baris kosong.
 */
export function pecahBerkas(kode: string): HasilPecah | null {
  const pembuka: string[] = [];
  const urutan: string[] = [];
  const isi = new Map<string, string[]>();
  let kini: string[] | null = null;
  for (const b of kode.split(/\r?\n/)) {
    const m = POLA_PENANDA.exec(b);
    const nama = m ? bersihkan(m[1] ?? "") : "";
    if (m && nama !== "") {
      const ada = isi.get(nama);
      if (ada) {
        ada.push("");
        kini = ada;
      } else {
        kini = [];
        isi.set(nama, kini);
        urutan.push(nama);
      }
    } else if (kini) {
      kini.push(b);
    } else {
      pembuka.push(b);
    }
  }
  if (urutan.length < 2) return null;

  const awal = pangkas(pembuka);
  let catatan = "";
  const pertama = isi.get(urutan[0] ?? "");
  if (awal.length > 0 && pertama) {
    if (awal.every((b) => b.trim() === "" || POLA_KOMENTAR.test(b))) catatan = awal.join("\n");
    else pertama.unshift(...awal);
  }
  return {
    catatan,
    berkas: urutan.map((nama) => {
      const baris = pangkas(isi.get(nama) ?? []);
      return { nama, isi: baris.join("\n"), baris: baris.length };
    }),
  };
}

/* ------------------------------------------------------------------ pohon */

export interface SimpulPohon {
  /** Kunci unik: jalur penuh. Untuk folder yang dipadatkan, jalur folder TERDALAM. */
  kunci: string;
  /** Yang tampil. Folder berantai dipadatkan: "src/main/java". */
  label: string;
  folder: boolean;
  /** Indeks di daftar berkas untuk berkas; -1 untuk folder. */
  berkas: number;
  anak: SimpulPohon[];
}

/**
 * Padatkan folder yang hanya berisi satu folder, seperti VS Code:
 * `src` lalu `main` lalu `java` menjadi satu baris "src/main/java". Kunci yang
 * dipakai kunci folder TERDALAM, karena itu yang membawa anak-anaknya.
 */
function padatkan(daftar: SimpulPohon[]): SimpulPohon[] {
  return daftar.map((s) => {
    if (!s.folder) return s;
    let kini = s;
    for (;;) {
      const satu = kini.anak.length === 1 ? kini.anak[0] : undefined;
      if (!satu || !satu.folder) break;
      kini = { ...satu, label: `${kini.label}/${satu.label}` };
    }
    return { ...kini, anak: padatkan(kini.anak) };
  });
}

/**
 * Pohon dari daftar nama jalur. Urutan penulis dipertahankan, bukan abjad:
 * urutan berkas di sebuah contoh itu sendiri bagian dari penjelasannya
 * (`package.json` lebih dulu, lalu modulnya, lalu titik masuknya). Folder
 * berdiri di tempat berkas pertamanya muncul.
 */
export function bangunPohon(nama: string[]): SimpulPohon[] {
  const akar: SimpulPohon[] = [];
  const folder = new Map<string, SimpulPohon>();
  nama.forEach((n, i) => {
    const bagian = n.split("/").filter((s) => s !== "" && s !== ".");
    if (bagian.length === 0) return;
    let daftar = akar;
    let jalur = "";
    for (let j = 0; j < bagian.length - 1; j++) {
      const potong = bagian[j] ?? "";
      jalur = jalur === "" ? potong : `${jalur}/${potong}`;
      let f = folder.get(jalur);
      if (!f) {
        f = { kunci: jalur, label: potong, folder: true, berkas: -1, anak: [] };
        folder.set(jalur, f);
        daftar.push(f);
      }
      daftar = f.anak;
    }
    daftar.push({
      kunci: bagian.join("/"),
      label: bagian[bagian.length - 1] ?? "",
      folder: false,
      berkas: i,
      anak: [],
    });
  });
  return padatkan(akar);
}

/** Jumlah berkas di bawah satu simpul (1 untuk berkas itu sendiri). */
export function hitungBerkas(s: SimpulPohon): number {
  return s.folder ? s.anak.reduce((t, a) => t + hitungBerkas(a), 0) : 1;
}

/** Kunci semua folder, untuk membukanya sekaligus. */
export function semuaFolder(pohon: SimpulPohon[]): string[] {
  const hasil: string[] = [];
  const jalan = (daftar: SimpulPohon[]) => {
    for (const s of daftar) {
      if (s.folder) {
        hasil.push(s.kunci);
        jalan(s.anak);
      }
    }
  };
  jalan(pohon);
  return hasil;
}

export interface BarisPohon {
  simpul: SimpulPohon;
  /** Tingkat sarang, mulai dari 0. */
  kedalaman: number;
  /** Indeks baris induknya di daftar yang sama, -1 untuk tingkat teratas. */
  induk: number;
  /** Urutan di antara saudaranya (mulai dari 1) dan jumlah saudaranya, untuk pembaca layar. */
  posisi: number;
  ukuran: number;
}

/** Baris yang tampak: anak sebuah folder hanya ikut bila folder itu terbuka. */
export function barisTampak(pohon: SimpulPohon[], terbuka: ReadonlySet<string>): BarisPohon[] {
  const hasil: BarisPohon[] = [];
  const jalan = (daftar: SimpulPohon[], kedalaman: number, induk: number) => {
    daftar.forEach((s, i) => {
      const idx = hasil.length;
      hasil.push({ simpul: s, kedalaman, induk, posisi: i + 1, ukuran: daftar.length });
      if (s.folder && terbuka.has(s.kunci)) jalan(s.anak, kedalaman + 1, idx);
    });
  };
  jalan(pohon, 0, -1);
  return hasil;
}

export interface AksiPohon {
  /** Indeks baris yang berfokus sesudah tombol itu. */
  fokus: number;
  /** Folder yang harus dibuka atau ditutup (kunci); kosong bila tidak ada. */
  buka?: string;
  tutup?: string;
  /** Berkas yang berfokus dipilih (Enter, Spasi). */
  pilih?: boolean;
}

/**
 * Tombol di pohon, menurut pola WAI-ARIA "tree". `null` bila tombolnya bukan
 * milik pohon, supaya pemanggil tidak menelan tombol yang bukan urusannya.
 *
 *  - Bawah dan atas: baris tampak berikutnya dan sebelumnya, tanpa berputar.
 *  - Kanan: folder tertutup dibuka; folder terbuka pindah ke anak pertamanya.
 *  - Kiri: folder terbuka ditutup; selain itu pindah ke folder induknya.
 *  - Home dan End: baris pertama dan terakhir.
 *  - Enter dan Spasi: berkas dipilih, folder dibuka atau ditutup.
 */
export function langkahPohon(
  baris: ReadonlyArray<BarisPohon>,
  fokus: number,
  tombol: string,
  terbuka: ReadonlySet<string>,
): AksiPohon | null {
  if (baris.length === 0) return null;
  const akhir = baris.length - 1;
  const i = Math.max(0, Math.min(akhir, fokus));
  const kini = baris[i];
  if (!kini) return null;
  const s = kini.simpul;
  switch (tombol) {
    case "ArrowDown":
      return { fokus: Math.min(akhir, i + 1) };
    case "ArrowUp":
      return { fokus: Math.max(0, i - 1) };
    case "Home":
      return { fokus: 0 };
    case "End":
      return { fokus: akhir };
    case "ArrowRight":
      if (!s.folder) return { fokus: i };
      if (!terbuka.has(s.kunci)) return { fokus: i, buka: s.kunci };
      return { fokus: baris[i + 1]?.induk === i ? i + 1 : i };
    case "ArrowLeft":
      if (s.folder && terbuka.has(s.kunci)) return { fokus: i, tutup: s.kunci };
      return { fokus: kini.induk >= 0 ? kini.induk : i };
    case "Enter":
    case " ":
      if (!s.folder) return { fokus: i, pilih: true };
      return terbuka.has(s.kunci) ? { fokus: i, tutup: s.kunci } : { fokus: i, buka: s.kunci };
    default:
      return null;
  }
}

/* ------------------------------------------------------------------ teks */

/** Folder dan nama berkas dipisah, untuk kepala panel kode: "toko/model/" dan "produk.py". */
export function jalurBerkas(nama: string): { folder: string; berkas: string } {
  const i = nama.lastIndexOf("/");
  return i < 0 ? { folder: "", berkas: nama } : { folder: nama.slice(0, i + 1), berkas: nama.slice(i + 1) };
}

const EKSTENSI: Record<string, string> = {
  py: "python", js: "javascript", mjs: "javascript", cjs: "javascript", jsx: "javascript",
  // Tidak ada penyorot JSON; aturan JavaScript mewarnai string, angka, dan tanda baca yang sama.
  json: "javascript", jsonc: "javascript",
  ts: "typescript", tsx: "typescript", mts: "typescript",
  go: "go", c: "c", h: "c", cpp: "cpp", hpp: "cpp", cc: "cpp", hh: "cpp", cxx: "cpp",
  java: "java", kt: "kotlin", kts: "kotlin", php: "php", rb: "ruby", rs: "rust",
  sh: "bash", bash: "bash", sql: "sql", html: "html", htm: "html",
  // SCSS bukan CSS, tapi properti, nilai, dan angkanya mirip; komentar `//` tidak ikut terwarnai.
  css: "css", scss: "css",
  yml: "yaml", yaml: "yaml", toml: "toml",
  // `.env` dan `.properties` sama-sama `KUNCI=nilai`, bentuk yang dikenali aturan ini.
  ini: "ini", properties: "ini", env: "ini", cs: "csharp",
};

/**
 * Nama penyorot untuk satu berkas, dari ekstensinya. Kosong untuk yang tidak
 * dikenal: `Makefile`, `Dockerfile`, `go.mod`, `.gitignore`, `.txt`. Berkas itu
 * tetap mendapat pewarnaan DASAR pemindai (string, angka, operator, dan nama
 * yang disusul kurung sebagai fungsi), tetapi tidak ada kata kunci, komentar,
 * atau nama bawaan yang diwarnai: kata kunci bahasa yang salah menyesatkan
 * lebih jauh daripada tidak ada.
 */
export function sorotBerkas(nama: string): string {
  const dasar = jalurBerkas(nama).berkas;
  const titik = dasar.lastIndexOf(".");
  if (titik < 0) return "";
  return EKSTENSI[dasar.slice(titik + 1).toLowerCase()] ?? "";
}

/** Nama yang dibacakan untuk satu baris pohon: berkas dengan jumlah barisnya, folder dengan isinya. */
export function labelBaris(b: BarisPohon, berkas: ReadonlyArray<BerkasPecah>): string {
  const s = b.simpul;
  if (s.folder) return `${s.label}, folder, ${hitungBerkas(s)} berkas`;
  const baris = berkas[s.berkas]?.baris ?? 0;
  return `${s.label}, ${baris === 0 ? "kosong" : `${baris} baris`}`;
}
