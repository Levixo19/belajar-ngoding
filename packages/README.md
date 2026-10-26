# packages/

Sisi TypeScript. Workspace npm (`"workspaces": ["packages/*"]` di akar).
**Tanpa langkah build untuk `bersama` dan `catatan`**: Node menjalankan `.ts`
langsung lewat pelucutan tipe, jadi `tsc` untuk keduanya pemeriksa
(`npm run tipe`, `noEmit`), bukan kompiler. `web` dibundel Vite.

`--experimental-strip-types` diberikan eksplisit di suite dan di baterai
mutasi: pelucutan tipe baru tanpa-flag sejak Node 23.6 (22.18 di jalur LTS),
dan di bawah itu SELURUH pembanding gagal dengan `ERR_UNKNOWN_FILE_EXTENSION`
-- empat belas tes merah karena alasan yang tidak ada hubungannya dengan
isinya. Flagnya diterima apa adanya oleh 22.11 maupun 24.21.

Aplikasinya sendiri tidak membutuhkan folder ini: `python3 belajar-web.py`
tetap jalan penuh tanpa `npm install`. Folder ini ada untuk perpindahan ke
React + TypeScript, dan sekarang sudah dipakai sebagai satu-satunya tempat
algoritma bersama diuji di luar Python.

```
konten/     seluruh kurikulum sebagai JSON + tipe.ts     (DIHASILKAN)
bersama/    sorot, beda, galat sebagai implementasi TS + rekaman golden
web/        antarmuka React + TypeScript, di atas API Python yang sama
catatan/    layanan pencarian catatan (Express + MongoDB). TAMBAHAN:
            aplikasinya jalan penuh tanpanya -- lihat catatan/README.md
```

Satu koreksi atas kalimat di atas, dan ia penting karena menyangkut aturan
"aplikasi ini wajib utuh tanpa internet": `catatan/` punya DUA dependensi
runtime sungguhan (`express`, `mongodb`), dan keduanya satu-satunya di seluruh
repo. Mereka milik paket itu saja -- `python3 belajar-web.py` tetap jalan penuh
tanpa `npm install`, dan tanpa `catatan/` yang hilang cuma pencarian di dalam
isi catatan.

## Menjalankan antarmuka React

DUA proses: server Python menyediakan API, Vite menyajikan React.

```bash
# 1. Server Python, PROFIL TERPISAH supaya progres aslimu tidak tertulisi
S=$(mktemp -d)
BELAJAR_PROGRESS_FILE=$S/p.json BELAJAR_CONFIG_FILE=$S/k.json \
BELAJAR_CATATAN_FILE=$S/c.json BELAJAR_WORKSPACE=$S/kerja \
  python3 belajar-web.py --tanpa-browser --port 7788

# 2. Vite, di terminal lain
npm run dev --workspace @belajar/web     # http://127.0.0.1:5173/
```

```bash
npm run build --workspace @belajar/web   # tsc --noEmit && vite build
```

Bundelnya bukan untuk dilayani -- yang dilayani `belajar-web.py` tetap
`webapp/statik/`. Gunanya SATU: membuktikan port React benar-benar bisa
dibangun. Dua hal yang dikatakan keluarannya dan keduanya benar:
`/gaya.css doesn't exist at build time` (ia memang diproksi, bukan disalin),
dan plugin tokennya `apply: "serve"` -- jadi bundel produksi tidak punya token
dan `api.ts` mengatakannya dengan kalimat yang menyebut perintahnya, bukan
membiarkan 403 yang membingungkan.

**`index.html` tidak boleh memuat teks tag penutup kepala, bahkan di dalam
komentar.** `vite build` menyuntikkan `<script src=...>` tepat sebelum
kecocokan PERTAMA teks itu, termasuk kecocokan di dalam komentar. Terukur:
dengan tag itu tertulis di sebuah komentar penjelas, skripnya mendarat DI DALAM
komentar dan bundel produksinya memuat nol JavaScript -- halaman kosong, tanpa
satu pun galat di konsol maupun di keluaran build. `vite build` yang ada tapi
tidak pernah dijalankan menyembunyikan tepat kelas cacat ini.

Token API tidak perlu disalin saat `npm run dev`: plugin `belajar-token`
mengambilnya dari `GET /` server Python setiap kali halaman dimuat. Kalau servernya tidak hidup,
layarnya mengatakannya beserta perintah yang harus dijalankan -- bukan 403 yang
membingungkan.

**Kalau menguji dev server dengan `curl`, tiga hal ini menghasilkan
negatif-palsu yang sangat meyakinkan:** tanpa `Accept: text/html` Vite
melayani `index.html` mentah tanpa transform; tanpa `server.host` ia mengikat
ke `localhost` yang beresolusi ke `::1` lebih dulu; dan `( cmd ) &` + `kill $!`
menelantarkan proses Vite-nya, sehingga instance lama yang menjawab.

## Apa yang DIHASILKAN dan apa yang ditulis tangan

Membedakan keduanya penting, karena menyunting berkas hasil dengan tangan
tidak menimbulkan error — ia cuma hilang pada ekspor berikutnya, dan yang
tersisa cuma dua salinan yang mulai berbeda pendapat.

| Jalur | Dari mana | Alat |
|---|---|---|
| `konten/**/*.json` | literal Python di `data/` | `alat/ekspor_konten.py` |
| `bersama/data/*.json` | `inti/sorot.py`, `inti/berkas.py`, `inti/galat.py` | `alat/ekspor_bersama.py` |
| `bersama/golden/*.json` | `inti/sorot.py`, `beda.py`, `galat.py` | `alat/golden_bersama.py` |
| `konten/tipe.ts` | ditulis tangan | — |
| `bersama/src/*.ts` | ditulis tangan | — |
| `bersama/uji/*` | ditulis tangan | — |

`konten/**/*.json` ada di `.prettierignore`. Sekali diformat ulang, 12,8 MB
berubah tanpa ada yang tahu apa yang bergeser.

## Cara memastikan portnya masih benar

```bash
npm run golden                                # tiga pembanding, dari akar
npm run tipe                                  # tsc --noEmit
npm run gigi --workspace @belajar/bersama     # baterai mutasi
npm run banding --workspace @belajar/web      # geometri rasi vs rasi.js
```

`banding` berbeda jenis dari `golden`. Ia tidak mengadu dengan rekaman
melainkan dengan implementasi JS yang masih hidup (`webapp/statik/js/rasi.js`),
karena keduanya JavaScript dan fungsinya murni — jadi tidak ada sisi Python
yang perlu direkam. Yang dijaganya: bentuk tiap rasi deterministik dari benih
(nama kurikulum), jadi satu bit yang meleset di `hash` atau `prng` mengubah
SETIAP rasi tanpa satu pun error.

Yang terakhir yang paling mudah dilewatkan dan paling penting. `npm run golden`
menjawab "apakah portnya cocok hari ini"; baterai mutasi menjawab pertanyaan
yang berbeda dan lebih tajam: **"kalau portnya rusak, apakah pembandingnya
akan memberi tahu?"** Ia merusak sumbernya dengan sengaja, dua belas kali, dan
menuntut tiap sel merah dengan KATEGORI keluhan yang benar — bukan sekadar
kode keluar bukan-nol, karena mutan yang bikin Node gagal memuat berkasnya
juga memberi kode keluar bukan-nol tanpa membuktikan apa pun.

Rekaman golden-nya ikut dijalankan suite Python lewat
`tests/test_konten_json.py`, dan ia SKIP kalau `node` tidak ada — bukan lulus
diam-diam.
