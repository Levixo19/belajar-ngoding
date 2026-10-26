/* Adu bagian murni halaman bahasa dengan `webapp/statik/js/layar-belajar.js`.
 *
 * Tiga fungsi, dan ketiganya MEMUTUSKAN sesuatu yang tidak kelihatan kalau
 * salah:
 *
 * * `kalimatBahasa` -- kalimat pertama yang dibaca orang di halaman ini. Tiga
 *   cabangnya dipilih dari `persen`, dan ambangnya (`>= 100`, `<= 0`) adalah
 *   jenis angka yang gampang bergeser jadi `> 100` / `< 0` tanpa satu pun tes
 *   gagal -- yang terjadi cuma kurikulum yang baru 0% menyapa dengan "Sudah 0%
 *   jalan".
 * * `faktaBahasa` -- empat angka di kepala halaman, plus kabar toolchain.
 * * `pilihLanjut` -- tautan di kartu paling terang di layar. Syarat panjang di
 *   cabang pertamanya menyandikan satu urutan belajar (baca blok, lalu uji yang
 *   baru dibaca, KECUALI kamu berhenti di tengah kalimat), dan satu operator
 *   yang terbalik di situ berarti kartu itu menawarkan hal yang salah pada
 *   separuh keadaan. Materi TERKUNCI yang lolos ke sini berarti tombol paling
 *   terang di halaman berujung di layar penolakan.
 *
 * Korpusnya 32 kurikulum sungguhan dari `packages/konten/`, dikalikan dengan
 * profil progres yang menyentuh setiap cabang.
 *
 *     node uji/banding-bahasa.mjs
 */

import { mkdtempSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

import {
  faktaBahasa,
  kalimatBahasa,
  pilihLanjut,
} from "../src/layar/bahasa-teks.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const AKAR = path.resolve(SINI, "..", "..", "..");
const SUMBER = path.join(AKAR, "webapp", "statik", "js", "layar-belajar.js");
const KONTEN = path.join(AKAR, "packages", "konten", "kurikulum");
const BAB_JSON = path.join(AKAR, "packages", "konten", "bab.json");

const teks = readFileSync(SUMBER, "utf-8");

/** Ambil satu deklarasi tingkat-atas dari sumber JS, apa adanya. */
function potong(pola, nama) {
  const cocok = teks.match(pola);
  if (!cocok) {
    console.error(
      `POTONGAN TIDAK KETEMU: ${nama}. layar-belajar.js mungkin ditulis ` +
        `ulang. Perbarui polanya, JANGAN biarkan pagar ini membandingkan nol ` +
        `fungsi.`,
    );
    process.exit(1);
  }
  return cocok[0];
}

const bagian = [
  potong(/function kalimatBahasa\(b, s\) \{[\s\S]*?\n\}/, "kalimatBahasa"),
  potong(/function barisFakta\(b, s\) \{[\s\S]*?\n\}/, "barisFakta"),
  potong(/function kartuLanjutBahasa\(b, key\) \{[\s\S]*?\n\}/, "kartuLanjutBahasa"),
];

/* `barisFakta` dan `kartuLanjutBahasa` MENGGAMBAR. Yang diadu di sini
   keputusannya, jadi penggambarnya diganti perekam: `h()` mencatat pemilih dan
   anaknya, `ikon()` cuma namanya, `keadaan()` menandai dirinya. Itu sah karena
   keduanya memang cuma menyusun satu objek lalu menggambarnya -- dan objek
   itulah yang dipindahkan ke `bahasa-teks.ts`. */
const PRELUDE = `
const h = (pemilih, _sifat = {}, ...anak) => ({
  pemilih, anak: anak.flat(4).filter((a) => a !== null && a !== undefined && a !== false),
});
const ikon = (nama) => ({ ikon: nama });
const keadaan = (o) => ({ keadaan: o });
const kosong = (judul, ket, aksi) => ({ kosong: [judul, ket, aksi] });
const tanpaNomor = (t) => String(t).replace(/^\\s*\\d+\\.\\s*/, "");
const bulat = (n) => Math.round(Number(n) || 0);
`;

const jalurTemp = path.join(
  mkdtempSync(path.join(tmpdir(), "banding-bahasa-")),
  "acuan.mjs",
);
writeFileSync(
  jalurTemp,
  PRELUDE + bagian.join("\n") +
    "\nexport { kalimatBahasa, barisFakta, kartuLanjutBahasa };\n",
);
const acuan = await import(pathToFileURL(jalurTemp).href);

let gagal = 0;
/* Dihitung DI DALAM `adu`, bukan di tiap loop. Versi pertama menghitungnya di
   loop profil dan melaporkan 239 untuk 1.139 perbandingan yang benar-benar
   dijalankan -- angka yang ditagih tes populasi di `test_konten_json.py`, jadi
   hitungan yang lebih kecil daripada kenyataan membuat lantainya kehilangan
   gigi tanpa ada yang tahu. */
let cacah = 0;
const adu = (nama, a, b) => {
  cacah += 1;
  const sa = JSON.stringify(a);
  const sb = JSON.stringify(b);
  if (sa !== sb) {
    gagal += 1;
    console.error(`  ${nama}\n    JS: ${sa}\n    TS: ${sb}`);
  }
};

/* --------------------------------------------------- bentuk ulang keluaran

   Sisi JS mengembalikan pohon `h()`; sisi TS mengembalikan data. Dua fungsi di
   bawah menerjemahkan pohon itu kembali ke data yang sama -- dan keduanya
   MENUNTUT bentuk yang diharapkan, bukan menebak: pohon yang berubah bentuk
   menghentikan pagar ini dengan pesan, bukan dengan nol perbandingan. */

function faktaDariPohon(pohon) {
  if (pohon.pemilih !== "div.fakta") {
    console.error(`BENTUK BARIS FAKTA BERUBAH: ${pohon.pemilih}`);
    process.exit(1);
  }
  return pohon.anak.map((butir) => {
    const [ik, span] = butir.anak;
    return {
      gambar: ik.ikon,
      teks: span.anak[0],
      kurang: butir.pemilih.includes(".fakta-kurang"),
    };
  });
}

function lanjutDariPohon(pohon, kunci) {
  // Tidak ada yang tersisa: versi JS mengembalikan `keadaan({jenis:"tuntas"})`.
  if (pohon.keadaan) return null;
  const [nomor, isi] = pohon.anak;
  const [mata, judul, ket] = isi.anak;
  const jalur = pohon.pemilih; // cuma kelasnya; href ada di sifat yang dibuang
  if (!jalur.startsWith("a.lanjutkan")) {
    console.error(`BENTUK KARTU LANJUTKAN BERUBAH: ${jalur}`);
    process.exit(1);
  }
  return {
    indeks: Number(nomor.anak[0]) - 1,
    mata: mata.anak[0],
    judulTampil: judul.anak[0],
    ket: ket.anak[0],
    kunci,
  };
}

/** Bentuk sisi TS ke bentuk yang sama -- `tanpaNomor` dipakai komponennya. */
function lanjutDariData(s) {
  if (!s) return null;
  return {
    indeks: s.indeks,
    mata: s.mata,
    judulTampil: s.judul.replace(/^\s*\d+\.\s*/, ""),
    ket: s.ket,
    kunci: s.tipe,
  };
}

/* ----------------------------------------------------------------- korpus */

const BAB = JSON.parse(readFileSync(BAB_JSON, "utf-8"));

/* Profil progres: tiap baris memberi status ke materi/kuis/latihan ke-i lewat
   sisa bagi, jadi satu profil menyentuh beberapa cabang sekaligus. Yang
   dikejar BUKAN kelengkapan statistik melainkan kelengkapan CABANG:
   `pilihLanjut` punya empat keluaran mungkin (materi, kuis, latihan, tidak ada
   apa-apa), dan dua di antaranya cuma tercapai kalau yang di atasnya habis. */
const PROFIL = [
  { nama: "baru", materi: () => "baru", kuis: () => false, latihan: () => "baru" },
  {
    nama: "separuh",
    materi: (i) => (i < 5 ? "selesai" : i === 5 ? "sebagian" : "baru"),
    kuis: (i) => i === 0,
    latihan: (i) => (i === 0 ? "lulus" : "baru"),
  },
  {
    nama: "materi-habis",
    materi: () => "selesai",
    kuis: (i) => i % 2 === 0,
    latihan: (i) => (i % 3 === 0 ? "lulus" : "baru"),
  },
  {
    nama: "materi-kuis-habis",
    materi: () => "selesai",
    kuis: () => true,
    latihan: (i) => (i === 0 ? "manual" : "baru"),
  },
  { nama: "tuntas", materi: () => "selesai", kuis: () => true, latihan: () => "lulus" },
  {
    nama: "terkunci-di-depan",
    materi: (i) => (i < 2 ? "selesai" : "baru"),
    kunci: (i) => i >= 2,
    kuis: () => false,
    latihan: () => "baru",
  },
  {
    nama: "berhenti-di-tengah",
    materi: (i) => (i === 0 ? "sebagian" : "baru"),
    kuis: () => false,
    siapKuis: true,
    latihan: () => "baru",
  },
];

const HILANG = [[], ["go"], ["dotnet", "rustc"]];

const kurikulum = readdirSync(KONTEN).sort();
for (const nama of kurikulum) {
  const k = JSON.parse(readFileSync(path.join(KONTEN, nama), "utf-8"));
  const jmlKuis = (k.kuis_mentah || []).length;
  const jmlLatihan = (k.latihan || []).length;

  for (const prof of PROFIL) {
    const b = {
      key: k.key,
      label: k.label,
      materi: k.materi.map((m, i) => ({
        indeks: i,
        judul: m.title,
        status: prof.materi(i),
        terkunci: prof.kunci ? prof.kunci(i) : false,
      })),
      kuis: Array.from({ length: jmlKuis }, (_v, i) => ({
        indeks: i,
        judul: `Kuis ${i + 1}`,
        pernah: prof.kuis(i),
        siap: prof.siapKuis ?? i % 2 === 0,
        jatuh_tempo: i === 1 && prof.kuis(i),
      })),
      latihan: Array.from({ length: jmlLatihan }, (_v, i) => ({
        indeks: i,
        judul: `Latihan ${i + 1}`,
        status: prof.latihan(i),
      })),
      bab: (BAB[k.key] || []).map((x, i) => ({ nomor: i + 1, judul: x.judul })),
    };

    // Statistik seperti `_stat()`: cuma medan yang dibaca ketiga fungsi itu.
    const selesai = b.materi.filter((m) => m.status === "selesai").length;
    const total = b.materi.length + jmlKuis + jmlLatihan;
    const skor =
      selesai + b.kuis.filter((q) => q.pernah).length +
      b.latihan.filter((e) => e.status === "lulus" || e.status === "manual").length;
    const s = {
      materi: selesai,
      total_materi: b.materi.length,
      total_kuis: jmlKuis,
      total_latihan: jmlLatihan,
      persen: total ? (skor / total) * 100 : 0,
    };

    adu(`kalimatBahasa(${k.key}/${prof.nama})`,
        acuan.kalimatBahasa(b, s), kalimatBahasa(s));

    adu(`pilihLanjut(${k.key}/${prof.nama})`,
        lanjutDariPohon(acuan.kartuLanjutBahasa(b, k.key), undefined) &&
          { ...lanjutDariPohon(acuan.kartuLanjutBahasa(b, k.key), undefined),
            kunci: undefined },
        lanjutDariData(pilihLanjut(b)) &&
          { ...lanjutDariData(pilihLanjut(b)), kunci: undefined });

    for (const hilang of HILANG) {
      const siap = hilang.length === 0;
      adu(
        `faktaBahasa(${k.key}/${prof.nama}/${hilang.join("+") || "siap"})`,
        faktaDariPohon(acuan.barisFakta({ siap, hilang }, s)),
        faktaBahasa(s, siap, hilang),
      );
    }
  }
}

/* Ambang persen diadu terpisah, pada angka yang justru paling mudah salah:
   nol, tepat seratus, dan yang ada di sebelahnya. Korpus di atas tidak pernah
   menghasilkan 99,9 atau 100,1. */
const AMBANG = [-1, 0, 0.0001, 0.4, 50, 99.4, 99.5, 99.9, 100, 100.1, 180];
for (const persen of AMBANG) {
  const s = {
    materi: 3, total_materi: 10, total_kuis: 4, total_latihan: 6, persen,
  };
  adu(`kalimatBahasa(persen=${persen})`,
      acuan.kalimatBahasa({}, s), kalimatBahasa(s));
}

/* Kurikulum tanpa kuis atau tanpa latihan: cabang "tidak ada yang tersisa"
   dicapai lewat daftar KOSONG, bukan lewat semuanya selesai. */
for (const b of [
  { materi: [], kuis: [], latihan: [] },
  { materi: [{ indeks: 0, judul: "A", status: "selesai" }], kuis: [], latihan: [] },
  {
    materi: [{ indeks: 0, judul: "A", status: "baru", terkunci: true }],
    kuis: [], latihan: [],
  },
  {
    materi: [{ indeks: 0, judul: "A", status: "baru", terkunci: true }],
    kuis: [], latihan: [{ indeks: 0, judul: "L", status: "baru" }],
  },
]) {
  const js = lanjutDariPohon(acuan.kartuLanjutBahasa(b, "x"), undefined);
  adu(
    `pilihLanjut(pinggiran ${JSON.stringify(b).slice(0, 48)})`,
    js && { ...js, kunci: undefined },
    (() => {
      const d = lanjutDariData(pilihLanjut(b));
      return d && { ...d, kunci: undefined };
    })(),
  );
}

console.log(
  `${cacah} perbandingan atas ${kurikulum.length} kurikulum x ` +
    `${PROFIL.length} profil progres`,
);
if (gagal) {
  console.error(`BERGESER: ${gagal} perbandingan berbeda.`);
  process.exit(1);
}
console.log("COCOK: bagian murni halaman bahasa identik dengan layar-belajar.js.");
