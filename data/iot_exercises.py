"""Kurikulum Embedded & IoT.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

IOT_EXERCISES = [
    {
        "title": "Latihan 1: Kalkulator Resistor LED",
        "difficulty": "Mudah",
        "question": [
            "Tulis program yang menghitung resistor untuk sebuah LED.",
            "",
            "Input satu baris berisi tiga bilangan bulat: tegangan sumber",
            "dalam mV, tegangan maju LED dalam mV, dan arus yang diinginkan",
            "dalam mA. Tegangan sumber paling besar 24000 mV dan arus paling",
            "kecil 1 mA.",
            "",
            "Aturannya:",
            "  1. Kalau tegangan sumber tidak lebih besar dari tegangan maju,",
            "     cetak satu baris: Tegangan sumber terlalu kecil untuk LED ini.",
            "  2. Hitung R = (Vs - Vf) / I, lalu bulatkan ke atas ke ohm bulat.",
            "  3. Pilih nilai deret E12 terkecil yang >= R hitung. Angka dasar",
            "     E12: 10 12 15 18 22 27 33 39 47 56 68 82, dikali 1, 10, 100,",
            "     1000, atau 10000.",
            "  4. Hitung arus nyata dalam mikroampere: (Vs - Vf) x 1000 dibagi R",
            "     standar, sisanya dibuang. Cetak dalam mA dengan dua angka di",
            "     belakang titik, juga dengan membuang sisa.",
            "",
            "Untuk input 5000 1800 15, keluarannya:",
            "R hitung   : 214 ohm",
            "R standar  : 220 ohm",
            "Arus nyata : 14.54 mA",
            "",
            "Untuk input 3300 2000 10, keluarannya:",
            "R hitung   : 130 ohm",
            "R standar  : 150 ohm",
            "Arus nyata : 8.66 mA",
            "",
            "Untuk input 3300 3400 10, keluarannya:",
            "Tegangan sumber terlalu kecil untuk LED ini.",
        ],
        "hints": [
            "Milivolt dibagi miliampere langsung menghasilkan ohm, jadi seluruh hitungan bisa memakai int tanpa angka desimal.",
            "Pembulatan ke atas untuk bilangan bulat positif bisa ditulis (a + b - 1) / b, dan nilai E12 dicari dengan dua loop: pengali 1 sampai 10000 di luar, dua belas angka dasar di dalam.",
            "Simpan arus dalam mikroampere, misalnya ua = selisih * 1000 / r_standar, lalu cetak dengan printf(\"%d.%02d mA\", ua / 1000, ua % 1000 / 10).",
        ],
        "stdin_list": [
            """5000 1800 15
""",
            """3300 2000 10
""",
            """3300 3400 10
""",
        ],
        "solution": "#include <stdio.h>\n\n/* Angka dasar deret E12. Nilai lain didapat dengan mengalikan 10, 100, ... */\nstatic const int E12[12] = {10, 12, 15, 18, 22, 27, 33, 39, 47, 56, 68, 82};\n\nint main(void) {\n    int vs, vf, arus;\n    if (scanf(\"%d %d %d\", &vs, &vf, &arus) != 3) {\n        return 1;\n    }\n\n    int selisih = vs - vf;\n    if (selisih <= 0) {\n        printf(\"Tegangan sumber terlalu kecil untuk LED ini.\\n\");\n        return 0;\n    }\n\n    /* Bagi lalu bulatkan ke atas: resistor yang lebih besar lebih aman. */\n    int r_hitung = (selisih + arus - 1) / arus;\n\n    int r_standar = 0;\n    for (int kali = 1; kali <= 10000 && r_standar == 0; kali *= 10) {\n        for (int i = 0; i < 12; i++) {\n            if (E12[i] * kali >= r_hitung) {\n                r_standar = E12[i] * kali;\n                break;\n            }\n        }\n    }\n\n    int mikroamp = selisih * 1000 / r_standar;\n    printf(\"R hitung   : %d ohm\\n\", r_hitung);\n    printf(\"R standar  : %d ohm\\n\", r_standar);\n    printf(\"Arus nyata : %d.%02d mA\\n\", mikroamp / 1000, mikroamp % 1000 / 10);\n    return 0;\n}",
    },
    {
        "title": "Latihan 2: Blink Tanpa delay dengan Jam Palsu",
        "difficulty": "Mudah",
        "question": [
            "Dua LED berkedip tanpa delay. LED A berganti keadaan tiap 300 ms",
            "dan LED B tiap 500 ms. Jam papan diganti jam palsu dari input.",
            "",
            "Input: deretan bilangan bulat tak bertanda 32 bit, dipisah spasi,",
            "berurutan seperti bacaan millis() di tiap putaran loop. Jamnya",
            "bisa meluap: sesudah 4294967295 kembali ke 0.",
            "",
            "Aturannya:",
            "  1. Bacaan pertama adalah saat setup selesai. Kedua LED mulai",
            "     mati, dan waktu terakhir kedua LED diisi bacaan pertama itu.",
            "     Bacaan ini tidak mencetak apa pun.",
            "  2. Untuk tiap bacaan berikutnya, cek LED A dulu, lalu LED B.",
            "     Kalau sekarang - terakhir >= periode, balik keadaan LED itu,",
            "     isi terakhir = sekarang, lalu cetak satu baris:",
            "     <waktu>: LED <A atau B> <nyala atau mati>",
            "  3. Sesudah input habis, cetak total perubahan: N",
            "  4. Pakai uint32_t untuk semua waktu supaya selisihnya tetap",
            "     benar saat jam meluap.",
            "",
            "Contoh input:",
            "0 120 290 310 480 520 650 900 1010 1100 1300 1530",
            "",
            "Keluaran yang diharapkan:",
            "310: LED A nyala",
            "520: LED B nyala",
            "650: LED A mati",
            "1010: LED A nyala",
            "1100: LED B mati",
            "1530: LED A mati",
            "total perubahan: 6",
            "",
            "Untuk input 4294967000 4294967200 4 150 210 400 520 700, keluarannya:",
            "4: LED A nyala",
            "210: LED B nyala",
            "400: LED A mati",
            "700: LED A nyala",
            "total perubahan: 4",
        ],
        "hints": [
            "Jam dari input menggantikan millis(), jadi pola pengecekan selisih waktu dari materi bisa dipakai apa adanya, satu kali untuk tiap LED.",
            "Baca bacaan pertama di luar loop untuk mengisi waktu terakhir kedua LED, lalu baca sisanya dengan while (scanf(\"%\" SCNu32, &sekarang) == 1).",
            "Tiap LED butuh periode, waktu terakhir, dan keadaan nyala; cetak dengan printf(\"%\" PRIu32 \": LED A %s\\n\", sekarang, led_a ? \"nyala\" : \"mati\").",
        ],
        "stdin_list": [
            """0 120 290 310 480 520 650 900 1010 1100 1300 1530
""",
            """4294967000 4294967200 4 150 210 400 520 700
""",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n#include <inttypes.h>\n\nint main(void) {\n    uint32_t sekarang;\n    if (scanf(\"%\" SCNu32, &sekarang) != 1) {\n        return 1;\n    }\n\n    /* Bacaan pertama = saat papan selesai setup. Dua LED mulai mati. */\n    const uint32_t periode_a = 300, periode_b = 500;\n    uint32_t terakhir_a = sekarang, terakhir_b = sekarang;\n    int led_a = 0, led_b = 0;\n    int perubahan = 0;\n\n    while (scanf(\"%\" SCNu32, &sekarang) == 1) {\n        if (sekarang - terakhir_a >= periode_a) {\n            terakhir_a = sekarang;\n            led_a = !led_a;\n            printf(\"%\" PRIu32 \": LED A %s\\n\", sekarang, led_a ? \"nyala\" : \"mati\");\n            perubahan++;\n        }\n        if (sekarang - terakhir_b >= periode_b) {\n            terakhir_b = sekarang;\n            led_b = !led_b;\n            printf(\"%\" PRIu32 \": LED B %s\\n\", sekarang, led_b ? \"nyala\" : \"mati\");\n            perubahan++;\n        }\n    }\n    printf(\"total perubahan: %d\\n\", perubahan);\n    return 0;\n}",
    },
    {
        "title": "Latihan 3: Debounce sebagai State Machine",
        "difficulty": "Menengah",
        "question": [
            "Sebuah tombol memakai pull-up, jadi pin bernilai 1 saat dilepas",
            "dan 0 saat ditekan (active-low). Sampel mentahnya masih memantul.",
            "",
            "Input: pasangan <ms> <nilai_pin>, satu pasangan per baris, dengan",
            "waktu yang terus naik.",
            "",
            "Tulis state machine empat keadaan dengan waktu stabil 20 ms:",
            "  - lepas: kalau pin 0, catat waktunya lalu pindah ke",
            "    mungkin_tekan.",
            "  - mungkin_tekan: kalau pin 1, kembali ke lepas. Kalau pin 0 dan",
            "    ms - waktu_catat >= 20, pindah ke tekan dan cetak",
            "    <ms> ms: tekan",
            "  - tekan: kalau pin 1, catat waktunya lalu pindah ke",
            "    mungkin_lepas.",
            "  - mungkin_lepas: kalau pin 0, kembali ke tekan. Kalau pin 1 dan",
            "    ms - waktu_catat >= 20, pindah ke lepas dan cetak",
            "    <ms> ms: lepas",
            "",
            "Keadaan awal lepas. Sesudah input habis, cetak jumlah tekan: N",
            "",
            "Contoh input (satu tekanan dengan pantulan, lalu satu gangguan",
            "singkat di 200 ms yang harus diabaikan):",
            "0 1",
            "5 1",
            "10 0",
            "12 1",
            "14 0",
            "20 0",
            "25 0",
            "30 0",
            "35 0",
            "60 0",
            "90 0",
            "120 1",
            "123 0",
            "126 1",
            "130 1",
            "140 1",
            "150 1",
            "160 1",
            "200 0",
            "205 1",
            "210 1",
            "",
            "Keluaran yang diharapkan (untuk contoh input di atas):",
            "35 ms: tekan",
            "150 ms: lepas",
            "jumlah tekan: 1",
        ],
        "hints": [
            "Pantulan cuma bisa dibedakan dari tekanan sungguhan lewat lamanya: tekanan sungguhan bertahan, sedangkan pantulan cepat berubah lagi.",
            "Pakai enum untuk empat keadaan dan switch di dalam while (scanf(...) == 2), dengan satu variabel mulai yang diisi saat masuk mungkin_tekan atau mungkin_lepas.",
            "Di mungkin_tekan, cek dulu if (pin == 1) untuk kembali ke lepas, baru else if (ms - mulai >= 20) untuk pindah ke tekan, menambah hitungan, dan mencetak.",
        ],
        "stdin_list": [
            """0 1
5 1
10 0
12 1
14 0
20 0
25 0
30 0
35 0
60 0
90 0
120 1
123 0
126 1
130 1
140 1
150 1
160 1
200 0
205 1
210 1
""",
            """0 1
10 0
15 0
20 0
30 0
50 1
55 1
65 1
70 1
80 0
90 0
95 1
100 1
110 0
115 1
116 0
130 0
140 0
150 0
""",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n#include <inttypes.h>\n\n#define WAKTU_STABIL 20u   /* ms */\n\nenum keadaan { LEPAS, MUNGKIN_TEKAN, TEKAN, MUNGKIN_LEPAS };\n\nint main(void) {\n    enum keadaan k = LEPAS;\n    uint32_t ms, mulai = 0;\n    int pin, jumlah_tekan = 0;\n\n    while (scanf(\"%\" SCNu32 \" %d\", &ms, &pin) == 2) {\n        switch (k) {\n        case LEPAS:\n            if (pin == 0) {            /* active-low: 0 = mungkin ditekan */\n                k = MUNGKIN_TEKAN;\n                mulai = ms;\n            }\n            break;\n        case MUNGKIN_TEKAN:\n            if (pin == 1) {\n                k = LEPAS;             /* cuma pantulan */\n            } else if (ms - mulai >= WAKTU_STABIL) {\n                k = TEKAN;\n                jumlah_tekan++;\n                printf(\"%\" PRIu32 \" ms: tekan\\n\", ms);\n            }\n            break;\n        case TEKAN:\n            if (pin == 1) {\n                k = MUNGKIN_LEPAS;\n                mulai = ms;\n            }\n            break;\n        case MUNGKIN_LEPAS:\n            if (pin == 0) {\n                k = TEKAN;             /* cuma pantulan */\n            } else if (ms - mulai >= WAKTU_STABIL) {\n                k = LEPAS;\n                printf(\"%\" PRIu32 \" ms: lepas\\n\", ms);\n            }\n            break;\n        }\n    }\n    printf(\"jumlah tekan: %d\\n\", jumlah_tekan);\n    return 0;\n}",
    },
    {
        "title": "Latihan 4: Driver GPIO dengan Register Tiruan",
        "difficulty": "Menengah",
        "question": [
            "Tiru satu port GPIO bergaya STM32 dengan tiga register uint32_t",
            "yang semuanya mulai dari 0, untuk pin 0 sampai 15:",
            "  - MODER: dua bit per pin. Pin p menempati bit 2p dan 2p+1.",
            "    00 = in, 01 = out, 10 = af (fungsi alternatif), 11 = analog.",
            "  - ODR: bit p = keluaran yang ditulis program untuk pin p.",
            "  - IDR: bit p = level pin p yang terbaca.",
            "",
            "Simpan juga level dari luar chip (mulai 0) untuk tiap pin. IDR",
            "dihitung ulang sesudah setiap perintah yang mengubah sesuatu:",
            "  - pin out: bit IDR = bit ODR (pin mengikuti keluarannya)",
            "  - pin analog: bit IDR = 0",
            "  - pin in atau af: bit IDR = level dari luar",
            "",
            "Input: satu perintah per baris.",
            "  mode <p> <in|out|af|analog>   ubah dua bit pin p di MODER",
            "  set <p> / clear <p> / toggle <p>   ubah bit p di ODR",
            "  luar <p> <0|1>   ubah level dari luar untuk pin p",
            "  baca <p>   baca bit p di IDR",
            "",
            "Untuk tiap baris, cetak baris itu apa adanya, lalu \" -> \", lalu:",
            "  - untuk baca: nilai bitnya (0 atau 1)",
            "  - kalau p di luar 0-15: pin di luar 0-15",
            "  - kalau nama mode salah: mode tidak dikenal",
            "  - kalau perintahnya tidak dikenal: perintah tidak dikenal",
            "  - selain itu: MODER=0x%08X ODR=0x%08X IDR=0x%08X",
            "",
            "Contoh input:",
            "mode 5 out",
            "set 5",
            "mode 3 in",
            "luar 3 1",
            "baca 3",
            "toggle 5",
            "set 7",
            "mode 7 out",
            "baca 7",
            "clear 7",
            "mode 2 analog",
            "luar 2 1",
            "baca 2",
            "mode 20 out",
            "",
            "Keluaran yang diharapkan:",
            "mode 5 out -> MODER=0x00000400 ODR=0x00000000 IDR=0x00000000",
            "set 5 -> MODER=0x00000400 ODR=0x00000020 IDR=0x00000020",
            "mode 3 in -> MODER=0x00000400 ODR=0x00000020 IDR=0x00000020",
            "luar 3 1 -> MODER=0x00000400 ODR=0x00000020 IDR=0x00000028",
            "baca 3 -> 1",
            "toggle 5 -> MODER=0x00000400 ODR=0x00000000 IDR=0x00000008",
            "set 7 -> MODER=0x00000400 ODR=0x00000080 IDR=0x00000008",
            "mode 7 out -> MODER=0x00004400 ODR=0x00000080 IDR=0x00000088",
            "baca 7 -> 1",
            "clear 7 -> MODER=0x00004400 ODR=0x00000000 IDR=0x00000008",
            "mode 2 analog -> MODER=0x00004430 ODR=0x00000000 IDR=0x00000008",
            "luar 2 1 -> MODER=0x00004430 ODR=0x00000000 IDR=0x00000008",
            "baca 2 -> 0",
            "mode 20 out -> pin di luar 0-15",
            "",
            "Perhatikan set 7: ODR berubah, tapi IDR tidak, karena pin 7 masih",
            "masukan. Itu juga yang terjadi di chip sungguhan.",
            "",
            "Untuk input mode 0 out, keluarannya:",
            "mode 0 out -> MODER=0x00000001 ODR=0x00000000 IDR=0x00000000",
            "mode 1 out -> MODER=0x00000005 ODR=0x00000000 IDR=0x00000000",
            "set 0 -> MODER=0x00000005 ODR=0x00000001 IDR=0x00000001",
            "set 1 -> MODER=0x00000005 ODR=0x00000003 IDR=0x00000003",
            "mode 1 af -> MODER=0x00000009 ODR=0x00000003 IDR=0x00000001",
            "toggle 0 -> MODER=0x00000009 ODR=0x00000002 IDR=0x00000000",
            "luar 1 1 -> MODER=0x00000009 ODR=0x00000002 IDR=0x00000002",
            "baca 1 -> 1",
            "baca 0 -> 0",
            "mode 0 in -> MODER=0x00000008 ODR=0x00000002 IDR=0x00000002",
            "baca 0 -> 0",
            "mode 4 keluar -> mode tidak dikenal",
            "lompat 3 -> perintah tidak dikenal",
        ],
        "hints": [
            "Semua perubahan register memakai pola dari materi Bitmask: set, clear, dan toggle untuk ODR, serta kosongkan-lalu-isi untuk bidang dua bit di MODER.",
            "Baca tiap baris dengan fgets, buang karakter baris baru, lalu pecah dengan sscanf(baris, \"%15s %d %15s\", cmd, &pin, arg) dan pakai jumlah yang berhasil dibaca untuk tahu ada argumen ketiga atau nggak.",
            "Hitung IDR dengan loop pin 0 sampai 15: ambil mode = (MODER >> (2 * p)) & 3u, lalu pilih bit dari ODR, dari level luar, atau 0, dan kumpulkan dengan hasil |= bit << p.",
        ],
        "stdin_list": [
            """mode 5 out
set 5
mode 3 in
luar 3 1
baca 3
toggle 5
set 7
mode 7 out
baca 7
clear 7
mode 2 analog
luar 2 1
baca 2
mode 20 out
""",
            """mode 0 out
mode 1 out
set 0
set 1
mode 1 af
toggle 0
luar 1 1
baca 1
baca 0
mode 0 in
baca 0
mode 4 keluar
lompat 3
""",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n#include <inttypes.h>\n#include <string.h>\n\n/* Register tiruan satu port bergaya STM32. Semua mulai dari 0. */\nstatic uint32_t MODER = 0;   /* 2 bit per pin: 00 in, 01 out, 10 af, 11 analog */\nstatic uint32_t ODR = 0;     /* bit p = keluaran pin p */\nstatic uint32_t IDR = 0;     /* bit p = level pin p yang terbaca */\nstatic uint32_t luar = 0;    /* level yang dipasang rangkaian di luar chip */\n\nstatic uint32_t mode_pin(int p) {\n    return (MODER >> (2 * p)) & 3u;\n}\n\nstatic void hitung_idr(void) {\n    uint32_t hasil = 0;\n    for (int p = 0; p < 16; p++) {\n        uint32_t m = mode_pin(p);\n        uint32_t bit;\n        if (m == 1u) {\n            bit = (ODR >> p) & 1u;     /* output: pin mengikuti ODR */\n        } else if (m == 3u) {\n            bit = 0;                   /* analog: IDR selalu terbaca 0 */\n        } else {\n            bit = (luar >> p) & 1u;    /* input dan af: level dari luar */\n        }\n        hasil |= bit << p;\n    }\n    IDR = hasil;\n}\n\nstatic int kode_mode(const char *nama) {\n    const char *daftar[4] = {\"in\", \"out\", \"af\", \"analog\"};\n    for (int i = 0; i < 4; i++) {\n        if (strcmp(nama, daftar[i]) == 0) {\n            return i;\n        }\n    }\n    return -1;\n}\n\nint main(void) {\n    char baris[64], cmd[16], arg[16];\n    int pin;\n\n    while (fgets(baris, sizeof baris, stdin)) {\n        baris[strcspn(baris, \"\\r\\n\")] = '\\0';\n        int n = sscanf(baris, \"%15s %d %15s\", cmd, &pin, arg);\n        if (n < 2) {\n            continue;\n        }\n        printf(\"%s -> \", baris);\n        if (pin < 0 || pin > 15) {\n            printf(\"pin di luar 0-15\\n\");\n            continue;\n        }\n\n        uint32_t bit = 1u << pin;\n        if (strcmp(cmd, \"baca\") == 0) {\n            printf(\"%\" PRIu32 \"\\n\", (IDR >> pin) & 1u);\n            continue;\n        } else if (strcmp(cmd, \"mode\") == 0 && n == 3) {\n            int m = kode_mode(arg);\n            if (m < 0) {\n                printf(\"mode tidak dikenal\\n\");\n                continue;\n            }\n            MODER &= ~(3u << (2 * pin));\n            MODER |= (uint32_t)m << (2 * pin);\n        } else if (strcmp(cmd, \"set\") == 0) {\n            ODR |= bit;\n        } else if (strcmp(cmd, \"clear\") == 0) {\n            ODR &= ~bit;\n        } else if (strcmp(cmd, \"toggle\") == 0) {\n            ODR ^= bit;\n        } else if (strcmp(cmd, \"luar\") == 0 && n == 3) {\n            if (strcmp(arg, \"1\") == 0) {\n                luar |= bit;\n            } else {\n                luar &= ~bit;\n            }\n        } else {\n            printf(\"perintah tidak dikenal\\n\");\n            continue;\n        }\n        hitung_idr();\n        printf(\"MODER=0x%08\" PRIX32 \" ODR=0x%08\" PRIX32 \" IDR=0x%08\" PRIX32 \"\\n\",\n               MODER, ODR, IDR);\n    }\n    return 0;\n}",
    },
    {
        "title": "Latihan 5: Pengepakan Data Sensor Little-Endian",
        "difficulty": "Menengah",
        "question": [
            "Node sensor mengirim satu paket 6 byte. Input satu baris berisi",
            "tiga bilangan bulat: suhu dalam perseratus derajat (bertanda,",
            "-4000 sampai 8500), kelembapan dalam per seribu (0 sampai 1000),",
            "dan id node (0 sampai 255).",
            "",
            "Kalau ada nilai di luar batas, cetak satu baris dan berhenti,",
            "diperiksa berurutan:",
            "  suhu di luar -4000..8500",
            "  kelembapan di luar 0..1000",
            "  id di luar 0..255",
            "",
            "Tata letak paket:",
            "  byte 0      id",
            "  byte 1-2    suhu sebagai int16_t, little-endian",
            "  byte 3-4    kelembapan sebagai uint16_t, little-endian",
            "  byte 5      byte cek = byte 0 ^ byte 1 ^ byte 2 ^ byte 3 ^ byte 4",
            "",
            "Cetak paketnya dalam heks dua digit huruf besar, lalu urai kembali",
            "paket itu (bukan memakai angka input) dan cetak nilainya. Suhu",
            "dicetak dengan dua angka di belakang titik, kelembapan dengan satu",
            "angka di belakang titik, keduanya pakai hitungan bilangan bulat.",
            "",
            "Untuk input 2537 655 12, keluarannya:",
            "paket: 0C E9 09 8F 02 61",
            "id=12 suhu=25.37 C kelembapan=65.5 %",
            "",
            "Untuk input -1234 567 7, keluarannya:",
            "paket: 07 2E FB 37 02 E7",
            "id=7 suhu=-12.34 C kelembapan=56.7 %",
            "",
            "Untuk input -5 1000 255, keluarannya:",
            "paket: FF FB FF E8 03 10",
            "id=255 suhu=-0.05 C kelembapan=100.0 %",
            "",
            "Untuk input 9000 500 3, keluarannya:",
            "suhu di luar -4000..8500",
        ],
        "hints": [
            "Angka negatif dikirim sebagai pola bit komplemen duanya, jadi -1234 jadi 0xFB2E, dan little-endian berarti byte rendah 2E dikirim lebih dulu.",
            "Kemas dengan geser bit, misalnya byte rendah (uint8_t)(s & 0xFF) dan byte tinggi (uint8_t)(s >> 8) dari s = (uint16_t)suhu, lalu urai dengan in[1] | ((uint16_t)in[2] << 8).",
            "Ubah hasil urai ke angka bertanda tanpa bergantung compiler: kalau u >= 0x8000, nilainya (int32_t)u - 0x10000; untuk mencetak -0.05, cetak tanda minus dulu lalu pakai nilai mutlaknya.",
        ],
        "stdin_list": [
            """2537 655 12
""",
            """-1234 567 7
""",
            """-5 1000 255
""",
            """9000 500 3
""",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n\n#define PANJANG 6\n\nstatic void kemas(uint8_t id, int16_t suhu, uint16_t lembap, uint8_t out[PANJANG]) {\n    uint16_t s = (uint16_t)suhu;       /* pola bit komplemen dua, apa adanya */\n    out[0] = id;\n    out[1] = (uint8_t)(s & 0xFF);      /* byte rendah dulu: little-endian */\n    out[2] = (uint8_t)(s >> 8);\n    out[3] = (uint8_t)(lembap & 0xFF);\n    out[4] = (uint8_t)(lembap >> 8);\n    out[5] = out[0] ^ out[1] ^ out[2] ^ out[3] ^ out[4];\n}\n\nstatic int urai(const uint8_t in[PANJANG], uint8_t *id, int16_t *suhu, uint16_t *lembap) {\n    uint8_t cek = in[0] ^ in[1] ^ in[2] ^ in[3] ^ in[4];\n    if (cek != in[5]) {\n        return 0;\n    }\n    uint16_t s = (uint16_t)(in[1] | ((uint16_t)in[2] << 8));\n    *id = in[0];\n    /* Ubah pola bit ke angka bertanda tanpa bergantung pada perilaku compiler. */\n    *suhu = (s >= 0x8000u) ? (int16_t)((int32_t)s - 0x10000) : (int16_t)s;\n    *lembap = (uint16_t)(in[3] | ((uint16_t)in[4] << 8));\n    return 1;\n}\n\nint main(void) {\n    int suhu, lembap, id;\n    if (scanf(\"%d %d %d\", &suhu, &lembap, &id) != 3) {\n        return 1;\n    }\n    if (suhu < -4000 || suhu > 8500) {\n        printf(\"suhu di luar -4000..8500\\n\");\n        return 0;\n    }\n    if (lembap < 0 || lembap > 1000) {\n        printf(\"kelembapan di luar 0..1000\\n\");\n        return 0;\n    }\n    if (id < 0 || id > 255) {\n        printf(\"id di luar 0..255\\n\");\n        return 0;\n    }\n\n    uint8_t paket[PANJANG];\n    kemas((uint8_t)id, (int16_t)suhu, (uint16_t)lembap, paket);\n    printf(\"paket:\");\n    for (int i = 0; i < PANJANG; i++) {\n        printf(\" %02X\", paket[i]);\n    }\n    printf(\"\\n\");\n\n    uint8_t id2;\n    int16_t s2;\n    uint16_t l2;\n    if (!urai(paket, &id2, &s2, &l2)) {\n        printf(\"byte cek tidak cocok\\n\");\n        return 0;\n    }\n    int mutlak = s2 < 0 ? -s2 : s2;\n    printf(\"id=%d suhu=%s%d.%02d C kelembapan=%d.%d %%\\n\",\n           id2, s2 < 0 ? \"-\" : \"\", mutlak / 100, mutlak % 100, l2 / 10, l2 % 10);\n    return 0;\n}",
    },
    {
        "title": "Latihan 6: Filter Rata-Rata Bergerak ADC",
        "difficulty": "Menengah",
        "question": [
            "Sebuah sensor dibaca ADC 12 bit, jadi angkanya 0 sampai 4095. Tulis",
            "program yang mengubah tiap angka jadi milivolt, lalu menghitung",
            "rata-rata bergerak 4 sampel.",
            "",
            "Masukan (stdin):",
            "  baris 1: tegangan referensi (mV) dan banyak sampel, misalnya 3300 7",
            "  baris 2: angka-angka ADC dipisah spasi",
            "",
            "Aturan hitung, semuanya bilangan bulat:",
            "  - mV = (adc * vref + 2047) / 4095. Tambahan 2047, setengah dari",
            "    4095, membuat hasilnya dibulatkan ke terdekat.",
            "  - Rata-rata memakai milivolt 4 sampel terakhir. Sebelum ada 4 sampel,",
            "    pakai semua sampel yang sudah ada.",
            "  - Rata-rata juga dibulatkan ke terdekat: (jumlah + isi / 2) / isi,",
            "    dengan isi = banyak sampel di jendela.",
            "  - Pakai uint32_t untuk perkalian, karena 4095 * 3300 jauh melewati",
            "    batas int 16 bit di mikrokontroler kecil.",
            "",
            "Cetak satu baris per sampel dengan bentuk:",
            "  sampel N: X mV, rata-rata Y mV",
            "",
            "Untuk input 3300 7, keluarannya:",
            "sampel 1: 999 mV, rata-rata 999 mV",
            "sampel 2: 1008 mV, rata-rata 1004 mV",
            "sampel 3: 996 mV, rata-rata 1001 mV",
            "sampel 4: 3300 mV, rata-rata 1576 mV",
            "sampel 5: 1002 mV, rata-rata 1577 mV",
            "sampel 6: 998 mV, rata-rata 1574 mV",
            "sampel 7: 1007 mV, rata-rata 1577 mV",
            "",
            "Angka ADC kasus itu: 1240 1251 1236 4095 1244 1238 1249.",
        ],
        "hints": [
            "Simpan empat milivolt terakhir di larik berukuran 4, dan isi slotnya bergiliran dengan indeks sampel modulo 4.",
            "Jaga jumlah berjalan: kurangi isi slot yang akan ditimpa, lalu tambahkan nilai barunya, jadi kamu nggak perlu menjumlah ulang.",
            "Banyak sampel di jendela adalah i + 1 selama i + 1 < 4 dan 4 sesudahnya, lalu rata-ratanya (jumlah + isi / 2) / isi.",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n#include <inttypes.h>\n\n#define ADC_MAKS 4095u\n#define JENDELA  4\n\nint main(void)\n{\n    uint32_t vref, n;\n    if (scanf(\"%\" SCNu32 \" %\" SCNu32, &vref, &n) != 2)\n        return 1;\n\n    uint32_t jendela[JENDELA] = {0};\n    uint32_t jumlah = 0;\n\n    for (uint32_t i = 0; i < n; i++) {\n        uint32_t adc;\n        if (scanf(\"%\" SCNu32, &adc) != 1)\n            return 1;\n\n        /* milivolt dibulatkan ke terdekat: tambah setengah pembagi dulu */\n        uint32_t mv = (adc * vref + ADC_MAKS / 2) / ADC_MAKS;\n\n        uint32_t slot = i % JENDELA;\n        jumlah = jumlah - jendela[slot] + mv;\n        jendela[slot] = mv;\n\n        uint32_t isi = i + 1 < JENDELA ? i + 1 : JENDELA;\n        uint32_t rata = (jumlah + isi / 2) / isi;\n\n        printf(\"sampel %\" PRIu32 \": %\" PRIu32 \" mV, rata-rata %\" PRIu32 \" mV\\n\",\n               i + 1, mv, rata);\n    }\n    return 0;\n}",
        "stdin_list": [
            """3300 7
1240 1251 1236 4095 1244 1238 1249
""",
            """5000 5
0 819 1638 2457 4095
""",
        ],
    },
    {
        "title": "Latihan 7: Ring Buffer UART",
        "difficulty": "Menengah",
        "question": [
            "Tiru penampung byte UART dengan ring buffer 8 byte. Pakai larik",
            "statis, tanpa malloc.",
            "",
            "Masukan berupa perintah, satu per baris:",
            "  terima <byte heks> <byte heks> ...",
            "      byte yang tiba dari UART, misalnya: terima 48 49 0A",
            "  baca <n>",
            "      loop utama mengambil paling banyak n byte",
            "",
            "Aturan:",
            "  - Buffer memuat paling banyak 8 byte. Urutan keluar sama dengan",
            "    urutan masuk.",
            "  - Kalau buffer penuh, byte yang baru tiba dibuang (kebijakan buang",
            "    yang terbaru). Byte yang sudah ada nggak diganggu.",
            "  - Sesudah terima, cetak  terima: M masuk, isi I",
            "    lalu, kalau ada yang dibuang, satu baris lagi:",
            "    meluap: D byte dibuang",
            "  - Sesudah baca, cetak  baca:  diikuti tiap byte yang terambil",
            "    sebagai dua digit heks kapital (didahului spasi), lalu  , isi I",
            "    Kalau buffer kosong saat perintah itu datang, cetak",
            "    baca: kosong, isi 0",
            "",
            "Untuk input terima 48 49 0A, keluarannya:",
            "terima: 3 masuk, isi 3",
            "baca: 48 49, isi 1",
            "terima: 7 masuk, isi 8",
            "meluap: 2 byte dibuang",
            "baca: 0A 41 42, isi 5",
            "terima: 1 masuk, isi 6",
            "baca: 43 44 45 46 47 7E, isi 0",
            "baca: kosong, isi 0",
            "",
            "Masukan lengkap kasus itu:",
            "  terima 48 49 0A",
            "  baca 2",
            "  terima 41 42 43 44 45 46 47 48 49",
            "  baca 3",
            "  terima 7E",
            "  baca 10",
            "  baca 1",
        ],
        "hints": [
            "Pakai dua indeks, kepala untuk menulis dan ekor untuk membaca, lalu hitung isi buffer dari selisih keduanya.",
            "Baca masukan per baris dengan fgets, pecah dengan strtok, dan ubah tiap token heks jadi angka dengan strtoul(tok, NULL, 16).",
            "Kalau kepala dan ekor bertipe uint8_t dan terus bertambah, isinya (uint8_t)(kepala - ekor) dan slotnya kepala & 7.",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n#include <stdlib.h>\n#include <string.h>\n\n#define UKURAN 8\n#define MASK   (UKURAN - 1)\n\nstatic uint8_t data[UKURAN];\nstatic uint8_t kepala, ekor;\n\nstatic int isi(void) { return (uint8_t)(kepala - ekor); }\n\nint main(void)\n{\n    char baris[256];\n    while (fgets(baris, sizeof baris, stdin)) {\n        char *perintah = strtok(baris, \" \\t\\r\\n\");\n        if (!perintah)\n            continue;\n\n        if (strcmp(perintah, \"terima\") == 0) {\n            int masuk = 0, dibuang = 0;\n            char *tok;\n            while ((tok = strtok(NULL, \" \\t\\r\\n\")) != NULL) {\n                uint8_t b = (uint8_t)strtoul(tok, NULL, 16);\n                if (isi() == UKURAN) {\n                    dibuang++;\n                } else {\n                    data[kepala & MASK] = b;\n                    kepala++;\n                    masuk++;\n                }\n            }\n            printf(\"terima: %d masuk, isi %d\\n\", masuk, isi());\n            if (dibuang > 0)\n                printf(\"meluap: %d byte dibuang\\n\", dibuang);\n        } else if (strcmp(perintah, \"baca\") == 0) {\n            char *tok = strtok(NULL, \" \\t\\r\\n\");\n            int n = tok ? atoi(tok) : 0;\n            fputs(\"baca:\", stdout);\n            if (isi() == 0)\n                printf(\" kosong\");\n            while (n-- > 0 && isi() > 0) {\n                printf(\" %02X\", data[ekor & MASK]);\n                ekor++;\n            }\n            printf(\", isi %d\\n\", isi());\n        }\n    }\n    return 0;\n}",
        "stdin_list": [
            """terima 48 49 0A
baca 2
terima 41 42 43 44 45 46 47 48 49
baca 3
terima 7E
baca 10
baca 1
""",
            """baca 4
terima 01 02 03 04 05 06 07 08
terima FF
baca 8
""",
        ],
    },
    {
        "title": "Latihan 8: Pengurai Konfigurasi platformio.ini",
        "difficulty": "Menengah",
        "question": [
            "PlatformIO menyimpan pengaturan build di platformio.ini. Tulis",
            "pengurai kecil yang membaca berkas itu dari stdin dan mencetak tabel",
            "lingkungan build hasil penggabungan.",
            "",
            "Aturan berkasnya:",
            "  - Baris kosong dan baris yang diawali ; atau # dilewati.",
            "  - [env:nama] membuka satu lingkungan bernama nama.",
            "  - [env] membuka bagian bersama. Nilainya diwarisi semua lingkungan,",
            "    kecuali lingkungan itu menulis kunci yang sama sendiri.",
            "  - [platformio] boleh berisi default_envs = daftar lingkungan.",
            "  - Bagian lain diabaikan. Isi bagian berbentuk kunci = nilai, dan",
            "    spasi di sekitar kunci dan nilai dibuang.",
            "  - Yang dicetak cuma kunci platform, board, dan framework. Kalau",
            "    nilainya nggak ada di lingkungan maupun di [env], cetak tanda -",
            "",
            "Bentuk keluaran:",
            "  - Baris judul dan tiap lingkungan dicetak dengan format printf",
            "    \"%-12s %-14s %-14s %s\\n\" berisi nama, platform, board, framework.",
            "  - Lingkungan diurutkan menurut nama (strcmp).",
            "  - Baris terakhir berbunyi  pio run membangun: X  dengan X isi",
            "    default_envs, atau kata semua kalau default_envs nggak ada.",
            "",
            "Contoh masukan:",
            "  [platformio]",
            "  default_envs = uno",
            "",
            "  ; stasiun cuaca: satu kode, tiga papan",
            "  [env]",
            "  framework = arduino",
            "  monitor_speed = 115200",
            "",
            "  [env:uno]",
            "  platform = atmelavr",
            "  board = uno",
            "",
            "  [env:esp32idf]",
            "  platform = espressif32",
            "  board = esp32dev",
            "  framework = espidf",
            "",
            "  [env:esp32dev]",
            "  platform = espressif32",
            "  board = esp32dev",
            "",
            "Keluaran yang diharapkan (masukan di atas):",
            "lingkungan   platform       board          framework",
            "esp32dev     espressif32    esp32dev       arduino",
            "esp32idf     espressif32    esp32dev       espidf",
            "uno          atmelavr       uno            arduino",
            "pio run membangun: uno",
        ],
        "hints": [
            "Baca berkas baris demi baris, rapikan spasinya, lalu tentukan apakah baris itu kepala bagian, pasangan kunci = nilai, atau baris yang dilewati.",
            "Simpan nilai [env] di satu tempat dan nilai tiap [env:nama] di struct terpisah, lalu lakukan penggabungan saat mencetak.",
            "Urutkan larik struct dengan insertion sort memakai strcmp, dan pakai \"-\" kalau nilai khusus dan nilai bersama sama-sama kosong.",
        ],
        "solution": "#include <stdio.h>\n#include <string.h>\n#include <ctype.h>\n\n#define MAKS_ENV 16\n#define PANJANG  48\n\nenum { PLATFORM, BOARD, FRAMEWORK, JUMLAH_KUNCI };\nstatic const char *KUNCI[JUMLAH_KUNCI] = {\"platform\", \"board\", \"framework\"};\n\nstruct env {\n    char nama[PANJANG];\n    char nilai[JUMLAH_KUNCI][PANJANG];\n};\n\nstatic struct env daftar[MAKS_ENV];\nstatic int banyak;\nstatic char bersama[JUMLAH_KUNCI][PANJANG];\nstatic char bawaan[PANJANG * 4];\n\nstatic char *rapikan(char *s)\n{\n    while (isspace((unsigned char)*s))\n        s++;\n    char *akhir = s + strlen(s);\n    while (akhir > s && isspace((unsigned char)akhir[-1]))\n        *--akhir = '\\0';\n    return s;\n}\n\nstatic void salin(char *tujuan, const char *asal, size_t ukuran)\n{\n    strncpy(tujuan, asal, ukuran - 1);\n    tujuan[ukuran - 1] = '\\0';\n}\n\nint main(void)\n{\n    char baris[256];\n    enum { LAIN, PIO, BERSAMA, KHUSUS } bagian = LAIN;\n    struct env *kini = NULL;\n\n    while (fgets(baris, sizeof baris, stdin)) {\n        char *s = rapikan(baris);\n        if (*s == '\\0' || *s == ';' || *s == '#')\n            continue;\n\n        if (*s == '[') {\n            char *tutup = strchr(s, ']');\n            if (tutup)\n                *tutup = '\\0';\n            char *nama = s + 1;\n            if (strcmp(nama, \"platformio\") == 0) {\n                bagian = PIO;\n            } else if (strcmp(nama, \"env\") == 0) {\n                bagian = BERSAMA;\n            } else if (strncmp(nama, \"env:\", 4) == 0 && banyak < MAKS_ENV) {\n                bagian = KHUSUS;\n                kini = &daftar[banyak++];\n                salin(kini->nama, nama + 4, PANJANG);\n            } else {\n                bagian = LAIN;\n            }\n            continue;\n        }\n\n        char *sama = strchr(s, '=');\n        if (!sama)\n            continue;\n        *sama = '\\0';\n        char *kunci = rapikan(s);\n        char *nilai = rapikan(sama + 1);\n\n        if (bagian == PIO && strcmp(kunci, \"default_envs\") == 0) {\n            salin(bawaan, nilai, sizeof bawaan);\n            continue;\n        }\n        for (int k = 0; k < JUMLAH_KUNCI; k++) {\n            if (strcmp(kunci, KUNCI[k]) != 0)\n                continue;\n            if (bagian == BERSAMA)\n                salin(bersama[k], nilai, PANJANG);\n            else if (bagian == KHUSUS)\n                salin(kini->nilai[k], nilai, PANJANG);\n        }\n    }\n\n    /* urutkan menurut nama (sisip) */\n    for (int i = 1; i < banyak; i++) {\n        struct env t = daftar[i];\n        int j = i - 1;\n        while (j >= 0 && strcmp(daftar[j].nama, t.nama) > 0) {\n            daftar[j + 1] = daftar[j];\n            j--;\n        }\n        daftar[j + 1] = t;\n    }\n\n    printf(\"%-12s %-14s %-14s %s\\n\", \"lingkungan\", \"platform\", \"board\", \"framework\");\n    for (int i = 0; i < banyak; i++) {\n        const char *v[JUMLAH_KUNCI];\n        for (int k = 0; k < JUMLAH_KUNCI; k++) {\n            if (daftar[i].nilai[k][0])\n                v[k] = daftar[i].nilai[k];\n            else if (bersama[k][0])\n                v[k] = bersama[k];\n            else\n                v[k] = \"-\";\n        }\n        printf(\"%-12s %-14s %-14s %s\\n\", daftar[i].nama, v[PLATFORM], v[BOARD],\n               v[FRAMEWORK]);\n    }\n    printf(\"pio run membangun: %s\\n\", bawaan[0] ? bawaan : \"semua\");\n    return 0;\n}",
        "stdin_list": [
            """[platformio]
default_envs = uno

; stasiun cuaca: satu kode, tiga papan
[env]
framework = arduino
monitor_speed = 115200

[env:uno]
platform = atmelavr
board = uno

[env:esp32idf]
platform = espressif32
board = esp32dev
framework = espidf

[env:esp32dev]
platform = espressif32
board = esp32dev
""",
            """[env:pico]
platform = raspberrypi
board = pico
framework = arduino

# tanpa [env] bersama
[env:nucleo]
platform   =   ststm32
board = nucleo_f401re
""",
        ],
    },
    {
        "title": "Latihan 9: Penjadwal RTOS Mini dengan Tick Palsu",
        "difficulty": "Lanjut",
        "question": [
            "Tulis simulasi penjadwal preemptif berbasis prioritas, dengan waktu",
            "berupa tick palsu.",
            "",
            "Masukan (stdin):",
            "  baris 1: banyak task (1 sampai 8) dan banyak tick N",
            "  baris berikutnya, satu per task: nama prioritas periode kerja",
            "",
            "Aturannya:",
            "  - Tiap task punya job yang datang di tick 0, periode, 2 x periode,",
            "    dan seterusnya. Satu job butuh kerja tick CPU.",
            "  - Tenggat sebuah job adalah saat job berikutnya datang. Kalau job",
            "    baru datang sementara job lama task itu masih punya sisa kerja,",
            "    cetak  tick K: tenggat NAMA terlewat  lalu buang sisa job lama",
            "    dan mulai job baru.",
            "  - Di setiap tick, urutannya: pertama tangani job yang datang (urut",
            "    sesuai masukan), lalu pilih task yang masih punya sisa kerja dengan",
            "    prioritas terbesar. Kalau prioritasnya seri, menangkan task yang",
            "    ditulis lebih dulu. Task itu bekerja satu tick.",
            "  - Cetak  tick K: NAMA  untuk task yang jalan, atau  tick K: idle",
            "    kalau nggak ada.",
            "  - Sesudah N tick, cetak tiap task (urut masukan):",
            "    NAMA: selesai S, terlewat T",
            "  - Job yang masih berjalan saat simulasi berhenti nggak dihitung",
            "    terlewat.",
            "",
            "Untuk input 3 12, keluarannya:",
            "tick 0: sensor",
            "tick 1: kirim",
            "tick 2: kirim",
            "tick 3: log",
            "tick 4: sensor",
            "tick 5: log",
            "tick 6: kirim",
            "tick 7: kirim",
            "tick 8: sensor",
            "tick 9: log",
            "tick 10: log",
            "tick 11: idle",
            "sensor: selesai 3, terlewat 0",
            "kirim: selesai 2, terlewat 0",
            "log: selesai 1, terlewat 0",
            "",
            "Task di kasus itu:",
            "  sensor 3 4 1",
            "  kirim 2 6 2",
            "  log 1 12 4",
            "",
            "Perhatikan tick 4: sensor merebut CPU dari log, lalu log melanjutkan",
            "di tick 5. Kasus uji lain sengaja membuat CPU kewalahan supaya ada",
            "tenggat yang terlewat.",
        ],
        "hints": [
            "Simpan sisa kerja tiap task, dan anggap job baru datang setiap kali nomor tick habis dibagi periodenya.",
            "Di tiap tick kerjakan dua langkah terpisah: tangani kedatangan job dulu untuk semua task, baru pilih satu task untuk dijalankan.",
            "Pemilihannya cukup satu perulangan yang menyimpan indeks dengan prioritas terbesar dan membandingkan pakai tanda lebih besar, supaya seri dimenangkan task yang lebih dulu.",
        ],
        "solution": "#include <stdio.h>\n#include <string.h>\n\n#define MAKS_TASK 8\n\nstruct task {\n    char nama[16];\n    int prioritas;   /* angka besar = lebih penting, seperti FreeRTOS */\n    int periode;     /* job baru datang tiap kelipatan periode */\n    int kerja;       /* tick CPU yang dibutuhkan satu job */\n    int sisa;        /* sisa kerja job yang sedang berjalan */\n    int selesai;\n    int terlewat;\n};\n\nint main(void)\n{\n    struct task t[MAKS_TASK];\n    int banyak, n_tick;\n    if (scanf(\"%d %d\", &banyak, &n_tick) != 2 || banyak < 1 || banyak > MAKS_TASK)\n        return 1;\n    for (int i = 0; i < banyak; i++) {\n        if (scanf(\"%15s %d %d %d\", t[i].nama, &t[i].prioritas, &t[i].periode,\n                  &t[i].kerja) != 4)\n            return 1;\n        t[i].sisa = 0;\n        t[i].selesai = 0;\n        t[i].terlewat = 0;\n    }\n\n    for (int k = 0; k < n_tick; k++) {\n        /* 1. Job baru datang. Job lama yang belum beres = tenggat terlewat. */\n        for (int i = 0; i < banyak; i++) {\n            if (k % t[i].periode != 0)\n                continue;\n            if (t[i].sisa > 0) {\n                printf(\"tick %d: tenggat %s terlewat\\n\", k, t[i].nama);\n                t[i].terlewat++;\n            }\n            t[i].sisa = t[i].kerja;\n        }\n\n        /* 2. Pilih task siap berprioritas tertinggi; seri = yang ditulis duluan. */\n        int pilih = -1;\n        for (int i = 0; i < banyak; i++)\n            if (t[i].sisa > 0 && (pilih < 0 || t[i].prioritas > t[pilih].prioritas))\n                pilih = i;\n\n        /* 3. Jalankan satu tick. */\n        if (pilih < 0) {\n            printf(\"tick %d: idle\\n\", k);\n            continue;\n        }\n        printf(\"tick %d: %s\\n\", k, t[pilih].nama);\n        if (--t[pilih].sisa == 0)\n            t[pilih].selesai++;\n    }\n\n    for (int i = 0; i < banyak; i++)\n        printf(\"%s: selesai %d, terlewat %d\\n\", t[i].nama, t[i].selesai,\n               t[i].terlewat);\n    return 0;\n}",
        "stdin_list": [
            """3 12
sensor 3 4 1
kirim 2 6 2
log 1 12 4
""",
            """3 12
motor 3 2 1
sensor 2 5 2
log 1 10 3
""",
        ],
    },
    {
        "title": "Latihan 10: CRC-16/CCITT untuk Frame Sensor",
        "difficulty": "Lanjut",
        "question": [
            "Tulis program yang menghitung CRC-16/CCITT-FALSE untuk setiap",
            "baris masukan. Tiap baris berisi byte heks dipisah spasi.",
            "",
            "Parameter CRC-nya:",
            "  lebar 16 bit, polinom 0x1021, nilai awal 0xFFFF,",
            "  refin tidak, refout tidak, xorout 0x0000.",
            "  Nilai uji: CRC untuk teks \"123456789\" adalah 0x29B1.",
            "",
            "Aturan:",
            "  - Baris kosong dilewati dan nggak diberi nomor.",
            "  - Satu baris berisi paling banyak 128 byte.",
            "  - Untuk tiap baris cetak:",
            "    pesan N: B byte, crc 0xXXXX, dikirim HH LL",
            "    HH LL adalah byte tinggi lalu byte rendah, urutan yang akan",
            "    ditempel di belakang frame.",
            "",
            "Untuk input berikut:",
            "  31 32 33 34 35 36 37 38 39",
            "  03 01 00 0E 02",
            "  00",
            "",
            "  FF FF",
            "",
            "keluarannya:",
            "pesan 1: 9 byte, crc 0x29B1, dikirim 29 B1",
            "pesan 2: 5 byte, crc 0x8A27, dikirim 8A 27",
            "pesan 3: 1 byte, crc 0xE1F0, dikirim E1 F0",
            "pesan 4: 2 byte, crc 0x0000, dikirim 00 00",
        ],
        "hints": [
            "CRC-16 bit demi bit bekerja dengan menaruh byte data di 8 bit atas register, lalu menggeser register ke kiri delapan kali.",
            "Pada tiap geseran, kalau bit 15 bernilai 1 sebelum digeser, hasil geseran di-XOR dengan polinom 0x1021.",
            "Mulai dari crc = 0xFFFF, lakukan crc ^= byte << 8 untuk tiap byte, dan selalu potong hasil geser ke 16 bit dengan cast ke uint16_t.",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n#include <stdlib.h>\n#include <string.h>\n\nstatic uint16_t crc16_ccitt_false(const uint8_t *data, int n)\n{\n    uint16_t crc = 0xFFFF;\n    for (int i = 0; i < n; i++) {\n        crc ^= (uint16_t)(data[i] << 8);\n        for (int b = 0; b < 8; b++) {\n            if (crc & 0x8000)\n                crc = (uint16_t)((crc << 1) ^ 0x1021);\n            else\n                crc = (uint16_t)(crc << 1);\n        }\n    }\n    return crc;\n}\n\nint main(void)\n{\n    char baris[512];\n    int nomor = 0;\n    while (fgets(baris, sizeof baris, stdin)) {\n        uint8_t data[128];\n        int n = 0;\n        for (char *tok = strtok(baris, \" \\t\\r\\n\"); tok && n < 128;\n             tok = strtok(NULL, \" \\t\\r\\n\"))\n            data[n++] = (uint8_t)strtoul(tok, NULL, 16);\n        if (n == 0)\n            continue;\n        uint16_t crc = crc16_ccitt_false(data, n);\n        nomor++;\n        printf(\"pesan %d: %d byte, crc 0x%04X, dikirim %02X %02X\\n\",\n               nomor, n, crc, crc >> 8, crc & 0xFF);\n    }\n    return 0;\n}",
        "stdin_list": [
            """31 32 33 34 35 36 37 38 39
03 01 00 0E 02
00

FF FF
""",
            """41
02 01 01 27
""",
        ],
    },
    {
        "title": "Latihan 11: Parser Frame Protokol Serial",
        "difficulty": "Lanjut",
        "question": [
            "Sebuah sensor mengirim frame lewat kabel serial yang berisik.",
            "Masukan berisi aliran byte heks dipisah spasi atau baris baru,",
            "sampai akhir masukan (paling banyak 1024 byte).",
            "",
            "Bentuk satu frame:",
            "  AA  panjang  tipe  payload (sebanyak panjang byte)  crc8",
            "",
            "Aturan:",
            "  - panjang bernilai 0 sampai 16. CRC-8 dihitung dari byte",
            "    panjang, tipe, dan semua byte payload, dengan polinom 0x07",
            "    dan nilai awal 0x00 (nilai uji \"123456789\" = 0xF4).",
            "  - Byte yang bukan AA saat mencari awal frame dihitung sampah.",
            "  - Kalau sesudah AA datang panjang lebih dari 16, byte AA itu",
            "    dihitung sampah, dan pencarian diteruskan dari byte panjang",
            "    tadi (byte itu diperiksa lagi sebagai calon AA).",
            "  - Frame yang CRC-nya cocok dicetak:",
            "    sah: tipe TT, payload P1 P2 ...   (atau: payload kosong)",
            "  - Frame yang CRC-nya salah dibuang utuh dan dicetak:",
            "    rusak: tipe TT, crc XX, seharusnya YY",
            "    Pencarian dilanjutkan sesudah byte CRC frame itu.",
            "  - Kalau aliran habis di tengah frame, cetak",
            "    terpotong: N byte di akhir aliran",
            "    (N dihitung dari AA sampai byte terakhir) lalu berhenti.",
            "  - Terakhir cetak  ringkasan: S sah, R rusak, X byte sampah",
            "",
            "Untuk input berikut:",
            "  13 37 AA 02 01 01 27 A7",
            "  AA 01 02 50 00 FF AA 00 05 1B",
            "  AA 30 AA 01 03 10 24",
            "",
            "keluarannya:",
            "sah: tipe 01, payload 01 27",
            "rusak: tipe 02, crc 00, seharusnya F6",
            "sah: tipe 05, payload kosong",
            "sah: tipe 03, payload 10",
            "ringkasan: 3 sah, 1 rusak, 5 byte sampah",
        ],
        "hints": [
            "Simpan seluruh aliran ke larik statis dulu, lalu telusuri dengan indeks supaya kamu bisa melihat beberapa byte ke depan.",
            "Pada indeks i yang berisi AA, ukuran frame adalah panjang + 4, jadi frame utuh kalau i + ukuran tidak melewati jumlah byte.",
            "Baca byte dengan scanf(\"%x\", &x) ke unsigned int, dan hitung CRC-8 dari &a[i + 1] sebanyak panjang + 2 byte.",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n\n#define AWAL 0xAA\n#define PAYLOAD_MAKS 16\n#define ALIRAN_MAKS 1024\n\nstatic uint8_t crc8(const uint8_t *p, int n)\n{\n    uint8_t crc = 0x00;\n    for (int i = 0; i < n; i++) {\n        crc ^= p[i];\n        for (int b = 0; b < 8; b++)\n            crc = (crc & 0x80) ? (uint8_t)((crc << 1) ^ 0x07) : (uint8_t)(crc << 1);\n    }\n    return crc;\n}\n\nint main(void)\n{\n    static uint8_t a[ALIRAN_MAKS];\n    int n = 0;\n    unsigned int x;\n    while (n < ALIRAN_MAKS && scanf(\"%x\", &x) == 1)\n        a[n++] = (uint8_t)x;\n\n    int sah = 0, rusak = 0, sampah = 0;\n    int i = 0;\n    while (i < n) {\n        if (a[i] != AWAL) {              /* bukan awal frame: sampah */\n            sampah++;\n            i++;\n            continue;\n        }\n        if (i + 1 >= n) {                /* AA di ujung aliran */\n            printf(\"terpotong: 1 byte di akhir aliran\\n\");\n            break;\n        }\n        int len = a[i + 1];\n        if (len > PAYLOAD_MAKS) {        /* panjang mustahil: AA tadi sampah */\n            sampah++;\n            i++;\n            continue;\n        }\n        int ukuran = len + 4;            /* AA, panjang, tipe, payload, crc */\n        if (i + ukuran > n) {\n            printf(\"terpotong: %d byte di akhir aliran\\n\", n - i);\n            break;\n        }\n        const uint8_t *f = &a[i];\n        uint8_t harus = crc8(&f[1], len + 2);\n        uint8_t tiba = f[3 + len];\n        if (harus == tiba) {\n            sah++;\n            printf(\"sah: tipe %02X, payload\", f[2]);\n            if (len == 0)\n                printf(\" kosong\");\n            for (int j = 0; j < len; j++)\n                printf(\" %02X\", f[3 + j]);\n            printf(\"\\n\");\n        } else {\n            rusak++;\n            printf(\"rusak: tipe %02X, crc %02X, seharusnya %02X\\n\", f[2], tiba, harus);\n        }\n        i += ukuran;\n    }\n    printf(\"ringkasan: %d sah, %d rusak, %d byte sampah\\n\", sah, rusak, sampah);\n    return 0;\n}",
        "stdin_list": [
            """13 37 AA 02 01 01 27 A7
AA 01 02 50 00 FF AA 00 05 1B
AA 30 AA 01 03 10 24
""",
            """AA 03 01 00 0E 02 68 00 AA 02 01
""",
        ],
    },
    {
        "title": "Latihan 12: Pencocok Topik MQTT dengan Wildcard",
        "difficulty": "Lanjut",
        "question": [
            "Tulis fungsi pencocok topik seperti milik broker MQTT. Program",
            "membaca daftar langganan (filter), lalu daftar topik terbitan.",
            "",
            "Masukan:",
            "  baris 1: jumlah filter F (paling banyak 32)",
            "  F baris berikutnya: satu filter per baris",
            "  lalu jumlah topik T, diikuti T baris topik",
            "",
            "Aturan pencocokan (dari spesifikasi MQTT):",
            "  - Topik dan filter dipecah per tingkat dengan garis miring.",
            "    Huruf besar dan kecil dibedakan.",
            "  - + cocok dengan tepat satu tingkat, termasuk tingkat kosong.",
            "    rumah/+/suhu cocok dengan rumah//suhu, tapi rumah/+ nggak",
            "    cocok dengan rumah.",
            "  - # selalu di akhir filter dan cocok dengan semua sisa tingkat,",
            "    termasuk induknya sendiri: rumah/# cocok dengan rumah.",
            "  - Topik yang diawali $ nggak cocok dengan filter yang tingkat",
            "    pertamanya + atau #.",
            "",
            "Untuk tiap topik cetak  topik -> filter1, filter2  dengan filter",
            "yang cocok urut sesuai masukan, atau  topik -> tidak ada.",
            "",
            "Untuk input berikut:",
            "  6",
            "  rumah/+/suhu",
            "  rumah/#",
            "  rumah/dapur/suhu",
            "  +/+",
            "  #",
            "  $SYS/#",
            "  7",
            "  rumah/dapur/suhu",
            "  rumah",
            "  rumah/kamar/lembap",
            "  rumah//suhu",
            "  kantor/lantai1",
            "  $SYS/broker/uptime",
            "  /keuangan",
            "",
            "keluarannya:",
            "rumah/dapur/suhu -> rumah/+/suhu, rumah/#, rumah/dapur/suhu, #",
            "rumah -> rumah/#, #",
            "rumah/kamar/lembap -> rumah/#, #",
            "rumah//suhu -> rumah/+/suhu, rumah/#, #",
            "kantor/lantai1 -> +/+, #",
            "$SYS/broker/uptime -> $SYS/#",
            "/keuangan -> +/+, #",
        ],
        "hints": [
            "Bandingkan filter dan topik satu tingkat demi satu tingkat dari kiri, karena wildcard cuma berlaku untuk satu tingkat utuh.",
            "Tingkat # langsung berarti cocok, tingkat + selalu lolos, dan tingkat biasa harus sama persis panjang dan isinya.",
            "Pakai strcspn(p, \"/\") untuk panjang tingkat, dan kalau topik habis lebih dulu, cocok hanya bila sisa filter tepat \"/#\".",
        ],
        "solution": "#include <stdio.h>\n#include <stdbool.h>\n#include <string.h>\n\n#define MAKS_FILTER 32\n#define PANJANG 128\n\n/* Cocokkan satu tingkat demi satu tingkat. Tingkat dipisah '/'. */\nstatic bool cocok(const char *filter, const char *topik)\n{\n    /* Topik sistem ($SYS/...) tidak ditangkap wildcard di tingkat pertama. */\n    if (topik[0] == '$' && (filter[0] == '+' || filter[0] == '#'))\n        return false;\n\n    const char *f = filter, *t = topik;\n    for (;;) {\n        /* panjang tingkat sekarang di filter dan di topik */\n        size_t pf = strcspn(f, \"/\");\n        size_t pt = strcspn(t, \"/\");\n\n        if (pf == 1 && f[0] == '#')\n            return true;                     /* sisa topik apa pun cocok */\n        if (!(pf == 1 && f[0] == '+')) {     /* tingkat biasa: harus sama */\n            if (pf != pt || strncmp(f, t, pf) != 0)\n                return false;\n        }\n\n        bool f_habis = f[pf] == '\\0';\n        bool t_habis = t[pt] == '\\0';\n        if (f_habis && t_habis)\n            return true;\n        if (t_habis)                         /* topik habis, filter masih ada */\n            return strcmp(f + pf, \"/#\") == 0;  /* rumah/# cocok dengan rumah */\n        if (f_habis)\n            return false;\n        f += pf + 1;\n        t += pt + 1;\n    }\n}\n\nstatic void buang_akhir_baris(char *s)\n{\n    s[strcspn(s, \"\\r\\n\")] = '\\0';\n}\n\nint main(void)\n{\n    char filter[MAKS_FILTER][PANJANG];\n    char baris[PANJANG];\n    int nf = 0, nt = 0;\n\n    if (!fgets(baris, sizeof baris, stdin) || sscanf(baris, \"%d\", &nf) != 1)\n        return 1;\n    for (int i = 0; i < nf && i < MAKS_FILTER; i++) {\n        if (!fgets(filter[i], PANJANG, stdin))\n            return 1;\n        buang_akhir_baris(filter[i]);\n    }\n    if (!fgets(baris, sizeof baris, stdin) || sscanf(baris, \"%d\", &nt) != 1)\n        return 1;\n    for (int i = 0; i < nt; i++) {\n        if (!fgets(baris, sizeof baris, stdin))\n            return 1;\n        buang_akhir_baris(baris);\n        printf(\"%s ->\", baris);\n        int kena = 0;\n        for (int j = 0; j < nf; j++) {\n            if (cocok(filter[j], baris)) {\n                printf(\"%s %s\", kena ? \",\" : \"\", filter[j]);\n                kena++;\n            }\n        }\n        printf(\"%s\\n\", kena ? \"\" : \" tidak ada\");\n    }\n    return 0;\n}",
        "stdin_list": [
            """6
rumah/+/suhu
rumah/#
rumah/dapur/suhu
+/+
#
$SYS/#
7
rumah/dapur/suhu
rumah
rumah/kamar/lembap
rumah//suhu
kantor/lantai1
$SYS/broker/uptime
/keuangan
""",
            """2
pabrik/+/mesin/#
gudang/suhu
5
pabrik/a/mesin
pabrik/a/mesin/3/rpm
pabrik/a/b/mesin
Gudang/suhu
gudang/suhu/
""",
        ],
    },
    {
        "title": "Latihan 13: Watchdog Timer Tiruan",
        "difficulty": "Lanjut",
        "question": [
            "Tiru watchdog dan logika mode aman sebuah firmware.",
            "",
            "Masukan: jumlah tick N, lalu satu kata berisi N karakter.",
            "Karakter ke-t menyatakan apa yang terjadi di tick t (mulai 1):",
            "  T  loop utama menendang watchdog",
            "  .  nggak ada tendangan (sibuk atau macet)",
            "",
            "Aturan, dicek berurutan di setiap tick:",
            "  1. T membuat hitungan watchdog jadi 0. Selain itu hitungannya",
            "     naik 1. Hitungan tick sejak boot juga naik 1.",
            "  2. Kalau hitungan watchdog mencapai 5, chip direset. Cetak",
            "     tick t: watchdog reset (reset ke-R, beruntun B)",
            "     lalu hitungan watchdog dan tick sejak boot jadi 0.",
            "     Kalau B mencapai 3, cetak",
            "     tick t: 3 reset beruntun, masuk mode aman",
            "     dan berhenti memproses tick berikutnya.",
            "  3. Kalau nggak ada reset, tick sejak boot tepat 10, dan B",
            "     lebih dari 0, cetak",
            "     tick t: stabil 10 tick, hitungan beruntun dinolkan",
            "     lalu B jadi 0.",
            "  Terakhir cetak  ringkasan: R reset, mode normal  atau",
            "  ringkasan: R reset, mode aman",
            "",
            "Untuk input 23 TT.T.....TTTTTTTTTT..TT, keluarannya:",
            "tick 9: watchdog reset (reset ke-1, beruntun 1)",
            "tick 19: stabil 10 tick, hitungan beruntun dinolkan",
            "ringkasan: 1 reset, mode normal",
        ],
        "hints": [
            "Simpan empat angka: hitungan watchdog, tick sejak boot, total reset, dan reset beruntun, lalu ubah keempatnya menurut urutan aturan di soal.",
            "Pemeriksaan stabil hanya dilakukan di tick yang nggak berakhir dengan reset, dan hanya saat tick sejak boot tepat 10.",
            "Baca dengan scanf(\"%d %1023s\", &n, jejak), lalu telusuri jejak[t - 1] untuk t dari 1 sampai n.",
        ],
        "solution": "#include <stdio.h>\n#include <stdbool.h>\n\n#define BATAS_WDT       5   /* tick tanpa tendangan sebelum reset */\n#define TICK_STABIL    10   /* tick tanpa reset sesudah boot = stabil */\n#define MAKS_BERUNTUN   3   /* reset beruntun sebelum mode aman */\n\nint main(void)\n{\n    int n;\n    char jejak[1024];\n    if (scanf(\"%d %1023s\", &n, jejak) != 2)\n        return 1;\n\n    int hitung_wdt = 0, sejak_boot = 0;\n    int total_reset = 0, beruntun = 0;\n    bool mode_aman = false;\n\n    for (int t = 1; t <= n && jejak[t - 1] != '\\0'; t++) {\n        if (jejak[t - 1] == 'T')\n            hitung_wdt = 0;              /* task menendang watchdog */\n        else\n            hitung_wdt++;\n        sejak_boot++;\n\n        if (hitung_wdt >= BATAS_WDT) {\n            total_reset++;\n            beruntun++;\n            printf(\"tick %d: watchdog reset (reset ke-%d, beruntun %d)\\n\",\n                   t, total_reset, beruntun);\n            hitung_wdt = 0;\n            sejak_boot = 0;\n            if (beruntun >= MAKS_BERUNTUN) {\n                printf(\"tick %d: %d reset beruntun, masuk mode aman\\n\",\n                       t, MAKS_BERUNTUN);\n                mode_aman = true;\n                break;\n            }\n        } else if (sejak_boot == TICK_STABIL && beruntun > 0) {\n            printf(\"tick %d: stabil %d tick, hitungan beruntun dinolkan\\n\",\n                   t, TICK_STABIL);\n            beruntun = 0;\n        }\n    }\n    printf(\"ringkasan: %d reset, mode %s\\n\", total_reset, mode_aman ? \"aman\" : \"normal\");\n    return 0;\n}",
        "stdin_list": [
            """23 TT.T.....TTTTTTTTTT..TT
""",
            """28 TT......T.....TT......TTTTTT
""",
            """8 T.T.T.T.
""",
        ],
    },
    {
        "title": "Latihan 14: Firmware Lampu Lalu Lintas dengan Telemetri",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Proyek akhir: firmware lampu penyeberangan jalan yang mengirim",
            "telemetri lewat UART. Semua waktu dihitung dalam tick palsu.",
            "",
            "Masukan: jumlah tick N, lalu N karakter sampel tombol",
            "penyeberang, satu per tick mulai tick 0. Tombolnya active-low",
            "seperti di bab Arduino: 0 = ditekan, 1 = lepas.",
            "",
            "Setiap tick dikerjakan dalam urutan ini:",
            "",
            "1. Debounce tombol, state machine lepas, mungkin_tekan, tekan,",
            "   mungkin_lepas. Sampel dianggap stabil kalau tiga sampel",
            "   berturut-turut sama. Dari lepas, sampel ditekan pindah ke",
            "   mungkin_tekan. Sampel ditekan ketiga berturut-turut pindah ke",
            "   tekan. Sampel lepas di mungkin_tekan kembali ke lepas. Begitu",
            "   juga sebaliknya untuk melepas. Saat masuk tekan, cetak",
            "   t=T tombol ditekan",
            "   kirim frame tombol, dan catat permintaan menyeberang kecuali",
            "   lampu sedang SEBERANG.",
            "",
            "2. State machine lampu. lama = tick sekarang dikurangi tick saat",
            "   state dimulai. Mulai di MERAH pada tick 0.",
            "     MERAH (kode 1): lama >= 4 -> HIJAU",
            "     HIJAU (kode 2): lama >= 8, atau ada permintaan dan",
            "                     lama >= 3 -> KUNING",
            "     KUNING (kode 3): lama >= 2 -> SEBERANG kalau ada",
            "                      permintaan (permintaan dihapus), selain",
            "                      itu MERAH",
            "     SEBERANG (kode 4): lama >= 5 -> HIJAU",
            "   Setiap masuk state, termasuk MERAH di tick 0, cetak",
            "   t=T state NAMA  lalu kirim frame state.",
            "",
            "3. UART mengambil paling banyak 4 byte dari ring buffer. Kalau",
            "   ada yang terambil, cetak  t=T uart: XX XX ...",
            "",
            "Frame (format bab Protokol Biner, dengan CRC-16):",
            "  AA  panjang  tipe  payload  crc_tinggi  crc_rendah",
            "  - frame state: tipe 01, payload tick_tinggi tick_rendah kode",
            "  - frame tombol: tipe 02, payload tick_tinggi tick_rendah",
            "  - CRC-16/CCITT-FALSE (polinom 0x1021, awal 0xFFFF) dihitung",
            "    dari panjang, tipe, dan payload.",
            "",
            "Ring buffer 32 byte, kebijakan buang yang terbaru seperti di",
            "latihan Ring Buffer UART. Bedanya, yang dibuang frame utuh: kalau",
            "sisa ruang kurang dari ukuran frame, frame itu nggak dimasukkan",
            "sama sekali dan dihitung dibuang.",
            "",
            "Terakhir cetak",
            "  selesai: B byte tersisa di buffer, D frame dibuang",
            "",
            "Untuk input 22 1111110100011111111111, keluarannya:",
            "t=0 state MERAH",
            "t=0 uart: AA 03 01 00",
            "t=1 uart: 00 01 99 4B",
            "t=4 state HIJAU",
            "t=4 uart: AA 03 01 00",
            "t=5 uart: 04 02 65 EC",
            "t=10 tombol ditekan",
            "t=10 state KUNING",
            "t=10 uart: AA 02 02 00",
            "t=11 uart: 0A A6 82 AA",
            "t=12 state SEBERANG",
            "t=12 uart: 03 01 00 0A",
            "t=13 uart: 03 56 C2 AA",
            "t=14 uart: 03 01 00 0C",
            "t=15 uart: 04 8C 83",
            "t=17 state HIJAU",
            "t=17 uart: AA 03 01 00",
            "t=18 uart: 11 02 99 6A",
            "selesai: 0 byte tersisa di buffer, 0 frame dibuang",
        ],
        "hints": [
            "Pecah program jadi tiga bagian yang masing-masing sudah pernah kamu tulis di latihan sebelumnya: debounce, state machine berwaktu, dan ring buffer, lalu satukan dengan satu fungsi kirim frame.",
            "Hitung CRC-16 dari byte panjang sampai byte terakhir payload, lalu tempel byte tingginya dulu, dan cek ruang ring buffer sebelum memasukkan satu byte pun.",
            "Di dalam loop tick, kerjakan debounce, lalu state lampu dengan variabel masuk dan minta, lalu kuras UART, persis dalam urutan itu.",
        ],
        "solution": "#include <stdio.h>\n#include <stdint.h>\n#include <stdbool.h>\n\n/* ---------- lampu ---------- */\nenum lampu { MERAH = 1, HIJAU = 2, KUNING = 3, SEBERANG = 4 };\nstatic const char *NAMA[] = {\"\", \"MERAH\", \"HIJAU\", \"KUNING\", \"SEBERANG\"};\n\n#define LAMA_MERAH     4\n#define LAMA_HIJAU     8\n#define HIJAU_MINIMUM  3\n#define LAMA_KUNING    2\n#define LAMA_SEBERANG  5\n\n/* ---------- debounce ---------- */\nenum tombol { LEPAS, MUNGKIN_TEKAN, TEKAN, MUNGKIN_LEPAS };\n#define SAMPEL_STABIL 3\n\n/* ---------- frame dan CRC-16/CCITT-FALSE ---------- */\n#define AWAL          0xAA\n#define TIPE_STATE    0x01\n#define TIPE_TOMBOL   0x02\n\nstatic uint16_t crc16(const uint8_t *p, int n)\n{\n    uint16_t crc = 0xFFFF;\n    for (int i = 0; i < n; i++) {\n        crc ^= (uint16_t)(p[i] << 8);\n        for (int b = 0; b < 8; b++)\n            crc = (crc & 0x8000) ? (uint16_t)((crc << 1) ^ 0x1021) : (uint16_t)(crc << 1);\n    }\n    return crc;\n}\n\n/* ---------- ring buffer 32 byte, buang yang terbaru ---------- */\n#define UKURAN 32\n#define MASK   (UKURAN - 1)\nstatic uint8_t data[UKURAN];\nstatic uint8_t kepala, ekor;\nstatic int frame_dibuang;\n\nstatic int isi(void) { return (uint8_t)(kepala - ekor); }\n\nstatic void kirim(uint8_t tipe, const uint8_t *payload, int n)\n{\n    uint8_t f[24];\n    f[0] = AWAL;\n    f[1] = (uint8_t)n;\n    f[2] = tipe;\n    for (int i = 0; i < n; i++)\n        f[3 + i] = payload[i];\n    uint16_t c = crc16(&f[1], n + 2);\n    f[3 + n] = (uint8_t)(c >> 8);\n    f[4 + n] = (uint8_t)(c & 0xFF);\n    int ukuran = n + 5;\n\n    if (UKURAN - isi() < ukuran) {       /* tidak muat: frame utuh dibuang */\n        frame_dibuang++;\n        return;\n    }\n    for (int i = 0; i < ukuran; i++) {\n        data[kepala & MASK] = f[i];\n        kepala++;\n    }\n}\n\nstatic void lapor_state(int t, enum lampu s)\n{\n    uint8_t p[3] = {(uint8_t)(t >> 8), (uint8_t)(t & 0xFF), (uint8_t)s};\n    printf(\"t=%d state %s\\n\", t, NAMA[s]);\n    kirim(TIPE_STATE, p, 3);\n}\n\nint main(void)\n{\n    int n;\n    char sampel[1024];\n    if (scanf(\"%d %1023s\", &n, sampel) != 2)\n        return 1;\n\n    enum lampu state = MERAH;\n    int masuk = 0;                       /* tick saat state sekarang dimulai */\n    bool minta = false;                  /* permintaan penyeberang tertunda */\n\n    enum tombol tb = LEPAS;\n    int stabil = 0;\n\n    lapor_state(0, state);\n\n    for (int t = 0; t < n && sampel[t] != '\\0'; t++) {\n        /* 1. debounce tombol penyeberang */\n        bool ditekan = sampel[t] == '0';   /* active-low */\n        switch (tb) {\n        case LEPAS:\n            if (ditekan) { tb = MUNGKIN_TEKAN; stabil = 1; }\n            break;\n        case MUNGKIN_TEKAN:\n            if (!ditekan) {\n                tb = LEPAS;\n            } else if (++stabil >= SAMPEL_STABIL) {\n                tb = TEKAN;\n                printf(\"t=%d tombol ditekan\\n\", t);\n                uint8_t p[2] = {(uint8_t)(t >> 8), (uint8_t)(t & 0xFF)};\n                kirim(TIPE_TOMBOL, p, 2);\n                if (state != SEBERANG)\n                    minta = true;\n            }\n            break;\n        case TEKAN:\n            if (!ditekan) { tb = MUNGKIN_LEPAS; stabil = 1; }\n            break;\n        case MUNGKIN_LEPAS:\n            if (ditekan)\n                tb = TEKAN;\n            else if (++stabil >= SAMPEL_STABIL)\n                tb = LEPAS;\n            break;\n        }\n\n        /* 2. state machine lampu */\n        int lama = t - masuk;\n        enum lampu baru = state;\n        switch (state) {\n        case MERAH:\n            if (lama >= LAMA_MERAH) baru = HIJAU;\n            break;\n        case HIJAU:\n            if (lama >= LAMA_HIJAU || (minta && lama >= HIJAU_MINIMUM))\n                baru = KUNING;\n            break;\n        case KUNING:\n            if (lama >= LAMA_KUNING) {\n                baru = minta ? SEBERANG : MERAH;\n                minta = false;\n            }\n            break;\n        case SEBERANG:\n            if (lama >= LAMA_SEBERANG) baru = HIJAU;\n            break;\n        }\n        if (baru != state) {\n            state = baru;\n            masuk = t;\n            lapor_state(t, state);\n        }\n\n        /* 3. UART menguras paling banyak 4 byte */\n        if (isi() > 0) {\n            printf(\"t=%d uart:\", t);\n            for (int k = 0; k < 4 && isi() > 0; k++) {\n                printf(\" %02X\", data[ekor & MASK]);\n                ekor++;\n            }\n            printf(\"\\n\");\n        }\n    }\n    printf(\"selesai: %d byte tersisa di buffer, %d frame dibuang\\n\", isi(), frame_dibuang);\n    return 0;\n}",
        "stdin_list": [
            """22 1111110100011111111111
""",
            """30 111111111111110001111100011111
""",
            """16 1111111111111111
""",
        ],
    },
]
