/** Fokus untuk dialog yang digambar sendiri (`Bantuan`, `Palet`, catatan di
 *  `Tanda`), bukan lewat `Jendela`: pulihkan fokus ke tempat asalnya, jerat
 *  Tab di dalam kotak, dan Escape menutup. Dulu ketiganya tidak punya satupun:
 *  menutup Bantuan atau Palet menjatuhkan fokus ke awal halaman, Tab keluar ke
 *  halaman di belakang tirai, dan dialog catatan tidak bisa ditutup dengan Esc.
 *  Pemakai papan ketik dan pembaca layar membayar tiga-tiganya, dan tidak ada
 *  galat di mana pun. */
import { useEffect, type RefObject } from "react";

/** Elemen yang bisa menerima fokus di dalam sebuah dialog, urut tab. */
export function bisaFokus(kotak: HTMLElement): HTMLElement[] {
  const pilih = 'a[href], button:not([disabled]), textarea, input, select,'
    + ' [tabindex]:not([tabindex="-1"])';
  return [...kotak.querySelectorAll<HTMLElement>(pilih)]
    .filter((el) => el.offsetParent !== null);
}

/** Dipasang di fase CAPTURE supaya pintasan cangkang (Ctrl+K dkk.) dan Esc
 *  layar di belakangnya (Langit memeriksa `.jendela` dan mengalah) tidak
 *  menang lebih dulu. `aktif` untuk dialog yang kotaknya baru ada sesudah
 *  sebuah state menyala; kotak yang selalu terpasang bersama komponennya
 *  cukup memakai bawaannya. Fokus awal hanya dipindah bila belum ada di
 *  dalam kotak: palet memusatkan kolom cari sendiri. */
export function useFokusDialog(
  kotak: RefObject<HTMLElement | null>,
  onTutup: () => void,
  aktif = true,
): void {
  useEffect(() => {
    if (!aktif) return;
    const asal = document.activeElement;
    const el = kotak.current;
    if (el && !el.contains(document.activeElement)) {
      (bisaFokus(el)[0] ?? el).focus();
    }
    const saatTombol = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        e.preventDefault();
        e.stopPropagation();
        onTutup();
        return;
      }
      if (e.key !== "Tab" || !kotak.current) return;
      const bisa = bisaFokus(kotak.current);
      if (!bisa.length) return;
      const awal = bisa[0]!;
      const akhir = bisa[bisa.length - 1]!;
      if (e.shiftKey && document.activeElement === awal) {
        e.preventDefault();
        akhir.focus();
      } else if (!e.shiftKey && document.activeElement === akhir) {
        e.preventDefault();
        awal.focus();
      }
    };
    document.addEventListener("keydown", saatTombol, true);
    return () => {
      document.removeEventListener("keydown", saatTombol, true);
      if (asal instanceof HTMLElement && asal.isConnected) asal.focus();
    };
  }, [kotak, onTutup, aktif]);
}
