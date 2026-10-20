/* Satu baris sakelar: judul, keterangan, dan knop.
 *
 * Diekstrak dari `layar/Atur.tsx` begitu layar KEDUA membutuhkannya (setelan
 * kuis). Menyalinnya ke sana akan membuat dua sakelar yang kebetulan mirip,
 * dan yang pertama kali berbeda -- `role`, `aria-checked`, atau nama kelasnya
 * -- tidak akan ada yang menyadarinya.
 *
 * `role="switch"` plus `aria-checked`, bukan warna saja: knop yang cuma
 * bergeser adalah sakelar yang keadaannya tidak pernah ada sama sekali untuk
 * pembaca layar.
 */
export function SakelarBaris({
  judul,
  ket,
  nyala,
  onUbah,
}: {
  judul: string;
  ket: string;
  nyala: boolean;
  onUbah: (v: boolean) => void;
}) {
  return (
    <button
      type="button"
      className={"sakelar" + (nyala ? " on" : "")}
      role="switch"
      aria-checked={nyala}
      onClick={() => onUbah(!nyala)}
    >
      <div className="isi">
        <b>{judul}</b>
        <span>{ket}</span>
      </div>
      <div className="knop" />
    </button>
  );
}
