/* Bingkai pratinjau: menjalankan HTML pelajar di browser yang sedang ia pakai.
 *
 * Port `pratinjauHtml` dari `webapp/statik/js/pratinjau.js`. Bagian murninya
 * (halaman contoh dari pemilih CSS) tinggal di `pratinjau-css.ts` dan sudah
 * diadu dengan JS-nya atas seluruh blok kode kurikulum.
 *
 * Keamanan, dan ini satu-satunya hal di berkas ini yang tidak boleh disentuh:
 * bingkainya `sandbox="allow-scripts"` TANPA `allow-same-origin`. Kombinasi itu
 * aturan yang diajarkan kurikulum ini sendiri di materi HTML 13 -- memberi
 * keduanya sekaligus untuk berkas se-asal membuat sandbox-nya sia-sia, karena
 * skrip di dalamnya bisa meraih dokumen induknya. Tanpa `allow-same-origin`,
 * isinya duduk di asal buram: skripnya jalan (itu bagian dari pelajaran), tapi
 * ia tidak bisa membaca DOM induk, cookie, maupun localStorage aplikasi.
 *
 * Konsekuensi dari asal buram itulah yang membentuk seluruh sisa berkas ini:
 * bingkainya TIDAK BISA diukur dari luar, jadi yang mengukur penghuninya
 * sendiri dan satu-satunya jalan keluar yang tersisa `postMessage`.
 */

import { useCallback, useEffect, useLayoutEffect, useRef, useState } from "react";

/* Tinggi awal sebelum halamannya sempat melapor. Dipilih cukup untuk contoh
   sepanjang satu-dua paragraf; hampir semua contoh di kurikulum lebih pendek
   dari ini, jadi yang terlihat bukan bingkai kosong yang menyusut melainkan
   halaman yang langsung pas. */
const TINGGI_AWAL = 260;
const TINGGI_MAKS = 560;
const KELONGGARAN = 8;

/* Pelapor tinggi yang diselipkan ke dalam halaman pelajar.
 *
 * WAJIB identik byte-per-byte dengan `PELAPOR` di `pratinjau.js`, dan itu
 * ditagih `uji/banding-pratinjau.mjs`. Ia jalan di dalam bingkai ber-asal
 * buram, jadi tidak ada cara mengujinya dari luar sama sekali -- yang bisa
 * dijamin cuma bahwa dua antarmuka memakai skrip yang sama. */
const PELAPOR = `
<script>
(function () {
  function lapor() {
    var b = document.body;
    if (!b) return;
    /* Tingginya diukur dari TEPI BAWAH TERJAUH anak-anak body, bukan dari
       scrollHeight sebuah elemen.

       Dua jebakan sekaligus dihindari di sini, dan keduanya sudah menggigit:

       1. scrollHeight <html> MELINGKAR. <html> mengisi tinggi bingkainya,
          jadi angkanya melaporkan ulang tinggi yang barusan dipasang
          induknya -- halaman berisi satu judul dan satu paragraf melapor
          321px karena bingkainya memang 260px, lalu tidak pernah menyusut.
       2. Kotak body MELUPAKAN margin yang kolaps. Margin atas <h1> kolaps
          keluar melewati body, jadi kotak body mulai DI BAWAH judulnya dan
          tingginya kurang -- halaman yang sama terpotong di 95px.

       Tepi bawah anak terjauh tidak punya keduanya: ia diukur relatif
       terhadap viewport bingkai, dan margin yang kolaps sudah termasuk di
       dalam posisinya. */
    var bawah = 0;
    for (var i = 0; i < b.children.length; i++) {
      var r = b.children[i].getBoundingClientRect();
      if (r.height || r.width) bawah = Math.max(bawah, r.bottom);
    }
    if (!bawah) {
      /* Tidak ada satu pun anak yang punya kotak. Dua sebab yang sangat
         berbeda: halamannya memang kosong, ATAU dokumennya belum ditata sama
         sekali (pengukuran pertama berjalan saat readyState masih "loading").
         Membedakannya penting -- melaporkan 8px untuk yang kedua membuat
         bingkai menyusut jadi satu baris lalu melompat lagi begitu tata
         letaknya selesai, dan lompatan itu tepat di bawah mata orang yang
         baru menekan Jalankan. */
      if (b.children.length) return;
      bawah = b.getBoundingClientRect().bottom;
    }
    /* Margin BAWAH tidak ikut dalam getBoundingClientRect, dan margin bawah
       anak terakhir kolaps bersama margin bawah body -- yang berlaku yang
       TERBESAR, bukan jumlahnya. Melupakan ini menyisakan satu bilah gulir
       tipis di halaman yang sebenarnya sudah muat: <p> bermargin 16px di
       dalam body bermargin 8px kurang tepat 8 piksel. */
    var sisa = 0, anak = b.children[b.children.length - 1];
    if (anak) sisa = parseFloat(getComputedStyle(anak).marginBottom || 0);
    sisa = Math.max(sisa, parseFloat(getComputedStyle(b).marginBottom || 0));
    var t = bawah + sisa;
    /* Koreksi terakhir, dan arahnya cuma satu: MENUMBUHKAN.
       Ukuran dari anak-anak body melewatkan hal-hal yang tidak duduk di alur
       normal -- elemen ber-position absolute, bayangan, garis luar. Kalau
       dokumennya benar-benar meluber melewati bingkainya, scrollHeight tahu
       itu dan angkanya dipakai. Kalau tidak meluber, ia diabaikan: nilainya
       sekurang-kurangnya setinggi bingkai, jadi memakainya di situ berarti
       kembali ke jebakan melingkar yang membuat bingkai tidak pernah bisa
       menyusut lagi. */
    if (document.documentElement.scrollHeight > innerHeight) {
      t = Math.max(t, document.documentElement.scrollHeight);
    }
    parent.postMessage({ pratinjauTinggi: Math.ceil(t) }, "*");
  }

  addEventListener("load", lapor);
  addEventListener("resize", lapor);
  addEventListener("message", function (e) {
    if (e.data && e.data.pratinjauMinta) lapor();
  });
  if (window.ResizeObserver && document.body) {
    new ResizeObserver(lapor).observe(document.body);
  }
  lapor();
})();
<\/script>`;

export function Pratinjau({
  kode,
  lebar = 0,
}: {
  /** HTML apa adanya, seperti yang ditulis pelajar (atau halaman karangan). */
  kode: string;
  /**
   * Lebar PERANGKAT yang disimulasikan, dalam piksel. Nol berarti keadaan
   * ALAMI bingkainya: `width: 100%` dari gaya.css, nol transform, nol gaya
   * inline pada wadahnya -- persis seperti sebelum sakelar lebar ada. Itu
   * kontrak, bukan kebetulan: pembaca materi memakai komponen ini tanpa
   * `lebar`, dan halaman materi tidak boleh berubah satu simpul pun karena
   * fitur yang hidup di layar lain.
   *
   * Yang disetel lebar BINGKAINYA, bukan wadahnya. Bedanya seluruh gunanya
   * fitur ini: halaman di dalam bingkai 360 px benar-benar MENATA ULANG
   * dirinya di 360 px -- media query-nya menyala, `auto-fill` jatuh ke satu
   * kolom, teksnya membungkus di tempat yang berbeda. Wadah yang disempitkan
   * cuma MEMOTONG halaman yang tetap ditata selebar aslinya, dan yang terlihat
   * bukan pelajaran melainkan separuh halaman yang hilang.
   */
  lebar?: number;
}) {
  const bingkaiRef = useRef<HTMLIFrameElement>(null);
  const wadahRef = useRef<HTMLDivElement>(null);
  const [tinggi, setTinggi] = useState(TINGGI_AWAL);
  const [penuh, setPenuh] = useState(false);

  // Dokumen baru berarti tinggi yang belum diketahui. Tanpa dikembalikan ke
  // awal, halaman berikutnya mewarisi tinggi halaman sebelumnya sampai ia
  // sempat melapor -- dan untuk halaman yang jauh lebih pendek, yang terlihat
  // ruang kosong besar yang baru menyusut sepersekian detik kemudian.
  useEffect(() => {
    setTinggi(TINGGI_AWAL);
    setPenuh(false);
  }, [kode]);

  /* Kenakan lebar + tinggi + skala sebagai SATU keputusan.
   *
   * Urutannya mengikat, dan membaliknya sudah salah secara aritmetik: tinggi
   * yang diskalakan adalah tinggi HASIL CLAMP, bukan angka mentah yang
   * dilaporkan halaman. Yang benar `lebar -> k -> tinggi x k`; menukar dua
   * langkah terakhir membuat wadah lebih tinggi daripada yang dibutuhkan pada
   * `k = 1` dan memangkas isinya pada `k < 1`.
   *
   * Kenapa SKALA dan bukan `overflow-x: auto`: menggulir ke samping
   * menyembunyikan separuh halaman yang justru mau dibandingkan, dan penggulir
   * bersarang di dalam `.kerja-hasil` berarti dua mesin pada satu sumbu --
   * salah satunya `wheel`, yang di sana isyarat putus-pin.
   *
   * Dan bingkainya TIDAK dibuat ulang saat lebarnya berubah: `srcdoc` cuma
   * bergantung pada `kode`, jadi React tidak menyentuhnya. Pelapor tinggi di
   * dalamnya sudah mendengarkan `resize`. Kalau `srcdoc` ikut ditulis ulang,
   * animasi dan skrip halaman pelajar diputar ulang di depan matanya sendiri,
   * setiap kali ia menekan pil lebar.
   *
   * Jalur `lebar === 0` mengosongkan kembali SEMUA yang dipasangnya. Itu
   * bentuk yang sama dengan aturan animasi di AGENTS.md: keadaan akhir sebuah
   * sakelar wajib keadaan alami elemennya, supaya "lebar penuh" benar-benar
   * mengembalikan bingkai ke rupa tanpa fitur ini -- bukan ke tiruannya yang
   * kebetulan mirip. */
  useLayoutEffect(() => {
    const bingkai = bingkaiRef.current;
    const wadah = wadahRef.current;
    if (!bingkai || !wadah) return;

    bingkai.style.height = tinggi + "px";
    if (!lebar) {
      // Menghapus properti yang memang belum pernah disetel adalah no-op,
      // jadi jalur bawaan menyisakan atribut gaya berisi `height` saja.
      bingkai.style.width = "";
      bingkai.style.transform = "";
      bingkai.style.transformOrigin = "";
      bingkai.style.marginRight = "";
      bingkai.style.marginBottom = "";
      wadah.style.height = "";
      return;
    }
    // `clientWidth` wadah, bukan `offsetWidth`: `.pratinjau` punya border, dan
    // lebar yang tersedia untuk bingkainya adalah lebar DALAM-nya.
    const tersedia = wadah.clientWidth;
    const k = tersedia > 0 ? Math.min(1, tersedia / lebar) : 1;
    bingkai.style.width = lebar + "px";
    // `top left`, bukan bawaan `center`: dengan titik tengah, halaman yang
    // mengecil ikut bergeser ke dalam dan tepi kirinya tidak lagi sejajar
    // dengan tepi kiri wadahnya.
    bingkai.style.transformOrigin = "top left";
    bingkai.style.transform = k < 1 ? `scale(${k})` : "";
    const tinggiGambar = Math.round(tinggi * k);
    /* Margin negatif, dan ini bukan hiasan -- ia menutup satu cacat TERUKUR.
     *
     * `transform` tidak mengubah satu kotak tata letak pun, jadi bingkai
     * `width: 1280px` yang tergambar selebar 761 px TETAP menyumbang kotak
     * 1280 px ke daerah luber wadahnya. Terukur di 1280x800: `.pratinjau`
     * melapor `scrollWidth 1280` vs `clientWidth 761`, dan `scrollLeft`-nya
     * benar-benar bisa digeser ke 400 -- wadah itu diam-diam jadi penggulir
     * ber-bilah tersembunyi, yang isinya separuh halaman yang justru sedang
     * dibandingkan.
     *
     * Margin negatif menyamakan kotak MARGIN bingkai dengan kotak yang
     * TERGAMBAR, jadi tidak ada lagi yang tersisa untuk diluberi. Ia aman
     * justru karena `transform-origin` ada di `top left`: yang digambar duduk
     * di pojok kiri atas, dan ruang yang dicabut margin negatif adalah ruang
     * yang memang sudah kosong.
     *
     * Dipasang hanya pada `k < 1`. Pada `k = 1` tidak ada yang berlebih, dan
     * margin negatif nol piksel cuma akan menambah satu properti ke atribut
     * gaya tanpa mengubah apa pun. */
    bingkai.style.marginRight = k < 1
      ? -Math.round(lebar - tersedia) + "px" : "";
    bingkai.style.marginBottom = k < 1
      ? -(tinggi - tinggiGambar) + "px" : "";
    wadah.style.height = tinggiGambar + "px";
  }, [lebar, tinggi]);

  useEffect(() => {
    const saatPesan = (e: MessageEvent) => {
      // Induknya tidak mempercayai isi bingkai begitu saja: sumber pesan
      // dicocokkan dengan jendela bingkainya sendiri sebelum angkanya dipakai.
      if (e.source !== bingkaiRef.current?.contentWindow) return;
      const t = (e.data as { pratinjauTinggi?: unknown } | null)
        ?.pratinjauTinggi;
      if (typeof t !== "number" || !isFinite(t)) return;
      // Kelonggaran beberapa piksel, dan sisi salahnya dipilih sadar: ruang
      // kosong setipis ini di bawah halaman tidak terlihat siapa pun,
      // sedangkan KEKURANGAN satu piksel memunculkan bilah gulir sepanjang
      // bingkai -- dan bilah gulir pada halaman yang sebenarnya sudah muat
      // membaca sebagai "ada yang belum kamu lihat di bawah sana".
      setTinggi(Math.min(TINGGI_MAKS, Math.max(72, t + KELONGGARAN)));
      setPenuh(t + KELONGGARAN > TINGGI_MAKS);
    };
    globalThis.addEventListener("message", saatPesan);
    return () => globalThis.removeEventListener("message", saatPesan);
  }, []);

  // Beberapa hal mengubah tinggi SESUDAH dokumennya siap: gambar yang baru
  // selesai diunduh, dan font yang baru terpasang. ResizeObserver di dalam
  // menangkap keduanya, tapi hanya kalau ia sempat dipasang -- halaman yang
  // skripnya gagal (dan di kurikulum ini halaman yang sengaja salah memang
  // ada) tidak pernah melapor sama sekali. Satu pengukuran ulang saat load
  // menutup itu tanpa membuat halaman yang sehat berkedip.
  const saatMuat = useCallback(() => {
    try {
      bingkaiRef.current?.contentWindow?.postMessage({ pratinjauMinta: 1 }, "*");
    } catch {
      /* asal buram menolak; pelapor di dalam sudah mengurusnya */
    }
  }, []);

  return (
    <div ref={wadahRef} className="pratinjau">
      <iframe
        ref={bingkaiRef}
        className={"pratinjau-bingkai" + (penuh ? " pratinjau-penuh" : "")}
        title="Pratinjau halaman"
        sandbox="allow-scripts"
        // Kode pelajar apa adanya, ditambah pelapor tinggi di ujungnya.
        // Ditempel di BELAKANG supaya nomor baris apa pun yang muncul di pesan
        // error browser tetap cocok dengan yang ia lihat di editor.
        srcDoc={kode + PELAPOR}
        // TANPA loading="lazy", dan itu bukan kelalaian. Kartu keluaran hampir
        // selalu lahir di bawah lipatan layar, jadi bingkai bermuat-malas
        // menerima dokumen KOSONG lebih dulu -- pelapornya jalan, mengukur
        // body tanpa anak, dan melapor 8px. Yang terlihat: kotak putih
        // setinggi satu baris di bawah kode yang barusan dijalankan. Lagi pula
        // tidak ada yang dihemat: bingkainya baru dibuat saat tombol ditekan.
        onLoad={saatMuat}
      />
    </div>
  );
}
