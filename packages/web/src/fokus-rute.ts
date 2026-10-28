/** Judul dokumen dan fokus saat berpindah layar.
 *
 *  Padanan `gambarRute()` di `aplikasi.js`, yang pada setiap navigasi (kecuali
 *  pemuatan pertama) mengubah `document.title` dan memindahkan fokus ke
 *  panggung. Port React-nya kehilangan keduanya: judul tab tetap
 *  "belajar-codingV2" di semua layar, dan sesudah mengeklik tautan fokus
 *  tertinggal di tautan itu (atau jatuh ke <body> bila pemicunya ikut dilepas),
 *  jadi pembaca layar tidak tahu halamannya berganti dan pengguna papan ketik
 *  menab lagi melewati bilah yang sama untuk kesekian kalinya.
 *
 *  Dua perbedaan dari versi lama, dan keduanya disengaja:
 *  * Judulnya diambil dari `<h1>` layar yang tergambar, bukan dari properti
 *    yang dikembalikan layar; layar React tidak punya properti itu. Layar yang
 *    hanya berisi kartu `Keadaan` ("Gagal memuat ...") tidak punya <h1>, dan
 *    memakai judul kartunya.
 *  * Fokus dipindah HANYA bila sedang di <body>, di bilah navigasi, di
 *    kontainer layar itu sendiri, atau pada elemen yang sudah dilepas. Versi
 *    lama memindahkannya tanpa syarat; di
 *    sini mengetik di kotak cari Pustaka lalu menekan Enter mengubah alamat,
 *    dan memindahkan fokus saat itu membuang kursor dari kotak yang sedang
 *    dipakai.
 *
 *  Layar baru dibangun SESUDAH data tiba, jadi `<h1>`-nya belum ada saat efek
 *  ini jalan, atau yang ada masih milik layar sebelumnya. Pengamatnya hidup
 *  selama jendela tunggu dan WAJIB lepas: pada pergantian layar berikutnya
 *  atau pada batas waktu.
 */
import { useEffect, useRef, type RefObject } from "react";

const MEREK = "belajar-codingV2";
const BATAS_TUNGGU_MS = 4000;

/** Judul tab untuk sebuah judul layar. */
export function judulDokumen(judul: string | null | undefined): string {
  const bersih = (judul ?? "").replace(/\s+/g, " ").trim();
  return bersih ? `${bersih} · ${MEREK}` : MEREK;
}

/** Apakah fokus sedang di tempat yang tidak berarti: orang tidak sedang
 *  berada di dalam isi layar. */
export function fokusLiar(aktif: Element | null): boolean {
  if (!aktif || aktif === document.body || !aktif.isConnected) return true;
  // Kontainer layar itu sendiri (fokus mendarat di sana sesudah "Lompat ke
  // isi"): orangnya belum di dalam isi mana pun, dan isi di bawahnya baru saja
  // diganti. Dibiarkan di situ, pembaca layar tidak tahu halamannya berganti.
  if (aktif.id === "layar") return true;
  return aktif.closest("#rel") !== null;
}

export function useFokusRute(
  layar: RefObject<HTMLElement | null>,
  kunci: string,
): void {
  // Fokus pindah HANYA sesudah orang berpindah layar (`hashchange`), bukan
  // sesudah kunci rute berubah. Kunci ikut berubah di pemuatan pertama begitu
  // `/api/awal` tiba (`alamat` dari undefined jadi "materi/python/3"), dan
  // pengaman "render pertama" yang dulu dipakai gagal di sana: fokus mendarat
  // di <h1> pada lima dari tujuh pintu masuk, dan Tab pertama tidak lagi
  // menjangkau "Lompat ke isi" (terukur di Chrome).
  const sudahPindah = useRef(false);
  useEffect(() => {
    const tandai = () => { sudahPindah.current = true; };
    globalThis.addEventListener("hashchange", tandai);
    return () => globalThis.removeEventListener("hashchange", tandai);
  }, []);

  useEffect(() => {
    const akar = layar.current;
    if (!akar) return;
    const boleh = sudahPindah.current;
    // Judul tab dikembalikan ke netral lebih dulu: layar tanpa <h1> (kartu
    // "Gagal memuat") tidak boleh mewarisi judul layar sebelumnya.
    document.title = MEREK;

    let diterapkan: Element | null = null;
    let teksDiterapkan = "";
    let difokus: HTMLElement | null = null;

    // Dipanggil pada tiap perubahan isi layar selama jendela tunggu, bukan
    // sekali. Pada pindah antar-materi (komponen yang sama, data baru), efek
    // ini jalan ketika <h1> materi LAMA masih terpasang; menerimanya sebagai
    // jawaban membuat judul tab tertinggal dan fokus mendarat di simpul yang
    // sebentar lagi dibuang. Maka <h1> yang berganti simpul atau teks diterapkan
    // ulang, dan fokus diulang selama yang sebelumnya sudah terlepas.
    const terapkan = () => {
      // Layar yang hanya berisi kartu `Keadaan` ("Gagal memuat Langit",
      // "Materi tidak terbuka") tidak punya <h1>; judul kartunya yang dipakai,
      // supaya tab dan pembaca layar tetap tahu apa yang terjadi. <h1> selalu
      // menang bila ada: kartu `Keadaan` juga muncul DI DALAM layar yang punya
      // <h1> (mis. "Perlu diketahui"), dan itu bukan judul layarnya.
      const kepala = akar.querySelector<HTMLElement>("h1")
        ?? akar.querySelector<HTMLElement>(".keadaan-isi > b");
      const judul = kepala?.textContent?.trim();
      if (!kepala || !judul) return;
      if (kepala !== diterapkan || judul !== teksDiterapkan) {
        diterapkan = kepala;
        teksDiterapkan = judul;
        document.title = judulDokumen(judul);
        // Judul kartu bukan <h1>; perannya dipasang supaya pembaca layar
        // menemukannya lewat navigasi heading, tanpa mengubah tampilan kartu.
        if (kepala.tagName !== "H1") {
          kepala.setAttribute("role", "heading");
          kepala.setAttribute("aria-level", "1");
        }
      }
      if (boleh && (!difokus || !difokus.isConnected)
          && fokusLiar(document.activeElement)) {
        kepala.setAttribute("tabindex", "-1");
        kepala.style.outline = "none";
        kepala.focus({ preventScroll: true });
        difokus = kepala;
      }
    };

    terapkan();
    const pengamat = new MutationObserver(terapkan);
    pengamat.observe(akar, { childList: true, subtree: true, characterData: true });
    const batas = setTimeout(() => pengamat.disconnect(), BATAS_TUNGGU_MS);
    return () => {
      pengamat.disconnect();
      clearTimeout(batas);
    };
  }, [layar, kunci]);
}
