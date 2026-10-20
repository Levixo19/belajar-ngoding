/* Konfigurasi Vite untuk antarmuka React.
 *
 * Masalah yang diselesaikan berkas ini, dan kenapa ia tidak sepele.
 *
 * Server Python MENJALANKAN KODE, jadi ia dijaga tiga lapis: bind wajib
 * loopback, Host/Origin diperiksa, dan setiap `/api/*` menuntut header
 * `X-Belajar-Token` yang cocok dengan token acak per-jalannya server
 * (`webapp/server.py`). Token itu ditanam ke `index.html` saat halaman
 * dilayani -- `window.TOKEN_BELAJAR = "{{TOKEN}}"`.
 *
 * Dev server Vite menyajikan HTML-nya SENDIRI, jadi tidak ada yang menanam
 * token ke sana. Akibatnya setiap panggilan API dari React menerima 403 sejak
 * klik pertama, dan pesannya "Token tidak sah. Muat ulang halaman." -- saran
 * yang tidak akan pernah menolong, karena memuat ulang Vite tidak membuat
 * token muncul.
 *
 * Dua jalan yang TIDAK diambil:
 *
 * * Melonggarkan pemeriksaan token di server untuk mode dev. Itu melepas
 *   pagar sungguhan demi kenyamanan perkakas, di server yang mengeksekusi
 *   kode pelajar. Pagar yang punya pintu belakang bukan pagar.
 * * Menyalin token dengan tangan ke `.env`. Ia berubah setiap kali server
 *   dinyalakan ulang, jadi yang didapat adalah 403 yang muncul sesekali dan
 *   selalu disalahartikan sebagai bug aplikasi.
 *
 * Yang diambil: plugin di bawah MENGAMBIL tokennya sendiri. `GET /` di server
 * Python dilayani TANPA token (`server.py` memeriksa rutenya sebelum
 * memeriksa token), jadi halamannya bisa dibaca apa adanya dan tokennya
 * dibacakan dari situ. Nol perubahan di sisi server, dan pagarnya utuh.
 *
 * Pemeriksaan Origin tetap lolos karena ia cuma menuntut hostname loopback;
 * `localhost:5173` memenuhinya.
 */

import react from "@vitejs/plugin-react";
import { defineConfig, type Plugin } from "vite";

/** Port server Python. Samakan dengan yang dipakai `belajar-web.py`. */
const PORT_PYTHON = Number(process.env.BELAJAR_PORT || 7788);
const ASAL_PYTHON = `http://127.0.0.1:${PORT_PYTHON}`;

/**
 * Ambil token dari halaman yang dilayani server Python.
 *
 * Mengembalikan `null` kalau servernya tidak hidup. Itu keadaan yang normal
 * (orang menjalankan `npm run dev` lebih dulu), jadi ia TIDAK boleh membunuh
 * dev server -- cukup satu pesan yang menyebut perintah yang harus dijalankan.
 */
async function ambilToken(): Promise<string | null> {
  try {
    const tanggapan = await fetch(ASAL_PYTHON + "/");
    if (!tanggapan.ok) return null;
    const html = await tanggapan.text();
    const cocok = html.match(/window\.TOKEN_BELAJAR\s*=\s*"([^"]+)"/);
    return cocok ? (cocok[1] as string) : null;
  } catch {
    return null;
  }
}

/**
 * Suntik token ke halaman dev, dan ambil ULANG setiap kali halaman dimuat.
 *
 * "Setiap kali" itu bagian yang penting. Mengambil token sekali saat dev
 * server start terdengar cukup, tapi server Python bisa dinyalakan ulang di
 * tengah sesi -- dan sejak saat itu tokennya berbeda sementara halaman masih
 * memegang yang lama. Yang terjadi bukan error yang jelas melainkan 403 yang
 * muncul mendadak pada aplikasi yang tadinya jalan.
 *
 * Tokennya disuntik lewat `tags`, BUKAN dengan mengganti teks di dalam sebuah
 * `<script>` di index.html. Itu bukan selera: `transformIndexHtml` tidak bisa
 * mengubah isi skrip inline sama sekali, karena Vite mengekstrak badannya
 * sebagai modul lalu menyajikan yang ASLI. Diukur di mesin ini -- pada satu
 * rantai `.replace()` yang sama, penanda sebelum `</head>` mendarat sementara
 * penggantian di dalam `<script>` dipulihkan diam-diam, tanpa satu pun
 * peringatan. Hook-nya tetap terpanggil dan `html` yang masuk memang memuat
 * placeholder-nya, jadi tidak ada satu pun tanda yang menunjukkan sebabnya.
 */
function tokenBelajar(): Plugin {
  let diberitahu = false;
  return {
    name: "belajar-token",
    apply: "serve",
    transformIndexHtml: {
      order: "pre",
      async handler(html) {
        const token = await ambilToken();
        if (!token) {
          if (!diberitahu) {
            diberitahu = true;
            console.warn(
              `\n[belajar-token] Server Python di ${ASAL_PYTHON} tidak ` +
                `menjawab, jadi API akan menjawab 403.\n` +
                `  Nyalakan dengan profil terpisah supaya progres aslimu ` +
                `tidak tertulisi:\n\n` +
                `  S=$(mktemp -d) && BELAJAR_PROGRESS_FILE=$S/p.json \\\n` +
                `    BELAJAR_CONFIG_FILE=$S/k.json ` +
                `BELAJAR_CATATAN_FILE=$S/c.json \\\n` +
                `    BELAJAR_WORKSPACE=$S/kerja python3 belajar-web.py ` +
                `--tanpa-browser --port ${PORT_PYTHON}\n`,
            );
          }
          return html;
        }
        diberitahu = false;
        return {
          html,
          tags: [
            {
              tag: "script",
              // `head-prepend`: ia harus sudah ada sebelum `main.tsx` jalan,
              // karena `api.ts` membacanya saat modulnya dievaluasi.
              injectTo: "head-prepend",
              children: `window.TOKEN_BELAJAR=${JSON.stringify(token)};`,
            },
          ],
        };
      },
    },
  };
}

export default defineConfig({
  plugins: [react(), tokenBelajar()],
  server: {
    host: "127.0.0.1",
    port: 5173,
    proxy: {
      // API dan berkas statik lama (huruf, vendor GSAP, gaya.css) diteruskan
      // ke server Python. Dengan begitu React memakai API, font, dan lembar
      // gaya yang SAMA -- bukan salinan kedua yang suatu hari berbeda.
      "/api": { target: ASAL_PYTHON, changeOrigin: false },
      "/huruf": { target: ASAL_PYTHON, changeOrigin: false },
      "/vendor": { target: ASAL_PYTHON, changeOrigin: false },
      "/gaya.css": { target: ASAL_PYTHON, changeOrigin: false },
    },
  },
});
