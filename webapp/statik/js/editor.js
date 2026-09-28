/* Editor kode: textarea telanjang, disulap jadi editor yang enak dipakai.
 *
 * Kenapa bukan CodeMirror atau Monaco? Karena keduanya berarti megabita
 * dependensi, langkah build, dan janji "tanpa dependensi luar" yang batal.
 * Yang benar-benar dibutuhkan pemula sebenarnya sedikit dan bisa dibuat
 * sendiri: penyorotan, nomor baris, indentasi otomatis, kurung yang menutup
 * sendiri, dan Tab yang menambah indentasi alih-alih memindahkan fokus.
 *
 * Caranya: sebuah <textarea> berteks TRANSPARAN diletakkan persis di atas
 * <pre> berisi versi tersorot dari teks yang sama. Yang terlihat adalah
 * <pre>-nya; yang menerima ketikan adalah textarea-nya. Kursor asli browser
 * tetap dipakai lewat caret-color, jadi seleksi, seret, klik dua kali, dan
 * pembaca layar semuanya tetap bekerja seperti pada textarea biasa.
 *
 * Syarat mutlak penyelarasan itu: font, ukuran, tinggi baris, padding, dan
 * tab-size KEDUANYA harus sama persis. Beda satu piksel dan kursor akan
 * mendarat di huruf yang salah pada baris panjang. Semua nilai itu dikunci
 * berdampingan di gaya.css, pada blok `.editor-lapis > pre, > textarea`.
 *
 * Importir: layar-kerja.js.
 */

import { h, tunda } from "./inti.js";
import { animasi, adaGerak } from "./gerak.js";
import { token, keFragmen } from "./sorot.js";

const INDENT = "    ";                    // 4 spasi, konsisten dengan kurikulum
const TINGGI_MAKS = 0.62;                 // bagian dari tinggi jendela

/* Di atas lebar ini, editor yang diminta `isiRuang` berhenti mengukur dirinya
 * dari isi dan menyerahkan tingginya kepada tata letak.
 *
 * ANGKANYA HARUS SAMA dengan ambang `@container panggung (min-width: 1100px)`
 * di gaya.css — di sanalah ruang kerja latihan berubah jadi dua panel setinggi
 * jendela. Kalau keduanya berbeda, ada pita lebar tempat CSS memberi editornya
 * satu baris grid setinggi sisa layar sementara JS tetap memaksa tinggi hasil
 * pengukuran isi: yang terlihat editor pendek menggantung di dalam kotak
 * tinggi, atau sebaliknya editor yang meluber melewati kakinya.
 *
 * #panggung membentang selebar viewport (tidak ada kolom tetap di kirinya),
 * jadi innerWidth adalah pengganti yang cukup tepat untuk lebar containernya. */
const AMBANG_RUANG = 1100;

const PASANGAN = { "(": ")", "[": "]", "{": "}", '"': '"', "'": "'", "`": "`" };

const KOMENTAR = {
  python: "# ", javascript: "// ", java: "// ", c: "// ", cpp: "// ",
  go: "// ", bash: "# ", sql: "-- ", aplikasi: "// ",
  csharp: "// ", rust: "// ", kotlin: "// ", typescript: "// ",
  php: "// ", ruby: "# ", fedora: "# ",
  // Visual Basic memakai kutip TUNGGAL untuk komentar, bukan garis miring.
  vb: "' ",
  fedora: "# ",
};

function escapeRegex(s) {
  return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

export class Editor {
  /**
   * @param {object} opsi
   *   bahasa    kunci aturan penyorot
   *   kode      isi awal
   *   saatUbah  dipanggil (kode) setiap perubahan, sudah ditunda
   *   pintasan  { "ctrl+enter": fn, ... } — dijalankan sebelum perilaku bawaan
   *   isiRuang  true = tingginya diserahkan kepada tata letak, bukan diukur
   *             dari isi. Dipakai ruang kerja latihan; lihat _ukur().
   */
  constructor({ bahasa = "python", kode = "", saatUbah, pintasan = {},
                label = "Editor kode", isiRuang = false } = {}) {
    this.bahasa = bahasa;
    this.saatUbah = saatUbah;
    this.pintasan = pintasan;
    this.isiRuang = isiRuang;

    this.nomor = h("pre.editor-nomor", { "aria-hidden": "true" });
    this.sorotan = h("pre", { "aria-hidden": "true" });
    this.teks = h("textarea", {
      spellcheck: false, autocapitalize: "off", autocomplete: "off",
      wrap: "off", "aria-label": label,
    });
    this.lapis = h("div.editor-lapis", {}, this.sorotan, this.teks);

    this.jumlahBaris = h("span", {}, "1 baris");
    this.posisi = h("span", {}, "Brs 1, Kol 1");
    this.pesan = h("span.tersimpan", {});
    this.kaki = h("div.editor-kaki", {},
      this.posisi, this.jumlahBaris, this.pesan,
      h("span.sembunyi-hp", { gaya: { marginLeft: "auto" } },
        "Tab menambah indentasi · Ctrl+/ komentari"));

    this.el = h("div.editor", {}, this.nomor, this.lapis, this.kaki);

    this.teks.value = kode;
    // Chrome menaruh kursor di AKHIR teks setelah .value diisi, sehingga baris
    // terakhirlah yang tersorot di gutter sebelum editor disentuh sama sekali.
    // Yang benar adalah baris pertama: di situ mata mulai membaca.
    this.teks.setSelectionRange(0, 0);
    this._pasangPeristiwa();
    this.gambar();
  }

  /* --------------------------------------------------------------- isi */

  get nilai() { return this.teks.value; }

  set nilai(v) {
    const berubah = this.teks.value !== v;
    this.teks.value = v;
    this.gambar();
    // Isi editor hanya berganti sendiri karena satu sebab: sesuatu di luar
    // yang menggantinya — "Kerangka kosong", contoh dari materi, pindah bahasa
    // di ruang coba. Tanpa tanda apa pun, perubahan sebesar itu bisa terlewat
    // sama sekali kalau mata sedang di tempat lain di halaman.
    if (berubah && adaGerak()) {
      animasi(this.sorotan, { opacity: [0.35, 1] }, { durasi: 200 });
    }
  }

  fokus() {
    this.teks.focus();
    return this;
  }

  catat(pesan) {
    this.pesan.textContent = pesan || "";
    if (pesan) {
      // "tersimpan" muncul sendiri di kaki editor, jauh dari tempat mata
      // sedang mengetik. Satu gerakan pendek 6 px adalah satu-satunya cara ia
      // punya kesempatan tertangkap penglihatan tepi.
      animasi(this.pesan, {
        opacity: [0, 1],
        transform: ["translateY(4px)", "none"],
      }, { pegas: "jawab" });
      clearTimeout(this._catatId);
      this._catatId = setTimeout(() => { this.pesan.textContent = ""; }, 2600);
    }
  }

  /* ----------------------------------------------------------- tampilan */

  gambar() {
    const isi = this.teks.value;

    // Baris terakhir tidak akan terlihat kalau teksnya berakhir dengan
    // newline: <pre> memangkas satu baris kosong di ujung. Satu newline
    // tambahan menutup selisih itu, dan tidak pernah kelihatan karena ia
    // memang kosong.
    this.sorotan.textContent = "";
    this.sorotan.appendChild(keFragmen(token(isi, this.bahasa)));
    this.sorotan.appendChild(document.createTextNode("\n"));

    const baris = isi.split("\n");
    this._gambarNomor(baris.length);
    this.jumlahBaris.textContent = `${baris.length} baris`;
    this._ukur();
    this._selaraskan();
  }

  _gambarNomor(jumlah) {
    const kini = this._barisKursor();
    this.nomor.textContent = "";
    for (let i = 1; i <= jumlah; i++) {
      const teks = i + (i < jumlah ? "\n" : "");
      // Baris yang sedang disunting ditandai — di berkas 60 baris, tanpa itu
      // mudah kehilangan jejak posisi setelah menggulir.
      if (i === kini) this.nomor.appendChild(h("b", {}, teks));
      else this.nomor.appendChild(document.createTextNode(teks));
    }
  }

  _ukur() {
    // Di ruang kerja yang setinggi jendela, tinggi editor BUKAN urusan isinya.
    // Kerangka latihan tiga baris di atas empat ratus piksel ruang kosong
    // adalah ruang kerja yang menolak dipakai bekerja — jadi di sana tata
    // letak yang memberi tinggi, dan editor cuma mengisinya. Kelas
    // `.editor-isi-ruang` di gaya.css yang mengurus sisanya.
    if (this.isiRuang && window.innerWidth >= AMBANG_RUANG) {
      this.el.classList.add("editor-isi-ruang");
      this.teks.style.height = "100%";
      this.lapis.style.height = "100%";
      this.nomor.style.maxHeight = "";
      return;
    }
    this.el.classList.remove("editor-isi-ruang");

    // Tumbuh mengikuti isi sampai batas, lalu menggulir sendiri. Editor yang
    // tingginya tetap memaksa menggulir sejak baris pertama; yang tumbuh tanpa
    // batas mendorong tombol Periksa keluar layar.
    const maks = Math.round(window.innerHeight * TINGGI_MAKS);
    this.teks.style.height = "auto";
    const tinggi = Math.min(maks, Math.max(150, this.teks.scrollHeight));
    this.teks.style.height = tinggi + "px";
    this.lapis.style.height = tinggi + "px";
    this.nomor.style.maxHeight = tinggi + "px";
  }

  _selaraskan() {
    this.sorotan.scrollTop = this.teks.scrollTop;
    this.sorotan.scrollLeft = this.teks.scrollLeft;
    this.nomor.scrollTop = this.teks.scrollTop;
  }

  _perbaruiPosisi() {
    const sampai = this.teks.value.slice(0, this.teks.selectionStart);
    const baris = sampai.split("\n");
    this.posisi.textContent =
      `Brs ${baris.length}, Kol ${baris[baris.length - 1].length + 1}`;
  }

  _barisKursor() {
    return this.teks.value.slice(0, this.teks.selectionStart).split("\n").length;
  }

  _segarkanTanda() {
    this._perbaruiPosisi();
    this._gambarNomor(this.teks.value.split("\n").length);
  }

  /* ---------------------------------------------------------- peristiwa */

  _pasangPeristiwa() {
    const beritahu = tunda(() => {
      if (this.saatUbah) this.saatUbah(this.teks.value);
    }, 420);

    this.teks.addEventListener("input", () => { this.gambar(); beritahu(); });
    this.teks.addEventListener("scroll", () => this._selaraskan());
    this.teks.addEventListener("keyup", () => this._segarkanTanda());
    this.teks.addEventListener("click", () => this._segarkanTanda());
    this.teks.addEventListener("keydown", (e) => this._saatTombol(e));

    // Satu-satunya pendengar yang dipasang di luar elemen editor sendiri, dan
    // karena itu satu-satunya yang harus dilepas tangan. Penanganannya
    // disimpan supaya `lepas()` punya rujukan yang sama persis untuk dicabut —
    // `tunda()` mengembalikan fungsi BARU tiap dipanggil, jadi memanggilnya
    // dua kali menghasilkan dua fungsi berbeda dan removeEventListener tidak
    // akan mencopot apa pun.
    this._saatUkur = tunda(() => this._ukur(), 160);
    window.addEventListener("resize", this._saatUkur);
  }

  /** Lepaskan editor dari halaman.
   *
   *  WAJIB dipanggil dari `saatKeluar` layar yang memakainya. Tanpa itu,
   *  pendengar `resize` di atas tetap terdaftar dan memegang instance ini,
   *  yang memegang `this.el`, yang memegang seluruh pohon DOM layarnya —
   *  termasuk soal, hint, dan solusi contoh yang tadi diunduh. Tidak ada satu
   *  pun dari itu yang bisa dikumpulkan sampah selama tab masih terbuka. */
  lepas() {
    window.removeEventListener("resize", this._saatUkur);
    clearTimeout(this._catatId);
  }

  _saatTombol(e) {
    const kombinasi = [
      e.ctrlKey || e.metaKey ? "ctrl" : "",
      e.shiftKey ? "shift" : "",
      e.altKey ? "alt" : "",
      e.key.toLowerCase(),
    ].filter(Boolean).join("+");

    const fn = this.pintasan[kombinasi];
    if (fn) { e.preventDefault(); fn(); return; }

    if (kombinasi === "ctrl+/" || kombinasi === "ctrl+shift+7") {
      e.preventDefault(); this._alihKomentar(); return;
    }
    if (e.key === "Tab") { e.preventDefault(); this._tab(e.shiftKey); return; }
    if (e.key === "Enter") { e.preventDefault(); this._enter(); return; }
    if (e.key === "Backspace") { this._hapusMundur(e); return; }
    if (PASANGAN[e.key]) { this._kurung(e); return; }
    if (e.key === ")" || e.key === "]" || e.key === "}") { this._lewatiTutup(e); }
  }

  /* -------------------------------------------------------- penyuntingan */

  _sisip(teks, pilihMulai, pilihAkhir) {
    const t = this.teks;
    // setRangeText menjaga riwayat undo browser tetap utuh. Menulis ulang
    // t.value membuang seluruh riwayat itu, dan Ctrl+Z yang tidak berfungsi
    // adalah cara tercepat kehilangan kepercayaan pada sebuah editor.
    t.setRangeText(teks, t.selectionStart, t.selectionEnd, "end");
    if (pilihMulai !== undefined) {
      t.setSelectionRange(pilihMulai,
                          pilihAkhir === undefined ? pilihMulai : pilihAkhir);
    }
    this._sesudahUbah();
  }

  _sisipRentang(teks, awal, akhir, kursor) {
    this.teks.setRangeText(teks, awal, akhir, "end");
    this.teks.setSelectionRange(kursor, kursor);
    this._sesudahUbah();
  }

  _sesudahUbah() {
    this.gambar();
    this._perbaruiPosisi();
    if (this.saatUbah) this.saatUbah(this.teks.value);
  }

  _batasBaris() {
    const t = this.teks;
    const nilai = t.value;
    const awal = nilai.lastIndexOf("\n", t.selectionStart - 1) + 1;
    let akhir = nilai.indexOf("\n", t.selectionEnd);
    if (akhir < 0) akhir = nilai.length;
    return [awal, akhir];
  }

  _tab(mundur) {
    const t = this.teks;
    const banyakBaris =
      t.value.slice(t.selectionStart, t.selectionEnd).includes("\n");

    if (!banyakBaris && !mundur) { this._sisip(INDENT); return; }

    const [awal, akhir] = this._batasBaris();
    const blok = t.value.slice(awal, akhir);
    let geser = 0;
    const baru = blok.split("\n").map((baris, i) => {
      if (mundur) {
        const buang = baris.startsWith(INDENT)
          ? INDENT.length
          : (baris.match(/^(?: {1,3}|\t)/) || [""])[0].length;
        if (i === 0) geser = -buang;
        return baris.slice(buang);
      }
      if (i === 0) geser = INDENT.length;
      return baris.trim() ? INDENT + baris : baris;
    }).join("\n");

    const mulaiLama = t.selectionStart;
    const akhirLama = t.selectionEnd;
    t.setRangeText(baru, awal, akhir, "preserve");
    t.setSelectionRange(Math.max(awal, mulaiLama + geser),
                        akhirLama + (baru.length - blok.length));
    this.gambar();
    if (this.saatUbah) this.saatUbah(t.value);
  }

  _indentasiBaris(pos) {
    const nilai = this.teks.value;
    const awal = nilai.lastIndexOf("\n", pos - 1) + 1;
    return (nilai.slice(awal, pos).match(/^[ \t]*/) || [""])[0];
  }

  _enter() {
    const t = this.teks;
    const nilai = t.value;
    const pos = t.selectionStart;
    const luar = this._indentasiBaris(pos);
    let indentasi = luar;

    const sebelum = nilai.slice(0, pos).trimEnd();
    if (/[{[(:]$/.test(sebelum)) indentasi += INDENT;

    // Kursor tepat di antara sepasang kurung: buka jadi tiga baris, dengan
    // penutupnya sejajar pembukanya. Ini gerakan yang paling sering dilakukan
    // tangan dan paling melelahkan kalau harus manual.
    const kiri = nilai[pos - 1];
    const kanan = nilai[t.selectionEnd];
    if (kiri && kanan && PASANGAN[kiri] === kanan && "([{".includes(kiri)) {
      this._sisip("\n" + indentasi + "\n" + luar, pos + 1 + indentasi.length);
      return;
    }
    this._sisip("\n" + indentasi);
  }

  _kurung(e) {
    const t = this.teks;
    const buka = e.key;
    const tutup = PASANGAN[buka];
    const terpilih = t.value.slice(t.selectionStart, t.selectionEnd);

    if (terpilih) {           // bungkus yang sedang dipilih
      e.preventDefault();
      const awal = t.selectionStart;
      this._sisip(buka + terpilih + tutup, awal + 1, awal + 1 + terpilih.length);
      return;
    }

    // Kutip di tengah kata bukan pembuka string, melainkan apostrof: "don't",
    // "it's". Menutupnya otomatis di situ selalu salah.
    if (buka === tutup) {
      const kiri = t.value[t.selectionStart - 1] || "";
      const kanan = t.value[t.selectionStart] || "";
      if (kanan === buka) { e.preventDefault(); this._majuSatu(); return; }
      if (/[\w"'`]/.test(kiri) || /\w/.test(kanan)) return;
    }

    e.preventDefault();
    const pos = t.selectionStart;
    this._sisip(buka + tutup, pos + 1);
  }

  _lewatiTutup(e) {
    // Mengetik ")" tepat di depan ")" yang tadi dibuat otomatis: lewati saja,
    // jangan menumpuknya jadi "))".
    if (this.teks.selectionStart === this.teks.selectionEnd
        && this.teks.value[this.teks.selectionStart] === e.key) {
      e.preventDefault();
      this._majuSatu();
    }
  }

  _majuSatu() {
    const p = this.teks.selectionStart + 1;
    this.teks.setSelectionRange(p, p);
    this._perbaruiPosisi();
  }

  _hapusMundur(e) {
    const t = this.teks;
    if (t.selectionStart !== t.selectionEnd) return;
    const pos = t.selectionStart;

    // Hapus sepasang kurung kosong sekaligus.
    const kiri = t.value[pos - 1];
    const kanan = t.value[pos];
    if (kiri && PASANGAN[kiri] === kanan) {
      e.preventDefault();
      this._sisipRentang("", pos - 1, pos + 1, pos - 1);
      return;
    }
    // Di dalam indentasi, hapus satu tingkat penuh, bukan satu spasi.
    const awalBaris = t.value.lastIndexOf("\n", pos - 1) + 1;
    const depan = t.value.slice(awalBaris, pos);
    if (depan.length >= INDENT.length && !depan.trim()
        && depan.length % INDENT.length === 0) {
      e.preventDefault();
      this._sisipRentang("", pos - INDENT.length, pos, pos - INDENT.length);
    }
  }

  _alihKomentar() {
    const tanda = KOMENTAR[this.bahasa] || "# ";
    const potong = tanda.trimEnd();
    const t = this.teks;
    const [awal, akhir] = this._batasBaris();
    const blok = t.value.slice(awal, akhir);
    const baris = blok.split("\n");

    const berisi = baris.filter((b) => b.trim());
    const semuaKomentar = berisi.length > 0
      && berisi.every((b) => b.trimStart().startsWith(potong));

    const baru = baris.map((b) => {
      if (!b.trim()) return b;
      if (semuaKomentar) {
        return b.replace(
          new RegExp("^(\\s*)" + escapeRegex(potong) + " ?"), "$1");
      }
      const depan = (b.match(/^\s*/) || [""])[0];
      return depan + tanda + b.slice(depan.length);
    }).join("\n");

    t.setRangeText(baru, awal, akhir, "select");
    this.gambar();
    if (this.saatUbah) this.saatUbah(t.value);
  }
}
