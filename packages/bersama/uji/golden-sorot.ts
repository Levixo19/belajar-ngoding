/* Adu pemindai TypeScript dengan rekaman yang dihasilkan Python.
 *
 * Ini pengganti tes diferensial `test_web.TestPenyorotJavaScript`. Yang lama
 * mengadu dua implementasi yang berjalan bersamaan; yang ini mengadu satu
 * implementasi dengan keluaran yang sudah DISEPAKATI, direkam sebelum berkas
 * ini ada. Bedanya penting: rekaman tidak bisa "ikut salah". Kalau keduanya
 * diubah bersamaan, tes diferensial tetap hijau -- rekaman tidak.
 *
 * Korpusnya tidak diketik di sini dan tidak diambil dari server: ia dibangun
 * ulang dari `packages/konten/kurikulum/*.json`, berkas yang sama yang dibaca
 * React nanti. Jadi kalau ekspor kontennya rusak, tes ini yang pertama tahu.
 *
 *     node uji/golden-sorot.ts
 *
 * Keluar 0 kalau semua sidik cocok, 1 kalau ada yang bergeser.
 */

import { createHash } from "node:crypto";
import { readFileSync, readdirSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

import { bahasaDikenal, namaPenyorot, token, type Token } from "../src/sorot.ts";

const SINI = path.dirname(fileURLToPath(import.meta.url));
const PAKET = path.resolve(SINI, "..");
const AKAR = path.resolve(PAKET, "..", "..");
const KONTEN = path.join(AKAR, "packages", "konten");
const GOLDEN = path.join(PAKET, "golden");

interface Bagian {
  code?: string;
  bahasa?: string;
}
interface Materi {
  title: string;
  sections: Bagian[];
}
interface Latihan {
  title: string;
  solution?: string;
}
interface Kurikulum {
  key: string;
  runner: string;
  materi: Materi[];
  latihan: Latihan[];
}
interface KasusGolden {
  nama: string;
  bahasa: string;
  sha256: string;
}

function muat<T>(...bagian: string[]): T {
  return JSON.parse(readFileSync(path.join(...bagian), "utf-8")) as T;
}

/**
 * Sidik yang WAJIB sama dengan `alat/golden_bersama.py:_sha`.
 *
 * `JSON.stringify` tanpa argumen kedua dan ketiga tidak pernah menyisipkan
 * spasi, dan sisi Python sudah disetel `separators=(",", ":")` supaya cocok.
 * Daftar token tidak memuat objek, jadi urutan kunci tidak jadi soal di sini.
 */
function sidik(nilai: Token[]): string {
  return createHash("sha256").update(JSON.stringify(nilai), "utf-8").digest("hex");
}

/**
 * Padanan `webapp/isi.py:bahasa_sorot` untuk sebuah entri kurikulum.
 *
 * Di Python syaratnya `lang["key"] in _BAHASA_SOROT`, dan `_BAHASA_SOROT`
 * ditulis persis `set(sorot.ATURAN)` -- jadi `bahasaDikenal` di sini bukan
 * tafsiran longgar melainkan predikat yang sama.
 */
function bahasaSorot(lang: Kurikulum): string {
  return bahasaDikenal(lang.key) ? lang.key : lang.runner;
}

/** Padanan `webapp/isi.py:bahasa_blok`, bagian penyorotnya saja. */
function bahasaBlok(bagian: Bagian, lang: Kurikulum): string {
  const sendiri = bagian.bahasa;
  if (!sendiri) return bahasaSorot(lang);
  return namaPenyorot(sendiri);
}

function korpus(): Array<{ nama: string; bahasa: string; kode: string }> {
  const keluar: Array<{ nama: string; bahasa: string; kode: string }> = [];
  const berkas = readdirSync(path.join(KONTEN, "kurikulum")).sort();
  for (const nama of berkas) {
    const lang = muat<Kurikulum>(KONTEN, "kurikulum", nama);
    for (const m of lang.materi) {
      m.sections.forEach((s, i) => {
        if (s.code) {
          keluar.push({
            nama: `${lang.key}/materi/${m.title}/${i}`,
            bahasa: bahasaBlok(s, lang),
            kode: s.code,
          });
        }
      });
    }
    const bhsLatihan = bahasaSorot(lang);
    for (const x of lang.latihan) {
      if (x.solution) {
        keluar.push({
          nama: `${lang.key}/latihan/${x.title}`,
          bahasa: bhsLatihan,
          kode: x.solution,
        });
      }
    }
  }
  return keluar;
}

function main(): number {
  const rekaman = muat<{ kasus: KasusGolden[] }>(GOLDEN, "sorot.json");
  const acuan = new Map(rekaman.kasus.map((k) => [k.nama, k]));
  const blok = korpus();

  // Populasi ditagih lebih dulu. Tanpa ini, korpus yang gagal dibangun
  // (direktori salah, ekspor kosong) membuat SEMUA perbandingan di bawah
  // lulus karena tidak ada yang dibandingkan -- bentuk kegagalan yang paling
  // meyakinkan, karena ia tampil sebagai keberhasilan.
  if (blok.length !== rekaman.kasus.length) {
    console.error(
      `POPULASI BEDA: korpus ${blok.length} blok, rekaman ` +
        `${rekaman.kasus.length}. Ekspor konten dan golden harus dari ` +
        `sumber yang sama; jalankan ulang keduanya.`,
    );
    return 1;
  }

  const bedaBahasa: string[] = [];
  const bedaToken: string[] = [];
  const takKetemu: string[] = [];
  let takUtuh = 0;

  for (const b of blok) {
    const a = acuan.get(b.nama);
    if (!a) {
      takKetemu.push(b.nama);
      continue;
    }
    if (a.bahasa !== b.bahasa) {
      bedaBahasa.push(`${b.nama}: rekaman ${a.bahasa}, di sini ${b.bahasa}`);
      continue;
    }
    const t = token(b.kode, b.bahasa);
    // Kontrak dasarnya diperiksa di sini juga, bukan cuma sidiknya: sebuah
    // pemindai bisa saja konsisten salah di kedua sisi, dan sidik yang cocok
    // tidak akan memberi tahu apa pun soal itu.
    if (t.map((p) => p[1]).join("") !== b.kode) takUtuh += 1;
    if (sidik(t) !== a.sha256) bedaToken.push(b.nama);
  }

  console.log(`korpus: ${blok.length} blok kode dari packages/konten/`);
  console.log(`rekaman: ${rekaman.kasus.length} kasus`);

  const lapor = (judul: string, daftar: string[]) => {
    if (!daftar.length) return;
    console.error(`${judul}: ${daftar.length}`);
    for (const d of daftar.slice(0, 10)) console.error(`  - ${d}`);
    if (daftar.length > 10) console.error(`  ... dan ${daftar.length - 10} lagi`);
  };

  lapor("nama tidak ada di rekaman", takKetemu);
  lapor("bahasa penyorot berbeda", bedaBahasa);
  lapor("sidik token bergeser", bedaToken);
  if (takUtuh) {
    console.error(
      `token tidak merekonstruksi sumbernya: ${takUtuh} blok. ` +
        `Ini kontrak yang paling dasar; sidik yang cocok tidak menebusnya.`,
    );
  }

  if (takKetemu.length || bedaBahasa.length || bedaToken.length || takUtuh) {
    return 1;
  }
  console.log("COCOK: pemindai TypeScript menghasilkan token identik dengan Python.");
  return 0;
}

process.exit(main());
