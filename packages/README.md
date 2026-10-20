# packages/

Sisi TypeScript. Workspace npm (`"workspaces": ["packages/*"]` di akar), dan
**tanpa langkah build**: Node 24 menjalankan `.ts` langsung lewat pelucutan
tipe, jadi `tsc` di sini pemeriksa (`npm run tipe`, `noEmit`), bukan kompiler.

Aplikasinya sendiri tidak membutuhkan folder ini: `python3 belajar-web.py`
tetap jalan penuh tanpa `npm install`. Folder ini ada untuk perpindahan ke
React + TypeScript, dan sekarang sudah dipakai sebagai satu-satunya tempat
algoritma bersama diuji di luar Python.

```
konten/     seluruh kurikulum sebagai JSON + tipe.ts     (DIHASILKAN)
bersama/    sorot, beda, galat sebagai implementasi TS + rekaman golden
web/        antarmuka React + TypeScript, di atas API Python yang sama
```

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

Token API tidak perlu disalin: plugin `belajar-token` mengambilnya dari
`GET /` server Python setiap kali halaman dimuat. Kalau servernya tidak hidup,
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
npm run golden                              # tiga pembanding, dari akar
npm run tipe                                # tsc --noEmit
npm run gigi --workspace @belajar/bersama   # baterai mutasi
```

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
