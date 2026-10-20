/* Bagian MURNI pratinjau: menurunkan halaman contoh dari sebuah lembar CSS.
 *
 * Port bagian non-DOM `webapp/statik/js/pratinjau.js`. Alasan seluruh berkas
 * ini ada ditulis di kepala berkas itu dan di AGENTS.md ("Apa yang DILIHAT
 * pelajar tidak selalu sama dengan apa yang DINILAI"); yang perlu diingat di
 * sini cuma satu kalimat: CSS tidak menggambar apa pun sendirian, jadi untuk
 * DITONTON ia butuh markup, dan markup itu diturunkan dari PEMILIHNYA sendiri.
 *
 * Karena diturunkan, ia karangan -- dan halaman karangan WAJIB mengaku
 * dikarang (`halamanDikarang`). Tanpa kalimat pengakuannya, yang dilihat
 * pelajar adalah markup yang tidak pernah ia tulis dan tidak akan pernah ia
 * temukan lagi di mana pun.
 *
 * Tidak ada satu pun rujukan `document` di berkas ini, dan itu syarat: ia
 * dijalankan dari Node oleh `uji/banding-pratinjau.mjs`, yang mengadu setiap
 * fungsi di sini dengan `pratinjau.js` yang masih melayani aplikasi lama atas
 * SELURUH blok kode HTML dan CSS di kurikulum.
 */

/* Elemen yang tidak sah berdiri sendiri di <body>. Menaruh <li> langsung di
   body membuat browser menampilkannya sebagai teks polos tanpa bulatan, dan
   pelajar akan menyimpulkan aturannya tidak berlaku. */
const INDUK_WAJIB: Record<string, string> = {
  li: "ul", td: "tr", th: "tr", tr: "table", tbody: "table", thead: "table",
  option: "select", figcaption: "figure", legend: "fieldset",
  summary: "details", dt: "dl", dd: "dl", source: "video", caption: "table",
};

/* Isi contoh. Elemen kosong tidak punya tinggi, dan aturan yang mengenai
   sesuatu yang tak terlihat sama saja dengan aturan yang tidak berlaku. */
const TEKS_CONTOH: Record<string, string> = {
  h1: "Judul Halaman", h2: "Sub Judul", h3: "Judul Bagian",
  h4: "Judul Kecil", h5: "Judul Lebih Kecil", h6: "Judul Terkecil",
  a: "sebuah tautan", button: "Tombol", label: "Label isian",
  li: "Butir daftar", td: "sel tabel", th: "kepala kolom",
  code: "kode()", strong: "tebal", em: "miring", small: "kecil",
  blockquote: "Kutipan contoh.", figcaption: "Keterangan gambar",
  summary: "Klik untuk buka", dt: "Istilah", dd: "Penjelasan istilah",
  p: "Paragraf contoh. Cukup panjang supaya tinggi baris, warna, dan "
   + "lebar kolomnya benar-benar kelihatan saat aturanmu berlaku.",
};
const TEKS_BAWAAN = "Teks contoh";

/* Elemen yang isinya bukan teks. */
const KOSONG = new Set(["img", "input", "br", "hr", "source", "video", "audio",
                        "canvas", "iframe", "textarea", "select"]);

const MAKS_CONTOH = 14;

/** Buang komentar CSS tanpa menyentuh isi string. */
function tanpaKomentar(css: string): string {
  return css.replace(/\/\*[\s\S]*?\*\//g, " ");
}

/** Semua pemilih di sebuah lembar CSS, termasuk yang di dalam @media.
 *
 *  Ditulis tangan sebagai pemindai kurung, bukan regex tunggal: pemilih
 *  bersarang di dalam at-rule dan deklarasi yang memuat kurung kurawal
 *  (seperti nilai `grid-template-areas`) membuat regex apa pun salah hitung.
 *
 *  Penghitung kedalaman yang ada di versi JS TIDAK diport. Ia dinaikkan dan
 *  diturunkan dengan benar, tapi tidak satu pun cabang pernah MEMBACANYA
 *  untuk memutuskan apa pun -- nilainya tidak sampai ke `keluar`. Pagarnya
 *  bukan pembacaan ini melainkan `uji/banding-pratinjau.mjs`, yang mengadu
 *  kedua versi atas seluruh lembar CSS di kurikulum. (Pola yang sama dengan
 *  dua loop perluasan `SequenceMatcher` di `bersama/src/beda.ts`: dibuktikan
 *  mati lebih dulu, baru dicabut.)
 */
function pemilihDi(css: string): string[] {
  const teks = tanpaKomentar(css);
  const keluar: string[] = [];
  let mulai = 0;
  for (let i = 0; i < teks.length; i++) {
    const c = teks.charAt(i);
    if (c === "{") {
      const kepala = teks.slice(mulai, i).trim();
      if (kepala.startsWith("@")) {
        // At-rule: preludenya bukan pemilih. @media & @supports MEMUAT
        // pemilih, @keyframes memuat persentase yang bukan pemilih.
        if (/^@(media|supports|layer|container|scope)\b/.test(kepala)) {
          mulai = i + 1;
          continue;
        }
        // Lewati seluruh badan at-rule lain.
        let d = 1;
        while (++i < teks.length && d) {
          if (teks.charAt(i) === "{") d += 1;
          else if (teks.charAt(i) === "}") d -= 1;
        }
        mulai = i + 1;
        continue;
      }
      if (kepala) keluar.push(kepala);
      // Lewati badan aturannya.
      let d = 1;
      while (++i < teks.length && d) {
        if (teks.charAt(i) === "{") d += 1;
        else if (teks.charAt(i) === "}") d -= 1;
      }
      mulai = i + 1;
    } else if (c === "}") {
      mulai = i + 1;
    }
  }
  return keluar;
}

interface Sederhana {
  tag: string;
  kelas: string[];
  id: string;
  atribut: Record<string, string>;
}

/** Satu pemilih sederhana -> {tag, kelas[], id, atribut{}} */
function uraiSederhana(bagian: string): Sederhana {
  // Pseudo-class dan pseudo-element dibuang: keadaan seperti :hover tidak bisa
  // ditunjukkan pada halaman diam, dan ::before butuh elemen tuannya -- yang
  // justru itulah yang sedang dibuat.
  const bersih = bagian.replace(/::?[\w-]+(\([^)]*\))?/g, "");
  const tag = ((bersih.match(/^[a-zA-Z][\w-]*/) ?? [""])[0] as string)
    .toLowerCase();
  const kelas = (bersih.match(/\.[\w-]+/g) ?? []).map((x) => x.slice(1));
  const id = ((bersih.match(/#[\w-]+/) ?? [""])[0] as string).slice(1);
  const atribut: Record<string, string> = {};
  for (const a of bersih.match(/\[[^\]]+\]/g) ?? []) {
    const m = a.slice(1, -1)
      .match(/^([\w-]+)\s*(?:[~^|*$]?=\s*['"]?([^'"\]]*)['"]?)?/);
    if (m) atribut[m[1] as string] = m[2] === undefined ? "" : m[2];
  }
  return { tag, kelas, id, atribut };
}

/** Rantai keturunan sebuah pemilih -> potongan HTML bersarang. */
function contohUntuk(pemilih: string): string {
  // Kombinator diratakan jadi keturunan biasa: > + ~ semuanya cukup
  // diwujudkan sebagai "ada di dalam", dan membedakannya hanya menambah
  // kerumitan tanpa menambah yang terlihat.
  const rantai = pemilih.replace(/\s*[>+~]\s*/g, " ").split(/\s+/)
    .filter(Boolean);
  if (!rantai.length) return "";

  let dalam = "";
  let butuh = "";          // induk yang diminta elemen di sebelah dalam
  for (let i = rantai.length - 1; i >= 0; i--) {
    const { tag, kelas, id, atribut } = uraiSederhana(rantai[i] as string);
    let nama = tag || "div";
    if (nama === "html" || nama === "body") nama = "div";
    /* Kalau yang di sebelah dalam menuntut induk tertentu dan pemilih ini
       TIDAK menyebut tag apa pun, pakai induk itu sebagai tagnya.
       `.menu > li` jadi <ul class="menu"><li>, bukan
       <div class="menu"><ul><li>. Bedanya menentukan: menyisipkan <ul> di
       tengah memutus hubungan "anak langsung", jadi aturannya tidak berlaku
       dan yang dilihat pelajar adalah CSS-nya seolah tidak bekerja. */
    if (butuh && !tag) nama = butuh;
    const sifat: string[] = [];
    if (kelas.length) sifat.push(` class="${kelas.join(" ")}"`);
    if (id) sifat.push(` id="${id}"`);
    for (const [k, v] of Object.entries(atribut)) {
      sifat.push(v ? ` ${k}="${v}"` : ` ${k}`);
    }
    if (butuh && nama !== butuh) {
      // Tagnya disebut eksplisit dan bukan induk yang sah; sisipkan induknya.
      dalam = `<${butuh}>${dalam}</${butuh}>`;
    }
    if (KOSONG.has(nama)) {
      dalam = `<${nama}${sifat.join("")}>` + dalam;
    } else {
      const isi = dalam || TEKS_CONTOH[nama] || TEKS_BAWAAN;
      dalam = `<${nama}${sifat.join("")}>${isi}</${nama}>`;
    }
    butuh = INDUK_WAJIB[nama] || "";
  }
  // Elemen terluar pun bisa menuntut induk (`li` sendirian, tanpa `ul`).
  if (butuh) dalam = `<${butuh}>${dalam}</${butuh}>`;
  return dalam;
}

/** Halaman contoh untuk sebuah lembar CSS. "" kalau tidak ada yang bisa dibuat. */
export function halamanDariCss(css: string): string {
  const sudah = new Set<string>();
  const potongan: string[] = [];
  for (const aturan of pemilihDi(css)) {
    for (const satu of aturan.split(",")) {
      const p = satu.trim();
      // `body`, `html`, `:root` memang mengenai halamannya sendiri -- CSS-nya
      // sudah dipasang di <head>, jadi tidak ada yang perlu dibuat untuknya.
      if (!p || /^(html|body|:root|\*)$/i.test(p)) continue;
      const kunci = p.replace(/\s+/g, " ");
      if (sudah.has(kunci)) continue;
      sudah.add(kunci);
      const x = contohUntuk(kunci);
      if (x) potongan.push(x);
      if (potongan.length >= MAKS_CONTOH) break;
    }
    if (potongan.length >= MAKS_CONTOH) break;
  }
  if (!potongan.length) return "";
  return `<!doctype html>
<html lang="id">
<head><meta charset="utf-8">
<style>
${css}
</style></head>
<body>
${potongan.join("\n")}
</body>
</html>`;
}

/** Apakah sebuah blok kode sudah berupa dokumen HTML utuh? */
export function adaMarkup(kode: string): boolean {
  return /<\s*(!doctype|html|body|div|p|h[1-6]|ul|ol|section|nav|header|footer|main|article|span|a|button|img|table|form)\b/i
    .test(kode);
}

/** Bahasa yang hasilnya lebih baik DILIHAT daripada dibaca sebagai teks. */
export function bisaDipratinjau(runner: string): boolean {
  return runner === "html" || runner === "css";
}

/** Dokumen yang harus dimuat ke bingkai untuk sebuah blok, atau "". */
export function dokumenPratinjau(runner: string, kode: string): string {
  if (runner === "html") return kode;
  if (runner !== "css") return "";
  // Materi CSS sering menulis halaman utuh ber-<style> di dalamnya; itu bukan
  // karangan siapa pun dan dipratinjau apa adanya.
  if (adaMarkup(kode)) return kode;
  return halamanDariCss(kode);
}

/** Apakah halamannya DIBUATKAN (bukan milik pelajar)? Menentukan labelnya. */
export function halamanDikarang(runner: string, kode: string): boolean {
  return runner === "css" && !adaMarkup(kode);
}
