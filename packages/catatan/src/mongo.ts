/* Koleksi `catatan` di MongoDB, dan penyelarasnya dari berkas JSON.
 *
 * Mongo di sini INDEKS, bukan tempat tinggal. Yang disimpan salinan catatan
 * plus satu indeks teks di atasnya; yang hilang kalau containernya dibuang
 * cuma kemampuan mencari. Alasan lengkapnya di kepala `sumber.ts`.
 *
 * **Tanpa autentikasi, dan itu keputusan yang punya syaratnya.** Container-nya
 * dijalankan dengan `-p 127.0.0.1:27017:27017`, jadi ia cuma bisa dihubungi
 * dari mesin ini -- batas yang sama yang dipakai server Python
 * (`server.buat()` menolak host selain 127.0.0.1). Begitu bind-nya diubah ke
 * 0.0.0.0, syarat itu hilang dan autentikasi jadi WAJIB. Jangan mengubah
 * bind-nya tanpa menambahkan auth di saat yang sama.
 */

import { MongoClient, type Collection, type Db } from "mongodb";

import { bacaCatatan, jalurCatatan, type Catatan } from "./sumber.ts";

/** Satu dokumen di koleksi `catatan`. `_id` = kunci progres. */
export interface DokCatatan {
  _id: string;
  teks: string;
  diubah: string;
}

export const NAMA_DB = "belajar";
export const NAMA_KOLEKSI = "catatan";

/**
 * Alamat Mongo. Loopback, dan `directConnection` supaya driver tidak mencoba
 * menemukan replica set yang tidak ada -- tanpa itu, container satu simpul
 * membuat setiap permintaan menunggu sampai `serverSelectionTimeoutMS` habis.
 */
export function alamatMongo(): string {
  return (
    process.env["BELAJAR_MONGO_URL"] ||
    "mongodb://127.0.0.1:27017/?directConnection=true"
  );
}

/* Jangan menunggu lama-lama. Layanan ini TAMBAHAN: Mongo yang mati harus
   dilaporkan dalam sekejap sebagai "pencarian tidak tersedia", bukan ditunggu
   tiga puluh detik sambil membuat layar catatan terasa menggantung. */
const BATAS_PILIH_MS = 1500;

let klien: MongoClient | null = null;

/** Klien tunggal. Driver Mongo mengurus kolam koneksinya sendiri; membuat
 *  klien baru per permintaan berarti satu kolam baru per permintaan. */
export function klienMongo(): MongoClient {
  if (!klien) {
    klien = new MongoClient(alamatMongo(), {
      serverSelectionTimeoutMS: BATAS_PILIH_MS,
    });
  }
  return klien;
}

export async function tutupMongo(): Promise<void> {
  if (klien) {
    await klien.close();
    klien = null;
  }
}

export function koleksi(db: Db): Collection<DokCatatan> {
  return db.collection<DokCatatan>(NAMA_KOLEKSI);
}

/**
 * Pasang indeks teks. Idempoten: `createIndex` dengan spesifikasi yang sama
 * tidak melakukan apa pun pada pemanggilan kedua.
 *
 * **`default_language: "none"`, dan itu bukan kelalaian.** MongoDB punya
 * stemmer untuk lima belas bahasa dan Indonesia BUKAN salah satunya. Dua
 * pilihan yang ada, dan keduanya buruk kalau dipilih tanpa sadar:
 *
 * * `"english"` -- stemmer Inggris memotong akhiran Inggris. Di catatan
 *   berbahasa Indonesia ia memotong yang bukan akhiran: "sedang" kehilangan
 *   "ing"-nya, dan kata yang dicari berhenti cocok dengan dirinya sendiri.
 *   Daftar stop word-nya juga membuang kata Inggris yang di sini justru
 *   istilah teknis ("for", "in", "is").
 * * `"none"` -- tanpa stemming, tanpa stop word. Pencariannya jadi per KATA
 *   utuh: "pointer" menemukan "pointer" tapi tidak "pointers". Itu harga yang
 *   dibayar, dan ia jujur -- berbeda dengan stemming yang salah, yang gagal
 *   tanpa memberi tahu kenapa.
 *
 * Yang dipilih `"none"`. Kalau suatu hari pencarian per akar kata diperlukan,
 * tempatnya bukan di sini melainkan di pemotong kata yang tahu morfologi
 * Indonesia -- dan itu pekerjaan sendiri, bukan satu medan di `createIndex`.
 */
export async function pasangIndeks(db: Db): Promise<void> {
  await koleksi(db).createIndex(
    { teks: "text" },
    { name: "teks_text", default_language: "none" },
  );
}

/**
 * Selaraskan koleksi dengan berkas JSON. Mengembalikan apa yang berubah.
 *
 * Arahnya SATU: berkas -> Mongo. Tidak ada jalur sebaliknya, dan itu seluruh
 * alasan layanan ini aman dimatikan kapan saja.
 *
 * Kunci yang sudah TIDAK ADA di berkas dibuang dari koleksi. Tanpa itu,
 * catatan yang dikosongkan pelajar tetap muncul di hasil pencarian -- dan
 * sebuah hasil yang mengantar ke halaman tanpa catatan adalah hasil yang
 * membuat orang mengira tulisannya hilang entah ke mana.
 */
export async function selaraskan(
  db: Db,
  jalur = jalurCatatan(),
): Promise<{ masuk: number; dibuang: number; total: number }> {
  const { daftar } = await bacaCatatan(jalur);
  const kol = koleksi(db);

  let masuk = 0;
  if (daftar.length) {
    const hasil = await kol.bulkWrite(
      daftar.map((c: Catatan) => ({
        replaceOne: {
          filter: { _id: c.kunci },
          replacement: { _id: c.kunci, teks: c.teks, diubah: c.diubah },
          upsert: true,
        },
      })),
      { ordered: false },
    );
    masuk = hasil.upsertedCount + hasil.modifiedCount;
  }

  const kunci = daftar.map((c) => c.kunci);
  const buang = await kol.deleteMany({ _id: { $nin: kunci } });
  return { masuk, dibuang: buang.deletedCount, total: daftar.length };
}

/** Satu hasil pencarian. `skor` dari `$meta: "textScore"` milik Mongo. */
export interface HasilCatatan {
  kunci: string;
  teks: string;
  diubah: string;
  skor: number;
}

/**
 * Cari `kueri` di dalam catatan, paling relevan dulu.
 *
 * Yang mengurutkan Mongo (`textScore`), bukan kode ini: itu seluruh alasan
 * indeks teks dipakai alih-alih `Array.filter` di sisi klien. Dan itu juga
 * yang membuat paket ini sebuah pelajaran Mongo yang nyata -- bukan demo yang
 * menyimpan data lalu membacanya kembali apa adanya.
 */
export async function cari(
  db: Db,
  kueri: string,
  batas = 50,
): Promise<HasilCatatan[]> {
  const dok = await koleksi(db)
    .find(
      { $text: { $search: kueri } },
      { projection: { skor: { $meta: "textScore" }, teks: 1, diubah: 1 } },
    )
    .sort({ skor: { $meta: "textScore" } })
    .limit(batas)
    .toArray();
  return dok.map((d) => ({
    kunci: d._id,
    teks: d.teks,
    diubah: d.diubah,
    skor: (d as DokCatatan & { skor?: number }).skor ?? 0,
  }));
}
