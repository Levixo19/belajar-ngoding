/** Saluran umpan balik NON-VISUAL: bunyi sintetis dan haptik perangkat.
 *
 *  Port `webapp/statik/js/suara.js`, nol dependensi seperti aslinya. Satu
 *  modul untuk dua saluran, dan itu bukan penghematan baris: keduanya
 *  menjawab pertanyaan yang sama -- "bolehkah aplikasi ini mengganggu orang
 *  lewat indra selain mata?" -- dan tunduk pada satu kebijakan yang tidak
 *  boleh punya dua rumusan: BAWAAN MATI, dan tidak pernah jadi satu-satunya
 *  cara mengetahui apa pun.
 *
 *  Yang SENGAJA tidak ada, sama seperti aslinya: nol aset dan nol pustaka
 *  (tiga isyarat dibangkitkan osilator, nol byte di disk), nol bunyi per
 *  penekanan tombol, nol bunyi per jawaban kuis termasuk yang salah, dan nol
 *  fanfare.
 *
 *  Kunci localStorage-nya DIBAGI dengan antarmuka lama -- `belajar.suara` dan
 *  `belajar.getarPerangkat`, dibaca MENTAH persis seperti aslinya, bukan lewat
 *  `lokal.ts`. Itu disengaja: `bacaSuara` punya aturan jatuh-ke-"mati" yang
 *  tidak sama dengan `ambilLokal`, dan dua pembaca dengan aturan jatuh yang
 *  berbeda berarti setelan rusak yang membunyikan aplikasi di satu antarmuka
 *  dan membisukannya di antarmuka lain.
 */

const KUNCI_TINGKAT = "belajar.suara";
const KUNCI_GETAR = "belajar.getarPerangkat";

export type TingkatSuara = "mati" | "halus" | "penuh";

/** Tiga tingkat, dan yang tengah bukan kompromi malas. Saklar dua posisi
 *  memaksa orang yang cuma tidak ingin diberi selamat untuk ikut membuang
 *  isyarat naik level -- padahal naik level memang jarang dan memang layak
 *  ditandai. */
export const SUARA: Array<[TingkatSuara, string, string]> = [
  ["mati", "Mati",
   "Tidak ada bunyi sama sekali. Ini bawaannya."],
  ["halus", "Halus",
   "Hanya peristiwa yang jarang: naik level dan badge baru. "
   + "XP yang bertambah tetap diam."],
  ["penuh", "Penuh",
   "Naik level, badge baru, dan satu nada pendek tiap kali XP bertambah."],
];

/** Satu-satunya yang berhak memutuskan tingkat suara. Kembarannya
 *  `tingkatGerak()`, dan alasannya sama.
 *
 *  `prefers-reduced-motion` TIDAK ikut memutuskan di sini: orang yang memakai
 *  pembaca layar sering justru meminta gerak dikurangi sambil tetap mau
 *  mendengar konfirmasi, dan orang yang bekerja di ruang terbuka ingin
 *  kebalikannya. Keduanya sah, dan satu saklar tidak bisa melayani keduanya.
 *
 *  Nilai yang tidak dikenal jatuh ke "mati", bukan "penuh". Sisi salahnya
 *  dipilih: setelan rusak yang membuat aplikasi diam cuma membingungkan,
 *  setelan rusak yang membuatnya berbunyi di ruang rapat tidak bisa
 *  dibatalkan sesudah terjadi. */
export function bacaSuara(): TingkatSuara {
  let mentah: string | null = null;
  try { mentah = localStorage.getItem(KUNCI_TINGKAT); } catch { return "mati"; }
  if (mentah === null) return "mati";
  let nilai: unknown = mentah;
  try { nilai = JSON.parse(mentah); } catch { /* nilai mentah, pakai apa adanya */ }
  return SUARA.some((s) => s[0] === nilai) ? (nilai as TingkatSuara) : "mati";
}

/** Saklar haptik BERDIRI SENDIRI -- ia bukan tingkat keempat dari `suara`.
 *  Telepon di saku di kereta adalah tempat getar berguna dan bunyi tidak
 *  sopan; laptop di meja adalah kebalikannya tepat. */
export function bacaGetar(): boolean {
  try { return localStorage.getItem(KUNCI_GETAR) === "true"; }
  catch { return false; }
}

export function setelSuara(
  { suara, getarPerangkat }: {
    suara?: TingkatSuara; getarPerangkat?: boolean;
  } = {},
): { suara: TingkatSuara; getarPerangkat: boolean } {
  try {
    if (suara !== undefined && SUARA.some((s) => s[0] === suara)) {
      localStorage.setItem(KUNCI_TINGKAT, JSON.stringify(suara));
    }
    if (getarPerangkat !== undefined) {
      localStorage.setItem(KUNCI_GETAR, String(Boolean(getarPerangkat)));
    }
  } catch { /* mode penyamaran atau kuota penuh: abaikan */ }
  return { suara: bacaSuara(), getarPerangkat: bacaGetar() };
}

/* ------------------------------------------------------------ mesin bunyi */

/* Peramban MENOLAK membuat AudioContext yang berbunyi sebelum ada gestur
   asli, dan konteks yang ditolak masuk ke keadaan "suspended" selamanya --
   jadi membuatnya di tingkat modul bukan cuma sia-sia, ia menukar
   satu-satunya konteks yang akan pernah ada dengan konteks yang mati. Karena
   itu ia dibuat LAZILY, dan saat idle ia di-`suspend()`, bukan `close()`.
   `close()` tidak bisa dibatalkan. */
let konteks: AudioContext | null = null;
let plafon: GainNode | null = null;
let hidup = 0;
let jamIdle: ReturnType<typeof setTimeout> | null = null;

const IDLE_MS = 20000;
/* Dua isyarat bersamaan masih terbaca sebagai dua kejadian; tiga terbaca
   sebagai satu akor. Yang ketiga DIBUANG, bukan diantre -- isyarat yang
   datang 300 md terlambat menjelaskan kejadian yang sudah lewat dari layar. */
const MAKS_BARENG = 2;

/** Ada gestur yang sah? Deteksi fitur, tanpa satu pun pendengar di tingkat
 *  modul: pendengar global berarti berkas ini menyentuh `document` saat
 *  diimpor, dan yang dijaga bukan "tidak melempar" melainkan "tidak
 *  menyentuh". */
function adaGestur(): boolean {
  const nav = globalThis.navigator as
    (Navigator & { userActivation?: { hasBeenActive: boolean } }) | undefined;
  const ua = nav?.userActivation;
  return ua ? Boolean(ua.hasBeenActive) : true;
}

/** Kelas AudioContext yang tersedia, dibaca dari `window`.
 *
 *  Dari `window`, BUKAN `globalThis`, dan itu bukan selera: di peramban
 *  keduanya objek yang sama, jadi perbedaannya mustahil diamati di sana --
 *  tapi driver uji di `tests/test_web.py` menstub `globalThis.window` saja,
 *  dan versi yang membaca `globalThis` tidak menemukan kelasnya sama sekali.
 *  Yang terjadi bukan error melainkan mesin audio yang diam-diam tidak pernah
 *  menyala, dan kontrol positif driver itulah yang menangkapnya. Perbedaan
 *  yang tidak bisa diamati di peramban tetap perbedaan. */
function Konteks(): typeof AudioContext | null {
  if (typeof window === "undefined") return null;
  const w = window as unknown as {
    AudioContext?: typeof AudioContext;
    webkitAudioContext?: typeof AudioContext;
  };
  return w.AudioContext ?? w.webkitAudioContext ?? null;
}

function pastikanKonteks(): AudioContext | null {
  if (konteks) return konteks;
  const Kelas = Konteks();
  if (!Kelas) return null;
  try {
    konteks = new Kelas();
    /* SATU GainNode master sebagai plafon, dan tiap isyarat menggantung di
       bawahnya. Tanpa plafon, "agak terlalu keras" cuma bisa dibetulkan
       dengan menyunting tiap isyarat satu per satu -- dan satu yang terlewat
       cukup untuk membuat seluruh setelan terasa tidak bekerja. */
    plafon = konteks.createGain();
    plafon.gain.value = 0.085;
    plafon.connect(konteks.destination);
  } catch {
    konteks = null;
    plafon = null;
  }
  return konteks;
}

function tundaIdle(): void {
  if (jamIdle) clearTimeout(jamIdle);
  jamIdle = setTimeout(() => {
    jamIdle = null;
    if (konteks && hidup === 0 && konteks.state === "running") {
      try { void konteks.suspend(); } catch { /* sudah ditutup peramban */ }
    }
  }, IDLE_MS);
}

interface Nada { hz: number; lama: number; pada?: number; puncak?: number }

/** Satu nada berselubung, dijadwalkan seluruhnya lewat `AudioParam`.
 *
 *  Amplopnya TIDAK digerakkan putaran `requestAnimationFrame`: penjadwal
 *  audio berjalan di utasnya sendiri dengan ketepatan sub-milidetik,
 *  sementara rAF berhenti total saat tab tidak terlihat -- dan isyarat yang
 *  amplopnya berhenti di tengah adalah nada yang menggantung sampai tabnya
 *  dibuka lagi.
 *
 *  Serangannya 8 md dan peredamannya eksponensial. Nada yang mulai seketika
 *  menghasilkan klik di awal, dan peredaman linier menuju nol terdengar
 *  dipotong, bukan selesai. */
function nada(mulai: number, { hz, lama, puncak = 1 }: Nada): OscillatorNode {
  const ctx = konteks!;
  const osc = ctx.createOscillator();
  const amp = ctx.createGain();
  osc.type = "sine";
  osc.frequency.setValueAtTime(hz, mulai);
  amp.gain.setValueAtTime(0.0001, mulai);
  amp.gain.linearRampToValueAtTime(puncak, mulai + 0.008);
  amp.gain.exponentialRampToValueAtTime(0.0001, mulai + lama);
  osc.connect(amp);
  amp.connect(plafon!);
  osc.start(mulai);
  osc.stop(mulai + lama + 0.02);
  return osc;
}

/* Tiga isyarat, tiap-tiapnya <= 120 md. Angkanya bukan selera: lebih panjang
   dari itu dan bunyinya mulai terdengar sebagai MUSIK -- sesuatu yang punya
   awal, tengah, dan akhir, yang karena itu menuntut didengarkan sampai habis.
   Yang dibutuhkan di sini cuma tanda baca. Nadanya dari satu triad supaya
   ketiganya terdengar berasal dari satu keluarga. */
const ISYARAT: Record<string, Nada[]> = {
  // Naik level atau badge baru. Dua nada NAIK, karena arah naik satu-satunya
  // hal yang bisa dibedakan telinga tanpa dilatih lebih dulu.
  acara: [{ hz: 587.33, lama: 0.055, pada: 0 },
          { hz: 880.00, lama: 0.075, pada: 0.045 }],
  // XP bertambah. Nada TENGAH triad-nya: terdengar sebagai bagian keluarga
  // yang sama tanpa terdengar sebagai kesimpulan.
  capai: [{ hz: 739.99, lama: 0.07, pada: 0 }],
  // Peragaan di kartu Pengaturan. Sama dengan `capai` supaya yang didengar
  // orang saat memilih memang yang akan ia dengar sesudahnya.
  contoh: [{ hz: 739.99, lama: 0.07, pada: 0 }],
};

/* Tingkat mana yang membunyikan isyarat mana. Tabel, bukan rantai `if`:
   pertanyaan "apa yang terdengar di 'halus'?" harus bisa dijawab dengan
   membaca satu baris. */
const IZIN: Record<TingkatSuara, string[]> = {
  mati: [],
  halus: ["acara"],
  penuh: ["acara", "capai", "contoh"],
};

/** Bunyikan satu isyarat, kalau tingkatnya mengizinkan.
 *
 *  Yang dimatikan pada tingkat "mati" adalah JALUR PANGGILNYA, bukan
 *  volumenya: fungsi ini keluar sebelum `pastikanKonteks()`, jadi peramban
 *  orang yang mematikan suara tidak pernah membuat AudioContext sama sekali.
 *  Menyetel plafon ke nol akan "terdengar" sama tapi tetap menyalakan mesin
 *  audio, dan mesin audio yang menyala adalah daya yang terpakai untuk
 *  menghasilkan keheningan.
 *
 *  DIEKSPOR, tapi bukan untuk layar. Di antarmuka lama `inti.js` berdiri di
 *  tengah dan sengaja TIDAK meneruskan fungsi ini; di React tidak ada
 *  perantara semacam itu, jadi kebijakannya dijaga sapuan
 *  `test_konten_json.test_layar_tidak_memanggil_isyarat_langsung` alih-alih
 *  oleh ketiadaan. Alasan kebijakannya tidak berubah: layar yang bisa
 *  memanggilnya langsung adalah layar yang bisa mengarang bunyi barunya
 *  sendiri, dan pada saat itu "tiga tingkat" berhenti menggambarkan apa yang
 *  terdengar. Yang diekspor juga dituntut driver uji suara, yang menagih
 *  permukaan ekspor modul ini sama dengan `suara.js`. */
export function isyarat(jenis: string): boolean {
  const tingkat = bacaSuara();
  if (!(IZIN[tingkat] || []).includes(jenis)) return false;
  if (!ISYARAT[jenis]) return false;
  if (hidup >= MAKS_BARENG) return false;
  if (!adaGestur()) return false;
  if (!pastikanKonteks()) return false;
  try {
    if (konteks!.state === "suspended") void konteks!.resume();
    const t0 = konteks!.currentTime + 0.005;
    hidup += 1;
    let terakhir: OscillatorNode | null = null;
    for (const n of ISYARAT[jenis]!) {
      terakhir = nada(t0 + (n.pada ?? 0), n);
    }
    /* `hidup` diturunkan oleh osilator TERAKHIR yang selesai, bukan oleh
       `setTimeout` yang menebak durasinya. Timer melenceng setiap kali tabnya
       di latar, dan yang terjadi bukan error melainkan penghitung yang tidak
       pernah kembali ke nol -- alias isyarat yang berhenti bekerja selamanya
       sesudah dua kali. */
    if (terakhir) terakhir.onended = () => { hidup = Math.max(0, hidup - 1); };
    else hidup = Math.max(0, hidup - 1);
    tundaIdle();
    return true;
  } catch {
    hidup = Math.max(0, hidup - 1);
    return false;
  }
}

/* ----------------------------------------------------------------- haptik */

/* 18 md. Di bawah ~10 md sebagian perangkat tidak menghasilkan apa pun; di
   atas ~30 md yang terasa berhenti jadi tanda baca dan mulai jadi alarm.
   Satu sentakan, PERNAH, tanpa ritme berulang: pola seperti `[30, 50, 30]`
   adalah kosakata notifikasi sistem, dan aplikasi yang meminjamnya sedang
   berpura-pura lebih penting daripada dirinya. */
const SENTAK_MS = 18;

/** Perangkat ini punya motor getar?
 *
 *  Tinggal di SINI, bukan di layar Pengaturan yang menampilkan saklarnya.
 *  Layar yang menanyai `navigator.vibrate` sendiri adalah saluran haptik
 *  kedua -- ia punya pendapatnya sendiri tentang apa yang dianggap "ada".
 *  Dipakai untuk menandai saklarnya SEBELUM ditekan: aturan "tidak boleh ada
 *  tombol yang berujung penolakan" berlaku untuk saklar juga, dan hampir
 *  seluruh desktop mendarat di cabang "tidak ada". */
export function adaHaptik(): boolean {
  const nav = globalThis.navigator as (Navigator & {
    vibrate?: (p: number | number[]) => boolean;
  }) | undefined;
  return typeof nav?.vibrate === "function";
}

/** Satu sentakan haptik, kalau perangkatnya punya dan saklarnya nyala.
 *
 *  Hanya untuk KONFIRMASI -- dan sengaja tidak pernah untuk kegagalan:
 *  menggetarkan telepon seseorang karena ia belum paham adalah hukuman yang
 *  dikirim ke tubuhnya. Namanya `sentuhPerangkat`, BUKAN `getar`, supaya ia
 *  tidak pernah tertukar dengan goyang visual di `gerak`. */
export function sentuhPerangkat(ms: number = SENTAK_MS): boolean {
  if (!bacaGetar()) return false;
  if (!adaHaptik()) return false;
  const lama = Math.max(1, Math.min(30, Number(ms) || SENTAK_MS));
  try {
    const nav = globalThis.navigator as Navigator & {
      vibrate: (p: number | number[]) => boolean;
    };
    return Boolean(nav.vibrate(lama));
  } catch { return false; }
}

/** Catat preferensi ke akar dokumen, TANPA menyentuh mesin audio.
 *
 *  Ini yang boleh berjalan saat halaman dimuat -- dan satu-satunya yang
 *  boleh. Apa pun yang membangun AudioContext dari sana akan membangunnya
 *  dalam keadaan ditolak. Yang ditulis cuma atribut, supaya CSS dan pagar tes
 *  bisa melihat setelan yang berlaku tanpa membaca localStorage sendiri. */
export function tandaiPreferensi(akar: HTMLElement | null): void {
  if (!akar?.dataset) return;
  akar.dataset.suara = bacaSuara();
  akar.dataset.getar = bacaGetar() ? "ya" : "tidak";
}

/** Satu-satunya pintu saluran non-visual yang dibuka ke layar, selain
 *  pembaca/penulis preferensinya.
 *
 *  Kartunya harus BERBUNYI saat ditekan, sama seperti kartu tingkat gerak di
 *  sebelahnya memperagakan geraknya. Kalau tidak, satu-satunya cara tahu arti
 *  "halus" adalah memilihnya, keluar dari Pengaturan, belajar sampai naik
 *  level, dan mencoba mengingat rasanya.
 *
 *  SATU fungsi untuk dua saluran, dan parameternya saluran. Dua pintu
 *  peragaan adalah dua tempat yang bisa berbeda pendapat tentang syarat mana
 *  yang berlaku, dan satu-satunya hal yang membuat "bawaan mati" bisa
 *  dipercaya adalah bahwa setiap jalur menuju bunyi melewati pemeriksaan yang
 *  sama.
 *
 *  Tingkatnya DIBACA dari preferensi yang baru dipasang, bukan diterima
 *  sebagai argumen: kartu yang memperagakan tingkat yang belum berlaku
 *  memperagakan sesuatu yang bohong. "mati" karena itu memang hening -- itu
 *  jawaban yang benar, dan layar yang memanggil ini bertanggung jawab
 *  mengatakannya dengan kata-kata. */
export function mainkanContoh(saluran: "suara" | "getar" = "suara"): boolean {
  if (saluran === "getar") return sentuhPerangkat();
  const tingkat = bacaSuara();
  return isyarat(tingkat === "halus" ? "acara" : "contoh");
}

/** Saluran non-visual untuk sebuah perayaan. Tingkatnya DITERIMA, tidak
 *  disimpulkan ulang: `rayakan()` sudah memutuskannya, dan pengait yang
 *  menyimpulkan sendiri dari isi hadiah adalah tempat kedua yang suatu hari
 *  berbeda pendapat.
 *
 *  Haptik ikut HANYA pada `acara`. Satu sentakan tiap kali XP bertambah
 *  berarti telepon yang berdenyut dua puluh kali per sesi belajar, dan itu
 *  berhenti berarti apa-apa pada denyut ketiga. */
export function rasakanPerayaan(tingkat: "acara" | "capai"): void {
  if (tingkat === "acara") {
    isyarat("acara");
    sentuhPerangkat();
  } else {
    isyarat("capai");
  }
}

/** Hanya untuk pagar tes: laporkan keadaan mesin tanpa membangunkannya.
 *
 *  "Nol konstruksi AudioContext sebelum satu gestur pun" harus bisa ditagih
 *  sebagai ANGKA, dan angka itu harus datang dari modulnya sendiri -- tes
 *  yang menghitung konstruksi dengan mengintip stub-nya masih bisa hijau di
 *  atas modul yang membangun konteksnya lewat jalan lain. */
export function keadaanSuara(): {
  tingkat: TingkatSuara; getar: boolean; konteksAda: boolean; hidup: number;
} {
  return {
    tingkat: bacaSuara(),
    getar: bacaGetar(),
    konteksAda: konteks !== null,
    hidup,
  };
}
