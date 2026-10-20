/* Sidik JSON yang bisa diadu dengan `alat/golden_bersama.py:_sha`.
 *
 * Dua hal yang harus sama, dan keduanya pernah jadi sumber sidik yang tidak
 * cocok padahal kedua sisi benar:
 *
 * 1. PEMISAH. Bawaan `json.dumps` menyisipkan spasi (`", "`, `": "`),
 *    `JSON.stringify` tidak pernah. Sisi Python sudah disetel
 *    `separators=(",", ":")`, jadi `JSON.stringify` polos sudah sepadan.
 * 2. URUTAN KUNCI. `json.dumps(sort_keys=True)` mengurutkan kunci objek;
 *    `JSON.stringify` memakai urutan penyisipan. Untuk daftar token urutan
 *    tidak pernah muncul, jadi `sorot` tidak terpengaruh -- tapi `beda`
 *    menyidik sebuah objek, dan di sana urutannya menentukan hasilnya.
 *
 * Karena itu penyerial di bawah mengurutkan kunci sendiri. Memakai
 * `JSON.stringify` polos untuk objek akan memberi sidik yang berbeda setiap
 * kali seseorang menukar urutan dua medan di kode -- perubahan yang tidak
 * mengubah satu pun perilaku, tapi memerahkan rekamannya.
 */

import { createHash } from "node:crypto";

type Nilai = string | number | boolean | null | Nilai[] | { [k: string]: Nilai };

/** Bentuk JSON padat dengan kunci objek TERURUT, sepadan dengan `json.dumps`. */
export function jsonKanonik(nilai: Nilai): string {
  if (nilai === null || typeof nilai !== "object") return JSON.stringify(nilai);
  if (Array.isArray(nilai)) {
    return "[" + nilai.map(jsonKanonik).join(",") + "]";
  }
  const kunci = Object.keys(nilai).sort();
  return (
    "{" +
    kunci
      .map((k) => JSON.stringify(k) + ":" + jsonKanonik(nilai[k] as Nilai))
      .join(",") +
    "}"
  );
}

/** SHA-256 atas bentuk kanonik di atas. */
export function sidik(nilai: Nilai): string {
  return createHash("sha256").update(jsonKanonik(nilai), "utf-8").digest("hex");
}
