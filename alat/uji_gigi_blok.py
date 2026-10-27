#!/usr/bin/env python3
"""Baterai mutasi untuk pagar layar Langit: buktikan `TestBlokLangit` (dan tes
kelas yatim) bisa MERAH, dengan alasan yang benar.

Tiap sel menyunting SATU berkas (gaya.css atau sebuah .tsx) dengan sengaja,
menjalankan kelas tes yang relevan, lalu memulihkan berkasnya. Yang dihitung
benar adalah sel yang merah KARENA tes yang dinamai di sel itu: tes lain yang
kebetulan merah, atau mutan yang membuat berkasnya tak terbaca, tidak
membuktikan apa pun. Sel bertanda `HIJAU` adalah kontrol negatif: mutan di
LUAR blok Langit tidak boleh diadili aturan khusus Langit.

Jalurnya diturunkan dari letak berkas ini, jadi bisa dijalankan dari salinan
repo mana pun. Sama dengan `packages/bersama/uji/gigi-golden.py`, ia menyunting
berkas di tempat dan memulihkannya di `finally`; jalankan di pohon yang bersih.

    python3 alat/uji_gigi_blok.py
"""

import os
import re
import subprocess
import sys
import tempfile

AKAR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(AKAR, "webapp", "statik", "gaya.css")
SRC = os.path.join(AKAR, "packages", "web", "src")
PENUTUP = "/* Akhir blok layar Langit. */"
BLOK = "tests.test_web.TestBlokLangit"
YATIM = "tests.test_web.TestKontrakKelasHidup"


def ganti(a, b):
    def f(s):
        assert s.count(a) == 1, f"jangkar tidak unik ({s.count(a)}): {a[:70]!r}"
        return s.replace(a, b)
    return f


def pindah_penunjuk_ke_akhir(s):
    """Letakkan garis penunjuk SESUDAH lencana (di atas label), seperti sebelum perbaikan."""
    awal = s.index("                {penunjuk && terpilihB ? (")
    akhir = s.index("                ) : null}\n", awal) + len("                ) : null}\n")
    blok = s[awal:akhir]
    sisip = s.index("                {terpilihB ? (\n                  <g\n                    className=\"lt-ln-terpilih\"")
    assert sisip > akhir, "urutan sumber berubah; sesuaikan sel ini"
    return s[:awal] + s[akhir:sisip] + blok + s[sisip:]


def tambah_di_dalam(x):
    """Sisip DI DALAM blok Langit (sebelum komentar penutup)."""
    return ganti(PENUTUP, x + "\n" + PENUTUP)


def tambah_di_luar(x):
    """Sisip SESUDAH komentar penutup: bukan lagi bagian blok Langit."""
    return lambda s: s + "\n" + x + "\n"


def tambah_di_kaki(x):
    return lambda s: s + "\n" + x + "\n"


# (nama, berkas, ubah, kelas tes, tes yang diharapkan merah | None = harus HIJAU)
SEL = [
    ("infinite di garis ikhtisar", CSS, ganti(".lt-ik-garis { fill: none;", ".lt-ik-garis { animation: x 1s infinite; fill: none;"), BLOK, "test_tanpa_animasi_tak_berhingga_dan_properti_berat"),
    ("will-change", CSS, ganti(".lt-ik-svg { position: absolute;", ".lt-ik-svg { will-change: transform; position: absolute;"), BLOK, "test_tanpa_animasi_tak_berhingga_dan_properti_berat"),
    ("fill forwards", CSS, ganti("animation: rasi-lensa-masuk 260ms var(--gaya-masuk) backwards;", "animation: rasi-lensa-masuk 260ms var(--gaya-masuk) forwards;"), BLOK, "test_tanpa_animasi_tak_berhingga_dan_properti_berat"),
    ("pemilih html", CSS, tambah_di_dalam("html { color: red; }"), BLOK, "test_tidak_ada_pemilih_yang_menunjuk_html"),
    ("kelas lama tanpa induk", CSS, tambah_di_dalam(".bimasakti-kepala { margin: 0; }"), BLOK, "test_kelas_lama_hanya_lewat_induk_kelas_baru"),
    ("token di :root", CSS, tambah_di_dalam(":root {\n  --lg-kunci: red;\n}"), BLOK, "test_token_baru_hanya_di_body"),
    ("token warna keluarga di :root", CSS, tambah_di_dalam(":root { --lt-kel-web: #fff; }"), BLOK, "test_token_baru_hanya_di_body"),
    ("outline tanpa pengganti", CSS, ganti(".lt-nama:focus-visible { outline: 2px solid var(--lg-sorot); outline-offset: -2px; background: color-mix(in srgb, var(--lg-sorot) 7%, transparent); }", ".lt-nama { outline: none; }"), BLOK, "test_fokus_papan_ketik_tidak_dipadamkan"),
    ("pengganti fokus cuma box-shadow", CSS, ganti(".lt-nama:focus-visible { outline: 2px solid var(--lg-sorot); outline-offset: -2px; background: color-mix(in srgb, var(--lg-sorot) 7%, transparent); }", ".lt-nama { outline: none; }\n.lt-nama:focus-visible { box-shadow: 0 0 0 2px var(--lg-sorot); }"), BLOK, "test_fokus_papan_ketik_tidak_dipadamkan"),
    ("forced-colors dibuang", CSS, ganti("@media (forced-colors: active) {\n  .lt-gl-isi", "@media (forced-colors: none) {\n  .lt-gl-isi"), BLOK, "test_forced_colors_dan_ambang_resmi"),
    ("@container tanpa nama", CSS, ganti("@container panggung (min-width: 1030px)", "@container (min-width: 1030px)"), BLOK, "test_forced_colors_dan_ambang_resmi"),
    ("kunci terang 72 -> 40", CSS, ganti("--lg-kunci: color-mix(in srgb, var(--teks) 72%, var(--dasar-dalam));", "--lg-kunci: color-mix(in srgb, var(--teks) 40%, var(--dasar-dalam));"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("garis gelap 62 -> 35", CSS, ganti("--lg-garis: color-mix(in srgb, var(--teks) 62%, var(--dasar-dalam));\n  --lg-lintang", "--lg-garis: color-mix(in srgb, var(--teks) 35%, var(--dasar-dalam));\n  --lg-lintang"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("cahaya gelap 26 -> 70", CSS, ganti("--lt-cahaya: 26%;", "--lt-cahaya: 70%;"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("inti kemajuan gelap 14 -> 42", CSS, ganti("--lt-cahaya: 26%;\n  --lt-maju: 14%;", "--lt-cahaya: 26%;\n  --lt-maju: 42%;"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("halo lensa gelap .30 -> .70", CSS, ganti("--lt-halo: .30;", "--lt-halo: .70;"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("baru kembali ke teks-2 (selisih luminans dengan terkunci)", CSS, ganti("bentuk. */\n  --lg-baru: var(--teks);\n", "bentuk. */\n  --lg-baru: var(--teks-2);\n"), BLOK, "test_baru_terbedakan_dari_terkunci_oleh_terang_gelap"),
    ("peredupan opacity pada nama rasi", CSS, tambah_di_dalam(".lt-redup { opacity: .34; }"), BLOK, "test_tidak_ada_peredupan_opacity"),
    ("peredupan opacity pada glif", CSS, tambah_di_dalam(".lt-gl-redup { opacity: .3; }"), BLOK, "test_tidak_ada_peredupan_opacity"),
    ("huruf peta kembali piksel", CSS, ganti("font-size: clamp(.75rem, .95cqw, 1.125rem);", "font-size: clamp(12px, .95cqw, 18px);"), BLOK, "test_ukuran_huruf_peta_mengikuti_rem"),
    ("kelas yatim lt-", CSS, tambah_di_luar(".lt-yatim { color: red; }"), YATIM, "test_kelas_yatim_hanya_yang_dizinkan"),
    ("kelas yatim lt-gl- (dulu lolos: awalan komposisi)", CSS, tambah_di_luar(".lt-gl-yatim { color: red; }"), YATIM, "test_kelas_yatim_hanya_yang_dizinkan"),
    ("kelas yatim lt-ik-", CSS, tambah_di_luar(".lt-ik-yatim { color: red; }"), YATIM, "test_kelas_yatim_hanya_yang_dizinkan"),
    # Kontrol negatif: kaki gaya.css adalah satu-satunya zona tambah-CSS tanpa pajak
    # alamat. CSS lain yang ditambahkan SESUDAH komentar penutup tidak boleh
    # diadili aturan khusus Langit (pesan merahnya akan menyalahkan layar yang salah).
    ("KONTROL: @media luar sesudah penutup", CSS, tambah_di_luar("@media (hover: hover) { .pusaran { opacity: 1; } }"), BLOK, None),
    ("KONTROL: infinite luar sesudah penutup", CSS, tambah_di_luar(".pusaran { animation: x 1s infinite; }"), BLOK, None),
    ("aria-disabled kembali di opsi lensa", os.path.join(SRC, "layar", "LangitLensa.tsx"), ganti('      aria-selected={terpilih}\n', '      aria-selected={terpilih}\n      aria-disabled={s.status === "terkunci" ? true : undefined}\n'), BLOK, "test_opsi_lensa_tanpa_aria_disabled"),
    ("panel dikunci per bintang (fokus jatuh ke BODY)", os.path.join(SRC, "layar", "LangitLensa.tsx"), ganti("              key={kunci}\n              b={b}\n              i={indeks}", "              key={`${kunci}/${indeks}`}\n              b={b}\n              i={indeks}"), BLOK, "test_lensa_tidak_membongkar_fokus_dan_esc_didengar_di_dokumen"),
    ("Esc kembali dipasang di <section>", os.path.join(SRC, "layar", "LangitLensa.tsx"), ganti("      aria-labelledby=\"lt-lensa-judul\"\n", "      aria-labelledby=\"lt-lensa-judul\"\n      onKeyDown={(e) => { if (e.key === \"Escape\") escRef.current(); }}\n"), BLOK, "test_lensa_tidak_membongkar_fokus_dan_esc_didengar_di_dokumen"),
    ("alamat didekode telanjang", os.path.join(SRC, "layar", "Langit.tsx"), ganti("const p = bacaAlamat(globalThis.location.hash);", "const p = { key: decodeURIComponent(globalThis.location.hash.slice(9)), indeks: null };"), BLOK, "test_alamat_lensa_tidak_didekode_telanjang"),
    ("kelas glif dirangkai kembali", os.path.join(SRC, "komponen", "Glif.tsx"), ganti("<path className={`${KELAS_GLIF[status]} lt-gl-isi`} d={bagian.isi} />", "<path className={`lt-gl-${status} lt-gl-isi`} d={bagian.isi} />"), BLOK, "test_kelas_glif_ditulis_literal"),
    # Pelat langit di tema terang: tokennya dibaca dari aturan pelat, jadi tiap
    # kerusakan di sana harus merahkan gerbang kontras atau bentuknya.
    ("pelat: kunci 70 -> 30 persen", CSS, ganti("--lg-kunci: color-mix(in srgb, var(--teks) 70%, var(--dasar-dalam));", "--lg-kunci: color-mix(in srgb, var(--teks) 30%, var(--dasar-dalam));"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("pelat: kunci hampir sama terang dengan baru (78 persen)", CSS, ganti("--lg-kunci: color-mix(in srgb, var(--teks) 70%, var(--dasar-dalam));", "--lg-kunci: color-mix(in srgb, var(--teks) 78%, var(--dasar-dalam));"), BLOK, "test_baru_terbedakan_dari_terkunci_oleh_terang_gelap"),
    ("pelat: halo .22 -> .45", CSS, ganti("--lt-halo: .22;", "--lt-halo: .45;"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("pelat: cahaya 22 -> 70", CSS, ganti("--lt-cahaya: 22%;\n  --lt-maju: 14%;\n  --lt-halo: .22;", "--lt-cahaya: 70%;\n  --lt-maju: 14%;\n  --lt-halo: .22;"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("pelat: titik gradasi terang (#1c2858 -> #6f7fd8)", CSS, ganti("#1c2858 0%, #111a3d 52%", "#6f7fd8 0%, #111a3d 52%"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("pelat: --redup gelap (#a6abc0 -> #4a4f66)", CSS, ganti("--redup: #a6abc0;", "--redup: #4a4f66;"), BLOK, "test_kontras_token_teks_di_empat_tema"),
    ("pelat: --teks-2 redup (#b4b7c7 -> #55596e)", CSS, ganti("--teks: #ece9df; --teks-2: #b4b7c7;", "--teks: #ece9df; --teks-2: #55596e;"), BLOK, "test_kontras_token_teks_di_empat_tema"),
    ("pelat: token wajib hilang (--tumbuh)", CSS, ganti("--nyala: #e4b96b; --nyala-lembut: #f1d39d; --tumbuh: #63bfa5; --tenang: #94b6d8;", "--nyala: #e4b96b; --nyala-lembut: #f1d39d; --tenang: #94b6d8;"), BLOK, "test_kontras_token_glif_dan_garis_di_empat_tema"),
    ("pelat bocor ke tema malam", CSS, ganti('[data-tema="terang"] .lt-lensa-kanvas { box-shadow: inset 0 0 0 1px rgba(228,185,107,.30); }', '[data-tema="malam"] .lt-lensa-kanvas { box-shadow: inset 0 0 0 1px rgba(228,185,107,.30); }'), BLOK, "test_pelat_sempit_dan_hanya_tema_terang"),
    ("token pelat hanya di satu wadah", CSS, ganti('[data-tema="terang"] .lt-ikhtisar,\n[data-tema="terang"] .lt-lensa-kanvas {\n  --dasar-dalam', '[data-tema="terang"] .lt-ikhtisar {\n  --dasar-dalam'), BLOK, "test_token_baru_hanya_di_body"),
    ("token pelat di wadah ketiga (pengecualian melebar)", CSS, ganti('[data-tema="terang"] .lt-ikhtisar,\n[data-tema="terang"] .lt-lensa-kanvas {\n  --dasar-dalam', '[data-tema="terang"] .lt-ikhtisar,\n[data-tema="terang"] .lt-lensa-kanvas,\n[data-tema="terang"] .lt-lensa-isi {\n  --dasar-dalam'), BLOK, "test_token_baru_hanya_di_body"),
    ("pelat menunjuk html", CSS, ganti('[data-tema="terang"] .lt-lensa-isi {\n  box-shadow', '[data-tema="terang"] {\n  box-shadow'), BLOK, "test_pelat_sempit_dan_hanya_tema_terang"),
    ("peredupan .6 pada glif (dulu lolos: ambang 0,5)", CSS, tambah_di_dalam(".lt-gl-baru-redup { opacity: .6; }"), BLOK, "test_tidak_ada_peredupan_opacity"),
    ("transisi kedua pada garis ikhtisar", CSS, tambah_di_dalam(".lt-ik-garis { transition: opacity var(--d-sedang) var(--gaya-masuk); }"), BLOK, "test_hanya_satu_transisi"),
    ("keterangan kembali runtuh bila kosong", CSS, ganti("  .lt-halaman .langit-keterangan { min-height: 1lh; }", "  .lt-halaman .langit-keterangan:empty { min-height: 0; }"), BLOK, "test_keterangan_tidak_menggeser_peta"),
    ("kepala dan peta tidak lagi selebar sama", CSS, ganti("width: min(100%, 1800px); justify-self: center;", "width: min(100%, 1700px); justify-self: center;"), BLOK, "test_kepala_dan_peta_selebar_sama"),
    ("cahaya kanvas lensa: satu keluarga tanpa aturan", CSS, ganti('.lt-lensa-kanvas[data-kel="tech"] { --kel: var(--lt-kel-tech); }', ''), BLOK, "test_kanvas_lensa_membawa_keluarga"),
    ("kanvas lensa tanpa data-kel", os.path.join(SRC, "layar", "LangitLensa.tsx"), ganti(' data-kel={TATA[kunci]?.[2] ?? "tech"}', ''), BLOK, "test_kanvas_lensa_membawa_keluarga"),
    ("Esc lensa tidak memeriksa menu Lainnya", os.path.join(SRC, "layar", "LangitLensa.tsx"), ganti('document.querySelector(".jendela, #cangkang.rel-buka")', 'document.querySelector(".jendela")'), BLOK, "test_esc_lensa_tidak_bentrok_dengan_menu_dan_kartu"),
    ("Esc yang melepas pilihan tidak menutup kartu", os.path.join(SRC, "layar", "LangitLensa.tsx"), ganti("      setTipTutup(true);\n      return;\n    }\n    onTutup();", "      return;\n    }\n    onTutup();"), BLOK, "test_esc_lensa_tidak_bentrok_dengan_menu_dan_kartu"),
    ("tujuan karier disalin lagi ke state", os.path.join(SRC, "layar", "Langit.tsx"), ganti("        setData(d);\n      })", "        setData(d);\n        if (d.tujuan) setProfesiPilihan((p) => p ?? d.tujuan ?? null);\n      })"), BLOK, "test_tujuan_karier_diturunkan_tidak_disalin_ke_state"),
    ("daftar profesi dipangkas tanpa penanda sisa", os.path.join(SRC, "layar", "LangitPanel.tsx"), ganti("dipakai.length - MAKS_PROFESI", "0"), BLOK, "test_profesi_dipakai_tidak_dipangkas_diam_diam"),
    ("garis penunjuk kembali di atas label", os.path.join(SRC, "layar", "LangitLensa.tsx"), pindah_penunjuk_ke_akhir, BLOK, "test_penunjuk_digambar_sebelum_label"),
    ("garis ikhtisar kembali ke ruasAntara", os.path.join(SRC, "layar", "LangitIkhtisar.tsx"), ganti("const u = ruasIkhtisar(", "const u = ruasAntara("), BLOK, "test_garis_ikhtisar_tepi_ke_tepi"),
    ("kata kapsul kembali dari XP", os.path.join(SRC, "layar", "LangitIkhtisar.tsx"), ganti("              {kataMulai(bintangSaran.status)}\n            </a>", "              {saran.mulai ? 'Mulai di sini' : 'Lanjutkan di sini'}\n            </a>"), BLOK, "test_kata_kapsul_dari_status_bintang"),
]


def jalankan(kelas):
    d = tempfile.mkdtemp(prefix="gigi-blok-")
    env = dict(os.environ, BELAJAR_SKIP_LAMBAT="1", BELAJAR_PROGRESS_FILE=d + "/p.json",
               BELAJAR_CONFIG_FILE=d + "/k.json", BELAJAR_CATATAN_FILE=d + "/c.json",
               BELAJAR_WORKSPACE=d + "/kerja")
    r = subprocess.run([sys.executable, "-m", "unittest", kelas], cwd=AKAR, env=env,
                       capture_output=True, text=True)
    merah = sorted(set(re.findall(r"^(?:FAIL|ERROR): (test_\w+)", r.stderr, re.M)))
    return r.returncode, merah


def main():
    asli = {}
    ada = [s for s in SEL if os.path.exists(s[1])]
    belum = len(SEL) - len(ada)
    for _n, berkas, _f, _k, _h in ada:
        if berkas not in asli:
            with open(berkas, encoding="utf-8") as f:
                asli[berkas] = f.read()
    # Pagar nol: tanpa mutasi, kedua kelas tes WAJIB hijau.
    for kelas in (BLOK, YATIM):
        rc, merah = jalankan(kelas)
        if rc != 0:
            print(f"PAGAR NOL GAGAL: {kelas} sudah merah sebelum dimutasi: {merah}")
            return 1
    print("pagar nol: hijau")
    ok_semua = []
    try:
        for nama, berkas, ubah, kelas, harap in ada:
            with open(berkas, "w", encoding="utf-8") as f:
                f.write(ubah(asli[berkas]))
            rc, merah = jalankan(kelas)
            if harap is None:
                ok = rc == 0
                print(f"  {'HIJAU ' if ok else 'SALAH '} {nama}" + ("" if ok else f" -> merah: {merah}"))
            else:
                ok = harap in merah
                print(f"  {'MERAH ' if ok else 'TUMPUL'} {nama} -> {merah}")
            ok_semua.append(ok)
            with open(berkas, "w", encoding="utf-8") as f:
                f.write(asli[berkas])
    finally:
        for berkas, isi in asli.items():
            with open(berkas, "w", encoding="utf-8") as f:
                f.write(isi)
    for kelas in (BLOK, YATIM):
        rc, merah = jalankan(kelas)
        if rc != 0:
            print(f"PEMULIHAN GAGAL: {kelas} merah sesudah berkas dipulihkan: {merah}")
            return 1
    print("pemulihan: hijau lagi")
    if belum:
        # Sel yang berkasnya tidak ada tidak membuktikan apa pun, dan melapor
        # "semua sesuai" sambil melewatkannya adalah cara pagar kehilangan
        # giginya tanpa ketahuan: berkas yang dihapus atau diganti nama harus
        # memerahkan baterai ini, bukan membuatnya lebih pendek.
        print(f"dilewati: {belum} sel (berkas sasarannya tidak ada); tidak dihitung sesuai")
        return 1
    if all(ok_semua):
        print(f"SEMUA {len(ok_semua)} sel sesuai: pagarnya bergigi.")
        return 0
    print(f"{ok_semua.count(False)} dari {len(ok_semua)} sel TUMPUL.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
