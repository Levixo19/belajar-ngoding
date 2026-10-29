/* Rumus murni angka yang menghitung naik (`AngkaHidup.tsx`). Tidak ada DOM dan tidak ada
 * React, jadi pembanding Node bisa mengimpornya langsung.
 *
 * Gagasannya dari komponen "Count Up" (unlumen, 21st.dev): angka yang melaju ke nilai
 * akhirnya saat tampil. Kodenya ditulis sendiri; di sini hanya dua rumus kecil yang
 * keduanya wajib patuh pada satu janji: keadaan AKHIR selalu angka yang sebenarnya.
 *   - `tahapAngka` di ujung (t >= 1) mengembalikan `ke` persis, bukan hasil pembulatan.
 *   - Sebelum mulai (t <= 0, atau t bukan angka) mengembalikan `dari`: cap waktu
 *     `requestAnimationFrame` adalah AWAL bingkai dan bisa lebih awal dari saat
 *     animasinya diminta, jadi `t` negatif harus aman (cacat yang sama pernah terjadi di
 *     fisika tetes kaca: bingkai berdurasi negatif).
 */

/** Nilai bulat pada kemajuan `t` (0..1): melambat di ujung (ease-out kubik), monoton. */
export function tahapAngka(dari: number, ke: number, t: number): number {
  if (!(t > 0)) return dari;
  if (t >= 1) return ke;
  const k = 1 - Math.pow(1 - t, 3);
  return Math.round(dari + (ke - dari) * k);
}

/** Lama animasi (ms): makin jauh makin lama tetapi pelan (log), antara 450 dan 1.100. */
export function durasiAngka(dari: number, ke: number): number {
  const jarak = Math.abs(ke - dari);
  return Math.min(1100, 450 + Math.round(Math.log10(1 + jarak) * 220));
}
