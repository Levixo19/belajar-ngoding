"""Registry kurikulum: satu-satunya sumber kebenaran daftar bahasa.

Dulu ini tinggal di `main.py` bersama seluruh menu terminal, dan akibatnya
tidak kelihatan tapi mahal: `webapp/api.py` melakukan `import main`, sementara
`main.py` mengimpor SELURUH `layar/`. Jadi membuka aplikasi WEB ikut memuat
ribuan baris antarmuka terminal yang tidak dipakainya sama sekali.

Yang tinggal di sini cuma data dan hitungan yang dipakai KEDUA antarmuka:
registry `LANGUAGES`, versi, ringkasan statistik per bahasa, dan laporan
kemajuan. Tidak ada satu pun yang mencetak ke layar.

Menambah bahasa baru = tambah satu entri di `LANGUAGES` plus tiga berkas di
`data/`. Kurikulum ranah tech stack tidak ditulis di sini sama sekali; ia
datang dari `data/kurikulum_tech.py`.
"""

from datetime import date

from inti import runner
from pelajar.progress import (
    DAFTAR_BADGE, gelar_dari_level, info_level, judul_kunci, statistik_bahasa,
    streak_aktif,
)

from data import (
    JAVA_MATERIALS, JAVA_QUIZZES, JAVA_EXERCISES,
    SQL_MATERIALS, SQL_QUIZZES, SQL_EXERCISES,
    PYTHON_MATERIALS, PYTHON_QUIZZES, PYTHON_EXERCISES,
    JAVASCRIPT_MATERIALS, JAVASCRIPT_QUIZZES, JAVASCRIPT_EXERCISES,
    C_MATERIALS, C_QUIZZES, C_EXERCISES,
    CPP_MATERIALS, CPP_QUIZZES, CPP_EXERCISES,
    BASH_MATERIALS, BASH_QUIZZES, BASH_EXERCISES,
    GO_MATERIALS, GO_QUIZZES, GO_EXERCISES,
    APLIKASI_MATERIALS, APLIKASI_QUIZZES, APLIKASI_EXERCISES,
    HTML_MATERIALS, HTML_QUIZZES, HTML_EXERCISES,
    CSS_MATERIALS, CSS_QUIZZES, CSS_EXERCISES,
    CSHARP_MATERIALS, CSHARP_QUIZZES, CSHARP_EXERCISES,
    RUST_MATERIALS, RUST_QUIZZES, RUST_EXERCISES,
    PHP_MATERIALS, PHP_QUIZZES, PHP_EXERCISES,
    RUBY_MATERIALS, RUBY_QUIZZES, RUBY_EXERCISES,
    KOTLIN_MATERIALS, KOTLIN_QUIZZES, KOTLIN_EXERCISES,
    TYPESCRIPT_MATERIALS, TYPESCRIPT_QUIZZES, TYPESCRIPT_EXERCISES,
    VB_MATERIALS, VB_QUIZZES, VB_EXERCISES,
    FEDORA_MATERIALS, FEDORA_QUIZZES, FEDORA_EXERCISES,
    GIT_MATERIALS, GIT_QUIZZES, GIT_EXERCISES,
)

VERSI = "2.0"

# Registry semua bahasa. Menambah bahasa baru = tambah satu entri di sini
# plus tiga file di folder data/.
#   key     : prefix kategori progres, harus stabil (jangan diubah setelah rilis)
#   runner  : kunci toolchain di runner.TOOLCHAINS untuk eksekusi kode
LANGUAGES = [
    # HTML dan CSS berdiri paling depan, dan urutan itu disengaja. Keduanya
    # satu-satunya bahasa di daftar ini yang TIDAK membutuhkan satu program pun
    # untuk dipasang — cukup aplikasi ini dan sebuah browser. Buat orang yang
    # baru mulai dan belum sanggup memasang compiler apa pun, di sinilah pintu
    # masuk yang paling mungkin dilewati tanpa tersandung lebih dulu.
    {
        "key": "html", "label": "HTML", "runner": "html",
        "materials": HTML_MATERIALS, "quizzes": HTML_QUIZZES,
        "exercises": HTML_EXERCISES,
        "run_info": ["Buka berkasnya di browser: klik dua kali, atau Ctrl+O.",
                     "Di aplikasi ini strukturnya dibaca lalu ditampilkan",
                     "sebagai pohon elemen — itulah yang browser lihat dari",
                     "markup yang kamu tulis."],
    },
    {
        "key": "css", "label": "CSS", "runner": "css",
        "materials": CSS_MATERIALS, "quizzes": CSS_QUIZZES,
        "exercises": CSS_EXERCISES,
        "run_info": ['Tautkan dari HTML: <link rel="stylesheet" href="gaya.css">',
                     "lalu buka berkas HTML-nya di browser.",
                     "Di aplikasi ini aturannya dibaca lalu ditampilkan setelah",
                     "dirapikan: pemilih, lalu properti dan nilainya."],
    },
    {
        "key": "java", "label": "Java", "runner": "java",
        "materials": JAVA_MATERIALS, "quizzes": JAVA_QUIZZES, "exercises": JAVA_EXERCISES,
        "run_info": ["Kompilasi : javac NamaFile.java", "Jalankan  : java NamaFile"],
    },
    {
        "key": "sql", "label": "SQL", "runner": "sql",
        "materials": SQL_MATERIALS, "quizzes": SQL_QUIZZES, "exercises": SQL_EXERCISES,
        "run_info": ["Latihan dijalankan dengan SQLite: sqlite3 :memory: < file.sql",
                     "Di MySQL/MariaDB: mysql -u root -p"],
    },
    {
        "key": "python", "label": "Python", "runner": "python",
        "materials": PYTHON_MATERIALS, "quizzes": PYTHON_QUIZZES,
        "exercises": PYTHON_EXERCISES,
        "run_info": ["Jalankan : python3 nama_file.py"],
    },
    {
        "key": "javascript", "label": "JavaScript", "runner": "javascript",
        "materials": JAVASCRIPT_MATERIALS, "quizzes": JAVASCRIPT_QUIZZES,
        "exercises": JAVASCRIPT_EXERCISES,
        "run_info": ["Jalankan di Node.js : node nama_file.js",
                     "Atau tempel di console browser (F12 > Console)."],
    },
    {
        "key": "c", "label": "C", "runner": "c",
        "materials": C_MATERIALS, "quizzes": C_QUIZZES, "exercises": C_EXERCISES,
        "run_info": ["Kompilasi : gcc nama_file.c -o program", "Jalankan  : ./program"],
    },
    {
        "key": "cpp", "label": "C++", "runner": "cpp",
        "materials": CPP_MATERIALS, "quizzes": CPP_QUIZZES, "exercises": CPP_EXERCISES,
        "run_info": ["Kompilasi : g++ nama_file.cpp -o program", "Jalankan  : ./program"],
    },
    {
        "key": "bash", "label": "Bash", "runner": "bash",
        "materials": BASH_MATERIALS, "quizzes": BASH_QUIZZES, "exercises": BASH_EXERCISES,
        "run_info": ["Jalankan : bash nama_file.sh",
                     "Atau: chmod +x nama_file.sh && ./nama_file.sh"],
    },
    {
        "key": "go", "label": "Go", "runner": "go",
        "materials": GO_MATERIALS, "quizzes": GO_QUIZZES, "exercises": GO_EXERCISES,
        "run_info": ["Jalankan : go run nama_file.go", "Build    : go build nama_file.go"],
    },
    {
        "key": "csharp", "label": "C#", "runner": "csharp",
        "materials": CSHARP_MATERIALS, "quizzes": CSHARP_QUIZZES,
        "exercises": CSHARP_EXERCISES,
        "run_info": ["Buat proyek : dotnet new console -o latihan",
                     "Jalankan    : cd latihan && dotnet run",
                     "Di aplikasi ini berkas Program.cs-mu dibungkus proyek",
                     "sementara, lalu dibangun dengan dotnet build."],
    },
    {
        "key": "rust", "label": "Rust", "runner": "rust",
        "materials": RUST_MATERIALS, "quizzes": RUST_QUIZZES,
        "exercises": RUST_EXERCISES,
        "run_info": ["Satu berkas : rustc main.rs -o program && ./program",
                     "Proyek      : cargo new nama && cd nama && cargo run",
                     "Periksa saja: cargo check  (jauh lebih cepat)"],
    },
    {
        "key": "php", "label": "PHP", "runner": "php",
        "materials": PHP_MATERIALS, "quizzes": PHP_QUIZZES,
        "exercises": PHP_EXERCISES,
        "run_info": ["Jalankan : php berkas.php",
                     "Periksa  : php -l berkas.php",
                     "Server   : php -S localhost:8000",
                     "Materi ini memakai PHP 8; tutorial ber-mysql_query",
                     "atau ereg ditulis untuk PHP 5 yang sudah lama tamat."],
    },
    {
        "key": "ruby", "label": "Ruby", "runner": "ruby",
        "materials": RUBY_MATERIALS, "quizzes": RUBY_QUIZZES,
        "exercises": RUBY_EXERCISES,
        "run_info": ["Jalankan   : ruby berkas.rb",
                     "Interaktif : irb",
                     "Periksa    : ruby -c berkas.rb"],
    },
    {
        "key": "kotlin", "label": "Kotlin", "runner": "kotlin",
        "materials": KOTLIN_MATERIALS, "quizzes": KOTLIN_QUIZZES,
        "exercises": KOTLIN_EXERCISES,
        "run_info": ["Kompilasi : kotlinc main.kt -d kelas",
                     "Jalankan  : kotlin -cp kelas MainKt",
                     "Satu jar  : kotlinc main.kt -include-runtime -d main.jar",
                     "Nama berkas menentukan nama class: main.kt -> MainKt.",
                     "Butuh JDK 17+ terpasang lebih dulu."],
    },
    {
        "key": "typescript", "label": "TypeScript", "runner": "typescript",
        "materials": TYPESCRIPT_MATERIALS, "quizzes": TYPESCRIPT_QUIZZES,
        "exercises": TYPESCRIPT_EXERCISES,
        "run_info": ["Kompilasi : tsc berkas.ts", "Jalankan  : node berkas.js",
                     "Sekaligus : npx tsx berkas.ts",
                     "Di aplikasi ini kodemu dikompilasi dengan --strict dan",
                     "target ES2023, lalu hasilnya dijalankan Node."],
    },
    {
        "key": "vb", "label": "Visual Basic", "runner": "vb",
        "materials": VB_MATERIALS, "quizzes": VB_QUIZZES,
        "exercises": VB_EXERCISES,
        "run_info": ["Buat proyek : dotnet new console -lang VB -o latihan",
                     "Jalankan    : cd latihan && dotnet run",
                     "Yang dipelajari di sini VB.NET, BUKAN VB6 atau VBA.",
                     "Option Strict dinyalakan, jadi konversi tipe harus",
                     "ditulis dan salah tipe ketahuan saat kompilasi."],
    },
    {
        # Bukan bahasa pemrograman, melainkan kurikulum arsitektur aplikasi.
        # Latihannya Java murni, jadi memakai runner "java" yang sudah ada.
        "key": "aplikasi", "label": "Bikin Aplikasi", "runner": "java",
        "tematik": True,
        "materials": APLIKASI_MATERIALS, "quizzes": APLIKASI_QUIZZES,
        "exercises": APLIKASI_EXERCISES,
        "run_info": ["Kompilasi : javac NamaFile.java", "Jalankan  : java NamaFile",
                     "Modul ini melatih cara berpikir membangun aplikasi,",
                     "bukan sintaks. Kerjakan setelah Java dasar terasa nyaman."],
    },
    {
        "key": "fedora", "label": "CLI Fedora", "runner": "fedora",
        "tematik": True,
        "materials": FEDORA_MATERIALS, "quizzes": FEDORA_QUIZZES,
        "exercises": FEDORA_EXERCISES,
        "run_info": ["Jalankan : bash nama_file.sh",
                     "Atau     : chmod +x nama_file.sh && ./nama_file.sh",
                     "Blok perintah di materi adalah SESI TERMINAL: baca dulu,",
                     "ketik sendiri, jangan dijalankan aplikasi. Yang berawalan",
                     "sudo mengubah sistemmu sungguhan.",
                     "Latihannya aman: semuanya bekerja di direktori sementara",
                     "dengan hak pengguna biasa, tidak ada yang perlu sudo."],
    },
    {
        "key": "git", "label": "Git & GitHub", "runner": "git",
        "tematik": True,
        "materials": GIT_MATERIALS, "quizzes": GIT_QUIZZES,
        "exercises": GIT_EXERCISES,
        "run_info": ["Jalankan : bash nama_file.sh",
                     "Latihannya skrip bash yang membuat repositori sendiri di",
                     "direktori sementara (mktemp -d), jadi repositorimu aman.",
                     "Blok perintah di materi adalah SESI TERMINAL: ketik sendiri",
                     "di repositorimu, jangan dijalankan aplikasi. reset --hard",
                     "dan push --force mengubah riwayat sungguhan."],
    },
]

# Kurikulum tech stack (frontend, backend, DevOps, ...) tinggal di satu
# registry; tiap kurikulum baru muncul begitu ketiga berkas datanya lengkap.
from data import kurikulum_tech  # noqa: E402
LANGUAGES.extend(kurikulum_tech.entri())

def _soal_per_kuis(lang):
    # Berkunci judul_kunci, sama seperti kunci progres yang tersimpan. Judul
    # kuis memang tidak berbentuk "angka-titik" sehingga tidak berubah hari
    # ini — tapi peta yang kuncinya beda bentuk dari yang mencarinya adalah
    # bug yang menunggu giliran, dan yang hilang nanti cuma penyebut skor:
    # angka yang salah, bukan error yang kelihatan.
    return {judul_kunci(q["title"]): len(q["questions"])
            for q in lang["quizzes"]}


def _tak_dinilai(lang):
    """Berapa latihan bahasa ini yang memang tidak bisa dinilai otomatis."""
    if not runner.tersedia(lang["runner"]):
        return len(lang["exercises"])
    return sum(1 for e in lang["exercises"] if e.get("auto_check") is False)


def _stat(lang, data):
    return statistik_bahasa(
        data, lang["key"], len(lang["materials"]), len(lang["quizzes"]),
        len(lang["exercises"]),
        soal_per_kuis=_soal_per_kuis(lang),
        latihan_tak_dinilai=_tak_dinilai(lang),
    )




def _teks_laporan(data):
    """Laporan kemajuan dalam Markdown, siap disimpan atau ditempel di mana pun."""
    xp = data.get("xp", 0)
    level, _, _ = info_level(xp)
    streak = data.get("streak", {})
    baris = [
        "# Laporan Kemajuan belajar-codingV2",
        "",
        f"Tanggal : {date.today().isoformat()}",
        f"Level   : {level} - {gelar_dari_level(level)}  ({xp} XP)",
        f"Streak  : {streak_aktif(data)} hari berjalan, "
        f"rekor {streak.get('terpanjang', 0)}, "
        f"total {streak.get('total_hari', 0)} hari belajar",
        f"Badge   : {len(data.get('badge', []))} dari {len(DAFTAR_BADGE)}",
        "",
        "## Progres per bahasa",
        "",
        "| Bahasa | Materi | Kuis | Latihan | Skor kuis | Selesai |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for lang in LANGUAGES:
        s = _stat(lang, data)
        skor = f"{s['skor']}/{s['skor_maks']}" if s["skor_maks"] else "-"
        baris.append(
            f"| {lang['label']} | {s['materi']}/{s['total_materi']} "
            f"| {s['kuis']}/{s['total_kuis']} "
            f"| {s['latihan_lulus'] + s['latihan_manual']}/{s['total_latihan']} "
            f"| {skor} | {s['persen']:.0f}% |"
        )

    dimiliki = set(data.get("badge", []))
    baris += ["", "## Badge yang terbuka", ""]
    terbuka = [f"- {nama} - {desk}" for bid, nama, desk, _ in DAFTAR_BADGE
               if bid in dimiliki]
    baris += terbuka or ["- (belum ada)"]
    return "\n".join(baris) + "\n"
