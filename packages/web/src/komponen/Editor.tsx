/* Editor kode: textarea transparan di atas `<pre>` bertoken.
 *
 * Port kelas `Editor` dari `webapp/statik/js/editor.js`. Bagian murninya
 * (warna kurung, pemandu indentasi, letak pita) tinggal di `editor-teks.ts`
 * dan sudah dibuktikan identik dengan JS-nya atas 3.315 blok kode
 * (`uji/banding-editor.mjs`).
 *
 * SATU keputusan rancangan yang mengikat: **textarea-nya TIDAK terkontrol
 * React.** Seluruh penyuntingan lewat `setRangeText`, yang menjaga riwayat
 * undo peramban tetap utuh. Menulis ulang `value` dari state membuang seluruh
 * riwayat itu, dan `Ctrl+Z` yang tidak berfungsi adalah cara tercepat
 * kehilangan kepercayaan pada sebuah editor. Jadi nilainya hidup di DOM,
 * induknya diberi tahu lewat callback, dan satu-satunya state React di sini
 * hal yang memang milik tampilan: token, nomor baris, posisi kursor.
 *
 * AMBANG_RUANG 1100 WAJIB cocok dengan `@container panggung (min-width: 1100px)`
 * di `gaya.css`. Kalau meleset, ada pita lebar tempat editor berhenti mengukur
 * dirinya dari isi sementara tata letaknya belum memberi tinggi -- dan yang
 * terlihat editor pendek yang menggantung di dalam kotak tinggi.
 */

import {
  useCallback,
  useEffect,
  useImperativeHandle,
  useLayoutEffect,
  useRef,
  useState,
  type RefObject,
} from "react";

import { token } from "../../../bersama/src/sorot.ts";
import { adaGerak } from "../gerak.ts";
import {
  alihKomentar,
  INDENT,
  PASANGAN,
  pisahInden,
  pisahKurung,
  posisiPita,
  type Potongan,
} from "./editor-teks.ts";

/** Bagian tinggi jendela yang boleh dipakai editor sebelum ia menggulir. */
const TINGGI_MAKS = 0.62;
const SOROT_TUJU_MS = 1400;
/** Sama dengan `@container panggung (min-width: 1100px)` di `gaya.css`. */
const AMBANG_RUANG = 1100;

export interface PeganganEditor {
  /** Isi editor saat ini, dibaca langsung dari DOM. */
  nilai(): string;
  /** Ganti isinya. Dipakai "Kerangka kosong", contoh materi, pindah bahasa. */
  setNilai(v: string): void;
  fokus(): void;
  /** Pesan singkat di kaki editor ("tersimpan"). */
  catat(pesan: string): void;
  /**
   * Antar caret ke baris `n` (1-basis). `false` kalau barisnya tidak ada.
   *
   * Mengembalikan `false` TANPA melempar dan tanpa menggeser apa pun --
   * pemanggilnya yang memutuskan tidak menawarkan tombol, karena tombol yang
   * berakhir "baris itu tidak ada" lebih buruk daripada tidak ada tombol.
   */
  keBaris(n: number): boolean;
}

export function Editor({
  pegangan,
  bahasa = "python",
  kodeAwal = "",
  onUbah,
  pintasan = {},
  label = "Editor kode",
  isiRuang = false,
}: {
  pegangan?: RefObject<PeganganEditor | null>;
  bahasa?: string;
  kodeAwal?: string;
  /** Dipanggil (kode) setiap perubahan, sudah ditunda 420 md. */
  onUbah?: (kode: string) => void;
  /** `{ "ctrl+enter": fn }` -- dijalankan sebelum perilaku bawaan. */
  pintasan?: Record<string, () => void>;
  label?: string;
  /** `true` = tingginya diserahkan ke tata letak, bukan diukur dari isi. */
  isiRuang?: boolean;
}) {
  const teksRef = useRef<HTMLTextAreaElement>(null);
  const lapisRef = useRef<HTMLDivElement>(null);
  const sorotRef = useRef<HTMLPreElement>(null);
  const nomorRef = useRef<HTMLPreElement>(null);
  const akarRef = useRef<HTMLDivElement>(null);

  const [potongan, setPotongan] = useState<Potongan[]>([]);
  const [jumlahBaris, setJumlahBaris] = useState(1);
  const [barisKini, setBarisKini] = useState(1);
  const [kolomKini, setKolomKini] = useState(1);
  const [tujuBaris, setTujuBaris] = useState(0);
  const [pesan, setPesan] = useState("");

  const tundaUbah = useRef<number | null>(null);
  const tundaCatat = useRef<number | null>(null);
  const tundaTuju = useRef<number | null>(null);
  /** Esc lalu Tab = keluar editor (WCAG 2.1.2). */
  const lepasTab = useRef(false);

  const barisKursor = useCallback(() => {
    const t = teksRef.current;
    if (!t) return 1;
    return t.value.slice(0, t.selectionStart).split("\n").length;
  }, []);

  /** Tulis letak pita baris aktif ke dua custom property di `.editor-lapis`.
   *
   *  Angkanya dibaca dari gaya TERHITUNG, bukan diketik: `line-height` dan
   *  `padding-top` hidup di `gaya.css`, dan satu angka yang disimpan di dua
   *  tempat akan berbeda suatu hari.
   *
   *  Yang ditulisi `.editor-lapis`, BUKAN lapisan sorotnya: penggantian isi
   *  menganimasikan `opacity` sorotan, dan menumpangkan keadaan pita pada
   *  elemen yang sedang dianimasikan berarti dua mesin berebut satu elemen. */
  const gambarPita = useCallback(() => {
    const t = teksRef.current;
    const lapis = lapisRef.current;
    if (!t || !lapis) return;
    const g = getComputedStyle(t);
    const { atas, tinggi } = posisiPita({
      baris: barisKursor(),
      tinggiBaris: parseFloat(g.lineHeight) || 0,
      paddingAtas: parseFloat(g.paddingTop) || 0,
      scrollTop: t.scrollTop,
    });
    lapis.style.setProperty("--pita-atas", atas + "px");
    lapis.style.setProperty("--pita-tinggi", tinggi + "px");
  }, [barisKursor]);

  const selaraskan = useCallback(() => {
    const t = teksRef.current;
    if (!t) return;
    if (sorotRef.current) {
      sorotRef.current.scrollTop = t.scrollTop;
      sorotRef.current.scrollLeft = t.scrollLeft;
    }
    if (nomorRef.current) nomorRef.current.scrollTop = t.scrollTop;
    gambarPita();
  }, [gambarPita]);

  /** Tumbuh mengikuti isi sampai batas, lalu menggulir sendiri.
   *
   *  Editor yang tingginya tetap memaksa menggulir sejak baris pertama; yang
   *  tumbuh tanpa batas mendorong tombol Periksa keluar layar. */
  const ukur = useCallback(() => {
    const t = teksRef.current;
    const lapis = lapisRef.current;
    const akar = akarRef.current;
    const nomor = nomorRef.current;
    if (!t || !lapis || !akar) return;

    // Di ruang kerja yang setinggi jendela, tinggi editor BUKAN urusan isinya.
    // Kerangka latihan tiga baris di atas empat ratus piksel ruang kosong
    // adalah ruang kerja yang menolak dipakai bekerja -- jadi di sana tata
    // letak yang memberi tinggi, dan editor cuma mengisinya.
    if (isiRuang && globalThis.innerWidth >= AMBANG_RUANG) {
      akar.classList.add("editor-isi-ruang");
      t.style.height = "100%";
      lapis.style.height = "100%";
      if (nomor) nomor.style.maxHeight = "";
      return;
    }
    akar.classList.remove("editor-isi-ruang");

    const maks = Math.round(globalThis.innerHeight * TINGGI_MAKS);
    t.style.height = "auto";
    const tinggi = Math.min(maks, Math.max(150, t.scrollHeight));
    t.style.height = tinggi + "px";
    lapis.style.height = tinggi + "px";
    if (nomor) nomor.style.maxHeight = tinggi + "px";
  }, [isiRuang]);

  /** Hitung ulang token dan nomor baris dari isi textarea. */
  const gambar = useCallback(() => {
    const t = teksRef.current;
    if (!t) return;
    const isi = t.value;
    setPotongan(pisahInden(pisahKurung(token(isi, bahasa))));
    setJumlahBaris(isi.split("\n").length);
  }, [bahasa]);

  const perbaruiPosisi = useCallback(() => {
    const t = teksRef.current;
    if (!t) return;
    const sampai = t.value.slice(0, t.selectionStart).split("\n");
    setBarisKini(sampai.length);
    setKolomKini((sampai[sampai.length - 1] as string).length + 1);
  }, []);

  /* Pengukuran dan penyelarasan dijalankan SESUDAH DOM diperbarui, bukan di
     efek biasa: keduanya membaca `scrollHeight`, dan membacanya sebelum token
     baru terpasang memberi tinggi isi yang LAMA. */
  useLayoutEffect(() => {
    ukur();
    selaraskan();
  }, [potongan, jumlahBaris, ukur, selaraskan]);

  // Isi awal. Chrome menaruh kursor di AKHIR teks setelah `value` diisi,
  // sehingga baris terakhirlah yang tersorot di gutter sebelum editor disentuh
  // sama sekali. Yang benar baris pertama: di situ mata mulai membaca.
  useEffect(() => {
    const t = teksRef.current;
    if (!t) return;
    t.value = kodeAwal;
    t.setSelectionRange(0, 0);
    gambar();
    perbaruiPosisi();
    // Sengaja hanya saat mount: `kodeAwal` yang berubah ditangani induknya
    // lewat `setNilai`, supaya mengetik tidak pernah tertimpa prop.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    let id: number | null = null;
    const tunda = () => {
      if (id !== null) clearTimeout(id);
      id = setTimeout(() => ukur(), 160) as unknown as number;
    };
    globalThis.addEventListener("resize", tunda);
    return () => {
      globalThis.removeEventListener("resize", tunda);
      if (id !== null) clearTimeout(id);
    };
  }, [ukur]);

  // Semua timer dicabut saat lepas. Timer sorot `keBaris()` menulis ke state;
  // dibiarkan hidup, ia menembak komponen yang sudah tidak ada.
  useEffect(
    () => () => {
      if (tundaUbah.current !== null) clearTimeout(tundaUbah.current);
      if (tundaCatat.current !== null) clearTimeout(tundaCatat.current);
      if (tundaTuju.current !== null) clearTimeout(tundaTuju.current);
    },
    [],
  );

  const beritahuTunda = useCallback(() => {
    if (!onUbah) return;
    if (tundaUbah.current !== null) clearTimeout(tundaUbah.current);
    tundaUbah.current = setTimeout(() => {
      if (teksRef.current) onUbah(teksRef.current.value);
    }, 420) as unknown as number;
  }, [onUbah]);

  const sesudahUbah = useCallback(() => {
    gambar();
    perbaruiPosisi();
    if (onUbah && teksRef.current) onUbah(teksRef.current.value);
  }, [gambar, perbaruiPosisi, onUbah]);

  /** Sisip teks di posisi kursor. `setRangeText` MENJAGA riwayat undo. */
  const sisip = useCallback(
    (teks: string, pilihMulai?: number, pilihAkhir?: number) => {
      const t = teksRef.current;
      if (!t) return;
      t.setRangeText(teks, t.selectionStart, t.selectionEnd, "end");
      if (pilihMulai !== undefined) {
        t.setSelectionRange(
          pilihMulai,
          pilihAkhir === undefined ? pilihMulai : pilihAkhir,
        );
      }
      sesudahUbah();
    },
    [sesudahUbah],
  );

  const sisipRentang = useCallback(
    (teks: string, awal: number, akhir: number, kursor: number) => {
      const t = teksRef.current;
      if (!t) return;
      t.setRangeText(teks, awal, akhir, "end");
      t.setSelectionRange(kursor, kursor);
      sesudahUbah();
    },
    [sesudahUbah],
  );

  const batasBaris = useCallback((): [number, number] => {
    const t = teksRef.current;
    if (!t) return [0, 0];
    const nilai = t.value;
    const awal = nilai.lastIndexOf("\n", t.selectionStart - 1) + 1;
    let akhir = nilai.indexOf("\n", t.selectionEnd);
    if (akhir < 0) akhir = nilai.length;
    return [awal, akhir];
  }, []);

  const indentasiBaris = useCallback((pos: number): string => {
    const nilai = teksRef.current?.value ?? "";
    const awal = nilai.lastIndexOf("\n", pos - 1) + 1;
    return (nilai.slice(awal, pos).match(/^[ \t]*/) ?? [""])[0] as string;
  }, []);

  const tab = useCallback(
    (mundur: boolean) => {
      const t = teksRef.current;
      if (!t) return;
      const banyakBaris = t.value
        .slice(t.selectionStart, t.selectionEnd)
        .includes("\n");
      if (!banyakBaris && !mundur) {
        sisip(INDENT);
        return;
      }

      const [awal, akhir] = batasBaris();
      const blok = t.value.slice(awal, akhir);
      let geser = 0;
      const baru = blok
        .split("\n")
        .map((baris, i) => {
          if (mundur) {
            const buang = baris.startsWith(INDENT)
              ? INDENT.length
              : ((baris.match(/^(?: {1,3}|\t)/) ?? [""])[0] as string).length;
            if (i === 0) geser = -buang;
            return baris.slice(buang);
          }
          if (i === 0) geser = INDENT.length;
          return baris.trim() ? INDENT + baris : baris;
        })
        .join("\n");

      const mulaiLama = t.selectionStart;
      const akhirLama = t.selectionEnd;
      t.setRangeText(baru, awal, akhir, "preserve");
      t.setSelectionRange(
        Math.max(awal, mulaiLama + geser),
        akhirLama + (baru.length - blok.length),
      );
      gambar();
      if (onUbah) onUbah(t.value);
    },
    [batasBaris, sisip, gambar, onUbah],
  );

  const enter = useCallback(() => {
    const t = teksRef.current;
    if (!t) return;
    const nilai = t.value;
    const pos = t.selectionStart;
    const luar = indentasiBaris(pos);
    let indentasi = luar;

    const sebelum = nilai.slice(0, pos).trimEnd();
    if (/[{[(:]$/.test(sebelum)) indentasi += INDENT;

    // Kursor tepat di antara sepasang kurung: buka jadi tiga baris, dengan
    // penutupnya sejajar pembukanya. Ini gerakan yang paling sering dilakukan
    // tangan dan paling melelahkan kalau harus manual.
    const kiri = nilai.charAt(pos - 1);
    const kanan = nilai.charAt(t.selectionEnd);
    if (kiri && kanan && PASANGAN[kiri] === kanan && "([{".includes(kiri)) {
      sisip("\n" + indentasi + "\n" + luar, pos + 1 + indentasi.length);
      return;
    }
    sisip("\n" + indentasi);
  }, [indentasiBaris, sisip]);

  const majuSatu = useCallback(() => {
    const t = teksRef.current;
    if (!t) return;
    const p = t.selectionStart + 1;
    t.setSelectionRange(p, p);
    perbaruiPosisi();
  }, [perbaruiPosisi]);

  const kurung = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      const t = teksRef.current;
      if (!t) return;
      const buka = e.key;
      const tutup = PASANGAN[buka] as string;
      const terpilih = t.value.slice(t.selectionStart, t.selectionEnd);

      if (terpilih) {
        // Bungkus yang sedang dipilih.
        e.preventDefault();
        const awal = t.selectionStart;
        sisip(buka + terpilih + tutup, awal + 1, awal + 1 + terpilih.length);
        return;
      }

      // Kutip di tengah kata bukan pembuka string, melainkan apostrof:
      // "don't", "it's". Menutupnya otomatis di situ selalu salah.
      if (buka === tutup) {
        const kiri = t.value.charAt(t.selectionStart - 1);
        const kanan = t.value.charAt(t.selectionStart);
        if (kanan === buka) {
          e.preventDefault();
          majuSatu();
          return;
        }
        if (/[\w"'`]/.test(kiri) || /\w/.test(kanan)) return;
      }

      e.preventDefault();
      sisip(buka + tutup, t.selectionStart + 1);
    },
    [sisip, majuSatu],
  );

  const hapusMundur = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      const t = teksRef.current;
      if (!t || t.selectionStart !== t.selectionEnd) return;
      const pos = t.selectionStart;

      // Hapus sepasang kurung kosong sekaligus.
      const kiri = t.value.charAt(pos - 1);
      const kanan = t.value.charAt(pos);
      if (kiri && PASANGAN[kiri] === kanan) {
        e.preventDefault();
        sisipRentang("", pos - 1, pos + 1, pos - 1);
        return;
      }
      // Di dalam indentasi, hapus satu tingkat penuh, bukan satu spasi.
      const awalBaris = t.value.lastIndexOf("\n", pos - 1) + 1;
      const depan = t.value.slice(awalBaris, pos);
      if (
        depan.length >= INDENT.length &&
        !depan.trim() &&
        depan.length % INDENT.length === 0
      ) {
        e.preventDefault();
        sisipRentang("", pos - INDENT.length, pos, pos - INDENT.length);
      }
    },
    [sisipRentang],
  );

  const komentari = useCallback(() => {
    const t = teksRef.current;
    if (!t) return;
    const [awal, akhir] = batasBaris();
    const baru = alihKomentar(t.value.slice(awal, akhir), bahasa);
    t.setRangeText(baru, awal, akhir, "select");
    gambar();
    if (onUbah) onUbah(t.value);
  }, [batasBaris, bahasa, gambar, onUbah]);

  const saatTombol = useCallback(
    (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
      const kombinasi = [
        e.ctrlKey || e.metaKey ? "ctrl" : "",
        e.shiftKey ? "shift" : "",
        e.altKey ? "alt" : "",
        e.key.toLowerCase(),
      ]
        .filter(Boolean)
        .join("+");

      // Esc lalu Tab = keluar editor (WCAG 2.1.2). Tanpa jalan keluar ini,
      // orang yang memakai papan ketik terperangkap di dalam editor.
      lepasTab.current =
        e.key === "Escape" ||
        ((e.key === "Tab" || e.key === "Shift") && lepasTab.current);

      const fn = pintasan[kombinasi];
      if (fn) {
        e.preventDefault();
        fn();
        return;
      }

      if (kombinasi === "ctrl+/" || kombinasi === "ctrl+shift+7") {
        e.preventDefault();
        komentari();
        return;
      }
      if (e.key === "Tab") {
        if (lepasTab.current) {
          lepasTab.current = false;
          return;
        }
        e.preventDefault();
        tab(e.shiftKey);
        return;
      }
      if (e.key === "Enter") {
        e.preventDefault();
        enter();
        return;
      }
      if (e.key === "Backspace") {
        hapusMundur(e);
        return;
      }
      if (PASANGAN[e.key]) {
        kurung(e);
        return;
      }
      if (e.key === ")" || e.key === "]" || e.key === "}") {
        const t = teksRef.current;
        // Mengetik ")" tepat di depan ")" yang tadi dibuat otomatis: lewati
        // saja, jangan menumpuknya jadi "))".
        if (
          t &&
          t.selectionStart === t.selectionEnd &&
          t.value.charAt(t.selectionStart) === e.key
        ) {
          e.preventDefault();
          majuSatu();
        }
      }
    },
    [pintasan, komentari, tab, enter, hapusMundur, kurung, majuSatu],
  );

  useImperativeHandle(
    pegangan,
    () => ({
      nilai: () => teksRef.current?.value ?? "",
      setNilai: (v: string) => {
        const t = teksRef.current;
        if (!t) return;
        const berubah = t.value !== v;
        t.value = v;
        gambar();
        perbaruiPosisi();
        // Isi editor hanya berganti sendiri karena satu sebab: sesuatu di luar
        // yang menggantinya. Tanpa tanda apa pun, perubahan sebesar itu bisa
        // terlewat sama sekali kalau mata sedang di tempat lain di halaman.
        if (berubah && adaGerak() && sorotRef.current) {
          sorotRef.current.animate({ opacity: [0.35, 1] }, { duration: 200 });
        }
      },
      fokus: () => teksRef.current?.focus(),
      catat: (p: string) => {
        setPesan(p || "");
        if (!p) return;
        if (tundaCatat.current !== null) clearTimeout(tundaCatat.current);
        tundaCatat.current = setTimeout(
          () => setPesan(""),
          2600,
        ) as unknown as number;
      },
      keBaris: (n: number) => {
        const t = teksRef.current;
        if (!t) return false;
        const baris = t.value.split("\n");
        if (!Number.isInteger(n) || n < 1 || n > baris.length) return false;

        let pos = 0;
        for (let i = 0; i < n - 1; i++) pos += (baris[i] as string).length + 1;

        t.focus();
        t.setSelectionRange(pos, pos);

        // Guliran disetel SESUDAH fokus dan caret, dan urutan itu terukur,
        // bukan selera: `focus()` pada textarea yang belum fokus menggulir
        // caret ke dalam pandangan sendiri, jadi menyetel `scrollTop` lebih
        // dulu membuat Chrome menariknya kembali ke posisi caret yang LAMA.
        //
        // `scrollIntoView` TIDAK dipakai di sini: ia menggulir setiap leluhur
        // yang bisa digulir, termasuk dokumen -- jadi melompat ke baris 40
        // akan ikut memindahkan halamannya, dan pesan galat yang baru saja
        // diklik orangnya hilang dari pandangan.
        const g = getComputedStyle(t);
        const tinggiBaris = parseFloat(g.lineHeight) || 0;
        const puncak = (parseFloat(g.paddingTop) || 0) + (n - 1) * tinggiBaris;
        const ruang = t.clientHeight;
        const batas = Math.max(0, t.scrollHeight - ruang);
        t.scrollTop = Math.min(
          batas,
          Math.max(0, puncak - (ruang - tinggiBaris) / 2),
        );

        // Pada tingkat gerak `mati`, caret dan guliran TETAP pindah: keduanya
        // informasi, bukan hiasan. Yang padam cuma sorotnya.
        const sorot = adaGerak() ? n : 0;
        setTujuBaris(sorot);
        perbaruiPosisi();
        selaraskan();
        if (sorot) {
          if (tundaTuju.current !== null) clearTimeout(tundaTuju.current);
          tundaTuju.current = setTimeout(
            () => setTujuBaris(0),
            SOROT_TUJU_MS,
          ) as unknown as number;
        }
        return true;
      },
    }),
    [gambar, perbaruiPosisi, selaraskan],
  );

  const nomor = [];
  for (let i = 1; i <= jumlahBaris; i++) {
    const teks = i + (i < jumlahBaris ? "\n" : "");
    if (i === tujuBaris) {
      nomor.push(
        <b key={i} className="editor-tuju">
          {teks}
        </b>,
      );
    } else if (i === barisKini) {
      nomor.push(<b key={i}>{teks}</b>);
    } else {
      nomor.push(teks);
    }
  }

  return (
    <div ref={akarRef} className="editor">
      <pre ref={nomorRef} className="editor-nomor" aria-hidden="true">
        {nomor}
      </pre>
      <div ref={lapisRef} className="editor-lapis">
        <pre ref={sorotRef} aria-hidden="true">
          {potongan.map(([jenis, teks, warna], i) =>
            jenis === "teks" ? (
              teks
            ) : (
              <span
                key={i}
                className={"tk-" + jenis}
                data-warna={warna === null ? undefined : String(warna)}
              >
                {teks}
              </span>
            ),
          )}
          {/* Baris terakhir tidak akan terlihat kalau teksnya berakhir dengan
              newline: `<pre>` memangkas satu baris kosong di ujung. Satu
              newline tambahan menutup selisih itu, dan tidak pernah kelihatan
              karena ia memang kosong. */}
          {"\n"}
        </pre>
        <textarea
          ref={teksRef}
          spellCheck={false}
          autoCapitalize="off"
          autoComplete="off"
          wrap="off"
          aria-label={label}
          onInput={() => {
            gambar();
            beritahuTunda();
          }}
          onScroll={selaraskan}
          onKeyUp={perbaruiPosisi}
          onClick={perbaruiPosisi}
          onKeyDown={saatTombol}
        />
      </div>
      <div className="editor-kaki">
        <span>{`Brs ${barisKini}, Kol ${kolomKini}`}</span>
        <span>{`${jumlahBaris} baris`}</span>
        <span className="tersimpan">{pesan}</span>
        <span className="sembunyi-hp" style={{ marginLeft: "auto" }}>
          Tab menambah indentasi · Esc lalu Tab untuk keluar · Ctrl+/ komentari
        </span>
      </div>
    </div>
  );
}
