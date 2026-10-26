/* Layanan pencarian catatan: Express di atas MongoDB.
 *
 * **Ia TAMBAHAN, bukan pengganti.** Aplikasi belajar-codingV2 jalan penuh
 * tanpa paket ini: catatan tetap ditulis, dibaca, dan didaftar oleh server
 * Python dari berkas JSON-nya. Yang ditambahkan satu kemampuan yang versi JSON
 * memang tidak punya -- pencarian teks berperingkat di dalam isi catatan.
 *
 * Tiga batas yang mengikat, dan ketiganya sama dengan yang dipegang server
 * Python:
 *
 * 1. **Bind loopback.** `server.buat()` di Python menolak host selain
 *    127.0.0.1 dengan `ValueError`, dan alasannya sama di sini: ini mesin
 *    pribadi, dan satu-satunya alasan Mongo di balik layanan ini boleh tanpa
 *    autentikasi adalah karena tidak ada yang bisa menghubunginya dari luar.
 * 2. **Hanya BACA dari berkas pelajar.** Tidak ada satu pun jalur tulis ke
 *    `~/.belajar_ngoding_catatan.json` di paket ini. Pengaman yang
 *    melindunginya (karantina, `.bak`, tulis atomik) hidup di
 *    `pelajar/simpanan.py`, dan menulis dari dua proses berarti dua definisi
 *    "tulis dengan aman".
 * 3. **Mongo yang mati bukan galat aplikasi.** Layanannya tetap menyala dan
 *    menjawab 503 dengan kalimat yang bisa dibaca. Yang memanggilnya berhak
 *    tahu bahwa yang tidak tersedia PENCARIANNYA, bukan catatannya.
 *
 * Jalankan:
 *
 *     podman run -d --name belajar-mongo \
 *       -p 127.0.0.1:27017:27017 -v belajar-mongo:/data/db mongo:8
 *     npm run mulai --workspace @belajar/catatan
 */

import { pathToFileURL } from "node:url";

import express from "express";

import { cari, klienMongo, NAMA_DB, pasangIndeks, selaraskan } from "./mongo.ts";
import { bacaCatatan, jalurCatatan } from "./sumber.ts";

const PORT = Number(process.env["BELAJAR_CATATAN_PORT"] || 7799);

/* Loopback, dan ia KONSTANTA -- bukan dibaca dari lingkungan. Variabel
   lingkungan yang bisa menaikkannya ke 0.0.0.0 adalah pagar yang bisa dilepas
   tanpa menyentuh satu baris kode pun, dan pagar seperti itu selalu dilepas
   "sebentar saja" lebih dulu. */
const HOST = "127.0.0.1";

/** Kueri terpendek yang dilayani. Satu huruf cocok dengan hampir setiap
 *  catatan, dan daftar seratus baris sama tidak bergunanya dengan nol. */
const MIN_KUERI = 2;

const app = express();
app.use(express.json({ limit: "64kb" }));

/* Asal yang boleh memanggil layanan ini: LOOPBACK saja.
 *
 * Antarmuka React hidup di port lain (5173 saat dev, 7788 lewat server
 * Python), jadi tanpa header ini peramban menolak jawabannya sebelum satu
 * baris JSON pun sampai -- dan yang terlihat pelajar bukan "layanan belum
 * jalan" melainkan pencarian yang diam tanpa sebab.
 *
 * Daftar putihnya POLA, bukan `*`. `Access-Control-Allow-Origin: *` di layanan
 * yang membacakan isi catatan pribadi berarti halaman mana pun di internet
 * yang dibuka di peramban ini bisa membacanya -- bind loopback tidak menolong
 * sama sekali, karena yang memanggil justru peramban milik pemiliknya. Yang
 * diizinkan hanya asal http/https di 127.0.0.1, [::1], atau localhost. */
const ASAL_LOOPBACK = /^https?:\/\/(127\.0\.0\.1|\[::1\]|localhost)(:\d+)?$/;

app.use((req, res, lanjut) => {
  const asal = req.headers.origin;
  res.setHeader("Vary", "Origin");
  if (asal && !ASAL_LOOPBACK.test(asal)) {
    // DITOLAK, bukan cuma "tidak diberi header CORS". Bedanya nyata dan ia
    // CSRF: tanpa header balasan, halaman asing memang tidak bisa MEMBACA
    // jawabannya -- tapi permintaannya tetap SAMPAI dan efek sampingnya tetap
    // terjadi. Untuk `POST /selaras` itu berarti halaman mana pun di internet
    // bisa memaksa penyelarasan ulang indeks berkali-kali. Ongkosnya kecil di
    // sini; polanya tidak, dan pola yang dibiarkan di satu endpoint adalah
    // pola yang disalin ke endpoint berikutnya.
    res.status(403).json({
      galat: "Asal tidak diizinkan. Layanan ini hanya melayani loopback.",
    });
    return;
  }
  if (asal) res.setHeader("Access-Control-Allow-Origin", asal);
  lanjut();
});

/* Preflight DIJAWAB eksplisit, dan `Access-Control-Allow-Headers` sengaja
   TIDAK memuat apa pun selain `Content-Type`.
   
   Itu separuh kedua dari penjagaan CSRF di atas: `POST` di bawah menuntut
   `Content-Type: application/json`, dan content-type itu BUKAN "simple
   request" -- jadi peramban wajib mengirim preflight lebih dulu. Permintaan
   dari asal asing karena itu mati di preflight, sebelum satu byte pun sampai
   ke penanganannya. Formulir HTML -- satu-satunya cara mengirim POST
   lintas-asal tanpa preflight -- cuma bisa mengirim tiga content-type, dan
   `application/json` bukan salah satunya. */
app.options("*splat", (req, res) => {
  const asal = req.headers.origin;
  if (!asal || !ASAL_LOOPBACK.test(asal)) {
    res.status(403).end();
    return;
  }
  res.setHeader("Access-Control-Allow-Origin", asal);
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");
  res.setHeader("Vary", "Origin");
  res.status(204).end();
});

/** Tolak POST yang content-type-nya tidak `application/json`.
 *
 *  Lihat alasannya di komentar preflight di atas: ini yang MEMAKSA preflight
 *  ada, dan tanpa itu formulir HTML lintas-asal bisa memicu `POST /selaras`
 *  tanpa satu pun permintaan pendahuluan. */
function wajibJson(req: express.Request, res: express.Response,
                   lanjut: express.NextFunction) {
  if (!req.is("application/json")) {
    res.status(415).json({
      galat: "POST ke layanan ini wajib `Content-Type: application/json`.",
    });
    return;
  }
  lanjut();
}

/** Terakhir kali koleksi diselaraskan dengan berkasnya, dari `mtimeMs`. */
let diselaraskan = -1;

/**
 * Selaraskan HANYA kalau berkasnya berubah.
 *
 * Pembandingnya `mtimeMs`, bukan jam dinding atau cap "sudah pernah": satu
 * `stat()` jauh lebih murah daripada `bulkWrite` seratus dokumen, dan layar
 * catatan mengetik satu permintaan per ketukan papan ketik. Yang dicegah bukan
 * ongkos CPU-nya melainkan kelasnya -- indeks yang ditulis ulang pada setiap
 * huruf adalah indeks yang suatu hari ditulis ulang saat seseorang sedang
 * membacanya.
 */
async function selaraskanJikaPerlu(db: Parameters<typeof selaraskan>[0]) {
  const { diubah } = await bacaCatatan();
  if (diubah === diselaraskan) return null;
  const hasil = await selaraskan(db);
  diselaraskan = diubah;
  return hasil;
}

/** Bungkus galat Mongo jadi 503 berkalimat, bukan 500 bertumpukan jejak. */
function balasMati(res: express.Response, e: unknown) {
  res.status(503).json({
    galat:
      "Pencarian catatan tidak tersedia: MongoDB tidak bisa dihubungi. " +
      "Catatanmu TIDAK terpengaruh -- ia tetap tersimpan di berkasnya sendiri " +
      "dan tetap bisa dibaca di aplikasi. Nyalakan containernya untuk " +
      "mengaktifkan pencarian.",
    sebab: e instanceof Error ? e.message : String(e),
  });
}

app.get("/sehat", async (_req, res) => {
  const { daftar } = await bacaCatatan();
  try {
    const db = klienMongo().db(NAMA_DB);
    await db.command({ ping: 1 });
    const hasil = await selaraskanJikaPerlu(db);
    res.json({
      sehat: true,
      berkas: jalurCatatan(),
      catatan: daftar.length,
      ...(hasil ? { selaras: hasil } : {}),
    });
  } catch (e) {
    // 200, bukan 503: pertanyaannya "apa keadaanmu", dan jawaban "Mongo mati"
    // adalah jawaban yang BERHASIL. Endpoint kesehatan yang ikut gagal saat
    // yang diawasinya gagal tidak bisa dipakai mengawasi apa pun.
    res.json({
      sehat: false,
      berkas: jalurCatatan(),
      catatan: daftar.length,
      sebab: e instanceof Error ? e.message : String(e),
    });
  }
});

app.get("/cari", async (req, res) => {
  const q = String(req.query["q"] ?? "").trim();
  if (q.length < MIN_KUERI) {
    res.status(400).json({ galat: `Ketik minimal ${MIN_KUERI} huruf.` });
    return;
  }
  try {
    const db = klienMongo().db(NAMA_DB);
    await pasangIndeks(db);
    await selaraskanJikaPerlu(db);
    res.json({ kata: q, hasil: await cari(db, q) });
  } catch (e) {
    balasMati(res, e);
  }
});

app.post("/selaras", wajibJson, async (_req, res) => {
  try {
    const db = klienMongo().db(NAMA_DB);
    await pasangIndeks(db);
    const hasil = await selaraskan(db);
    diselaraskan = (await bacaCatatan()).diubah;
    res.json(hasil);
  } catch (e) {
    balasMati(res, e);
  }
});

/* Dijalankan hanya kalau berkas ini TITIK MASUK, bukan diimpor. Tanpa penjaga
   ini, pengujinya yang mengimpor modul ini akan ikut menyalakan servernya dan
   menggantung tanpa penjelasan.
   
   Dibandingkan sebagai URL yang SUDAH diselesaikan, bukan dengan mencocokkan
   nama berkasnya: `endsWith("indeks.ts")` juga benar untuk berkas lain bernama
   sama di direktori lain, dan "kebetulan namanya sama" adalah cara yang paling
   membingungkan untuk memutuskan apakah sebuah server menyala. */
if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) {
  app.listen(PORT, HOST, () => {
    console.log(`Layanan catatan: http://${HOST}:${PORT}`);
    console.log(`Berkas catatan : ${jalurCatatan()}`);
    console.log(`MongoDB        : ${process.env["BELAJAR_MONGO_URL"] || "127.0.0.1:27017"}`);
  });
}

export { app };
