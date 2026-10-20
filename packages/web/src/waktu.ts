/* Tanggal dan jam. Port dari `inti.js`.
 *
 * `tanggalLokal()` adalah SATU-SATUNYA pintu untuk mengurai ISO dari server.
 * Jangan memanggil `new Date(iso)` langsung di mana pun lagi, dan alasannya
 * tidak kelihatan sampai salah:
 *
 *   ECMAScript mengurai dua bentuk dengan aturan yang BERBEDA, dan perbedaan
 *   itu tidak pernah memberi pesan galat:
 *
 *     "2026-09-28"            (date-only, 10 karakter) -> tengah malam UTC
 *     "2026-09-28T07:15:00"   (tanpa offset)           -> tengah malam LOKAL
 *
 * Server ini menulis KEDUANYA: `date.today().isoformat()` untuk tanggal
 * (riwayat harian, jadwal kuis, tanggal streak) dan
 * `datetime.now().isoformat()` untuk cap waktu. Keduanya bermaksud waktu
 * setempat, tidak satu pun membawa offset.
 *
 * Terukur sebelum diperbaiki di sisi JS: `tanggalRamah("2026-09-28")`
 * mengembalikan 27/9/2026 di TZ=Pacific/Niue. Jadi yang perlu ditolong cuma
 * bentuk pertama, dan pertolongannya memindahkannya ke cabang parser yang
 * satunya. Cap waktu TIDAK boleh ikut disentuh -- ia sudah benar, dan
 * menambahi apa pun padanya akan menggesernya.
 */

/** Urai ISO dari server jadi `Date` LOKAL. `null` kalau tidak terbaca. */
export function tanggalLokal(iso: string | null | undefined): Date | null {
  if (!iso) return null;
  const s = String(iso);
  const t = new Date(s.length === 10 ? s + "T00:00:00" : s);
  return isNaN(t.getTime()) ? null : t;
}

/**
 * Tanggal hari ini menurut jam DINDING orang yang memakainya.
 *
 * `new Date().toISOString().slice(0, 10)` memberi tanggal UTC, jadi di
 * Asia/Makassar (UTC+8) ia masih menyebut kemarin sampai pukul 08:00 pagi.
 * Dipakai untuk menandai sel "hari ini" dan menamai berkas ekspor.
 */
export function hariIniISO(): string {
  const t = new Date();
  const dua = (n: number) => String(n).padStart(2, "0");
  return `${t.getFullYear()}-${dua(t.getMonth() + 1)}-${dua(t.getDate())}`;
}

/**
 * Selisih HARI dari hari ini; negatif berarti sudah lewat. `null` kalau
 * ISO-nya tidak terbaca.
 *
 * Kedua cap waktu dibulatkan ke tengah malam lebih dulu, dan itu seluruh
 * gunanya: yang ditanyakan "berapa hari lagi", bukan "berapa jam lagi". Tanpa
 * pembulatan, kuis yang jatuh tempo besok pagi akan disebut "hari ini" kalau
 * dilihat malam ini dan "besok" kalau dilihat pagi ini -- satu fakta, dua
 * jawaban, tergantung jam berapa orangnya membuka aplikasi.
 */
export function selisihHari(iso: string | null | undefined): number | null {
  const t = tanggalLokal(iso);
  if (!t) return null;
  t.setHours(0, 0, 0, 0);
  const kini = new Date();
  kini.setHours(0, 0, 0, 0);
  return Math.round((t.getTime() - kini.getTime()) / 86400000);
}

/** "28 Sep 2026". Kosong kalau ISO-nya tidak terbaca. */
export function tanggalRamah(iso: string | null | undefined): string {
  const t = tanggalLokal(iso);
  if (!t) return iso ? String(iso) : "";
  return t.toLocaleDateString("id-ID", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

/** "28 Sep, 07.15". Untuk cap waktu catatan dan kuis terakhir. */
export function jamRamah(iso: string | null | undefined): string {
  const t = tanggalLokal(iso);
  if (!t) return iso ? String(iso) : "";
  return t.toLocaleString("id-ID", {
    day: "numeric",
    month: "short",
    hour: "2-digit",
    minute: "2-digit",
  });
}

/**
 * Detik -> "MM:SS". Dipakai jam mundur mode timer kuis.
 *
 * Dijepit ke nol: `sisaDetik` di kuis boleh jatuh ke -1 satu tik sebelum
 * jamnya dimatikan, dan "-1:59" di layar yang sedang menghitung sisa waktu
 * terbaca sebagai aplikasi yang kacau, bukan sebagai waktu habis.
 */
export function jamMundur(detik: number): string {
  const d = Math.max(0, Math.floor(detik));
  return `${String(Math.floor(d / 60)).padStart(2, "0")}:`
       + `${String(d % 60).padStart(2, "0")}`;
}
