/* Uji layanan pencarian catatan.
 *
 * Dua lapis, dan yang pertama jalan TANPA MongoDB:
 *
 * 1. `sumber.ts` -- pembaca berkas JSON. Murni, jadi ia diuji dengan berkas
 *    sementara dan tidak pernah menyentuh catatan siapa pun.
 * 2. `mongo.ts` -- penyelaras dan pencarinya. Butuh container; kalau ia tidak
 *    jalan, lapisan ini DILEWATI dengan pesan yang menyebutkan perintah untuk
 *    menyalakannya -- bukan lulus diam-diam, dan bukan merah karena alasan
 *    yang tidak ada hubungannya dengan kodenya.
 *
 * Databasenya `belajar_uji`, BUKAN `belajar`. Tanpa pemisahan itu, menjalankan
 * uji ini membuang indeks catatan sungguhan milik pemiliknya dan menggantinya
 * dengan tiga catatan karangan -- dan karena Mongo di sini cuma indeks, yang
 * terlihat bukan kehilangan data melainkan pencarian yang mendadak bohong.
 *
 *     npm run uji --workspace @belajar/catatan
 */

import assert from "node:assert/strict";
import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";

import { request } from "node:http";

import { MongoClient } from "mongodb";

import { alamatMongo, cari, pasangIndeks, selaraskan, tutupMongo } from "../src/mongo.ts";
import { bacaCatatan, jalurCatatan } from "../src/sumber.ts";

const DB_UJI = "belajar_uji";

let lulus = 0;
function cek(nama: string, fn: () => void | Promise<void>) {
  return Promise.resolve()
    .then(fn)
    .then(() => {
      lulus += 1;
      console.log(`  ok   ${nama}`);
    })
    .catch((e: Error) => {
      console.error(`  GAGAL ${nama}\n       ${e.message}`);
      process.exitCode = 1;
    });
}

/* ------------------------------------------------- lapisan 1: tanpa Mongo */

const DIR = mkdtempSync(path.join(tmpdir(), "uji-catatan-"));
const jalurBerkas = (nama: string) => path.join(DIR, nama);

console.log("sumber.ts (tanpa MongoDB)");

await cek("berkas yang belum ada memberi daftar kosong, bukan galat", async () => {
  const r = await bacaCatatan(jalurBerkas("tidak-ada.json"));
  assert.deepEqual(r, { daftar: [], diubah: 0 });
});

await cek("catatan dibaca beserta kunci dan cap waktunya", async () => {
  const p = jalurBerkas("isi.json");
  writeFileSync(
    p,
    JSON.stringify({
      versi: 1,
      catatan: {
        "c_materi::Pointer": { teks: "alamat memori", diubah: "2026-10-01T10:00:00" },
        "go_materi::Chan": { teks: "channel", diubah: "2026-10-02T10:00:00" },
      },
    }),
  );
  const r = await bacaCatatan(p);
  assert.equal(r.daftar.length, 2);
  assert.deepEqual(r.daftar.map((c) => c.kunci).sort(),
                   ["c_materi::Pointer", "go_materi::Chan"]);
  assert.ok(r.diubah > 0, "mtime harus terbaca");
});

await cek("catatan bertulisan KOSONG dilewati", async () => {
  const p = jalurBerkas("kosong.json");
  writeFileSync(p, JSON.stringify({
    catatan: { "a::b": { teks: "", diubah: "x" }, "c::d": { teks: "ada", diubah: "y" } },
  }));
  const r = await bacaCatatan(p);
  assert.deepEqual(r.daftar.map((c) => c.kunci), ["c::d"]);
});

await cek("berkas yang ADA tapi rusak MELEMPAR, bukan dilaporkan nol", async () => {
  const p = jalurBerkas("rusak.json");
  writeFileSync(p, "{ bukan json");
  await assert.rejects(() => bacaCatatan(p));
});

await cek("BELAJAR_CATATAN_FILE dihormati", () => {
  const sebelum = process.env["BELAJAR_CATATAN_FILE"];
  process.env["BELAJAR_CATATAN_FILE"] = "/tmp/jalur-uji.json";
  assert.equal(jalurCatatan(), "/tmp/jalur-uji.json");
  if (sebelum === undefined) delete process.env["BELAJAR_CATATAN_FILE"];
  else process.env["BELAJAR_CATATAN_FILE"] = sebelum;
});

/* ------------------------------------- lapisan 1b: penjagaan HTTP, tanpa Mongo

   Ketiga penjagaan di bawah menolak SEBELUM satu pun panggilan Mongo, jadi
   mereka bisa diuji tanpa container -- dan itu memang tempatnya: penjagaan
   keamanan yang cuma teruji saat sebuah container menyala adalah penjagaan
   yang diam-diam berhenti teruji. */

console.log("\npenjagaan HTTP (tanpa MongoDB)");

const { app } = await import("../src/indeks.ts");
const srv = app.listen(0, "127.0.0.1");
await new Promise<void>((res) => srv.once("listening", () => res()));
const port = (srv.address() as { port: number }).port;

/* Permintaannya lewat `node:http` MENTAH, bukan `fetch`, dan itu bukan selera:
   undici (fetch milik Node) MELARANG menyetel header `Host` -- ia
   mengabaikannya tanpa suara. Jadi seluruh uji DNS rebinding di bawah akan
   "lulus" dengan Host yang benar, membuktikan nol.
   
   `Connection: close` juga ikut, dan itu menutup jebakan kedua: fetch memakai
   keep-alive, dan `srv.close()` menunggu setiap koneksi yang masih hidup --
   jadi ujinya menggantung di akhir alih-alih selesai. */
function minta(jalur: string, opsi: {
  metode?: string; host?: string; asal?: string; tipe?: string; isi?: string;
} = {}): Promise<{ kode: number; kepala: Record<string, string | string[] | undefined>; teks: string }> {
  return new Promise((selesai, gagal) => {
    const kepala: Record<string, string> = { Connection: "close" };
    if (opsi.host !== undefined) kepala["Host"] = opsi.host;
    if (opsi.asal) kepala["Origin"] = opsi.asal;
    if (opsi.tipe) kepala["Content-Type"] = opsi.tipe;
    const req = request(
      { host: "127.0.0.1", port, path: jalur, method: opsi.metode ?? "GET", headers: kepala },
      (res) => {
        let teks = "";
        res.on("data", (c) => { teks += c; });
        res.on("end", () => selesai({
          kode: res.statusCode ?? 0, kepala: res.headers, teks,
        }));
      },
    );
    req.on("error", gagal);
    if (opsi.isi !== undefined) req.write(opsi.isi);
    req.end();
  });
}

await cek("Host asing DITOLAK 403 (DNS rebinding)", async () => {
  // Nama domain penyerang yang DNS-nya diarahkan ke 127.0.0.1 membuat
  // peramban menganggap permintaannya same-origin -- jadi `Origin` tidak
  // dikirim sama sekali. Yang membedakannya cuma `Host`.
  const r = await minta("/sehat", { host: "jahat.contoh" });
  assert.equal(r.kode, 403);
});

await cek("Host loopback diterima", async () => {
  for (const h of [`127.0.0.1:${port}`, `localhost:${port}`]) {
    const r = await minta("/sehat", { host: h });
    assert.equal(r.kode, 200, h);
  }
});

await cek("asal asing DITOLAK 403, bukan cuma tanpa header CORS", async () => {
  // Bedanya nyata dan ia CSRF: tanpa header balasan, halaman asing memang
  // tidak bisa MEMBACA jawabannya -- tapi permintaannya tetap SAMPAI dan efek
  // sampingnya tetap terjadi.
  const r = await minta("/selaras", {
    metode: "POST", asal: "https://jahat.contoh",
    tipe: "application/json", isi: "{}",
  });
  assert.equal(r.kode, 403);
});

await cek("asal loopback mendapat header CORS yang menyebut dirinya", async () => {
  const asal = "http://127.0.0.1:5173";
  const r = await minta("/sehat", { asal });
  assert.equal(r.kepala["access-control-allow-origin"], asal);
  // `Vary: Origin` WAJIB ikut: tanpa itu, cache boleh melayani jawaban yang
  // header CORS-nya menyebut asal lain.
  assert.equal(r.kepala["vary"], "Origin");
});

await cek("POST tanpa Content-Type JSON ditolak 415", async () => {
  // Ini yang MEMAKSA preflight ada: `application/json` bukan "simple
  // request", jadi formulir HTML lintas-asal -- satu-satunya POST tanpa
  // preflight -- tidak bisa mengirimnya.
  const r = await minta("/selaras", {
    metode: "POST", tipe: "text/plain", isi: "x",
  });
  assert.equal(r.kode, 415);
});

await cek("preflight: loopback diizinkan, asal asing 403", async () => {
  const baik = await minta("/selaras", {
    metode: "OPTIONS", asal: "http://localhost:5173",
  });
  assert.equal(baik.kode, 204);
  assert.equal(baik.kepala["access-control-allow-headers"], "Content-Type");
  const buruk = await minta("/selaras", {
    metode: "OPTIONS", asal: "https://jahat.contoh",
  });
  assert.equal(buruk.kode, 403);
});

await cek("kueri satu huruf ditolak 400 dengan sebabnya", async () => {
  const r = await minta("/cari?q=a");
  assert.equal(r.kode, 400);
  assert.match(r.teks, /minimal 2 huruf/);
});

srv.closeAllConnections();
await new Promise<void>((res) => srv.close(() => res()));
/* Klien Mongo yang dibuat oleh app DITUTUP di sini, dan ia terpisah dari klien
   uji di bawah. Tanpa ini prosesnya tidak pernah keluar: kolam koneksi driver
   memegang socket yang hidup, dan Node menunggu setiap handle terbuka --
   gejalanya uji yang mencetak "lulus" lalu menggantung, yang jauh lebih
   membingungkan daripada uji yang gagal. */
await tutupMongo();

/* --------------------------------------------- lapisan 2: dengan MongoDB */

const klien = new MongoClient(alamatMongo(), { serverSelectionTimeoutMS: 1200 });
let adaMongo = false;
try {
  await klien.connect();
  await klien.db(DB_UJI).command({ ping: 1 });
  adaMongo = true;
} catch {
  adaMongo = false;
}

if (!adaMongo) {
  await klien.close().catch(() => {});
  console.log(
    "\nmongo.ts  DILEWATI: MongoDB tidak bisa dihubungi di " + alamatMongo() +
      "\n          podman start belajar-mongo   (atau `podman run` pertama kali;" +
      "\n          perintah lengkapnya di kepala src/indeks.ts)",
  );
  console.log(`\n${lulus} pemeriksaan lulus, lapisan Mongo dilewati.`);
} else {
  console.log("\nmongo.ts (dengan MongoDB)");
  const db = klien.db(DB_UJI);
  await db.collection("catatan").deleteMany({});
  await pasangIndeks(db);

  const p = jalurBerkas("mongo.json");
  const tulis = (isi: Record<string, { teks: string; diubah: string }>) =>
    writeFileSync(p, JSON.stringify({ versi: 1, catatan: isi }));

  await cek("selaraskan memasukkan seluruh catatan", async () => {
    tulis({
      "c_materi::Pointer Dasar": {
        teks: "Pointer itu variabel yang isinya alamat memori",
        diubah: "2026-10-01T10:00:00",
      },
      "python_materi::Fungsi": {
        teks: "Fungsi di Python memakai def",
        diubah: "2026-10-02T10:00:00",
      },
      "go_materi::Goroutine": {
        // Menyebut "memori" SEKALI, dan sengaja: tanpa dokumen KEDUA yang ikut
        // cocok, pemeriksaan urutan di bawah tidak membuktikan apa pun --
        // mencabut `.sort({$meta: "textScore"})` tetap hijau kalau cuma satu
        // dokumen yang cocok. Diukur: dengan dokumen ini, mencabutnya memerah.
        //
        // Ia juga disisipkan LEBIH AKHIR di berkasnya daripada Pointer Dasar,
        // jadi urutan sisipan dan urutan relevansi memang berbeda.
        teks: "Goroutine murah: channel yang menyinkronkan, bukan memori bersama",
        diubah: "2026-10-03T10:00:00",
      },
    });
    const r = await selaraskan(db, p);
    assert.equal(r.total, 3);
    assert.equal(r.masuk, 3);
    assert.equal(r.dibuang, 0);
  });

  /* BATAS PEMERIKSAAN INI, dan ia diukur: mencabut
     `.sort({ skor: { $meta: "textScore" } })` dari `cari()` TIDAK selalu
     memerahkannya. Urutan `find()` tanpa `sort` adalah urutan pemindaian
     indeks, dan itu implementation-defined di MongoDB -- terukur KEDUA arah
     dengan korpus yang sama persis: di database `belajar_ukur2` ia memberi
     `go_materi:0.56 | c_materi:1.14` (salah), di `belajar_uji` ia memberi
     `c_materi:1.14 | go_materi:0.56` (kebetulan benar).

     Jadi yang dijaga pemeriksaan ini RELEVANSINYA -- bahwa dua dokumen cocok,
     bahwa skornya berbeda, dan bahwa yang menyebut kedua kata berskor lebih
     tinggi. Kehadiran `.sort()` sendiri tidak bisa ditagih dari lapisan ini,
     dan menagihnya lewat `explain()` berarti memagari rencana kueri Mongo
     alih-alih perilaku yang dijanjikan paket ini. */
  await cek("pencarian diurut menurut relevansi, bukan urutan berkas", async () => {
    const h = await cari(db, "alamat memori");
    assert.equal(h.length, 2, "dua catatan harus cocok");
    // Pointer Dasar menyebut KEDUA kata; Goroutine cuma "memori".
    assert.deepEqual(h.map((x) => x.kunci),
                     ["c_materi::Pointer Dasar", "go_materi::Goroutine"]);
    assert.ok((h[0]?.skor ?? 0) > (h[1]?.skor ?? 0),
              "skor yang pertama harus lebih tinggi");
    // Skor non-naik: properti yang memang dijanjikan `cari()`.
    const skor = h.map((x) => x.skor);
    assert.deepEqual(skor, [...skor].sort((a, b) => b - a));
  });

  await cek("kata yang tidak ada memberi nol hasil", async () => {
    assert.deepEqual(await cari(db, "zzzqqqwww"), []);
  });

  await cek("kunci yang hilang dari berkas DIBUANG dari koleksi", async () => {
    tulis({
      "c_materi::Pointer Dasar": {
        teks: "Pointer itu variabel yang isinya alamat memori",
        diubah: "2026-10-01T10:00:00",
      },
    });
    const r = await selaraskan(db, p);
    assert.equal(r.total, 1);
    assert.equal(r.dibuang, 2);
    assert.deepEqual(await cari(db, "goroutine"), []);
  });

  await cek("selaraskan IDEMPOTEN: dijalankan dua kali tidak mengubah apa pun",
    async () => {
      const a = await selaraskan(db, p);
      const b = await selaraskan(db, p);
      assert.equal(a.total, b.total);
      assert.equal(b.masuk, 0, "jalannya kedua tidak boleh menulis apa pun");
      assert.equal(b.dibuang, 0);
    });

  await cek("teks yang DIUBAH ikut terbaru di indeks", async () => {
    tulis({
      "c_materi::Pointer Dasar": {
        teks: "Sudah diganti: yang penting sekarang channel",
        diubah: "2026-10-05T10:00:00",
      },
    });
    await selaraskan(db, p);
    assert.deepEqual(await cari(db, "alamat"), [],
                     "teks lama tidak boleh tertinggal di indeks");
    const h = await cari(db, "channel");
    assert.equal(h[0]?.kunci, "c_materi::Pointer Dasar");
  });

  await cek("berkas yang hilang mengosongkan indeks, bukan melempar", async () => {
    const r = await selaraskan(db, jalurBerkas("tidak-ada-sama-sekali.json"));
    assert.equal(r.total, 0);
    assert.equal(r.dibuang, 1);
  });

  await db.collection("catatan").deleteMany({});
  await klien.close();
  console.log(`\n${lulus} pemeriksaan lulus (termasuk lapisan MongoDB).`);
}

if (process.exitCode) console.error("\nADA YANG GAGAL.");
