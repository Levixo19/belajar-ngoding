/* Sifat-sifat geometri layar Langit (ikhtisar dan lensa) atas SELURUH kurikulum.
 *
 * Beda dari pembanding lain di folder ini: tidak ada implementasi lama yang
 * bisa diadu, karena ikhtisar-plus-lensa memang tidak ada di antarmuka lama.
 * Yang dijaga di sini SIFAT yang membuat peta bisa dipakai, bukan keluaran
 * yang dibekukan:
 *
 *   [grid]     pencari bintang terdekat sama dengan pencarian paksa
 *   [jari]     jari-jari bintang tidak pernah membuat dua bintang bersentuhan
 *   [sasaran]  pusat sebuah bintang menunjuk bintang itu sendiri, dan wilayah
 *              rasi memuat seluruh bintangnya
 *   [lensa]    lensa adalah bentuk ikhtisar yang diskalakan (pelebaran paling
 *              banyak 1,5 per sumbu), tidak ada bintang atau label yang
 *              keluar kanvas, dan label tidak menumpuk
 *   [tombol]   tabel tombol papan ketik pohon bintang
 *   [glif]     empat bentuk status berbeda, semuanya path berkoordinat mutlak
 *   [wilayah]  selubung cembung dan uji titik-di-dalam
 *   [garis]    garis rasi ikhtisar: >= 95 persen ruas dalam-bab tergambar di
 *              akar 1156, 1440, dan 1905 px, dari tepi glif ke tepi glif
 *   [kartu]    bintang yang pusatnya tertutup kartu judul bintang lain tetap
 *              bisa disorot dan diklik lewat kartu
 *   [bentuk]   `bentukJawabanSah`: `200 {}` dan teman-temannya tidak lolos
 *   [pembuka]  `ringkasPembuka` sama dengan rekaman dari acuan Python, dan
 *              tidak pernah melempar (teks kosong, teks spasi)
 *   [kontrak]  angka kontrak (jari-jari, jangkauan, ukuran lencana dan kartu)
 *              ditulis sebagai LITERAL di sini, bukan dibaca dari modul
 *   [label]    nama aksesibel bintang: nomor, judul, status; "berikutnya" dan
 *              "cocok dengan X" hanya bila penandanya digambar
 *   [tip]      kartu judul lensa: di dalam kanvas, bintangnya di antara tepi
 *              atas-bawah, sisi dekatnya <= 20 px dari bintang, bisa dilayangi
 *              (koridor), dan bintang yang terhimpit tetap bisa dicapai
 *   [alamat]   `bacaAlamat` tidak pernah melempar (persen-sandi rusak = null)
 *   [gulir]    gulir yang membuat bintang berfokus dan judul panel tampak
 *   [skala]    ukuran huruf aplikasi: lencana dan nomor ikut membesar, dan 1 =
 *              persis lensa lama
 *   [keluarga] judul keluarga tidak menimpa bintang (tabel `TATA`/`KELUARGA`
 *              diimpor dari `langit-data.ts`, bukan disalin)
 *
 * Korpusnya 32 kurikulum nyata dari `packages/konten` (jumlah materi dan
 * pembagian bab), dengan enam profil progres yang diturunkan dari indeks
 * (bukan dari berkas pelajar): peta langit kosong, setengah, penuh, dan tiga
 * acak berbenih tetap. Pelanggaran invarian server ("terkunci" hanya
 * berpasangan dengan status "baru") sengaja tidak dibuat.
 *
 *     node uji/banding-lensa.mjs
 */

import { readFileSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import {
  bagianGlif,
  bangunGrid,
  bangunIkhtisar,
  bangunLensa,
  bintangDiBawahKartu,
  jalurPenunjuk,
  JARI_LENSA_PX,
  JANGKAU_BINTANG_PX,
  JANGKAU_LENSA_PX,
  JARI_PX,
  jariIkhtisar,
  KORIDOR_TIP_PX,
  LEBAR_KANVAS_TIP_MIN,
  LEBAR_TIP_MAKS,
  CELAH_TIP,
  TINGGI_TIP_MAKS,
  pilihSorotLensa,
  romawi,
  ruasIkhtisar,
  sasaranLensa,
  tempatTip,
  langkahTombol,
  CELAH_GULIR,
  deltaGulirPanel,
  deltaGulirTampak,
  LETAK_PANEL,
  pathBraket,
  pathWilayah,
  sasaranIkhtisar,
  selubungCembung,
  statusBintang,
  terdekat,
  titikDiPoligon,
  URUTAN_STATUS,
  wilayahPoligon,
} from "../src/komponen/lensa-geometri.ts";
import {
  bacaAlamat, hitungBab, kalimatDipilih, kataAksiBaca, kataMulai, labelBintang, labelRasi, pecahKode, ringkasPembuka,
} from "../src/komponen/lensa-teks.ts";
import { bentukJawabanSah, KELUARGA, KONSEP, TATA } from "../src/layar/langit-data.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const KONTEN = path.resolve(SINI, "..", "..", "konten");
const baca = (...p) => JSON.parse(readFileSync(path.join(...p), "utf-8"));

let gagal = 0;
let cacah = 0;
const keluhan = {};

/** Satu perbandingan. `kategori` muncul di awal pesan: baterai mutasi
 *  menagihnya, jadi sel yang memerah karena alasan LAIN tidak dihitung. */
function aku(kategori, kondisi, pesan) {
  cacah += 1;
  if (kondisi) return;
  gagal += 1;
  keluhan[kategori] = (keluhan[kategori] ?? 0) + 1;
  if (keluhan[kategori] <= 3) console.error(`  [${kategori}] ${pesan}`);
}

/** Kotak sebuah label nomor, dihitung dari jangkar dan lebarnya (6,8 px per
 *  angka + 3, tinggi 13): rumus yang sama dengan pemecah label. */
function kotakLabel(s) {
  const w = String(s.i + 1).length * 6.8 + 3;
  const x0 = s.label.jangkar === "start" ? s.label.x : s.label.jangkar === "end" ? s.label.x - w : s.label.x - w / 2;
  return { x0, x1: x0 + w, y0: s.label.y - 6.5, y1: s.label.y + 6.5 };
}

const beririsanKotak = (a, b) => a.x0 < b.x1 && a.x1 > b.x0 && a.y0 < b.y1 && a.y1 > b.y0;
const kotakPil = (p) => ({ x0: p.x - p.w / 2, x1: p.x + p.w / 2, y0: p.y - p.h / 2, y1: p.y + p.h / 2 });
/** Delapan segmen garis braket empat-sudut (`pathBraket`): yang digambar, bukan
 *  persegi pembatasnya. */
function segBraket(x, y, R, p) {
  const a = x - R, b = x + R, c = y - R, d = y + R;
  return [[a, c + p, a, c], [a, c, a + p, c], [b - p, c, b, c], [b, c, b, c + p],
          [b, d - p, b, d], [b, d, b - p, d], [a + p, d, a, d], [a, d, a, d - p]];
}
const segKenaKotak = (s, k) =>
  Math.min(s[0], s[2]) < k.x1 && Math.max(s[0], s[2]) > k.x0 && Math.min(s[1], s[3]) < k.y1 && Math.max(s[1], s[3]) > k.y0;

/** mulberry32: acak berbenih, supaya korpus sama di tiap mesin. */
function acak(benih) {
  let b = benih;
  return () => {
    b |= 0;
    b = (b + 0x6d2b79f5) | 0;
    let t = Math.imul(b ^ (b >>> 15), 1 | b);
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

/* ----------------------------------------------------------------- korpus */

const BAB = baca(KONTEN, "bab.json");
const KURIKULUM = Object.keys(BAB).map((key) => {
  const k = baca(KONTEN, "kurikulum", `${key}.json`);
  return { key, label: k.label, judul: k.materi.map((m) => m.title), bab: BAB[key] };
});
if (KURIKULUM.length < 32) {
  console.error(`KORPUS BERUBAH: ${KURIKULUM.length} kurikulum, harusnya >= 32.`);
  process.exit(1);
}

/* Profil: status tiap bab (tuntas / terbuka / terkunci), lalu tiap materi di
   dalamnya. "terkunci" selalu berpasangan dengan "baru". */
const PROFIL = [
  { nama: "kosong", bab: (k) => (k === 0 ? "terbuka" : "terkunci"), isi: () => "baru" },
  { nama: "separuh", bab: (k, n) => (k < n / 2 ? "tuntas" : k < n / 2 + 1 ? "terbuka" : "terkunci"),
    isi: (i, k) => (k === 0 || i % 3 !== 2 ? "selesai" : i % 5 === 0 ? "sebagian" : "baru") },
  { nama: "penuh", bab: () => "tuntas", isi: () => "selesai" },
  ...[1, 2, 3].map((s) => {
    const r = acak(20261027 + s);
    return {
      nama: `acak${s}`,
      bab: (k) => (k === 0 ? "terbuka" : ["tuntas", "terbuka", "terkunci"][Math.floor(r() * 3)]),
      isi: () => ["selesai", "sebagian", "baru"][Math.floor(r() * 3)],
    };
  }),
];

function bahasaDari(kur, profil) {
  const materi = [];
  const bab = kur.bab.map((b, k) => {
    const st = profil.bab(k, kur.bab.length);
    const idx = [];
    for (let i = b.awal; i <= b.akhir; i++) {
      const status = st === "terkunci" ? "baru" : st === "tuntas" ? "selesai" : profil.isi(i, k);
      materi[i] = { judul: `${i + 1}. ${kur.judul[i]}`, status, terkunci: st === "terkunci" };
      idx.push(i);
    }
    return { nomor: k + 1, judul: b.judul, materi: idx };
  });
  return { key: kur.key, label: kur.label, materi, bab };
}

const SKALA = [0.571, 0.826, 0.964, 1.286];
const KANVAS = [[1356, 678], [946, 700], [892, 544], [358, 480]];

/* ------------------------------------------------------- ikhtisar dan lensa */

let totalBintang = 0;
const labelLebar = { menimpa: 0, total: 0 };
const labelNyata = { menimpa: 0, total: 0 };
for (const profil of PROFIL) {
  const bahasa = KURIKULUM.map((k) => bahasaDari(k, profil));
  for (const skala of SKALA) {
    const ik = bangunIkhtisar(bahasa, TATA, skala);
    const r = acak(7 + Math.round(skala * 1000));
    totalBintang += ik.semua.length;

    // [grid] pencari terdekat == pencarian paksa
    for (let n = 0; n < 400; n++) {
      const x = r() * ik.lebar;
      const y = r() * ik.tinggi;
      let terbaik = null;
      let d2 = 40 * 40;
      for (const s of ik.semua) {
        const dd = (s.x - x) ** 2 + (s.y - y) ** 2;
        if (dd < d2) { d2 = dd; terbaik = s; }
      }
      const h = terdekat(ik.grid, x, y, 40);
      aku("grid", (terbaik === null) === (h === null) &&
          (terbaik === null || Math.abs(Math.sqrt(d2) - h.jarak) < 1e-9),
          `titik ${x.toFixed(1)},${y.toFixed(1)} skala ${skala}`);
    }

    for (const rasi of ik.rasi) {
      for (const s of rasi.bintang) {
        // [jari] batas status, batas tetangga, lantai
        aku("jari", s.r <= JARI_PX[s.status] + 1e-9, `r > batas status ${rasi.key}#${s.i}`);
        aku("jari", s.r <= Math.max(1.25, 0.46 * s.nn) + 1e-9, `r > 46% tetangga ${rasi.key}#${s.i}`);
        aku("jari", s.r >= 1.25 - 1e-9 || s.nn < 2.7, `r di bawah lantai ${rasi.key}#${s.i}`);
        // [sasaran] pusat menunjuk dirinya sendiri; ada di wilayahnya sendiri
        const h = sasaranIkhtisar(ik, s.x, s.y);
        aku("sasaran", h !== null && h.bintang === s && h.tepat, `pusat ${rasi.key}#${s.i} menunjuk lain`);
        aku("wilayah", titikDiPoligon(rasi.wilayah, s.x, s.y), `bintang di luar wilayah ${rasi.key}#${s.i}`);
      }
      // dua bintang tidak bersentuhan (hanya diperiksa dalam rasi yang sama:
      // jarak antar-rasi minimum 24 satuan dasar)
      for (let i = 1; i < rasi.bintang.length; i++) {
        const a = rasi.bintang[i - 1];
        const b = rasi.bintang[i];
        if (Math.min(a.nn, b.nn) > 2.7) {
          aku("jari", Math.hypot(a.x - b.x, a.y - b.y) >= a.r + b.r - 1e-9, `bersentuhan ${rasi.key}#${i}`);
        }
      }
    }
    // [keluarga] judul keluarga (Bodoni 20-30 px + keterangan) tidak menimpa
    // bintang. Kotaknya diukur dari DOM di 1156-1905 px: paling lebar 183
    // satuan dasar ("Perkakas & data" di 1156) dan tinggi 48-62 px.
    for (const [k, [nama, x, y]] of Object.entries(KELUARGA)) {
      const x0 = x * skala, x1 = x0 + 185 * skala, y1 = y * skala, y0 = y1 - 64;
      const kena = ik.semua.filter((s) => s.x + s.r > x0 && s.x - s.r < x1 && s.y + s.r > y0 && s.y - s.r < y1);
      aku("keluarga", kena.length === 0, `judul "${nama}" menimpa ${kena.length} bintang @${skala}`);
    }
    // urutan terang: jari-jari tidak naik menurut status "makin jauh"
    for (let i = 1; i < URUTAN_STATUS.length; i++) {
      aku("jari", JARI_PX[URUTAN_STATUS[i - 1]] > JARI_PX[URUTAN_STATUS[i]], "urutan terang status");
      aku("jari", JARI_LENSA_PX[URUTAN_STATUS[i - 1]] > JARI_LENSA_PX[URUTAN_STATUS[i]], "urutan terang status lensa");
    }
  }

  // [lensa] per kanvas per rasi
  for (const [lb, tg] of KANVAS) {
    for (const b of bahasa) {
      const tepiX = lb > 600 ? 72 : 30;
      const lens = bangunLensa(b.materi, b.bab, b.key, { lebar: lb, tinggi: tg, tepiX, tepiY: 54 });
      aku("lensa", lens.bintang.length === b.materi.length, `jumlah ${b.key}`);
      const ik0 = bangunIkhtisar([b], { [b.key]: [700, 700, "web"] }, 1).semua;
      const lx = lens.bintang.map((p) => p.x);
      const ly = lens.bintang.map((p) => p.y);
      const ix = ik0.map((p) => p.x);
      const iy = ik0.map((p) => p.y);
      const rentang = (a) => Math.max(...a) - Math.min(...a);
      const mid = (a) => (Math.max(...a) + Math.min(...a)) / 2;
      if (b.materi.length > 2 && rentang(ix) > 0 && rentang(iy) > 0) {
        const sx = rentang(lx) / rentang(ix);
        const sy = rentang(ly) / rentang(iy);
        aku("lensa", Math.max(sx / sy, sy / sx) <= 1.5 * (1 + 1e-4) || sx === sy, `pelebaran > 1,5 ${b.key}`);
        let maks = 0;
        for (let i = 0; i < ik0.length; i++) {
          maks = Math.max(maks, Math.abs(lx[i] - mid(lx) - (ix[i] - mid(ix)) * sx), Math.abs(ly[i] - mid(ly) - (iy[i] - mid(iy)) * sy));
        }
        aku("lensa", maks < 1e-6, `bentuk lensa menyimpang dari ikhtisar ${b.key}: ${maks}`);
      }
      for (const s of lens.bintang) {
        aku("lensa", s.x - s.r >= 0 && s.x + s.r <= lb && s.y - s.r >= 0 && s.y + s.r <= tg, `bintang keluar ${b.key}#${s.i}`);
        aku("lensa", s.r <= JARI_LENSA_PX[s.status] + 1e-9 && s.r <= Math.max(3.2, 0.46 * s.nn) + 1e-9, `r lensa ${b.key}#${s.i}`);
        const kl = kotakLabel(s);
        aku("lensa", kl.x0 >= -1 && kl.x1 <= lb + 1 && kl.y0 >= -1 && kl.y1 <= tg + 1, `label keluar ${b.key}#${s.i}`);
        // penunjuk berakhir di tepi kanvas
        const kanan = jalurPenunjuk(s, lb, tg, "kanan");
        const bawah = jalurPenunjuk(s, lb, tg, "bawah");
        aku("lensa", kanan.ujungX === lb && kanan.ujungY === s.y && bawah.ujungY === tg && bawah.ujungX === s.x, `penunjuk ${b.key}#${s.i}`);
      }
      aku("lensa", lens.tumpang.keluar === 0, `label keluar kanvas ${b.key}: ${lens.tumpang.keluar}`);
      // label tidak menumpuk: di kanvas lebar (>= 892) paling banyak 13 persen
      // label SATU rasi menimpa bintang atau label lain (rasi padat seperti
      // backend, 56 bintang, adalah yang terburuk: 6 dari 73), dan 1,5 persen
      // di seluruh korpus. Di kanvas sempit (358) tidak ditagih: terukur 5,2
      // persen, dilaporkan saja.
      if (lb >= 892) {
        const total = lens.bintang.length + lens.bab.length + 1;
        aku("lensa", lens.tumpang.bintang <= Math.max(3, 0.13 * total), `label menumpuk ${b.key} @${lb}: ${lens.tumpang.bintang}/${total}`);
        labelLebar.menimpa += lens.tumpang.bintang;
        labelLebar.total += total;
      }
      // tumpang tindih label dihitung ULANG dari keluaran, tidak mempercayai
      // `lens.tumpang` (laporan pemecah sendiri: sel yang membutakannya lolos)
      if (lb >= 892) {
        const semuaKotak = lens.bintang.map(kotakLabel);
        let menimpa = 0;
        semuaKotak.forEach((k, i) => {
          const bukan = lens.bintang.some((s, j) => j !== i && k.x0 < s.x + s.r && k.x1 > s.x - s.r && k.y0 < s.y + s.r && k.y1 > s.y - s.r);
          const lain = semuaKotak.some((o, j) => j > i && k.x0 < o.x1 && k.x1 > o.x0 && k.y0 < o.y1 && k.y1 > o.y0);
          if (bukan || lain) menimpa += 1;
        });
        labelNyata.menimpa += menimpa;
        labelNyata.total += semuaKotak.length;
      }
      // garis hanya di dalam satu bab dan tidak melintasi batas bab
      const babDari = new Array(b.materi.length).fill(-1);
      b.bab.forEach((bb, k) => bb.materi.forEach((i) => { babDari[i] = k; }));
      for (const g of lens.garis) aku("lensa", babDari[g.dari] === babDari[g.ke], `garis lintas bab ${b.key}#${g.dari}`);
      // berikutnya = bintang pertama yang belum selesai dan tidak terkunci
      const ib = b.materi.findIndex((m) => m.status !== "selesai" && !m.terkunci);
      aku("lensa", (ib < 0) === (lens.berikut === null) && (ib < 0 || lens.berikut.i === ib), `berikutnya ${b.key}`);
      // GARIS braket "berikutnya" tidak tertimpa lencana bab atau lencana
      // "berikutnya" sendiri (28 dari 32 rasi pada profil kosong sebelum
      // lencana ditempatkan sesudah braket).
      if (ib >= 0 && lb >= 892) {
        const sb = lens.bintang[ib];
        const segs = segBraket(sb.x, sb.y, sb.r + 9, 7);
        const pil = lens.bab.filter((p) => p.awal >= 0).map(kotakPil);
        if (lens.berikut) pil.push(kotakPil(lens.berikut));
        aku("lensa", !pil.some((k) => segs.some((sg) => segKenaKotak(sg, k))), `braket berikutnya tertimpa lencana ${b.key} @${lb}x${tg} (${profil.nama})`);
      }
      // sasaran lensa: pusat tiap bintang menunjuk dirinya sendiri
      const grid = bangunGrid(lens.bintang, lb, tg, 24);
      for (const s of lens.bintang) {
        const h = terdekat(grid, s.x, s.y, 22);
        aku("sasaran", h !== null && h.t === s, `pusat lensa ${b.key}#${s.i}`);
      }
    }
  }
}

/* [garis] Lebar yang dipakai pelajar: 1156 (batas bawah peta), 1440, dan 1905
   (wadah dipatok 1800). `ruasAntara` memberi 35, 53, dan 69 persen; ruas dari
   tepi ke tepi glif memberi >= 98 persen. Ujungnya diperiksa terhadap
   jari-jari: ujung di r + 3 (aturan lama) atau di pusat (tertimpa glif
   "baru" yang berongga) sama-sama salah. */
{
  let kasus = 0;
  for (const profil of PROFIL) {
    const bahasa = KURIKULUM.map((k) => bahasaDari(k, profil));
    for (const lebar of [1156, 1440, 1800]) {
      const ik = bangunIkhtisar(bahasa, TATA, lebar / 1400);
      let mungkin = 0, tergambar = 0;
      for (const r of ik.rasi) {
        for (let i = 1; i < r.bintang.length; i++) {
          if (r.awalBab.has(i)) continue;
          const a = r.bintang[i - 1], b = r.bintang[i];
          mungkin += 1;
          const u = ruasIkhtisar([a.x, a.y], [b.x, b.y], a.r, b.r);
          if (!u) continue;
          tergambar += 1;
          const d = Math.hypot(b.x - a.x, b.y - a.y);
          const ujungA = Math.hypot(u.x1 - a.x, u.y1 - a.y), ujungB = Math.hypot(u.x2 - b.x, u.y2 - b.y);
          const lurus = Math.abs((u.x1 - a.x) * (b.y - a.y) - (u.y1 - a.y) * (b.x - a.x)) / d
            + Math.abs((u.x2 - a.x) * (b.y - a.y) - (u.y2 - a.y) * (b.x - a.x)) / d;
          aku("garis", Math.abs(ujungA - a.r) < 1e-6 && Math.abs(ujungB - b.r) < 1e-6 && lurus < 1e-6 &&
              Math.abs(Math.hypot(u.x2 - u.x1, u.y2 - u.y1) - (d - a.r - b.r)) < 1e-6,
              `ruas ${r.key}#${i} @${lebar} (${profil.nama}) bukan tepi ke tepi: ${ujungA.toFixed(2)}/${a.r.toFixed(2)} ${ujungB.toFixed(2)}/${b.r.toFixed(2)}`);
        }
      }
      kasus += 1;
      aku("garis", tergambar >= 0.95 * mungkin, `garis ikhtisar ${tergambar}/${mungkin} @${lebar} (${profil.nama}) di bawah 95 persen`);
      // sentuhan dua glif (tidak ada garis yang bisa terlihat): tidak digambar
      aku("garis", ruasIkhtisar([0, 0], [5, 0], 3, 2) === null && ruasIkhtisar([0, 0], [5.01, 0], 3, 2) !== null, "ruas hanya ditolak bila glif bersentuhan");
    }
  }
  aku("garis", kasus === PROFIL.length * 3, "korpus garis menyusut");
}

aku("lensa", labelNyata.menimpa <= 0.02 * labelNyata.total,
    `label nomor menimpa ${labelNyata.menimpa} dari ${labelNyata.total} (dihitung ulang dari keluaran, > 2 persen)`);
aku("lensa", labelLebar.menimpa <= 0.015 * labelLebar.total,
    `label menimpa ${labelLebar.menimpa} dari ${labelLebar.total} di kanvas lebar (> 1,5 persen)`);

/* Kanvas sempit sengaja diperketat: di kanvas lebar pemecah label tidak pernah
   terpaksa memilih arah yang keluar, jadi sel yang mematikan pagar tepinya
   lolos tanpa ini. */
{
  const kecil = bahasaDari(KURIKULUM.find((k) => k.key === "typescript") ?? KURIKULUM[0], PROFIL[1]);
  for (const [lb, tg] of [[240, 180], [200, 260], [300, 160]]) {
    const lens = bangunLensa(kecil.materi, kecil.bab, kecil.key, { lebar: lb, tinggi: tg, tepiX: 26, tepiY: 26, tarik: 1 });
    for (const s of lens.bintang) {
      const kl = kotakLabel(s);
      aku("lensa", kl.x0 >= -1 && kl.x1 <= lb + 1 && kl.y0 >= -1 && kl.y1 <= tg + 1, `label keluar kanvas kecil ${lb}x${tg} #${s.i}`);
    }
    aku("lensa", lens.tumpang.keluar === 0, `kanvas kecil ${lb}x${tg}: ${lens.tumpang.keluar} label keluar`);
  }
}

/* ------------------------------------------------------------------ tombol */

{
  const babDari = [0, 0, 0, 1, 1, 2, 2, 2];
  const awal = [0, 3, 5];
  const T = (k, kini) => langkahTombol(k, kini, 8, babDari, awal);
  aku("tombol", T("ArrowRight", 3) === 4 && T("ArrowDown", 3) === 4, "kanan/bawah maju satu");
  aku("tombol", T("ArrowLeft", 3) === 2 && T("ArrowUp", 3) === 2, "kiri/atas mundur satu");
  aku("tombol", T("ArrowRight", 7) === 7 && T("ArrowLeft", 0) === 0, "tidak melewati ujung");
  aku("tombol", T("Home", 5) === 0 && T("End", 2) === 7, "Home dan End");
  aku("tombol", T("PageDown", 1) === 3 && T("PageDown", 4) === 5 && T("PageDown", 6) === 7, "PageDown: awal bab berikutnya, atau ujung");
  aku("tombol", T("PageUp", 4) === 3 && T("PageUp", 3) === 0 && T("PageUp", 0) === 0, "PageUp: awal bab ini, lalu bab sebelumnya");
  for (const k of ["Enter", " ", "Tab", "Escape", "a", "?", "g"]) {
    aku("tombol", T(k, 3) === null, `tombol ${JSON.stringify(k)} bukan milik pohon`);
  }
  // Alt+Panah = Mundur/Maju peramban, Ctrl+Home/End = gulir dokumen, Meta+Panah
  // = Mundur/Maju (macOS): bukan milik pohon. Shift tidak mengubah apa pun.
  for (const k of ["ArrowRight", "ArrowLeft", "ArrowUp", "ArrowDown", "Home", "End", "PageUp", "PageDown"]) {
    for (const mod of ["alt", "ctrl", "meta"]) {
      aku("tombol", langkahTombol(k, 3, 8, babDari, awal, { [mod]: true }) === null, `${mod}+${k} harus dikembalikan ke peramban`);
    }
    aku("tombol", langkahTombol(k, 3, 8, babDari, awal, { alt: false, ctrl: false, meta: false }) === T(k, 3), `tanpa pengubah sama dengan biasa: ${k}`);
  }
}

/* ------------------------------------------------------------------ alamat */

{
  const ok = (h, key, idx) => { const r = bacaAlamat(h); return r !== null && r.key === key && r.indeks === idx; };
  aku("alamat", ok("#/langit/html", "html", null) && ok("#/langit/html/13", "html", 13) && ok("#/langit/cpp/0", "cpp", 0), "alamat sah");
  aku("alamat", bacaAlamat("#/dasbor") === null && bacaAlamat("#/langit") === null && bacaAlamat("#/langit/") === null && bacaAlamat("") === null, "bukan alamat lensa");
  aku("alamat", ok("#/langit/html/abc", "html", null) && ok("#/langit/html?x=1", "html", null), "ekor yang bukan angka diabaikan");
  // persen-sandi rusak: sebelum penjaga, `decodeURIComponent` melempar URIError di
  // dalam useEffect dan SELURUH pohon React mati (#akar tanpa anak)
  for (const h of ["#/langit/%", "#/langit/%E0%A4%A", "#/langit/%E0%A4%A/3", "#/langit/%FF", "#/langit/%C0%AF/1", "#/langit/100%"]) {
    let r, melempar = false;
    try { r = bacaAlamat(h); } catch { melempar = true; }
    aku("alamat", !melempar && r === null, `${h} harus null tanpa melempar`);
  }
  aku("alamat", ok("#/langit/%68tml/2", "html", 2), "persen-sandi sah didekode");
  // Nomor bintang: bilangan bulat utuh. `\d+` tanpa penjaga menelan angka
  // depan `1.5` dan `1e3` sebagai bintang 2; ekor seperti itu diabaikan.
  aku("alamat", ok("#/langit/html/1.5", "html", null) && ok("#/langit/html/1e3", "html", null) && ok("#/langit/html/12abc", "html", null) && ok("#/langit/html/0.5", "html", null), "nomor bukan bilangan bulat diabaikan");
  aku("alamat", ok("#/langit/html/3/", "html", 3) && ok("#/langit/html/3?x=1", "html", 3) && ok("#/langit/html/3#x", "html", 3) && ok("#/langit/html/007", "html", 7), "bilangan bulat utuh tetap dibaca");
  const r = acak(20261027);
  const abjad = ["%", "/", "#", "a", "0", "9", "E", "4", "%E0%A4", "%41", "?", "-"];
  for (let n = 0; n < 3000; n++) {
    let h = "#/langit/";
    for (let k = Math.floor(r() * 8); k >= 0; k--) h += abjad[Math.floor(r() * abjad.length)];
    let melempar = false;
    try { bacaAlamat(h); } catch { melempar = true; }
    aku("alamat", !melempar, `bacaAlamat melempar untuk ${JSON.stringify(h)}`);
  }
}

/* ------------------------------------------------------------------- gulir */

{
  // Benda yang muat: sesudah digulir, tampak penuh di antara bawah pil + celah dan tinggi layar - celah.
  const r = acak(20261028);
  let kasus = 0;
  for (let n = 0; n < 4000; n++) {
    const tinggi = 360 + Math.floor(r() * 700);
    const rel = Math.floor(r() * 90);
    const tb = 20 + Math.floor(r() * 60);
    const atas = Math.floor(r() * (tinggi + 600)) - 300;
    const d = deltaGulirTampak(atas, atas + tb, tinggi, rel);
    const a2 = atas - d, b2 = atas + tb - d;
    const lo = rel + CELAH_GULIR, hi = tinggi - CELAH_GULIR;
    kasus++;
    aku("gulir", a2 >= lo - 1e-9 && b2 <= hi + 1e-9, `benda ${atas}+${tb} @${tinggi}/${rel}: ${a2}..${b2} di luar [${lo}, ${hi}]`);
    aku("gulir", deltaGulirTampak(a2, b2, tinggi, rel) === 0, `gulir tidak idempoten ${atas}+${tb} @${tinggi}/${rel}`);
    const tampak = atas >= lo && atas + tb <= hi;
    aku("gulir", (d === 0) === tampak, `d=${d} padahal tampak=${tampak} (${atas}+${tb} @${tinggi}/${rel})`);
    aku("gulir", d === 0 || (atas < lo ? d < 0 : d > 0), `arah gulir salah ${atas}+${tb} @${tinggi}/${rel}`);
  }
  // Benda lebih tinggi daripada ruang: tepi atasnya disejajarkan.
  aku("gulir", deltaGulirTampak(500, 1200, 600, 66) === 500 - (66 + CELAH_GULIR), "benda terlalu tinggi: sejajarkan tepi atas");
  // Judul panel: sesudah digulir tampak; tepi atas panel tidak di atas bawah pil.
  for (let n = 0; n < 4000; n++) {
    const tinggi = 360 + Math.floor(r() * 700);
    const rel = Math.floor(r() * 90);
    const atas = Math.floor(r() * (tinggi + 900)) - 200;
    const bawahJudul = atas + 28;
    const d = deltaGulirPanel(atas, bawahJudul, tinggi, rel);
    kasus++;
    const tampak = atas >= rel + CELAH_GULIR && bawahJudul <= tinggi - CELAH_GULIR;
    aku("gulir", (d === 0) === tampak, `panel: d=${d} padahal tampak=${tampak} (${atas} @${tinggi}/${rel})`);
    aku("gulir", deltaGulirPanel(atas - d, bawahJudul - d, tinggi, rel) === 0, `panel: judul tidak tampak sesudah gulir (${atas} @${tinggi}/${rel})`);
    aku("gulir", d === 0 || Math.abs(atas - d - Math.max(rel + CELAH_GULIR, LETAK_PANEL * tinggi)) < 1e-9, `panel: tepi atas panel bukan di ${LETAK_PANEL} tinggi layar (${atas} @${tinggi}/${rel})`);
  }
  // Bintang terpilih tetap tampak sesudah menggulir ke judul panel: kanvas ada di
  // atas panel, dan gulir ke judul mendorong bintang di bagian atas kanvas ke
  // bawah pil atas (terukur di peramban: 4 dari 12 klik di 320x568 sampai
  // 952x600). Gulir hanya dikurangi, tidak pernah dibalik atau ditambah.
  let dibatasi = 0;
  for (let n = 0; n < 4000; n++) {
    const tinggi = 360 + Math.floor(r() * 700);
    const rel = Math.floor(r() * 90);
    const lo = rel + CELAH_GULIR;
    const atas = Math.floor(r() * (tinggi + 900)) - 200;
    const bintangAtas = lo + Math.floor(r() * (tinggi - 2 * CELAH_GULIR - rel - 20));
    const bebas = deltaGulirPanel(atas, atas + 28, tinggi, rel);
    const d = deltaGulirPanel(atas, atas + 28, tinggi, rel, CELAH_GULIR, bintangAtas);
    kasus++;
    aku("gulir", bintangAtas - d >= lo - 1e-9, `bintang terpilih keluar: atas ${bintangAtas} gulir ${d} (panel ${atas} @${tinggi}/${rel})`);
    aku("gulir", d <= bebas + 1e-9 && (d === bebas || bintangAtas - bebas < lo), `batas bintang menambah gulir atau menggulir tanpa perlu (${bebas} lalu ${d})`);
    if (d !== bebas) dibatasi += 1;
  }
  aku("gulir", dibatasi >= 300, `batas bintang hampir tidak pernah bekerja di korpus (${dibatasi} dari 4000)`);
  aku("gulir", deltaGulirPanel(760, 800, 600, 66, CELAH_GULIR, 80) === 80 - (66 + CELAH_GULIR), "kasus nyata 952x600: bintang di y=80, gulir cuma sampai bintang di bawah pil");
  aku("gulir", deltaGulirPanel(760, 800, 600, 66, CELAH_GULIR, 700) === deltaGulirPanel(760, 800, 600, 66), "bintang jauh dari pil: gulir tidak dibatasi");
  aku("gulir", kasus >= 12000, "korpus gulir menyusut");
  // Tinggi pakai laptop yang nyata: panel di bawah kanvas (y 760) pada layar 452 dan 384.
  aku("gulir", deltaGulirPanel(760, 800, 452, 66) > 0 && deltaGulirPanel(760, 800, 384, 66) > 0, "layar pendek: judul panel di bawah lipatan digulir ke atas");
}

/* ----------------------------------------------------------- label rasi dst */

{
  const bahasa = KURIKULUM.map((k) => bahasaDari(k, PROFIL[1]));
  let n = 0;
  for (const b of bahasa) {
    const selesai = b.materi.filter((m) => m.status === "selesai").length;
    const jumlah = b.materi.length;
    for (const [konsep, cocok, profesi, bekal] of [[null, 0, null, false], ["Perulangan", 3, null, false], ["Perulangan", 0, null, false], [null, 0, "Frontend Developer", true], [null, 0, "Frontend Developer", false], ["Fungsi", 12, "Data Analyst", true]]) {
      n++;
      const t = labelRasi({ label: b.label, selesai, jumlah, konsep, cocok, profesi, bekal });
      aku("label", t.startsWith(`${b.label} ${selesai}/${jumlah}: ${selesai} dari ${jumlah} materi sudah dibaca`), `labelRasi dasar ${b.key}: ${t}`);
      aku("label", t.endsWith(". Perbesar rasi."), `labelRasi penutup ${b.key}`);
      aku("label", t.includes(`, ${cocok} materi cocok dengan ${konsep}`) === (konsep !== null && cocok > 0), `labelRasi konsep ${b.key}: ${t}`);
      aku("label", t.includes(`, bagian bekal ${profesi}`) === (profesi !== null && bekal), `labelRasi profesi ${b.key}: ${t}`);
    }
  }
  aku("label", n >= 190, "korpus labelRasi menyusut");
  // saringan yang menyala MENGUBAH nama tautan (dulu 0 dari 32 berubah)
  const polos = bahasa.map((b) => labelRasi({ label: b.label, selesai: 0, jumlah: b.materi.length, konsep: null, cocok: 0, profesi: null, bekal: false }));
  const [nama, pola] = KONSEP.find(([x]) => x === "Perulangan");
  const hitung = bahasa.map((b) => b.materi.filter((m) => pola.test(m.judul.replace(/^\s*\d+\.\s*/, ""))).length);
  const dgnKonsep = bahasa.map((b, i) => labelRasi({ label: b.label, selesai: 0, jumlah: b.materi.length, konsep: nama, cocok: hitung[i], profesi: null, bekal: false }));
  aku("label", dgnKonsep.filter((t, i) => t !== polos[i]).length === hitung.filter((c) => c > 0).length && hitung.filter((c) => c > 0).length >= 10, "nama tautan berubah tepat pada rasi yang punya kecocokan");
  // kalimat `role=status`
  const ks = kalimatDipilih({ judul: "12. Fungsi", status: "baru" });
  aku("label", ks === "Dipilih: Fungsi, belum dibaca.", `kalimat dipilih biasa: ${ks}`);
  const kt = kalimatDipilih({ judul: "12. Fungsi", status: "terkunci", alasan: "Baca 4 materi lagi di Bab 1." });
  aku("label", kt === "Dipilih: Fungsi, masih terkunci. Baca 4 materi lagi di Bab 1.", `kalimat dipilih terkunci: ${kt}`);
  aku("label", kalimatDipilih({ judul: "1. A", status: "selesai", alasan: "tidak boleh ikut" }) === "Dipilih: A, sudah dibaca.", "alasan hanya untuk bintang terkunci");
  aku("label", kalimatDipilih({ judul: "1. A", status: "terkunci", alasan: null }) === "Dipilih: A, masih terkunci.", "terkunci tanpa alasan (belum tiba)");
  // backtick di paragraf pembuka: dipecah jadi bagian biasa dan kode
  const pk = (t) => pecahKode(t);
  aku("label", JSON.stringify(pk("Fungsi di Rust ditulis pakai kata `fn`.")) === JSON.stringify([{ teks: "Fungsi di Rust ditulis pakai kata ", kode: false }, { teks: "fn", kode: true }, { teks: ".", kode: false }]), "pecahKode: satu pasang");
  aku("label", pk("tanpa kode").length === 1 && !pk("tanpa kode")[0].kode, "pecahKode: tanpa backtick");
  aku("label", pk("a `b").every((x) => !x.kode && !x.teks.includes("`")), "pecahKode: backtick tanpa pasangan dibuang, bukan dicetak");
  for (const t of ["`a` dan `b`", "`a``b`", "``", "x`y`z`w", "`", "", "`kode`"]) {
    const p = pk(t);
    aku("label", p.map((x) => x.teks).join("") === t.replaceAll("`", "") && p.every((x) => !x.teks.includes("`")), `pecahKode menghilangkan teks: ${JSON.stringify(t)}`);
  }
}

/* ------------------------------------------------------------------- skala */

{
  const bahasa = KURIKULUM.map((k) => bahasaDari(k, PROFIL[1]));
  const kosong = KURIKULUM.map((k) => bahasaDari(k, PROFIL[0]));
  // 1 persis lensa lama (bukan "kira-kira")
  for (const b of [bahasa[0], bahasa[5], bahasa[20]]) {
    const o = { lebar: 902, tinggi: 542, tepiX: 72, tepiY: 54 };
    const a = bangunLensa(b.materi, b.bab, b.key, o);
    const c = bangunLensa(b.materi, b.bab, b.key, { ...o, skalaTeks: 1 });
    aku("skala", JSON.stringify(a) === JSON.stringify(c), `skalaTeks 1 berbeda dari bawaan ${b.key}`);
  }
  // lencana ikut membesar, nomor ikut membesar, tidak keluar kanvas dan tidak menimpa berlebihan
  for (const [lb, tg] of [[1441, 678], [902, 542]]) {
    for (const sk of [1.25, 1.5]) {
      let menimpa = 0, total = 0, tindih = 0;
      for (const b of [...bahasa, ...kosong]) {
        const lens = bangunLensa(b.materi, b.bab, b.key, { lebar: lb, tinggi: tg, tepiX: 72, tepiY: 54, skalaTeks: sk });
        aku("skala", lens.tumpang.keluar === 0, `label keluar kanvas ${b.key} @${lb}x${tg} skala ${sk}`);
        const pil = lens.bab.filter((p) => p.awal >= 0);
        aku("skala", pil.every((p) => p.h === 22 * sk && Math.abs(p.w - (romawi(p.nomor).length * 9 + 16) * sk) < 1e-9), `lencana bab tidak diskalakan ${b.key} @${sk}`);
        aku("skala", lens.berikut === null || (lens.berikut.w === 82 * sk && lens.berikut.h === 22 * sk), `lencana berikutnya tidak diskalakan ${b.key} @${sk}`);
        const kot = lens.bintang.map((s) => {
          const w = (String(s.i + 1).length * 6.8 + 3) * sk;
          const x0 = s.label.jangkar === "start" ? s.label.x : s.label.jangkar === "end" ? s.label.x - w : s.label.x - w / 2;
          return { x0, x1: x0 + w, y0: s.label.y - 7 * sk, y1: s.label.y + 7 * sk };
        });
        aku("skala", kot.every((k) => k.x0 >= -1 && k.x1 <= lb + 1 && k.y0 >= -1 && k.y1 <= tg + 1), `nomor keluar kanvas ${b.key} @${lb}x${tg} skala ${sk}`);
        kot.forEach((k, i) => {
          const bukan = lens.bintang.some((s, j) => j !== i && k.x0 < s.x + s.r && k.x1 > s.x - s.r && k.y0 < s.y + s.r && k.y1 > s.y - s.r);
          const lain = kot.some((o, j) => j > i && beririsanKotak(k, o));
          if (bukan || lain) menimpa += 1;
          total += 1;
        });
        const semua = lens.bab.filter((p) => p.awal >= 0).map(kotakPil);
        if (lens.berikut) semua.push(kotakPil(lens.berikut));
        for (let i = 0; i < semua.length; i++) for (let j = i + 1; j < semua.length; j++) if (beririsanKotak(semua[i], semua[j])) tindih += 1;
      }
      // Terukur: nomor menimpa 0,2-1,1 persen pada skala 1,25 dan <= 1,6 pada 1,5
      // (kanvas 902 x 542); lencana saling menimpa paling banyak 4 dari 64 lensa.
      aku("skala", menimpa <= 0.025 * total, `nomor menimpa ${menimpa}/${total} @${lb}x${tg} skala ${sk} (> 2,5 persen)`);
      aku("skala", tindih <= 8, `lencana saling menimpa ${tindih} @${lb}x${tg} skala ${sk}`);
    }
  }
  aku("skala", JSON.stringify(bangunLensa(bahasa[0].materi, bahasa[0].bab, "x", { lebar: 902, tinggi: 542, tepiX: 72, tepiY: 54, skalaTeks: 0.2 }))
      === JSON.stringify(bangunLensa(bahasa[0].materi, bahasa[0].bab, "x", { lebar: 902, tinggi: 542, tepiX: 72, tepiY: 54 })), "skalaTeks di bawah 1 dijepit ke 1");
}

/* -------------------------------------------------------------------- glif */

{
  const sidik = new Set();
  for (const st of URUTAN_STATUS) {
    const g = bagianGlif(st, 100, 50, 8);
    const d = [g.isi, g.tepi].filter(Boolean).join("");
    sidik.add(d);
    aku("glif", d.startsWith("M") && !/NaN|undefined|Infinity/.test(d), `path ${st} rusak`);
    aku("glif", !/transform/i.test(d), `path ${st} memuat transform`);
    // semua koordinat mutlak dalam kotak r di sekitar pusat (+1 untuk busur)
    const angka = [...d.matchAll(/-?\d+\.\d+/g)].map((m) => Number(m[0]));
    aku("glif", angka.length > 0, `path ${st} tanpa angka`);
  }
  aku("glif", sidik.size === 4, "empat status harus empat bentuk berbeda");
  const sel = bagianGlif("selesai", 0, 0, 10).isi;
  aku("glif", (sel.match(/L/g) ?? []).length === 7, "percik: delapan titik (satu M, tujuh L)");
  aku("glif", bagianGlif("sebagian", 0, 0, 5).isi !== undefined && bagianGlif("sebagian", 0, 0, 5).tepi !== undefined, "sebagian: isi dan tepi");
  aku("glif", bagianGlif("baru", 0, 0, 5).isi === undefined, "baru: hanya tepi");
  aku("glif", bagianGlif("terkunci", 0, 0, 5).tepi === undefined, "terkunci: hanya isi");
  aku("glif", pathBraket(10, 10, 8, 4).startsWith("M") && (pathBraket(10, 10, 8, 4).match(/M/g) ?? []).length === 4, "braket empat sudut");
  aku("glif", statusBintang({ judul: "", status: "baru", terkunci: true }) === "terkunci", "terkunci menang atas baru");
  aku("glif", jariIkhtisar("selesai", 100) === JARI_PX.selesai && jariIkhtisar("selesai", 4) < JARI_PX.selesai, "jari dibatasi tetangga");
}

/* ----------------------------------------------------------------- wilayah */

{
  const segi = [[0, 0], [10, 0], [5, 5], [10, 10], [0, 10]];
  aku("wilayah", selubungCembung(segi).length === 4, "selubung membuang titik dalam");
  aku("wilayah", pathWilayah(segi, 8).startsWith("M") && pathWilayah(segi, 8).endsWith("Z"), "path wilayah tertutup");
  const poli = wilayahPoligon(segi, 8);
  aku("wilayah", titikDiPoligon(poli, 5, 5) && titikDiPoligon(poli, -5, 5) && !titikDiPoligon(poli, -12, 5), "pengembangan wilayah");
  // Poligon CEKUNG: untuk poligon cembung, menghitung persilangan ke kiri atau ke
  // kanan memberi jawaban sama, jadi sel mutasi yang membalik sisinya lolos.
  const L = [[0, 0], [10, 0], [10, 4], [4, 4], [4, 10], [0, 10]];
  aku("wilayah", titikDiPoligon(L, 2, 7) && titikDiPoligon(L, 7, 2) && !titikDiPoligon(L, 7, 7) && !titikDiPoligon(L, -1, 5), "poligon cekung");
  aku("wilayah", wilayahPoligon([[1, 1]], 8).length === 1 && pathWilayah([[1, 1]], 8).startsWith("M"), "satu titik");
}

/* ----------------------------------------------------------------- pembuka */

{
  const rekaman = JSON.parse(readFileSync(path.join(SINI, "golden-pembuka.json"), "utf-8"));
  // Melempar dihitung sebagai selisih berkategori, bukan menghentikan skrip:
  // sel mutasi menagih kategorinya, dan tumpukan galat tidak membuktikan apa pun.
  const aman = (fn) => { try { return fn(); } catch (e) { return `melempar ${e.message}`; } };
  for (const k of rekaman) {
    const bagian = [{ jenis: k.jenis, blok: k.jenis === "prosa" ? k.blok : null }];
    aku("pembuka", aman(() => ringkasPembuka(bagian)) === k.ringkas, `${k.k} [${k.cabang.join(",")}]`);
  }
  // Paragraf pembuka kosong tidak boleh melempar di tengah render (tidak ada
  // error boundary): teks kosong, hanya spasi, medan `teks` hilang, blok bukan teks.
  for (const [nama, blok] of [["teks kosong", [{ jenis: "teks", teks: "", peran: "" }]], ["teks spasi", [{ jenis: "teks", teks: " \n  ", peran: "" }]],
    ["tanpa medan teks", [{ jenis: "teks", peran: "" }]]]) {
    aku("pembuka", aman(() => ringkasPembuka([{ jenis: "prosa", blok }])) === null, `paragraf pembuka ${nama} harus null tanpa melempar`);
  }
  aku("pembuka", ringkasPembuka(null) === null && ringkasPembuka([]) === null, "tanpa bagian");
  aku("pembuka", ringkasPembuka([{ jenis: "kode", blok: null }]) === null, "bagian pertama kode");
  aku("pembuka", kataAksiBaca("baru") === "Mulai membaca" && kataAksiBaca("sebagian") === "Lanjutkan membaca"
      && kataAksiBaca("selesai") === "Baca lagi" && kataAksiBaca("terkunci") === null, "kata aksi");
  const h = hitungBab([{ status: "selesai" }, { status: "sebagian" }, { status: "baru" }, { status: "selesai" }], [0, 1, 3]);
  aku("pembuka", h.selesai === 2 && h.jumlah === 3 && h.persen === 67, "sebagian tidak dihitung selesai");
  if (rekaman.length < 90) {
    console.error(`REKAMAN PEMBUKA MENGECIL: ${rekaman.length} kasus.`);
    process.exit(1);
  }
}

/* ------------------------------------------------------------------- label */

{
  const KATA = { selesai: "sudah dibaca", sebagian: "dibaca sebagian", baru: "belum dibaca", terkunci: "masih terkunci" };
  const bahasa = KURIKULUM.map((k) => bahasaDari(k, PROFIL[1]));
  let n = 0;
  for (const b of bahasa) {
    const ib = b.materi.findIndex((m) => m.status !== "selesai" && !m.terkunci);
    b.materi.forEach((m, i) => {
      n++;
      const st = statusBintang(m);
      const biasa = labelBintang({ indeks: i, judul: m.judul, status: st, berikutnya: i === ib, konsepCocok: null });
      const cocok = labelBintang({ indeks: i, judul: m.judul, status: st, berikutnya: false, konsepCocok: "Perulangan" });
      const judul = m.judul.replace(/^\s*\d+\.\s*/, "");
      aku("label", biasa.startsWith(`${i + 1}. ${judul}, ${KATA[st]}`), `nama bintang ${b.key}#${i}: ${biasa}`);
      aku("label", biasa.endsWith(", berikutnya") === (i === ib), `'berikutnya' hanya pada bintang berbraket ${b.key}#${i}`);
      aku("label", !biasa.includes("cocok dengan") && cocok.endsWith(", cocok dengan Perulangan") && !cocok.includes("berikutnya"), `'cocok dengan' hanya bila cincinnya digambar ${b.key}#${i}`);
    });
  }
  aku("label", n >= 1062, "korpus label menyusut");
  // Kata kapsul "mulai di sini" dari status bintang sasarannya, bukan dari XP.
  aku("label", kataMulai("sebagian") === "Lanjutkan di sini" && kataMulai("baru") === "Mulai di sini" && kataMulai("selesai") === "Mulai di sini", "kata kapsul menurut status bintang sasaran");
}

/* ------------------------------------------------------------------ bentuk */

{
  const ada = { bahasa: KURIKULUM.map((k) => bahasaDari(k, PROFIL[1])), profesi: [{ id: "frontend", nama: "Frontend", bekal: [["html"], ["css", "javascript"]] }], tujuan: "" };
  aku("bentuk", bentukJawabanSah(ada) && bentukJawabanSah({ ...ada, tujuan: undefined }) && bentukJawabanSah({ ...ada, ekstra: 1 }), "jawaban sungguhan lolos");
  aku("bentuk", bentukJawabanSah({ bahasa: [], profesi: [] }), "daftar kosong tetap bentuk sah");
  const rusak = [
    ["null", null], ["angka", 7], ["daftar", []], ["objek kosong", {}], ["bahasa objek", { ...ada, bahasa: {} }], ["tanpa profesi", { bahasa: ada.bahasa }],
    ["bahasa tanpa materi", { ...ada, bahasa: [{ key: "a", label: "A" }] }], ["materi bukan objek", { ...ada, bahasa: [{ key: "a", label: "A", materi: [1] }] }],
    ["materi tanpa status", { ...ada, bahasa: [{ key: "a", label: "A", materi: [{ judul: "x" }] }] }], ["kunci bukan teks", { ...ada, bahasa: [{ key: 7, label: "A", materi: [] }] }],
    ["bab rusak", { ...ada, bahasa: [{ key: "a", label: "A", materi: [], bab: [{ nomor: "1", judul: "x", materi: [] }] }] }],
    ["bab bukan daftar", { ...ada, bahasa: [{ key: "a", label: "A", materi: [], bab: {} }] }],
    ["indeks bab bukan angka", { ...ada, bahasa: [{ key: "a", label: "A", materi: [], bab: [{ nomor: 1, judul: "x", materi: ["0"] }] }] }],
    ["profesi tanpa bekal", { ...ada, profesi: [{ id: "a", nama: "A" }] }], ["bekal bukan kelompok", { ...ada, profesi: [{ id: "a", nama: "A", bekal: ["html"] }] }],
    ["tujuan bukan teks", { ...ada, tujuan: 5 }],
  ];
  for (const [nama, d] of rusak) {
    let hasil;
    try { hasil = bentukJawabanSah(d); } catch (e) { hasil = `melempar ${e.message}`; }
    aku("bentuk", hasil === false, `bentuk rusak (${nama}) harus ditolak tanpa melempar: ${hasil}`);
  }
}

/* ---------------------------------------------------------------- kontrak */

// Angka kontrak ditulis LITERAL: pembanding yang membaca konstanta dari modul
// yang diujinya tidak menangkap mutan yang menggeser konstanta itu.
{
  const sama = (a, b) => JSON.stringify(a) === JSON.stringify(b);
  aku("kontrak", sama(JARI_PX, { selesai: 4.6, sebagian: 4, baru: 3.7, terkunci: 2.4 }), "JARI_PX");
  aku("kontrak", sama(JARI_LENSA_PX, { selesai: 10, sebagian: 8, baru: 7.5, terkunci: 6 }), "JARI_LENSA_PX");
  aku("kontrak", JANGKAU_LENSA_PX === 22 && JANGKAU_BINTANG_PX === 14, "jangkauan sasaran");
  aku("kontrak", LEBAR_TIP_MAKS === 260 && TINGGI_TIP_MAKS === 64 && CELAH_TIP === 4 && KORIDOR_TIP_PX === 8 && LEBAR_KANVAS_TIP_MIN === 560, "ukuran kartu judul");
  // Lencana: teks 12 px. Bab = 9 px per huruf + 16 lebar, tinggi 22; "berikutnya" 82 x 22.
  const py = KURIKULUM.find((k) => k.key === "python");
  const pb = bahasaDari(py, PROFIL[1]);
  const lens = bangunLensa(pb.materi, pb.bab, pb.key, { lebar: 902, tinggi: 542, tepiX: 72, tepiY: 54 });
  const pil = lens.bab.filter((x) => x.awal >= 0);
  aku("kontrak", pil.length > 5 && pil.every((x) => x.h === 22 && x.w === romawi(x.nomor).length * 9 + 16), "lencana bab 9 px per huruf + 16, tinggi 22");
  aku("kontrak", lens.berikut !== null && lens.berikut.w === 82 && lens.berikut.h === 22, "lencana berikutnya 82 x 22");
  // Gulir: napas 8 px dan panel di 40 persen tinggi layar, juga LITERAL (properti
  // gulir di atas memakai konstanta dari modulnya, jadi ia tidak menangkap
  // mutan yang menggeser konstanta itu).
  aku("kontrak", CELAH_GULIR === 8 && LETAK_PANEL === 0.4, "celah gulir 8 px, panel di 40 persen tinggi layar");
}

/* --------------------------------------------------------------------- tip */

{
  // Ukuran kanvas lensa yang sungguh terjadi (1905, 1536, 1440, 1366, 1280, ditumpuk 1000) dan 390.
  const KANVAS_TIP = [[1441, 678], [1072, 638], [976, 674], [902, 542], [816, 494], [936, 496], [366, 523]];
  let kartuTertutup = 0;
  const bahasa = KURIKULUM.map((k) => bahasaDari(k, PROFIL[1]));
  for (const [lb, tg] of KANVAS_TIP) {
    for (const b of bahasa) {
      const lens = bangunLensa(b.materi, b.bab, b.key, { lebar: lb, tinggi: tg, tepiX: lb > 600 ? 72 : 30, tepiY: 54 });
      if (lb < 560) {
        aku("tip", lens.bintang.every((s) => tempatTip(s, lb, tg) === null), `kanvas ${lb}: tanpa kartu`);
        continue;
      }
      for (const s of lens.bintang) {
        const t = tempatTip(s, lb, tg);
        aku("tip", t !== null, `kanvas ${lb}: kartu ada ${b.key}#${s.i}`);
        if (t === null) continue;
        aku("tip", t.kiri >= 4 - 1e-6 && t.kiri + 260 <= lb - 4 + 1e-6 && t.atas >= 4 - 1e-6 && t.atas + 64 <= tg - 4 + 1e-6, `kartu keluar kanvas ${b.key}#${s.i} @${lb}`);
        aku("tip", s.y >= t.atas && s.y <= t.atas + 64, `bintang di luar rentang tegak kartu ${b.key}#${s.i} @${lb}`);
        const tepi = t.sisi === "kanan" ? t.kiri : t.kiri + 260;
        aku("tip", Math.abs(tepi - s.x) <= 20, `sisi dekat kartu > 20 px dari bintang ${b.key}#${s.i} @${lb}: ${Math.abs(tepi - s.x)}`);
        // jalan lurus pusat bintang -> tengah kartu (2 px/langkah): sorot bertahan,
        // kecuali penunjuk melewati glif bintang lain (jari-jari + 3 px).
        const cx = t.kiri + (t.sisi === "kanan" ? 60 : 200), cy = t.atas + 32;
        const dx = cx - s.x, dy = cy - s.y, langkah = Math.max(1, Math.round(Math.hypot(dx, dy) / 2));
        let bertahan = s, putus = false;
        for (let k = 1; k <= langkah && !putus; k++) {
          const px = s.x + (dx * k) / langkah, py = s.y + (dy * k) / langkah;
          if (px >= t.kiri && px <= t.kiri + 260 && py >= t.atas && py <= t.atas + 64) break;
          const di = pilihSorotLensa(bertahan, sasaranLensa(lens, px, py), px, py, lb, tg);
          if (di && di.i !== s.i && Math.hypot(di.x - px, di.y - py) <= di.r + 3) break;
          if (!di || di.i !== s.i) { aku("tip", false, `kartu berganti di tengah jalan ${b.key}#${s.i} @${lb} langkah ${k}`); putus = true; }
          else bertahan = di;
        }
        // Kartu hover menangkap penunjuk: bintang yang pusatnya di bawahnya hanya
        // bisa disorot dan diklik kalau kartu meneruskannya. Persegi kartu
        // ukuran penempatan (260 x 64) melingkupi kartu yang sungguh tergambar.
        const kx1 = t.kiri + 260, ky1 = t.atas + 64;
        for (const o of lens.bintang) {
          if (o.i === s.i || o.x < t.kiri || o.x > kx1 || o.y < t.atas || o.y > ky1) continue;
          const di = bintangDiBawahKartu(lens, s.i, o.x, o.y);
          aku("kartu", di !== null && di.i === o.i, `bintang ${b.key}#${o.i} tertutup kartu #${s.i} @${lb} dan tidak terjangkau`);
          kartuTertutup += 1;
        }
        // invarian di titik mana pun pada kartu: tidak pernah bintang yang sedang disorot,
        // selalu dalam jangkauan glifnya, dan null hanya bila tak ada glif lain di bawahnya
        for (let n = 0; n < 4; n++) {
          const px = t.kiri + ((n * 61 + s.i * 17) % 260), py = t.atas + ((n * 23 + s.i * 7) % 64);
          const di = bintangDiBawahKartu(lens, s.i, px, py);
          const ada = lens.bintang.filter((o) => o.i !== s.i && (o.x - px) ** 2 + (o.y - py) ** 2 <= (o.r + 3) ** 2);
          aku("kartu", (di === null) === (ada.length === 0) && (di === null || (di.i !== s.i && ada.includes(di))), `kartu #${s.i} di ${px.toFixed(0)},${py.toFixed(0)} salah pilih`);
        }
        // bintang yang terhimpit di dalam koridor bintang lain tetap bisa dicapai
        const x0 = Math.min(s.x, tepi), x1 = Math.max(s.x, tepi), lk = Math.max(s.r, 8);
        for (const o of lens.bintang) {
          if (o.i === s.i || o.x < x0 || o.x > x1 || Math.abs(o.y - s.y) > lk) continue;
          const di = pilihSorotLensa(s, o, o.x, o.y, lb, tg);
          aku("tip", di !== null && di.i === o.i, `bintang ${b.key}#${o.i} tak terjangkau dari koridor #${s.i} @${lb}`);
        }
      }
    }
  }
  aku("kartu", kartuTertutup >= 1000, `korpus kartu menyusut: hanya ${kartuTertutup} bintang tertutup kartu`);
  // Tiga glif yang saling menimpa (jarak 4 dan 8 px): terdekat menang, dan bintang
  // yang sedang disorot tidak pernah dipilih lagi lewat kartunya sendiri.
  const rapat = { bintang: [{ i: 0, x: 100, y: 100, r: 6 }, { i: 1, x: 108, y: 100, r: 6 }, { i: 2, x: 104, y: 100, r: 6 }] };
  aku("kartu", bintangDiBawahKartu(rapat, 5, 107.5, 100)?.i === 1, "bintang terdekat menang di antara glif yang saling menimpa");
  aku("kartu", bintangDiBawahKartu(rapat, 1, 107.5, 100)?.i === 2, "bintang yang sedang disorot tidak ikut dipilih");
  aku("kartu", bintangDiBawahKartu(rapat, 5, 160, 100) === null, "di luar semua glif: tidak ada yang dipilih");
}

console.log(
  `${cacah} perbandingan atas ${KURIKULUM.length} kurikulum x ${PROFIL.length} profil ` +
    `x ${SKALA.length} skala (${totalBintang} bintang di ikhtisar) dan ${KANVAS.length} ukuran kanvas`,
);
if (gagal) {
  console.error(`GAGAL: ${gagal} perbandingan berbeda ${JSON.stringify(keluhan)}`);
  process.exit(1);
}
console.log("COCOK: geometri ikhtisar dan lensa memenuhi semua sifat.");
