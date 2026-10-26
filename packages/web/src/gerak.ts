/** Mesin gerak: pegas, urutan, pemicu, dan isyarat sentuhan.
 *
 *  Port `webapp/statik/js/gerak.js`. Satu modul untuk seluruh aplikasi, dan
 *  itu bukan kerapian: begitu ada tempat kedua yang memutuskan "seberapa
 *  cepat" atau "boleh bergerak atau tidak", dua permukaan akan berbeda
 *  pendapat tentang setelan yang sama.
 *
 *  Empat aturan yang mengikat SELURUH pemakainya, dan ketiganya sudah pernah
 *  dilanggar di repo ini dengan akibat yang tertulis di AGENTS.md:
 *
 *  1. **`tingkatGerak()` satu-satunya yang memutuskan**, dan
 *     `prefers-reduced-motion` sistem SELALU menang atas saklar di halaman.
 *  2. **Bingkai harus berakhir di keadaan ALAMI elemennya.** Kalau gerak
 *     dimatikan, `animasi()` tidak menyentuh apa pun -- jadi keadaan akhir
 *     sebuah animasi tidak boleh jadi satu-satunya cara elemen itu terlihat.
 *  3. **Siapa yang memasang `fill: "forwards"` wajib membatalkannya.** Ia
 *     memaksakan nilai akhirnya SELAMANYA, jadi animasi berikutnya yang
 *     selesai akan kalah lagi oleh yang lama.
 *  4. **Satu properti, satu mesin.** Kalau WAAPI menganimasikan sebuah
 *     properti, `transition` CSS untuk properti yang sama harus dilepas.
 */

/* ========================================================== bagian murni */

export const DETIK = 1000;

export function jepit(n: number, bawah = 0, atas = 1): number {
  return n < bawah ? bawah : n > atas ? atas : n;
}

export function antara(a: number, b: number, t: number): number {
  return a + (b - a) * t;
}

/** Petakan angka dari satu rentang ke rentang lain. */
export function petakan(
  nilai: number, dari: [number, number], ke: [number, number],
  { jepitHasil = true } = {},
): number {
  const [a0, a1] = dari;
  const [b0, b1] = ke;
  const t = a1 === a0 ? 0 : (nilai - a0) / (a1 - a0);
  const hasil = antara(b0, b1, t);
  if (!jepitHasil) return hasil;
  return b1 >= b0 ? jepit(hasil, b0, b1) : jepit(hasil, b1, b0);
}

/* ------------------------------------------------------------------ pegas
 *
 * Sebuah pegas dijelaskan dengan dua angka yang bisa DIBAYANGKAN:
 *
 *   durasiTampak  berapa detik sampai gerakannya TERLIHAT selesai
 *   pantul        0 = berhenti mulus, 0.3 = melewati tujuan sedikit lalu balik
 *
 * "Terlihat selesai" = saat pertama menempuh 99% jarak. Definisi itu dipilih
 * sesudah yang lebih jelas gagal: "waktu pertama MENYENTUH sasaran" punya
 * rumus tertutup yang rapi, tapi untuk pegas yang nyaris tak berpantul
 * kurvanya merayap ke sasaran secara asimtotik -- ia sudah 99,5% sampai jauh
 * sebelum itu, sehingga angka yang diminta tidak lagi mengendalikan apa pun
 * yang terlihat. Dengan pantul 0, "0,28 detik" dan "0,19 detik" keluar sebagai
 * animasi yang sama persis.
 */

export interface PerianPegas {
  durasiTampak?: number;
  pantul?: number;
  massa?: number;
  kecepatan?: number;
  kekakuan?: number;
  redaman?: number;
}

export const PEGAS: Record<string, PerianPegas> = {
  /* Menjawab sentuhan: secepat mungkin tanpa terasa mendadak. */
  jawab: { durasiTampak: 0.19, pantul: 0.05 },
  /* Bawaan untuk apa pun yang masuk ke layar. */
  halus: { durasiTampak: 0.28, pantul: 0.00 },
  /* Untuk hal yang layak dirayakan sedikit. Pantulnya dijaga di 0.26 karena
     pantulan itu mahal -- tiap tambahan pantul memperpanjang ekor pegasnya
     jauh lebih cepat daripada yang diduga. */
  lentur: { durasiTampak: 0.22, pantul: 0.26 },
  /* Untuk elemen besar yang berpindah tempat -- pantulan di benda besar
     terasa seperti kesalahan, bukan kelincahan. */
  berat: { durasiTampak: 0.40, pantul: 0.00 },
  /* Angka yang berjalan naik dan bilah kemajuan. */
  panjang: { durasiTampak: 0.60, pantul: 0.03 },
};

const PANTUL_BAWAAN = 0.06;
const DURASI_TAMPAK_BAWAAN = 0.3;

export interface ParamPegas {
  kekakuan: number;
  redaman: number;
  massa: number;
  kecepatan: number;
}

/** Terjemahkan pemerian pegas yang ramah manusia jadi parameter fisikanya. */
export function paramPegas(opsi: PerianPegas = {}): ParamPegas {
  const massa = (opsi.massa ?? 0) > 0 ? opsi.massa! : 1;
  const kecepatan = Number(opsi.kecepatan) || 0;

  if (opsi.kekakuan || opsi.redaman) {
    return {
      kekakuan: (opsi.kekakuan ?? 0) > 0 ? opsi.kekakuan! : 170,
      redaman: (opsi.redaman ?? -1) >= 0 ? opsi.redaman! : 26,
      massa,
      kecepatan,
    };
  }

  const durasiTampak = (opsi.durasiTampak ?? 0) > 0
    ? opsi.durasiTampak! : DURASI_TAMPAK_BAWAAN;
  const pantul = opsi.pantul === undefined ? PANTUL_BAWAAN : opsi.pantul;
  // zeta = 1 berarti teredam kritis. 0.99 sudah tak terbedakan dari 1 oleh
  // mata, dan menghindarkan cabang kasus khusus di dalam solvernya.
  const zeta = jepit(1 - pantul, 0.05, 0.99);
  const omega0 = tauSampai(zeta) / durasiTampak;

  return {
    kekakuan: massa * omega0 * omega0,
    redaman: 2 * zeta * massa * omega0,
    massa,
    kecepatan,
  };
}

const _tau = new Map<string, number>();

/** Pada kurva pegas satuan, di waktu berapa ia menembus 99%? */
export function tauSampai(zeta: number, ambang = 0.99): number {
  const kunci = `${zeta.toFixed(4)}|${ambang}`;
  const ada = _tau.get(kunci);
  if (ada !== undefined) return ada;

  const g = jalurPegas({ kekakuan: 1, redaman: 2 * zeta, massa: 1,
                         kecepatan: 0 });
  const langkah = 0.002;
  let hasil = 60;
  for (let t = 0; t <= 60; t += langkah) {
    if (g(t) >= ambang) { hasil = t; break; }
  }
  _tau.set(kunci, hasil);
  return hasil;
}

/** Fungsi t(detik) -> kemajuan 0..1 untuk sebuah pegas.
 *
 *  Bentuk tertutup, bukan integrasi langkah demi langkah: tiga kasus
 *  (teredam kurang, kritis, lebih) masing-masing punya penyelesaian eksak,
 *  dan memakai rumusnya berarti hasilnya tidak bergantung pada ukuran
 *  langkah. */
export function jalurPegas(p: ParamPegas): (t: number) => number {
  const { kekakuan, redaman, massa, kecepatan } = p;
  const omega0 = Math.sqrt(kekakuan / massa);
  const zeta = redaman / (2 * Math.sqrt(kekakuan * massa));

  if (zeta < 1 - 1e-6) {
    const omegaD = omega0 * Math.sqrt(1 - zeta * zeta);
    const b = (zeta * omega0 - kecepatan) / omegaD;
    return (t) => 1 - Math.exp(-zeta * omega0 * t)
      * (Math.cos(omegaD * t) + b * Math.sin(omegaD * t));
  }
  if (zeta < 1 + 1e-6) {
    return (t) => 1 - Math.exp(-omega0 * t)
      * (1 + (omega0 - kecepatan) * t);
  }
  const akar = omega0 * Math.sqrt(zeta * zeta - 1);
  const r1 = -zeta * omega0 + akar;
  const r2 = -zeta * omega0 - akar;
  const c1 = (-kecepatan - r2) / (r1 - r2);
  const c2 = 1 - c1;
  return (t) => 1 - (c1 * Math.exp(r1 * t) + c2 * Math.exp(r2 * t));
}

const _kurvaTersimpan = new Map<string, KurvaPegas>();

/* Di bawah 0,5% dari jarak tempuh, gerakan sudah lebih kecil daripada satu
   piksel untuk hampir semua animasi di aplikasi ini. Meneruskan sesudah itu
   cuma memperpanjang durasi tanpa ada yang melihat bedanya -- dan ekor pegas
   yang panjang itulah yang membuat animasi pegas terkenal terasa lamban
   padahal puncaknya sudah lewat sejak lama. */
const DIAM = 0.005;
const BATAS_DETIK = 6;

export interface KurvaPegas {
  durasi: number;
  easing: string;
  titik: number[];
  param: ParamPegas;
}

/** Ubah sebuah pegas jadi `{ durasi, easing }` yang bisa dipakai WAAPI.
 *
 *  easing-nya `linear(a, b, c, ...)`: daftar sampel kurva pegasnya. Browser
 *  menyambungkan titik-titik itu jadi kurva, dan karena hasilnya easing
 *  biasa, animasinya berjalan di compositor. */
export function kurvaPegas(opsi: PerianPegas = {}): KurvaPegas {
  const p = paramPegas(opsi);
  const kunci = `${p.kekakuan.toFixed(4)}|${p.redaman.toFixed(4)}`
    + `|${p.massa}|${p.kecepatan}`;
  const tersimpan = _kurvaTersimpan.get(kunci);
  if (tersimpan) return tersimpan;

  const f = jalurPegas(p);
  const langkah = 1 / 240;
  let akhir = langkah;
  for (let t = langkah; t <= BATAS_DETIK; t += langkah) {
    if (Math.abs(1 - f(t)) > DIAM) akhir = t;
  }
  akhir = Math.min(akhir + langkah * 2, BATAS_DETIK);

  // Satu titik tiap ~16 md sudah melewati apa yang bisa dibedakan mata pada
  // 60 Hz; batas atasnya menjaga panjang stringnya tetap wajar.
  const titik = Math.min(140, Math.max(8, Math.round(akhir * 60)));
  const nilai: number[] = [];
  for (let i = 0; i <= titik; i++) {
    nilai.push(Math.round(f((i / titik) * akhir) * 10000) / 10000);
  }
  nilai[0] = 0;
  nilai[titik] = 1;

  const hasil: KurvaPegas = {
    durasi: Math.max(1, Math.round(akhir * DETIK)),
    easing: `linear(${nilai.join(",")})`,
    titik: nilai,
    param: p,
  };
  _kurvaTersimpan.set(kunci, hasil);
  return hasil;
}

/* ----------------------------------------------------------------- urutan */

export interface OpsiUrut {
  mulai?: number;
  per?: number;
  dari?: "awal" | "akhir" | "tengah" | number;
  maks?: number;
}

/** Bangun fungsi indeks -> penundaan (md).
 *
 *  Bedanya dari `stagger()` di Motion satu: ada `maks`. Motion mengalikan
 *  jarak dengan penundaan begitu saja, jadi daftar 60 baris berarti baris
 *  terakhir menunggu dua detik. Di sini seluruh urutan dipadatkan supaya
 *  tidak pernah melewati `maks`. */
export function berurut(jumlah: number, opsi: OpsiUrut = {}): (i: number) => number {
  const { mulai = 0, per = 34, dari = "awal", maks = 300 } = opsi;
  const n = Math.max(1, jumlah);
  const pusat = dari === "akhir" ? n - 1
    : dari === "tengah" ? (n - 1) / 2
    : typeof dari === "number" ? dari : 0;
  const jarakMaks = Math.max(pusat, n - 1 - pusat) || 1;
  const langkah = Math.min(per, maks / jarakMaks);
  return (i) => mulai + Math.abs(i - pusat) * langkah;
}

/* ======================================================== bagian ber-DOM */

export type TingkatGerak = "penuh" | "halus" | "mati";

const ADA_DOM = typeof document !== "undefined"
  && typeof window !== "undefined";

const _kurangiGerak = ADA_DOM && typeof matchMedia === "function"
  ? matchMedia("(prefers-reduced-motion: reduce)")
  : null;

/* Browser yang belum mengenal easing `linear()` tetap harus dapat animasi,
   cuma tanpa pantulannya. */
const DUKUNG_LINEAR = ADA_DOM && typeof CSS !== "undefined"
  && typeof CSS.supports === "function"
  && CSS.supports("animation-timing-function", "linear(0, 1)");

export const MULUS = "cubic-bezier(.32,.72,.36,1)";
export const KELUAR = "cubic-bezier(.4,0,1,1)";

/** `"penuh"` | `"halus"` | `"mati"`. Setelan sistem menang atas apa pun. */
export function tingkatGerak(): TingkatGerak {
  if (!ADA_DOM) return "mati";
  if (_kurangiGerak?.matches) return "mati";
  const d = document.documentElement.dataset.gerak;
  if (d === "mati") return "mati";
  if (d === "halus") return "halus";
  return "penuh";
}

export const adaGerak = (): boolean => tingkatGerak() !== "mati";
export const gerakPenuh = (): boolean => tingkatGerak() === "penuh";

/** Pengali amplitudo. Di tingkat "halus" JARAKNYA dipendekkan, bukan
 *  durasinya diperlambat: gerakan pendek yang tetap cepat terasa tenang,
 *  gerakan panjang yang diperlambat justru terasa berat. */
export function skala(): number {
  const t = tingkatGerak();
  return t === "penuh" ? 1 : t === "halus" ? 0.45 : 0;
}

export function saatGerakBerubah(fn: (t: TingkatGerak) => void): () => void {
  if (!_kurangiGerak) return () => {};
  const bungkus = () => fn(tingkatGerak());
  _kurangiGerak.addEventListener("change", bungkus);
  return () => _kurangiGerak.removeEventListener("change", bungkus);
}

export type Sasaran = Element | ArrayLike<Element> | null | undefined;

function keDaftar(x: Sasaran): Element[] {
  if (!x || !ADA_DOM) return [];
  if (x instanceof Element) return [x];
  if (typeof (x as ArrayLike<Element>).length === "number") {
    return Array.from(x as ArrayLike<Element>).filter((e) => e instanceof Element);
  }
  return [];
}

export interface Kendali {
  animasi: Animation[];
  selesai: Promise<unknown>;
  batal(): void;
  tuntaskan(): void;
}

function kendaliKosong(): Kendali {
  return {
    animasi: [],
    selesai: Promise.resolve(),
    batal() {},
    tuntaskan() {},
  };
}

function gabungKendali(daftar: Kendali[]): Kendali {
  const semua = daftar.flatMap((k) => k.animasi);
  return {
    animasi: semua,
    selesai: Promise.all(daftar.map((k) => k.selesai)),
    batal() { for (const k of daftar) k.batal(); },
    tuntaskan() { for (const k of daftar) k.tuntaskan(); },
  };
}

export interface OpsiAnimasi {
  pegas?: string | PerianPegas;
  durasi?: number;
  delay?: number | ((i: number, n: number) => number);
  easing?: string;
  isi?: FillMode;
  ulang?: number;
  arah?: PlaybackDirection;
  gabung?: CompositeOperation;
  paksa?: boolean;
  saatSelesai?: () => void;
  geser?: number;
  zum?: number;
  jarak?: number;
}

/** Padanan `animate()` di Motion.
 *
 *  BINGKAI HARUS BERAKHIR DI KEADAAN ALAMI ELEMENNYA. Kalau gerak dimatikan,
 *  fungsi ini tidak menyentuh apa pun dan langsung selesai. */
export function animasi(
  sasaran: Sasaran, bingkai: Keyframe[] | PropertyIndexedKeyframes,
  opsi: OpsiAnimasi = {},
): Kendali {
  const daftar = keDaftar(sasaran);
  if (!daftar.length) return kendaliKosong();
  if (!adaGerak() && !opsi.paksa) return kendaliKosong();
  if (typeof daftar[0]!.animate !== "function") return kendaliKosong();

  let durasi = opsi.durasi;
  let easing = opsi.easing || MULUS;

  const minta = opsi.pegas;
  if (minta) {
    const k = kurvaPegas(typeof minta === "string" ? (PEGAS[minta] || {}) : minta);
    if (durasi === undefined) durasi = k.durasi;
    if (DUKUNG_LINEAR) easing = k.easing;
  }
  if (durasi === undefined) durasi = 220;

  const hitungDelay = typeof opsi.delay === "function"
    ? opsi.delay
    : () => (typeof opsi.delay === "number" ? opsi.delay : 0);

  const jalan = daftar.map((el, i) => el.animate(bingkai, {
    duration: durasi,
    delay: hitungDelay(i, daftar.length),
    easing,
    fill: opsi.isi || "backwards",
    iterations: opsi.ulang || 1,
    direction: opsi.arah || "normal",
    composite: opsi.gabung || "replace",
  }));

  // `finished` MENOLAK kalau animasinya dibatalkan. Itu bukan kesalahan --
  // membatalkan animasi adalah hal yang normal saat layar berganti -- jadi
  // jangan biarkan ia jadi unhandled rejection yang mengotori konsol.
  const selesai = Promise.all(jalan.map((a) => a.finished.catch(() => {})));
  if (opsi.saatSelesai) void selesai.then(() => opsi.saatSelesai!());

  return {
    animasi: jalan,
    selesai,
    batal() { for (const a of jalan) a.cancel(); },
    tuntaskan() {
      for (const a of jalan) { try { a.finish(); } catch { /* sudah usai */ } }
    },
  };
}

/* -------------------------------------------------------- masuk & keluar */

/** Satu elemen masuk: naik sedikit sambil muncul. Tidak ada yang meluncur
 *  dari samping -- itu memberi kesan halamannya berpindah tempat, padahal
 *  yang berganti cuma isinya. */
export function masuk(sasaran: Sasaran, opsi: OpsiAnimasi = {}): Kendali {
  const s = skala();
  const geser = (opsi.geser === undefined ? 10 : opsi.geser) * s;
  const zum = antara(1, opsi.zum === undefined ? 0.988 : opsi.zum, s);
  return animasi(sasaran, {
    opacity: [0, 1],
    transform: [
      `translate3d(0, ${geser.toFixed(2)}px, 0) scale(${zum.toFixed(4)})`,
      "none",
    ],
  }, { pegas: "halus", ...opsi });
}

/** Kebalikannya, untuk sesuatu yang akan dibuang. Sengaja lebih cepat
 *  daripada masuknya: menunggu sesuatu PERGI selalu terasa lebih lama
 *  daripada menunggu sesuatu datang. */
export function keluar(sasaran: Sasaran, opsi: OpsiAnimasi = {}): Kendali {
  const geser = (opsi.geser === undefined ? -7 : opsi.geser) * skala();
  return animasi(sasaran, {
    opacity: [1, 0],
    transform: ["none", `translate3d(0, ${geser.toFixed(2)}px, 0)`],
  }, { durasi: 130, easing: KELUAR, isi: "forwards", ...opsi });
}

/** Sekumpulan elemen masuk berurutan. */
export function masukBerurut(
  sasaran: Sasaran, opsi: OpsiAnimasi & OpsiUrut = {},
): Kendali {
  const daftar = keDaftar(sasaran);
  if (!daftar.length) return kendaliKosong();
  const delay = berurut(daftar.length, opsi);
  return gabungKendali(
    daftar.map((el, i) => masuk(el, { ...opsi, delay: delay(i) })));
}

/* ---------------------------------------------------------------- pemicu */

export interface OpsiTampak {
  tepi?: string;
  bagian?: number | number[];
  sekali?: boolean;
}

/** Padanan `inView()` di Motion. Callback boleh mengembalikan fungsi; fungsi
 *  itu dipanggil saat elemennya keluar lagi dari layar. */
export function saatTampak(
  sasaran: Sasaran,
  saatMasuk: (el: Element, c?: IntersectionObserverEntry) => void | (() => void),
  opsi: OpsiTampak = {},
): () => void {
  const daftar = keDaftar(sasaran);
  if (!daftar.length) return () => {};
  if (typeof IntersectionObserver === "undefined") {
    for (const el of daftar) saatMasuk(el);
    return () => {};
  }
  const { tepi = "0px 0px -6% 0px", bagian = 0.1, sekali = true } = opsi;
  const saatKeluar = new Map<Element, () => void>();

  const pengamat = new IntersectionObserver((catatan) => {
    for (const c of catatan) {
      if (c.isIntersecting) {
        const balik = saatMasuk(c.target, c);
        if (typeof balik === "function") saatKeluar.set(c.target, balik);
        if (sekali) pengamat.unobserve(c.target);
      } else {
        const balik = saatKeluar.get(c.target);
        if (balik) { balik(); saatKeluar.delete(c.target); }
      }
    }
  }, { rootMargin: tepi, threshold: bagian });

  for (const el of daftar) pengamat.observe(el);
  return () => pengamat.disconnect();
}

/* Pengaman: kalau pengamatnya tidak pernah menyala, apa pun yang sempat
   disembunyikan harus muncul kembali sendiri. Elemen yang tak terlihat
   selamanya adalah kegagalan yang jauh lebih buruk daripada animasi yang
   terlewat.

   TAPI pengaman ini tidak boleh ASAL menyala. Versi pertamanya di sisi JS
   mengosongkan opacity SEMUA anak pada detik 2,5 tanpa mematikan pemicunya --
   termasuk anak yang masih di bawah lipatan dan masih diamati. Akibatnya:
   pembaca menggulir turun, bagian itu tergambar penuh dulu, lalu callback
   pengamatnya menyala dan menjatuhkannya kembali ke opacity 0 sebelum memudar
   naik lagi. Itu KEDIPAN, tepat di bawah mata orang yang sedang membaca.

   Yang benar: pengamannya bertanya "apakah pengamat ini pernah menyala sama
   sekali?". Kalau pernah, biarkan sisanya diungkap saat tergulir. */
const JAGA_MD = 2500;

/** Ungkap anak-anak sebuah wadah begitu tergulir ke layar, berurutan. */
export function ungkap(
  wadah: Sasaran,
  opsi: OpsiAnimasi & OpsiUrut & OpsiTampak & { pilih?: string } = {},
): () => void {
  const induk = keDaftar(wadah)[0];
  if (!induk) return () => {};
  const anak = keDaftar(opsi.pilih ? induk.querySelectorAll(opsi.pilih)
                                   : induk.children);
  if (!anak.length || !adaGerak()) return () => {};

  for (const el of anak) (el as HTMLElement).style.opacity = "0";
  const delay = berurut(anak.length, opsi);
  const nomor = new Map(anak.map((el, i) => [el, i] as const));

  let pernahMenyala = false;
  let menyerah = false;
  let hentikan: () => void = () => {};

  const jaga = setTimeout(() => {
    if (pernahMenyala) return;
    menyerah = true;
    hentikan();
    for (const el of anak) (el as HTMLElement).style.opacity = "";
  }, JAGA_MD);

  hentikan = saatTampak(anak, (el) => {
    if (menyerah) return;
    pernahMenyala = true;
    (el as HTMLElement).style.opacity = "";
    masuk(el, { ...opsi, delay: delay(nomor.get(el) ?? 0) });
  }, opsi);

  return () => { clearTimeout(jaga); hentikan(); };
}

/* ------------------------------------------------------------------ FLIP */

/** Jalankan `ubah()` lalu animasikan elemen dari tempat LAMANYA ke tempat
 *  barunya. Tata letaknya berubah seketika; yang bergerak cuma transformnya,
 *  jadi tidak ada layout yang dihitung ulang tiap frame. */
export function tata(
  sasaran: Sasaran, ubah: () => void, opsi: OpsiAnimasi = {},
): Kendali {
  const daftar = keDaftar(sasaran);
  if (!daftar.length || !adaGerak()) {
    ubah();
    return kendaliKosong();
  }
  const sebelum = daftar.map((el) => el.getBoundingClientRect());
  ubah();

  const kendali: Kendali[] = [];
  daftar.forEach((el, i) => {
    const a = sebelum[i]!;
    const b = el.getBoundingClientRect();
    const dx = a.left - b.left;
    const dy = a.top - b.top;
    const sx = b.width > 0 ? a.width / b.width : 1;
    const sy = b.height > 0 ? a.height / b.height : 1;
    const diam = Math.abs(dx) < 0.5 && Math.abs(dy) < 0.5
      && Math.abs(sx - 1) < 0.005 && Math.abs(sy - 1) < 0.005;
    if (diam) return;
    kendali.push(animasi(el, {
      transform: [
        `translate3d(${dx.toFixed(2)}px, ${dy.toFixed(2)}px, 0)`
        + ` scale(${sx.toFixed(4)}, ${sy.toFixed(4)})`,
        "none",
      ],
    }, { pegas: "jawab", ...opsi }));
  });
  return gabungKendali(kendali);
}

/* --------------------------------------------------------- isyarat sentuh */

const BISA_TUNJUK = ADA_DOM && typeof matchMedia === "function"
  && matchMedia("(hover: hover) and (pointer: fine)").matches;

/* Permukaan yang menjawab saat ditekan. Semuanya elemen yang memang bisa
   diklik — menganimasikan yang lain cuma menjanjikan sesuatu yang tidak
   terjadi. */
export const BISA_DITEKAN =
  ".tbl, .baris, .opsi button, .kartu[href], .palet-item, .sakelar,"
  + " .rel-menu a, .tanda, .ikon-tombol, .medali.punya,"
  // Dua permukaan navbar yang sebelumnya diam saat ditekan padahal semua
  // tetangganya menjawab. Ditambahkan di sini, bukan dengan memanggil WAAPI
  // dari komponennya: pasangIsyarat() yang memegang pasangan tekan/lepas,
  // dan hanya lewat jalur itu pembatalannya dijamin.
  + " .rel-tombol, .rel-pemicu,"
  // `.pil[href]`, bukan `.pil`. Dari 58 pil di aplikasi ini, 56 adalah LABEL
  // statis ("dinilai otomatis", "terkunci", "5x dikerjakan") dan hanya 2 yang
  // berupa tautan. Memberi fisika tekan pada seluruh `.pil` membuat lima
  // puluh enam penanda mengecil saat disentuh lalu tidak melakukan apa-apa --
  // kebalikan dari janji bahwa yang menjawab sentuhan itu bisa ditekan.
  + " .pil[href], .ubin,"
  // Kepala bab adalah `<summary>`, dan ia satu-satunya permukaan besar di
  // halaman bahasa yang diam saat ditekan padahal seluruh tetangganya
  // menjawab. Didaftarkan di sini, BUKAN dengan memanggil tekan() dari
  // komponennya: `pasangIsyarat()` yang memegang pasangan tekan/lepas, dan
  // hanya lewat jalur itu pembatalannya dijamin (invarian #1).
  //
  // Aman untuk papan ketik tanpa syarat tambahan: jalur ini cuma menumpang
  // pointerdown/pointerup/pointercancel, jadi Enter pada `<summary>` — yang
  // memang cara membukanya dengan papan ketik — tidak pernah memicu tekan()
  // dan tidak ada animasi mengecil yang bisa tertinggal tanpa pasangannya.
  + " .bab-kepala";

const _tekanan = new WeakMap<Element, Kendali>();

/** Elemen di dalam sebuah `<svg>`. Ruang nama, bukan `instanceof SVGElement`:
 *  berkas ini diimpor juga oleh pembanding Node yang tidak punya kelas itu. */
const SVG_NS = "http://www.w3.org/2000/svg";
const elemenSvg = (el: Element): boolean => el.namespaceURI === SVG_NS;

function skalaTekan(opsi: { skala?: number }): number {
  const dasar = opsi.skala === undefined ? 0.975 : opsi.skala;
  return 1 - (1 - dasar) * skala();
}

/** Tekan sekali: mengecil sedikit, lalu memantul balik dengan pegas. Kesan
 *  yang ditinggalkan bukan "ada animasi" melainkan "benda ini PADAT".
 *
 *  Hidup di tingkat "halus" juga, dan itu bukan kelonggaran: umpan balik
 *  sentuhan justru SATU-SATUNYA alasan tingkat tengah itu ada. Kalau ia ikut
 *  padam di situ, "halus" tidak ada bedanya dengan "mati".
 *
 *  TIDAK PERNAH menyentuh elemen SVG. Properti CSS `transform` menimpa atribut
 *  `transform` bawaannya, jadi sebuah `<g transform="translate(x,y)">` yang
 *  ditekan kehilangan `translate`-nya dan melompat ke titik asal `viewBox` --
 *  dengan `fill: "forwards"` ia TERPARKIR di sana. Terukur di Peta Karier:
 *  node berpindah dari (184, 60) ke (-13, -13) saat tombol ditekan, dan
 *  `pointerup` lalu mendarat di elemen LAIN karena node itu sudah tidak ada di
 *  bawah kursor -- jadi pelepasnya tidak pernah menemukannya. Klik mouse tidak
 *  bisa memilih node sama sekali. Daftar `BISA_DITEKAN` memang tidak memuat
 *  elemen SVG; pagar ini lapis kedua, untuk kelas yang ditambahkan belakangan. */
export function tekan(el: Element | null, opsi: { skala?: number } = {}): void {
  if (!adaGerak() || !el || elemenSvg(el)) return;
  const kecil = skalaTekan(opsi);
  // fill "forwards" WAJIB: selama jarinya masih menempel, tombolnya harus
  // tetap kecil, bukan memantul balik sendiri setelah 90 md.
  _tekanan.set(el, animasi(el, { transform: ["none", `scale(${kecil})`] },
    { durasi: 90, easing: KELUAR, isi: "forwards" }));
}

export function lepas(el: Element | null, opsi: { skala?: number } = {}): void {
  if (!el) return;
  // Membatalkan yang menekan adalah KEHARUSAN, bukan kerapian. Animasi
  // ber-fill "forwards" memaksakan nilai akhirnya selamanya, jadi begitu
  // animasi memantul di bawah selesai, yang menekan akan menang lagi dan
  // tombolnya tinggal mengecil 2,5% untuk seterusnya. Satu tombol tidak
  // kelihatan; tiga puluh tombol dalam satu sesi membuat seluruh antarmuka
  // pelan-pelan menyusut.
  //
  // Dibatalkan SEBELUM memeriksa tingkat gerak: kalau gerak dimatikan tepat
  // di antara menekan dan melepas, yang menekan tetap harus dilepaskan.
  const menekan = _tekanan.get(el);
  if (menekan) { menekan.batal(); _tekanan.delete(el); }
  if (!adaGerak() || elemenSvg(el)) return;

  animasi(el, { transform: [`scale(${skalaTekan(opsi)})`, "none"] },
          { pegas: "lentur" });
}

/** Pasang isyarat tekan untuk SELURUH aplikasi lewat satu pendengar.
 *
 *  Port `pasangIsyarat()` dari `gerak.js`, dan inilah yang dulu terlewat:
 *  versi pertama cangkang React memasang penangan sendiri yang memilih sasaran
 *  dengan `button, a, [role="button"]` lalu melepas `closest(target)` saat
 *  `pointerup`. Dua-duanya salah. Daftar putih `BISA_DITEKAN` adalah janji
 *  bahwa yang menjawab sentuhan memang bisa ditekan, dan yang dilepas harus
 *  elemen yang DITEKAN -- bukan elemen yang kebetulan ada di bawah kursor saat
 *  jari diangkat, yang bisa saja bukan elemen yang sama.
 *
 *  Mengembalikan pelepas, beda dari versi JS yang memasang pendengarnya
 *  sekali dan selamanya: efek React dijalankan dua kali di StrictMode. */
export function pasangIsyarat(): () => void {
  if (!ADA_DOM) return () => {};

  let ditekan: Element | null = null;

  const turun = (e: PointerEvent) => {
    if (!adaGerak()) return;
    if (e.button !== 0 && e.pointerType === "mouse") return;
    if (!(e.target instanceof Element)) return;
    const el = e.target.closest(BISA_DITEKAN);
    if (!el || el.hasAttribute("disabled")) return;
    if (el.closest("[data-gerak-lewat]")) return;
    ditekan = el;
    tekan(el);
  };

  const selesaikan = () => {
    if (!ditekan) return;
    lepas(ditekan);
    ditekan = null;
  };

  const opsi = { passive: true } as const;
  document.addEventListener("pointerdown", turun, opsi);
  document.addEventListener("pointerup", selesaikan, opsi);
  document.addEventListener("pointercancel", selesaikan, opsi);
  // Kursor yang keluar dari tombol sambil ditekan tidak memicu pointerup di
  // atas tombol itu. `selesaikan` melepas elemen yang DITEKAN di mana pun
  // jarinya diangkat, jadi tombolnya tidak tertinggal mengecil.
  document.addEventListener("pointerleave", selesaikan, opsi);

  // Pelepasan dicocokkan lewat `capture` saja (bawaan false, sama dengan
  // pemasangan), jadi `passive` tidak perlu -- dan tipenya memang menolaknya.
  return () => {
    document.removeEventListener("pointerdown", turun);
    document.removeEventListener("pointerup", selesaikan);
    document.removeEventListener("pointercancel", selesaikan);
    document.removeEventListener("pointerleave", selesaikan);
    // Pelepas yang meninggalkan tombol dalam keadaan ditekan adalah pelepas
    // yang membuat tombol itu mengecil selamanya.
    selesaikan();
  };
}

/** Getar mendatar -- untuk jawaban salah dan penolakan. Amplitudonya kecil
 *  dan simetris: ini isyarat "bukan itu", bukan hukuman. */
export function getar(el: Element | null, opsi: OpsiAnimasi = {}): Kendali {
  const s = skala();
  if (!s || !el) return kendaliKosong();
  const a = (opsi.jarak === undefined ? 5 : opsi.jarak) * s;
  return animasi(el, {
    transform: ["none", `translateX(${-a}px)`, `translateX(${a * 0.8}px)`,
                `translateX(${-a * 0.4}px)`, "none"],
  }, { durasi: 300, easing: "ease-in-out", ...opsi });
}

/** Denyut SEKALI -- untuk menarik mata ke sesuatu yang baru saja berubah.
 *  Tidak berulang: apa pun yang berdenyut terus akan diabaikan dalam satu
 *  menit dan mengganggu selamanya sesudahnya. */
export function denyut(el: Element | null, opsi: OpsiAnimasi = {}): Kendali {
  const s = skala();
  if (!s || !el) return kendaliKosong();
  const besar = 1 + 0.028 * s;
  return animasi(el, {
    transform: ["none", `scale(${besar.toFixed(4)})`, "none"],
  }, { durasi: 340, easing: "ease-in-out", ...opsi });
}

/** Tombol utama mengikuti kursor beberapa piksel. Jaraknya sengaja KECIL:
 *  yang dicari kesan "benda ini sadar kamu di sini", bukan benda yang lari
 *  dari kursor. Mati di layar sentuh -- di sana tidak ada kursor. */
export function magnet(
  el: HTMLElement | null, opsi: { kuat?: number } = {},
): () => void {
  if (!el || !BISA_TUNJUK) return () => {};
  const kuat = opsi.kuat === undefined ? 3 : opsi.kuat;
  let dipasang = false;

  const gerakkan = (e: PointerEvent) => {
    if (!gerakPenuh()) return;
    const r = el.getBoundingClientRect();
    const x = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
    const y = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
    el.style.transform =
      `translate3d(${(jepit(x, -1, 1) * kuat).toFixed(2)}px,`
      + ` ${(jepit(y, -1, 1) * kuat * 0.6).toFixed(2)}px, 0)`;
    dipasang = true;
  };

  const lepaskan = () => {
    if (!dipasang) return;
    dipasang = false;
    const dari = el.style.transform;
    el.style.transform = "";
    animasi(el, { transform: [dari, "none"] }, { pegas: "lentur" });
  };

  el.addEventListener("pointermove", gerakkan);
  el.addEventListener("pointerleave", lepaskan);
  el.addEventListener("pointerdown", lepaskan);
  return () => {
    el.removeEventListener("pointermove", gerakkan);
    el.removeEventListener("pointerleave", lepaskan);
    el.removeEventListener("pointerdown", lepaskan);
    el.style.transform = "";
  };
}
