"""Kurikulum Mobile & Desktop.

Dirakit alat/rakit_kurikulum.py dari draf per bab (2026-10-19).
Sesudah dirakit, berkas ini disunting seperti kurikulum lain
(alat/ganti_badan.py, alat/tambah_bagian.py). <KEY>_BAB tetap
spesifikasi JUMLAH; rentangnya dihitung data/kurikulum_tech.py.
"""

MOBILE_BAB = [
    {
        "judul": "Peta Dunia Aplikasi",
        "ket": "Empat cara membuat aplikasi dan jalur belajar dari Fedora.",
        "tingkat": "dasar",
        "jumlah": 3,
    },
    {
        "judul": "Android Pertama",
        "ket": "Platform, alat, sistem build, dan siklus hidup aplikasi Android.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Jetpack Compose",
        "ket": "Membangun layar Android secara deklaratif dengan state.",
        "tingkat": "dasar",
        "jumlah": 4,
    },
    {
        "judul": "Arsitektur Aplikasi Android",
        "ket": "ViewModel, coroutines, database lokal, jaringan, dan DI.",
        "tingkat": "menengah",
        "jumlah": 5,
    },
    {
        "judul": "Dunia Apple dari Linux",
        "ket": "Swift, SwiftUI, UIKit, dan alat Apple dengan batas yang jujur.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Flutter dan Dart",
        "ket": "Satu kode Dart untuk Android, iOS, web, dan desktop.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "React Native dan Expo",
        "ket": "Aplikasi native dari React, plus build iOS lewat cloud.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Berbagi Kode Lintas Platform Lain",
        "ket": "Kotlin Multiplatform, aplikasi hybrid, dan pemain lain.",
        "tingkat": "menengah",
        "jumlah": 3,
    },
    {
        "judul": "Aplikasi Desktop",
        "ket": "Electron, Tauri, Wails, immediate mode, dan toolkit native.",
        "tingkat": "menengah",
        "jumlah": 4,
    },
    {
        "judul": "Uji, Otomasi, dan Layanan Backend",
        "ket": "Pengujian, Firebase, dan Fastlane untuk aplikasi mobile.",
        "tingkat": "mahir",
        "jumlah": 3,
    },
    {
        "judul": "Rilis ke Toko Aplikasi",
        "ket": "Play Store, App Store, toko lain, dan aturan baru 2025-2026.",
        "tingkat": "mahir",
        "jumlah": 5,
    },
]

MOBILE_MATERIALS = [
    {
        "title": "1. Native, Lintas Platform, Web, dan Desktop",
        "sections": [
            {
                "body": [
                    "Coba buka HP-mu. Ada WhatsApp, aplikasi bank, game, aplikasi",
                    "ojek online, mungkin juga aplikasi kasir punya warung tetangga.",
                    "Semuanya kelihatan sama aja: ikon di layar, diketuk, terbuka.",
                    "Tapi cara bikinnya bisa beda jauh.",
                    "",
                    "Kurikulum ini membahas aplikasi yang jalan di HP dan di laptop.",
                    "Sebelum masuk ke kodenya, kamu perlu tahu dulu ada empat cara",
                    "besar untuk bikin aplikasi. Pilihan itu menentukan bahasa yang",
                    "kamu pelajari, alat yang kamu pasang, dan berapa banyak kode yang",
                    "harus kamu tulis.",
                    "",
                    "Satu istilah dulu. Platform artinya sistem operasi tempat",
                    "aplikasi jalan: Android dan iOS di HP, lalu Windows, macOS, dan",
                    "Linux di laptop. Aplikasi untuk satu platform nggak otomatis bisa",
                    "jalan di platform lain.",
                ],
            },
            {
                "heading": "Cara pertama: native",
                "body": [
                    "Native artinya aplikasi ditulis pakai bahasa dan alat resmi dari",
                    "pembuat platformnya. Untuk Android itu Kotlin, Android SDK, dan",
                    "Jetpack Compose dari Google. Untuk iPhone itu Swift, SwiftUI atau",
                    "UIKit, dan Xcode dari Apple. SDK (Software Development Kit) adalah",
                    "paket berisi pustaka, alat build, dan emulator yang disediakan",
                    "pembuat platform.",
                    "",
                    "Kelebihannya, aplikasi native bisa memakai fitur HP begitu fitur",
                    "itu dirilis, tampilannya pas dengan kebiasaan pengguna platform",
                    "itu, dan performanya paling bisa diatur. Kekurangannya juga",
                    "jelas. Kalau kamu mau aplikasi yang sama ada di Android dan",
                    "iPhone, kamu menulis dua aplikasi terpisah dengan dua bahasa.",
                    "Makanya banyak perusahaan punya tim Android dan tim iOS",
                    "sendiri-sendiri.",
                ],
            },
            {
                "heading": "Cara kedua: lintas platform",
                "body": [
                    "Lintas platform (cross-platform) artinya satu kode dipakai untuk",
                    "beberapa platform. Yang paling banyak dipakai sekarang:",
                    "  - Flutter dari Google, pakai bahasa Dart. Flutter menggambar",
                    "    sendiri setiap piksel di layar, jadi tampilannya sama persis",
                    "    di Android dan iPhone. Versi stabil terbaru saat materi ini",
                    "    ditulis (Oktober 2026) adalah 3.47.7.",
                    "  - React Native dari Meta, pakai JavaScript atau TypeScript",
                    "    dengan gaya React. Komponennya diubah jadi tampilan native",
                    "    milik platform, jadi nggak ada HTML di layar. Versi",
                    "    terbarunya 0.88, dirilis Oktober 2026.",
                    "  - Kotlin Multiplatform dari JetBrains. Yang dibagi biasanya",
                    "    logikanya (jaringan, database, aturan bisnis), sementara",
                    "    tampilannya boleh tetap native di tiap platform.",
                    "",
                    "Kelebihannya, satu tim bisa melayani dua platform. Harganya:",
                    "fitur baru Android atau iOS biasanya baru bisa dipakai setelah",
                    "framework-nya menyusul, dan untuk fitur yang belum didukung kamu",
                    "tetap harus menulis sedikit kode native. Aplikasi iOS-nya juga",
                    "tetap harus di-build di macOS. Soal itu dibahas di materi",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Cara ketiga: web dan PWA",
                "body": [
                    "Aplikasi web dibuka lewat browser, jadi otomatis jalan di semua",
                    "perangkat yang punya browser. Kalau kamu sudah belajar HTML, CSS,",
                    "dan JavaScript, kamu sudah bisa bikin ini.",
                    "",
                    "PWA (Progressive Web App) adalah aplikasi web yang bisa dipasang",
                    "ke layar utama HP dan tetap bisa dibuka waktu offline. Yang bikin",
                    "bisa offline itu service worker, yaitu skrip yang jalan di",
                    "belakang halaman dan menyimpan salinan berkas di HP.",
                    "",
                    "Web atau PWA sering udah cukup untuk daftar produk, formulir",
                    "pendaftaran, atau dasbor sederhana. Batasnya ada di akses ke",
                    "perangkat. Contohnya, Safari di iPhone nggak mendukung Web",
                    "Bluetooth. Notifikasi push untuk web di iPhone juga baru ada",
                    "sejak iOS 16.4, itu pun cuma untuk web app yang sudah ditambahkan",
                    "ke layar utama. Kalau aplikasimu butuh hal semacam itu, kamu",
                    "bakal mentok.",
                ],
            },
            {
                "heading": "Cara keempat: aplikasi desktop",
                "body": [
                    "Aplikasi desktop jalan di Windows, macOS, atau Linux. Pilihannya",
                    "juga banyak:",
                    "  - Electron membungkus halaman web jadi aplikasi desktop. Tiap",
                    "    aplikasi membawa Chromium dan Node.js sendiri, makanya",
                    "    ukurannya besar. Visual Studio Code dibangun di atas",
                    "    Electron. Versinya sekarang 44.9.0.",
                    "  - Tauri mirip Electron, tapi memakai webview bawaan sistem",
                    "    operasi dan bagian belakangnya ditulis di Rust, jadi ukuran",
                    "    aplikasinya jauh lebih kecil.",
                    "  - Toolkit native seperti Qt, GTK (dipakai desktop GNOME di",
                    "    Fedora-mu), dan WPF di Windows.",
                    "",
                    "Semuanya dibahas lebih dalam di bab Aplikasi Desktop.",
                ],
            },
            {
                "heading": "Dari kode ke aplikasi",
                "bahasa": "teks",
                "code": """cara             kamu menulis     diubah oleh      hasilnya jalan di
native Android   Kotlin           Android SDK      Android
native iOS       Swift            Xcode (macOS)    iPhone, iPad
Flutter          Dart             Flutter          Android, iOS, web, desktop
React Native     JavaScript/TS    React Native     Android, iOS
PWA              HTML, CSS, JS    browser          semua yang punya browser
Electron         HTML, CSS, JS    Electron         Windows, macOS, Linux""",
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "Empat pertanyaan ini paling menolong waktu memilih:",
                    "  1. Siapa penggunanya dan HP apa yang mereka pakai? Di Indonesia",
                    "     Android jauh lebih umum, tapi kalau banyak penggunamu pakai",
                    "     iPhone, iOS nggak bisa dilewati.",
                    "  2. Fitur HP apa yang dibutuhkan? Kamera, lokasi, dan notifikasi",
                    "     bisa dipakai dari semua cara. Bluetooth, NFC, atau sensor",
                    "     khusus lebih aman lewat native atau lintas platform.",
                    "  3. Bahasa apa yang sudah kamu kuasai? Dari JavaScript, React",
                    "     Native paling dekat. Dari Kotlin, Android native atau Kotlin",
                    "     Multiplatform.",
                    "  4. Perlu masuk toko aplikasi? PWA nggak wajib lewat toko, tapi",
                    "     juga nggak otomatis muncul di Play Store atau App Store.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: lintas platform sering dibaca \"tulis sekali, beres di",
                    "semua tempat\". Kenyataannya kamu tetap menguji di Android dan",
                    "iPhone, tetap mengurus tanda tangan aplikasi dan aturan dua toko,",
                    "dan tetap butuh macOS untuk build iOS. Yang berkurang adalah",
                    "jumlah kode tampilan dan logika yang ditulis dua kali.",
                    "",
                    "Satu lagi: jangan memilih karena katanya paling cepat. Flutter,",
                    "React Native, dan native sama-sama dipakai di aplikasi besar.",
                    "Untuk aplikasi pertamamu, beda kecepatannya nggak bakal terasa.",
                    "Yang terasa adalah seberapa nyaman kamu dengan bahasanya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kamu bisa ngecek sendiri satu contoh. Buka Visual Studio Code,",
                    "lalu pilih Help > About. Jendela itu menampilkan versi Electron,",
                    "Chromium, dan Node.js yang dibawa aplikasinya. Itu tanda aplikasi",
                    "desktop yang dibangun dari teknologi web. Di HP, aplikasi toko",
                    "online dan layanan sering memakai Flutter atau React Native supaya",
                    "satu tim bisa merilis versi Android dan iOS bersamaan.",
                    "",
                    "Kasus kecil: koperasi sekolahmu minta aplikasi untuk anggota.",
                    "Isinya daftar barang, harga, dan stok. Anggotanya pakai Android",
                    "dan iPhone, dan nggak ada yang punya Mac.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis kebutuhannya: daftar barang, harga, stok, mungkin",
                    "     pemesanan.",
                    "     Nggak ada Bluetooth, NFC, atau sensor khusus.",
                    "  2. Karena kebutuhannya cuma menampilkan data dan formulir, coba",
                    "     PWA dulu. Satu kode HTML, CSS, dan JavaScript langsung jalan",
                    "     di Android dan iPhone lewat browser, tanpa biaya akun toko.",
                    "  3. Kalau nanti koperasi minta notifikasi stok atau ingin",
                    "     aplikasinya ada di Play Store dan App Store, pindah ke React",
                    "     Native dengan Expo. Kode JavaScript-mu masih kepakai, dan",
                    "     build iOS bisa dikerjakan layanan cloud tanpa Mac.",
                    "  4. Catat alasan pilihanmu di README proyek, supaya pengurus",
                    "     berikutnya tahu kenapa aplikasinya nggak dibuat native.",
                ],
            },
        ],
    },
    {
        "title": "2. Jalur Belajar dari Fedora Tanpa Mac",
        "sections": [
            {
                "body": [
                    "Kamu pakai laptop Fedora dan nggak punya Mac. Kabar baiknya,",
                    "hampir semua alat di kurikulum ini jalan di Linux:",
                    "  - Android Studio dan emulator Android. Syaratnya Linux 64-bit",
                    "    berprosesor x86_64; Linux berprosesor ARM belum didukung.",
                    "  - Flutter, React Native dengan Expo, dan Kotlin Multiplatform,",
                    "    untuk bagian Android-nya.",
                    "  - Electron dan Tauri untuk aplikasi desktop.",
                    "  - Bahasa Swift. Swift bisa dipasang di Linux dari swift.org,",
                    "    jadi kamu tetap bisa belajar bahasanya.",
                    "",
                    "Yang nggak jalan cuma satu, tapi besar: Xcode. Tanpa Xcode, kamu",
                    "nggak bisa membangun aplikasi iOS di laptopmu sendiri, termasuk",
                    "yang memakai SwiftUI atau UIKit.",
                ],
            },
            {
                "heading": "Kenapa iOS butuh macOS",
                "body": [
                    "Apple cuma merilis Xcode untuk macOS. Di dalam Xcode ada SDK iOS,",
                    "compiler untuk aplikasi iPhone, alat penanda tangan aplikasi, dan",
                    "iOS Simulator. Semua itu nggak tersedia untuk Linux atau Windows.",
                    "Lisensi macOS sendiri cuma mengizinkan macOS dipasang di komputer",
                    "buatan Apple.",
                    "",
                    "Aturannya juga terus naik. Sejak 28 April 2026, aplikasi yang",
                    "diunggah ke App Store wajib dibangun dengan Xcode 26 atau yang",
                    "lebih baru. Jadi Mac yang terlalu tua untuk memasang Xcode",
                    "terbaru juga nggak bisa dipakai untuk rilis.",
                ],
            },
            {
                "heading": "Build di cloud",
                "body": [
                    "Jalan keluarnya adalah build cloud, yaitu layanan yang",
                    "menyewakan mesin macOS lewat internet. Kamu mengirim kodenya,",
                    "mesin macOS di sana menjalankan Xcode, lalu kamu menerima berkas",
                    "aplikasi iOS yang siap diunggah ke App Store. Dua yang paling",
                    "sering dipakai untuk keadaan seperti ini:",
                    "  - EAS Build dari Expo, untuk proyek React Native. Paket",
                    "    gratisnya saat materi ini ditulis (Oktober 2026) berisi 15",
                    "    build Android dan 15 build iOS per bulan, dengan antrean",
                    "    prioritas rendah.",
                    "  - Codemagic, untuk Flutter, React Native, dan proyek native.",
                    "    Akun pribadi gratisnya dapat 500 menit mesin macOS M2 per",
                    "    bulan.",
                    "",
                    "Layanan CI seperti GitHub Actions juga punya mesin macOS. Kuota",
                    "dan harga semua layanan ini bisa berubah, jadi cek halaman",
                    "harganya sebelum merencanakan rilis.",
                    "",
                    "Build cloud cuma membereskan urusan build. Dua hal ini tetap",
                    "harus kamu siapkan sendiri:",
                    "  - Akun Apple Developer Program, 99 dolar AS per tahun. Akun",
                    "    ini dibutuhkan untuk memasang hasil build di iPhone",
                    "    sungguhan tanpa Xcode dan untuk rilis ke App Store.",
                    "  - Sebuah iPhone untuk mencoba. Selama belajar, aplikasi Expo Go",
                    "    di iPhone bisa menjalankan proyek Expo langsung dari laptop",
                    "    Fedora, asalkan proyeknya nggak memakai kode native buatan",
                    "    sendiri.",
                ],
            },
            {
                "heading": "Biaya akun toko",
                "body": [
                    "Untuk merilis, kamu butuh akun di toko aplikasinya:",
                    "  - Google Play: 25 dolar AS, sekali bayar.",
                    "  - Apple Developer Program: 99 dolar AS per tahun. Kalau",
                    "    keanggotaannya habis, aplikasimu hilang dari App Store.",
                    "",
                    "Ada dua aturan Android yang perlu kamu tahu dari sekarang, karena",
                    "banyak tutorial lama belum menyebutnya. Akun Play pribadi yang",
                    "baru wajib menjalankan uji tertutup dengan minimal 12 penguji",
                    "selama 14 hari berturut-turut sebelum boleh rilis ke publik.",
                    "Lalu sejak 30 September 2026, aplikasi yang dipasang di HP",
                    "Android bersertifikat di Indonesia harus berasal dari developer",
                    "yang terverifikasi, termasuk APK yang dibagikan di luar Play",
                    "Store. Untuk pelajar ada akun distribusi terbatas yang gratis,",
                    "tanpa KTP, untuk paling banyak 20 perangkat. Rinciannya ada di",
                    "bab Rilis ke Toko Aplikasi.",
                ],
            },
            {
                "heading": "Tabel keputusan",
                "bahasa": "teks",
                "code": """target           bahasa yang kamu kuasai   jalur
android          kotlin                    Kotlin + Jetpack Compose
android          javascript                React Native + Expo
android          dart                      Flutter
ios / keduanya   javascript                React Native + Expo
ios / keduanya   dart                      Flutter
ios / keduanya   kotlin                    Kotlin Multiplatform
desktop          javascript                Electron
desktop          kotlin                    Compose Multiplatform
desktop          dart                      Flutter

build iOS, diperiksa dari atas:
  target android atau desktop      -> tidak perlu
  punya Mac                        -> Xcode di Mac sendiri
  tanpa Mac, React Native + Expo   -> EAS Build
  tanpa Mac, jalur lain            -> Codemagic""",
            },
            {
                "body": [
                    "Cara membacanya: cari baris yang cocok dengan target aplikasimu",
                    "dan bahasa yang kamu kuasai. Kata keduanya artinya Android dan",
                    "iPhone sekaligus. Kalau aplikasimu harus jalan di iPhone, lihat",
                    "aturan build iOS di bawah tabel.",
                    "",
                    "Tabel ini sengaja disederhanakan supaya bisa dipakai di latihan",
                    "bab ini. Di dunia kerja, pilihannya juga ditentukan tim dan kode",
                    "yang sudah ada.",
                    "",
                    "Data masukan latihan nanti berbentuk baris kunci=nilai. Potongan",
                    "JavaScript di bawah mengubah baris seperti itu jadi objek, jadi",
                    "urutan barisnya nggak penting lagi.",
                ],
            },
            {
                "heading": "Dari baris kunci=nilai ke objek",
                "code": "const masukan = 'target=keduanya\\nmac=tidak\\nbahasa=javascript';\nconst data = {};\nfor (const baris of masukan.split('\\n')) {\n  const [kunci, nilai] = baris.split('=');\n  data[kunci] = nilai;\n}\nconsole.log(data);\nconsole.log('target:', data.target);",
            },
            {
                "body": [
                    "Keluaran:",
                    "  { target: 'keduanya', mac: 'tidak', bahasa: 'javascript' }",
                    "  target: keduanya",
                    "",
                    "split('=') memotong satu baris jadi dua bagian, dan destructuring",
                    "[kunci, nilai] menaruh bagian pertama ke kunci dan bagian kedua",
                    "ke nilai. Sesudah itu kamu cukup bertanya data.target atau",
                    "data.mac, di mana pun barisnya tadi berada.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: mengira build cloud bisa menggantikan Mac sepenuhnya.",
                    "Build cloud membuatkan berkas aplikasinya, tapi kamu nggak bisa",
                    "membuka iOS Simulator atau men-debug langkah demi langkah di",
                    "Xcode. Untuk melihat aplikasinya jalan, kamu tetap butuh iPhone",
                    "sungguhan.",
                    "",
                    "Jebakan: menunda urusan akun sampai aplikasinya jadi. Uji",
                    "tertutup Play butuh 14 hari dan 12 penguji, jadi kumpulkan",
                    "pengujinya dari awal, misalnya teman sekelas.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak developer Flutter dan React Native bekerja di Windows atau",
                    "Linux, lalu menyerahkan build iOS ke layanan cloud. Expo dan",
                    "Codemagic menulis alur ini di dokumentasi resminya, termasuk cara",
                    "mengunggah hasil build langsung ke App Store Connect dari mesin",
                    "cloud tanpa pernah menyentuh Mac.",
                    "",
                    "Kasus kecil: kamu sedang PKL dan ingin menunjukkan aplikasi",
                    "catatan buatanmu ke pembimbing yang memakai iPhone. Laptopmu",
                    "Fedora, dan aplikasinya ditulis dengan React Native dan Expo.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kalau proyeknya belum memakai kode native tambahan, pasang",
                    "     Expo Go di iPhone pembimbing. Jalankan server pengembangan",
                    "     di laptop, lalu pindai kode QR yang muncul:",
                    "       npx expo start",
                    "  2. Kalau iPhone dan laptop beda jaringan Wi-Fi, pakai mode",
                    "     tunnel supaya keduanya tetap tersambung:",
                    "       npx expo start --tunnel",
                    "  3. Kalau aplikasinya butuh modul native atau harus terpasang",
                    "     permanen, siapkan akun Apple Developer, lalu minta build iOS",
                    "     dari cloud:",
                    "       eas build --platform ios",
                    "  4. Cek sisa kuota build bulan itu. Build gratis masuk antrean",
                    "     prioritas rendah, jadi jangan baru minta build sejam sebelum",
                    "     presentasi.",
                ],
            },
        ],
    },
    {
        "title": "3. UI Thread, Event, dan Siklus Hidup Layar",
        "sections": [
            {
                "body": [
                    "Aplikasi di HP kebanyakan waktunya dipakai untuk menunggu.",
                    "Menunggu jarimu menyentuh layar, menunggu data dari server,",
                    "menunggu berkas selesai dibaca. Tiap kali sesuatu terjadi,",
                    "misalnya layar disentuh atau data datang, itu disebut event.",
                    "",
                    "Semua event yang menyangkut tampilan diurus satu thread khusus.",
                    "Thread itu jalur kerja di dalam program; satu thread mengerjakan",
                    "satu hal pada satu waktu. Thread khusus ini namanya UI thread,",
                    "atau main thread. Cuma dia yang boleh mengubah tampilan, dan cuma",
                    "dia yang menggambar layar.",
                    "",
                    "Bayangkan warung dengan satu kasir. Pembeli antre, kasir melayani",
                    "satu per satu. Kalau satu pembeli minta dihitungkan belanjaan",
                    "sebulan di kasir, semua pembeli di belakangnya ikut berdiri",
                    "menunggu. UI thread juga begitu: event berbaris di antrean, dan",
                    "UI thread mengambilnya satu per satu. Putaran ambil event lalu",
                    "kerjakan ini disebut event loop.",
                ],
            },
            {
                "heading": "Enam belas milidetik",
                "body": [
                    "Layar HP biasa menggambar ulang 60 kali per detik. Artinya UI",
                    "thread punya waktu sekitar 16 milidetik untuk tiap gambar, yang",
                    "disebut frame. Layar 120 Hz cuma memberi sekitar 8 milidetik.",
                    "",
                    "Kalau sebuah event makan waktu lebih lama dari itu, frame",
                    "berikutnya telat digambar. Animasi jadi patah-patah dan daftar",
                    "terasa berat waktu digulir. Programmer menyebutnya jank.",
                    "",
                    "Program di bawah meniru antrean event di UI thread. Lama tiap",
                    "event sudah ditentukan, jadi hasilnya selalu sama.",
                ],
            },
            {
                "heading": "Simulasi antrean event",
                "code": """// Satuan waktu: milidetik. Lama tiap event ditentukan di sini.
const BATAS_FRAME = 16;
const antrean = [
  { nama: 'ketuk tombol', lama: 2 },
  { nama: 'gulir daftar', lama: 5 },
  { nama: 'baca berkas 2 MB', lama: 180 },
  { nama: 'ketuk tombol', lama: 2 },
];

let jam = 0;
for (const event of antrean) {
  const mulai = jam;
  jam += event.lama;
  const terlewat = Math.floor(event.lama / BATAS_FRAME);
  let baris = `${String(mulai).padStart(3)} ms  ${event.nama.padEnd(17)}`;
  baris += ` ${event.lama} ms`;
  if (terlewat > 0) baris += `  -> ${terlewat} frame terlewat`;
  console.log(baris);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "    0 ms  ketuk tombol      2 ms",
                    "    2 ms  gulir daftar      5 ms",
                    "    7 ms  baca berkas 2 MB  180 ms  -> 11 frame terlewat",
                    "  187 ms  ketuk tombol      2 ms",
                    "",
                    "Membaca berkas makan 180 milidetik, kira-kira 11 frame. Selama",
                    "itu layar nggak digambar ulang. Ketukan kedua sudah datang, tapi",
                    "baru dilayani di milidetik ke-187. Buat pengguna, tombolnya",
                    "terasa telat bereaksi hampir dua per sepuluh detik.",
                ],
            },
            {
                "heading": "Kalau UI thread diblokir terlalu lama",
                "body": [
                    "Android punya batas keras. Kalau aplikasi nggak menanggapi",
                    "sentuhan atau tombol dalam 5 detik, sistem menampilkan dialog",
                    "ANR (Application Not Responding) yang menawarkan pengguna untuk",
                    "menutup aplikasimu. Di browser, halaman yang JavaScript-nya",
                    "berputar terlalu lama juga membeku, lalu browser menawarkan untuk",
                    "menghentikannya.",
                    "",
                    "Solusinya sama di semua platform. Pekerjaan berat seperti membaca",
                    "berkas besar, memanggil server, atau mengolah gambar dipindah ke",
                    "luar UI thread. Kalau sudah selesai, hasilnya dikirim balik ke UI",
                    "thread untuk ditampilkan. Di Kotlin itu dikerjakan coroutine, di",
                    "JavaScript async dan await, di Dart Future dan isolate. Kamu akan",
                    "ketemu semuanya di bab-bab berikutnya.",
                ],
            },
            {
                "heading": "JavaScript menunjukkan aturannya",
                "code": """console.log('1. handler klik mulai');
setTimeout(() => console.log('4. tugas berikutnya di antrean'), 0);
Promise.resolve().then(() => console.log('3. lanjutan await'));
console.log('2. handler klik selesai');""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  1. handler klik mulai",
                    "  2. handler klik selesai",
                    "  3. lanjutan await",
                    "  4. tugas berikutnya di antrean",
                    "",
                    "Handler selalu dikerjakan sampai habis dulu. Lanjutan Promise,",
                    "yaitu kode sesudah await, baru jalan setelah itu. Tugas dari",
                    "setTimeout menunggu paling belakang walaupun jedanya 0. Jadi",
                    "kalau handler klik-mu berputar 3 detik, nggak ada apa pun yang",
                    "bisa menyela, termasuk menggambar layar.",
                ],
            },
            {
                "heading": "Siklus hidup layar",
                "body": [
                    "Ada satu hal lagi yang bikin aplikasi HP beda dari program",
                    "terminal. Sistem operasi yang memutuskan kapan layar aplikasimu",
                    "dibuat, tampil, disembunyikan, atau dihancurkan. Kamu menekan",
                    "Home, ada telepon masuk, HP diputar, atau memori hampir habis.",
                    "Aplikasi nggak bisa mencegahnya; dia cuma diberi tahu.",
                    "",
                    "Keadaan-keadaan itu disebut siklus hidup (lifecycle). Cara",
                    "paling gampang memahaminya adalah sebagai state machine, yaitu",
                    "daftar keadaan ditambah aturan pindahnya: dari keadaan ini,",
                    "kalau event itu datang, pindah ke keadaan sana dan jalankan",
                    "fungsi tertentu.",
                ],
            },
            {
                "heading": "Siklus hidup sebagai tabel",
                "bahasa": "teks",
                "code": """keadaan sekarang   event            keadaan baru   yang dipanggil
belum ada          buka aplikasi    aktif          dibuat, tampil, aktif
aktif              tekan Home       di belakang    jeda, berhenti
di belakang        kembali          aktif          tampil, aktif
di belakang        memori habis     dihancurkan    (proses dimatikan)""",
            },
            {
                "body": [
                    "Nama fungsinya beda di tiap platform. Android memakai onCreate",
                    "sampai onDestroy, iOS memakai viewDidLoad dan kawan-kawannya,",
                    "Flutter memakai initState dan dispose. Polanya sama. Versi",
                    "Android dibahas rinci di bab Android Pertama.",
                    "",
                    "Jebakan: menyimpan data penting cuma di variabel layar. Waktu",
                    "aplikasi ada di belakang, sistem boleh mematikan prosesnya untuk",
                    "membebaskan memori, tanpa memanggil fungsi penutup apa pun.",
                    "Isian formulir yang belum disimpan ikut hilang.",
                    "",
                    "Jebakan: mengira pekerjaan yang cuma sebentar aman di UI thread.",
                    "Membaca berkas 2 MB memang cepat di laptopmu, tapi HP murah",
                    "dengan penyimpanan lambat bisa butuh jauh lebih lama.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Play Console punya halaman Android vitals yang mencatat seberapa sering",
                    "aplikasi macet dari HP pengguna sungguhan, dan Google Play memakai",
                    "angka itu untuk menilai kualitas aplikasi. Di sisi kode, Android",
                    "punya StrictMode, yang bisa diatur supaya memprotes setiap kali",
                    "UI thread membaca disk atau memanggil jaringan.",
                    "",
                    "Kasus kecil: aplikasi catatanmu punya tombol Ekspor yang menulis",
                    "5.000 catatan ke satu berkas. Begitu tombol diketuk, layar",
                    "membeku beberapa detik, dan di HP lama sesekali muncul dialog",
                    "aplikasi tidak merespons.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan dulu penyebabnya. Ekspor dijalankan langsung di",
                    "     handler tombol, berarti di UI thread.",
                    "  2. Pindahkan penulisan berkas ke luar UI thread. Di Kotlin",
                    "     bentuknya kira-kira begini:",
                    "       scope.launch {",
                    "           withContext(Dispatchers.IO) { tulisBerkas(catatan) }",
                    "           tampilkanPesan(\"Ekspor selesai\")",
                    "       }",
                    "  3. Selama menunggu, tampilkan indikator proses dan matikan",
                    "     tombolnya, supaya pengguna nggak mengetuk dua kali.",
                    "  4. Uji di emulator berprofil HP kelas bawah, karena laptopmu",
                    "     jauh lebih cepat dari HP kebanyakan penggunamu.",
                ],
            },
        ],
    },
    {
        "title": "4. Platform Android, API Level, dan Struktur Proyek",
        "sections": [
            {
                "body": [
                    "Android adalah sistem operasi buatan Google yang berdiri di atas",
                    "kernel Linux. Kode dasarnya terbuka dengan nama AOSP (Android",
                    "Open Source Project) berlisensi Apache-2.0. Pabrik HP mengambil",
                    "kode itu, menambahkan aplikasi dan tampilannya sendiri, lalu",
                    "memasangnya di HP yang mereka jual.",
                    "",
                    "Tiap versi Android membawa kemampuan baru yang bisa dipanggil",
                    "aplikasi, misalnya izin notifikasi atau cara baru menampilkan",
                    "layar penuh. Kumpulan fungsi yang boleh dipanggil aplikasi itu",
                    "disebut API. Supaya gampang dibandingkan, tiap versi diberi",
                    "nomor urut yang disebut API level. Android 17, yang dirilis",
                    "stabil Juni 2026, punya API level 37.",
                    "",
                    "Sejak Android 16, Google merilis SDK besar tiap kuartal kedua dan",
                    "rilis kecil tiap kuartal keempat. Jadi angka API level naik sekitar",
                    "setahun sekali, dan aturan Play Store ikut naik di belakangnya.",
                ],
            },
            {
                "heading": "Versi Android dan API level",
                "body": [
                    "Programmer lebih sering menyebut API level daripada nama versi,",
                    "karena angka itulah yang ditulis di berkas build. Tabel di bawah",
                    "menunjukkan pasangan versi dan API level beberapa tahun terakhir,",
                    "plus satu perubahan yang terasa di tiap versi. Sebagian perubahan",
                    "itu baru berlaku kalau aplikasimu menyatakan siap untuk versi",
                    "tersebut, lewat targetSdk yang dibahas sebentar lagi.",
                ],
            },
            {
                "heading": "minSdk, targetSdk, dan compileSdk",
                "bahasa": "gradle",
                "code": """// app/build.gradle.kts (sebagian)
android {
    namespace = "id.belajar.catatan"
    compileSdk = 37

    defaultConfig {
        applicationId = "id.belajar.catatan"
        minSdk = 26
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"
    }
}""",
            },
            {
                "body": [
                    "Tiga angka di situ sering tertukar, padahal artinya beda:",
                    "  - compileSdk adalah API level yang dipakai waktu kode",
                    "    dikompilasi. Fungsi yang baru ada di Android 17 cuma bisa",
                    "    dipanggil kalau compileSdk-nya 37.",
                    "  - minSdk adalah versi Android paling rendah yang boleh memasang",
                    "    aplikasimu. HP dengan versi di bawahnya nggak akan melihat",
                    "    aplikasimu di Play Store.",
                    "  - targetSdk adalah versi yang perilakunya sudah kamu uji.",
                    "    Android menyalakan perubahan perilaku baru sesuai angka ini.",
                    "    Sejak 31 Agustus 2026, aplikasi baru dan update di Play Store",
                    "    wajib memakai targetSdk minimal 36.",
                    "",
                    "Waktu membuat proyek baru, Android Studio menampilkan perkiraan",
                    "persentase perangkat yang bisa memasang aplikasimu untuk tiap",
                    "pilihan minSdk. Makin rendah minSdk, makin banyak HP yang",
                    "terjangkau, tapi makin banyak juga versi lama yang harus diuji.",
                    "",
                    "Dua baris terakhir juga penting. versionCode adalah angka bulat",
                    "yang wajib naik setiap kali kamu mengunggah versi baru ke Play",
                    "Store. versionName cuma teks untuk dibaca manusia, misalnya 1.0",
                    "atau 2.3.1. applicationId adalah nama unik aplikasimu di Play",
                    "Store, dan nggak boleh diganti setelah rilis.",
                ],
            },
            {
                "heading": "Siapa yang bisa memasang? (Kotlin)",
                "bahasa": "kotlin",
                "code": """data class Perangkat(val nama: String, val api: Int)

fun main() {
    val minSdk = 26
    val perangkat = listOf(
        Perangkat("HP lama kakak", 23),
        Perangkat("HP ibu", 29),
        Perangkat("HP sendiri", 35),
        Perangkat("Tablet sekolah", 37),
    )
    for (p in perangkat) {
        val status = if (p.api >= minSdk) "bisa pasang" else "nggak muncul di Play Store"
        println("${p.nama.padEnd(15)} API ${p.api}  $status")
    }
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  HP lama kakak   API 23  nggak muncul di Play Store",
                    "  HP ibu          API 29  bisa pasang",
                    "  HP sendiri      API 35  bisa pasang",
                    "  Tablet sekolah  API 37  bisa pasang",
                    "",
                    "Program kecil ini ditulis dengan Kotlin biasa, jadi bisa kamu",
                    "jalankan di aplikasi ini. Kotlin adalah bahasa utama Android:",
                    "Google menyebutnya bahasa resmi sejak 2017 dan mengumumkan",
                    "pendekatan Kotlin-first sejak 2019. Jetpack Compose cuma bisa",
                    "ditulis dengan Kotlin. Java masih didukung dan banyak ditemui di",
                    "kode lama, tapi materi resmi Google sekarang memakai Kotlin.",
                    "Versi Kotlin terbaru saat materi ini ditulis adalah 2.4.21.",
                    "Kurikulum ini nggak mengajar ulang sintaksnya; kalau ada yang",
                    "asing, buka lagi kurikulum Kotlin.",
                ],
            },
            {
                "heading": "Struktur proyek",
                "bahasa": "teks",
                "code": """Catatanku/
├── settings.gradle.kts        daftar modul di proyek ini
├── build.gradle.kts           pengaturan tingkat proyek
├── gradle/
│   ├── libs.versions.toml     daftar versi pustaka (version catalog)
│   └── wrapper/               versi Gradle yang dikunci proyek
├── gradlew                    skrip untuk menjalankan Gradle
└── app/
    ├── build.gradle.kts       pengaturan modul aplikasi
    └── src/
        ├── main/
        │   ├── AndroidManifest.xml
        │   ├── java/id/belajar/catatan/MainActivity.kt
        │   └── res/           gambar, teks, warna, ikon
        ├── test/              uji unit, jalan di laptop
        └── androidTest/       uji instrumentasi, jalan di HP""",
            },
            {
                "body": [
                    "Berkas Kotlin tinggal di app/src/main. Nama foldernya sering",
                    "masih java walaupun isinya berkas .kt, karena begitulah bawaan",
                    "proyek Android sejak lama; folder kotlin juga diterima. Folder res",
                    "berisi semua yang bukan kode: gambar di drawable, ikon di mipmap,",
                    "dan teks di values/strings.xml. Teks sengaja dipisah dari kode",
                    "supaya aplikasinya gampang diterjemahkan.",
                    "",
                    "Satu berkas lagi wajib ada di tiap aplikasi: AndroidManifest.xml.",
                    "Isinya memberi tahu sistem nama aplikasi, ikonnya, izin yang",
                    "diminta, dan komponen apa saja yang ada di dalamnya.",
                ],
            },
            {
                "heading": "AndroidManifest.xml",
                "bahasa": "xml",
                "code": """<manifest xmlns:android="http://schemas.android.com/apk/res/android">

    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:label="@string/app_name"
        android:icon="@mipmap/ic_launcher"
        android:theme="@style/Theme.Catatanku">

        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>""",
            },
            {
                "body": [
                    "Activity adalah satu layar atau jendela aplikasi. Aplikasi Compose",
                    "modern biasanya cuma punya satu Activity, dan perpindahan layar",
                    "diurus di dalamnya. Intent filter berisi action main dan category",
                    "launcher di manifest tadi membuat ikon aplikasimu muncul di daftar",
                    "aplikasi HP.",
                    "Sejak Android 12, komponen yang punya intent filter wajib menulis",
                    "android:exported secara jelas, true atau false. Kalau lupa,",
                    "build-nya gagal.",
                    "",
                    "Ada tiga jenis komponen lain yang juga didaftarkan di manifest.",
                    "Service dipakai untuk pekerjaan di belakang layar.",
                    "BroadcastReceiver menanggapi kabar dari sistem, misalnya baterai",
                    "lemah. ContentProvider membagi data ke aplikasi lain.",
                    "",
                    "Jebakan: mengganti applicationId setelah aplikasinya rilis. Play",
                    "Store menganggapnya aplikasi yang sama sekali baru, jadi pengguna",
                    "lama nggak dapat update.",
                    "",
                    "Jebakan: lupa menaikkan versionCode. Play Console menolak unggahan",
                    "yang versionCode-nya sudah pernah dipakai.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Setiap tahun, tim Android di perusahaan mana pun mengerjakan",
                    "pekerjaan yang sama: menaikkan targetSdk supaya aplikasinya tetap",
                    "boleh di-update di Play Store. Halaman Behavior changes di",
                    "developer.android.com mendaftar apa saja yang berubah untuk tiap",
                    "API level, dan halaman itulah yang mereka baca sebelum menaikkan",
                    "angkanya.",
                    "",
                    "Kasus kecil: di tempat PKL kamu diberi aplikasi lama dengan",
                    "minSdk 21 dan targetSdk 33. Pembimbing minta aplikasinya bisa",
                    "di-update lagi di Play Store.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek aturan Play sekarang: update wajib targetSdk minimal 36.",
                    "     Berarti ada tiga lompatan: 34, 35, dan 36.",
                    "  2. Baca halaman Behavior changes untuk tiap API level itu.",
                    "     Contohnya, targetSdk 34 mewajibkan jenis foreground service",
                    "     ditulis, dan targetSdk 35 membuat tampilan edge-to-edge",
                    "     jadi wajib.",
                    "  3. Ubah angkanya di app/build.gradle.kts, lalu naikkan juga",
                    "     compileSdk supaya fungsi barunya bisa dipanggil:",
                    "       compileSdk = 37",
                    "       targetSdk = 36",
                    "  4. Uji di emulator Android 15 dan 16, terutama layar yang",
                    "     tertutup bilah status setelah edge-to-edge berlaku.",
                    "  5. Naikkan versionCode, lalu unggah ke jalur uji dulu sebelum",
                    "     ke produksi.",
                ],
            },
        ],
    },
    {
        "title": "5. Android Studio dan Emulator di Fedora",
        "sections": [
            {
                "body": [
                    "Android Studio adalah IDE resmi untuk Android, dibangun di atas",
                    "IntelliJ buatan JetBrains. Di dalamnya ada editor kode, pratinjau",
                    "Compose, emulator, Logcat untuk membaca log aplikasi, dan",
                    "profiler untuk mengukur memori dan CPU. Semuanya gratis.",
                    "",
                    "Versi stabil terbaru saat materi ini ditulis adalah Android Studio",
                    "Rabbit 1 (2026.2.1), dirilis 1 Oktober 2026. Rilisnya diberi nama",
                    "hewan berurutan abjad: Narwhal, Otter, Panda, Quail, lalu Rabbit.",
                    "Android Studio jalan di Fedora tanpa masalah, asal laptopmu",
                    "memenuhi syaratnya.",
                ],
            },
            {
                "heading": "Cek dulu laptopmu",
                "body": [
                    "Syarat resmi untuk Linux, dari halaman pemasangan Android Studio:",
                    "  - Linux 64-bit yang mendukung GNOME, KDE, atau Unity, dengan",
                    "    glibc 2.31 atau lebih baru. Fedora versi sekarang lolos.",
                    "  - RAM 8 GB kalau cuma Android Studio, 16 GB kalau ditambah",
                    "    emulator. Yang disarankan 32 GB.",
                    "  - Ruang kosong 8 GB untuk Android Studio, 16 GB kalau ditambah",
                    "    emulator. Yang disarankan SSD dengan ruang 32 GB.",
                    "  - Prosesor x86_64 dengan fitur virtualisasi Intel atau AMD yang",
                    "    menyala di BIOS. Laptop Linux berprosesor ARM",
                    "    belum didukung.",
                    "",
                    "Perintah di bawah membantu kamu ngecek semuanya dari terminal.",
                ],
            },
            {
                "heading": "Perintah pengecekan",
                "bahasa": "terminal",
                "code": """free -h                                 # total RAM
df -h ~                                 # ruang kosong di folder rumah
grep -c -E 'vmx|svm' /proc/cpuinfo      # lebih dari 0: CPU punya virtualisasi
lsmod | grep kvm                        # modul kvm_intel atau kvm_amd termuat
ls -l /dev/kvm                          # izin perangkat KVM""",
            },
            {
                "heading": "Memasang di Fedora",
                "bahasa": "terminal",
                "code": """# 1. pustaka 32-bit yang diminta dokumentasi resmi untuk Fedora
sudo dnf install zlib.i686 ncurses-libs.i686 bzip2-libs.i686

# 2. ekstrak arsip dari developer.android.com/studio ke /opt
sudo tar -xzf ~/Unduhan/android-studio-rabbit1-linux.tar.gz -C /opt

# 3. jalankan
/opt/android-studio/bin/studio""",
            },
            {
                "body": [
                    "Dokumentasi resminya masih menulis yum untuk Fedora; di Fedora",
                    "sekarang perintahnya dnf. Folder unduhanmu bisa bernama Unduhan",
                    "atau Downloads, tergantung bahasa sistemmu. Kalau Android Studio",
                    "cuma dipakai akunmu sendiri, dokumentasi juga menyarankan",
                    "/usr/local sebagai tempat ekstrak.",
                    "",
                    "Pertama kali dijalankan, Setup Wizard mengunduh Android SDK ke",
                    "~/Android/Sdk. Ukurannya beberapa GB, jadi pakai koneksi yang",
                    "stabil. Sesudah itu pilih Tools > Create Desktop Entry supaya",
                    "Android Studio muncul di daftar aplikasi GNOME.",
                ],
            },
            {
                "heading": "Kenapa emulator butuh KVM",
                "body": [
                    "Emulator Android menjalankan sistem Android lengkap sebagai mesin",
                    "virtual di laptopmu. Tanpa bantuan hardware, CPU laptop harus",
                    "meniru setiap instruksi satu per satu, dan Android jadi lambat",
                    "sekali sampai nggak bisa dipakai. KVM (Kernel-based Virtual",
                    "Machine) adalah fitur kernel Linux yang membiarkan mesin virtual",
                    "memakai fitur virtualisasi CPU secara langsung. Dengan KVM dan",
                    "system image x86_64, emulator jalan hampir secepat HP sungguhan.",
                    "",
                    "Emulator punya perintah untuk ngecek apakah KVM bisa dipakai:",
                ],
            },
            {
                "heading": "Cek KVM",
                "bahasa": "terminal",
                "code": """~/Android/Sdk/emulator/emulator -accel-check
# keluarannya kira-kira:
# accel:
# 0
# KVM (version 12) is installed and usable.

ls -l /dev/kvm
# crw-rw-rw-. 1 root kvm 10, 232 ...   <- semua pengguna boleh memakai

# hanya kalau izinnya crw-rw---- dan akunmu belum anggota grup kvm:
sudo usermod -aG kvm $USER""",
            },
            {
                "body": [
                    "Di Fedora versi baru, /dev/kvm biasanya sudah boleh dipakai semua",
                    "pengguna, jadi kamu nggak perlu berbuat apa-apa. Kalau izinnya",
                    "cuma untuk grup kvm dan akunmu bukan anggotanya, jalankan",
                    "usermod di atas, lalu keluar dan masuk lagi dari sesi desktop",
                    "supaya keanggotaan grupnya berlaku. Kalau grep tadi menghasilkan",
                    "0, fitur virtualisasinya mati di BIOS; nyalakan dari menu",
                    "pengaturan BIOS laptop.",
                ],
            },
            {
                "heading": "Membuat emulator",
                "body": [
                    "Emulator di Android Studio disebut AVD (Android Virtual Device).",
                    "Langkahnya:",
                    "  1. Buka Device Manager, lalu Create Virtual Device.",
                    "  2. Pilih profil HP, misalnya salah satu seri Pixel.",
                    "  3. Pilih system image x86_64. Image berlabel Google Play",
                    "     membawa Play Store, cocok untuk mencoba alur login Google.",
                    "  4. Atur RAM emulator. Di laptop 8 GB, 2 GB untuk emulator sudah",
                    "     cukup untuk belajar.",
                    "",
                    "Laptopmu cuma punya RAM 8 GB? Pakai HP sungguhan. Ketuk Build",
                    "number tujuh kali di Settings > About phone sampai Developer",
                    "options terbuka. Di situ nyalakan USB debugging, atau Wireless",
                    "debugging untuk Android 11 ke atas, supaya HP tersambung tanpa",
                    "kabel. HP yang tersambung muncul di daftar perangkat Android",
                    "Studio dan di perintah adb devices.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di kantor pun banyak developer Android yang lebih sering menguji",
                    "di HP sungguhan daripada emulator, terutama untuk kamera, sensor,",
                    "dan performa. Emulator dipakai untuk mencoba banyak ukuran layar",
                    "dan versi Android tanpa harus membeli HP satu per satu.",
                    "",
                    "Kasus kecil: laptopmu ber-RAM 8 GB. Begitu emulator dinyalakan",
                    "bersama Android Studio dan browser, laptop macet dan kipasnya",
                    "berbunyi keras.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek dulu angkanya. RAM 8 GB memang batas minimum untuk",
                    "     Android Studio saja, tanpa emulator.",
                    "       free -h",
                    "  2. Tutup browser dan aplikasi berat lain selama build.",
                    "  3. Kecilkan RAM emulator di Device Manager, atau matikan",
                    "     emulator sama sekali dan pakai HP sungguhan lewat Wireless",
                    "     debugging.",
                    "  4. Pastikan emulator memakai KVM. Tanpa KVM, emulator memakan",
                    "     CPU jauh lebih banyak:",
                    "       ~/Android/Sdk/emulator/emulator -accel-check",
                ],
            },
        ],
    },
    {
        "title": "6. Gradle dan Android Gradle Plugin",
        "sections": [
            {
                "body": [
                    "Kode Kotlin di proyekmu belum bisa dipasang di HP. Ia harus",
                    "dikompilasi, digabung dengan gambar dan teks dari folder res,",
                    "dikecilkan, ditandatangani, lalu dibungkus jadi APK untuk dipasang",
                    "atau AAB untuk diunggah ke Play Store. Rangkaian langkah itu",
                    "disebut build.",
                    "",
                    "Gradle adalah sistem build yang mengatur semua langkah itu. Gradle",
                    "juga dipakai di proyek Kotlin, Java, dan Spring Boot. Versi",
                    "terbarunya 9.8.1, dirilis 7 Oktober 2026.",
                    "",
                    "Gradle sendiri nggak tahu apa-apa soal Android. Yang mengajarinya",
                    "adalah Android Gradle Plugin (AGP) buatan Google: cara memproses",
                    "manifest dan resource, cara membuat varian build, dan cara",
                    "menandatangani aplikasi. Versi terbaru Android Gradle Plugin",
                    "adalah 9.4.0 (September 2026), dan versi itu butuh Gradle minimal",
                    "9.6.0 serta JDK 17.",
                ],
            },
            {
                "heading": "Semua pekerjaan adalah tugas",
                "body": [
                    "Gradle membagi build jadi tugas (task). Tiap tugas bisa",
                    "bergantung pada tugas lain: merakit APK butuh kode yang sudah",
                    "dikompilasi, dan kompilasi butuh berkas konfigurasi yang sudah",
                    "dibuat. Gradle menyusun semua ketergantungan itu jadi graf, lalu",
                    "menjalankan tugas dalam urutan yang benar.",
                    "",
                    "Gradle juga melewati tugas yang masukannya nggak berubah sejak",
                    "build terakhir. Makanya build kedua jauh lebih cepat dari",
                    "build pertama. Tiruan di bawah menunjukkan idenya.",
                ],
            },
            {
                "heading": "Tiruan pemeriksaan tugas yang sudah mutakhir",
                "code": """// Tugas dilewati kalau masukannya sama dengan saat terakhir dijalankan.
const terakhir = {};

function jalankan(tugas, masukan) {
  const sidik = JSON.stringify(masukan);
  if (terakhir[tugas] === sidik) {
    console.log(`> Task :app:${tugas} UP-TO-DATE`);
    return;
  }
  terakhir[tugas] = sidik;
  console.log(`> Task :app:${tugas}`);
}

console.log('build pertama');
jalankan('compileDebugKotlin', ['MainActivity.kt v1']);
jalankan('mergeDebugResources', ['strings.xml v1']);
console.log('build kedua, cuma MainActivity.kt yang berubah');
jalankan('compileDebugKotlin', ['MainActivity.kt v2']);
jalankan('mergeDebugResources', ['strings.xml v1']);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  build pertama",
                    "  > Task :app:compileDebugKotlin",
                    "  > Task :app:mergeDebugResources",
                    "  build kedua, cuma MainActivity.kt yang berubah",
                    "  > Task :app:compileDebugKotlin",
                    "  > Task :app:mergeDebugResources UP-TO-DATE",
                    "",
                    "Gradle sungguhan menyimpan sidik dari berkas masukan dan keluaran",
                    "tiap tugas. Format lognya juga mirip, jadi waktu kamu menjalankan",
                    "build di terminal, kamu akan melihat baris-baris seperti ini.",
                    "Tugas yang ditandai begitu nggak dikerjakan ulang.",
                ],
            },
            {
                "heading": "Menjalankan tugas",
                "bahasa": "terminal",
                "code": """./gradlew tasks            # daftar tugas yang tersedia
./gradlew assembleDebug    # APK debug di app/build/outputs/apk/debug/
./gradlew test             # uji unit
./gradlew bundleRelease    # AAB untuk Play Store""",
            },
            {
                "body": [
                    "gradlew adalah Gradle wrapper, skrip kecil yang ikut disimpan di",
                    "proyek. Ia mengunduh versi Gradle yang tertulis di",
                    "gradle/wrapper/gradle-wrapper.properties, jadi semua orang di tim",
                    "memakai versi yang sama tanpa memasang Gradle sendiri. Tombol Run",
                    "di Android Studio juga menjalankan tugas-tugas ini di belakang",
                    "layar.",
                ],
            },
            {
                "heading": "Berkas build dengan Kotlin DSL",
                "bahasa": "gradle",
                "code": """// app/build.gradle.kts
plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.compose)
}

android {
    namespace = "id.belajar.catatan"
    compileSdk = 37

    defaultConfig {
        applicationId = "id.belajar.catatan"
        minSdk = 26
        targetSdk = 36
        versionCode = 1
        versionName = "1.0"
    }

    buildTypes {
        release {
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }

    flavorDimensions += "paket"
    productFlavors {
        create("gratis") { dimension = "paket" }
        create("berbayar") { dimension = "paket" }
    }
}

dependencies {
    implementation(libs.androidx.activity.compose)
    implementation(libs.androidx.compose.material3)
    testImplementation(libs.junit)
}""",
            },
            {
                "body": [
                    "Akhiran .kts artinya berkas ini ditulis dengan Kotlin DSL, yaitu",
                    "Kotlin yang dipakai sebagai bahasa konfigurasi. Kotlin DSL jadi",
                    "bawaan proyek Android baru. Proyek lama sering masih memakai",
                    "build.gradle tanpa .kts, yang ditulis dengan Groovy.",
                    "",
                    "Perhatikan bagian plugins. Sejak versi 9.0, dukungan Kotlin sudah",
                    "dibawa Android Gradle Plugin sendiri, jadi proyek baru nggak",
                    "perlu lagi plugin org.jetbrains.kotlin.android yang ada di",
                    "tutorial lama. Plugin kotlin.compose tetap dipasang karena ia yang",
                    "menyalakan compiler Compose.",
                    "",
                    "buildTypes dan productFlavors bergabung jadi varian build. Dua",
                    "build type (debug, release) kali dua flavor (gratis, berbayar)",
                    "menghasilkan empat varian: gratisDebug, gratisRelease,",
                    "berbayarDebug, dan berbayarRelease. Tiap varian punya tugasnya",
                    "sendiri, misalnya assembleGratisDebug.",
                ],
            },
            {
                "heading": "Version catalog",
                "bahasa": "toml",
                "code": """# gradle/libs.versions.toml
[versions]
agp = "9.4.0"
kotlin = "2.4.21"
activityCompose = "1.13.0"
material3 = "1.4.0"
junit = "4.13.2"

[libraries]
androidx-activity-compose = { group = "androidx.activity", name = "activity-compose", version.ref = "activityCompose" }
androidx-compose-material3 = { group = "androidx.compose.material3", name = "material3", version.ref = "material3" }
junit = { group = "junit", name = "junit", version.ref = "junit" }

[plugins]
android-application = { id = "com.android.application", version.ref = "agp" }
kotlin-compose = { id = "org.jetbrains.kotlin.plugin.compose", version.ref = "kotlin" }""",
            },
            {
                "body": [
                    "Version catalog menyimpan semua nomor versi di satu berkas.",
                    "Tanda hubung di nama berubah jadi titik waktu dipakai, jadi",
                    "androidx-activity-compose dipanggil sebagai",
                    "libs.androidx.activity.compose. Waktu ada versi baru, kamu cukup",
                    "mengubah satu baris di [versions].",
                    "",
                    "Gradle juga jadi tempat memasang alat pemeriksa kode. Detekt",
                    "mencari pola kode Kotlin yang rawan bug, dan ktlint merapikan",
                    "gaya penulisan. Keduanya dijalankan sebagai tugas Gradle, jadi",
                    "bisa ikut dijalankan otomatis di server CI.",
                ],
            },
            {
                "heading": "Error versi yang nggak cocok",
                "body": [
                    "Error paling sering dialami pemula yang membuka proyek orang",
                    "lain berbunyi kira-kira begini:",
                    "  Minimum supported Gradle version is 9.6.0. Current version is 9.2.1.",
                    "",
                    "Artinya proyek itu memakai Android Gradle Plugin yang butuh",
                    "Gradle lebih baru daripada yang dikunci wrapper-nya. Ada dua",
                    "jalan keluar:",
                    "  - Ubah distributionUrl di gradle-wrapper.properties ke versi",
                    "    Gradle yang diminta atau yang lebih baru.",
                    "  - Pakai menu Tools > AGP Upgrade Assistant di Android Studio.",
                    "    Alat itu menaikkan versi plugin dan Gradle bersamaan sambil",
                    "    menunjukkan apa yang berubah.",
                    "",
                    "Jebakan: build pertama selalu lambat karena Gradle mengunduh",
                    "dirinya sendiri dan semua pustaka ke ~/.gradle. Jangan panik dan",
                    "jangan menghapus folder itu tiap kali build gagal; isinya cache",
                    "yang membuat build berikutnya cepat.",
                    "",
                    "Jebakan: menyimpan local.properties ke Git. Berkas itu berisi",
                    "lokasi SDK di laptopmu sendiri, misalnya sdk.dir, dan akan salah",
                    "di laptop orang lain.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek contoh resmi Google di GitHub, misalnya Now in Android,",
                    "memakai Gradle Kotlin DSL dan version catalog persis seperti di",
                    "atas. Server CI di perusahaan juga menjalankan ./gradlew yang",
                    "sama dengan laptop developernya, jadi hasil build di keduanya",
                    "bisa dibandingkan.",
                    "",
                    "Kasus kecil: kamu mengkloning proyek Android dari GitHub yang",
                    "terakhir diubah dua tahun lalu. Begitu dibuka di Android Studio",
                    "Rabbit, sinkronisasi Gradle gagal dengan pesan versi yang nggak",
                    "cocok.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca baris pertama pesan errornya, bukan baris terakhir.",
                    "     Biasanya di situ tertulis versi minimum yang diminta.",
                    "  2. Cek versi Gradle proyek:",
                    "       grep distributionUrl gradle/wrapper/gradle-wrapper.properties",
                    "  3. Jalankan Upgrade Assistant tadi supaya plugin dan Gradle",
                    "     naik bersama, lalu baca daftar perubahan yang ditawarkannya.",
                    "  4. Kalau masih ada plugin org.jetbrains.kotlin.android di",
                    "     berkas build, ikuti panduan migrasi built-in Kotlin di",
                    "     dokumentasi Android.",
                    "  5. Jalankan ./gradlew assembleDebug dari terminal. Sinkronisasi",
                    "     yang berhasil belum menjamin build-nya lolos sampai akhir.",
                ],
            },
        ],
    },
    {
        "title": "7. Siklus Hidup Activity dan Perubahan Konfigurasi",
        "sections": [
            {
                "body": [
                    "Di materi UI Thread kamu sudah kenal ide siklus hidup: sistem",
                    "operasi yang memutuskan kapan layar dibuat dan dihancurkan.",
                    "Di Android, layar itu adalah Activity, dan sistem memberi tahu",
                    "Activity lewat fungsi-fungsi yang disebut callback. Kamu nggak",
                    "pernah memanggil callback itu sendiri. Sistem yang memanggilnya,",
                    "dan tugasmu mengisi apa yang harus terjadi di tiap callback.",
                ],
            },
            {
                "heading": "Callback utama",
                "body": [
                    "Tujuh callback yang paling sering kamu temui:",
                    "  - onCreate: objek Activity baru saja dibuat. Di sini tampilan",
                    "    dipasang dengan setContent. Dipanggil sekali per objek.",
                    "  - onStart: Activity mulai terlihat.",
                    "  - onResume: Activity ada di depan dan bisa disentuh.",
                    "  - onPause: Activity kehilangan fokus, misalnya tertutup dialog",
                    "    izin atau dibagi layar dengan aplikasi lain.",
                    "  - onStop: Activity nggak terlihat lagi.",
                    "  - onRestart: Activity yang tadinya berhenti akan tampil lagi.",
                    "    Sesudahnya selalu onStart.",
                    "  - onDestroy: objek Activity akan dibuang.",
                ],
            },
            {
                "heading": "Urutan untuk kejadian sehari-hari",
                "bahasa": "teks",
                "code": """kejadian               callback yang dipanggil
buka aplikasi          onCreate, onStart, onResume
tekan Home             onPause, onStop
kembali ke aplikasi    onRestart, onStart, onResume
putar layar            onPause, onStop, onDestroy,
                       lalu onCreate, onStart, onResume (objek baru)
aplikasi ditutup       onPause, onStop, onDestroy""",
            },
            {
                "body": [
                    "Baris aplikasi ditutup berlaku waktu Activity diselesaikan sampai",
                    "tuntas, misalnya kode memanggil finish() atau pengguna",
                    "mengusapnya dari daftar aplikasi terbaru. Tombol Back nggak",
                    "selalu begitu. Sejak Android 12, menekan Back di Activity",
                    "pertama aplikasi cuma memindahkannya ke belakang, sama seperti",
                    "tombol Home, jadi yang terpanggil cuma onPause dan onStop.",
                    "",
                    "Mau melihat urutannya sendiri? Tulis log di tiap callback, lalu",
                    "saring tag Siklus di jendela Logcat Android Studio.",
                ],
            },
            {
                "heading": "Menulis log di tiap callback",
                "bahasa": "kotlin",
                "code": """class MainActivity : ComponentActivity() {
    private var hitung = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        Log.d("Siklus", "onCreate, hitung = $hitung")
        setContent { LayarPenghitung() }
    }

    override fun onStart() { super.onStart(); Log.d("Siklus", "onStart") }
    override fun onResume() { super.onResume(); Log.d("Siklus", "onResume") }
    override fun onPause() { super.onPause(); Log.d("Siklus", "onPause") }
    override fun onStop() { super.onStop(); Log.d("Siklus", "onStop") }
    override fun onDestroy() { super.onDestroy(); Log.d("Siklus", "onDestroy") }
}""",
            },
            {
                "heading": "Kenapa state hilang saat layar diputar",
                "body": [
                    "Memutar layar termasuk perubahan konfigurasi. Konfigurasi adalah",
                    "keadaan perangkat yang memengaruhi tampilan: arah layar, bahasa,",
                    "mode gelap, ukuran huruf, dan ukuran jendela. Waktu konfigurasi",
                    "berubah, bawaan Android adalah menghancurkan Activity lalu",
                    "membuatnya ulang, supaya tata letak dan teks bisa dimuat ulang",
                    "sesuai konfigurasi baru.",
                    "",
                    "Masalahnya, Activity yang baru adalah objek baru. Variabel hitung",
                    "di objek lama ikut dibuang, dan objek baru mulai lagi dari 0.",
                    "Tiruan di bawah ditulis dengan Kotlin biasa, tanpa Android, jadi",
                    "bisa kamu jalankan.",
                ],
            },
            {
                "heading": "Tiruan layar yang dibuat ulang",
                "bahasa": "kotlin",
                "code": """class LayarTiruan(simpanan: Map<String, Int>?) {
    var hitung = simpanan?.get("hitung") ?: 0
    fun simpanState(): Map<String, Int> = mapOf("hitung" to hitung)
}

fun main() {
    var layar = LayarTiruan(null)
    layar.hitung += 3
    println("sebelum diputar: ${layar.hitung}")

    layar = LayarTiruan(null)          // dibuat ulang tanpa menyimpan apa pun
    println("diputar, tanpa simpan: ${layar.hitung}")

    layar.hitung += 3
    val bundle = layar.simpanState()   // mirip onSaveInstanceState
    layar = LayarTiruan(bundle)        // onCreate menerima simpanannya
    println("diputar, dengan simpan: ${layar.hitung}")
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  sebelum diputar: 3",
                    "  diputar, tanpa simpan: 0",
                    "  diputar, dengan simpan: 3",
                    "",
                    "Android punya tiga cara supaya data selamat, dan masing-masing",
                    "cocok untuk data yang berbeda:",
                    "  - ViewModel menyimpan data layar selama layar itu belum ditutup",
                    "    sepenuhnya, termasuk saat diputar. Ini yang paling sering",
                    "    dipakai, dan dibahas di bab Arsitektur Aplikasi Android.",
                    "  - rememberSaveable di Compose, atau onSaveInstanceState di kode",
                    "    lama, menyimpan data kecil ke Bundle. Bundle selamat dari",
                    "    putar layar dan juga dari proses yang dimatikan sistem.",
                    "  - Database atau DataStore untuk data yang harus tetap ada",
                    "    walaupun aplikasinya ditutup.",
                    "",
                    "Mengunci layar di posisi tegak juga nggak menolong. Untuk",
                    "aplikasi yang menargetkan API 37, pembatasan arah dan ukuran",
                    "layar diabaikan di layar besar (lebar minimal 600dp). Jadi di",
                    "tablet dan HP lipat, aplikasimu tetap bisa diputar dan diubah",
                    "ukurannya.",
                ],
            },
            {
                "heading": "Jebakan pemula",
                "body": [
                    "Jebakan: mengira onDestroy pasti dipanggil. Kalau sistem",
                    "mematikan proses aplikasi yang sedang di belakang, nggak ada",
                    "callback apa pun yang jalan. Simpan data penting begitu pengguna",
                    "mengubahnya, jangan menunggu onDestroy.",
                    "",
                    "Jebakan: mengerjakan hal berat di onCreate. Selama onCreate belum",
                    "selesai, layar belum bisa digambar, dan pengguna menatap layar",
                    "kosong. Muat data di luar UI thread, lalu tampilkan hasilnya",
                    "begitu siap.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Developer Android memakai opsi Don't keep activities di",
                    "Developer options untuk menguji keadaan ini. Kalau opsi itu",
                    "menyala, setiap Activity yang ditinggalkan langsung dihancurkan,",
                    "jadi data yang nggak disimpan dengan benar langsung ketahuan",
                    "hilang.",
                    "",
                    "Kasus kecil: aplikasi kuis buatanmu menghitung skor di variabel",
                    "Activity. Temanmu memutar HP di tengah kuis, dan skornya kembali",
                    "jadi 0.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ulangi kejadiannya di emulator dengan tombol putar di",
                    "     panel samping emulator.",
                    "  2. Lihat Logcat dengan saringan tag Siklus. Kamu akan melihat",
                    "     onDestroy lalu onCreate, dan hitung kembali 0.",
                    "  3. Untuk data sekecil skor dan nomor soal, pakai",
                    "     rememberSaveable di Compose:",
                    "       var skor by rememberSaveable { mutableStateOf(0) }",
                    "  4. Kalau datanya lebih besar, misalnya daftar soal dari server,",
                    "     pindahkan ke ViewModel.",
                    "  5. Uji lagi dengan Don't keep activities menyala, lalu tekan",
                    "     Home dan kembali ke aplikasi.",
                ],
            },
        ],
    },
    {
        "title": "8. Composable Pertama dan Cara Compose Menggambar",
        "sections": [
            {
                "body": [
                    "Ada dua cara memberi perintah untuk sebuah tampilan. Cara pertama",
                    "disebut imperatif: kamu menyuruh langkah demi langkah. Ambil",
                    "label itu, ganti teksnya, sembunyikan tombol ini, tampilkan yang",
                    "itu. Cara kedua disebut deklaratif: kamu cukup menjelaskan layar",
                    "harus kelihatan seperti apa untuk data tertentu, dan toolkit-nya",
                    "yang mengurus perubahan.",
                    "",
                    "Jetpack Compose adalah toolkit UI deklaratif untuk Android, dan",
                    "Google menyarankannya untuk semua aplikasi baru. Versi terbarunya",
                    "saat materi ini ditulis adalah compose-ui 1.12.1 (9 September",
                    "2026) dengan Material 3 versi 1.4.0. Kalau kamu pernah melihat",
                    "React di web, idenya mirip: tampilan adalah fungsi dari data.",
                    "Programmer sering menulisnya UI = f(state).",
                ],
            },
            {
                "heading": "Fungsi @Composable",
                "bahasa": "kotlin",
                "code": """@Composable
fun KartuSapa(nama: String, kelas: String) {
    Column(modifier = Modifier.padding(16.dp)) {
        Text(
            text = "Halo, $nama!",
            style = MaterialTheme.typography.titleLarge
        )
        Text(text = "Kelas $kelas")
    }
}

@Preview(showBackground = true)
@Composable
fun KartuSapaPreview() {
    MaterialTheme {
        KartuSapa(nama = "Rina", kelas = "XI RPL 2")
    }
}""",
            },
            {
                "body": [
                    "Fungsi yang diberi anotasi @Composable disebut composable. Ada",
                    "beberapa aturan yang langsung kelihatan dari contoh di atas:",
                    "  - Composable nggak mengembalikan apa-apa. Ia memancarkan",
                    "    tampilan, artinya menambahkan potongan UI ke layar waktu",
                    "    dipanggil.",
                    "  - Namanya diawali huruf besar dan berupa kata benda, seperti",
                    "    KartuSapa atau Text, karena ia mewakili sesuatu yang tampil.",
                    "  - Composable cuma boleh dipanggil dari composable lain.",
                    "  - Column menyusun anaknya dari atas ke bawah, dan Text",
                    "    menampilkan tulisan. Keduanya juga composable.",
                    "",
                    "Fungsi berlabel @Preview nggak dipakai aplikasinya. Android",
                    "Studio menggambarnya di panel pratinjau, jadi kamu bisa melihat",
                    "kartu itu tanpa menjalankan emulator.",
                ],
            },
            {
                "heading": "Memasang ke Activity",
                "bahasa": "kotlin",
                "code": """class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            MaterialTheme {
                KartuSapa(nama = "Rina", kelas = "XI RPL 2")
            }
        }
    }
}""",
            },
            {
                "heading": "Tiga fase menggambar",
                "body": [
                    "Waktu setContent dijalankan, Compose mengerjakan tiga fase:",
                    "  1. Composition: semua composable dipanggil, dan hasilnya",
                    "     dicatat sebagai pohon UI.",
                    "  2. Layout: tiap simpul di pohon diukur, lalu diberi posisi.",
                    "  3. Drawing: piksel digambar ke layar.",
                    "",
                    "Pohon UI itu mirip DOM di HTML: Column jadi induk, dua Text jadi",
                    "anaknya. Tiruan JavaScript di bawah meniru fase pertama. Tiap",
                    "fungsi mengembalikan simpul pohon dari datanya, lalu pohonnya",
                    "dicetak. Compose sungguhan nggak mengembalikan objek seperti ini,",
                    "tapi gagasannya sama: fungsi yang sama dengan data berbeda",
                    "menghasilkan pohon berbeda.",
                ],
            },
            {
                "heading": "Tiruan fase composition",
                "code": """function Teks(isi) { return { jenis: 'Text', isi, anak: [] }; }
function Kolom(...anak) { return { jenis: 'Column', anak }; }
function KartuSapa(nama, kelas) {
  return Kolom(Teks(`Halo, ${nama}!`), Teks(`Kelas ${kelas}`));
}

function cetak(simpul, dalam = 0) {
  const label = simpul.isi ? `${simpul.jenis} "${simpul.isi}"` : simpul.jenis;
  console.log('  '.repeat(dalam) + label);
  for (const a of simpul.anak) cetak(a, dalam + 1);
}

cetak(KartuSapa('Rina', 'XI RPL 2'));
cetak(KartuSapa('Budi', 'X TKJ 1'));""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Column",
                    "    Text \"Halo, Rina!\"",
                    "    Text \"Kelas XI RPL 2\"",
                    "  Column",
                    "    Text \"Halo, Budi!\"",
                    "    Text \"Kelas X TKJ 1\"",
                ],
            },
            {
                "heading": "Modifier",
                "bahasa": "kotlin",
                "code": """Text(
    text = "Simpan",
    color = Color.White,
    modifier = Modifier
        .padding(8.dp)
        .background(Color(0xFF2E7D32))
        .padding(16.dp)
        .clickable { simpan() }
)""",
            },
            {
                "body": [
                    "Modifier mengatur ukuran, jarak, latar, dan perilaku sentuh",
                    "sebuah composable. Modifier dirangkai dengan titik, dan urutannya",
                    "berpengaruh. Rangkaian di atas dibaca dari luar ke dalam:",
                    "  - padding(8.dp) pertama memberi jarak bening di luar kotak,",
                    "    mirip margin di CSS.",
                    "  - background mewarnai kotak hijau.",
                    "  - padding(16.dp) kedua memberi jarak di dalam kotak hijau,",
                    "    mirip padding di CSS.",
                    "  - clickable di paling belakang cuma menutupi area tulisannya.",
                    "",
                    "Jebakan: karena clickable ditaruh paling akhir, mengetuk pinggir",
                    "kotak hijau nggak berbuat apa-apa. Pindahkan clickable ke depan",
                    "padding(16.dp) supaya seluruh kotak hijau bisa diketuk.",
                    "",
                    "Jebakan: menganggap composable cuma dipanggil sekali. Compose",
                    "boleh memanggil composable berkali-kali, kapan saja datanya",
                    "berubah, dan boleh juga melewatinya. Jadi badan composable cuma",
                    "boleh menggambar. Urusan lain seperti memanggil server dibahas",
                    "di materi berikutnya.",
                    "",
                    "Dibanding cara lama, Compose memangkas banyak hal. Nggak ada lagi",
                    "berkas tata letak XML yang terpisah dari kodenya, nggak ada",
                    "findViewById, dan nggak ada adapter untuk daftar. Semuanya",
                    "ditulis dengan Kotlin, jadi if, for, dan fungsi biasa langsung",
                    "bisa dipakai untuk menyusun tampilan. API yang sama juga dipakai",
                    "Compose Multiplatform dari JetBrains untuk iOS dan desktop, yang",
                    "dibahas di bab Berbagi Kode Lintas Platform Lain.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi contoh resmi Google, seperti Now in Android dan Jetsnack",
                    "di GitHub, ditulis seluruhnya dengan Compose. Pola yang paling",
                    "sering kamu lihat di kode seperti itu adalah composable kecil",
                    "berparameter, misalnya kartu produk, yang dipakai ulang di banyak",
                    "layar dengan data berbeda.",
                    "",
                    "Kasus kecil: wali kelas minta layar profil untuk tiap siswa:",
                    "nama, kelas, dan nomor induk. Isinya sama untuk 32 siswa, cuma",
                    "datanya yang beda.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan data yang berubah antarsiswa. Itulah parameter",
                    "     composable-nya.",
                    "  2. Tulis satu composable berparameter:",
                    "       @Composable",
                    "       fun KartuSiswa(nama: String, kelas: String, nis: String)",
                    "  3. Buat @Preview dengan dua atau tiga contoh data, termasuk nama",
                    "     yang panjang, supaya kelihatan apakah tulisannya terpotong.",
                    "  4. Panggil KartuSiswa yang sama untuk tiap siswa. Kalau tampilan",
                    "     kartunya perlu diubah, kamu cukup mengubah satu fungsi.",
                ],
            },
        ],
    },
    {
        "title": "9. State, remember, dan Recomposition",
        "sections": [
            {
                "body": [
                    "State adalah data yang bisa berubah dan memengaruhi tampilan:",
                    "jumlah pesanan, isi kolom pencarian, apakah dialog sedang",
                    "terbuka. Waktu state berubah, Compose memanggil ulang composable",
                    "yang membaca state itu supaya tampilannya ikut berubah. Proses",
                    "memanggil ulang ini disebut recomposition.",
                    "",
                    "Coba lihat penghitung di bawah. Kelihatannya benar, tapi angkanya",
                    "nggak pernah naik.",
                ],
            },
            {
                "heading": "Penghitung yang nggak mau naik",
                "bahasa": "kotlin",
                "code": """@Composable
fun PenghitungSalah() {
    var hitung = 0
    Button(onClick = { hitung++ }) {
        Text("Diketuk $hitung kali")
    }
}""",
            },
            {
                "body": [
                    "Ada dua masalah sekaligus. Pertama, hitung cuma variabel biasa.",
                    "Compose nggak tahu nilainya berubah, jadi nggak ada recomposition.",
                    "Kedua, seandainya recomposition terjadi karena hal lain, baris",
                    "var hitung = 0 ikut dijalankan lagi, dan angkanya kembali 0.",
                    "",
                    "Dua alat membereskan keduanya:",
                    "  - mutableStateOf membuat state yang diawasi Compose. Compose",
                    "    mencatat composable mana yang membacanya, lalu menjadwalkan",
                    "    recomposition untuk composable itu saat nilainya berubah.",
                    "  - remember menyimpan sebuah nilai di dalam komposisi, jadi",
                    "    nilainya bertahan walaupun composable-nya dipanggil ulang.",
                ],
            },
            {
                "heading": "mutableStateOf dan remember",
                "bahasa": "kotlin",
                "code": """@Composable
fun Penghitung() {
    var hitung by remember { mutableStateOf(0) }
    Button(onClick = { hitung++ }) {
        Text("Diketuk $hitung kali")
    }
}""",
            },
            {
                "body": [
                    "Kata by membuat hitung bisa dipakai seperti variabel biasa,",
                    "padahal di belakangnya ia membaca dan menulis nilai state.",
                    "Supaya by jalan, berkasnya butuh impor getValue dan setValue dari",
                    "androidx.compose.runtime; Android Studio biasanya menawarkannya",
                    "otomatis. Untuk angka bulat ada versi yang lebih hemat,",
                    "mutableIntStateOf.",
                    "",
                    "remember cuma bertahan selama composable-nya ada di layar. Waktu",
                    "Activity dibuat ulang karena layar diputar, nilainya hilang.",
                    "Kalau nilainya harus selamat dari putar layar, pakai",
                    "rememberSaveable, yang menyimpan nilainya ke Bundle seperti",
                    "dibahas di materi siklus hidup Activity.",
                    "",
                    "Tiga tempat menyimpan state, dan apa saja yang bisa mereka",
                    "lewati:",
                    "  remember          selamat dari recomposition saja",
                    "  rememberSaveable  juga selamat dari putar layar dan proses",
                    "                    yang dimatikan, asal datanya kecil",
                    "  ViewModel         selamat dari putar layar, cocok untuk data",
                    "                    layar yang besar (bab berikutnya)",
                ],
            },
            {
                "heading": "Siapa yang dipanggil ulang",
                "bahasa": "teks",
                "code": """@Composable fun LayarKantin() {      // membaca: tidak ada
    Column {
        Judul("Kantin Sekolah")      // membaca: tidak ada
        Penghitung()                 // membaca: hitung
    }
}

ketukan   hitung   yang dipanggil
awal      0        LayarKantin, Judul, Penghitung
1         1        Penghitung
2         2        Penghitung""",
            },
            {
                "body": [
                    "Waktu tombol diketuk, cuma bagian yang membaca hitung yang",
                    "dipanggil ulang. Judul nggak membaca state apa pun, jadi Compose",
                    "melewatinya. Cara ini yang membuat Compose tetap cepat walaupun",
                    "layarnya penuh composable: kerja ulangnya sekecil mungkin.",
                    "Tepatnya, Compose bahkan cuma mengulang lambda di dalam",
                    "Penghitung yang membaca hitung, tapi gambaran di atas cukup untuk",
                    "sekarang.",
                ],
            },
            {
                "heading": "State hoisting",
                "bahasa": "kotlin",
                "code": """@Composable
fun Penghitung(hitung: Int, onTambah: () -> Unit) {
    Button(onClick = onTambah) {
        Text("Diketuk $hitung kali")
    }
}

@Composable
fun LayarKantin() {
    var porsi by rememberSaveable { mutableStateOf(0) }
    Column {
        Text("Total: ${porsi * 12000} rupiah")
        Penghitung(hitung = porsi, onTambah = { porsi++ })
    }
}""",
            },
            {
                "body": [
                    "State hoisting artinya memindahkan state ke atas, ke pemanggil.",
                    "Penghitung sekarang nggak menyimpan apa-apa. Ia menerima angka",
                    "lewat parameter, dan melaporkan ketukan lewat fungsi onTambah.",
                    "Composable seperti ini disebut stateless.",
                    "",
                    "Keuntungannya terasa di contoh: LayarKantin butuh angka porsi",
                    "untuk menghitung total, jadi state-nya memang harus tinggal di",
                    "LayarKantin. Penghitung juga jadi gampang dipakai ulang dan diuji,",
                    "karena tampilannya cuma bergantung pada parameternya. Polanya",
                    "sering diringkas jadi: state turun, event naik.",
                ],
            },
            {
                "heading": "Efek samping",
                "bahasa": "kotlin",
                "code": """@Composable
fun DaftarBerita(vm: BeritaViewModel) {
    // Salah: dipanggil lagi setiap kali DaftarBerita direkomposisi
    // vm.muat()

    LaunchedEffect(Unit) {
        vm.muat()   // jalan sekali waktu DaftarBerita masuk layar
    }
    // ... tampilkan beritanya
}""",
            },
            {
                "body": [
                    "Efek samping adalah apa pun yang dikerjakan composable selain",
                    "menggambar: memanggil server, menulis ke database, atau mencatat",
                    "log analitik. Karena composable bisa dipanggil puluhan kali,",
                    "efek samping di badannya ikut jalan puluhan kali.",
                    "",
                    "Compose menyediakan tempat khusus untuk itu. LaunchedEffect",
                    "menjalankan kodenya di coroutine saat composable masuk layar, dan",
                    "mengulangnya cuma kalau kunci yang diberikan berubah.",
                    "DisposableEffect dipakai kalau ada yang perlu dibereskan saat",
                    "composable keluar dari layar, misalnya mencabut pendengar sensor.",
                    "Di aplikasi sungguhan, memuat data paling rapi dipicu dari",
                    "ViewModel, yang dibahas di bab berikutnya.",
                    "",
                    "Jebakan: mengubah isi list di dalam mutableStateOf. Misalnya",
                    "state-mu berbentuk mutableStateOf(mutableListOf(\"Teh\")), lalu kamu",
                    "memanggil daftar.value.add(\"Kopi\"), layarnya nggak berubah.",
                    "Objek list-nya tetap objek yang sama, jadi Compose nggak melihat",
                    "perubahan. Pakai mutableStateListOf, atau ganti list-nya dengan",
                    "list baru: daftar.value = daftar.value + \"Kopi\".",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kolom pencarian di aplikasi toko online adalah contoh state",
                    "hoisting yang paling umum. Teks yang diketik disimpan di",
                    "pemanggil atau ViewModel, karena teks itu dipakai di banyak",
                    "tempat: untuk memfilter daftar, menampilkan tombol hapus, dan",
                    "menyimpan riwayat pencarian.",
                    "",
                    "Kasus kecil: kamu membuat kolom pencarian dengan TextField. Huruf",
                    "yang diketik nggak pernah muncul, dan setelah diperbaiki, isinya",
                    "hilang setiap kali HP diputar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Huruf nggak muncul berarti nilai TextField nggak pernah",
                    "     diperbarui. TextField nggak menyimpan teksnya sendiri; ia",
                    "     menampilkan value dan melaporkan ketikan lewat onValueChange.",
                    "  2. Simpan teksnya sebagai state, lalu perbarui di onValueChange:",
                    "       var kata by remember { mutableStateOf(\"\") }",
                    "       TextField(value = kata, onValueChange = { kata = it })",
                    "  3. Teks hilang saat diputar berarti remember kurang. Ganti",
                    "     dengan rememberSaveable.",
                    "  4. Kalau teks itu juga dipakai untuk memfilter daftar, angkat",
                    "     state-nya ke composable layar, lalu oper ke TextField dan",
                    "     ke daftar lewat parameter.",
                ],
            },
        ],
    },
    {
        "title": "10. Layout, Daftar, dan Material 3",
        "sections": [
            {
                "body": [
                    "Compose punya tiga wadah dasar untuk menyusun tampilan:",
                    "  - Column menyusun anaknya dari atas ke bawah.",
                    "  - Row menyusun anaknya dari kiri ke kanan.",
                    "  - Box menumpuk anaknya di tempat yang sama, yang belakangan",
                    "    ditaruh di atas.",
                    "",
                    "Kalau kamu sudah belajar flexbox di kurikulum CSS, Row dan Column",
                    "terasa akrab. Arrangement mengatur sumbu utama, seperti",
                    "justify-content. Alignment mengatur sumbu silang, seperti",
                    "align-items. Modifier.weight(1f) mirip flex: 1, yaitu mengambil",
                    "sisa ruang.",
                ],
            },
            {
                "heading": "Row dengan dua ujung",
                "bahasa": "kotlin",
                "code": """@Composable
fun BarisProduk(nama: String, harga: Int) {
    Row(
        modifier = Modifier.fillMaxWidth().padding(16.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Text(nama)
        Text("Rp$harga")
    }
}

// BarisProduk("Es teh manis", 5000)""",
            },
            {
                "body": [
                    "Arrangement.SpaceBetween menempelkan anak pertama ke kiri dan",
                    "anak terakhir ke kanan, persis justify-content: space-between.",
                    "Alignment.CenterVertically membuat keduanya sejajar di tengah",
                    "secara tegak.",
                    "",
                    "Box dipakai kalau ada yang harus menumpuk, misalnya label Baru",
                    "di pojok foto produk:",
                    "  Box(modifier = Modifier.size(96.dp)) {",
                    "      Image(painterResource(R.drawable.foto), contentDescription = null)",
                    "      Text(\"Baru\", modifier = Modifier.align(Alignment.TopEnd))",
                    "  }",
                ],
            },
            {
                "heading": "Daftar panjang dengan LazyColumn",
                "bahasa": "kotlin",
                "code": """data class Siswa(val nis: String, val nama: String)

@Composable
fun DaftarSiswa(siswa: List<Siswa>, modifier: Modifier = Modifier) {
    LazyColumn(modifier = modifier, contentPadding = PaddingValues(16.dp)) {
        items(siswa, key = { it.nis }) { s ->
            Text(s.nama, modifier = Modifier.padding(vertical = 12.dp))
        }
    }
}""",
            },
            {
                "body": [
                    "Column biasa memanggil composable untuk semua anaknya, walaupun",
                    "sebagian besar ada di luar layar. Untuk 1.000 siswa, itu 1.000",
                    "baris yang dibuat dan diukur, padahal yang kelihatan cuma",
                    "sepuluhan. LazyColumn cuma membuat baris yang terlihat ditambah",
                    "sedikit cadangan. Waktu daftar digulir, baris yang keluar layar",
                    "dibuang dan baris baru dibuat.",
                    "",
                    "Parameter key memberi tiap baris identitas tetap, di sini nomor",
                    "induk siswa. Tanpa key, Compose mengenali baris dari posisinya,",
                    "jadi kalau ada siswa yang dihapus dari tengah, state milik baris",
                    "di bawahnya bisa ikut bergeser ke baris yang salah.",
                    "",
                    "Tiruan di bawah menghitung baris mana saja yang dibuat LazyColumn",
                    "pada beberapa posisi gulir. Angka cadangannya disederhanakan jadi",
                    "satu baris di atas dan bawah layar.",
                ],
            },
            {
                "heading": "Tiruan jendela LazyColumn",
                "code": """const TINGGI_BARIS = 72;   // dp
const TINGGI_LAYAR = 640;  // dp
const CADANGAN = 1;        // baris ekstra di atas dan bawah layar
const total = 1000;

function barisDibuat(gulir) {
  const awal = Math.max(0, Math.floor(gulir / TINGGI_BARIS) - CADANGAN);
  const akhir = Math.min(total - 1,
    Math.floor((gulir + TINGGI_LAYAR - 1) / TINGGI_BARIS) + CADANGAN);
  return [awal, akhir];
}

for (const gulir of [0, 300, 7200]) {
  const [awal, akhir] = barisDibuat(gulir);
  console.log(`gulir ${gulir} dp: baris ${awal}-${akhir} (${akhir - awal + 1} dari ${total})`);
}
console.log(`Column biasa: selalu ${total} dari ${total}`);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  gulir 0 dp: baris 0-9 (10 dari 1000)",
                    "  gulir 300 dp: baris 3-14 (12 dari 1000)",
                    "  gulir 7200 dp: baris 99-109 (11 dari 1000)",
                    "  Column biasa: selalu 1000 dari 1000",
                    "",
                    "Ada juga LazyRow untuk daftar mendatar dan LazyVerticalGrid untuk",
                    "kisi, misalnya galeri foto. Cara kerjanya sama.",
                    "",
                    "Soal ukuran, Compose memakai dua satuan. dp (density-independent",
                    "pixel) dipakai untuk jarak dan ukuran kotak, supaya tampilannya",
                    "sama besar di HP berlayar rapat maupun renggang. sp dipakai untuk",
                    "ukuran huruf, karena sp ikut membesar kalau pengguna memilih",
                    "huruf besar di pengaturan HP. Teks yang tampil di layar sebaiknya",
                    "diambil dari res/values/strings.xml lewat stringResource, supaya",
                    "aplikasimu bisa diterjemahkan tanpa mengubah kode.",
                    "",
                    "Jebakan: menaruh LazyColumn di dalam Column yang diberi",
                    "verticalScroll. Dua-duanya menggulir ke arah yang sama, dan",
                    "aplikasinya berhenti dengan pesan seperti Vertically scrollable",
                    "component was measured with an infinity maximum height",
                    "constraints. Kalau butuh judul di atas daftar, jadikan judul itu",
                    "butir pertama LazyColumn dengan item { }.",
                ],
            },
            {
                "heading": "Material 3",
                "bahasa": "kotlin",
                "code": """@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun LayarSiswa(siswa: List<Siswa>, onTambah: () -> Unit) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Siswa XI RPL 2") }) },
        floatingActionButton = {
            FloatingActionButton(onClick = onTambah) {
                Icon(
                    painterResource(R.drawable.ic_tambah),
                    contentDescription = "Tambah siswa"
                )
            }
        }
    ) { padding ->
        DaftarSiswa(siswa, modifier = Modifier.padding(padding))
    }
}""",
            },
            {
                "body": [
                    "Material 3 adalah sistem desain dari Google. Pustakanya,",
                    "androidx.compose.material3 versi 1.4.0, menyediakan komponen siap",
                    "pakai: Scaffold sebagai kerangka layar, TopAppBar, Card, Button,",
                    "FloatingActionButton, NavigationBar di bawah layar, dan banyak",
                    "lagi. Warna dan huruf diambil dari MaterialTheme, jadi mengganti",
                    "tema cukup di satu tempat. Di Android 12 ke atas, Material 3 bisa",
                    "memakai dynamic color, yaitu warna tema yang diambil dari",
                    "wallpaper pengguna.",
                    "",
                    "Scaffold memberi padding ke isinya supaya daftar nggak tertutup",
                    "TopAppBar. Padding itu wajib diteruskan ke isi, seperti",
                    "Modifier.padding(padding) di atas. Untuk animasi yang dibuat",
                    "desainer di After Effects, banyak aplikasi memakai pustaka Lottie,",
                    "yang juga punya versi Compose.",
                    "",
                    "Jebakan: lupa contentDescription di ikon. Pembaca layar TalkBack",
                    "membacakan teks itu untuk pengguna tunanetra. Ikon hiasan yang",
                    "nggak punya arti boleh diberi null.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Daftar produk di aplikasi toko online, daftar chat, dan riwayat",
                    "transaksi dompet digital semuanya berupa daftar panjang. Di",
                    "aplikasi Compose, daftar seperti itu ditulis dengan LazyColumn",
                    "atau LazyVerticalGrid, dengan key berupa ID dari database.",
                    "",
                    "Kasus kecil: aplikasi koperasi menampilkan 2.000 barang. Waktu",
                    "digulir, daftarnya patah-patah, dan kadang tanda centang pindah",
                    "ke barang yang salah setelah ada barang dihapus.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek wadahnya. Kalau masih Column dengan verticalScroll, ganti",
                    "     dengan LazyColumn supaya cuma baris terlihat yang dibuat.",
                    "  2. Beri key dari ID barang supaya state tiap baris, termasuk",
                    "     centangnya, menempel ke barangnya, bukan ke posisinya:",
                    "       items(barang, key = { it.id }) { b -> BarisBarang(b) }",
                    "  3. Keluarkan pekerjaan berat dari badan baris, misalnya",
                    "     memformat harga atau mengurutkan data. Kerjakan sekali di",
                    "     ViewModel, jangan di setiap baris.",
                    "  4. Ukur di build release. Build debug Compose jauh lebih lambat,",
                    "     jadi patah-patah di debug belum tentu terjadi di HP pengguna.",
                ],
            },
        ],
    },
    {
        "title": "11. Warisan View dan Layout XML",
        "sections": [
            {
                "body": [
                    "Sebelum Compose stabil pada Juli 2021, tampilan Android dibangun",
                    "dengan View system. Tata letak ditulis di berkas XML, lalu",
                    "dihubungkan ke kode Kotlin atau Java. Cara ini masih didukung",
                    "penuh dan masih ada di banyak aplikasi yang dirawat sampai",
                    "sekarang, tapi statusnya menurun: materi dan fitur baru Google",
                    "berfokus ke Compose.",
                    "",
                    "Kenapa tetap perlu dipelajari? Kalau kamu PKL atau kerja di",
                    "perusahaan yang aplikasinya sudah berumur beberapa tahun, besar",
                    "kemungkinan kamu bertemu layout XML di hari pertama.",
                ],
            },
            {
                "heading": "Layout XML",
                "bahasa": "xml",
                "code": """<!-- res/layout/activity_main.xml -->
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:padding="16dp">

    <TextView
        android:id="@+id/teksHitung"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Diketuk 0 kali" />

    <Button
        android:id="@+id/tombolTambah"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Tambah" />
</LinearLayout>""",
            },
            {
                "body": [
                    "LinearLayout dengan orientation vertical sama tugasnya dengan",
                    "Column. match_parent artinya selebar induknya, wrap_content",
                    "artinya secukupnya untuk isi. android:id memberi nama supaya",
                    "kode bisa menemukan elemen itu.",
                ],
            },
            {
                "heading": "Kode yang mengubah tampilan sendiri",
                "bahasa": "kotlin",
                "code": """class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding
    private var hitung = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        binding.tombolTambah.setOnClickListener {
            hitung++
            binding.teksHitung.text = "Diketuk $hitung kali"
        }
    }
}""",
            },
            {
                "body": [
                    "Ini gaya imperatif. Setelah hitung naik, kamu sendiri yang",
                    "mengubah teks TextView-nya. Kalau angka yang sama tampil di tiga",
                    "tempat dan kamu lupa memperbarui satu, tampilannya jadi nggak",
                    "sinkron. Di Compose masalah itu hilang karena semua tempat",
                    "membaca state yang sama.",
                    "",
                    "ActivityMainBinding dibuat otomatis dari activity_main.xml oleh",
                    "fitur ViewBinding, yang dinyalakan dengan",
                    "buildFeatures { viewBinding = true } di berkas build. Kode yang",
                    "lebih tua memakai findViewById, yang mencari elemen lewat ID dan",
                    "bisa gagal saat aplikasi jalan kalau ID atau tipenya salah.",
                    "Tutorial lama juga sering memakai kotlinx.android.synthetic.",
                    "Plugin itu sudah dihapus sejak Kotlin 1.8, jadi kodenya nggak",
                    "bisa dikompilasi lagi.",
                ],
            },
            {
                "heading": "RecyclerView, padanan LazyColumn",
                "bahasa": "kotlin",
                "code": """class SiswaAdapter : ListAdapter<Siswa, SiswaAdapter.Penampung>(Beda) {

    class Penampung(val binding: ItemSiswaBinding) :
        RecyclerView.ViewHolder(binding.root)

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int) =
        Penampung(ItemSiswaBinding.inflate(LayoutInflater.from(parent.context), parent, false))

    override fun onBindViewHolder(holder: Penampung, position: Int) {
        holder.binding.teksNama.text = getItem(position).nama
    }

    object Beda : DiffUtil.ItemCallback<Siswa>() {
        override fun areItemsTheSame(a: Siswa, b: Siswa) = a.nis == b.nis
        override fun areContentsTheSame(a: Siswa, b: Siswa) = a == b
    }
}""",
            },
            {
                "body": [
                    "RecyclerView menampilkan daftar panjang dengan memakai ulang",
                    "beberapa baris yang sama sambil digulir. Adapter menghubungkan",
                    "data ke baris: onCreateViewHolder membuat baris baru, dan",
                    "onBindViewHolder mengisi baris dengan data di posisi tertentu.",
                    "DiffUtil membandingkan daftar lama dan baru supaya cuma baris",
                    "yang berubah yang digambar ulang; perannya mirip key di",
                    "LazyColumn. Satu daftar di Compose cukup beberapa baris,",
                    "sedangkan di RecyclerView butuh adapter, layout baris, dan kelas",
                    "penampung.",
                    "",
                    "Dua nama lain yang sering muncul di kode lama:",
                    "  - Fragment adalah potongan layar yang punya siklus hidup",
                    "    sendiri di dalam Activity. Fragment dulu dipakai untuk tab dan",
                    "    tata letak dua panel di tablet.",
                    "  - ConstraintLayout menyusun elemen dengan aturan seperti tombol",
                    "    ini di bawah judul dan sejajar kanan. Layout ini dulu jadi",
                    "    pilihan utama untuk layar yang rumit.",
                    "",
                    "Jebakan: di Fragment, objek binding harus dikosongkan di",
                    "onDestroyView. Tampilan Fragment bisa dibuang sementara",
                    "Fragment-nya masih hidup, dan binding yang tertinggal menahan",
                    "seluruh tampilan lama di memori.",
                ],
            },
            {
                "heading": "Hidup berdampingan",
                "bahasa": "kotlin",
                "code": """// Compose di dalam layar XML lama (ComposeView di layout)
binding.composeView.setContent {
    MaterialTheme { KartuSapa(nama = "Rina", kelas = "XI RPL 2") }
}

// View lama di dalam Compose
@Composable
fun HalamanBantuan() {
    AndroidView(factory = { context -> WebView(context) })
}""",
            },
            {
                "body": [
                    "Kamu nggak perlu memilih satu untuk selamanya. ComposeView",
                    "memasang composable di dalam layout XML, dan AndroidView",
                    "memasang View lama di dalam Compose. Banyak tim memindahkan",
                    "aplikasinya ke Compose satu layar demi satu layar dengan cara",
                    "ini, tanpa menulis ulang semuanya sekaligus.",
                    "",
                    "Komponen Material di dunia View datang dari pustaka Material",
                    "Components for Android, yang juga masih dirawat. Jadi aplikasi",
                    "lama bisa tetap tampil dengan gaya Material walaupun belum",
                    "pindah ke Compose. Kalau kamu ragu sebuah layar ditulis dengan",
                    "cara apa, cari berkasnya: ada res/layout untuk XML, atau fungsi",
                    "berlabel @Composable untuk Compose.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi yang sudah berumur beberapa tahun, misalnya aplikasi",
                    "internal perusahaan atau aplikasi kasir, sering masih penuh",
                    "layout XML, Fragment, dan RecyclerView. Panduan resmi Android",
                    "punya bagian khusus tentang migrasi bertahap ke Compose karena",
                    "keadaan ini umum sekali.",
                    "",
                    "Kasus kecil: di tempat PKL kamu diminta menambah kolom nomor HP",
                    "di formulir pendaftaran lama. Formulirnya ditulis dengan layout",
                    "XML dan ViewBinding.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari layout-nya. Nama kelas binding menunjukkan nama berkas:",
                    "     FormDaftarBinding berasal dari res/layout/form_daftar.xml.",
                    "  2. Tambahkan elemen baru di XML dengan ID yang jelas:",
                    "       <EditText",
                    "           android:id=\"@+id/isianHp\"",
                    "           android:inputType=\"phone\"",
                    "           android:hint=\"@string/nomor_hp\" />",
                    "  3. Tulis teks petunjuknya di res/values/strings.xml, jangan",
                    "     langsung di XML, supaya ikut diterjemahkan.",
                    "  4. Di kode, baca isinya lewat binding.isianHp.text, lalu",
                    "     sertakan dalam data yang dikirim.",
                    "  5. Jangan memindahkan formulir itu ke Compose di tugas yang",
                    "     sama. Perubahan kecil lebih gampang ditinjau dan diuji.",
                ],
            },
        ],
    },
    {
        "title": "12. ViewModel, UiState, dan Navigasi",
        "sections": [
            {
                "body": [
                    "Di bab sebelumnya semua state tinggal di composable atau di",
                    "Activity. Untuk aplikasi kecil itu cukup. Begitu aplikasinya",
                    "memuat data dari server, menyimpan ke database, dan punya",
                    "beberapa layar, kode seperti itu cepat kusut. Data yang sudah",
                    "dimuat hilang setiap layar diputar, dan kode tampilan bercampur",
                    "dengan kode jaringan.",
                    "",
                    "Panduan arsitektur resmi Android membagi aplikasi jadi lapisan:",
                    "  - Lapisan UI: composable yang menggambar, plus ViewModel yang",
                    "    menyimpan state layar.",
                    "  - Lapisan data: repository yang jadi satu-satunya pintu ke",
                    "    data, plus sumber datanya, misalnya database lokal dan API.",
                    "  - Lapisan domain, opsional, untuk aturan bisnis yang dipakai",
                    "    beberapa ViewModel sekaligus.",
                    "",
                    "Datanya mengalir satu arah. State turun dari ViewModel ke",
                    "composable, dan event seperti ketukan naik dari composable ke",
                    "ViewModel. Ini pola yang sama dengan state hoisting di bab",
                    "Compose, cuma tempat state-nya sekarang pindah ke ViewModel.",
                ],
            },
            {
                "heading": "ViewModel dan UiState",
                "bahasa": "kotlin",
                "code": """data class CatatanUiState(
    val memuat: Boolean = false,
    val catatan: List<Catatan> = emptyList(),
    val pesanGalat: String? = null,
)

class CatatanViewModel(
    private val repo: CatatanRepository
) : ViewModel() {

    private val _uiState = MutableStateFlow(CatatanUiState())
    val uiState: StateFlow<CatatanUiState> = _uiState.asStateFlow()

    init { muat() }

    fun muat() {
        viewModelScope.launch {
            _uiState.update { it.copy(memuat = true, pesanGalat = null) }
            try {
                val hasil = repo.ambilSemua()
                _uiState.update { it.copy(memuat = false, catatan = hasil) }
            } catch (e: IOException) {
                _uiState.update { it.copy(memuat = false, pesanGalat = "Gagal memuat") }
            }
        }
    }
}""",
            },
            {
                "body": [
                    "UiState adalah satu objek yang menggambarkan seluruh keadaan",
                    "layar: sedang memuat atau nggak, datanya apa, ada pesan galat",
                    "atau nggak. Karena semuanya ada di satu objek, layar nggak",
                    "mungkin menampilkan keadaan yang saling bertentangan, misalnya",
                    "indikator memuat yang terus berputar padahal datanya sudah ada.",
                    "",
                    "Perhatikan dua properti _uiState dan uiState. Yang pertama",
                    "MutableStateFlow, bisa diubah, dan disembunyikan dengan private.",
                    "Yang kedua cuma bisa dibaca dari luar. Jadi hanya ViewModel yang",
                    "boleh mengubah state, dan layar cuma boleh membacanya. StateFlow",
                    "sendiri dibahas di materi berikutnya.",
                    "",
                    "Sebagian programmer lebih suka sealed interface, supaya keadaan",
                    "yang mustahil memang nggak bisa ditulis:",
                    "  sealed interface UiState {",
                    "      data object Memuat : UiState",
                    "      data class Sukses(val catatan: List<Catatan>) : UiState",
                    "      data class Gagal(val pesan: String) : UiState",
                    "  }",
                ],
            },
            {
                "heading": "Membaca state di Compose",
                "bahasa": "kotlin",
                "code": """@Composable
fun LayarCatatan(vm: CatatanViewModel) {
    val state by vm.uiState.collectAsStateWithLifecycle()
    when {
        state.memuat -> CircularProgressIndicator()
        state.pesanGalat != null -> Text(state.pesanGalat!!)
        else -> DaftarCatatan(state.catatan, onMuatUlang = vm::muat)
    }
}""",
            },
            {
                "body": [
                    "collectAsStateWithLifecycle mengubah StateFlow jadi state",
                    "Compose, dan berhenti membaca waktu aplikasi ada di belakang",
                    "supaya nggak membuang baterai. Ketukan tombol muat ulang naik ke",
                    "ViewModel lewat vm::muat.",
                    "",
                    "Kenapa ViewModel selamat dari putar layar? ViewModel nggak",
                    "disimpan di objek Activity. Ia disimpan di wadah terpisah yang",
                    "dipertahankan sistem selama layar itu belum ditutup sepenuhnya.",
                    "Activity baru hasil putar layar meminta ViewModel ke wadah yang",
                    "sama, dan mendapat objek yang sama. Waktu layarnya ditutup untuk",
                    "selamanya, ViewModel dibuang dan onCleared dipanggil. Tiruan di",
                    "bawah menunjukkan idenya dengan Kotlin biasa.",
                ],
            },
            {
                "heading": "Tiruan wadah ViewModel",
                "bahasa": "kotlin",
                "code": """class PenghitungViewModel {
    var hitung = 0
}

// Tiruan wadah ViewModel: hidup lebih lama dari objek layar.
class PenyimpanViewModel {
    private val isi = mutableMapOf<String, PenghitungViewModel>()
    fun ambil(kunci: String) = isi.getOrPut(kunci) { PenghitungViewModel() }
}

class LayarTiruan(penyimpan: PenyimpanViewModel) {
    val vm = penyimpan.ambil("penghitung")
    var hitungLokal = 0
}

fun main() {
    val penyimpan = PenyimpanViewModel()
    var layar = LayarTiruan(penyimpan)
    layar.vm.hitung += 2
    layar.hitungLokal += 2

    layar = LayarTiruan(penyimpan)      // putar layar: objek layar baru
    println("di ViewModel: ${layar.vm.hitung}")
    println("di field layar: ${layar.hitungLokal}")
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  di ViewModel: 2",
                    "  di field layar: 0",
                    "",
                    "Jebakan: menyimpan Activity, Context milik Activity, atau View di",
                    "dalam ViewModel. ViewModel hidup lebih lama dari Activity, jadi",
                    "Activity lama yang seharusnya dibuang tetap tertahan di memori.",
                    "Pustaka lifecycle versi terbaru saat materi ini ditulis adalah",
                    "2.11.0.",
                ],
            },
            {
                "heading": "Navigasi antarlayar",
                "bahasa": "kotlin",
                "code": """data object Beranda
data class Detail(val id: Int)

@Composable
fun AplikasiCatatan() {
    val backStack = remember { mutableStateListOf<Any>(Beranda) }
    NavDisplay(
        backStack = backStack,
        onBack = { backStack.removeLastOrNull() },
        entryProvider = { kunci ->
            when (kunci) {
                is Beranda -> NavEntry(kunci) {
                    LayarBeranda(onBuka = { id -> backStack.add(Detail(id)) })
                }
                is Detail -> NavEntry(kunci) { LayarDetail(kunci.id) }
                else -> NavEntry(Unit) { Text("Rute nggak dikenal") }
            }
        }
    )
}""",
            },
            {
                "body": [
                    "Android Jetpack punya dua pustaka navigasi. Navigation 2.10",
                    "dipakai di banyak aplikasi yang sudah ada: NavHost dan",
                    "NavController mengatur perpindahan layar, dan rute bisa ditulis",
                    "sebagai kelas Kotlin. Navigation 3 (versi 1.2.0) adalah pustaka",
                    "baru yang dibuat khusus untuk Compose. Ide besarnya: tumpukan",
                    "layar atau back stack adalah list milikmu sendiri. Menambah",
                    "elemen ke list berarti membuka layar baru, dan membuang elemen",
                    "terakhir berarti kembali. NavDisplay cuma mengamati list itu dan",
                    "menggambar layar paling atas.",
                    "",
                    "Contoh di atas menyimpan back stack dengan remember supaya",
                    "singkat. Untuk aplikasi sungguhan, dokumentasi Navigation 3",
                    "menyediakan rememberNavBackStack supaya tumpukannya ikut selamat",
                    "dari putar layar.",
                ],
            },
            {
                "heading": "Dua pustaka Jetpack lain yang sering ikut",
                "body": [
                    "WorkManager (versi 2.12.0) menjalankan pekerjaan latar yang",
                    "harus selesai walaupun aplikasinya ditutup atau HP dinyalakan",
                    "ulang, misalnya mengirim catatan yang tertunda saat internet",
                    "kembali. Pekerjaannya bisa diberi syarat seperti harus ada",
                    "jaringan atau HP sedang diisi daya.",
                    "",
                    "DataStore (versi 1.2.1) menyimpan data kecil seperti pilihan tema",
                    "atau token login, dan menggantikan SharedPreferences yang lama.",
                    "DataStore membaca dan menulis di luar UI thread, dan perubahan",
                    "nilainya bisa diamati lewat Flow.",
                    "  val Context.pengaturan by preferencesDataStore(name = \"pengaturan\")",
                    "  val TEMA_GELAP = booleanPreferencesKey(\"tema_gelap\")",
                    "",
                    "  suspend fun simpanTema(context: Context, gelap: Boolean) {",
                    "      context.pengaturan.edit { it[TEMA_GELAP] = gelap }",
                    "  }",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi contoh resmi Now in Android di GitHub memakai susunan",
                    "ini persis. Composable membaca UiState dari ViewModel lewat",
                    "StateFlow. ViewModel memanggil repository, dan repository",
                    "memutuskan apakah data diambil dari database lokal atau dari",
                    "jaringan. Struktur foldernya bisa kamu jadikan contoh.",
                    "",
                    "Kasus kecil: aplikasi absensi PKL memuat daftar hadir dari server",
                    "di onCreate. Setiap kali HP diputar, daftar dimuat ulang,",
                    "indikator memuat muncul lagi, dan kuota internet terpakai",
                    "percuma.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan pemanggilan server dari Activity ke ViewModel, dan",
                    "     panggil dari init supaya cuma jalan sekali per ViewModel.",
                    "  2. Simpan hasilnya di MutableStateFlow berisi UiState, lalu",
                    "     buka versi hanya-baca untuk layar.",
                    "  3. Di composable, baca dengan collectAsStateWithLifecycle.",
                    "  4. Putar emulator beberapa kali sambil melihat Logcat. Log",
                    "     permintaan server seharusnya cuma muncul sekali.",
                    "  5. Kalau datanya juga perlu ada saat offline, simpan ke Room",
                    "     lewat repository. Caranya ada di materi Room.",
                ],
            },
        ],
    },
    {
        "title": "13. Coroutines dan Flow untuk Kode Asinkron",
        "sections": [
            {
                "body": [
                    "Di bab pertama kamu sudah tahu aturannya: pekerjaan lama nggak",
                    "boleh dijalankan di UI thread. Pertanyaannya, bagaimana menulis",
                    "kode yang menunggu jawaban server tanpa memblokir apa pun, tapi",
                    "tetap enak dibaca?",
                    "",
                    "Dulu Android memakai callback bersarang, lalu AsyncTask (sudah",
                    "usang sejak Android 11), lalu RxJava. Kode baru sekarang memakai",
                    "coroutine Kotlin. Coroutine adalah fungsi yang bisa berhenti",
                    "sejenak di tengah jalan, misalnya menunggu jaringan, lalu",
                    "melanjutkan lagi tanpa menahan thread. Pustakanya bernama",
                    "kotlinx.coroutines. Ia nggak termasuk pustaka standar Kotlin, dan",
                    "versi terbarunya 1.11.0 (Mei 2026).",
                ],
            },
            {
                "heading": "Padanannya di JavaScript",
                "code": """// Tiruan jaringan: Promise yang langsung selesai, supaya hasilnya pasti.
function ambilProfil(id) {
  return Promise.resolve({ id, nama: id === 7 ? 'Rina' : 'Tamu' });
}

async function muatLayar() {
  console.log('2. mulai muat');
  const profil = await ambilProfil(7);
  console.log(`4. profil datang: ${profil.nama}`);
}

console.log('1. layar tampil');
muatLayar();
console.log('3. UI tetap bisa disentuh');""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  1. layar tampil",
                    "  2. mulai muat",
                    "  3. UI tetap bisa disentuh",
                    "  4. profil datang: Rina",
                    "",
                    "await membuat muatLayar berhenti sejenak dan mengembalikan",
                    "kendali, jadi baris ketiga tercetak sebelum profilnya datang.",
                    "Kotlin melakukan hal yang sama dengan kata kunci suspend:",
                ],
            },
            {
                "heading": "Versi Kotlin",
                "bahasa": "kotlin",
                "code": """suspend fun ambilProfil(id: Int): Profil = withContext(Dispatchers.IO) {
    api.profil(id)
}

fun muatLayar() {
    viewModelScope.launch {
        val profil = ambilProfil(7)   // menunggu tanpa memblokir UI thread
        _uiState.update { it.copy(nama = profil.nama) }
    }
}""",
            },
            {
                "body": [
                    "Padanan istilahnya:",
                    "  JavaScript           Kotlin",
                    "  async function       suspend fun",
                    "  await x              panggil fungsi suspend seperti biasa",
                    "  Promise              Deferred, hasil dari async { }",
                    "  Promise.all          awaitAll",
                    "  event loop           Dispatchers.Main",
                    "",
                    "Bedanya, JavaScript cuma punya satu thread untuk kodemu, sedangkan",
                    "Kotlin di Android punya banyak. Dispatcher menentukan thread mana",
                    "yang menjalankan coroutine:",
                    "  - Dispatchers.Main untuk menyentuh tampilan.",
                    "  - Dispatchers.IO untuk menunggu disk dan jaringan.",
                    "  - Dispatchers.Default untuk hitungan berat seperti mengolah",
                    "    gambar atau mengurutkan data besar.",
                    "withContext memindahkan sepotong kode ke dispatcher lain lalu",
                    "kembali membawa hasilnya.",
                ],
            },
            {
                "heading": "Structured concurrency",
                "bahasa": "kotlin",
                "code": """viewModelScope.launch {
    val profil = async { api.profil(7) }
    val nilai = async { api.nilai(7) }
    tampilkan(profil.await(), nilai.await())   // dua permintaan jalan bersamaan
}""",
            },
            {
                "body": [
                    "Setiap coroutine hidup di dalam sebuah scope. Kalau scope-nya",
                    "dibatalkan, semua coroutine di dalamnya ikut dibatalkan. Aturan",
                    "ini disebut structured concurrency. viewModelScope dibatalkan",
                    "waktu ViewModel dibuang, jadi permintaan yang masih berjalan",
                    "untuk layar yang sudah ditutup ikut berhenti, dan hasilnya nggak",
                    "ditulis ke layar yang sudah nggak ada.",
                    "",
                    "Pembatalan terjadi di titik suspend, misalnya saat menunggu",
                    "jaringan. GlobalScope melewati aturan ini karena hidup selama",
                    "aplikasi berjalan, makanya dokumentasinya menyarankan untuk",
                    "nggak dipakai di kode biasa.",
                    "",
                    "Jebakan: menangkap catch (e: Exception) di dalam coroutine.",
                    "Pembatalan dikirim sebagai CancellationException, dan menelannya",
                    "membuat coroutine terus jalan padahal seharusnya berhenti. Tangkap",
                    "jenis galat yang memang kamu tunggu, seperti IOException.",
                ],
            },
            {
                "heading": "Flow dan StateFlow",
                "bahasa": "kotlin",
                "code": """val catatan: StateFlow<List<Catatan>> = dao.semua()   // Flow dari Room
    .map { daftar -> daftar.sortedByDescending { it.diubah } }
    .stateIn(viewModelScope, SharingStarted.WhileSubscribed(5_000), emptyList())""",
            },
            {
                "body": [
                    "Fungsi suspend mengembalikan satu nilai. Flow adalah aliran",
                    "nilai yang datang dari waktu ke waktu, misalnya isi tabel yang",
                    "berubah setiap ada catatan baru. Flow biasa bersifat dingin:",
                    "kodenya baru jalan saat ada yang mengumpulkan nilainya dengan",
                    "collect, dan jalan ulang untuk setiap pengumpul.",
                    "",
                    "StateFlow adalah Flow panas yang selalu punya nilai sekarang.",
                    "Pengumpul yang baru datang langsung menerima nilai terakhir,",
                    "makanya StateFlow cocok untuk state layar. stateIn di atas",
                    "mengubah Flow dari Room jadi StateFlow, dan WhileSubscribed(5_000)",
                    "menghentikan pengumpulan lima detik setelah layar berhenti",
                    "membaca. Lima detik itu cukup untuk melewati putar layar tanpa",
                    "mengulang query.",
                    "",
                    "LiveData adalah pendahulu StateFlow dari Jetpack dan masih ada di",
                    "banyak kode lama. Kode baru umumnya memakai StateFlow, karena ia",
                    "bagian dari coroutines dan bisa dipakai di luar Android juga.",
                    "",
                    "Sifat dingin itu berasal dari mekanisme yang sama dengan",
                    "sequence di pustaka standar Kotlin, yang juga dibangun di atas",
                    "fungsi yang bisa berhenti sejenak. Contoh ini jalan tanpa pustaka",
                    "tambahan:",
                ],
            },
            {
                "heading": "Sequence: dingin sampai dibaca",
                "bahasa": "kotlin",
                "code": """fun main() {
    val angka = sequence {
        println("  mulai menghasilkan")
        for (i in 1..3) {
            println("  hasilkan $i")
            yield(i)
        }
    }
    println("sequence dibuat, belum ada yang jalan")
    println("ambil 2 pertama: ${angka.take(2).toList()}")
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  sequence dibuat, belum ada yang jalan",
                    "    mulai menghasilkan",
                    "    hasilkan 1",
                    "    hasilkan 2",
                    "  ambil 2 pertama: [1, 2]",
                    "",
                    "Kode di dalam sequence baru jalan saat toList meminta nilainya,",
                    "dan berhenti di yield setiap kali satu nilai diserahkan. Angka 3",
                    "nggak pernah dihasilkan karena nggak ada yang memintanya. Flow",
                    "bekerja dengan cara yang mirip, cuma versinya bisa menunggu",
                    "jaringan dan pindah dispatcher.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Room dan Retrofit sama-sama mendukung fungsi suspend, dan Room",
                    "bisa mengembalikan Flow. Jadi di aplikasi Android modern, hampir",
                    "semua pekerjaan asinkron berupa coroutine di viewModelScope yang",
                    "memanggil repository, dengan hasil yang dialirkan ke layar lewat",
                    "StateFlow.",
                    "",
                    "Kasus kecil: layar rapor memanggil dua API, profil siswa dan",
                    "daftar nilai. Masing-masing butuh sekitar satu detik, dan layarnya",
                    "baru tampil setelah dua detik.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek kodenya. Dua panggilan suspend yang ditulis berurutan",
                    "     memang berjalan berurutan: yang kedua menunggu yang pertama.",
                    "  2. Karena dua permintaan itu nggak saling bergantung, jalankan",
                    "     bersamaan dengan async:",
                    "       val profil = async { api.profil(id) }",
                    "       val nilai = async { api.nilai(id) }",
                    "       tampilkan(profil.await(), nilai.await())",
                    "  3. Tetap jalankan di dalam viewModelScope, supaya keduanya ikut",
                    "     batal kalau pengguna keluar dari layar rapor.",
                    "  4. Tangkap IOException untuk memberi pesan galat, tanpa menelan",
                    "     CancellationException.",
                ],
            },
        ],
    },
    {
        "title": "14. Room: Database Lokal di Android",
        "sections": [
            {
                "body": [
                    "Aplikasi yang tetap jalan tanpa sinyal terasa jauh lebih enak",
                    "dipakai, apalagi di kereta atau di daerah yang jaringannya putus",
                    "sambung. Caranya, data disimpan di HP dulu, lalu dikirim ke",
                    "server saat internet ada. Pola ini disebut offline-first.",
                    "",
                    "Android sudah membawa SQLite, database kecil yang tersimpan",
                    "sebagai satu berkas. Room adalah lapisan di atas SQLite dari",
                    "Jetpack. Room memeriksa query SQL-mu saat kompilasi, mengubah",
                    "baris tabel jadi objek Kotlin, dan mendukung fungsi suspend serta",
                    "Flow. Versi stabil terbarunya 2.8.5 (September 2026). Sejak",
                    "seri 2.7, Room juga jadi pustaka Kotlin Multiplatform yang jalan",
                    "di Android, iOS, dan desktop JVM.",
                    "",
                    "Materi ini menganggap kamu sudah kenal SQL dasar dari kurikulum",
                    "SQL: CREATE TABLE, INSERT, SELECT, dan ALTER TABLE.",
                ],
            },
            {
                "heading": "Entity, DAO, dan Database",
                "bahasa": "kotlin",
                "code": """@Entity(tableName = "catatan")
data class Catatan(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val judul: String,
    val isi: String,
    val diubah: Long,
)

@Dao
interface CatatanDao {
    @Query("SELECT * FROM catatan ORDER BY diubah DESC")
    fun semua(): Flow<List<Catatan>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun simpan(catatan: Catatan)

    @Query("DELETE FROM catatan WHERE id = :id")
    suspend fun hapus(id: Long)
}

@Database(entities = [Catatan::class], version = 1)
abstract class DatabaseAplikasi : RoomDatabase() {
    abstract fun catatanDao(): CatatanDao
}

// sekali saja untuk seluruh aplikasi
val db = Room.databaseBuilder(context, DatabaseAplikasi::class.java, "catatan.db")
    .build()""",
            },
            {
                "body": [
                    "Room terdiri dari tiga bagian:",
                    "  - Entity: data class yang mewakili satu tabel. Tiap properti",
                    "    jadi kolom.",
                    "  - DAO (Data Access Object): interface berisi query. Room",
                    "    membuatkan isinya waktu build lewat KSP, alat pembangkit kode",
                    "    untuk Kotlin. Kalau ada nama kolom yang salah ketik di",
                    "    @Query, build-nya gagal, jadi kesalahannya ketahuan sebelum",
                    "    aplikasi jalan.",
                    "  - Database: kelas abstrak yang merangkai Entity dan DAO, dan",
                    "    mencatat nomor versi skema.",
                    "",
                    "Fungsi semua() mengembalikan Flow. Setiap kali isi tabel",
                    "berubah, Flow itu mengirim daftar terbaru, jadi layar yang",
                    "membacanya selalu mutakhir tanpa kamu memanggil query lagi.",
                    "",
                    "Tabel yang dibuat Room untuk Entity di atas kurang lebih seperti",
                    "di bawah. Program SQL ini bisa kamu jalankan di aplikasi ini.",
                ],
            },
            {
                "heading": "Tabel di balik Entity",
                "bahasa": "sql",
                "code": """CREATE TABLE catatan (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  judul TEXT NOT NULL,
  isi TEXT NOT NULL,
  diubah INTEGER NOT NULL
);
INSERT INTO catatan (judul, isi, diubah) VALUES ('Belanja', 'telur, beras', 100);
INSERT INTO catatan (judul, isi, diubah) VALUES ('PKL', 'laporan minggu 3', 200);
SELECT id, judul FROM catatan ORDER BY diubah DESC;""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  2|PKL",
                    "  1|Belanja",
                    "",
                    "Kolom yang tipenya String di Kotlin jadi TEXT NOT NULL, karena",
                    "String tanpa tanda tanya nggak boleh null. Long jadi INTEGER.",
                    "Catatan dengan nilai diubah terbesar tampil paling atas, sama",
                    "seperti query di DAO.",
                ],
            },
            {
                "heading": "Kenapa Room menolak query di UI thread",
                "body": [
                    "Kalau kamu memanggil fungsi DAO biasa (bukan suspend) dari UI",
                    "thread, aplikasinya berhenti dengan pesan:",
                    "  Cannot access database on the main thread since it may",
                    "  potentially lock the UI for a long period of time.",
                    "",
                    "Room sengaja menolaknya, karena membaca disk bisa lama dan",
                    "membekukan layar. Jalan keluarnya ada di DAO tadi: tandai fungsi",
                    "tulis dengan suspend dan kembalikan Flow untuk fungsi baca. Room",
                    "lalu menjalankan query-nya di thread miliknya sendiri. Ada",
                    "allowMainThreadQueries() di builder, tapi itu cuma untuk uji",
                    "otomatis, jangan dipakai di aplikasi.",
                ],
            },
            {
                "heading": "Migrasi saat skema berubah",
                "bahasa": "kotlin",
                "code": """@Database(entities = [Catatan::class], version = 2)
abstract class DatabaseAplikasi : RoomDatabase() { /* ... */ }

val MIGRASI_1_2 = object : Migration(1, 2) {
    override fun migrate(db: SupportSQLiteDatabase) {
        db.execSQL("ALTER TABLE catatan ADD COLUMN favorit INTEGER NOT NULL DEFAULT 0")
    }
}

Room.databaseBuilder(context, DatabaseAplikasi::class.java, "catatan.db")
    .addMigrations(MIGRASI_1_2)
    .build()""",
            },
            {
                "body": [
                    "Misalnya versi kedua aplikasimu menambah kolom favorit ke",
                    "Entity. Di HP pengguna sudah ada berkas catatan.db versi 1 yang",
                    "berisi catatan mereka. Kalau nomor versi dinaikkan tanpa migrasi,",
                    "aplikasinya berhenti saat dibuka dengan pesan yang diawali A",
                    "migration from 1 to 2 was required but not found.",
                    "",
                    "Migrasi adalah resep mengubah skema lama jadi skema baru tanpa",
                    "membuang data. Untuk perubahan sederhana seperti kolom baru, Room",
                    "juga bisa membuat migrasinya sendiri lewat autoMigrations di",
                    "anotasi @Database, asalkan skema tiap versi diekspor ke berkas",
                    "JSON di proyek.",
                    "",
                    "Jebakan: memakai fallbackToDestructiveMigration supaya errornya",
                    "hilang. Pilihan itu membuat Room menghapus seluruh database lama",
                    "dan membuatnya dari nol. Error-nya memang hilang, catatan",
                    "pengguna juga.",
                    "",
                    "Program SQL di bawah meniru isi migrasi tadi. Data lama tetap",
                    "ada, dan kolom barunya terisi nilai bawaan.",
                ],
            },
            {
                "heading": "Migrasi dalam SQL",
                "bahasa": "sql",
                "code": """CREATE TABLE catatan (id INTEGER PRIMARY KEY, judul TEXT NOT NULL);
INSERT INTO catatan (judul) VALUES ('Belanja');
-- versi 2: kolom baru, data lama tetap ada
ALTER TABLE catatan ADD COLUMN favorit INTEGER NOT NULL DEFAULT 0;
INSERT INTO catatan (judul, favorit) VALUES ('PKL', 1);
SELECT id, judul, favorit FROM catatan;""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  1|Belanja|0",
                    "  2|PKL|1",
                    "",
                    "Jebakan: membuat beberapa objek database dengan",
                    "Room.databaseBuilder di banyak tempat. Tiap objek membuka",
                    "koneksinya sendiri ke berkas yang sama. Buat sekali untuk seluruh",
                    "aplikasi, lalu bagikan. Materi Hilt menunjukkan cara rapinya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi catatan, kasir, dan pembaca berita yang tetap bisa",
                    "dibuka tanpa sinyal biasanya menyimpan datanya di SQLite. Di",
                    "Android, Room adalah cara yang disarankan dokumentasi resmi untuk",
                    "itu, dan codelab resmi Android Basics with Compose punya bab",
                    "khusus tentang Room.",
                    "",
                    "Kasus kecil: aplikasi kasir warung harus tetap mencatat",
                    "penjualan saat internet mati. Versi kedua aplikasinya menambah",
                    "kolom diskon di setiap transaksi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat Entity Transaksi dengan kolom id, barang, jumlah, harga,",
                    "     waktu, dan terkirim (0 atau 1) untuk menandai mana yang sudah",
                    "     masuk server.",
                    "  2. Setiap penjualan disimpan lewat DAO dengan fungsi suspend,",
                    "     dan layar membaca daftar transaksi lewat Flow.",
                    "  3. Saat internet kembali, kirim transaksi yang terkirim = 0,",
                    "     lalu tandai jadi 1. WorkManager cocok untuk pengiriman ini.",
                    "  4. Untuk versi kedua, naikkan versi database jadi 2 dan tulis",
                    "     migrasinya:",
                    "       ALTER TABLE transaksi ADD COLUMN diskon INTEGER NOT NULL DEFAULT 0",
                    "  5. Uji migrasi dengan memasang versi 1, mengisi beberapa",
                    "     transaksi, lalu memasang versi 2 di atasnya. Transaksi lama",
                    "     harus masih ada.",
                ],
            },
        ],
    },
    {
        "title": "15. Retrofit dan OkHttp: Bicara dengan API",
        "sections": [
            {
                "body": [
                    "Kebanyakan aplikasi mengambil datanya dari server lewat HTTP.",
                    "Server menyediakan API: alamat seperti /produk atau /pesanan yang",
                    "menjawab dengan data JSON. Di Android, dua pustaka dari Square",
                    "paling sering dipakai untuk urusan ini:",
                    "  - OkHttp adalah klien HTTP. Ia mengurus koneksi, HTTP/2, cache,",
                    "    dan interceptor. Versi terbarunya 5.5.0 (Agustus 2026).",
                    "  - Retrofit dibangun di atas OkHttp. Kamu menulis interface",
                    "    berisi anotasi, dan Retrofit membuatkan kode yang mengirim",
                    "    permintaannya. Versi terbarunya 3.0.0 (Mei 2025).",
                    "",
                    "Untuk mengubah JSON jadi objek Kotlin, Retrofit memakai konverter.",
                    "Pilihan yang umum adalah kotlinx.serialization dari JetBrains;",
                    "kode lama sering memakai Moshi atau Gson. Jangan lupa, aplikasi",
                    "yang memakai internet wajib meminta izin internet di manifest.",
                ],
            },
            {
                "heading": "Interface Retrofit",
                "bahasa": "kotlin",
                "code": """@Serializable
data class Produk(val id: Int, val nama: String, val harga: Int)

interface TokoApi {
    @GET("produk")
    suspend fun daftarProduk(@Query("kategori") kategori: String): List<Produk>

    @GET("produk/{id}")
    suspend fun produk(@Path("id") id: Int): Produk

    @POST("pesanan")
    suspend fun pesan(@Body pesanan: Pesanan): HasilPesanan
}""",
            },
            {
                "body": [
                    "Tiap fungsi mewakili satu permintaan. @GET(\"produk/{id}\")",
                    "dengan @Path(\"id\") menghasilkan alamat seperti produk/7.",
                    "@Query(\"kategori\") menambahkan ?kategori=minuman di belakang",
                    "alamat. @Body mengubah objek Kotlin jadi isi JSON permintaan.",
                    "Karena fungsinya suspend, kamu memanggilnya dari coroutine",
                    "seperti fungsi biasa.",
                ],
            },
            {
                "heading": "Merakit klien",
                "bahasa": "kotlin",
                "code": """val okHttp = OkHttpClient.Builder()
    .addInterceptor(TokenInterceptor(penyimpanToken))
    .addInterceptor(HttpLoggingInterceptor().apply {
        level = HttpLoggingInterceptor.Level.BASIC
    })
    .build()

val api: TokoApi = Retrofit.Builder()
    .baseUrl("https://api.toko-contoh.id/")
    .client(okHttp)
    .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
    .build()
    .create(TokoApi::class.java)""",
            },
            {
                "body": [
                    "Jebakan: baseUrl wajib diakhiri garis miring. Tanpa garis miring",
                    "itu, Retrofit menolak dengan pesan baseUrl must end in /.",
                    "",
                    "Satu OkHttpClient sebaiknya dibuat sekali dan dipakai bersama,",
                    "karena ia menyimpan kumpulan koneksi dan cache. Membuat klien",
                    "baru di tiap permintaan membuang semua itu.",
                ],
            },
            {
                "heading": "Interceptor",
                "bahasa": "kotlin",
                "code": """class TokenInterceptor(private val token: PenyimpanToken) : Interceptor {
    override fun intercept(chain: Interceptor.Chain): Response {
        val permintaan = chain.request().newBuilder()
            .header("Authorization", "Bearer ${token.ambil()}")
            .build()
        return chain.proceed(permintaan)
    }
}""",
            },
            {
                "body": [
                    "Interceptor adalah fungsi yang dilewati setiap permintaan sebelum",
                    "sampai ke server, dan setiap respons sebelum sampai ke kodemu.",
                    "Interceptor dipasang berderet seperti rantai. Masing-masing boleh",
                    "mengubah permintaan, meneruskannya dengan chain.proceed, mengubah",
                    "responsnya, atau langsung mengembalikan respons sendiri tanpa",
                    "meneruskan, misalnya dari cache. Pola ini disebut chain of",
                    "responsibility.",
                    "",
                    "TokenInterceptor di atas menempelkan token login ke semua",
                    "permintaan, jadi fungsi di TokoApi nggak perlu mengurus token",
                    "satu per satu. OkHttp membedakan addInterceptor, yang dijalankan",
                    "sekali per panggilan, dan addNetworkInterceptor, yang dijalankan",
                    "untuk setiap permintaan jaringan sungguhan termasuk pengalihan.",
                    "",
                    "Urutan pemasangan berpengaruh. Tiruan di bawah memakai dua",
                    "interceptor yang sama dengan urutan berbeda.",
                ],
            },
            {
                "heading": "Tiruan rantai interceptor",
                "code": """// Tiruan rantai interceptor ala OkHttp, tanpa jaringan.
function rantai(interceptors, server) {
  const jalan = (i, req) => (i === interceptors.length
    ? server(req)
    : interceptors[i]({ request: req, proceed: (r) => jalan(i + 1, r) }));
  return (req) => jalan(0, req);
}

const token = (chain) => chain.proceed({
  ...chain.request,
  header: { ...chain.request.header, Authorization: 'Bearer abc123' },
});

const logging = (chain) => {
  const nama = Object.keys(chain.request.header).join(', ') || '-';
  console.log(`--> GET ${chain.request.url}  header: ${nama}`);
  const res = chain.proceed(chain.request);
  console.log(`<-- ${res.kode} ${chain.request.url}`);
  return res;
};

const server = (req) => ({ kode: req.header.Authorization ? 200 : 401 });

console.log('urutan [token, logging]:');
rantai([token, logging], server)({ url: '/produk', header: {} });
console.log('urutan [logging, token]:');
rantai([logging, token], server)({ url: '/produk', header: {} });""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  urutan [token, logging]:",
                    "  --> GET /produk  header: Authorization",
                    "  <-- 200 /produk",
                    "  urutan [logging, token]:",
                    "  --> GET /produk  header: -",
                    "  <-- 200 /produk",
                    "",
                    "Dua-duanya berhasil, tapi log kedua nggak memperlihatkan header",
                    "token, karena logging berjalan sebelum token ditempel. Waktu",
                    "kamu mencari kenapa server menolak permintaan, log yang kedua",
                    "bisa menyesatkan.",
                ],
            },
            {
                "heading": "Galat dan alat bantu",
                "body": [
                    "Ada dua jenis kegagalan yang perlu ditangani. IOException muncul",
                    "kalau jaringan putus atau server nggak terjangkau. HttpException",
                    "muncul kalau server menjawab dengan kode di luar 2xx, misalnya",
                    "404 atau 500. Tangkap keduanya di repository atau ViewModel,",
                    "lalu ubah jadi pesan galat di UiState.",
                    "",
                    "Dua hal yang sering membingungkan pemula:",
                    "  - Sejak Android 9, aplikasi yang targetSdk-nya 28 ke atas",
                    "    menolak alamat http:// biasa secara bawaan. Pakai https://.",
                    "  - Di emulator, localhost menunjuk ke emulator itu sendiri.",
                    "    Server yang jalan di laptopmu dicapai lewat alamat 10.0.2.2.",
                    "",
                    "Ada tiga pustaka pendamping yang sering kamu temui di proyek",
                    "Android. Chucker menampilkan semua permintaan HTTP di dalam",
                    "aplikasi versi debug. Timber membungkus log supaya gampang",
                    "dimatikan di versi rilis. LeakCanary mendeteksi objek yang",
                    "tertahan di memori. Untuk proyek Kotlin Multiplatform, pilihan",
                    "klien HTTP yang umum adalah Ktor Client dari JetBrains, karena",
                    "jalan di Android dan iOS sekaligus.",
                    "",
                    "Jebakan: menaruh kunci API rahasia di kode aplikasi. APK bisa",
                    "dibongkar siapa pun yang mengunduhnya, jadi rahasia yang ikut",
                    "terkirim ke HP pengguna bukan rahasia lagi. Simpan rahasia di",
                    "server, dan biarkan aplikasi cuma memegang token login",
                    "pengguna.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Codelab resmi Android tentang mengambil data dari internet",
                    "memakai Retrofit dengan kotlinx.serialization, dan banyak",
                    "lowongan Android di Indonesia mencantumkan Retrofit sebagai",
                    "syarat. Pola token di interceptor dipakai hampir semua aplikasi",
                    "yang punya fitur login.",
                    "",
                    "Kasus kecil: semua endpoint API sekolah butuh token. Token itu",
                    "kedaluwarsa setiap jam, dan setelahnya semua permintaan dijawab",
                    "401 sampai pengguna login ulang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tempel token di satu tempat saja, yaitu TokenInterceptor,",
                    "     supaya fungsi di interface API tetap bersih.",
                    "  2. Untuk jawaban 401, pasang Authenticator milik OkHttp. Ia",
                    "     dipanggil otomatis setiap kali server menjawab 401, dan",
                    "     boleh mengembalikan permintaan baru dengan token yang sudah",
                    "     diperbarui:",
                    "       OkHttpClient.Builder().authenticator(PenyegarToken(repo))",
                    "  3. Di dalam Authenticator, minta token baru ke server dengan",
                    "     refresh token. Kalau itu juga gagal, kembalikan null supaya",
                    "     OkHttp berhenti mencoba, lalu arahkan pengguna ke layar",
                    "     login.",
                    "  4. Pasang HttpLoggingInterceptor di build debug saja, karena",
                    "     lognya memuat header termasuk token.",
                ],
            },
        ],
    },
    {
        "title": "16. Hilt dan Dependency Injection",
        "sections": [
            {
                "body": [
                    "Bayangkan CatatanViewModel membuat sendiri semua yang ia",
                    "butuhkan: objek Retrofit, OkHttpClient, database Room, lalu",
                    "repository. Kodenya jalan, tapi tiga masalah muncul. Setiap",
                    "ViewModel membuat database dan klien HTTP-nya sendiri. Mengganti",
                    "server sungguhan dengan server tiruan untuk diuji berarti",
                    "mengubah isi ViewModel. Dan susunan objeknya tersebar di banyak",
                    "berkas.",
                    "",
                    "Dependency injection (DI) membalik caranya. Sebuah kelas menerima",
                    "apa yang ia butuhkan dari luar, biasanya lewat konstruktor, dan",
                    "nggak membuatnya sendiri. Kebutuhan itu disebut dependensi.",
                    "Mirip tukang yang datang dan dibawakan alatnya, jadi ia nggak",
                    "perlu membuat palu sendiri sebelum bisa bekerja.",
                ],
            },
            {
                "heading": "DI tanpa pustaka apa pun",
                "bahasa": "kotlin",
                "code": """interface SumberCatatan {
    fun semua(): List<String>
}

class SumberPalsu : SumberCatatan {
    override fun semua() = listOf("Belanja", "PKL minggu 3")
}

class SumberKosong : SumberCatatan {
    override fun semua() = emptyList<String>()
}

class CatatanRepository(private val sumber: SumberCatatan) {
    fun jumlah() = sumber.semua().size
}

class CatatanViewModel(private val repo: CatatanRepository) {
    fun judulLayar() =
        if (repo.jumlah() == 0) "Belum ada catatan" else "Catatanku (${repo.jumlah()})"
}

fun main() {
    // Satu tempat yang merakit semua objek: kontainer manual.
    val vm = CatatanViewModel(CatatanRepository(SumberPalsu()))
    println(vm.judulLayar())

    // Mengganti sumber nggak perlu menyentuh ViewModel sama sekali.
    val vmKosong = CatatanViewModel(CatatanRepository(SumberKosong()))
    println(vmKosong.judulLayar())
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  Catatanku (2)",
                    "  Belum ada catatan",
                    "",
                    "Itulah DI dalam bentuk paling sederhana, dan program ini bisa",
                    "kamu jalankan. CatatanViewModel cuma tahu ia butuh",
                    "CatatanRepository. Ia nggak tahu datanya datang dari mana. Fungsi",
                    "main menjadi kontainer manual: satu tempat yang merakit semua",
                    "objek. Di aplikasi kecil, kontainer manual seperti ini sudah",
                    "cukup. Begitu objeknya puluhan, merakitnya dengan tangan mulai",
                    "melelahkan, dan di situlah pustaka DI membantu.",
                ],
            },
            {
                "heading": "Hilt",
                "bahasa": "kotlin",
                "code": """@HiltAndroidApp
class AplikasiCatatan : Application()

@AndroidEntryPoint
class MainActivity : ComponentActivity() { /* setContent { ... } */ }

@HiltViewModel
class CatatanViewModel @Inject constructor(
    private val repo: CatatanRepository
) : ViewModel()

class CatatanRepository @Inject constructor(
    private val dao: CatatanDao,
    private val api: TokoApi,
)

@Module
@InstallIn(SingletonComponent::class)
object ModulData {
    @Provides @Singleton
    fun database(@ApplicationContext context: Context): DatabaseAplikasi =
        Room.databaseBuilder(context, DatabaseAplikasi::class.java, "catatan.db").build()

    @Provides
    fun catatanDao(db: DatabaseAplikasi): CatatanDao = db.catatanDao()
}

// di composable: val vm: CatatanViewModel = hiltViewModel()""",
            },
            {
                "body": [
                    "Hilt adalah pustaka DI resmi Android, dibangun di atas Dagger.",
                    "Versi terbarunya Dagger/Hilt 2.60.1 (Juli 2026), dengan pustaka",
                    "pendamping androidx.hilt 1.4.0. Hilt membaca anotasi saat build",
                    "lalu membangkitkan kode perakitnya, sama seperti Room memakai",
                    "KSP. Cara membaca contoh di atas:",
                    "  - @HiltAndroidApp di kelas Application menyalakan Hilt untuk",
                    "    seluruh aplikasi.",
                    "  - @AndroidEntryPoint menandai Activity yang boleh menerima",
                    "    objek dari Hilt.",
                    "  - @Inject constructor memberi tahu Hilt cara membuat sebuah",
                    "    kelas: panggil konstruktornya dengan dependensi yang ia minta.",
                    "  - @Module dengan @Provides dipakai untuk objek yang nggak bisa",
                    "    diberi @Inject, misalnya database Room yang dibuat lewat",
                    "    builder, atau kelas dari pustaka lain.",
                    "  - @HiltViewModel membuat ViewModel bisa diambil dengan",
                    "    hiltViewModel() di composable, lengkap dengan dependensinya.",
                ],
            },
            {
                "heading": "Dibuat sekali atau tiap kali",
                "body": [
                    "Secara bawaan, Hilt membuat objek baru setiap kali objek itu",
                    "dibutuhkan. Anotasi @Singleton di dalam SingletonComponent",
                    "membuatnya dibuat sekali untuk seluruh aplikasi. Database Room",
                    "dan OkHttpClient sebaiknya singleton karena mahal dibuat dan",
                    "menyimpan koneksi. DAO murah dibuat, jadi boleh dibuat tiap kali",
                    "diminta. Ada juga cakupan lain seperti @ViewModelScoped, yang",
                    "berarti satu objek untuk satu ViewModel.",
                    "",
                    "Kalau ada dependensi yang lupa disediakan, Hilt menolak saat",
                    "build, sebelum aplikasi jalan. Pesannya panjang, tapi baris",
                    "pertamanya biasanya cukup jelas:",
                    "  [Dagger/MissingBinding] CatatanDao cannot be provided without",
                    "  an @Provides-annotated method.",
                    "Di bawahnya ada rantai is injected at yang menunjukkan siapa yang",
                    "meminta objek itu. Kalau dua kelas saling membutuhkan, pesannya",
                    "berawal [Dagger/DependencyCycle].",
                ],
            },
            {
                "heading": "Koin dan Kodein",
                "bahasa": "kotlin",
                "code": """val modulAplikasi = module {
    single { Room.databaseBuilder(get(), DatabaseAplikasi::class.java, "catatan.db").build() }
    single { get<DatabaseAplikasi>().catatanDao() }
    single { CatatanRepository(get(), get()) }
    viewModel { CatatanViewModel(get()) }
}""",
            },
            {
                "body": [
                    "Koin adalah alternatif yang populer, terutama di proyek Kotlin",
                    "Multiplatform. Koin nggak membangkitkan kode saat build. Ia",
                    "merakit objek saat aplikasi jalan, berdasarkan modul yang kamu",
                    "tulis dengan DSL Kotlin seperti di atas. Akibatnya build lebih",
                    "cepat dan pengaturannya lebih ringkas, tapi dependensi yang lupa",
                    "didaftarkan baru ketahuan saat aplikasi jalan, bukan saat build.",
                    "Kodein bekerja dengan cara serupa dan lebih jarang ditemui.",
                    "",
                    "Ringkasnya:",
                    "  manual   paling sederhana, cocok untuk aplikasi kecil",
                    "  Hilt     galat ketahuan saat build, disarankan Google",
                    "  Koin     ringkas, galat ketahuan saat aplikasi jalan, umum",
                    "           di Kotlin Multiplatform",
                    "",
                    "Jebakan: menyuntikkan Context milik Activity ke objek",
                    "singleton. Singleton hidup selama aplikasi, jadi Activity itu",
                    "ikut tertahan di memori. Untuk singleton, pakai",
                    "@ApplicationContext seperti di ModulData.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Keuntungan DI paling terasa saat menguji. Hilt punya anotasi",
                    "@TestInstallIn untuk mengganti modul sungguhan dengan modul",
                    "tiruan di uji otomatis, sehingga uji nggak perlu menyentuh server",
                    "asli. Itu yang dipakai tim Android untuk menguji layar yang",
                    "biasanya butuh internet.",
                    "",
                    "Kasus kecil: kamu ingin menguji CatatanViewModel, tapi setiap",
                    "uji gagal kalau laptopnya offline, karena ViewModel membuat",
                    "Retrofit sendiri dan memanggil server sungguhan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Ubah ViewModel supaya menerima CatatanRepository lewat",
                    "     konstruktor, bukan membuatnya sendiri.",
                    "  2. Jadikan sumber data sebuah interface, lalu tulis versi",
                    "     tiruannya yang mengembalikan data tetap:",
                    "       class ApiPalsu : TokoApi { /* kembalikan daftar tetap */ }",
                    "  3. Di uji unit biasa, rakit ViewModel dengan tangan memakai",
                    "     ApiPalsu, persis seperti fungsi main di contoh manual.",
                    "  4. Untuk uji yang menjalankan seluruh aplikasi dengan Hilt,",
                    "     ganti modul jaringan dengan @TestInstallIn yang menyediakan",
                    "     ApiPalsu.",
                    "  5. Jalankan ujinya dengan Wi-Fi mati. Kalau masih lulus, uji",
                    "     itu sudah lepas dari server.",
                ],
            },
        ],
    },
    {
        "title": "17. Swift Sekilas untuk Pelajar Kotlin",
        "sections": [
            {
                "body": [
                    "Swift adalah bahasa resmi Apple untuk aplikasi iPhone, iPad, Mac,",
                    "Apple Watch, dan Vision Pro. Apple memperkenalkannya tahun 2014",
                    "sebagai pengganti Objective-C, lalu membukanya jadi open source di",
                    "akhir 2015 dengan lisensi Apache 2.0. Versi stabil terbaru saat",
                    "materi ini ditulis (Oktober 2026) adalah Swift 6.4, rilis 15",
                    "September 2026, dengan patch 6.4.1 di halaman unduhan swift.org.",
                    "",
                    "Kalau kamu sudah menamatkan kurikulum Kotlin, kamu bakal merasa",
                    "akrab. Kotlin dan Swift lahir di masa yang hampir sama dan mengejar",
                    "hal yang mirip: kode yang lebih pendek dari Java atau Objective-C,",
                    "dan null yang dicek sebelum program jalan. Di Survei Stack Overflow",
                    "2025, Swift dipakai 5,4% responden dan Kotlin 10,8%.",
                    "",
                    "Soal laptopmu: bahasa Swift dan pustaka standarnya bisa dipasang di",
                    "Linux. Yang nggak bisa jalan di Linux adalah Xcode dan framework",
                    "layar iPhone (SwiftUI dan UIKit, materi berikutnya). Jadi materi ini",
                    "fokus ke membaca dan menulis Swift-nya dulu, lewat padanan yang udah",
                    "kamu kenal di Kotlin.",
                ],
            },
            {
                "heading": "Kode Swift pertama",
                "bahasa": "swift",
                "code": "let nama = \"Rina\"          // seperti val di Kotlin\nvar poin = 10              // seperti var\npoin += 5\n\nfunc sapa(pelanggan: String, poin: Int) -> String {\n    return \"Halo \\(pelanggan), poinmu \\(poin)\"\n}\n\nprint(sapa(pelanggan: nama, poin: poin))\n// Halo Rina, poinmu 15",
            },
            {
                "body": [
                    "Baca baris demi baris sambil membayangkan versi Kotlin-nya:",
                    "",
                    "  - let sama dengan val, var sama dengan var. Tipe ditebak dari",
                    "    nilainya, jadi nama otomatis String dan poin otomatis Int.",
                    "  - Fungsi ditulis func, bukan fun. Tipe kembaliannya ditulis",
                    "    sesudah panah ->, sedangkan Kotlin memakai titik dua.",
                    "  - Interpolasi string memakai \\(nama). Kotlin memakai $nama.",
                    "  - Nggak ada titik koma, dan berkas skrip nggak butuh fungsi main.",
                    "",
                    "Yang paling sering bikin kaget orang Kotlin adalah label argumen.",
                    "Saat memanggil sapa, kamu wajib menulis pelanggan: dan poin:. Di",
                    "Kotlin, menyebut nama argumen itu pilihan. Di Swift, nama itu bagian",
                    "dari fungsinya. Kalau mau dipanggil tanpa label, penulis fungsinya",
                    "memberi garis bawah: func sapa(_ nama: String).",
                ],
            },
            {
                "heading": "Optional: padanan tipe nullable",
                "bahasa": "swift",
                "code": "func cariNama(id: Int) -> String? {\n    id == 1 ? \"Rina\" : nil\n}\n\nlet nama = cariNama(id: 2)      // tipenya String?\n\nif let n = nama {\n    print(\"Halo, \\(n)\")\n} else {\n    print(\"Nama nggak ketemu\")\n}\n\nprint(nama ?? \"tamu\")           // tamu\nprint(nama?.count ?? 0)         // 0\n\nfunc sapa(_ nama: String?) {\n    guard let nama else {\n        print(\"Siapa ini?\")\n        return\n    }\n    print(\"Halo, \\(nama)\")        // di sini nama pasti String\n}",
            },
            {
                "body": [
                    "Swift menyebut nilai kosong nil, bukan null. Tipe yang boleh kosong",
                    "diberi tanda tanya, persis seperti Kotlin: String? boleh nil, String",
                    "nggak boleh. Operator ?. dan ?? juga sama artinya. Bedanya ada di",
                    "cara membuka isinya:",
                    "",
                    "  - if let n = nama membuka optional kalau isinya ada. Di dalam",
                    "    kurungnya, n sudah pasti String. Ini padanan smart cast Kotlin",
                    "    sesudah if (nama != null).",
                    "  - guard let membalik urutannya: kalau kosong, keluar dulu dari",
                    "    fungsi. Sisa fungsi bebas memakai nama tanpa tanda tanya.",
                    "  - Tanda seru nama! memaksa membuka isi, padanan nama!! di Kotlin.",
                    "    Kalau isinya nil, aplikasi langsung berhenti.",
                    "",
                    "Sekarang soal yang beda betulan dari Kotlin. Swift punya dua jenis",
                    "tipe buatan sendiri: struct dan class. Struct adalah tipe nilai,",
                    "artinya setiap kali disalin ke variabel lain, isinya ikut digandakan.",
                    "Class adalah tipe referensi: yang disalin cuma alamatnya, jadi dua",
                    "variabel menunjuk objek yang sama. Kotlin cuma punya yang kedua.",
                ],
            },
            {
                "heading": "struct dan class",
                "bahasa": "swift",
                "code": """struct Titik {
    var x: Int
    var y: Int
}

class Akun {
    var saldo: Int
    init(saldo: Int) { self.saldo = saldo }
}

var a = Titik(x: 1, y: 2)
var b = a                  // b salinan baru
b.x = 10
print(a.x, b.x)            // 1 10

let akun1 = Akun(saldo: 100)
let akun2 = akun1          // menunjuk objek yang sama
akun2.saldo = 50
print(akun1.saldo, akun2.saldo)  // 50 50""",
            },
            {
                "heading": "Perilaku yang sama, ditiru di JavaScript",
                "code": """// Objek JavaScript dibagi lewat referensi, mirip class di Swift.
const akun1 = { saldo: 100 };
const akun2 = akun1;
akun2.saldo = 50;
console.log('mirip class:', akun1.saldo, akun2.saldo);

// Salinan dengan spread meniru struct: tiap variabel punya isinya sendiri.
const a = { x: 1, y: 2 };
const b = { ...a };
b.x = 10;
console.log('mirip struct:', a.x, b.x);""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  mirip class: 50 50",
                    "  mirip struct: 1 10",
                    "",
                    "Apple menyarankan struct sebagai pilihan awal, dan class dipakai",
                    "kalau kamu memang butuh satu objek yang dibagi banyak bagian program.",
                    "String, Array, dan Dictionary di Swift juga tipe nilai. Jadi kalau",
                    "kamu mengirim array ke fungsi lalu fungsinya mengubah salinannya,",
                    "array aslimu nggak ikut berubah.",
                    "",
                    "Closure di Swift mirip lambda Kotlin. Bentuk singkatnya memakai $0",
                    "untuk argumen pertama, padanan it di Kotlin:",
                    "",
                    "  let harga = [12000, 8000, 25000]",
                    "  let mahal = harga.filter { $0 > 10000 }    // [12000, 25000]",
                    "  let label = harga.map { h in \"Rp\\(h)\" }",
                    "",
                    "Swift juga punya async/await sejak versi 5.5, mirip suspend di",
                    "Kotlin. Swift 6 menambah pemeriksaan data race saat kompilasi: kode",
                    "yang membiarkan dua thread mengubah data yang sama tanpa pengaman",
                    "ditolak compiler. Kode lama sering memunculkan banyak peringatan",
                    "waktu pertama kali dipindah ke mode bahasa Swift 6.",
                ],
            },
            {
                "heading": "Memasang Swift di Linux",
                "bahasa": "terminal",
                "code": """curl -O https://download.swift.org/swiftly/linux/swiftly-$(uname -m).tar.gz
tar zxf swiftly-$(uname -m).tar.gz
./swiftly init --quiet-shell-followup
. "${SWIFTLY_HOME_DIR:-$HOME/.local/share/swiftly}/env.sh"
hash -r
swift --version

mkdir halo-swift && cd halo-swift
swift package init --type executable
swift run""",
            },
            {
                "body": [
                    "Perintah di atas diambil dari halaman swift.org/install. Alat",
                    "pasangnya bernama swiftly, yang juga bisa mengganti versi Swift dan",
                    "mengunduh pembaruan. Cek dulu daftar distro yang didukung di halaman",
                    "itu. Kalau versi Fedora-mu belum tercantum, Swift juga tersedia",
                    "sebagai image kontainer resmi di Docker Hub.",
                    "",
                    "Jebakan: tanda seru terasa praktis karena error kompilasinya hilang.",
                    "Tapi setiap ! adalah janji bahwa nilainya nggak mungkin nil. Kalau",
                    "janji itu meleset, aplikasi berhenti di tangan pengguna, dan di",
                    "iPhone itu kelihatan sebagai aplikasi yang tiba-tiba tertutup.",
                    "",
                    "Jebakan: struct yang disimpan di let nggak bisa diubah isinya,",
                    "termasuk properti var di dalamnya. Ini beda dengan class: properti",
                    "var milik class tetap bisa diubah walaupun variabelnya let, seperti",
                    "akun2.saldo = 50 di contoh tadi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tim yang punya aplikasi Android dan iOS native biasanya merawat dua",
                    "basis kode: Kotlin untuk Android dan Swift untuk iOS, kadang dengan",
                    "sisa Objective-C di bagian lama. Programmer Android sering diminta",
                    "ikut membaca kode Swift saat ada bug yang muncul di dua platform.",
                    "",
                    "Kasus kecil: aplikasi iOS kantormu tertutup sendiri setiap kali",
                    "profil pengguna tanpa foto dibuka. Versi Android-nya aman. Kamu",
                    "menemukan baris ini di kode Swift:",
                    "",
                    "  let url = URL(string: pengguna.fotoUrl!)!",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari semua tanda ! di baris itu. Ada dua: satu membuka",
                    "     fotoUrl, satu lagi membuka hasil URL(string:), yang juga",
                    "     optional karena teksnya bisa bukan alamat yang sah.",
                    "  2. Cek tipe fotoUrl. Kalau String?, pengguna tanpa foto punya",
                    "     nil di situ, dan tanda ! pertama yang menghentikan aplikasi.",
                    "  3. Ganti dengan guard let supaya kasus kosong punya jalan keluar:",
                    "       guard let teks = pengguna.fotoUrl,",
                    "             let url = URL(string: teks) else {",
                    "           tampilkanFotoBawaan()",
                    "           return",
                    "       }",
                    "  4. Bandingkan dengan kode Android-nya. Biasanya di sana sudah",
                    "     ada pengecekan null yang setara, makanya Android nggak ikut",
                    "     tertutup.",
                    "  5. Kamu nggak punya Mac untuk mencoba layarnya, tapi logika",
                    "     pembuka optional itu bisa diuji dengan swift test di Fedora,",
                    "     karena Foundation (tempat URL tinggal) juga ada di Linux.",
                ],
            },
        ],
    },
    {
        "title": "18. SwiftUI dan UIKit: Dua Cara Membangun Layar iOS",
        "sections": [
            {
                "body": [
                    "Aplikasi iOS punya dua framework untuk membangun layar. UIKit sudah",
                    "ada sejak SDK iPhone pertama tahun 2008. SwiftUI datang tahun 2019",
                    "bersama iOS 13. Keduanya ikut terpasang di SDK iOS, jadi versinya",
                    "mengikuti SDK. Saat materi ini ditulis (Oktober 2026), keduanya",
                    "ikut SDK iOS 27 yang dibawa Xcode 27.1, rilis 15 Oktober 2026.",
                    "Apple memakai nomor versi berbasis tahun sejak 2025, makanya",
                    "lompatannya dari iOS 18 langsung ke iOS 26.",
                    "",
                    "Bedanya mirip beda Jetpack Compose dan layout XML di bab 03. SwiftUI",
                    "itu deklaratif: kamu menulis seperti apa layarnya untuk state",
                    "tertentu, lalu SwiftUI yang mengurus perubahannya. UIKit itu",
                    "imperatif: kamu membuat objek label dan tombol, lalu mengubah",
                    "isinya sendiri setiap kali datanya berubah.",
                    "",
                    "Ingat: keduanya cuma bisa dijalankan di macOS dengan Xcode. Di",
                    "Fedora kamu bisa membaca dan menulis kodenya, tapi pratinjau dan",
                    "simulatornya butuh Mac. Contoh di materi ini untuk dibaca.",
                ],
            },
            {
                "heading": "SwiftUI: layar sebagai fungsi dari state",
                "bahasa": "swift",
                "code": "import SwiftUI\n\nstruct PenghitungView: View {\n    @State private var jumlah = 0\n\n    var body: some View {\n        VStack(spacing: 12) {\n            Text(\"Diklik \\(jumlah) kali\")\n                .font(.title)\n            Button(\"Tambah\") {\n                jumlah += 1\n            }\n        }\n        .padding()\n    }\n}\n\n#Preview {\n    PenghitungView()\n}",
            },
            {
                "body": [
                    "Layar SwiftUI adalah struct yang memenuhi protokol View. Isinya",
                    "satu properti wajib, body, yang mengembalikan susunan view lain.",
                    "VStack menyusun anaknya dari atas ke bawah, HStack dari kiri ke",
                    "kanan. Padanannya Column dan Row di Compose.",
                    "",
                    "@State menandai data milik view ini. Begitu jumlah berubah, SwiftUI",
                    "memanggil body lagi, membandingkan hasil baru dengan yang lama, lalu",
                    "cuma mengubah bagian yang beda. Cara SwiftUI mengenali \"view yang",
                    "sama\" adalah lewat tipe dan posisinya di susunan, kecuali kamu",
                    "memberinya id sendiri. Latihan bab ini meniru cara membandingkan",
                    "itu.",
                    "",
                    "Baris seperti .font(.title) dan .padding() disebut modifier. Tiap",
                    "modifier membungkus view jadi view baru, jadi urutannya berpengaruh:",
                    ".padding() lalu .background(.yellow) memberi latar yang ikut",
                    "melebar, kebalikannya nggak. #Preview menampilkan layarnya di kanvas",
                    "Xcode tanpa menjalankan simulator.",
                    "",
                    "Untuk data yang dipakai banyak layar, iOS 17 ke atas memakai makro",
                    "@Observable pada class model. Data milik induk diteruskan ke anak",
                    "lewat @Binding supaya anak bisa mengubahnya.",
                ],
            },
            {
                "heading": "UIKit: kamu yang memegang kendali",
                "bahasa": "swift",
                "code": "import UIKit\n\nfinal class PenghitungViewController: UIViewController {\n    private var jumlah = 0\n    private let label = UILabel()\n    private let tombol = UIButton(type: .system)\n\n    override func viewDidLoad() {\n        super.viewDidLoad()\n        view.backgroundColor = .systemBackground\n        label.text = \"Diklik 0 kali\"\n        tombol.setTitle(\"Tambah\", for: .normal)\n        tombol.addTarget(self, action: #selector(tambah), for: .touchUpInside)\n\n        let susun = UIStackView(arrangedSubviews: [label, tombol])\n        susun.axis = .vertical\n        susun.spacing = 12\n        susun.translatesAutoresizingMaskIntoConstraints = false\n        view.addSubview(susun)\n        NSLayoutConstraint.activate([\n            susun.centerXAnchor.constraint(equalTo: view.centerXAnchor),\n            susun.centerYAnchor.constraint(equalTo: view.centerYAnchor),\n        ])\n    }\n\n    @objc private func tambah() {\n        jumlah += 1\n        label.text = \"Diklik \\(jumlah) kali\"\n    }\n}",
            },
            {
                "body": [
                    "Hasil di layar sama persis dengan versi SwiftUI. Bedanya ada di",
                    "siapa yang bekerja:",
                    "",
                    "  - Satu layar UIKit dipegang satu view controller. Ia punya siklus",
                    "    hidup: viewDidLoad sekali saat view dibuat, lalu viewWillAppear",
                    "    dan viewDidAppear setiap kali layarnya akan dan sudah tampil.",
                    "    Mirip onCreate dan onResume di Activity Android.",
                    "  - Posisi diatur Auto Layout lewat constraint, yaitu aturan seperti",
                    "    \"tengah susunan sama dengan tengah layar\". Baris",
                    "    translatesAutoresizingMaskIntoConstraints = false wajib ada",
                    "    kalau constraint-nya kamu tulis sendiri lewat kode.",
                    "  - Setiap kali jumlah berubah, kamu sendiri yang menulis ulang",
                    "    label.text. Lupa satu baris itu, dan label menampilkan angka",
                    "    lama padahal datanya sudah berubah.",
                    "",
                    "Selain lewat kode, layar UIKit bisa digambar di storyboard dengan",
                    "Interface Builder, editor seret-taruh di Xcode. Daftar panjang",
                    "memakai UITableView atau UICollectionView yang diisi lewat pola",
                    "delegate dan data source, padanan RecyclerView dan adapter-nya.",
                ],
            },
            {
                "heading": "Kapan pakai yang mana",
                "body": [
                    "Untuk aplikasi baru, mulai dari SwiftUI. Tutorial resmi Apple",
                    "sekarang mengutamakan SwiftUI, dan fitur baru seperti widget layar",
                    "utama ditulis dengan SwiftUI.",
                    "",
                    "UIKit statusnya stabil dan matang. Ia masih diperbarui tiap tahun",
                    "dan masih jadi fondasi di bawah SwiftUI. Kamu bakal ketemu UIKit di",
                    "tiga situasi:",
                    "",
                    "  1. Aplikasi besar yang umurnya sudah bertahun-tahun.",
                    "  2. Komponen yang belum ada padanannya di SwiftUI, atau butuh",
                    "     kendali yang rinci atas gulir dan animasi.",
                    "  3. Pustaka pihak ketiga lama yang cuma menyediakan versi UIKit.",
                    "",
                    "Keduanya bisa dicampur. UIHostingController menaruh layar SwiftUI",
                    "di dalam aplikasi UIKit, dan UIViewRepresentable membungkus view",
                    "UIKit supaya bisa dipakai di SwiftUI. Aplikasi lama biasanya pindah",
                    "pelan-pelan dengan cara ini, satu layar demi satu layar.",
                ],
            },
            {
                "body": [
                    "Jebakan: body SwiftUI bisa dipanggil berkali-kali dalam sedetik.",
                    "Jangan taruh pekerjaan berat atau pemanggilan jaringan langsung di",
                    "dalam body. Pakai modifier .task { } yang berjalan saat view muncul.",
                    "",
                    "Jebakan: UIKit nggak aman dipakai dari thread lain. Kalau hasil",
                    "jaringan datang di thread latar lalu kamu langsung mengubah",
                    "label.text, hasilnya bisa aneh atau aplikasi berhenti. Ubah UI di",
                    "main thread, misalnya lewat fungsi yang ditandai @MainActor.",
                    "",
                    "Kalau kamu nggak punya Mac sama sekali, jalur realistis untuk",
                    "membuat aplikasi iPhone adalah kerangka lintas platform di bab",
                    "06 dan 07, ditambah layanan build di cloud.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi iOS yang sudah berumur biasanya campuran: layar lama",
                    "ditulis dengan UIKit, layar baru dengan SwiftUI yang disisipkan",
                    "lewat UIHostingController. Lowongan iOS karena itu sering meminta",
                    "dua-duanya.",
                    "",
                    "Kasus kecil: di aplikasi toko berbasis UIKit, angka di ikon",
                    "keranjang nggak berubah setelah pengguna menambah barang dari",
                    "layar detail. Angkanya baru benar setelah aplikasi dibuka ulang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari tempat label keranjang diisi. Biasanya cuma di",
                    "     viewDidLoad, yang dipanggil sekali saja.",
                    "  2. Pindahkan pengisiannya ke viewWillAppear supaya dibaca ulang",
                    "     setiap kali layar tampil lagi:",
                    "       override func viewWillAppear(_ animated: Bool) {",
                    "           super.viewWillAppear(animated)",
                    "           labelKeranjang.text = \"\\(keranjang.jumlah)\"",
                    "       }",
                    "  3. Kalau perubahan datang dari jaringan, pastikan label diubah",
                    "     di main thread.",
                    "  4. Untuk perbaikan jangka panjang, tulis ulang layar itu dengan",
                    "     SwiftUI dan model @Observable. Label lalu ikut berubah",
                    "     sendiri karena body dibaca ulang setiap state-nya berubah.",
                ],
            },
        ],
    },
    {
        "title": "19. Xcode, Simulator, dan Pengelola Paket Swift",
        "sections": [
            {
                "body": [
                    "Xcode adalah IDE resmi Apple untuk semua platform Apple. Isinya",
                    "editor, compiler, simulator iPhone dan iPad, alat ukur kinerja",
                    "bernama Instruments, dan jalur pengunggahan ke App Store. Xcode",
                    "gratis, tapi cuma ada untuk macOS. Versi terbaru saat materi ini",
                    "ditulis (Oktober 2026) adalah Xcode 27.1 (build 27A9275), rilis 15",
                    "Oktober 2026. Di Survei Stack Overflow 2025, Xcode dipakai 10%",
                    "responden.",
                    "",
                    "Aturan yang perlu kamu tahu: sejak 28 April 2026, aplikasi yang",
                    "diunggah ke App Store wajib dibangun dengan Xcode 26 atau lebih",
                    "baru. Aplikasi Flutter dan React Native juga lewat Xcode untuk",
                    "versi iOS-nya, karena di ujungnya mereka tetap jadi proyek Xcode.",
                    "",
                    "Di Fedora, Xcode nggak bisa dipasang, dan lisensi macOS cuma",
                    "mengizinkan macOS dipasang di perangkat Apple. Pilihan yang sah:",
                    "meminjam Mac, menyewa Mac di cloud, memakai layanan CI bermesin",
                    "macOS, atau layanan build seperti yang dipakai Expo di bab 07.",
                ],
            },
            {
                "heading": "Bagian Xcode yang perlu dikenal",
                "body": [
                    "Kalau suatu hari kamu duduk di depan Mac, ini yang bakal kamu",
                    "pakai paling sering:",
                    "",
                    "  - Editor dengan kanvas pratinjau SwiftUI di sebelah kanan.",
                    "  - Simulator, iPhone dan iPad virtual. Simulator menjalankan",
                    "    aplikasi yang dikompilasi untuk prosesor Mac, jadi jalannya",
                    "    cepat. Ini beda dari emulator Android yang meniru perangkat",
                    "    utuh. Beberapa hal, misalnya kamera, tetap harus dicoba di",
                    "    iPhone sungguhan.",
                    "  - Signing & Capabilities, tempat mengisi tim developer, bundle",
                    "    identifier (nama unik aplikasi seperti id.contoh.kasir), dan",
                    "    izin seperti notifikasi atau akses kamera.",
                    "  - Organizer, tempat hasil Archive (build untuk rilis) diunggah",
                    "    ke App Store Connect.",
                    "  - Instruments, untuk mencari kebocoran memori dan bagian kode",
                    "    yang lambat.",
                ],
            },
            {
                "heading": "Swift Package Manager: Package.swift",
                "bahasa": "swift",
                "code": """// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "Kasir",
    dependencies: [
        .package(url: "https://github.com/apple/swift-argument-parser", from: "1.5.0"),
    ],
    targets: [
        .executableTarget(
            name: "Kasir",
            dependencies: [
                .product(name: "ArgumentParser", package: "swift-argument-parser"),
            ]
        ),
    ]
)""",
            },
            {
                "body": [
                    "Swift Package Manager (SwiftPM) adalah pengelola paket resmi Swift.",
                    "Ia ikut terpasang di Xcode dan di toolchain Swift, termasuk yang",
                    "kamu pasang di Linux, dan versinya mengikuti Swift (6.4 saat ini).",
                    "Daftar dependensinya ditulis di Package.swift, yang ditulis dalam",
                    "Swift juga.",
                    "",
                    "from: \"1.5.0\" artinya versi 1.5.0 atau lebih baru, tapi di bawah",
                    "2.0.0. Angka depan yang naik menandakan perubahan yang bisa merusak",
                    "kodemu, jadi SwiftPM nggak mengambilnya tanpa izin. Versi persis",
                    "yang terpilih dicatat di Package.resolved. Untuk aplikasi, ikutkan",
                    "berkas itu ke git supaya semua orang di tim memakai versi yang",
                    "sama.",
                    "",
                    "Di Linux, swift build mengunduh dan membangun paketnya. Di Xcode,",
                    "paket ditambah lewat menu File, lalu Add Package Dependencies.",
                    "Menurut catatan rilisnya, React Native 0.87 juga mulai menambah",
                    "dukungan SwiftPM yang masih eksperimental.",
                ],
            },
            {
                "heading": "CocoaPods: Podfile di proyek lama",
                "bahasa": "ruby",
                "code": """platform :ios, '16.0'

target 'Kasir' do
  use_frameworks!
  pod 'Alamofire', '~> 5.12'
  ...
end""",
            },
            {
                "heading": "Perintah CocoaPods",
                "bahasa": "terminal",
                "code": """pod install
open Kasir.xcworkspace
pod deintegrate""",
            },
            {
                "body": [
                    "CocoaPods adalah pengelola dependensi iOS yang lebih tua, ditulis",
                    "dalam Ruby. Berkasnya bernama Podfile. ~> 5.12 artinya 5.12 atau",
                    "lebih baru, tapi di bawah 6.0. pod install membaca Podfile lalu",
                    "membuat folder Pods/ dan berkas .xcworkspace, sedangkan pod",
                    "deintegrate mencabut CocoaPods dari proyek. Versi terakhirnya",
                    "1.17.0, rilis 6 Juli 2026.",
                    "",
                    "Statusnya usang. Menurut blog resmi CocoaPods, trunk (gudang pusat",
                    "daftar pod) berhenti menerima podspec baru secara permanen pada 2",
                    "Desember 2026, dengan uji coba 1 sampai 7 November 2026. Sesudah",
                    "itu nggak ada pod atau versi baru yang bisa diterbitkan. Build yang",
                    "sudah ada tetap jalan selama repositori Specs dan CDN-nya masih",
                    "hidup. Untuk proyek baru, pakai SwiftPM.",
                    "",
                    "Kamu tetap bakal sering melihat Podfile, misalnya di folder ios/",
                    "proyek Flutter atau React Native yang dibuat beberapa tahun",
                    "terakhir.",
                    "",
                    "Carthage adalah pengelola ketiga. Ia cuma membangun framework tanpa",
                    "mengubah proyek Xcode-mu, jadi kamu menautkannya sendiri. Rilis",
                    "terakhirnya 0.40.0 pada 9 September 2024, dan ekosistemnya sudah",
                    "pindah ke SwiftPM. Anggap ini sejarah yang masih tercantum di",
                    "roadmap.sh iOS.",
                    "",
                    "Jebakan: sesudah pod install, buka berkas .xcworkspace, bukan",
                    ".xcodeproj. Kalau yang dibuka .xcodeproj, Xcode nggak melihat",
                    "folder Pods, dan build gagal dengan pesan modul nggak ditemukan.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek iOS warisan berumur lima tahun ke atas hampir pasti punya",
                    "Podfile. Dengan trunk CocoaPods yang ditutup akhir 2026, banyak",
                    "tim sedang memindahkan dependensinya ke SwiftPM.",
                    "",
                    "Kasus kecil: kamu diminta menyiapkan proyek iOS lama berisi enam",
                    "pod supaya tetap bisa menerima versi pustaka baru sesudah Desember",
                    "2026.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Catat keenam pod beserta versinya dari Podfile.lock.",
                    "  2. Buka repositori tiap pustaka. Cari berkas Package.swift di",
                    "     akarnya. Kalau ada, pustaka itu bisa dipasang lewat SwiftPM.",
                    "  3. Untuk pod tanpa Package.swift, cari pengganti, atau salin",
                    "     kodenya ke proyek kalau lisensinya mengizinkan.",
                    "  4. Di Mac atau mesin CI macOS, jalankan pod deintegrate, lalu",
                    "     tambahkan paket satu per satu lewat Add Package Dependencies.",
                    "  5. Build dan uji setiap kali satu pustaka pindah. Kalau rusak,",
                    "     kamu langsung tahu pustaka mana penyebabnya.",
                    "  6. Ikutkan Package.resolved ke git supaya versinya terkunci.",
                ],
            },
        ],
    },
    {
        "title": "20. Peta Framework Apple",
        "sections": [
            {
                "body": [
                    "Kode iOS dan lowongan kerja iOS penuh nama framework. Materi ini",
                    "peta untuk mengenali nama-nama itu: gunanya apa, statusnya",
                    "bagaimana, dan padanannya di Android yang sudah kamu kenal. Kamu",
                    "nggak perlu menguasai semuanya sekarang.",
                    "",
                    "Hampir semua framework di sini milik Apple dan versinya ikut SDK",
                    "iOS (iOS 27 saat materi ini ditulis, Oktober 2026). Contoh kodenya",
                    "untuk dibaca, karena cuma bisa dijalankan di platform Apple.",
                ],
            },
            {
                "heading": "Combine: aliran event",
                "bahasa": "swift",
                "code": """import Combine

let kotakCari = PassthroughSubject<String, Never>()
var langganan = Set<AnyCancellable>()

kotakCari
    .map { $0.trimmingCharacters(in: .whitespaces) }
    .filter { $0.count >= 3 }
    .removeDuplicates()
    .sink { kata in print("cari:", kata) }
    .store(in: &langganan)

kotakCari.send("ko")
kotakCari.send("kopi")
kotakCari.send("kopi ")
kotakCari.send("kopi susu")
// cari: kopi
// cari: kopi susu""",
            },
            {
                "body": [
                    "Combine adalah framework pemrograman reaktif Apple. Publisher",
                    "mengirim nilai, operator seperti map dan filter mengolahnya, dan",
                    "subscriber (di sini sink) menerimanya. Di contoh, \"ko\" dibuang",
                    "filter karena kurang dari tiga huruf, dan \"kopi \" dibuang",
                    "removeDuplicates karena sesudah spasinya dipangkas ia sama dengan",
                    "nilai sebelumnya.",
                    "",
                    "Konsepnya sama dengan Flow di Kotlin dan RxJS di JavaScript.",
                    "Statusnya stabil dan matang. Untuk kode baru, banyak bagian yang",
                    "dulu memakai Combine sekarang ditulis dengan async/await dan",
                    "framework Observation (makro @Observable).",
                ],
            },
            {
                "heading": "SwiftData: model sebagai class biasa",
                "bahasa": "swift",
                "code": "import SwiftData\nimport SwiftUI\n\n@Model\nfinal class Catatan {\n    var judul: String\n    var dibuat: Date\n\n    init(judul: String, dibuat: Date = .now) {\n        self.judul = judul\n        self.dibuat = dibuat\n    }\n}\n\nstruct DaftarCatatan: View {\n    @Query(sort: \\Catatan.dibuat, order: .reverse) private var catatan: [Catatan]\n    @Environment(\\.modelContext) private var konteks\n\n    var body: some View {\n        List(catatan) { c in Text(c.judul) }\n        Button(\"Tambah\") {\n            konteks.insert(Catatan(judul: \"Belanja\"))\n        }\n    }\n}",
            },
            {
                "body": [
                    "Ada dua cara menyimpan data lokal di aplikasi Apple, dan dua-duanya",
                    "padanan Room di bab 04.",
                    "",
                    "Core Data adalah yang lama. Ia mengelola graf objek, biasanya",
                    "disimpan di SQLite, dengan model yang digambar di berkas",
                    ".xcdatamodeld dan objek turunan NSManagedObject. Core Data juga",
                    "bisa menyinkronkan data ke iCloud lewat CloudKit. Statusnya stabil",
                    "dan matang: masih didukung, banyak dipakai aplikasi lama.",
                    "",
                    "SwiftData hadir di iOS 17 (2023). Model cukup ditulis sebagai class",
                    "Swift biasa yang diberi makro @Model, seperti contoh di atas. Di",
                    "baliknya, SwiftData memakai teknologi Core Data. @Query mengambil",
                    "data dan membuat layar ikut berubah saat datanya berubah. Supaya",
                    "contoh itu jalan, aplikasi juga perlu .modelContainer(for:",
                    "Catatan.self) di bagian App-nya. Untuk proyek SwiftUI baru, SwiftData",
                    "jadi pilihan utama Apple.",
                    "",
                    "Kamu juga mungkin ketemu Realm, database objek pihak ketiga yang",
                    "tersedia untuk iOS dan Android. roadmap.sh iOS mencantumkannya,",
                    "bersama SQLite langsung, sebagai alternatif Core Data.",
                ],
            },
            {
                "heading": "URLSession dan Alamofire",
                "bahasa": "swift",
                "code": """struct Produk: Decodable {
    let id: Int
    let nama: String
}

// Bawaan Apple: URLSession dengan async/await
func ambilProduk() async throws -> [Produk] {
    let url = URL(string: "https://api.contoh.id/produk")!
    let (data, _) = try await URLSession.shared.data(from: url)
    return try JSONDecoder().decode([Produk].self, from: data)
}

// Dengan Alamofire, hasil yang sama dalam satu baris
// let produk = try await AF.request(url).serializingDecodable([Produk].self).value""",
            },
            {
                "body": [
                    "Alamofire adalah pustaka HTTP pihak ketiga yang menyederhanakan",
                    "URLSession, mirip peran Retrofit di Android. Versi terbarunya 5.12.2",
                    "(10 September 2026), lisensi MIT. Statusnya stabil dan matang.",
                    "Sejak URLSession mendukung async/await, banyak proyek baru cukup",
                    "memakai URLSession bawaan seperti fungsi ambilProduk di atas.",
                    "Decodable menandai struct yang bisa diisi dari JSON, padanan",
                    "@Serializable di kotlinx.serialization.",
                ],
            },
            {
                "heading": "Objective-C: bahasa sebelum Swift",
                "bahasa": "objectivec",
                "code": """#import <Foundation/Foundation.h>

@interface Sapaan : NSObject
- (NSString *)sapa:(NSString *)nama;
@end

@implementation Sapaan
- (NSString *)sapa:(NSString *)nama {
    return [NSString stringWithFormat:@"Halo, %@", nama];
}
@end

int main(void) {
    @autoreleasepool {
        Sapaan *s = [[Sapaan alloc] init];
        NSLog(@"%@", [s sapa:@"Rina"]);
    }
    return 0;
}""",
            },
            {
                "body": [
                    "Objective-C adalah bahasa C yang ditambah gaya kirim pesan dari",
                    "Smalltalk. Ciri yang paling gampang dikenali adalah kurung siku:",
                    "[s sapa:@\"Rina\"] artinya kirim pesan sapa ke objek s dengan",
                    "argumen \"Rina\". String diawali @, dan header dipisah di berkas .h.",
                    "",
                    "Statusnya menurun. Apple mengarahkan semua kode baru ke Swift. Di",
                    "Survei Stack Overflow 2024, Objective-C dipakai 2,1% responden, dan",
                    "di survei 2025 sudah nggak tercantum. Kamu masih bakal ketemu di",
                    "aplikasi lama dan pustaka lama. Swift dan Objective-C bisa saling",
                    "panggil dalam satu proyek, jadi aplikasi lama biasanya pindah",
                    "sedikit demi sedikit.",
                    "",
                    "AppKit adalah framework layar untuk aplikasi Mac, padanan UIKit di",
                    "macOS: ada NSWindow, NSViewController, dan menu bar. Versinya ikut",
                    "SDK macOS 27 di Xcode 27.1. Statusnya stabil dan matang, sementara",
                    "aplikasi Mac baru makin banyak memakai SwiftUI, yang juga jalan di",
                    "macOS.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Lowongan iOS hampir selalu menulis campuran nama dari materi ini,",
                    "dan pelamar yang bisa memisahkan mana bahasa, mana framework UI,",
                    "dan mana penyimpanan data jauh lebih cepat menyusun rencana",
                    "belajar.",
                    "",
                    "Kasus kecil: kamu membaca lowongan \"iOS Developer: Swift, SwiftUI,",
                    "UIKit, Combine, Core Data, nilai plus Objective-C\" dan bingung",
                    "harus mulai dari mana, padahal laptopmu Fedora.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan bahasa dari framework. Bahasanya Swift dan",
                    "     Objective-C. Sisanya framework.",
                    "  2. Kelompokkan framework menurut tugas: layar (SwiftUI, UIKit),",
                    "     data lokal (Core Data), dan aliran event (Combine).",
                    "  3. Tulis padanan Android tiap kelompok: Compose dan View, Room,",
                    "     lalu Flow. Konsep yang sudah kamu pahami di sana tinggal",
                    "     dipetakan ulang.",
                    "  4. Mulai dari yang bisa dilatih di Fedora: bahasa Swift lewat",
                    "     swiftly, plus konsep reaktif lewat Flow di Kotlin.",
                    "  5. Untuk SwiftUI, UIKit, Core Data, dan Combine, rencanakan akses",
                    "     ke Mac. Sampai saat itu, baca kodenya di dokumentasi Apple",
                    "     sambil mencocokkan dengan padanan Android-nya.",
                ],
            },
        ],
    },
    {
        "title": "21. Dart untuk Pemrogram JavaScript",
        "sections": [
            {
                "body": [
                    "Dart adalah bahasa buatan Google yang bertipe statis, artinya tipe",
                    "setiap variabel dicek sebelum program jalan. Dart terutama dipakai",
                    "bersama Flutter, kerangka yang kamu pelajari di materi berikutnya.",
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "Dart 3.13.5, rilis 29 September 2026, dengan lisensi BSD-3-Clause.",
                    "Di Survei Stack Overflow 2025, Dart dipakai 5,9% responden.",
                    "",
                    "Kalau kamu sudah lulus kurikulum JavaScript, banyak bagian Dart",
                    "bakal terasa akrab: kurung kurawal, async dan await, fungsi panah",
                    "=>, dan operator ?? serta ?.. Bedanya ada di dua hal. Tipe dicek",
                    "sebelum program jalan, dan nilai yang boleh kosong harus dinyatakan",
                    "dari awal.",
                    "",
                    "Dart SDK tersedia untuk Linux, jadi kamu bisa memasangnya di",
                    "Fedora. Aplikasi ini belum punya kurikulum Dart, jadi di materi ini",
                    "setiap contoh Dart disandingkan dengan versi JavaScript yang bisa",
                    "kamu jalankan langsung. Kalau mau mencoba Dart tanpa memasang apa",
                    "pun, ada DartPad (dartpad.dev), editor daring resmi yang butuh",
                    "internet.",
                ],
            },
            {
                "heading": "Program Dart pertama",
                "bahasa": "dart",
                "code": """void main() {
  final nama = 'Rina';
  var jumlah = 3;
  const pajak = 0.11;
  int? diskon; // boleh null, nilai awalnya null

  jumlah += 1;
  final total = 50000 * jumlah * (1 + pajak) - (diskon ?? 0);
  print('Halo $nama, total: ${total.round()}');
}""",
            },
            {
                "heading": "Padanannya di JavaScript",
                "code": """const nama = 'Rina';
let jumlah = 3;
const pajak = 0.11;
let diskon = null;

jumlah += 1;
const total = 50000 * jumlah * (1 + pajak) - (diskon ?? 0);
console.log(`Halo ${nama}, total: ${Math.round(total)}`);""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  Halo Rina, total: 222000",
                    "",
                    "Versi Dart mencetak baris yang sama persis. Yang perlu kamu",
                    "perhatikan dari dua kode itu:",
                    "",
                    "  - Dart wajib punya fungsi main sebagai titik mulai, dan setiap",
                    "    pernyataan diakhiri titik koma.",
                    "  - final di Dart mirip const di JavaScript: nilainya ditetapkan",
                    "    sekali saat program jalan. const di Dart lebih ketat, nilainya",
                    "    harus sudah diketahui waktu kompilasi.",
                    "  - var menebak tipe dari nilai pertama. Sesudah jumlah jadi int,",
                    "    kamu nggak bisa mengisinya dengan teks. Di JavaScript bisa.",
                    "  - Interpolasi string memakai $nama atau ${ekspresi} di dalam",
                    "    tanda kutip biasa, mirip Kotlin. JavaScript butuh backtick.",
                    "  - int? artinya int yang boleh null. Tanpa tanda tanya, Dart",
                    "    menolak null.",
                ],
            },
            {
                "heading": "Null safety",
                "bahasa": "dart",
                "code": """String? cariKota(String kode) {
  const kota = {'BDG': 'Bandung', 'MLG': 'Malang'};
  return kota[kode];
}

void main() {
  final a = cariKota('BDG');
  final b = cariKota('XYZ');
  // print(a.length);          // error kompilasi: a bisa null
  print(a?.length);            // 7
  print(b ?? 'nggak dikenal');  // nggak dikenal
  if (a != null) {
    print(a.toUpperCase());    // BANDUNG: di sini a pasti String
  }
}""",
            },
            {
                "body": [
                    "Dart memakai sound null safety, dan sejak Dart 3 aturan itu wajib",
                    "untuk semua kode. Sound artinya kalau tipenya String, Dart menjamin",
                    "isinya nggak pernah null saat program jalan. Kalau baris yang",
                    "dikomentari di atas diaktifkan, compiler menolak dengan pesan:",
                    "",
                    "  Property 'length' cannot be accessed on 'String?' because it is",
                    "  potentially null.",
                    "",
                    "Bandingkan dengan JavaScript, yang baru protes TypeError saat baris",
                    "itu dijalankan, mungkin di ponsel pengguna. Sesudah if (a != null),",
                    "Dart tahu a pasti String, jadi a.toUpperCase() boleh. Ini sama",
                    "dengan smart cast di Kotlin.",
                    "",
                    "Tanda seru a! memaksa nilai dianggap bukan null. Kalau ternyata",
                    "null, program berhenti dengan error. Kata kunci late menunda",
                    "pengisian variabel non-null sampai nanti, dan error juga muncul",
                    "kalau variabel itu dibaca sebelum diisi.",
                ],
            },
            {
                "heading": "Future, async, dan await",
                "bahasa": "dart",
                "code": """Future<String> ambilSaldo() async {
  await Future.delayed(const Duration(milliseconds: 300));
  return 'Rp150.000';
}

Future<void> main() async {
  print('memuat...');
  try {
    final saldo = await ambilSaldo();
    print('saldo: $saldo');
  } catch (e) {
    print('gagal: $e');
  }
}""",
            },
            {
                "heading": "Padanannya dengan Promise",
                "code": """function ambilSaldo() {
  return new Promise((selesai) => {
    setTimeout(() => selesai('Rp150.000'), 300);
  });
}

async function main() {
  console.log('memuat...');
  try {
    const saldo = await ambilSaldo();
    console.log(`saldo: ${saldo}`);
  } catch (e) {
    console.log(`gagal: ${e}`);
  }
}

main();""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  memuat...",
                    "  saldo: Rp150.000",
                    "",
                    "Future di Dart sama dengan Promise di JavaScript: janji bahwa",
                    "nilainya datang nanti. async dan await bekerja dengan cara yang",
                    "sama, termasuk try dan catch untuk menangkap kegagalan. Aliran",
                    "banyak nilai yang datang bergiliran disebut Stream, padanan async",
                    "iterator di JavaScript.",
                    "",
                    "Seperti JavaScript, Dart menjalankan kodemu di satu thread dengan",
                    "event loop. Untuk pekerjaan berat, misalnya mengurai JSON berukuran",
                    "megabyte, Dart punya isolate: pekerja terpisah yang nggak berbagi",
                    "memori, mirip Web Worker. Cara paling ringkasnya Isolate.run(...).",
                    "",
                    "Jebakan: lupa menulis await. Kalau kamu mencetak ambilSaldo()",
                    "tanpa await, yang keluar teks Instance of 'Future<String>', dan",
                    "saldonya nggak pernah tercetak. Di aplikasi Flutter, teks aneh itu",
                    "bisa muncul langsung di layar.",
                ],
            },
            {
                "heading": "Class dan koleksi yang sering muncul di Flutter",
                "bahasa": "dart",
                "code": """class Produk {
  final String nama;
  final int harga;
  const Produk({required this.nama, required this.harga});

  String get label => '$nama (Rp$harga)';
}

void main() {
  final daftar = [
    const Produk(nama: 'Kopi', harga: 18000),
    const Produk(nama: 'Teh', harga: 8000),
  ];
  final adaPromo = true;
  final baris = [
    'Menu',
    if (adaPromo) 'Promo hari ini',
    for (final p in daftar) p.label,
  ];
  print(baris); // [Menu, Promo hari ini, Kopi (Rp18000), Teh (Rp8000)]
  print(7 ~/ 2); // 3
  print(7 / 2);  // 3.5
}""",
            },
            {
                "body": [
                    "Tiga hal di contoh ini bakal kamu lihat di hampir setiap berkas",
                    "Flutter:",
                    "",
                    "  - Parameter bernama di dalam kurung kurawal, dengan required untuk",
                    "    yang wajib. Widget Flutter dipanggil seperti",
                    "    Padding(padding: ..., child: ...).",
                    "  - Konstruktor singkat this.nama yang langsung mengisi field.",
                    "  - if dan for di dalam literal daftar. Flutter memakainya untuk",
                    "    menyusun anak widget sesuai kondisi.",
                    "",
                    "Pembagian juga beda dari JavaScript. Operator / selalu menghasilkan",
                    "double, dan pembagian bulat memakai ~/. Paket Dart diambil dari",
                    "pub.dev, padanan npm. Perintah sehari-harinya dart create, dart run,",
                    "dart pub add nama_paket, dan dart analyze untuk mencari kesalahan",
                    "tanpa menjalankan program.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Programmer JavaScript yang pindah ke Flutter biasanya cepat",
                    "membaca Dart. Yang paling sering membuat mereka tersandung adalah",
                    "null safety dan Future yang lupa ditunggu.",
                    "",
                    "Kasus kecil: halaman profil di aplikasi Flutter menampilkan tulisan",
                    "Instance of 'Future<String>' di tempat yang mestinya berisi nama",
                    "pengguna.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali polanya. Teks Instance of 'Future<...>' berarti sebuah",
                    "     Future dicetak langsung, belum ditunggu hasilnya.",
                    "  2. Cari pemanggil fungsi yang mengembalikan Future<String>, misalnya",
                    "     ambilNama(). Biasanya ia dipakai langsung di dalam teks:",
                    "       Text('Halo ${ambilNama()}')",
                    "  3. Fungsi build di Flutter nggak boleh async, jadi await nggak",
                    "     bisa ditulis di sana. Muat nama di luar build, misalnya di",
                    "     initState, lalu simpan hasilnya di state.",
                    "  4. Atau pakai widget FutureBuilder, yang menggambar teks \"memuat\"",
                    "     selama Future belum selesai dan nama sesudahnya. Cara yang",
                    "     lebih rapi untuk aplikasi besar dibahas di materi state",
                    "     management.",
                ],
            },
        ],
    },
    {
        "title": "22. Widget, Element, dan Cara Flutter Menggambar",
        "sections": [
            {
                "body": [
                    "Flutter adalah kerangka UI buatan Google untuk membuat aplikasi",
                    "Android, iOS, web, dan desktop (Windows, macOS, Linux) dari satu",
                    "kode Dart. Versi stabil terbaru saat materi ini ditulis (Oktober",
                    "2026) adalah Flutter 3.47.7, rilis 8 Oktober 2026, berpasangan",
                    "dengan Dart 3.13.5. Lisensinya BSD-3-Clause. Di Survei Stack",
                    "Overflow 2024, Flutter dipakai 9,4% responden, tertinggi di antara",
                    "kerangka mobile, dan repositorinya punya sekitar 180 ribu bintang",
                    "di GitHub.",
                    "",
                    "Hal pertama yang membedakan Flutter: ia nggak memakai tombol atau",
                    "kotak teks bawaan Android dan iOS. Flutter menggambar sendiri setiap",
                    "pikselnya dengan mesin render miliknya, mirip cara game menggambar",
                    "layar. Akibatnya tampilan aplikasimu sama persis di semua platform.",
                    "Kalau ingin terasa seperti aplikasi iPhone, kamu memakai widget",
                    "bergaya Cupertino. Gaya Android memakai widget Material.",
                    "",
                    "Di Fedora, Flutter bisa membangun aplikasi Android, web, dan Linux",
                    "desktop. Versi iOS dan macOS tetap butuh Mac dengan Xcode, atau",
                    "layanan build di cloud seperti Codemagic.",
                ],
            },
            {
                "heading": "Aplikasi Flutter kecil",
                "bahasa": "dart",
                "code": """import 'package:flutter/material.dart';

void main() => runApp(const AplikasiKu());

class AplikasiKu extends StatelessWidget {
  const AplikasiKu({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: Penghitung());
  }
}

class Penghitung extends StatefulWidget {
  const Penghitung({super.key});

  @override
  State<Penghitung> createState() => _PenghitungState();
}

class _PenghitungState extends State<Penghitung> {
  int _jumlah = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Penghitung')),
      body: Center(child: Text('Diklik $_jumlah kali')),
      floatingActionButton: FloatingActionButton(
        onPressed: () => setState(() => _jumlah++),
        child: const Icon(Icons.add),
      ),
    );
  }
}""",
            },
            {
                "body": [
                    "Di Flutter, hampir semua hal adalah widget: teks, tombol, jarak,",
                    "bahkan tata letak seperti Center dan Padding. Widget adalah",
                    "deskripsi yang nggak bisa diubah, semacam cetak biru. Kalau",
                    "tampilan perlu berubah, Flutter membuat widget baru, nggak mengubah",
                    "yang lama.",
                    "",
                    "Ada dua jenis widget:",
                    "",
                    "  - StatelessWidget, yang tampilannya cuma bergantung pada",
                    "    parameter dari induknya. AplikasiKu termasuk jenis ini.",
                    "  - StatefulWidget, yang punya objek State terpisah untuk menyimpan",
                    "    data yang bisa berubah. Penghitung menyimpan _jumlah di",
                    "    _PenghitungState.",
                    "",
                    "Setiap kali tombol ditekan, setState memberi tahu Flutter bahwa",
                    "state berubah. Flutter lalu memanggil build milik _PenghitungState",
                    "lagi di frame berikutnya. Garis bawah di depan nama artinya privat",
                    "untuk berkas itu.",
                ],
            },
            {
                "heading": "Tiga pohon di balik layar",
                "body": [
                    "Widget cuma cetak biru. Supaya bisa tampil, Flutter menyusun tiga",
                    "pohon yang saling terhubung:",
                    "",
                    "  1. Pohon widget, hasil fungsi build. Murah dibuat dan dibuang",
                    "     setiap kali build dipanggil.",
                    "  2. Pohon element. Satu element mewakili satu widget di posisi",
                    "     tertentu, dan element-lah yang bertahan dari frame ke frame.",
                    "     Objek State juga dipegang element, makanya _jumlah nggak",
                    "     hilang walau widget Penghitung dibuat ulang.",
                    "  3. Pohon render. Isinya RenderObject yang mengukur ukuran,",
                    "     menentukan posisi, lalu menggambar piksel.",
                    "",
                    "Saat build menghasilkan widget baru, element membandingkannya",
                    "dengan widget lama di posisi yang sama. Kalau tipe dan key-nya",
                    "sama, element dipakai ulang dan cuma diberi konfigurasi baru.",
                    "Kalau beda, element lama dibuang beserta state-nya, lalu dibuat",
                    "yang baru. Ini aturan yang sama dengan SwiftUI di bab sebelumnya:",
                    "identitas ditentukan tipe dan posisi.",
                    "",
                    "setState cuma menandai element milik State itu sebagai kotor. Di",
                    "frame berikutnya, yang dibangun ulang cuma pohon di bawahnya.",
                    "Widget yang ditulis dengan const, seperti const Text('Penghitung'),",
                    "adalah objek yang sama setiap kali, jadi Flutter melewatinya.",
                ],
            },
            {
                "heading": "Constraint turun, ukuran naik",
                "bahasa": "dart",
                "code": """Column(
  children: [
    const Text('Riwayat belanja'),
    Expanded(
      child: ListView.builder(
        itemCount: 1000,
        itemBuilder: (context, i) => ListTile(
          title: Text('Transaksi ${i + 1}'),
        ),
      ),
    ),
  ],
)""",
            },
            {
                "body": [
                    "Tata letak Flutter mengikuti satu aturan yang ditulis di",
                    "dokumentasinya: constraint turun, ukuran naik, dan induk menentukan",
                    "posisi. Induk memberi tahu anak batas lebar dan tinggi yang boleh",
                    "dipakai, anak memilih ukurannya di dalam batas itu, lalu induk",
                    "menaruhnya.",
                    "",
                    "Aturan itu menjelaskan dua error yang paling sering ditemui",
                    "pemula:",
                    "",
                    "  - Garis kuning-hitam bertuliskan RenderFlex overflowed by ...",
                    "    pixels. Anak di dalam Row atau Column butuh tempat lebih besar",
                    "    dari yang tersedia.",
                    "  - Vertical viewport was given unbounded height. ListView ditaruh",
                    "    langsung di dalam Column, padahal Column nggak memberi batas",
                    "    tinggi. Expanded seperti di contoh atas memberi ListView sisa",
                    "    tinggi yang ada.",
                    "",
                    "ListView.builder hanya membuat baris yang sedang terlihat, jadi",
                    "seribu transaksi tetap ringan. Padanannya LazyColumn di Compose.",
                ],
            },
            {
                "heading": "Impeller dan hot reload",
                "body": [
                    "Mesin render Flutter sekarang bernama Impeller, pengganti Skia.",
                    "Impeller menyiapkan shader sebelum aplikasi jalan, jadi animasi",
                    "pertama nggak tersendat karena menunggu shader dikompilasi. Menurut",
                    "dokumentasi Flutter saat materi ini ditulis:",
                    "",
                    "  - Di iOS, Impeller satu-satunya mesin render.",
                    "  - Di Android, Impeller aktif bawaan untuk API 29 ke atas. Perangkat",
                    "    lebih lama atau tanpa Vulkan memakai renderer OpenGL lama.",
                    "  - Di macOS, Windows, dan Linux, Impeller aktif bawaan sejak",
                    "    Flutter 3.47.",
                    "  - Di web, Flutter masih memakai Skia.",
                    "",
                    "Hot reload memasukkan kode baru ke aplikasi yang sedang jalan lalu",
                    "membangun ulang pohon widget, tanpa menghapus state. Kamu bisa",
                    "mengubah warna tombol di layar kelima tanpa login ulang. Yang nggak",
                    "ikut terulang adalah main() dan initState(). Hot restart memulai",
                    "ulang aplikasi dan state-nya hilang. Restart penuh dibutuhkan kalau",
                    "kamu mengubah kode Kotlin atau Swift di dalam proyek. Web sekarang",
                    "juga mendukung hot reload.",
                ],
            },
            {
                "heading": "Perintah sehari-hari",
                "bahasa": "terminal",
                "code": """flutter doctor
flutter create kasir
cd kasir
flutter run -d linux
flutter run -d chrome
flutter build appbundle""",
            },
            {
                "body": [
                    "flutter doctor memeriksa apa yang belum terpasang, misalnya Android",
                    "SDK atau paket pembangun aplikasi Linux. Selama flutter run jalan,",
                    "tekan r untuk hot reload dan R untuk hot restart. flutter build",
                    "appbundle menghasilkan berkas .aab untuk Play Store.",
                    "",
                    "Jebakan: mengubah isi initState lalu menekan r, dan heran kenapa",
                    "nggak ada yang berubah. initState cuma jalan sekali saat element",
                    "dibuat. Pakai hot restart untuk perubahan semacam itu.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Flutter dipakai untuk aplikasi pembayaran, aplikasi toko, dan",
                    "banyak aplikasi startup yang ingin satu tim merawat Android dan iOS",
                    "sekaligus. Bug yang berasal dari cara element dicocokkan termasuk",
                    "yang paling membingungkan di sana.",
                    "",
                    "Kasus kecil: di aplikasi daftar tugas, setiap baris adalah",
                    "StatefulWidget dengan kotak centang yang state-nya disimpan di",
                    "baris itu. Pengguna mencentang tugas pertama lalu menghapusnya.",
                    "Tiba-tiba tugas yang tadinya kedua ikut tercentang.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami penyebabnya. Sesudah tugas pertama dihapus, widget",
                    "     tugas kedua sekarang ada di posisi pertama. Tipenya sama,",
                    "     jadi Flutter memakai ulang element pertama beserta State-nya,",
                    "     termasuk centang tadi.",
                    "  2. Beri setiap baris key yang mengikuti datanya, bukan posisinya:",
                    "       BarisTugas(key: ValueKey(tugas.id), tugas: tugas)",
                    "  3. Uji lagi: hapus tugas yang tercentang. Centangnya harus ikut",
                    "     hilang bersama barisnya.",
                    "  4. Untuk perbaikan yang lebih kokoh, pindahkan status centang ke",
                    "     data tugas itu sendiri, jangan disimpan di State widget.",
                ],
            },
        ],
    },
    {
        "title": "23. State Management Flutter: setState, Riverpod, dan Bloc",
        "sections": [
            {
                "body": [
                    "setState cukup untuk data yang cuma dipakai satu widget, misalnya",
                    "kotak centang atau tab yang sedang aktif. Masalah muncul saat data",
                    "yang sama dibutuhkan banyak layar. Contohnya jumlah barang di",
                    "keranjang, yang tampil di ikon atas, di halaman produk, dan di",
                    "halaman bayar.",
                    "",
                    "Cara paling polos adalah mengangkat state ke induk bersama lalu",
                    "meneruskannya lewat parameter, tingkat demi tingkat. Untuk tiga",
                    "tingkat masih wajar. Untuk sepuluh tingkat, setiap widget di",
                    "tengah ikut menerima parameter yang nggak ia pakai, dan kode jadi",
                    "berantakan. Di titik ini orang mulai mencari pustaka state management.",
                    "",
                    "roadmap.sh Flutter mencantumkan Provider, Riverpod, Bloc, GetX, dan",
                    "Redux. Dua yang paling sering kamu temui di proyek tim sekarang",
                    "adalah Riverpod dan Bloc.",
                ],
            },
            {
                "heading": "Riverpod: keranjang yang dibagi banyak layar",
                "bahasa": "dart",
                "code": """import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

class Keranjang extends Notifier<List<String>> {
  @override
  List<String> build() => [];

  void tambah(String barang) {
    state = [...state, barang];
  }
}

final keranjangProvider =
    NotifierProvider<Keranjang, List<String>>(Keranjang.new);

class TombolKeranjang extends ConsumerWidget {
  const TombolKeranjang({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final isi = ref.watch(keranjangProvider);
    return TextButton(
      onPressed: () => ref.read(keranjangProvider.notifier).tambah('Kopi'),
      child: Text('Keranjang (${isi.length})'),
    );
  }
}

void main() => runApp(
      const ProviderScope(
        child: MaterialApp(home: Scaffold(body: Center(child: TombolKeranjang()))),
      ),
    );""",
            },
            {
                "body": [
                    "Provider adalah pustaka lama yang dibangun di atas InheritedWidget,",
                    "mekanisme bawaan Flutter untuk menitipkan data ke seluruh widget di",
                    "bawahnya. Riverpod adalah penerusnya dari penulis yang sama.",
                    "Bedanya, provider Riverpod nggak bergantung pada posisi di pohon",
                    "widget, jadi bisa dibaca dari mana saja dan kesalahan nama",
                    "ketahuan saat kompilasi.",
                    "",
                    "Versi terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "flutter_riverpod 3.4.3, lisensi MIT, dengan sekitar 3,82 juta",
                    "unduhan per minggu di pub.dev. Cara bacanya:",
                    "",
                    "  - Notifier menyimpan state dan fungsi untuk mengubahnya. build()",
                    "    memberi nilai awal.",
                    "  - ref.watch di dalam build membuat widget digambar ulang setiap",
                    "    nilainya berubah. ref.read dipakai di dalam aksi seperti",
                    "    onPressed, karena di sana kamu cuma perlu nilai saat itu.",
                    "  - ProviderScope di akar aplikasi wajib ada. Di situlah semua",
                    "    nilai provider disimpan.",
                    "",
                    "Riverpod 3.0 membawa beberapa perubahan yang membuat tutorial lama",
                    "kurang cocok. StateProvider, StateNotifierProvider, dan",
                    "ChangeNotifierProvider dipindah ke impor legacy karena nggak",
                    "disarankan lagi. Notifier dan NotifierProvider jadi cara utama.",
                    "Provider yang gagal sekarang juga dicoba ulang otomatis dengan jeda",
                    "yang makin panjang.",
                ],
            },
            {
                "heading": "Bloc: event masuk, state keluar",
                "bahasa": "dart",
                "code": """import 'package:flutter_bloc/flutter_bloc.dart';

sealed class EventSaldo {}

final class Tambah extends EventSaldo {
  Tambah(this.jumlah);
  final int jumlah;
}

final class Reset extends EventSaldo {}

class SaldoBloc extends Bloc<EventSaldo, int> {
  SaldoBloc() : super(0) {
    on<Tambah>((event, emit) => emit(state + event.jumlah));
    on<Reset>((event, emit) => emit(0));
  }
}

// Di widget:
// BlocBuilder<SaldoBloc, int>(builder: (context, saldo) => Text('Rp$saldo'))
// context.read<SaldoBloc>().add(Tambah(5000));""",
            },
            {
                "body": [
                    "Bloc memisahkan dua arah dengan tegas. Widget cuma boleh mengirim",
                    "event (Tambah, Reset). Bloc menerima event, menghitung state baru,",
                    "lalu memancarkannya lewat emit. BlocBuilder menggambar ulang widget",
                    "setiap ada state baru. Karena semua perubahan lewat event, setiap",
                    "transisi bisa dicatat dan diuji: state lama, event, state baru.",
                    "",
                    "Versi pustakanya flutter_bloc 9.1.1, lisensi MIT, dengan sekitar 8",
                    "ribu like di pub.dev. Rilis terakhirnya sekitar 17 bulan sebelum",
                    "materi ini ditulis, tapi pemakaiannya tetap luas, jadi statusnya",
                    "stabil dan matang. Ada juga versi ringannya, Cubit, yang memakai",
                    "fungsi biasa seperti increment() alih-alih kelas event.",
                    "",
                    "Satu aturan Bloc yang dipakai di latihan bab ini: Bloc dan Cubit",
                    "mengabaikan state kembar. Kalau state baru sama dengan state yang",
                    "sekarang, nggak ada perubahan yang dipancarkan dan widget nggak",
                    "digambar ulang.",
                    "",
                    "Jebakan: \"sama\" di sini memakai operator ==. Untuk state berupa",
                    "class buatanmu, == bawaan Dart cuma membandingkan identitas objek.",
                    "Dua objek berisi sama tetap dianggap beda, kecuali kamu menimpa ==",
                    "atau memakai paket seperti equatable.",
                ],
            },
            {
                "heading": "Memilih pola sesuai ukuran aplikasi",
                "body": [
                    "Nggak ada pola yang paling cocok untuk semua situasi. Pegangan",
                    "yang masuk akal:",
                    "",
                    "  - State milik satu widget, seperti kotak centang atau isian form:",
                    "    setState.",
                    "  - Beberapa layar berbagi data dan timnya kecil: Riverpod.",
                    "  - Tim besar yang butuh jejak setiap perubahan dan alur yang",
                    "    seragam: Bloc.",
                    "  - Proyek warisan: ikuti yang sudah dipakai dulu, baru",
                    "    pertimbangkan pindah.",
                    "",
                    "Dua nama lain yang mungkin kamu warisi: GetX, paket serba ada",
                    "yang menggabungkan state (Obx), navigasi (Get.to), dan dependency",
                    "injection (Get.put) dalam satu paket; dan Redux, pola satu store",
                    "global yang dikenal dari dunia React. Kalau mewarisi proyek GetX,",
                    "pahami dulu ketiga bagian itu sebelum mengubah apa pun.",
                    "",
                    "Jebakan: mengubah daftar di tempat, misalnya state.add(barang) di",
                    "Notifier Riverpod. Isi daftarnya memang berubah, tapi objeknya",
                    "masih yang lama, jadi Riverpod nggak tahu ada perubahan dan layar",
                    "nggak digambar ulang. Selalu buat daftar baru seperti",
                    "[...state, barang].",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Bug state management di aplikasi Flutter hampir selalu terlihat",
                    "sama dari luar: datanya sudah berubah, tapi layarnya nggak.",
                    "",
                    "Kasus kecil: di aplikasi toko berbasis Riverpod, angka di tombol",
                    "keranjang nggak bertambah saat pengguna menekan Tambah ke",
                    "keranjang. Kalau aplikasi dibuka ulang, angkanya baru benar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan widget tombol memakai ref.watch, bukan ref.read,",
                    "     untuk membaca keranjang di dalam build.",
                    "  2. Buka Notifier-nya. Kalau ada state.add(barang), itulah",
                    "     penyebabnya: daftarnya diubah di tempat.",
                    "  3. Ganti dengan daftar baru:",
                    "       state = [...state, barang];",
                    "  4. Kunci perbaikannya dengan tes tanpa layar:",
                    "       final c = ProviderContainer();",
                    "       c.read(keranjangProvider.notifier).tambah('Kopi');",
                    "       expect(c.read(keranjangProvider).length, 1);",
                    "  5. Jalankan dengan flutter test. Tes seperti ini jalan di Fedora",
                    "     tanpa emulator.",
                ],
            },
        ],
    },
    {
        "title": "24. React Native: Komponen Native dari JavaScript",
        "sections": [
            {
                "body": [
                    "React Native adalah kerangka buatan Meta untuk membuat aplikasi",
                    "Android dan iOS memakai React. Komponen yang kamu tulis berubah",
                    "jadi view asli milik sistem operasi, misalnya UILabel di iOS dan",
                    "TextView di Android. Jadi aplikasinya bukan halaman web yang",
                    "dibungkus. Versi stabil terbaru saat materi ini ditulis (Oktober",
                    "2026) adalah 0.88.0, rilis 15 Oktober 2026, dengan lisensi MIT.",
                    "",
                    "Angka pemakaiannya besar. Di Survei Stack Overflow 2024, React",
                    "Native dipakai 8,4% responden. Di State of JS 2024, ada 2.629",
                    "responden yang memakainya di tempat kerja, terbanyak di kategori",
                    "mobile dan desktop. Repositorinya punya sekitar 126 ribu bintang di",
                    "GitHub.",
                    "",
                    "Materi ini menganggap kamu sudah kenal JavaScript dan sedikit",
                    "React: komponen adalah fungsi yang mengembalikan tampilan, props",
                    "adalah parameternya, dan useState menyimpan data yang bisa berubah.",
                    "Kode React Native biasanya ditulis dengan TypeScript, tapi contoh",
                    "di sini memakai JavaScript supaya lebih ringkas.",
                ],
            },
            {
                "heading": "Komponen pertama",
                "bahasa": "jsx",
                "code": """import { useState } from 'react';
import { View, Text, Pressable, StyleSheet } from 'react-native';

export default function Penghitung() {
  const [jumlah, setJumlah] = useState(0);
  return (
    <View style={gaya.wadah}>
      <Text style={gaya.angka}>Diklik {jumlah} kali</Text>
      <Pressable style={gaya.tombol} onPress={() => setJumlah(jumlah + 1)}>
        <Text style={gaya.teksTombol}>Tambah</Text>
      </Pressable>
    </View>
  );
}

const gaya = StyleSheet.create({
  wadah: { flex: 1, alignItems: 'center', justifyContent: 'center', gap: 12 },
  angka: { fontSize: 24 },
  tombol: { backgroundColor: '#1f6feb', paddingHorizontal: 20, paddingVertical: 10, borderRadius: 8 },
  teksTombol: { color: 'white' },
});""",
            },
            {
                "body": [
                    "Kalau kamu pernah menulis React untuk web, bentuknya sama. Yang",
                    "beda adalah bahan bangunannya:",
                    "",
                    "  - Nggak ada div, span, atau p. Penggantinya View untuk kotak,",
                    "    Text untuk tulisan, Image, ScrollView, FlatList untuk daftar",
                    "    panjang, TextInput untuk isian, dan Pressable untuk apa pun yang",
                    "    bisa disentuh.",
                    "  - Semua tulisan wajib berada di dalam Text. Teks lepas di dalam",
                    "    View memunculkan error Text strings must be rendered within a",
                    "    <Text> component.",
                    "  - Gaya ditulis sebagai objek JavaScript dengan nama camelCase,",
                    "    seperti backgroundColor. Nggak ada berkas CSS dan nggak ada",
                    "    cascade, kecuali Text di dalam Text yang mewarisi gaya induknya.",
                    "  - Tata letaknya Flexbox, tapi arah bawaannya kolom (atas ke",
                    "    bawah). Di CSS web, arah bawaan flex adalah baris.",
                    "  - Angka ukuran nggak memakai px. Satuannya piksel yang",
                    "    disesuaikan kepadatan layar, jadi 24 terlihat kira-kira sama",
                    "    besar di ponsel murah dan ponsel mahal.",
                ],
            },
            {
                "heading": "Dari JavaScript ke layar native",
                "body": [
                    "Kodemu jalan di mesin JavaScript di dalam aplikasi. Mesin bawaannya",
                    "Hermes, buatan Meta, yang jadi bawaan sejak React Native 0.70.",
                    "Hermes mengubah JavaScript jadi bytecode saat build, jadi aplikasi",
                    "lebih cepat terbuka.",
                    "",
                    "Sejak versi 0.82 (Oktober 2025), React Native berjalan sepenuhnya",
                    "di atas New Architecture. Isinya tiga bagian:",
                    "",
                    "  1. JSI (JavaScript Interface), lapisan C++ yang membuat",
                    "     JavaScript bisa memegang rujukan ke objek native dan memanggil",
                    "     fungsinya langsung, termasuk secara sinkron kalau perlu.",
                    "  2. Fabric, sistem render baru. Hasil render React diubah jadi",
                    "     shadow tree di C++, posisinya dihitung Yoga (mesin Flexbox",
                    "     milik React Native), lalu view native dibuat atau diubah.",
                    "  3. TurboModules, modul native yang baru dimuat saat pertama",
                    "     dipakai, dengan antarmuka bertipe yang dibuatkan alat Codegen.",
                    "",
                    "Sebelum itu, ada jembatan (bridge): setiap panggilan ke native",
                    "diubah jadi pesan JSON, dikumpulkan, lalu dikirim secara asinkron.",
                    "Simulasi di bawah menunjukkan beda rasanya.",
                ],
            },
            {
                "heading": "Simulasi: jembatan lama dan JSI",
                "code": """// Simulasi kecil: jembatan lama dibanding pemanggilan langsung ala JSI.
const modulNative = {
  lebarLayar: () => 393,
};

// Jembatan lama: panggilan diubah jadi teks JSON, dikirim belakangan,
// dan jawabannya baru datang di putaran event loop berikutnya.
function jembatanLama(metode) {
  const pesan = JSON.stringify({ modul: 'Layar', metode });
  return new Promise((selesai) => {
    setTimeout(() => {
      const diterima = JSON.parse(pesan);
      selesai(modulNative[diterima.metode]());
    }, 0);
  });
}

// JSI: JavaScript memegang rujukan ke fungsi native dan memanggilnya langsung.
function lewatJsi(metode) {
  return modulNative[metode]();
}

console.log('langkah 1: minta lebar lewat jembatan lama');
jembatanLama('lebarLayar').then((lebar) => {
  console.log('langkah 3: jembatan lama baru menjawab', lebar);
});
console.log('langkah 2: JSI langsung menjawab', lewatJsi('lebarLayar'));""",
            },
            {
                "body": [
                    "Keluarannya:",
                    "  langkah 1: minta lebar lewat jembatan lama",
                    "  langkah 2: JSI langsung menjawab 393",
                    "  langkah 3: jembatan lama baru menjawab 393",
                    "",
                    "Jembatan lama menjawab paling akhir walaupun dipanggil paling awal,",
                    "karena pesannya harus diubah jadi teks, dikirim, lalu dibaca lagi",
                    "di seberang. Untuk satu panggilan selisihnya kecil. Untuk animasi",
                    "atau gulir yang butuh ratusan panggilan per detik, selisih itu",
                    "terasa sebagai layar yang tersendat. Simulasi ini tentu",
                    "menyederhanakan: React Native asli memakai C++ di bawahnya.",
                    "",
                    "Catatan rilis 0.82 menulis bahwa menyetel newArchEnabled=false di",
                    "Android, atau RCT_NEW_ARCH_ENABLED=0 saat memasang CocoaPods di",
                    "iOS, sekarang diabaikan. Aplikasimu tetap jalan di New",
                    "Architecture. Versi itu juga membawa React 19.1.1 dan versi",
                    "percobaan Hermes V1.",
                ],
            },
            {
                "heading": "React Native dibanding pilihan lain",
                "body": [
                    "Dibanding Flutter, React Native memakai view bawaan platform,",
                    "sedangkan Flutter menggambar sendiri. Akibatnya tampilan React",
                    "Native otomatis terasa seperti aplikasi platform itu, dan tim yang",
                    "sudah bisa React serta TypeScript langsung produktif.",
                    "",
                    "Dibanding aplikasi hybrid seperti Capacitor (bab 08), React Native",
                    "nggak memakai WebView. Daftar panjang dan animasi biasanya lebih",
                    "mulus.",
                    "",
                    "Pilih React Native kalau timmu kuat di React, kamu ingin tampilan",
                    "terasa native, atau sebagian logika ingin dibagi dengan aplikasi",
                    "web. Pertimbangkan pilihan lain untuk aplikasi yang hampir semua",
                    "fiturnya khas satu platform, atau untuk grafis berat seperti game.",
                    "",
                    "Dokumentasi resmi React Native sekarang menyarankan memulai proyek",
                    "baru dengan kerangka seperti Expo, yang dibahas di materi",
                    "berikutnya.",
                    "",
                    "Jebakan: tutorial sebelum akhir 2025 banyak yang masih membahas",
                    "bridge, NativeModules gaya lama, atau langkah mematikan New",
                    "Architecture. Di React Native 0.82 ke atas, langkah itu nggak",
                    "berpengaruh lagi. Cek tanggal tutorial dan versi React Native-nya",
                    "sebelum mengikutinya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak tim startup memakai React Native supaya programmer web",
                    "mereka bisa ikut membangun aplikasi ponsel. Pustaka pihak ketiga",
                    "yang belum mendukung New Architecture jadi masalah yang paling",
                    "sering muncul saat proyek lama dinaikkan versinya.",
                    "",
                    "Kasus kecil: proyek kantor dinaikkan ke React Native 0.88. Satu",
                    "pustaka peta mulai error, dan tutorial tahun 2023 menyarankan",
                    "menyetel newArchEnabled=false. Kamu sudah melakukannya, tapi",
                    "error-nya tetap sama.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cek versi react-native di package.json. Mulai 0.82, saklar",
                    "     newArchEnabled diabaikan, jadi langkah dari tutorial itu",
                    "     memang nggak akan berpengaruh.",
                    "  2. Cari pustaka itu di React Native Directory",
                    "     (reactnative.directory). Di sana tercatat apakah sebuah",
                    "     pustaka sudah mendukung New Architecture.",
                    "  3. Naikkan pustakanya ke versi yang mendukung, atau cari",
                    "     pengganti yang aktif dirawat.",
                    "  4. Kalau proyeknya memakai Expo, jalankan npx expo-doctor untuk",
                    "     menemukan versi paket yang nggak cocok dengan SDK-mu.",
                    "  5. Hapus kembali baris newArchEnabled=false supaya nggak",
                    "     membingungkan orang berikutnya.",
                ],
            },
        ],
    },
    {
        "title": "25. Expo, EAS Build, dan Jalur iOS dari Linux",
        "sections": [
            {
                "body": [
                    "Expo adalah kerangka dan kumpulan layanan di atas React Native.",
                    "Isinya tiga hal: SDK berisi modul siap pakai (kamera, lokasi,",
                    "notifikasi, penyimpanan, dan banyak lagi), Expo Router untuk",
                    "navigasi, dan layanan cloud bernama EAS (Expo Application",
                    "Services). Versi terbaru saat materi ini ditulis (Oktober 2026)",
                    "adalah SDK 58, rilis 15 Oktober 2026, yang memakai React Native",
                    "0.88. SDK-nya berlisensi MIT, sedangkan layanan cloud-nya berbayar",
                    "dengan kuota gratis.",
                    "",
                    "Di State of JS 2024, 1.288 responden memakai Expo di tempat kerja.",
                    "Buat kamu yang memakai Fedora tanpa Mac, Expo adalah jalur paling",
                    "realistis untuk menghasilkan aplikasi iPhone, karena build iOS-nya",
                    "bisa dikerjakan mesin macOS milik layanan build Expo.",
                ],
            },
            {
                "heading": "Membuat proyek dan menjalankannya",
                "bahasa": "terminal",
                "code": """npx create-expo-app@latest kasir-saku
cd kasir-saku
npx expo start""",
            },
            {
                "body": [
                    "npx expo start menyalakan server pengembangan dan menampilkan kode",
                    "QR di terminal. Dari situ ada beberapa cara melihat aplikasinya:",
                    "",
                    "  - Tekan a untuk membukanya di emulator Android dari Android",
                    "    Studio (bab 02).",
                    "  - Tekan w untuk membukanya di browser.",
                    "  - Di ponsel Android atau iPhone, pasang aplikasi Expo Go dari",
                    "    toko, lalu pindai kode QR-nya. Laptop dan ponsel harus di",
                    "    jaringan Wi-Fi yang sama.",
                    "",
                    "Cara ketiga artinya kamu bisa melihat aplikasimu jalan di iPhone",
                    "tanpa Mac sama sekali. SDK 58 butuh Node.js 22.13 atau lebih baru.",
                    "Menurut catatan rilisnya, Expo Go untuk SDK 58 menyusul di App",
                    "Store dan Google Play beberapa minggu sesudah 15 Oktober 2026. Kalau",
                    "Expo Go di ponselmu belum mendukung SDK proyekmu, pakai development",
                    "build yang dijelaskan di bawah.",
                ],
            },
            {
                "heading": "Expo Go dan development build",
                "bahasa": "json",
                "code": """{
  "expo": {
    "name": "Kasir Saku",
    "slug": "kasir-saku",
    "scheme": "kasirsaku",
    "ios": { "bundleIdentifier": "id.contoh.kasirsaku" },
    "android": { "package": "id.contoh.kasirsaku" },
    "plugins": ["expo-camera"]
  }
}""",
            },
            {
                "body": [
                    "Expo Go adalah aplikasi taman bermain yang sudah berisi sekumpulan",
                    "modul native tertentu. Kodemu yang JavaScript dimuat ke dalamnya.",
                    "Dokumentasi Expo sendiri menyebutnya tempat mencoba untuk pelajar,",
                    "terbatas, dan nggak cocok untuk proyek produksi. Kamu nggak bisa",
                    "menambah pustaka berisi kode native yang nggak ada di Expo Go.",
                    "",
                    "Development build adalah versi Expo Go milikmu sendiri: aplikasimu,",
                    "dibangun dengan pustaka expo-dev-client, berisi modul native apa",
                    "pun yang kamu butuhkan. Development build Android bisa dibangun di",
                    "Fedora dengan Android Studio. Development build iOS butuh Mac atau",
                    "build di cloud.",
                    "",
                    "Berkas app.json di atas adalah pusat konfigurasinya. Folder android/",
                    "dan ios/ bisa dihasilkan dari berkas ini dengan npx expo prebuild.",
                    "Pustaka seperti expo-camera membawa config plugin yang menambahkan",
                    "izin kamera ke kedua folder itu secara otomatis. bundleIdentifier",
                    "dan package adalah nama unik aplikasimu di App Store dan Play",
                    "Store, dan nggak bisa diganti sesudah rilis.",
                    "",
                    "Jebakan: pasang pustaka dengan npx expo install, bukan npm install",
                    "biasa. npx expo install memilih versi yang cocok dengan SDK",
                    "proyekmu. npm install mengambil versi terbaru, yang bisa jadi belum",
                    "cocok.",
                ],
            },
            {
                "heading": "Membangun iOS tanpa Mac",
                "bahasa": "terminal",
                "code": """npm install --global eas-cli
eas login
eas build:configure
eas build --platform android
eas build --platform ios
eas submit --platform ios""",
            },
            {
                "body": [
                    "eas build:configure membuat berkas eas.json berisi profil build,",
                    "misalnya development, preview, dan production. eas build --platform",
                    "ios mengunggah kodemu ke server Expo. Di sana mesin macOS menjalankan",
                    "Xcode dan menghasilkan berkas .ipa yang sudah ditandatangani. Untuk",
                    "Android hasilnya berkas .aab. eas submit mengunggah hasil build ke",
                    "App Store Connect atau Play Console.",
                    "",
                    "Tanda tangan iOS butuh akun Apple Developer Program, 99 dolar AS per",
                    "tahun. Layanan build Expo bisa membuat dan menyimpan sertifikat",
                    "serta provisioning profile untukmu, jadi kamu nggak perlu membuka",
                    "Xcode. Tanpa akun itu, hasil build nggak bisa dipasang di iPhone",
                    "sungguhan maupun dikirim ke TestFlight.",
                    "",
                    "Menurut halaman harga Expo saat materi ini ditulis, paket gratis",
                    "memberi 15 build Android dan 15 build iOS per bulan. Build gratis",
                    "masuk antrean berprioritas rendah, dengan batas waktu 45 menit per",
                    "build. Paket",
                    "berbayar termurah, Starter, mulai 19 dolar AS per bulan. Harga bisa",
                    "berubah, jadi cek lagi sebelum merencanakan anggaran.",
                    "",
                    "Ada juga EAS Update, yang mengirim perubahan JavaScript ke aplikasi",
                    "yang sudah terpasang tanpa build ulang. Perubahan kode native tetap",
                    "butuh build baru dan lewat toko.",
                ],
            },
            {
                "heading": "Kapan Expo, kapan React Native polos",
                "body": [
                    "Untuk proyek baru, mulai dengan Expo. Kebutuhan kode native khusus",
                    "tetap bisa dipenuhi lewat config plugin atau modul native buatanmu",
                    "sendiri.",
                    "",
                    "React Native tanpa Expo biasanya dipakai saat perusahaan sudah",
                    "punya aplikasi native besar lalu menyisipkan beberapa layar React",
                    "Native ke dalamnya. Alasan lainnya, tim ingin memegang sendiri",
                    "seluruh folder android/ dan ios/.",
                    "",
                    "Jebakan: menyunting folder android/ atau ios/ dengan tangan di",
                    "proyek yang memakai prebuild. Perintah prebuild berikutnya bisa",
                    "menimpa suntinganmu. Taruh perubahan itu di app.json atau di config",
                    "plugin, supaya selalu ikut dihasilkan ulang.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Freelancer dan tim kecil sering memakai Expo untuk mengerjakan",
                    "aplikasi Android dan iPhone sekaligus dari laptop Windows atau",
                    "Linux. Akun Apple Developer-nya biasanya atas nama klien, karena",
                    "aplikasinya terbit atas nama usaha klien.",
                    "",
                    "Kasus kecil: kedai kopi langganan minta aplikasi pesan ulang untuk",
                    "Android dan iPhone. Kamu cuma punya laptop Fedora, dan pemilik",
                    "kedai memakai iPhone.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat proyek dengan npx create-expo-app@latest, lalu kerjakan",
                    "     di emulator Android dan browser.",
                    "  2. Tunjukkan kemajuan ke pemilik kedai lewat Expo Go di",
                    "     iPhone-nya, selama fiturnya cuma memakai modul yang ada di",
                    "     Expo Go.",
                    "  3. Pasang setiap pustaka dengan npx expo install supaya versinya",
                    "     cocok dengan SDK.",
                    "  4. Minta pemilik kedai mendaftar Apple Developer Program atas",
                    "     nama usahanya, lalu undang akunmu sebagai anggota tim.",
                    "  5. Jalankan eas build --platform ios, lalu eas submit --platform",
                    "     ios, dan bagikan versi uji lewat TestFlight.",
                    "  6. Rencanakan jumlah build. Dengan paket gratis, 15 build iOS per",
                    "     bulan cukup kalau kamu nggak membangun ulang untuk setiap",
                    "     perubahan kecil.",
                ],
            },
        ],
    },
    {
        "title": "26. Navigasi dengan React Navigation dan Expo Router",
        "sections": [
            {
                "body": [
                    "Di web, perpindahan halaman diurus alamat URL dan riwayat browser.",
                    "Di aplikasi ponsel, perpindahan layar diurus navigator. Bentuk yang",
                    "paling umum adalah stack: layar baru ditumpuk di atas layar lama,",
                    "dan tombol kembali (tombol Back di Android, geser dari tepi kiri di",
                    "iPhone) membuang layar teratas. Bentuk lainnya tab di bagian bawah",
                    "dan drawer yang meluncur dari samping.",
                    "",
                    "React Native nggak punya navigator bawaan. Ada dua pilihan yang",
                    "umum:",
                    "",
                    "  - React Navigation, pustaka navigasi standar React Native. Versi",
                    "    terbarunya @react-navigation/native 7.5.1 (13 Oktober 2026),",
                    "    sementara versi 8 masih alfa.",
                    "  - Expo Router, yang membuat rute dari susunan berkas dan",
                    "    dibangun di atas React Navigation.",
                ],
            },
            {
                "heading": "Stack dengan React Navigation",
                "bahasa": "jsx",
                "code": """import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import { Button, Text, View } from 'react-native';

const Stack = createNativeStackNavigator();

function Beranda({ navigation }) {
  return (
    <View>
      <Text>Menu hari ini</Text>
      <Button title="Lihat kopi" onPress={() => navigation.navigate('Produk', { id: 7 })} />
    </View>
  );
}

function Produk({ route, navigation }) {
  return (
    <View>
      <Text>Produk nomor {route.params.id}</Text>
      <Button title="Produk serupa" onPress={() => navigation.push('Produk', { id: 9 })} />
      <Button title="Kembali" onPress={() => navigation.goBack()} />
    </View>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Beranda" component={Beranda} />
        <Stack.Screen name="Produk" component={Produk} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}""",
            },
            {
                "body": [
                    "Isi navigator stack berupa daftar layar. Setiap aksi",
                    "mengubah daftar itu:",
                    "",
                    "  - push('Produk', ...) selalu menambah layar baru di atas, walau",
                    "    layar dengan nama sama sudah ada. Cocok untuk produk serupa yang",
                    "    membuka produk lain.",
                    "  - goBack() membuang layar teratas.",
                    "  - reset(...) mengganti seluruh isi stack. Dipakai sesudah login,",
                    "    supaya tombol kembali nggak membawa pengguna ke layar login.",
                    "  - navigate('Produk', ...) di React Navigation 7 tetap di layar",
                    "    itu kalau sudah sedang tampil, dan menambah layar baru kalau",
                    "    belum.",
                    "  - popTo('Beranda') kembali ke layar itu kalau ada di stack.",
                    "",
                    "Jebakan: di versi 6, navigate kembali ke layar yang sudah ada di",
                    "stack. Versi 7 mengubahnya, dan menambah popTo untuk perilaku",
                    "lama itu. Selama migrasi tersedia navigateDeprecated. Kalau",
                    "tutorial yang kamu ikuti menulis \"navigate akan kembali ke layar",
                    "sebelumnya\", cek dulu versi yang dipakainya.",
                    "",
                    "Data antar layar dikirim lewat params, lalu dibaca dengan",
                    "route.params di layar tujuan.",
                ],
            },
            {
                "heading": "Expo Router: berkas sebagai rute",
                "bahasa": "teks",
                "code": """app/
  _layout.tsx          pembungkus semua layar (Stack)
  index.tsx            /
  (tabs)/
    _layout.tsx        tab di bagian bawah
    profil.tsx         /profil
  produk/
    [id].tsx           /produk/7, /produk/9, ...
  bantuan/
    [...topik].tsx     /bantuan/akun/sandi
  +not-found.tsx       layar kalau alamat nggak cocok""",
            },
            {
                "heading": "Isi app/produk/[id].tsx",
                "bahasa": "tsx",
                "code": """import { Link, useLocalSearchParams } from 'expo-router';
import { Text, View } from 'react-native';

export default function HalamanProduk() {
  const { id } = useLocalSearchParams<{ id: string }>();
  return (
    <View>
      <Text>Produk nomor {id}</Text>
      <Link href="/produk/9">Lihat produk lain</Link>
    </View>
  );
}""",
            },
            {
                "body": [
                    "Di Expo Router, setiap berkas di folder app/ adalah satu layar, dan",
                    "jalurnya jadi alamat layar itu. Aturannya:",
                    "",
                    "  - index.tsx mewakili folder tempatnya. app/index.tsx adalah /.",
                    "  - Folder dalam kurung, seperti (tabs), nggak ikut jadi bagian",
                    "    alamat. Gunanya mengelompokkan layar di bawah satu tata letak,",
                    "    misalnya tab bawah.",
                    "  - [id] cocok dengan satu ruas alamat apa pun dan menjadikannya",
                    "    parameter. [...topik] cocok dengan satu ruas atau lebih.",
                    "  - _layout.tsx bukan layar. Ia menentukan navigator untuk",
                    "    foldernya, misalnya Stack atau Tabs.",
                    "  - +not-found.tsx tampil kalau nggak ada rute yang cocok.",
                    "",
                    "Untuk berpindah, pakai komponen Link seperti tautan web, atau objek",
                    "router. Dokumentasi Expo Router menulis bahwa router.navigate akan",
                    "menambah layar baru, atau mundur ke rute yang sudah ada di stack.",
                    "router.push selalu menambah, router.back mundur satu, dan",
                    "router.replace mengganti layar sekarang.",
                    "",
                    "Karena setiap layar punya alamat, deep link didapat hampir gratis.",
                    "Dengan scheme kasirsaku di app.json, tautan kasirsaku://produk/7",
                    "langsung membuka layar produk nomor 7. Di React Navigation, deep",
                    "link butuh konfigurasi linking yang ditulis sendiri.",
                    "",
                    "Ingat: parameter dari alamat selalu berupa teks. id di contoh atas",
                    "bernilai \"7\", bukan angka 7. Ubah dengan Number(id) sebelum",
                    "dipakai menghitung atau dibandingkan dengan angka.",
                ],
            },
            {
                "heading": "Memilih salah satu",
                "body": [
                    "Untuk proyek Expo baru, Expo Router jadi pilihan yang wajar karena",
                    "template bawaannya sudah memakainya. Untuk proyek React Native",
                    "lama, atau tim yang lebih suka menulis daftar layar di kode,",
                    "React Navigation langsung tetap pilihan yang matang. Di baliknya",
                    "keduanya memakai mesin yang sama, jadi konsep stack, tab, dan",
                    "params berlaku untuk dua-duanya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hampir setiap aplikasi dengan akun pengguna punya alur masuk lalu",
                    "beranda, dan bug navigasi yang paling sering dilaporkan pengguna",
                    "muncul di perpindahan itu.",
                    "",
                    "Kasus kecil: sesudah login berhasil, pengguna Android menekan",
                    "tombol Back dan malah kembali ke layar login, lengkap dengan isian",
                    "sandi yang masih terisi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Gambar isi stack-nya. Sesudah login dengan navigate atau push,",
                    "     isinya [Masuk, Beranda], jadi Back membuang Beranda.",
                    "  2. Di React Navigation, ganti seluruh stack sesudah login:",
                    "       navigation.reset({ index: 0, routes: [{ name: 'Beranda' }] });",
                    "  3. Di Expo Router, ganti layar sekarang alih-alih menambah:",
                    "       router.replace('/');",
                    "  4. Untuk layar yang wajib login, arahkan pengguna yang belum",
                    "     masuk ke layar login dengan komponen Redirect dari",
                    "     expo-router, jangan sebaliknya.",
                    "  5. Uji lagi dengan tombol Back dan gerakan geser kembali di",
                    "     iPhone.",
                ],
            },
        ],
    },
    {
        "title": "27. Kotlin Multiplatform dan Compose Multiplatform",
        "sections": [
            {
                "body": [
                    "Kotlin Multiplatform (KMP) adalah teknologi JetBrains untuk",
                    "berbagi kode Kotlin antara Android, iOS, desktop, web, dan server.",
                    "Yang biasanya dibagi adalah logika: model data, aturan bisnis,",
                    "pemanggilan jaringan, dan database lokal. Tampilannya boleh tetap",
                    "native, misalnya Compose di Android dan SwiftUI di iOS.",
                    "",
                    "KMP stabil sejak Kotlin 1.9.20 (November 2023), dan versinya ikut",
                    "Kotlin. Saat materi ini ditulis (Oktober 2026), versi terbarunya",
                    "Kotlin 2.4.21, rilis 8 Oktober 2026, dengan lisensi Apache 2.0.",
                    "Beberapa pustaka Jetpack yang kamu kenal dari bab 04, seperti Room,",
                    "DataStore, dan ViewModel, sekarang juga mendukung KMP.",
                    "",
                    "Caranya: kode yang sama dikompilasi berbeda untuk tiap target. Untuk",
                    "Android jadi bytecode JVM seperti biasa. Untuk iOS, Kotlin/Native",
                    "mengubahnya jadi kode mesin dan membungkusnya sebagai framework yang",
                    "bisa dipanggil dari Swift. Untuk web, jadi JavaScript atau",
                    "WebAssembly.",
                    "",
                    "Compose Multiplatform melangkah lebih jauh: tampilannya ikut dibagi.",
                    "Ini versi Jetpack Compose buatan JetBrains yang jalan di Android,",
                    "iOS, desktop, dan web. Versi terbarunya 1.12.2 (15 Oktober 2026).",
                    "Menurut dokumentasi Kotlin, dukungan Android, iOS, dan desktop JVM",
                    "sudah stabil, sedangkan web lewat Kotlin/Wasm masih Beta.",
                ],
            },
            {
                "heading": "Susunan proyek KMP",
                "bahasa": "teks",
                "code": """kasir/
  shared/
    src/
      commonMain/kotlin/    logika bersama: model, aturan, repository
      androidMain/kotlin/   bagian khusus Android (actual)
      iosMain/kotlin/       bagian khusus iOS (actual)
      commonTest/kotlin/    tes untuk logika bersama
  androidApp/               aplikasi Android: Activity dan UI Compose
  iosApp/                   proyek Xcode: UI SwiftUI yang memanggil shared""",
            },
            {
                "body": [
                    "Nama foldernya bisa sedikit beda tergantung template. Template",
                    "baru dari JetBrains, misalnya, sering memakai composeApp/ untuk",
                    "aplikasi yang tampilannya ikut dibagi. Polanya tetap sama: satu",
                    "modul bersama, plus satu folder per platform.",
                    "",
                    "Kode di commonMain cuma boleh memakai Kotlin murni dan pustaka",
                    "multiplatform. java.io.File atau android.content.Context nggak",
                    "tersedia di sana, karena keduanya nggak ada di iOS. Kode yang",
                    "butuh API khas platform ditaruh di androidMain atau iosMain.",
                ],
            },
            {
                "heading": "expect dan actual",
                "bahasa": "kotlin",
                "code": """// commonMain/kotlin/Platform.kt
expect fun namaPlatform(): String

class Sapaan {
    fun sapa(): String = "Halo dari ${namaPlatform()}"
}

// androidMain/kotlin/Platform.android.kt
actual fun namaPlatform(): String =
    "Android ${android.os.Build.VERSION.SDK_INT}"

// iosMain/kotlin/Platform.ios.kt
actual fun namaPlatform(): String =
    platform.UIKit.UIDevice.currentDevice.systemName() + " " +
        platform.UIKit.UIDevice.currentDevice.systemVersion""",
            },
            {
                "body": [
                    "Blok di atas sebetulnya tiga berkas. expect di commonMain berjanji",
                    "bahwa fungsi namaPlatform ada, tanpa isi. Setiap platform menepati",
                    "janji itu dengan actual di paket yang sama. Compiler memeriksa",
                    "bahwa setiap expect punya actual di semua target. Kalau iosMain",
                    "lupa, build iOS gagal.",
                    "",
                    "Dokumentasi Kotlin memberi dua catatan penting. expect dan actual",
                    "untuk class masih Beta. Lalu untuk kasus sederhana, mereka",
                    "menyarankan interface biasa: commonMain mendefinisikan interface,",
                    "tiap platform memberi implementasinya, lalu implementasi itu",
                    "disuntikkan seperti dependency injection di bab 04. Dengan cara",
                    "itu, tes bisa memakai implementasi palsu.",
                ],
            },
            {
                "heading": "Tampilan yang ikut dibagi",
                "bahasa": "kotlin",
                "code": """@Composable
fun LayarSapaan(sapaan: Sapaan) {
    var tampil by remember { mutableStateOf(false) }
    Column(Modifier.padding(16.dp)) {
        Button(onClick = { tampil = !tampil }) {
            Text("Sapa")
        }
        if (tampil) Text(sapaan.sapa())
    }
}""",
            },
            {
                "body": [
                    "Composable di atas ditulis persis seperti di bab 03. Dengan",
                    "Compose Multiplatform, fungsi yang sama dipakai di Android, di iOS",
                    "(dibungkus ComposeUIViewController lalu ditaruh di aplikasi Swift),",
                    "dan di desktop sebagai jendela JVM. Target desktop berguna buat",
                    "kamu: tampilannya bisa dicoba di Fedora tanpa emulator.",
                    "",
                    "Jadi ada dua cara memakai KMP:",
                    "",
                    "  1. Berbagi logika saja. Tampilan tetap ditulis dua kali, Compose",
                    "     dan SwiftUI, supaya terasa paling native di tiap platform.",
                    "     Cara ini juga paling gampang dipasang di aplikasi yang sudah",
                    "     ada: mulai dari satu modul kecil, misalnya aturan diskon.",
                    "  2. Berbagi logika dan tampilan dengan Compose Multiplatform.",
                    "     Kodenya jauh lebih sedikit. Di iOS, Compose menggambar",
                    "     tampilannya sendiri, mirip Flutter, jadi tampilannya nggak",
                    "     otomatis memakai komponen iOS asli.",
                    "",
                    "Pustaka yang sudah multiplatform dan sering dipakai bersama KMP:",
                    "Ktor Client untuk HTTP, kotlinx.serialization untuk JSON,",
                    "kotlinx.coroutines, SQLDelight atau Room untuk database, dan Koin",
                    "untuk dependency injection.",
                ],
            },
            {
                "heading": "Batas yang perlu kamu tahu",
                "body": [
                    "Membangun target iOS tetap butuh macOS dan Xcode, karena",
                    "Kotlin/Native memakai SDK iOS milik Apple. Di Fedora kamu bisa",
                    "menulis commonMain, membangun aplikasi Android dan desktop, serta",
                    "menjalankan tes logika bersama untuk target JVM atau Android.",
                    "Bagian iOS dibangun di Mac atau di layanan CI bermesin macOS.",
                    "",
                    "Kode Kotlin terlihat dari Swift lewat header Objective-C. Akibatnya,",
                    "beberapa fitur Kotlin seperti suspend function dan sealed class",
                    "terasa kurang alami saat dipanggil dari Swift. Tim iOS biasanya",
                    "perlu sedikit kode pembungkus.",
                    "",
                    "Dibanding Flutter dan React Native, kekuatan KMP ada di adopsi",
                    "bertahap. Kamu nggak perlu menulis ulang aplikasi. Syaratnya, tim",
                    "menguasai Kotlin, dan tim iOS mau memakai modul yang ditulis dalam",
                    "Kotlin.",
                    "",
                    "Jebakan: menaruh semua hal di expect dan actual. Kalau yang",
                    "dibutuhkan cuma satu kemampuan platform, interface ditambah",
                    "implementasi per platform lebih mudah diuji dan diganti.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perusahaan yang punya aplikasi Android dan iOS native sering",
                    "memakai KMP untuk lapisan data saja. Satu modul bersama berisi",
                    "pemanggilan API, cache, dan aturan bisnis. Tampilannya tetap",
                    "dirawat tim masing-masing.",
                    "",
                    "Kasus kecil: aplikasi kasir punya aturan \"diskon 10% untuk belanja",
                    "di atas Rp100.000, maksimal Rp15.000\". Untuk belanja Rp95.000",
                    "dengan ongkos kirim Rp5.000, Android memberi diskon, iOS nggak.",
                    "Ternyata aturan itu ditulis dua kali, dan tim iOS menghitung",
                    "ongkos kirim sebagai bagian belanja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturan diskon sekali di commonMain, dengan nama",
                    "     parameter yang jelas:",
                    "       fun diskon(belanja: Long, ongkir: Long): Long =",
                    "           if (belanja > 100_000) minOf(belanja / 10, 15_000) else 0",
                    "  2. Tulis tes di commonTest untuk batasnya: Rp100.000 pas,",
                    "     Rp100.001, dan belanja besar yang kena batas Rp15.000.",
                    "  3. Jalankan tes itu di Fedora untuk target JVM atau Android.",
                    "  4. Android memanggil fungsi itu langsung. iOS memanggilnya lewat",
                    "     framework shared yang dibangun di Mac atau CI macOS.",
                    "  5. Hapus dua versi lama supaya nggak ada lagi aturan kembar.",
                ],
            },
        ],
    },
    {
        "title": "28. Aplikasi Hybrid: Ionic, Capacitor, dan Cordova",
        "sections": [
            {
                "body": [
                    "Aplikasi hybrid adalah aplikasi web (HTML, CSS, JavaScript) yang",
                    "dijalankan di dalam WebView, yaitu komponen browser yang ditanam di",
                    "aplikasi native. Di iOS komponen itu WKWebView, di Android Android",
                    "System WebView yang berbasis Chromium. Fitur yang nggak tersedia",
                    "di browser, seperti kamera penuh atau penyimpanan aman, dipanggil",
                    "lewat plugin native.",
                    "",
                    "Bedakan dengan dua jalur di bab sebelumnya. React Native memakai",
                    "view native asli, Flutter menggambar sendiri, dan hybrid memakai",
                    "halaman web. Keuntungannya, tim web bisa memakai keahlian dan kode",
                    "yang sudah ada. Kurikulum HTML, CSS, dan JavaScript di aplikasi ini",
                    "sudah cukup untuk mulai.",
                ],
            },
            {
                "heading": "Capacitor: membungkus aplikasi web",
                "bahasa": "terminal",
                "code": """npm create vite@latest kasir-web
cd kasir-web
npm install
npm install @capacitor/core
npm install -D @capacitor/cli
npx cap init "Kasir Web" id.contoh.kasirweb --web-dir=dist
npm install @capacitor/android
npx cap add android
npm run build
npx cap sync
npx cap open android""",
            },
            {
                "body": [
                    "Capacitor adalah runtime dari tim Ionic yang membungkus aplikasi",
                    "web jadi aplikasi Android dan iOS. Versi terbarunya 8.5.3 (7",
                    "Oktober 2026), lisensi MIT, sementara Capacitor 9 masih alfa. Di",
                    "Survei Stack Overflow 2024, Capacitor dipakai 1,8% responden, dan",
                    "di State of JS 2024 ada 855 responden yang memakainya di tempat",
                    "kerja.",
                    "",
                    "Urutan perintah di atas: buat aplikasi web dengan Vite, pasang",
                    "Capacitor, beri nama dan id aplikasi, lalu tambahkan platform",
                    "Android. Sesudah itu bangun versi web ke folder dist, salin",
                    "hasilnya ke proyek native dengan npx cap sync, dan buka di Android",
                    "Studio. Proyek iOS",
                    "ditambah dengan npx cap add ios, tapi dibuka dan dibangun di Xcode,",
                    "jadi butuh Mac.",
                    "",
                    "Ciri penting Capacitor: folder android/ dan ios/ adalah kode",
                    "sumber milikmu. Kamu boleh menyuntingnya di Android Studio atau",
                    "Xcode, dan folder itu ikut disimpan di git.",
                ],
            },
            {
                "heading": "Memanggil fitur native lewat plugin",
                "code": """import { Camera, CameraResultType } from '@capacitor/camera';

export async function ambilFotoStruk() {
  const foto = await Camera.getPhoto({
    quality: 80,
    resultType: CameraResultType.Uri,
  });
  return foto.webPath;
}""",
            },
            {
                "body": [
                    "Dari sisi kodemu, Camera.getPhoto cuma fungsi yang mengembalikan",
                    "Promise. Di baliknya ada perjalanan yang lebih panjang:",
                    "",
                    "  1. Capacitor mengubah panggilan itu jadi pesan berisi nama",
                    "     plugin, nama metode, argumen, dan nomor panggilan.",
                    "  2. Pesan dikirim dari WebView ke sisi native lewat mekanisme",
                    "     pesan yang disediakan WebView di tiap platform.",
                    "  3. Plugin native (Swift di iOS, Kotlin atau Java di Android)",
                    "     membuka kamera dan menunggu pengguna memotret.",
                    "  4. Hasilnya dikirim balik dengan nomor panggilan yang sama,",
                    "     lalu Promise yang cocok diselesaikan atau ditolak.",
                    "",
                    "Nomor panggilan itu yang membuat banyak panggilan bisa berjalan",
                    "bersamaan tanpa tertukar hasilnya. Latihan bab ini membangun",
                    "jembatan tiruan dengan cara yang sama.",
                    "",
                    "Jebakan: di iOS, akses kamera butuh kalimat alasan",
                    "NSCameraUsageDescription di Info.plist. Tanpa kalimat itu, aplikasi",
                    "langsung tertutup saat kamera dipanggil. Ikuti bagian izin di",
                    "dokumentasi setiap plugin, untuk Android maupun iOS.",
                ],
            },
            {
                "heading": "Ionic: komponen yang terasa seperti aplikasi",
                "bahasa": "jsx",
                "code": """import {
  IonButton, IonContent, IonHeader, IonItem, IonLabel,
  IonList, IonPage, IonTitle, IonToolbar,
} from '@ionic/react';

export default function Menu() {
  const menu = ['Kopi susu', 'Teh tarik', 'Roti bakar'];
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar><IonTitle>Menu</IonTitle></IonToolbar>
      </IonHeader>
      <IonContent>
        <IonList>
          {menu.map((m) => (
            <IonItem key={m}><IonLabel>{m}</IonLabel></IonItem>
          ))}
        </IonList>
        <IonButton expand="block">Pesan</IonButton>
      </IonContent>
    </IonPage>
  );
}""",
            },
            {
                "body": [
                    "Ionic Framework adalah kumpulan komponen UI web yang tampil seperti",
                    "aplikasi ponsel: bilah judul, daftar, tombol, tab, dan animasi",
                    "perpindahan layar. Gayanya menyesuaikan platform, mengikuti gaya",
                    "iOS di iPhone dan Material di Android. Ionic dipakai bersama",
                    "Angular, React, atau Vue. Versi terbarunya 9.0.8 (14 Oktober",
                    "2026), lisensi MIT. Di Survei Stack Overflow 2024 ia dipakai 2,5%",
                    "responden, dan di State of JS 2024 ada 1.118 responden yang",
                    "memakainya di tempat kerja.",
                    "",
                    "Ionic dan Capacitor sering disebut bersamaan, padahal tugasnya",
                    "beda. Ionic mengurus tampilan, Capacitor mengurus pembungkus dan",
                    "akses native. Capacitor bisa dipakai dengan kerangka web apa pun",
                    "tanpa Ionic, dan Ionic bisa dipakai sebagai PWA tanpa Capacitor.",
                ],
            },
            {
                "heading": "Cordova: pendahulu yang masih dirawat",
                "bahasa": "browser",
                "code": """document.addEventListener('deviceready', () => {
  navigator.camera.getPicture(
    (uri) => console.log('foto di', uri),
    (pesan) => console.log('gagal:', pesan),
    { quality: 80 },
  );
});""",
            },
            {
                "body": [
                    "Apache Cordova adalah pembungkus aplikasi web yang lebih tua, dulu",
                    "dikenal sebagai PhoneGap. Adobe menghentikan PhoneGap pada 2020,",
                    "tapi Cordova sendiri masih dirawat di bawah Apache dengan lisensi",
                    "Apache 2.0. Rilis terbarunya cordova-android 15.1.0, cordova-ios",
                    "8.1.1, dan CLI 13.0.0, dengan pembaruan platform Android terakhir",
                    "pada 22 Juli 2026.",
                    "",
                    "Statusnya menurun: proyek baru umumnya memilih Capacitor. Di Survei",
                    "Stack Overflow 2024 Cordova masih dipakai 2,2% responden, dan di",
                    "State of JS 2024 ada 759 responden yang memakainya di tempat kerja,",
                    "kebanyakan untuk merawat aplikasi lama. Ciri kode Cordova ada di",
                    "contoh atas: semua plugin baru boleh dipakai sesudah event",
                    "deviceready, dan hasilnya datang lewat callback. Folder platforms/",
                    "di proyek Cordova dihasilkan ulang dari config.xml, jadi suntingan",
                    "langsung di sana bisa hilang. Capacitor bisa menjalankan banyak",
                    "plugin Cordova, jadi pindah ke Capacitor biasanya bisa bertahap.",
                ],
            },
            {
                "heading": "Kapan hybrid cukup, kapan nggak",
                "body": [
                    "Hybrid cukup untuk aplikasi yang isinya kebanyakan formulir,",
                    "daftar, dan konten: aplikasi internal kantor, daftar produk, atau versi",
                    "toko dari aplikasi web yang sudah ada.",
                    "",
                    "Pertimbangkan pilihan lain kalau:",
                    "",
                    "  - Aplikasinya penuh animasi, gulir panjang yang berat, atau",
                    "    grafis. WebView biasanya kalah mulus dibanding view native.",
                    "  - Pengguna mengharapkan perilaku yang persis khas platform.",
                    "  - Aplikasinya cuma membungkus situs tanpa nilai tambah. Pedoman",
                    "    App Store bagian 4.2 (fungsi minimum) bisa membuat aplikasi",
                    "    seperti itu ditolak.",
                    "",
                    "Kalau aplikasimu nggak butuh toko dan fitur native, PWA dari bab 01",
                    "bisa jadi sudah cukup, tanpa pembungkus sama sekali.",
                    "",
                    "Jebakan: lupa menjalankan npx cap sync sesudah npm run build atau",
                    "sesudah memasang plugin baru. Aplikasi di ponsel tetap memakai",
                    "salinan web yang lama, dan perubahanmu seolah nggak berpengaruh.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi internal perusahaan dan aplikasi pendamping situs",
                    "web dibangun sebagai hybrid, karena timnya tim web dan kodenya",
                    "sudah ada.",
                    "",
                    "Kasus kecil: koperasi sekolah sudah punya web pencatatan iuran",
                    "berbasis React dan Vite. Bendahara minta versi aplikasi Android",
                    "yang bisa memotret struk pembelian.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tambahkan Capacitor ke proyek web yang ada dengan npm install",
                    "     @capacitor/core dan @capacitor/cli, lalu npx cap init.",
                    "  2. Pasang @capacitor/camera, lalu panggil Camera.getPhoto dari",
                    "     tombol Foto struk.",
                    "  3. Ikuti bagian izin di dokumentasi plugin kamera untuk",
                    "     AndroidManifest.xml.",
                    "  4. Jalankan npm run build, npx cap sync, lalu npx cap open",
                    "     android, dan coba di ponsel sungguhan. Di browser, plugin",
                    "     kamera berjalan dengan implementasi web yang terbatas.",
                    "  5. Bagikan ke bendahara lewat jalur uji internal Play Console",
                    "     (bab 11), sebelum rilis yang lebih luas.",
                ],
            },
        ],
    },
    {
        "title": "29. Peta Lintas Platform Lain",
        "sections": [
            {
                "body": [
                    "Selain Flutter, React Native, KMP, dan hybrid, masih ada beberapa",
                    "kerangka yang bakal kamu temui di lowongan atau di proyek warisan.",
                    "Materi ini peta untuk mengenalinya: bahasanya apa, statusnya",
                    "bagaimana, dan kapan masuk akal dipilih. Kamu nggak perlu",
                    "mempelajari semuanya.",
                    "",
                    "Dokumentasi Kotlin punya halaman perbandingan kerangka lintas",
                    "platform yang menyebut Flutter, React Native, KMP, Ionic, .NET",
                    "MAUI, Uno, dan NativeScript. Halaman itu nggak memberi angka",
                    "survei, jadi angka pemakaian di bawah diambil dari Survei Stack",
                    "Overflow 2024 dan State of JS 2024.",
                ],
            },
            {
                "heading": ".NET MAUI: tampilan dengan XAML",
                "bahasa": "xml",
                "code": """<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             x:Class="Kasir.HalamanUtama">
  <VerticalStackLayout Padding="24" Spacing="12">
    <Label Text="{Binding Teks}" FontSize="24" />
    <Button Text="Tambah" Command="{Binding TambahCommand}" />
  </VerticalStackLayout>
</ContentPage>""",
            },
            {
                "heading": "ViewModel-nya di C#",
                "bahasa": "csharp",
                "code": """using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

public partial class PenghitungViewModel : ObservableObject
{
    [ObservableProperty]
    private int jumlah;

    public string Teks => $"Diklik {Jumlah} kali";

    [RelayCommand]
    private void Tambah()
    {
        Jumlah++;
        OnPropertyChanged(nameof(Teks));
    }
}""",
            },
            {
                "body": [
                    ".NET MAUI adalah kerangka Microsoft untuk membuat aplikasi Android,",
                    "iOS, macOS, dan Windows dari satu proyek C#. Tampilannya biasanya",
                    "ditulis dalam bahasa markup XAML, lalu diikat ke ViewModel lewat",
                    "binding: {Binding Teks} membaca properti Teks, dan tombol menjalankan",
                    "TambahCommand. Pustaka CommunityToolkit.Mvvm membuatkan properti",
                    "Jumlah dan perintah TambahCommand dari atribut di atas. Pola ini",
                    "disebut MVVM.",
                    "",
                    "Versi terbarunya 10.0.110, bagian dari .NET 10 LTS, rilis 22",
                    "September 2026, dan .NET 11 sedang dalam tahap RC. Lisensinya MIT.",
                    "Di Survei Stack Overflow 2024, MAUI dipakai 3,1% responden. MAUI",
                    "cocok untuk tim yang sudah memakai C# dan .NET, misalnya untuk",
                    "aplikasi bisnis internal. Linux desktop bukan target MAUI, dan",
                    "versi iOS-nya tetap dibangun di Mac.",
                    "",
                    "Xamarin dan Xamarin.Forms adalah pendahulu MAUI. Dukungan untuk",
                    "semua SDK Xamarin berakhir 1 Mei 2024. Di Survei Stack Overflow",
                    "2024 Xamarin masih dipakai 2,9% responden, hampir pasti untuk",
                    "aplikasi lama. Statusnya usang: jangan dipilih untuk proyek baru,",
                    "dan aplikasi yang masih memakainya perlu dipindah ke MAUI.",
                ],
            },
            {
                "heading": "Uno Platform, NativeScript, Lynx, dan Quasar",
                "body": [
                    "Uno Platform memakai C# dan XAML bergaya WinUI, dan berjalan di",
                    "Windows, Android, iOS, macOS, Linux, serta WebAssembly. Gunanya",
                    "membawa aplikasi WinUI atau UWP ke platform lain. Versi terbarunya",
                    "6.7.135 (11 September 2026), lisensi Apache 2.0. Pesaingnya di",
                    "dunia .NET adalah Avalonia, yang dibahas di bab desktop.",
                    "",
                    "NativeScript menjalankan JavaScript atau TypeScript dan memanggil",
                    "API native Android dan iOS secara langsung, tanpa plugin pembungkus.",
                    "Ia bisa dipakai dengan Angular, Vue, Svelte, atau TypeScript murni.",
                    "Versi terbarunya @nativescript/core 9.1.3 (6 Oktober 2026), lisensi",
                    "MIT. Komunitasnya kecil: di State of JS 2024 ada 140 responden yang",
                    "memakainya di tempat kerja. Rilisnya tetap rutin.",
                    "",
                    "Lynx adalah kerangka open source dari ByteDance, perusahaan di",
                    "balik TikTok, yang dibuka pada 2025 dengan lisensi Apache 2.0. Ia",
                    "memakai CSS asli dan dua thread JavaScript terpisah: satu untuk",
                    "tampilan, satu untuk logika, supaya tampilan pertama cepat muncul.",
                    "Kodenya bisa ditulis dengan ReactLynx. Versi terbarunya 4.0.3 (11",
                    "September 2026). Lynx masih muda, jadi cocok untuk dicoba, belum",
                    "untuk dijadikan taruhan proyek kantor pertamamu.",
                    "",
                    "Quasar Framework berbasis Vue. Dari satu kode, Quasar bisa",
                    "menghasilkan situs web, PWA, aplikasi ponsel lewat Capacitor atau",
                    "Cordova, dan aplikasi desktop lewat Electron. Versi terbarunya",
                    "2.35.1 (12 Oktober 2026), lisensi MIT, dan di State of JS 2024 ada",
                    "268 responden yang memakainya di tempat kerja. Ia banyak dipakai",
                    "untuk dasbor dan aplikasi internal oleh tim yang sudah memakai Vue.",
                ],
            },
            {
                "heading": "Cara memilih dari peta ini",
                "body": [
                    "Pertanyaan pertama yang paling berguna biasanya: bahasa apa yang",
                    "sudah dikuasai tim?",
                    "",
                    "  - Tim C# dan .NET: .NET MAUI untuk mobile, atau Uno Platform",
                    "    kalau aplikasi WinUI yang sudah ada mau dibawa ke platform lain.",
                    "  - Tim Vue: Quasar, atau Ionic dengan Vue.",
                    "  - Tim TypeScript yang butuh akses langsung ke API native:",
                    "    NativeScript.",
                    "  - Proyek Xamarin warisan: rencanakan migrasi ke MAUI.",
                    "",
                    "Jebakan: memilih kerangka karena tampil keren di video, padahal",
                    "komunitasnya kecil. Sebelum memulai proyek, cek tanggal rilis",
                    "terakhir, jumlah pertanyaan yang dijawab di forumnya, dan apakah",
                    "pustaka yang kamu butuhkan (pembayaran, peta, notifikasi) tersedia.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perusahaan distribusi dan logistik banyak yang punya aplikasi",
                    "sales lapangan berbasis Xamarin.Forms dari masa sebelum 2024.",
                    "Aplikasi seperti itu sekarang harus dipindah, karena SDK Xamarin",
                    "nggak lagi diperbarui untuk aturan toko yang terus naik.",
                    "",
                    "Kasus kecil: aplikasi pencatat pesanan berbasis Xamarin.Forms",
                    "harus mengirim update ke Play Store. Sejak 31 Agustus 2026, update",
                    "wajib menargetkan API 36, dan SDK Xamarin terakhir nggak mendukung",
                    "target itu.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Catat semua layar, pustaka pihak ketiga, dan kode khusus",
                    "     platform (custom renderer) di proyek lama.",
                    "  2. Pakai .NET Upgrade Assistant untuk memindahkan proyek ke .NET",
                    "     MAUI dengan .NET 10. Alat itu menangani bagian yang mekanis,",
                    "     sisanya tetap dikerjakan tangan.",
                    "  3. Ganti custom renderer dengan handler, mekanisme pengganti di",
                    "     MAUI.",
                    "  4. Kalau waktunya mepet, ajukan perpanjangan tenggat target API",
                    "     lewat Play Console. Menurut aturan Play, perpanjangan bisa",
                    "     diminta sampai 1 November 2026.",
                    "  5. Uji di perangkat sungguhan yang dipakai tim sales, lalu rilis",
                    "     bertahap.",
                ],
            },
        ],
    },
    {
        "title": "30. Electron: Proses Main, Renderer, dan IPC",
        "sections": [
            {
                "body": [
                    "Kamu sudah bisa bikin halaman web pakai HTML, CSS, dan",
                    "JavaScript. Sekarang bayangkan halaman itu jadi aplikasi yang",
                    "dipasang di laptop. Punya ikon sendiri, jendela sendiri, dan",
                    "bisa menyimpan catatan ke folder Documents. Browser biasa",
                    "nggak mengizinkan itu. Halaman web sengaja dikurung supaya",
                    "situs nakal nggak bisa membaca berkas di laptopmu.",
                    "",
                    "Electron menyelesaikan masalah itu dengan cara yang lugas. Dia",
                    "membungkus Chromium (mesin browser milik Chrome) dan Node.js",
                    "(JavaScript yang boleh menyentuh berkas) jadi satu aplikasi.",
                    "Tampilannya tetap HTML dan CSS. Bedanya, ada bagian program",
                    "yang boleh mengakses sistem operasi.",
                    "",
                    "Banyak aplikasi yang mungkin sudah kamu pakai dibangun dengan",
                    "Electron, misalnya VS Code, Slack, Discord, dan Obsidian. Versi",
                    "stabil terbaru saat materi ini ditulis (Oktober 2026) adalah",
                    "Electron 44.9.0, rilis 17 Oktober 2026, yang membawa Chromium",
                    "152 dan Node.js 24.22.0. Versi mayor baru keluar kira-kira tiap",
                    "delapan minggu, dan tiga versi mayor terakhir didukung",
                    "bersamaan. Lisensinya MIT. Di Survei Stack Overflow 2024, 6,5%",
                    "responden menyebut memakai Electron.",
                ],
            },
            {
                "heading": "Dua jenis proses",
                "body": [
                    "Aplikasi Electron selalu terdiri dari minimal dua proses.",
                    "Proses itu program yang sedang jalan dan punya memori sendiri.",
                    "",
                    "  - Proses main. Cuma ada satu. Dia jalan di Node.js, jadi boleh",
                    "    membaca berkas, membuka jendela, membuat menu, dan memanggil",
                    "    fitur sistem operasi. Anggap saja dia pengelola aplikasinya.",
                    "  - Proses renderer. Ada satu untuk tiap jendela. Isinya halaman",
                    "    web biasa, lengkap dengan document dan window, mirip satu tab",
                    "    di Chrome. Demi keamanan, renderer nggak boleh menyentuh",
                    "    berkas langsung.",
                    "",
                    "Lalu bagaimana tombol di renderer bisa menyimpan berkas? Lewat",
                    "pesan. Renderer mengirim permintaan, main mengerjakannya, lalu",
                    "membalas. Cara dua proses saling berkirim pesan ini disebut",
                    "IPC, singkatan dari inter-process communication.",
                    "",
                    "Di antara keduanya ada skrip preload. Skrip ini jalan di",
                    "renderer sebelum halamannya dimuat, tapi boleh memakai sebagian",
                    "kecil API Electron. Tugasnya membuka loket: dia menentukan",
                    "fungsi apa saja yang boleh dipanggil halaman. Mirip loket bank.",
                    "Nasabah nggak masuk ke ruang brankas, dia cuma bisa minta",
                    "layanan yang tertulis di papan loket.",
                ],
            },
            {
                "heading": "main.js",
                "code": """const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('node:path');
const fs = require('node:fs/promises');

const FOLDER = path.join(app.getPath('documents'), 'catatanku');

function bikinJendela() {
  const jendela = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      // tiga nilai ini sudah bawaan, ditulis supaya kelihatan disengaja
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
    },
  });
  jendela.loadFile('index.html');
}

ipcMain.handle('catatan:baca', async (_event, nama) => {
  if (!/^[a-z0-9-]+$/.test(nama)) throw new Error('nama tidak sah');
  return fs.readFile(path.join(FOLDER, nama + '.txt'), 'utf8');
});

app.whenReady().then(bikinJendela);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});""",
            },
            {
                "heading": "preload.js",
                "code": """const { contextBridge, ipcRenderer } = require('electron');

// Halaman cuma melihat window.catatan.baca, bukan ipcRenderer utuh.
contextBridge.exposeInMainWorld('catatan', {
  baca: (nama) => ipcRenderer.invoke('catatan:baca', nama),
});""",
            },
            {
                "heading": "renderer.js (dimuat oleh index.html)",
                "bahasa": "browser",
                "code": """const tombol = document.querySelector('#buka');

tombol.addEventListener('click', async () => {
  try {
    const isi = await window.catatan.baca('belanja');
    document.querySelector('#isi').textContent = isi;
  } catch (e) {
    document.querySelector('#isi').textContent = 'Gagal: ' + e.message;
  }
});""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Urutannya begini waktu tombol diklik:",
                    "",
                    "  1. renderer.js memanggil window.catatan.baca('belanja').",
                    "     Fungsi itu ada karena preload menaruhnya lewat",
                    "     contextBridge.exposeInMainWorld.",
                    "  2. Preload meneruskannya ke ipcRenderer.invoke dengan nama",
                    "     kanal 'catatan:baca'. Hasilnya Promise, jadi renderer bisa",
                    "     menunggu pakai await.",
                    "  3. Di main, ipcMain.handle('catatan:baca', ...) menerima pesan",
                    "     itu, memeriksa namanya, lalu membaca berkas dengan fs.",
                    "  4. Nilai yang dikembalikan handler dikirim balik dan jadi hasil",
                    "     Promise. Kalau handler melempar error, Promise di renderer",
                    "     ditolak dan masuk ke blok catch.",
                    "",
                    "Nama kanal seperti 'catatan:baca' cuma teks bebas. Titik dua di",
                    "tengahnya kebiasaan supaya kanal gampang dikelompokkan.",
                    "",
                    "Selain pasangan invoke dan handle, ada pesan satu arah:",
                    "ipcRenderer.send ke main, dan webContents.send dari main ke",
                    "renderer. Untuk tanya-jawab seperti membaca berkas, invoke",
                    "paling enak dipakai karena hasilnya langsung balik sebagai",
                    "Promise.",
                ],
            },
            {
                "heading": "Jebakan keamanan",
                "body": [
                    "Electron membuka akses ke sistem, jadi kesalahan kecil bisa",
                    "jadi lubang besar. Tiga setelan di main.js tadi sudah jadi",
                    "nilai bawaan: contextIsolation sejak Electron 12, sandbox sejak",
                    "Electron 20, dan nodeIntegration mati sejak Electron 5. Tetap",
                    "tulis ketiganya supaya pembaca kodemu tahu itu disengaja.",
                    "",
                    "Jebakan: tutorial lama sering menulis nodeIntegration: true dan",
                    "contextIsolation: false supaya halaman bisa langsung memanggil",
                    "require('fs'). Akibatnya, skrip apa pun yang berhasil masuk ke",
                    "halaman, misalnya lewat teks pengguna yang nggak disaring, bisa",
                    "menjalankan perintah apa saja di laptop pemakainya.",
                    "",
                    "Aturan dari dokumentasi keamanan Electron yang paling sering",
                    "dilanggar pemula:",
                    "  - Jangan mengekspos ipcRenderer utuh lewat contextBridge. Buka",
                    "    fungsi kecil yang spesifik, satu per kebutuhan.",
                    "  - Anggap semua argumen dari renderer nggak bisa dipercaya.",
                    "    Contoh tadi menolak nama yang memuat garis miring atau titik,",
                    "    jadi '../../.bashrc' nggak bisa dipakai untuk membaca berkas",
                    "    di luar folder catatan.",
                    "  - Periksa pengirim pesan lewat event.senderFrame kalau",
                    "    aplikasimu memuat lebih dari satu sumber halaman.",
                    "  - Muat halaman dari berkas lokal. Kalau terpaksa membuka situs",
                    "    luar, jangan beri jendela itu preload yang kuat.",
                ],
            },
            {
                "heading": "Kapan memilih Electron",
                "body": [
                    "Kelebihan terbesarnya: satu kode untuk Windows, macOS, dan",
                    "Linux, dan tampilannya sama persis di ketiganya karena tiap",
                    "aplikasi membawa Chromium sendiri. Kamu juga bisa memakai paket",
                    "npm dan framework web yang sudah kamu kenal, seperti React atau",
                    "Vue.",
                    "",
                    "Harganya ada di ukuran. Karena Chromium dan Node ikut dibungkus,",
                    "pemasang aplikasi Electron paling sederhana pun biasanya",
                    "berukuran puluhan megabyte. Tiap aplikasi Electron yang terbuka",
                    "juga memakai RAM sendiri-sendiri. Kritik boros RAM yang sering",
                    "kamu dengar datang dari sini.",
                    "",
                    "Untuk membungkus aplikasi jadi pemasang (.exe, .dmg, .deb,",
                    ".rpm), dua alat yang paling umum adalah Electron Forge dan",
                    "electron-builder. Kalau ukuran jadi masalah utama, lihat materi",
                    "berikutnya: Tauri dan Wails memakai mesin browser yang sudah ada",
                    "di sistem operasi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "VS Code, Slack, Discord, dan Obsidian versi desktop dibangun",
                    "dengan Electron. Kamu bisa membuktikannya sendiri: di folder",
                    "pemasangan aplikasi seperti itu biasanya ada berkas app.asar di",
                    "dalam folder resources. Berkas itu arsip berisi kode",
                    "JavaScript, HTML, dan CSS aplikasinya.",
                    "",
                    "Kasus kecil: petugas perpustakaan sekolah minta aplikasi",
                    "desktop untuk mencatat buku yang dipinjam. Catatan disimpan",
                    "sebagai berkas teks di folder Documents. Petugas cuma mengetik",
                    "nama berkas dan isinya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Di main.js, tambahkan handler simpan yang memeriksa nama",
                    "     berkas dulu, baru menulis:",
                    "       ipcMain.handle('catatan:simpan', async (_e, nama, isi) => {",
                    "         if (!/^[a-z0-9-]+$/.test(nama)) throw new Error('nama?');",
                    "         await fs.mkdir(FOLDER, { recursive: true });",
                    "         await fs.writeFile(path.join(FOLDER, nama + '.txt'), isi);",
                    "         return 'tersimpan';",
                    "       });",
                    "  2. Di preload.js, tambahkan satu fungsi saja ke objek catatan:",
                    "       simpan: (nama, isi) =>",
                    "         ipcRenderer.invoke('catatan:simpan', nama, isi),",
                    "  3. Di renderer, panggil window.catatan.simpan('pinjam-01',",
                    "     teks) saat tombol Simpan diklik, lalu tampilkan hasilnya.",
                    "  4. Uji jebakannya: coba simpan dengan nama '../coba'. Promise",
                    "     harus ditolak dan nggak ada berkas yang tertulis di luar",
                    "     folder catatan.",
                ],
            },
        ],
    },
    {
        "title": "31. Tauri dan Wails: Desktop Ringan dengan Webview Bawaan",
        "sections": [
            {
                "body": [
                    "Di materi sebelumnya kamu sudah lihat harga Electron: tiap",
                    "aplikasi membawa Chromium sendiri. Padahal semua sistem operasi",
                    "modern sudah punya komponen untuk menampilkan halaman web,",
                    "namanya webview. Webview itu mesin browser tanpa bilah alamat",
                    "dan tombol, yang bisa ditempel di dalam aplikasi lain.",
                    "",
                    "  Windows   WebView2, berbasis Chromium milik Microsoft Edge",
                    "  macOS     WKWebView, berbasis WebKit milik Safari",
                    "  Linux     WebKitGTK, juga berbasis WebKit",
                    "",
                    "Tauri dan Wails memakai webview bawaan itu untuk tampilan, lalu",
                    "mengganti Node.js dengan bahasa lain untuk bagian yang",
                    "menyentuh sistem. Tauri memakai Rust, Wails memakai Go.",
                    "Hasilnya aplikasi yang jauh lebih kecil. Dokumentasi Tauri",
                    "menyebut aplikasi Tauri paling minimal bisa berukuran kurang",
                    "dari 600 KB.",
                ],
            },
            {
                "heading": "Tauri",
                "body": [
                    "Versi stabil terbaru saat materi ini ditulis (Oktober 2026)",
                    "adalah Tauri 2.12.4, rilis 14 Oktober 2026. Lini Tauri 2 stabil",
                    "sejak 2024, dan sejak itu Tauri juga bisa membuat aplikasi",
                    "Android dan iOS selain desktop. Tauri 3 masih alfa.",
                    "Lisensinya ganda, MIT atau Apache-2.0, boleh pilih salah satu.",
                    "",
                    "Di Survei Stack Overflow 2024, 2,4% responden memakai Tauri.",
                    "State of JS 2024 mencatat tingkat retensinya termasuk paling",
                    "tinggi di kategori mobile dan desktop. Retensi di sini artinya",
                    "orang yang sudah mencoba ingin memakainya lagi.",
                    "",
                    "Proyek Tauri punya dua folder utama. Folder src berisi tampilan",
                    "web (HTML, CSS, JavaScript, atau React, Vue, Svelte). Folder",
                    "src-tauri berisi kode Rust. Fungsi Rust yang boleh dipanggil",
                    "dari tampilan ditandai #[tauri::command], lalu didaftarkan ke",
                    "builder aplikasi.",
                ],
            },
            {
                "heading": "src-tauri/src/lib.rs",
                "bahasa": "rust",
                "code": """#[tauri::command]
fn sapa(nama: &str) -> String {
    format!("Halo, {}! Salam dari Rust.", nama)
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![sapa])
        .run(tauri::generate_context!())
        .expect("gagal menjalankan aplikasi Tauri");
}""",
            },
            {
                "heading": "Memanggilnya dari tampilan",
                "code": """import { invoke } from '@tauri-apps/api/core';

const balasan = await invoke('sapa', { nama: 'Rina' });
document.querySelector('#salam').textContent = balasan;""",
            },
            {
                "heading": "Izin lewat capabilities",
                "body": [
                    "invoke('sapa', { nama: 'Rina' }) mengirim nama perintah dan",
                    "argumennya ke Rust. Nama kunci di objek argumen harus sama",
                    "dengan nama parameter fungsi Rust-nya. Hasil fungsi Rust balik",
                    "sebagai Promise, sama seperti invoke di Electron.",
                    "",
                    "Bedanya ada di izin. Tauri 2 memakai sistem capabilities:",
                    "fitur dari plugin, misalnya membaca berkas atau membuka dialog",
                    "simpan, baru bisa dipanggil tampilan kalau izinnya ditulis di",
                    "berkas capabilities. Yang nggak ditulis berarti ditolak. Jadi",
                    "kamu mulai dari keadaan tertutup dan membuka satu per satu,",
                    "kebalikan dari tutorial Electron lama yang membuka semuanya",
                    "dulu.",
                ],
            },
            {
                "heading": "src-tauri/capabilities/default.json",
                "bahasa": "json",
                "code": """{
  "identifier": "default",
  "description": "izin untuk jendela utama",
  "windows": ["main"],
  "permissions": [
    "core:default",
    "fs:allow-read-text-file"
  ]
}""",
            },
            {
                "heading": "Wails",
                "body": [
                    "Wails membawa ide yang sama untuk pemrogram Go. Versi",
                    "stabilnya 2.17.0, rilis 18 Oktober 2026, sedangkan Wails 3",
                    "masih beta (3.0.0-beta.32). Lisensinya MIT. Method milik struct",
                    "Go yang kamu daftarkan ke aplikasi otomatis dibuatkan fungsi",
                    "JavaScript oleh Wails, lengkap dengan Promise-nya. Fungsi-fungsi",
                    "itu ditaruh di folder frontend/wailsjs.",
                ],
            },
            {
                "heading": "app.go",
                "bahasa": "go",
                "code": """package main

import "fmt"

type App struct{}

func (a *App) Sapa(nama string) string {
	return fmt.Sprintf("Halo, %s! Salam dari Go.", nama)
}""",
            },
            {
                "heading": "frontend/src/main.js",
                "bahasa": "browser",
                "code": """import { Sapa } from '../wailsjs/go/main/App';

const balasan = await Sapa('Rina');
document.querySelector('#salam').textContent = balasan;""",
            },
            {
                "heading": "Memilih di antara ketiganya",
                "body": [
                    "Electron cocok kalau timmu cuma bisa JavaScript, tampilannya",
                    "harus sama persis di semua sistem operasi, atau kamu butuh",
                    "paket npm yang khusus Node. Tauri cocok kalau ukuran dan",
                    "pemakaian memori penting, kamu mau belajar Rust, atau",
                    "aplikasinya nanti juga perlu versi Android dan iOS. Wails cocok",
                    "kalau backend-mu memang sudah Go.",
                    "",
                    "Jebakan: karena memakai webview bawaan, tampilan aplikasi Tauri",
                    "dan Wails bisa sedikit beda di tiap sistem operasi. CSS atau",
                    "API web terbaru yang jalan di WebView2 belum tentu sudah ada di",
                    "WebKitGTK. Uji di ketiga sistem sebelum rilis, jangan cuma di",
                    "laptopmu sendiri.",
                    "",
                    "Membangun aplikasi Tauri di Fedora butuh pustaka pengembangan",
                    "WebKitGTK dan perkakas C. Perintah dari dokumentasi resmi Tauri",
                    "ada di bawah. Bacalah dulu sebelum mengetiknya, karena perintah",
                    "itu memasang paket ke sistemmu.",
                ],
            },
            {
                "heading": "Pustaka yang dibutuhkan Tauri di Fedora",
                "bahasa": "terminal",
                "code": "sudo dnf check-update\nsudo dnf install webkit2gtk4.1-devel openssl-devel curl wget file libappindicator-gtk3-devel librsvg2-devel libxdo-devel\nsudo dnf group install \"c-development\"",
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Daftar aplikasi buatan komunitas Tauri bisa kamu lihat di",
                    "repositori awesome-tauri di GitHub: pengelola clipboard, klien",
                    "API, pemutar musik, sampai aplikasi catatan. Aplikasi Wails",
                    "memakai pola yang sama: satu biner Go yang membuka jendela",
                    "berisi tampilan web.",
                    "",
                    "Kasus kecil: koperasi sekolah butuh aplikasi kasir yang jalan",
                    "di laptop lama ber-RAM 4 GB. Meja kasir memakai Windows,",
                    "laptop bendahara memakai Fedora. Satu tombol harus menghitung",
                    "total belanja.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat proyek dengan npm create tauri-app@latest, lalu pilih",
                    "     JavaScript polos supaya tampilannya ringan.",
                    "  2. Tulis perintah Rust yang menjumlahkan daftar harga:",
                    "       #[tauri::command]",
                    "       fn total(harga: Vec<u32>) -> u32 {",
                    "           harga.iter().sum()",
                    "       }",
                    "     lalu daftarkan di generate_handler![total].",
                    "  3. Panggil dari tampilan:",
                    "       await invoke('total', { harga: [5000, 12000] })",
                    "  4. Jangan tambahkan izin plugin yang nggak dipakai. Kasir ini",
                    "     nggak butuh akses berkas, jadi capabilities cukup",
                    "     core:default.",
                    "  5. Bangun pemasang di sistem operasinya masing-masing atau",
                    "     lewat CI. Di Fedora, npm run tauri build menghasilkan paket",
                    "     .rpm, .deb, dan AppImage. Membangun pemasang Windows dari",
                    "     Linux masih berstatus eksperimental di dokumentasi Tauri.",
                ],
            },
        ],
    },
    {
        "title": "32. GUI Immediate Mode dengan Dear ImGui",
        "sections": [
            {
                "body": [
                    "Toolkit yang sudah kamu kenal sejauh ini, dari DOM di browser,",
                    "widget Qt, sampai View di Android, bekerja dengan cara yang",
                    "sama. Kamu membuat objek tombol sekali, toolkit menyimpannya di",
                    "sebuah pohon, lalu kamu mengubah sifatnya kalau perlu. Saat",
                    "tombol diklik, toolkit memanggil fungsi yang sudah kamu",
                    "daftarkan. Model ini disebut retained mode, karena toolkit",
                    "menahan (retain) objek-objek tampilan untukmu.",
                    "",
                    "Ada model kedua yang terasa aneh di awal: immediate mode. Di",
                    "sini nggak ada objek tombol yang kamu simpan. Tiap frame, yaitu",
                    "tiap kali layar digambar ulang (biasanya 60 kali per detik),",
                    "kodemu memanggil fungsi yang menggambar tombol. Fungsi itu",
                    "langsung mengembalikan true kalau tombolnya diklik pada frame",
                    "itu.",
                    "",
                    "Pustaka immediate mode paling terkenal adalah Dear ImGui,",
                    "ditulis dalam C++ dengan lisensi MIT. Versi terbarunya saat",
                    "materi ini ditulis (Oktober 2026) adalah 1.93.0, rilis",
                    "14 Oktober 2026. Dear ImGui banyak dipakai untuk panel debug di",
                    "engine game, alat internal studio, dan emulator.",
                ],
            },
            {
                "heading": "Satu jendela penghitung",
                "bahasa": "cpp",
                "code": """// dijalankan sekali tiap frame, di dalam game loop
static int hitung = 0;

ImGui::Begin("Penghitung");
ImGui::Text("Nilai: %d", hitung);
if (ImGui::Button("Tambah")) {
    hitung++;
}
if (hitung > 0 && ImGui::Button("Reset")) {
    hitung = 0;
}
ImGui::End();""",
            },
            {
                "heading": "Cara kerjanya",
                "body": [
                    "Kode itu dijalankan ulang dari atas setiap frame. Panggilan",
                    "ImGui::Button(\"Tambah\") menggambar tombol sekaligus bertanya",
                    "ke ImGui: apakah mouse diklik di atas kotak tombol ini pada",
                    "frame ini? Kalau iya, hasilnya true dan hitung bertambah.",
                    "",
                    "Perhatikan tiga hal:",
                    "  - State aplikasi tinggal di variabelmu sendiri, di sini",
                    "    hitung. Tombol nggak punya salinan nilainya, jadi nggak ada",
                    "    data ganda yang harus disamakan.",
                    "  - Tombol Reset cuma ada di frame ketika hitung lebih dari nol.",
                    "    Mau menyembunyikan tombol? Jangan panggil fungsinya. Nggak",
                    "    perlu setVisible(false) seperti di retained mode.",
                    "  - Teks Nilai digambar sebelum tombol diproses. Di frame tempat",
                    "    tombol diklik, teks masih menampilkan angka lama, dan baru",
                    "    benar di frame berikutnya. Di 60 frame per detik, beda satu",
                    "    frame itu nggak kelihatan.",
                    "",
                    "Di balik layar, ImGui tetap menyimpan sedikit data, misalnya",
                    "posisi jendela dan tombol mana yang sedang ditekan. Data itu",
                    "dikenali lewat ID yang dibentuk dari label. Dari sisi",
                    "pemrogram, kamu tetap merasa nggak menyimpan apa pun.",
                ],
            },
            {
                "heading": "Simulasi lima frame di Node",
                "code": """// Simulasi GUI immediate mode di Node: tiap frame, UI dideklarasikan ulang.
let hitung = 0;

function tombol(label, klik) {
  const kena = klik === label;
  console.log(`  tombol [${label}]` + (kena ? ' diklik' : ''));
  return kena;
}

function frame(nomor, klik) {
  console.log(`frame ${nomor}`);
  console.log(`  teks Nilai: ${hitung}`);
  if (tombol('Tambah', klik)) hitung++;
  if (hitung > 0 && tombol('Reset', klik)) hitung = 0;
}

frame(1, null);
frame(2, 'Tambah');
frame(3, null);
frame(4, 'Reset');
frame(5, null);""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  frame 1",
                    "    teks Nilai: 0",
                    "    tombol [Tambah]",
                    "  frame 2",
                    "    teks Nilai: 0",
                    "    tombol [Tambah] diklik",
                    "    tombol [Reset]",
                    "  frame 3",
                    "    teks Nilai: 1",
                    "    tombol [Tambah]",
                    "    tombol [Reset]",
                    "  frame 4",
                    "    teks Nilai: 1",
                    "    tombol [Tambah]",
                    "    tombol [Reset] diklik",
                    "  frame 5",
                    "    teks Nilai: 0",
                    "    tombol [Tambah]",
                    "",
                    "Lihat frame 2: tombol Reset sudah muncul di frame yang sama",
                    "dengan klik Tambah, karena saat baris Reset dijalankan, hitung",
                    "sudah 1. Teks Nilai baru ikut berubah di frame 3. Di frame 5,",
                    "Reset hilang lagi karena kodenya nggak memanggil tombol itu.",
                ],
            },
            {
                "heading": "Siapa yang menggambar",
                "body": [
                    "Dear ImGui sendiri nggak tahu cara membuka jendela atau bicara",
                    "dengan kartu grafis. Dia cuma menghasilkan daftar segitiga dan",
                    "teks yang perlu digambar. Sisanya dikerjakan dua jenis",
                    "backend:",
                    "  - backend platform, yang membuka jendela dan membaca mouse",
                    "    serta keyboard, misalnya SDL, GLFW, atau Win32;",
                    "  - backend renderer, yang mengirim segitiga ke GPU, misalnya",
                    "    OpenGL, Vulkan, DirectX, atau Metal.",
                    "",
                    "Repositori Dear ImGui sudah menyediakan contoh pasangan backend",
                    "yang siap dipakai, jadi kamu jarang perlu menulisnya sendiri.",
                ],
            },
            {
                "heading": "Kapan memilih immediate mode",
                "body": [
                    "Immediate mode cocok untuk program yang memang menggambar ulang",
                    "layar terus-menerus, seperti game, emulator, dan visualisasi",
                    "data langsung. Menambah panel pengaturan cuma butuh beberapa",
                    "baris, dan kamu nggak perlu mengurus penyamaan data dengan",
                    "tampilan.",
                    "",
                    "Untuk aplikasi biasa yang dipakai banyak orang, retained mode",
                    "masih pilihan yang lebih aman. Dear ImGui menggambar piksel",
                    "sendiri, jadi tampilannya nggak mengikuti gaya sistem operasi.",
                    "Dukungan pembaca layar dan metode input untuk aksara seperti",
                    "Jepang atau Mandarin juga masih terbatas. Karena menggambar",
                    "ulang terus, ia boros baterai kalau nggak diatur untuk",
                    "berhenti saat nggak ada input.",
                    "",
                    "Pustaka immediate mode lain yang mungkin kamu temui: egui untuk",
                    "Rust, Nuklear untuk C, dan raygui untuk pengguna raylib.",
                    "",
                    "Jebakan: dua tombol berlabel sama di jendela yang sama, misalnya",
                    "dua tombol \"Hapus\" di satu daftar, punya ID yang sama. ImGui",
                    "bisa salah mengenali tombol mana yang diklik. Bedakan dengan",
                    "akhiran ##, misalnya \"Hapus##1\" dan \"Hapus##2\" (bagian",
                    "setelah ## nggak ditampilkan), atau bungkus tiap baris daftar",
                    "dengan ImGui::PushID dan ImGui::PopID.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Wiki Dear ImGui punya halaman Software using Dear ImGui yang",
                    "memuat banyak contoh: panel debug engine game, editor level",
                    "buatan studio, emulator konsol lama, sampai alat pemantau",
                    "perangkat keras. Polanya sama: program utamanya sudah",
                    "menggambar tiap frame, jadi panel ImGui tinggal ditumpangkan di",
                    "atasnya.",
                    "",
                    "Kasus kecil: kamu bikin game balap kecil dengan C++ dan ingin",
                    "mencoba-coba kecepatan mobil musuh tanpa mengompilasi ulang",
                    "tiap kali angkanya diubah.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Simpan kecepatan di variabel biasa yang dibaca logika game,",
                    "     misalnya float kecepatanMusuh = 4.0f;",
                    "  2. Di dalam game loop, sesudah ImGui::NewFrame(), buat jendela",
                    "     kecil:",
                    "       ImGui::Begin(\"Debug\");",
                    "       ImGui::SliderFloat(\"kecepatan\", &kecepatanMusuh, 0, 10);",
                    "       ImGui::End();",
                    "  3. Geser slider saat game jalan. Karena slider menulis langsung",
                    "     ke variabel yang sama, mobil musuh langsung berubah",
                    "     kecepatan di frame berikutnya.",
                    "  4. Bungkus kode panel itu dengan #ifndef NDEBUG supaya nggak",
                    "     ikut terbawa di versi rilis.",
                ],
            },
        ],
    },
    {
        "title": "33. Peta Toolkit Desktop Native",
        "sections": [
            {
                "body": [
                    "Sebelum Electron dan kawan-kawannya ada, aplikasi desktop",
                    "dibuat dengan toolkit native. Toolkit itu pustaka berisi",
                    "tombol, kotak teks, menu, dan jendela yang dirancang untuk",
                    "sistem operasi tertentu. Banyak di antaranya masih aktif, dan",
                    "lowongan kerja untuk C#, Java, dan C++ sering menyebut",
                    "namanya.",
                    "",
                    "Kamu nggak perlu mempelajari semuanya. Cukup kenali nama,",
                    "bahasa, dan statusnya, supaya waktu ketemu di kode atau iklan",
                    "lowongan, kamu tahu itu barang apa. Semua versi di materi ini",
                    "dicek Oktober 2026.",
                ],
            },
            {
                "heading": "Qt",
                "body": [
                    "Qt (dibaca \"kyut\") adalah framework C++ lintas platform untuk",
                    "desktop, perangkat tertanam, dan mobile. Versi terbarunya Qt",
                    "6.12 LTS, rilis 30 September 2026. Desktop KDE Plasma dibangun",
                    "dengan Qt, begitu juga banyak aplikasi industri, layar mesin,",
                    "dan sistem hiburan mobil. Di Survei Stack Overflow 2024, 7,3%",
                    "responden memakai Qt.",
                    "",
                    "Ada dua cara membuat tampilan Qt. Qt Widgets memakai C++ dengan",
                    "widget klasik. QML memakai bahasa deklaratif yang mirip JSON",
                    "plus JavaScript, cocok untuk layar sentuh yang banyak animasi.",
                    "Kalau kamu lebih nyaman dengan Python, PySide6 adalah binding",
                    "Python resmi dari Qt. Editor resminya Qt Creator.",
                ],
            },
            {
                "heading": "Tombol pertama dengan Qt Widgets",
                "bahasa": "cpp",
                "code": """#include <QApplication>
#include <QPushButton>

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);
    QPushButton tombol("Tutup aku");
    QObject::connect(&tombol, &QPushButton::clicked,
                     &app, &QApplication::quit);
    tombol.show();
    return app.exec();
}""",
            },
            {
                "body": [
                    "QObject::connect menyambungkan sinyal clicked milik tombol ke",
                    "slot quit milik aplikasi. Sinyal dan slot adalah cara Qt",
                    "menangani event: sinyal dipancarkan saat sesuatu terjadi, dan",
                    "slot adalah fungsi yang dipanggil karenanya. app.exec()",
                    "menjalankan event loop sampai aplikasi ditutup.",
                    "",
                    "Jebakan: Qt versi open source berlisensi LGPL-3.0 atau GPL.",
                    "LGPL mewajibkan pemakai aplikasimu bisa mengganti pustaka Qt di",
                    "dalamnya, biasanya dengan menautkan Qt secara dinamis. Baca",
                    "syaratnya sebelum menjual aplikasi berkode tertutup, atau pakai",
                    "lisensi komersial Qt.",
                ],
            },
            {
                "heading": "GTK",
                "body": [
                    "GTK adalah toolkit milik proyek GNOME, desktop bawaan Fedora",
                    "Workstation. Aplikasi seperti Files dan Text Editor di laptopmu",
                    "memakai GTK 4, dan GIMP juga dibangun di atas GTK. Versi",
                    "terbarunya 4.24.1, rilis 1 Oktober 2026, dengan lisensi",
                    "LGPL-2.1 atau lebih baru. Di Survei Stack Overflow 2024, 2,6%",
                    "responden memakai GTK.",
                    "",
                    "Bahasa utamanya C, tapi banyak aplikasi GNOME baru ditulis",
                    "dengan Python (PyGObject), Rust (gtk-rs), atau Vala. Untuk",
                    "tampilan bergaya GNOME modern, GTK dipasangkan dengan",
                    "libadwaita, dan aplikasinya biasanya dibagikan sebagai Flatpak",
                    "lewat Flathub.",
                ],
            },
            {
                "heading": "Dunia Windows: WinForms, WPF, dan WinUI 3",
                "body": [
                    "Ketiganya cuma jalan di Windows, dan ketiganya masih dipakai.",
                    "",
                    "  - WinForms adalah yang tertua. Form dan tombol diseret di",
                    "    desainer Visual Studio, lalu logikanya ditulis di event",
                    "    handler seperti tombol1_Click. Cepat jadi, makanya banyak",
                    "    dipakai untuk aplikasi bisnis lama dan tugas sekolah atau",
                    "    PKL. Bisa ditulis dengan C# atau Visual Basic.",
                    "  - WPF menyusun tampilan dengan XAML, bahasa markup berbasis",
                    "    XML, dan punya data binding yang kuat untuk menyambungkan",
                    "    tampilan ke data. Pola yang biasa dipakai bersamanya disebut",
                    "    MVVM (Model, View, ViewModel), mirip ViewModel di Android.",
                    "  - WinUI 3 adalah toolkit terbaru dengan gaya Fluent milik",
                    "    Windows 11. Ia dikirim lewat Windows App SDK, yang versi",
                    "    terbarunya 2.5.1 (16 September 2026), dan jadi penerus UWP.",
                    "",
                    "WinForms dan WPF ikut di .NET 10 LTS, dengan patch terbaru",
                    "10.0.13 (13 Oktober 2026). Contoh di bawah adalah jendela WPF",
                    "yang menampilkan total belanja dan tombol yang tersambung ke",
                    "ViewModel lewat binding.",
                ],
            },
            {
                "heading": "MainWindow.xaml",
                "bahasa": "xml",
                "code": """<Window x:Class="Kasir.MainWindow"
        xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
        Title="Kasir" Width="320" Height="160">
  <StackPanel Margin="12">
    <TextBlock Text="{Binding Total}" FontSize="24"/>
    <Button Content="Tambah barang" Command="{Binding TambahCommand}"/>
  </StackPanel>
</Window>""",
            },
            {
                "heading": "Lintas platform dari C# dan Java",
                "body": [
                    "Avalonia UI membawa gaya WPF ke Windows, macOS, Linux, mobile,",
                    "dan WebAssembly. Versi terbarunya 12.1.4 (9 Oktober 2026),",
                    "berlisensi MIT. Kalau kamu menguasai C# dan aplikasinya harus",
                    "jalan di Fedora juga, Avalonia saat ini pilihan bergaya WPF",
                    "yang paling matang di Linux.",
                    "",
                    "JavaFX adalah toolkit modern untuk Java dengan scene graph,",
                    "properti yang bisa di-bind, dan gaya CSS. Versi terbarunya",
                    "JavaFX 27, dan versi LTS terakhirnya 25. Sejak JDK 11, JavaFX",
                    "nggak ikut di dalam JDK, jadi harus ditambahkan lewat Maven atau",
                    "Gradle. Scene Builder membantu menyusun tampilannya secara",
                    "visual.",
                    "",
                    "Swing masih ikut di dalam JDK sampai sekarang (JDK 27), tapi",
                    "praktis sudah dalam mode pemeliharaan. Kamu masih akan",
                    "menemuinya di aplikasi Java lama dan tugas kuliah. Kalau",
                    "terpaksa memakai Swing, pustaka FlatLaf bisa membuat",
                    "tampilannya lebih modern. Untuk proyek Java baru, pilih JavaFX.",
                ],
            },
            {
                "heading": "Sisanya, dengan status jujur",
                "body": [
                    "  - wxWidgets 3.2.12 (C++, juga Python lewat wxPython) memakai",
                    "    kontrol asli tiap sistem operasi. Audacity, FileZilla, dan",
                    "    Code::Blocks dibangun dengannya. Statusnya stabil dan",
                    "    matang, komunitasnya kecil.",
                    "  - NW.js 0.118 lebih tua dari Electron dan sama-sama",
                    "    menggabungkan Chromium dan Node.js. Masih rutin diperbarui,",
                    "    tapi pemakaiannya jauh di bawah Electron. Kamu mungkin",
                    "    menemuinya di game HTML5 yang diekspor dari RPG Maker MV.",
                    "    Jangan dipilih untuk proyek baru.",
                    "  - MFC adalah pustaka C++ lama Microsoft yang membungkus Win32",
                    "    API. Statusnya usang dan cuma dirawat untuk kode warisan,",
                    "    misalnya aplikasi desain teknik atau perangkat lunak mesin.",
                    "    Jangan dipilih untuk proyek baru.",
                    "  - AppKit adalah toolkit klasik aplikasi Mac. Ia dibahas di",
                    "    materi Peta Framework Apple, dan seperti iOS, butuh Mac",
                    "    untuk dibangun.",
                ],
            },
            {
                "heading": "Cara memilih",
                "body": [
                    "Tiga pertanyaan biasanya sudah cukup:",
                    "  1. Aplikasinya harus jalan di sistem operasi apa? Kalau cuma",
                    "     Windows, WinForms, WPF, atau WinUI 3 masuk akal. Kalau harus",
                    "     jalan juga di Linux, coret ketiganya.",
                    "  2. Bahasa apa yang kamu atau timmu kuasai? C++ ke Qt atau",
                    "     wxWidgets, C# ke Avalonia, Java ke JavaFX, C atau Python",
                    "     atau Rust ke GTK, JavaScript ke Electron atau Tauri.",
                    "  3. Apakah tampilannya harus terasa asli di tiap sistem? Yang",
                    "     paling dekat ke kontrol asli adalah wxWidgets. Qt dan GTK",
                    "     menggambar widget sendiri, walau Qt bisa meniru gaya",
                    "     sistemnya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kalau kamu PKL di kantor yang sudah lama memakai komputer,",
                    "besar kemungkinan ada aplikasi WinForms atau WPF buatan sendiri",
                    "untuk kasir, gudang, atau absensi. Di Fedora, aplikasi GNOME",
                    "bawaan seperti Files dan Text Editor adalah contoh GTK 4 yang",
                    "bisa kamu buka sekarang juga.",
                    "",
                    "Kasus kecil: koperasi karyawan punya aplikasi WinForms lama",
                    "untuk mencatat simpanan anggota. Sekarang setengah komputernya",
                    "pindah ke Linux, dan pengurus minta aplikasinya jalan di",
                    "keduanya tanpa ditulis ulang dari nol.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan dulu logika simpanan (hitung saldo, validasi) dari",
                    "     kode form. Logika yang nggak menyentuh tombol bisa dipakai",
                    "     ulang apa adanya.",
                    "  2. Pilih toolkit lintas platform yang sebahasa, yaitu Avalonia,",
                    "     karena kodenya tetap C# dan polanya mirip WPF.",
                    "  3. Susun ulang tampilannya dengan XAML versi Avalonia, lalu",
                    "     sambungkan ke logika lama lewat ViewModel.",
                    "  4. Uji di Windows dan Fedora, lalu bagikan versi Linux sebagai",
                    "     paket .rpm atau Flatpak.",
                ],
            },
        ],
    },
    {
        "title": "34. Menguji Aplikasi Mobile: Unit, UI, dan Instrumentasi",
        "sections": [
            {
                "body": [
                    "Sebelum rilis, kamu bisa saja membuka emulator lalu menekan",
                    "tombol satu per satu untuk memastikan semuanya jalan. Masalahnya,",
                    "aplikasi terus bertambah fitur. Tiap rilis butuh waktu lebih",
                    "lama, dan cepat atau lambat ada layar yang lupa dicoba. Bug yang",
                    "dulu sudah dibetulkan bisa muncul lagi tanpa ada yang sadar.",
                    "",
                    "Uji otomatis adalah kode yang memeriksa kode lain. Kamu",
                    "menulisnya sekali, lalu komputer menjalankannya setiap kali ada",
                    "perubahan. Di aplikasi mobile ada tiga jenis yang perlu kamu",
                    "bedakan:",
                    "  - Uji unit lokal. Menguji satu fungsi atau kelas, misalnya",
                    "    ViewModel, langsung di komputermu tanpa emulator. Di proyek",
                    "    Android, letaknya di folder src/test. Jalannya dalam hitungan",
                    "    detik.",
                    "  - Uji instrumentasi. Jalan di perangkat atau emulator",
                    "    sungguhan, jadi bisa memakai fitur Android seperti database",
                    "    Room atau Context. Letaknya di src/androidTest. Lebih lambat,",
                    "    karena aplikasi harus dipasang dulu.",
                    "  - Uji UI. Jenis uji instrumentasi yang menekan tombol dan",
                    "    memeriksa apa yang tampil di layar, seperti pengguna",
                    "    sungguhan.",
                    "",
                    "Aturan praktisnya dikenal sebagai piramida uji: banyak uji unit",
                    "di dasar, lebih sedikit uji instrumentasi di tengah, dan",
                    "sedikit uji UI di puncak. Makin ke atas, uji makin lambat dan",
                    "makin gampang gagal karena hal yang nggak berhubungan dengan",
                    "kodemu.",
                ],
            },
            {
                "heading": "Uji unit lokal dengan JUnit",
                "bahasa": "kotlin",
                "code": """import org.junit.Assert.assertEquals
import org.junit.Test

class PenghitungViewModelTest {
    @Test
    fun tambah_menaikkanNilaiSatu() {
        val vm = PenghitungViewModel()
        vm.tambah()
        assertEquals(1, vm.nilai.value)
    }
}""",
            },
            {
                "body": [
                    "Anotasi @Test menandai fungsi sebagai satu kasus uji.",
                    "assertEquals(1, vm.nilai.value) gagal kalau nilainya bukan 1,",
                    "dan Gradle melaporkan uji mana yang merah. Dokumentasi Android",
                    "untuk uji lokal masih memakai JUnit 4, jadi itu yang paling",
                    "sering kamu temui di proyek Android.",
                    "",
                    "Uji ini bisa jalan tanpa emulator karena PenghitungViewModel",
                    "nggak menyentuh layar sama sekali. Di sini pemisahan logika ke",
                    "ViewModel dari bab Arsitektur Aplikasi Android terbayar: logika",
                    "yang terpisah dari layar bisa diuji dalam hitungan detik.",
                    "Untuk ketergantungan yang sulit dibuat, misalnya repository yang",
                    "memanggil jaringan, pakai objek palsu (fake) atau pustaka",
                    "seperti Mockito dan MockK. Robolectric bisa menjalankan sebagian",
                    "kode Android di JVM komputermu tanpa emulator.",
                ],
            },
            {
                "heading": "Uji UI Compose dan Espresso",
                "bahasa": "kotlin",
                "code": """class LayarPenghitungTest {
    @get:Rule
    val aturan = createComposeRule()

    @Test
    fun klikTambah_angkaJadiSatu() {
        aturan.setContent { LayarPenghitung() }
        aturan.onNodeWithText("Tambah").performClick()
        aturan.onNodeWithText("Nilai: 1").assertIsDisplayed()
    }
}

// Versi Espresso untuk layar lama berbasis View dan layout XML:
// onView(withId(R.id.tombolTambah)).perform(click())
// onView(withId(R.id.teksNilai)).check(matches(withText("Nilai: 1")))""",
            },
            {
                "body": [
                    "Compose UI Test mencari elemen di layar lewat teks atau tag,",
                    "melakukan aksi seperti performClick, lalu memeriksa hasilnya.",
                    "Espresso melakukan hal yang sama untuk layar berbasis View.",
                    "Keduanya menunggu otomatis sampai aplikasi diam (nggak ada",
                    "pekerjaan di thread UI) sebelum memeriksa, jadi kamu nggak perlu",
                    "menulis jeda manual.",
                    "",
                    "Dari terminal, ./gradlew test menjalankan uji unit lokal tanpa",
                    "emulator. ./gradlew connectedAndroidTest menjalankan uji",
                    "instrumentasi, jadi emulator harus menyala atau HP harus",
                    "tersambung lewat USB dulu.",
                ],
            },
            {
                "heading": "Menjalankan uji di proyek Android",
                "bahasa": "terminal",
                "code": """./gradlew test
./gradlew connectedAndroidTest""",
            },
            {
                "heading": "Ide yang sama di Node",
                "code": """const assert = require('node:assert');

// Logika keranjang dipisah dari layar, jadi bisa diuji tanpa emulator.
function totalBelanja(barang, kodeDiskon) {
  const subtotal = barang.reduce((jumlah, b) => jumlah + b.harga * b.qty, 0);
  const potongan = kodeDiskon === 'HEMAT10' ? Math.floor(subtotal / 10) : 0;
  return subtotal - potongan;
}

const keranjang = [
  { harga: 12000, qty: 2 },
  { harga: 5500, qty: 1 },
];

assert.strictEqual(totalBelanja(keranjang, null), 29500);
assert.strictEqual(totalBelanja(keranjang, 'HEMAT10'), 26550);
assert.strictEqual(totalBelanja([], 'HEMAT10'), 0);
console.log('3 uji lulus');""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  3 uji lulus",
                    "",
                    "Kalau salah satu assert gagal, program berhenti dengan pesan",
                    "AssertionError yang menyebut nilai yang diharapkan dan nilai",
                    "yang keluar. Prinsipnya sama persis dengan JUnit: siapkan data,",
                    "panggil fungsi, bandingkan hasilnya.",
                ],
            },
            {
                "heading": "Lintas platform dan iOS",
                "body": [
                    "Alat uji di platform lain mengikuti piramida yang sama:",
                    "  - iOS memakai XCTest untuk uji unit dan XCUITest untuk uji UI.",
                    "    Sejak Xcode 16 ada juga Swift Testing dengan @Test dan",
                    "    #expect. Semuanya butuh Mac dengan Xcode.",
                    "  - Flutter punya flutter test untuk uji unit dan widget, plus",
                    "    paket integration_test untuk uji di perangkat.",
                    "  - React Native biasanya memakai Jest untuk uji unit dan Detox",
                    "    untuk uji end-to-end. Detox buatan Wix menjalankan aplikasi",
                    "    sungguhan di emulator lalu menekan tombolnya.",
                    "  - Appium menguji aplikasi apa pun lewat protokol WebDriver,",
                    "    dari banyak bahasa, untuk Android maupun iOS.",
                    "  - Firebase Test Lab menjalankan uji instrumentasimu di",
                    "    perangkat fisik milik Google, berguna kalau kamu cuma punya",
                    "    satu HP.",
                ],
            },
            {
                "heading": "Detox untuk React Native",
                "code": """const { device, element, by, expect } = require('detox');

describe('Layar penghitung', () => {
  beforeAll(async () => {
    await device.launchApp();
  });

  it('menambah nilai saat tombol ditekan', async () => {
    await element(by.id('tombol-tambah')).tap();
    await expect(element(by.id('teks-nilai'))).toHaveText('Nilai: 1');
  });
});""",
            },
            {
                "heading": "XCTest untuk Swift",
                "bahasa": "swift",
                "code": """import XCTest

final class PenghitungTests: XCTestCase {
    func testTambah() {
        var p = Penghitung()
        p.tambah()
        XCTAssertEqual(p.nilai, 1)
    }
}""",
            },
            {
                "heading": "Jebakan yang bikin uji nggak bisa dipercaya",
                "body": [
                    "Uji yang kadang lulus kadang gagal tanpa perubahan kode disebut",
                    "flaky. Uji seperti itu lebih buruk daripada nggak ada uji,",
                    "karena lama-lama timmu mengabaikan warna merahnya. Penyebab yang",
                    "paling sering:",
                    "  - Animasi. Matikan skala animasi di Opsi Developer pada",
                    "    perangkat uji supaya tombol nggak sedang bergerak saat",
                    "    ditekan.",
                    "  - Jaringan sungguhan. Uji yang memanggil server asli ikut gagal",
                    "    kalau sinyal jelek. Ganti repository dengan versi palsu yang",
                    "    mengembalikan data tetap.",
                    "  - Logika di Activity. Kode yang menempel di layar cuma bisa",
                    "    diuji lewat uji UI yang lambat. Pindahkan ke ViewModel atau",
                    "    fungsi biasa supaya bisa diuji unit.",
                    "",
                    "Jebakan: jangan mengejar angka cakupan (coverage) 100%. Uji",
                    "paling berharga adalah uji untuk bug yang pernah terjadi, supaya",
                    "bug yang sama nggak lolos lagi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Proyek contoh resmi Google, Now in Android (repositori",
                    "android/nowinandroid di GitHub), memuat uji unit, uji UI",
                    "Compose, dan alur CI yang menjalankannya di setiap pull request.",
                    "Kamu bisa membuka foldernya untuk melihat bagaimana tim besar",
                    "menyusun piramida uji.",
                    "",
                    "Kasus kecil: aplikasi kasir kantin sekolah sudah dua kali",
                    "dirilis dengan bug yang sama. Kode diskon terhitung dua kali",
                    "kalau pembeli menekan tombol Pakai dua kali.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pindahkan perhitungan total dari Activity ke fungsi biasa,",
                    "     misalnya totalBelanja(barang, kodeDiskon), yang nggak tahu",
                    "     apa-apa soal tombol.",
                    "  2. Tulis uji unit yang meniru bug-nya: panggil fungsi pemakai",
                    "     diskon dua kali, lalu pastikan totalnya tetap dipotong",
                    "     sekali.",
                    "  3. Jalankan ./gradlew test. Uji itu harus merah dulu, karena",
                    "     bug-nya masih ada.",
                    "  4. Betulkan kodenya sampai uji itu hijau, lalu jalankan uji",
                    "     ini otomatis di CI setiap ada perubahan.",
                ],
            },
        ],
    },
    {
        "title": "35. Firebase untuk Aplikasi Mobile",
        "sections": [
            {
                "body": [
                    "Hampir semua aplikasi mobile butuh hal yang sama: login, data",
                    "yang tersinkron antar HP, notifikasi, dan laporan kalau",
                    "aplikasinya crash. Membangun server sendiri untuk semua itu",
                    "butuh waktu berminggu-minggu. Firebase adalah platform backend",
                    "milik Google yang menyediakannya sebagai layanan siap pakai.",
                    "Istilahnya BaaS, backend as a service.",
                    "",
                    "Layanan yang paling sering dipakai di aplikasi mobile:",
                    "  - Authentication: login dengan email, nomor HP, atau akun",
                    "    Google.",
                    "  - Cloud Firestore: database dokumen yang tersinkron langsung",
                    "    ke aplikasi.",
                    "  - Cloud Messaging (FCM): mengirim notifikasi push.",
                    "  - Crashlytics: mengumpulkan laporan crash dari HP pengguna.",
                    "  - Remote Config: mengubah nilai di aplikasi tanpa rilis baru.",
                    "  - App Distribution: membagikan versi uji ke penguji.",
                    "",
                    "SDK klien Firebase berlisensi Apache-2.0, sedangkan layanannya",
                    "milik Google. Ada paket gratis Spark dengan kuota terbatas, dan",
                    "paket Blaze yang dibayar sesuai pemakaian. Versi paket pengatur",
                    "versi (BoM) Firebase untuk Android saat materi ini ditulis",
                    "(Oktober 2026) adalah 35.0.2, rilis 15 Oktober 2026.",
                ],
            },
            {
                "heading": "app/build.gradle.kts",
                "bahasa": "gradle",
                "code": """dependencies {
    implementation(platform("com.google.firebase:firebase-bom:35.0.2"))
    implementation("com.google.firebase:firebase-auth")
    implementation("com.google.firebase:firebase-firestore")
}""",
            },
            {
                "heading": "Firestore: koleksi dan dokumen",
                "body": [
                    "Firestore nggak punya tabel. Datanya berbentuk dokumen, yaitu",
                    "kumpulan pasangan nama dan nilai mirip objek JSON. Dokumen",
                    "dikelompokkan dalam koleksi, dan satu dokumen boleh punya",
                    "subkoleksi. Alamat sebuah dokumen ditulis seperti jalur folder,",
                    "misalnya pengguna/uid_budi/catatan/c1.",
                    "",
                    "Di Android dan iOS, Firestore menyimpan salinan data di HP",
                    "secara bawaan. Aplikasi tetap bisa membaca dan menulis saat",
                    "offline, lalu perubahan dikirim begitu sinyal kembali. Cara",
                    "kerja semacam itu yang kamu bangun sendiri di proyek akhir bab",
                    "berikutnya.",
                ],
            },
            {
                "heading": "Menyimpan catatan dari Kotlin",
                "bahasa": "kotlin",
                "code": """import com.google.firebase.Firebase
import com.google.firebase.firestore.firestore

val db = Firebase.firestore

fun simpanCatatan(uid: String, teks: String) {
    val data = hashMapOf("pemilik" to uid, "teks" to teks)
    db.collection("catatan").add(data)
        .addOnSuccessListener { ref -> println("tersimpan: ${ref.id}") }
        .addOnFailureListener { e -> println("gagal: ${e.message}") }
}""",
            },
            {
                "heading": "Aturan keamanan",
                "body": [
                    "Aplikasi berbicara langsung dengan database, tanpa server",
                    "buatanmu di tengah. Artinya satu-satunya penjaga datamu adalah",
                    "aturan keamanan (security rules) Firestore. Aturan menentukan",
                    "siapa boleh membaca dan menulis dokumen mana:",
                    "",
                    "  rules_version = '2';",
                    "  service cloud.firestore {",
                    "    match /databases/{database}/documents {",
                    "      match /catatan/{id} {",
                    "        allow read: if request.auth != null",
                    "          && request.auth.uid == resource.data.pemilik;",
                    "        allow create: if request.auth != null",
                    "          && request.auth.uid == request.resource.data.pemilik;",
                    "      }",
                    "    }",
                    "  }",
                    "",
                    "request.auth berisi pengguna yang sedang login, atau null kalau",
                    "belum login. resource.data adalah dokumen yang sudah ada di",
                    "database, sedangkan request.resource.data adalah data yang mau",
                    "ditulis. Semua yang nggak diizinkan aturan otomatis ditolak.",
                    "Aturan juga bukan penyaring: query yang mungkin mengambil",
                    "dokumen milik orang lain langsung ditolak seluruhnya, jadi",
                    "query-mu harus ikut menyaring dengan where pemilik sama dengan",
                    "uid.",
                    "",
                    "Jebakan: mode uji saat membuat database memberi aturan yang",
                    "membuka semua data untuk sementara waktu. Banyak aplikasi",
                    "pemula lupa menggantinya, sehingga data penggunanya bisa dibaca",
                    "siapa saja yang tahu nama proyeknya. Uji aturanmu di Firebase",
                    "Emulator Suite sebelum rilis.",
                    "",
                    "Ingat: API key di berkas google-services.json memang ikut",
                    "terbawa di aplikasi dan bukan rahasia. Ia cuma menandai",
                    "proyekmu. Keamanan datang dari aturan di atas dan dari App",
                    "Check, yang memastikan permintaan datang dari aplikasimu yang",
                    "asli.",
                ],
            },
            {
                "heading": "Notifikasi dengan FCM",
                "body": [
                    "FCM mengirim pesan ke perangkat lewat token, yaitu kode unik",
                    "yang didapat aplikasi saat pertama berjalan. Server atau Cloud",
                    "Functions milikmu mengirim pesan ke API HTTP v1 FCM dalam",
                    "bentuk JSON seperti di bawah.",
                    "",
                    "Di Android 13 ke atas, aplikasi wajib minta izin",
                    "POST_NOTIFICATIONS ke pengguna sebelum boleh menampilkan",
                    "notifikasi. Di iOS, proyek Firebase-mu perlu kunci APNs dari",
                    "akun developer Apple.",
                ],
            },
            {
                "heading": "Isi pesan FCM (HTTP v1)",
                "bahasa": "json",
                "code": """{
  "message": {
    "token": "TOKEN_PERANGKAT_PENERIMA",
    "notification": {
      "title": "Pesanan dikirim",
      "body": "Paketmu sedang dalam perjalanan"
    },
    "data": { "pesanan_id": "A-1029" }
  }
}""",
            },
            {
                "heading": "Crashlytics, Remote Config, dan App Distribution",
                "body": [
                    "Crashlytics mengumpulkan crash dari HP pengguna, lengkap dengan",
                    "jejak tumpukan (stack trace) dan jumlah pengguna yang kena,",
                    "lalu mengelompokkan crash yang sama. Kalau build rilismu",
                    "diacak namanya oleh R8, plugin Gradle Crashlytics mengunggah",
                    "berkas pemetaan supaya jejaknya tetap terbaca.",
                    "",
                    "Remote Config menyimpan nilai yang bisa kamu ubah dari konsol",
                    "tanpa rilis baru, misalnya teks banner promo atau saklar untuk",
                    "menyalakan fitur baru ke sebagian pengguna dulu. Aplikasi tetap",
                    "harus punya nilai bawaan kalau gagal mengambil yang terbaru.",
                    "",
                    "App Distribution membagikan versi uji Android dan iOS ke",
                    "penguji lewat email, tanpa lewat toko. Bedakan dengan jalur uji",
                    "tertutup di Play Console: syarat uji tertutup untuk akun",
                    "pribadi baru harus dipenuhi di Play Console sendiri.",
                ],
            },
            {
                "heading": "Yang sudah berubah dari tutorial lama",
                "body": [
                    "Firebase sering berubah, jadi tutorial dua tahun lalu bisa",
                    "menyesatkan. Tiga perubahan yang paling sering bikin bingung:",
                    "  - Modul KTX (misalnya firebase-firestore-ktx dan impor",
                    "    com.google.firebase.ktx) berhenti dirilis Juli 2025 dan",
                    "    dikeluarkan dari BoM versi 34.0.0. Fungsi Kotlin-nya sudah",
                    "    pindah ke modul utama, seperti di contoh tadi.",
                    "  - API lama FCM yang memakai server key sudah usang sejak",
                    "    20 Juni 2023 dan mulai dimatikan 22 Juli 2024. Pakai API",
                    "    HTTP v1 dengan token akses berumur pendek.",
                    "  - Firebase Dynamic Links dimatikan 25 Agustus 2025. Tautan",
                    "    page.link lama sudah nggak berfungsi.",
                    "",
                    "Kapan sebaiknya nggak memakai Firebase? Query Firestore",
                    "terbatas (nggak ada JOIN seperti SQL), biaya paket Blaze bisa",
                    "naik cepat kalau aplikasimu membaca data terlalu sering, dan",
                    "kamu terikat pada layanan Google. Toko F-Droid juga menolak",
                    "aplikasi yang memuat Firebase. Alternatifnya Supabase (berbasis",
                    "PostgreSQL), Appwrite, PocketBase, atau backend buatanmu",
                    "sendiri seperti di kurikulum Backend.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Buka berkas APK aplikasi Android mana pun dengan APK Analyzer",
                    "di Android Studio (menu Build, Analyze APK). Di banyak aplikasi",
                    "populer kamu akan menemukan paket com.google.firebase, tanda",
                    "aplikasinya memakai FCM, Crashlytics, atau layanan Firebase",
                    "lain.",
                    "",
                    "Kasus kecil: aplikasi catatan kelas memakai Firestore. Tiap",
                    "siswa cuma boleh membaca dan mengubah catatannya sendiri,",
                    "sedangkan guru boleh membaca semua catatan. Akun guru diberi",
                    "penanda custom claim guru bernilai true lewat Firebase Admin SDK",
                    "di server.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Simpan uid pemilik di setiap dokumen catatan, di medan",
                    "     pemilik.",
                    "  2. Izinkan baca untuk pemilik atau guru:",
                    "       allow read: if request.auth != null && (",
                    "         request.auth.uid == resource.data.pemilik",
                    "         || request.auth.token.guru == true);",
                    "  3. Izinkan tulis cuma untuk pemilik, dan pastikan medan",
                    "     pemilik di data baru tetap uid si penulis.",
                    "  4. Uji di Emulator Suite dengan tiga akun palsu: siswa A,",
                    "     siswa B, dan guru. Siswa B harus ditolak saat membaca",
                    "     catatan siswa A.",
                ],
            },
        ],
    },
    {
        "title": "36. Fastlane dan CI/CD Rilis Mobile",
        "sections": [
            {
                "body": [
                    "Merilis satu versi aplikasi Android itu banyak langkahnya.",
                    "Jalankan uji, naikkan versionCode, build AAB, tanda tangani,",
                    "unggah ke Play Console, isi catatan rilis, lalu pilih jalurnya.",
                    "Di iOS ditambah urusan sertifikat dan provisioning profile.",
                    "Kalau dikerjakan manual tiap minggu, cepat atau lambat ada",
                    "langkah yang terlewat.",
                    "",
                    "Fastlane mengubah langkah-langkah itu jadi satu perintah. Ia",
                    "ditulis dalam Ruby dan berlisensi MIT. Versi terbarunya saat",
                    "materi ini ditulis (Oktober 2026) adalah 2.241.1, rilis",
                    "15 Oktober 2026. Urutan langkah ditulis sebagai lane (jalur) di",
                    "berkas Fastfile, dan tiap langkah disebut action. Ada action",
                    "untuk menjalankan Gradle, membangun aplikasi iOS, mengambil",
                    "tangkapan layar, sampai mengunggah ke Play Store dan",
                    "TestFlight.",
                ],
            },
            {
                "heading": "fastlane/Fastfile untuk Android",
                "bahasa": "ruby",
                "code": """default_platform(:android)

platform :android do
  desc "Uji, build AAB, lalu kirim ke jalur internal Play"
  lane :internal do
    gradle(task: "test")
    gradle(task: "bundle", build_type: "Release")
    upload_to_play_store(track: "internal")
  end
end

# blok platform :ios menyusul di bawah
...""",
            },
            {
                "body": [
                    "gradle(task: \"bundle\", build_type: \"Release\") menjalankan",
                    "tugas bundleRelease, yang menghasilkan berkas AAB.",
                    "upload_to_play_store (nama lainnya supply) mengunggah berkas",
                    "itu lewat API Google Play. Supaya boleh mengunggah, Fastlane",
                    "butuh kunci akun layanan (service account) berformat JSON dari",
                    "Google Cloud yang diberi akses di Play Console. Alamat kunci",
                    "dan nama paket aplikasimu ditulis di berkas fastlane/Appfile.",
                ],
            },
            {
                "heading": "Lane untuk iOS",
                "bahasa": "ruby",
                "code": """# lanjutan Fastfile yang sama, sesudah blok :android
...

platform :ios do
  desc "Build lalu kirim ke TestFlight"
  lane :beta do
    increment_build_number
    match(type: "appstore")
    build_app(scheme: "Catatan")
    upload_to_testflight
  end
end""",
            },
            {
                "body": [
                    "match mengambil sertifikat dan provisioning profile tim dari",
                    "repositori git privat yang terenkripsi, jadi semua anggota tim",
                    "dan mesin CI memakai identitas penandatangan yang sama.",
                    "build_app (nama lainnya gym) membangun aplikasi dengan Xcode,",
                    "dan upload_to_testflight (nama lainnya pilot) mengunggahnya.",
                    "Lane iOS cuma bisa jalan di macOS, karena Xcode cuma ada di",
                    "sana.",
                    "",
                    "Dokumentasi Fastlane menyarankan memasangnya lewat Bundler,",
                    "yaitu pengelola paket Ruby, dengan Gemfile di proyek supaya",
                    "versi Fastlane semua anggota tim sama:",
                ],
            },
            {
                "heading": "Menjalankan lane",
                "bahasa": "terminal",
                "code": """bundle install
bundle exec fastlane android internal
bundle exec fastlane ios beta""",
            },
            {
                "heading": "Menjalankan di CI",
                "body": [
                    "CI (continuous integration) adalah server yang menjalankan",
                    "uji dan build otomatis setiap ada perubahan. CD (continuous",
                    "delivery) melanjutkannya sampai rilis. Contoh di bawah adalah",
                    "alur GitHub Actions yang menjalankan lane internal setiap kali",
                    "kamu mendorong tag versi seperti v1.4.2. Kunci Play disimpan",
                    "sebagai secret repositori, bukan di dalam kode.",
                ],
            },
            {
                "heading": ".github/workflows/rilis.yml",
                "bahasa": "yaml",
                "code": """name: rilis-internal
on:
  push:
    tags: ["v*"]

jobs:
  android:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: "21"
      - uses: ruby/setup-ruby@v1
        with:
          bundler-cache: true
      - run: echo "$KUNCI_PLAY" > kunci-play.json
        env:
          KUNCI_PLAY: ${{ secrets.KUNCI_PLAY }}
      - run: bundle exec fastlane android internal""",
            },
            {
                "body": [
                    "Untuk iOS, job-nya harus memakai mesin macOS, misalnya",
                    "runs-on: macos-latest, karena Xcode nggak ada di Linux. Di",
                    "GitHub Actions, menit mesin macOS dihitung jauh lebih mahal",
                    "daripada mesin Linux untuk repositori privat, jadi banyak tim",
                    "cuma menjalankan build iOS saat rilis.",
                    "",
                    "Selain GitHub Actions, ada layanan CI yang khusus mobile.",
                    "Codemagic populer di kalangan pengguna Flutter dan menyediakan",
                    "mesin macOS. Bitrise juga fokus ke aplikasi mobile. CircleCI",
                    "adalah CI umum yang punya mesin macOS. Apple sendiri punya",
                    "Xcode Cloud yang terhubung ke App Store Connect, dan Expo punya",
                    "EAS Build untuk proyek React Native.",
                ],
            },
            {
                "heading": "Nomor versi dari tag",
                "code": """// Mengubah tag rilis jadi versionCode yang selalu naik.
function versionCode(tag) {
  const [mayor, minor, patch] = tag.replace(/^v/, '').split('.').map(Number);
  if (minor > 99 || patch > 99) throw new Error(`${tag}: minor/patch maksimal 99`);
  return mayor * 10000 + minor * 100 + patch;
}

for (const tag of ['v1.4.2', 'v1.10.0', 'v2.0.0']) {
  console.log(`${tag} -> ${versionCode(tag)}`);
}""",
            },
            {
                "body": [
                    "Keluaran:",
                    "  v1.4.2 -> 10402",
                    "  v1.10.0 -> 11000",
                    "  v2.0.0 -> 20000",
                    "",
                    "Play Console menolak berkas yang versionCode-nya nggak lebih",
                    "besar dari yang pernah diunggah. Banyak tim menurunkan angka itu",
                    "dari tag git seperti di atas, jadi nggak ada lagi yang lupa",
                    "menaikkannya. Batas 99 itu penting: tanpa batas, v1.100.0 akan",
                    "menghasilkan angka yang sama dengan v2.0.0.",
                ],
            },
            {
                "heading": "Tanda tangan dan rahasia",
                "body": [
                    "Aplikasi Android ditandatangani dengan kunci dari berkas",
                    "keystore. Dengan Play App Signing, Google memegang kunci",
                    "penandatangan aplikasi yang asli, sedangkan kamu memakai kunci",
                    "unggah (upload key). Kalau kunci unggah hilang, kamu bisa minta",
                    "Google menggantinya. Aplikasi iOS ditandatangani dengan",
                    "sertifikat dan provisioning profile dari akun developer Apple.",
                    "",
                    "Jebakan: keystore, kata sandinya, kunci akun layanan Play, dan",
                    "sertifikat iOS nggak boleh masuk ke repositori git, termasuk",
                    "repositori privat. Simpan sebagai secret di CI, lalu tulis ke",
                    "berkas sementara saat job berjalan seperti contoh tadi.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi Android open source menyimpan deskripsi toko,",
                    "tangkapan layar, dan catatan rilis di folder",
                    "fastlane/metadata/android di repositorinya. Struktur itu",
                    "dibaca Fastlane saat mengunggah ke Play, dan juga dibaca F-Droid",
                    "saat menampilkan aplikasinya.",
                    "",
                    "Kasus kecil: aplikasi pengumuman sekolah dirilis ke jalur",
                    "internal setiap Jumat. Selama ini satu orang mengerjakannya",
                    "manual dari laptopnya, dan rilis sempat batal karena ia sakit.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat akun layanan di Google Cloud, beri aksesnya di Play",
                    "     Console, lalu unduh kuncinya sebagai JSON.",
                    "  2. Simpan isi JSON itu sebagai secret KUNCI_PLAY di GitHub,",
                    "     begitu juga keystore dan kata sandinya.",
                    "  3. Tulis lane internal di Fastfile dan coba sekali dari",
                    "     laptop dengan bundle exec fastlane android internal.",
                    "  4. Tambahkan alur GitHub Actions yang berjalan saat tag v*",
                    "     didorong. Rilis Jumat cukup dengan git tag v1.5.0 lalu",
                    "     git push origin v1.5.0, dari laptop siapa pun di tim.",
                ],
            },
        ],
    },
    {
        "title": "37. Google Play Console: Jalur Rilis dan Uji Tertutup",
        "sections": [
            {
                "body": [
                    "Aplikasimu sudah jalan di emulator dan di HP sendiri. Supaya",
                    "orang lain bisa memasangnya dari Play Store, kamu perlu Google",
                    "Play Console, yaitu portal Google untuk menerbitkan aplikasi",
                    "Android. Di sana kamu mengunggah berkas aplikasi, mengatur",
                    "siapa yang boleh mencobanya, melihat laporan crash, dan",
                    "membalas ulasan.",
                    "",
                    "Pendaftarannya dibayar sekali, 25 dolar AS, untuk akun pribadi",
                    "maupun akun organisasi. Google juga meminta verifikasi",
                    "identitas pemilik akun. Sebelum aplikasi bisa tampil di toko,",
                    "kamu wajib mengisi beberapa formulir. Ada halaman toko (nama,",
                    "ikon, tangkapan layar), kuesioner rating konten, target usia",
                    "pengguna, dan alamat kebijakan privasi. Ada juga bagian Keamanan",
                    "Data yang menjelaskan data apa saja yang dikumpulkan aplikasimu.",
                ],
            },
            {
                "heading": "Berkas yang diunggah: AAB",
                "body": [
                    "Sejak Agustus 2021, aplikasi baru di Play wajib diunggah",
                    "sebagai Android App Bundle (AAB), bukan APK. AAB berisi semua",
                    "kode dan sumber daya aplikasi, lalu Play membuatkan APK yang",
                    "pas untuk tiap jenis HP. Hasilnya unduhan pengguna lebih kecil.",
                    "AAB selalu memakai Play App Signing: Google memegang kunci",
                    "penandatangan aplikasi, dan kamu menandatangani unggahan dengan",
                    "kunci unggah.",
                    "",
                    "Dua angka versi di build.gradle.kts punya tugas berbeda.",
                    "versionCode adalah bilangan bulat yang wajib naik setiap kali",
                    "kamu mengunggah. versionName adalah teks yang dilihat pengguna,",
                    "misalnya 1.2.0. Play menolak unggahan yang versionCode-nya",
                    "nggak lebih besar dari yang pernah diunggah, walaupun",
                    "versionName-nya beda.",
                ],
            },
            {
                "heading": "app/build.gradle.kts",
                "bahasa": "gradle",
                "code": """android {
    namespace = "id.sekolah.jadwal"
    compileSdk = 37

    defaultConfig {
        applicationId = "id.sekolah.jadwal"
        minSdk = 24
        targetSdk = 36
        versionCode = 7
        versionName = "1.2.0"
    }
}""",
            },
            {
                "heading": "Membangun AAB rilis",
                "bahasa": "terminal",
                "code": """./gradlew bundleRelease
ls app/build/outputs/bundle/release/""",
            },
            {
                "heading": "Empat jalur rilis",
                "body": [
                    "Play Console punya empat jalur (track). Satu build yang sama",
                    "bisa dipromosikan dari jalur sempit ke jalur yang lebih luas:",
                    "  1. Internal. Paling cepat tersedia, untuk paling banyak 100",
                    "     penguji yang kamu undang lewat email. Cocok untuk timmu",
                    "     sendiri.",
                    "  2. Tertutup. Untuk daftar penguji tertentu, biasanya lewat",
                    "     daftar email atau Google Group.",
                    "  3. Terbuka. Siapa pun bisa ikut jadi penguji lewat halaman",
                    "     aplikasimu di Play Store.",
                    "  4. Produksi. Semua pengguna Play di negara yang kamu pilih.",
                    "",
                    "Di jalur produksi, kamu bisa memakai rollout bertahap: versi",
                    "baru dikirim dulu ke sebagian kecil pengguna, misalnya 10%,",
                    "lalu dinaikkan kalau laporan crash-nya aman. Kalau ada masalah,",
                    "rollout bisa dihentikan sebelum semua orang kena.",
                ],
            },
            {
                "heading": "Syarat uji tertutup untuk akun pribadi baru",
                "body": [
                    "Aturan ini yang paling sering menjebak pelajar. Akun",
                    "developer pribadi yang dibuat sesudah 13 November 2023 nggak",
                    "bisa langsung rilis ke produksi. Aplikasinya harus lebih dulu",
                    "diuji di jalur tertutup oleh minimal 12 penguji yang ikut",
                    "(opt-in) terus-menerus selama minimal 14 hari.",
                    "",
                    "Sesudah syarat itu terpenuhi, kamu mengajukan akses produksi",
                    "lewat Dasbor Play Console. Google menanyakan tiga hal: soal uji",
                    "tertutupmu, soal aplikasimu, dan soal kesiapan produksinya.",
                    "",
                    "Jebakan: 14 harinya harus berturut-turut untuk tiap penguji.",
                    "Penguji yang keluar lalu masuk lagi mulai menghitung dari nol.",
                    "Undang lebih dari 12 orang, misalnya 15 sampai 20, supaya",
                    "masih cukup kalau ada yang keluar di tengah jalan.",
                    "",
                    "Akun organisasi nggak kena syarat ini, tapi pendaftarannya",
                    "butuh dokumen badan usaha.",
                ],
            },
            {
                "heading": "Target API level",
                "body": [
                    "Setiap tahun Google menaikkan target API minimal untuk",
                    "aplikasi di Play. Target API adalah nilai targetSdk, yaitu",
                    "versi Android yang perilakunya sudah kamu uji. Tujuannya supaya",
                    "aplikasi ikut aturan keamanan dan privasi Android terbaru.",
                    "",
                    "Aturan yang berlaku saat materi ini ditulis (Oktober 2026):",
                    "  - Sejak 31 Agustus 2026, aplikasi baru dan pembaruan wajib",
                    "    menargetkan Android 16 (API 36). Aplikasi Wear OS dan",
                    "    Android Automotive OS cukup API 35, sedangkan Android TV dan",
                    "    Android XR cukup API 34.",
                    "  - Perpanjangan sampai 1 November 2026 bisa diminta lewat",
                    "    formulir di Play Console.",
                    "  - Aplikasi lama yang sudah terbit harus menargetkan minimal",
                    "    API 35. Kalau lebih rendah, aplikasinya nggak bisa lagi",
                    "    ditemukan pengguna baru yang HP-nya memakai Android lebih",
                    "    baru dari target itu.",
                    "",
                    "Polanya beberapa tahun terakhir: target minimal naik satu",
                    "level tiap akhir Agustus. Cek halaman resmi persyaratan target",
                    "API setiap kali kamu mau rilis, jangan mengandalkan tutorial.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Semua aplikasi di Play Store melewati jalur yang sama, dari",
                    "aplikasi bank sampai aplikasi absensi sekolah. Halaman bantuan",
                    "Play Console menulis aturan di materi ini dengan rinci, dan",
                    "tanggal-tanggalnya bisa kamu cek sendiri di sana.",
                    "",
                    "Kasus kecil: siswa SMK membuat aplikasi Jadwal Pelajaran dan",
                    "ingin merilisnya di Play Store sebelum ujian akhir semester,",
                    "kira-kira lima minggu lagi. Akun developer pribadinya baru",
                    "dibuat minggu ini.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Hari pertama: bayar pendaftaran, selesaikan verifikasi",
                    "     identitas, dan isi formulir halaman toko, rating konten,",
                    "     kebijakan privasi, serta Keamanan Data.",
                    "  2. Pastikan targetSdk = 36, naikkan versionCode, lalu bangun",
                    "     AAB dengan ./gradlew bundleRelease.",
                    "  3. Unggah ke jalur internal untuk mencobanya di HP sendiri.",
                    "  4. Buat jalur tertutup, undang 15 sampai 20 teman lewat Google",
                    "     Group, dan minta mereka tetap ikut sampai uji selesai.",
                    "  5. Sesudah 14 hari, ajukan akses produksi lewat Dasbor.",
                    "     Sisakan seminggu untuk proses peninjauan.",
                    "  6. Rilis produksi dengan rollout bertahap, mulai dari 20%.",
                ],
            },
        ],
    },
    {
        "title": "38. Verifikasi Developer Android Mulai 2026",
        "sections": [
            {
                "body": [
                    "Selama ini Android dikenal terbuka. Siapa pun bisa membangun",
                    "APK lalu membagikannya lewat situs atau aplikasi chat, dan",
                    "pengguna cukup mengizinkan pemasangan dari sumber yang nggak",
                    "dikenal. Keterbukaan yang sama juga dipakai penipu. Di",
                    "Indonesia, modus APK palsu berkedok undangan pernikahan atau",
                    "surat tilang yang dikirim lewat WhatsApp ramai diberitakan",
                    "sejak 2023.",
                    "",
                    "Google menjawabnya dengan verifikasi developer Android:",
                    "aplikasi yang dipasang di perangkat Android bersertifikat harus",
                    "berasal dari developer yang sudah mendaftarkan identitas dan",
                    "nama paket aplikasinya. Perangkat bersertifikat artinya HP yang",
                    "sudah lolos pengujian Google dan memuat layanan Google Play,",
                    "yaitu hampir semua HP Android yang dijual resmi. Indonesia",
                    "termasuk empat negara pertama yang memberlakukannya.",
                ],
            },
            {
                "heading": "Siapa yang kena dan sejak kapan",
                "body": [
                    "Jadwal dari halaman resmi Android Developers:",
                    "",
                    "  Juni 2026       layanan sistem mulai digulirkan",
                    "  Agustus 2026    akun limited distribution dan advanced flow",
                    "                  dibuka untuk semua",
                    "  30 Sept 2026    penegakan di Brasil, Indonesia, Singapura,",
                    "                  dan Thailand",
                    "  2027            diperluas ke semua aplikasi di perangkat",
                    "                  bersertifikat di seluruh dunia",
                    "",
                    "Penegakan tahap pertama ini berlaku untuk HP bersertifikat",
                    "dengan Android 7 ke atas. Yang diperiksa adalah aplikasi yang",
                    "dipasang dari toko mitra: Google Play, toko aplikasi Honor dan",
                    "Oppo, Samsung Galaxy Store, Palm Store milik Transsion,",
                    "V-Appstore milik vivo, dan GetApps milik Xiaomi. Developer yang belum",
                    "terverifikasi sampai 30 September 2026 nggak bisa dipasang",
                    "aplikasinya dari toko-toko itu di empat negara tadi.",
                    "",
                    "Menurut FAQ resminya, APK yang dipasang langsung dan toko lain",
                    "seperti F-Droid belum kena di tahap ini. Tapi Google menyebut",
                    "kemampuan verifikasi akan diperluas ke semua toko pihak ketiga,",
                    "dan tahun 2027 berlaku untuk semua aplikasi. Jadi anggap saja",
                    "aturan ini akan berlaku untuk semua APK-mu.",
                ],
            },
            {
                "heading": "Apa artinya untuk developer",
                "body": [
                    "Kalau aplikasimu ada di Google Play dan memakai Play App",
                    "Signing, Google sudah punya data untuk mengenali pemiliknya,",
                    "dan aplikasi yang memenuhi syarat didaftarkan otomatis.",
                    "",
                    "Kalau aplikasimu dibagikan di luar Play, pendaftarannya lewat",
                    "Android Developer Console. Ada dua jenis akun:",
                    "  - Full distribution: verifikasi identitas dengan dokumen",
                    "    resmi dan biaya 25 dolar AS. Kamu mendaftarkan nama paket",
                    "    dan kunci penandatangannya. Satu paket boleh punya lebih",
                    "    dari satu kunci.",
                    "  - Limited distribution: untuk pelajar, guru, dan hobi. Tanpa",
                    "    KTP dan tanpa biaya, tapi aplikasinya cuma bisa dibagikan ke",
                    "    paling banyak 20 perangkat tertentu, untuk uji dan",
                    "    pemakaian pribadi.",
                ],
            },
            {
                "heading": "Pintu untuk developer dan pengguna mahir",
                "body": [
                    "Saat mengembangkan aplikasi, kamu tetap bebas memasang lewat",
                    "ADB (Android Debug Bridge) tanpa verifikasi. Jalur ini memang",
                    "disediakan untuk uji di HP sendiri:",
                ],
            },
            {
                "heading": "Memasang APK uji lewat kabel USB",
                "bahasa": "terminal",
                "code": """adb devices
adb install app/build/outputs/apk/debug/app-debug.apk""",
            },
            {
                "body": [
                    "Untuk pengguna mahir yang ingin memasang aplikasi dari",
                    "developer yang belum terverifikasi, Google menyediakan advanced",
                    "flow. Langkahnya menurut FAQ resmi:",
                    "  1. Nyalakan mode developer di pengaturan sistem.",
                    "  2. Lewati pemeriksaan singkat yang memastikan nggak ada orang",
                    "     yang sedang membujukmu mematikan perlindungan.",
                    "  3. Mulai ulang HP dan masuk lagi. Ini memutus akses jarak jauh",
                    "     dan panggilan telepon yang sedang berjalan.",
                    "  4. Tunggu masa perlindungan satu hari, sekali saja.",
                    "  5. Konfirmasi bahwa kamu paham risikonya, lalu pilih izinkan",
                    "     selama 7 hari atau seterusnya.",
                    "",
                    "Langkah 2 dan 3 sengaja dibuat untuk menggagalkan modus penipu",
                    "yang menelepon korban sambil menuntunnya memasang APK.",
                ],
            },
            {
                "heading": "Dampak ke toko lain",
                "body": [
                    "F-Droid membangun dan menandatangani banyak aplikasinya",
                    "sendiri dari kode sumber, jadi aturan yang mengikat kunci",
                    "penandatangan ke identitas developer menyentuh cara kerjanya.",
                    "Saat materi ini ditulis, situs F-Droid memasang spanduk yang",
                    "menyebut F-Droid sedang terancam oleh perubahan cara Google",
                    "mengatur pemasangan aplikasi.",
                    "",
                    "Ingat: aturan ini masih bergerak. Sebelum membagikan APK di luar",
                    "Play, buka halaman developer verification di",
                    "developer.android.com dan baca bagian jadwal dan FAQ-nya.",
                    "Artikel lama yang cuma menyuruh menyalakan sumber tidak dikenal",
                    "nggak lagi menceritakan seluruh ceritanya.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak aplikasi kecil di Indonesia dibagikan sebagai APK:",
                    "aplikasi absensi ekskul, kasir warung, atau aplikasi internal",
                    "kantor kelurahan. Untuk aplikasi seperti itu, 2027 adalah batas",
                    "untuk menentukan jalurnya, entah lewat Play, akun full",
                    "distribution, atau akun limited distribution.",
                    "",
                    "Kasus kecil: kamu membuat aplikasi absensi untuk 15 anggota",
                    "ekskul robotik. Aplikasinya nggak mau kamu terbitkan di Play,",
                    "dan kamu belum punya KTP karena masih 16 tahun.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Selama pengembangan, pasang ke HP teman lewat adb install",
                    "     saat kumpul ekskul. Jalur ADB nggak butuh verifikasi.",
                    "  2. Daftar akun limited distribution di Android Developer",
                    "     Console. Akun ini gratis dan nggak meminta KTP.",
                    "  3. Daftarkan nama paket dan kunci penandatangan aplikasimu,",
                    "     lalu daftarkan HP anggota mengikuti petunjuk di konsol.",
                    "     Batasnya 20 perangkat, jadi 15 anggota masih cukup.",
                    "  4. Kalau anggota bertambah lewat dari 20, pindah ke jalur",
                    "     Play dengan uji tertutup, atau minta pembina ekskul membuat",
                    "     akun full distribution.",
                ],
            },
        ],
    },
    {
        "title": "39. App Store Connect dan TestFlight",
        "sections": [
            {
                "body": [
                    "Untuk iPhone dan iPad, portalnya bernama App Store Connect.",
                    "Di sana kamu membuat catatan aplikasi, mengunggah build,",
                    "membagikan versi uji lewat TestFlight, dan mengirim aplikasi",
                    "untuk ditinjau sebelum terbit.",
                    "",
                    "Syaratnya:",
                    "  - Ikut Apple Developer Program, 99 dolar AS per tahun. Akun",
                    "    organisasi juga butuh nomor identitas usaha dari Dun &",
                    "    Bradstreet.",
                    "  - Build harus dibangun dengan Xcode 26 atau lebih baru",
                    "    memakai SDK 26. Aturan ini berlaku sejak 28 April 2026.",
                    "  - Sejak 9 September 2026, aplikasi iOS dan iPadOS yang diunggah",
                    "    harus menargetkan iOS 13 atau lebih baru.",
                    "",
                    "Tanpa membayar, kamu tetap bisa memasang aplikasi buatanmu ke",
                    "iPhone sendiri lewat Xcode dengan Apple ID biasa, tapi",
                    "aplikasinya berhenti bisa dibuka sesudah 7 hari dan harus",
                    "dipasang ulang.",
                    "",
                    "Jebakan: Xcode cuma ada di macOS. Dari Fedora, jalurnya lewat",
                    "build di cloud: layanan build Expo, Codemagic, atau",
                    "CI dengan mesin macOS seperti di materi Fastlane.",
                ],
            },
            {
                "heading": "Dari build sampai toko",
                "body": [
                    "Urutan kerjanya:",
                    "  1. Daftarkan bundle ID, misalnya id.sekolah.jadwal, di akun",
                    "     developer, lalu buat catatan aplikasi di App Store Connect.",
                    "  2. Bangun build rilis. Di Mac lewat Xcode (Product, lalu",
                    "     Archive), dari Linux lewat build cloud Expo atau CI macOS.",
                    "  3. Unggah lewat Xcode Organizer, aplikasi Transporter, perintah",
                    "     eas submit, atau action upload_to_testflight milik Fastlane.",
                    "  4. Tunggu build selesai diproses, lalu bagikan lewat",
                    "     TestFlight.",
                    "  5. Lengkapi halaman toko: tangkapan layar, deskripsi, rincian",
                    "     privasi aplikasi, dan jawaban kuesioner rating usia.",
                    "  6. Kirim untuk App Review. Sesudah disetujui, terbitkan manual",
                    "     atau otomatis. Pembaruan juga bisa dirilis bertahap",
                    "     (phased release) selama 7 hari.",
                ],
            },
            {
                "heading": "Dari Fedora lewat Expo",
                "bahasa": "terminal",
                "code": """npx eas-cli build --platform ios --profile production
npx eas-cli submit --platform ios --latest""",
            },
            {
                "heading": "TestFlight",
                "body": [
                    "TestFlight adalah layanan uji beta Apple. Angka yang perlu kamu",
                    "tahu, dari dokumentasi Apple:",
                    "  - Penguji internal: sampai 100 orang, yaitu anggota timmu yang",
                    "    punya akses ke App Store Connect.",
                    "  - Penguji eksternal: sampai 10.000 orang, diundang lewat email",
                    "    atau tautan publik.",
                    "  - Build pertama yang dibagikan ke grup eksternal harus lolos",
                    "    tinjauan dulu. Build berikutnya biasanya nggak perlu",
                    "    tinjauan penuh.",
                    "  - Satu build bisa diuji paling lama 90 hari. Sesudah itu",
                    "    penguji nggak bisa membukanya lagi.",
                    "  - Satu penguji bisa memakai aplikasi beta di sampai 30",
                    "    perangkat.",
                    "",
                    "Beda dengan Play, Apple nggak mewajibkan jumlah penguji",
                    "tertentu sebelum rilis. Yang wajib dilewati adalah App Review.",
                ],
            },
            {
                "heading": "App Review",
                "body": [
                    "Setiap aplikasi dan setiap pembaruan ditinjau tim Apple",
                    "berdasarkan App Review Guidelines. Alasan penolakan yang",
                    "paling sering dialami pemula:",
                    "  - Aplikasi crash atau masih berisi teks contoh (placeholder).",
                    "  - Aplikasi butuh login tapi kamu nggak memberi akun demo untuk",
                    "    peninjau.",
                    "  - Aplikasinya terlalu sederhana, misalnya cuma membungkus satu",
                    "    situs web tanpa fitur tambahan. Pedomannya menyebut ini",
                    "    fungsi minimum.",
                    "  - Rincian privasi di halaman toko nggak cocok dengan data yang",
                    "    dikumpulkan aplikasi atau SDK di dalamnya.",
                    "",
                    "Sejak 1 Mei 2024, aplikasi yang memakai API tertentu, termasuk",
                    "lewat SDK pihak ketiga, wajib menyertakan alasan pemakaiannya",
                    "di privacy manifest. Kalau ditolak, baca pasal pedoman yang",
                    "disebut di pesan penolakan, betulkan, lalu kirim ulang. Kamu",
                    "juga bisa membalas peninjau lewat App Store Connect.",
                ],
            },
            {
                "heading": "Sertifikat dan provisioning profile",
                "body": [
                    "Aplikasi iOS ditandatangani dengan sertifikat dari akun",
                    "developer. Provisioning profile menghubungkan sertifikat itu",
                    "dengan bundle ID dan, untuk build uji, dengan daftar perangkat.",
                    "Xcode bisa mengurusnya otomatis lewat opsi automatic signing.",
                    "Layanan build Expo bisa membuatkannya untukmu, dan Fastlane",
                    "match membagikannya ke seluruh tim lewat repositori terenkripsi.",
                    "",
                    "Ringkasnya, dibandingkan Play Console: biaya Apple tahunan,",
                    "bukan sekali bayar; uji beta nggak punya syarat jumlah penguji;",
                    "setiap rilis ditinjau manusia; dan alat build-nya terikat pada",
                    "macOS.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Semua aplikasi di App Store, dari aplikasi bank sampai game,",
                    "melewati App Store Connect dan App Review. Banyak tim kecil",
                    "yang memakai React Native atau Flutter membangun versi iOS-nya",
                    "tanpa pernah membuka Xcode, lewat layanan build Expo atau",
                    "Codemagic.",
                    "",
                    "Kasus kecil: aplikasi Jadwal Pelajaran buatanmu memakai Expo,",
                    "dan kamu cuma punya laptop Fedora. Wali kelas dan beberapa guru",
                    "memakai iPhone dan ingin mencobanya sebelum dirilis.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar Apple Developer Program (99 dolar AS per tahun),",
                    "     misalnya lewat akun sekolah kalau ada dana.",
                    "  2. Jalankan npx eas-cli build --platform ios. Expo membangun",
                    "     di mesin macOS milik Expo dan membuatkan sertifikat serta",
                    "     provisioning profile kalau kamu mengizinkan.",
                    "  3. Jalankan npx eas-cli submit --platform ios --latest untuk",
                    "     mengunggah build itu ke App Store Connect.",
                    "  4. Buat grup penguji eksternal di TestFlight dan bagikan",
                    "     tautan publiknya ke guru-guru. Build pertama menunggu",
                    "     tinjauan beta dulu.",
                    "  5. Sesudah masukan guru beres, kirim build yang sama untuk",
                    "     App Review dengan akun demo kalau aplikasinya butuh login.",
                ],
            },
        ],
    },
    {
        "title": "40. Toko Lain: F-Droid dan Microsoft Store",
        "sections": [
            {
                "body": [
                    "Play Store dan App Store bukan satu-satunya tempat membagikan",
                    "aplikasi. Kalau aplikasimu open source, atau aplikasimu justru",
                    "aplikasi desktop, ada toko lain yang lebih cocok. Materi ini",
                    "membahas dua yang paling sering ditanyakan: F-Droid untuk",
                    "Android dan Microsoft Store untuk Windows.",
                ],
            },
            {
                "heading": "F-Droid",
                "body": [
                    "F-Droid adalah toko aplikasi Android khusus perangkat lunak",
                    "bebas dan open source. Aplikasi klien F-Droid sendiri",
                    "berlisensi GPL-3.0. Aturan masuknya ketat, dan semuanya demi",
                    "satu hal: pengguna bisa yakin aplikasinya dibangun dari kode",
                    "yang bisa dilihat siapa saja.",
                    "",
                    "Menurut kebijakan inklusinya:",
                    "  - Seluruh aplikasi wajib berlisensi bebas dan open source,",
                    "    misalnya GPL atau Apache.",
                    "  - Proses build-nya harus memakai perkakas yang seluruhnya",
                    "    open source. F-Droid membangun aplikasinya sendiri dari",
                    "    kode sumber, bukan menerima APK buatanmu.",
                    "  - Pustaka pelacak, iklan, dan analitik proprietary seperti",
                    "    Google Play Services, Firebase, dan Crashlytics dilarang.",
                    "    Kalau aplikasimu memakainya, sediakan varian build",
                    "    (flavor) tanpa pustaka itu.",
                    "",
                    "F-Droid juga memasang label anti-fitur. Label ini memberi tahu",
                    "pengguna hal yang mungkin nggak mereka sukai, misalnya Ads",
                    "(iklan), Tracking (pelacakan), Non-Free Network Services",
                    "(bergantung pada layanan jaringan yang nggak bebas), dan Known",
                    "Vulnerability (ada celah keamanan yang diketahui).",
                    "",
                    "Cara mengajukan aplikasi: buat berkas metadata di repositori",
                    "fdroiddata di GitLab lewat merge request. Contohnya di bawah.",
                    "Deskripsi dan tangkapan layar bisa diambil F-Droid dari folder",
                    "fastlane/metadata di repositorimu.",
                ],
            },
            {
                "heading": "metadata/id.sekolah.jadwal.yml",
                "bahasa": "yaml",
                "code": """License: GPL-3.0-or-later
SourceCode: https://github.com/contoh/jadwal-pelajaran
IssueTracker: https://github.com/contoh/jadwal-pelajaran/issues

RepoType: git
Repo: https://github.com/contoh/jadwal-pelajaran.git

Builds:
  - versionName: 1.2.0
    versionCode: 7
    commit: v1.2.0
    subdir: app
    gradle:
      - yes

AutoUpdateMode: Version
UpdateCheckMode: Tags
CurrentVersion: 1.2.0
CurrentVersionCode: 7""",
            },
            {
                "body": [
                    "Builds memberi tahu F-Droid commit atau tag mana yang dibangun",
                    "untuk tiap versi. UpdateCheckMode: Tags membuat F-Droid",
                    "memeriksa tag baru di repositorimu, dan AutoUpdateMode: Version",
                    "menambahkan versi baru otomatis. Prosesnya lebih lambat dari",
                    "Play: dari tag baru sampai aplikasinya muncul di F-Droid bisa",
                    "butuh beberapa hari.",
                    "",
                    "Ingat: F-Droid termasuk pihak yang terdampak verifikasi",
                    "developer Android yang dibahas di materi sebelumnya. Cek kabar",
                    "terbarunya di situs F-Droid sebelum memilihnya sebagai",
                    "satu-satunya jalur distribusi.",
                ],
            },
            {
                "heading": "Microsoft Store",
                "body": [
                    "Microsoft Store adalah toko aplikasi bawaan Windows. Ia",
                    "menerima banyak jenis aplikasi desktop: WinUI, WPF, WinForms,",
                    "Electron, Tauri, sampai PWA. Paketnya boleh berformat .msix atau",
                    "pemasang biasa berformat .exe atau .msi.",
                    "",
                    "Sejak September 2025, pendaftaran developer perorangan di",
                    "Microsoft Store gratis di hampir 200 negara, dan nggak butuh",
                    "kartu kredit. Gantinya, kamu memverifikasi identitas dengan",
                    "kartu identitas dan swafoto. Akun perusahaan masih dikenai",
                    "biaya pendaftaran. Pengajuan aplikasi dilakukan lewat Partner",
                    "Center, lalu aplikasinya melewati proses sertifikasi sebelum",
                    "tampil di toko.",
                    "",
                    "Pilihan lain di Windows adalah winget, pengelola paket bawaan",
                    "Windows. Aplikasimu bisa didaftarkan ke repositori komunitasnya",
                    "(winget-pkgs di GitHub) supaya orang bisa memasangnya dengan",
                    "satu perintah.",
                ],
            },
            {
                "heading": "Distribusi desktop lain",
                "body": [
                    "  - Linux: Flathub adalah toko utama untuk paket Flatpak, dan",
                    "    aplikasi GNOME biasanya terbit di sana. Snap Store milik",
                    "    Canonical melayani paket Snap. AppImage adalah satu berkas",
                    "    yang bisa langsung dijalankan tanpa toko.",
                    "  - macOS: Mac App Store lewat App Store Connect yang sama",
                    "    dengan iOS. Di luar toko, aplikasi Mac perlu ditandatangani",
                    "    dengan sertifikat Developer ID dan dinotarisasi Apple supaya",
                    "    nggak diblokir Gatekeeper.",
                    "  - Game punya toko sendiri, seperti Steam dan itch.io. Keduanya",
                    "    dibahas di kurikulum Game.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi open source populer seperti pemutar podcast,",
                    "pengelola kata sandi, dan peramban privasi sering terbit di",
                    "F-Droid sekaligus di Play. Di Windows, banyak aplikasi Electron",
                    "dan PWA sekarang bisa ditemukan di Microsoft Store.",
                    "",
                    "Kasus kecil: kamu membuat aplikasi catatan open source dengan",
                    "dua versi, yaitu Android (Kotlin) dan desktop Windows (Tauri).",
                    "Versi Android memakai Firebase Crashlytics untuk laporan crash.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Buat dua flavor Android: play yang memakai Crashlytics, dan",
                    "     foss yang tanpa Firebase sama sekali.",
                    "  2. Pastikan seluruh kode berlisensi bebas, misalnya GPL-3.0,",
                    "     dan tulis berkas LICENSE di repositori.",
                    "  3. Tulis metadata F-Droid yang membangun flavor foss dari tag",
                    "     rilis, lalu ajukan merge request ke fdroiddata.",
                    "  4. Untuk versi Windows, daftar akun perorangan gratis di",
                    "     Microsoft Store, verifikasi identitas, lalu unggah pemasang",
                    "     .msi hasil npm run tauri build lewat Partner Center.",
                ],
            },
        ],
    },
    {
        "title": "41. Aturan Baru yang Bikin Tutorial Lama Menyesatkan",
        "sections": [
            {
                "body": [
                    "Video dan artikel tutorial bertahan bertahun-tahun di internet,",
                    "sementara aturan toko dan alatnya berubah tiap tahun. Akibatnya",
                    "kamu bisa mengikuti tutorial langkah demi langkah dengan benar,",
                    "lalu tetap gagal di akhir. Kesalahannya ada di aturan yang",
                    "sudah berganti, sementara tutorialnya nggak ikut diperbarui.",
                    "",
                    "Materi ini merangkum perubahan yang paling sering bikin",
                    "tutorial lama menyesatkan, lengkap dengan tanggalnya, supaya",
                    "kamu bisa menilai sendiri tutorial yang sedang kamu baca.",
                ],
            },
            {
                "heading": "Distribusi Android",
                "body": [
                    "  - Aplikasi baru wajib AAB sejak Agustus 2021. Tutorial yang",
                    "    mengunggah APK ke Play Console sudah basi.",
                    "  - Akun Play pribadi yang dibuat sesudah 13 November 2023 wajib",
                    "    uji tertutup dengan minimal 12 penguji selama 14 hari",
                    "    berturut-turut sebelum rilis produksi. Tutorial yang",
                    "    langsung menekan tombol rilis produksi nggak berlaku untuk",
                    "    akun baru.",
                    "  - Sejak 31 Agustus 2026, aplikasi baru dan pembaruan wajib",
                    "    menargetkan API 36, dengan perpanjangan sampai",
                    "    1 November 2026. Tutorial yang menulis targetSdk 33 atau 34",
                    "    akan ditolak saat unggah.",
                    "  - Sejak 30 September 2026, pemasangan dari toko mitra di",
                    "    Indonesia butuh developer terverifikasi, dan tahun 2027",
                    "    diperluas ke semua aplikasi. Tutorial yang menganggap APK",
                    "    bisa dibagikan bebas ke siapa saja perlu dibaca dengan",
                    "    hati-hati.",
                ],
            },
            {
                "heading": "iOS dan Apple",
                "body": [
                    "  - Sejak 28 April 2026, unggahan ke App Store Connect wajib",
                    "    dibangun dengan Xcode 26 atau lebih baru. Tutorial yang",
                    "    memakai Xcode 15 atau 16 nggak bisa diikuti sampai rilis.",
                    "  - Trunk CocoaPods, yaitu daftar pusat paketnya, dijadwalkan",
                    "    jadi read-only permanen mulai 2 Desember 2026, dengan uji",
                    "    coba 1 sampai 7 November 2026. Sesudah itu nggak ada paket",
                    "    baru yang bisa diterbitkan ke sana. Proyek baru sebaiknya",
                    "    memakai Swift Package Manager.",
                    "  - SwiftUI sudah jadi pilihan bawaan untuk tampilan di proyek",
                    "    Xcode baru. Tutorial berbasis storyboard UIKit masih berguna",
                    "    untuk kode lama, tapi bukan titik mulai yang disarankan.",
                ],
            },
            {
                "heading": "Lintas platform dan desktop",
                "body": [
                    "  - React Native 0.82 (Oktober 2025) cuma mendukung New",
                    "    Architecture, dan arsitektur lama dengan bridge sudah",
                    "    dihapus. Tutorial dari sebelum itu yang mengatur",
                    "    newArchEnabled atau membahas bridge sudah nggak cocok.",
                    "  - Dukungan Xamarin dan Xamarin.Forms berakhir 1 Mei 2024.",
                    "    Penggantinya .NET MAUI.",
                    "  - Di Electron, contextIsolation jadi bawaan sejak versi 12 dan",
                    "    sandbox renderer sejak versi 20. Tutorial yang menyalakan",
                    "    nodeIntegration supaya halaman bisa memanggil require",
                    "    berbahaya untuk diikuti.",
                    "  - Template proyek baru di Android Studio memakai Jetpack",
                    "    Compose. Layout XML tetap perlu kamu pahami untuk kode lama.",
                ],
            },
            {
                "heading": "Layanan dan pustaka",
                "body": [
                    "  - API lama Firebase Cloud Messaging yang memakai server key",
                    "    mulai dimatikan 22 Juli 2024. Pakai API HTTP v1.",
                    "  - Modul KTX Firebase dikeluarkan dari BoM 34.0.0 pada bulan",
                    "    Juli 2025. Impor com.google.firebase.ktx sudah nggak dipakai.",
                    "  - Firebase Dynamic Links dimatikan 25 Agustus 2025.",
                    "  - Repositori JCenter berhenti menerima paket baru sejak 2021.",
                    "    Proyek Gradle yang masih menulis jcenter() perlu",
                    "    dibersihkan.",
                    "  - Plugin kotlin-android-extensions (synthetic import) dihapus",
                    "    di Kotlin 1.8, dan AsyncTask sudah usang sejak API 30.",
                    "    Penggantinya ViewBinding dan coroutines.",
                ],
            },
            {
                "heading": "Memindai tanda basi secara otomatis",
                "code": "// Pemindai kecil: cari tanda tutorial basi di potongan kode.\nconst aturan = [\n  (b) => /nodeIntegration:\\s*true/.test(b) && 'Electron: nodeIntegration harus mati',\n  (b) => /jcenter\\(\\)/.test(b) && 'Gradle: JCenter nggak menerima paket baru sejak 2021',\n  (b) => /com\\.google\\.firebase\\.ktx/.test(b) && 'Firebase: modul KTX keluar dari BoM 34.0.0',\n  (b) => {\n    const m = b.match(/targetSdk\\s*=\\s*(\\d+)/);\n    return m && Number(m[1]) < 36 && `Play: targetSdk ${m[1]} < 36 sejak 31 Agustus 2026`;\n  },\n  (b) => {\n    const m = b.match(/\"react-native\":\\s*\"\\^?0\\.(\\d+)/);\n    return m && Number(m[1]) < 82 && `React Native 0.${m[1]}: sebelum era New Architecture saja`;\n  },\n];\n\nconst tutorial = [\n  'repositories { jcenter() }',\n  'targetSdk = 34',\n  'webPreferences: { nodeIntegration: true }',\n  'import com.google.firebase.ktx.Firebase',\n  '\"react-native\": \"0.72.4\"',\n  'targetSdk = 36',\n];\n\ntutorial.forEach((baris, i) => {\n  const temuan = aturan.map((cek) => cek(baris)).filter(Boolean);\n  console.log(`baris ${i + 1}: ${temuan.length ? temuan.join('; ') : 'aman'}`);\n});",
            },
            {
                "body": [
                    "Keluaran:",
                    "  baris 1: Gradle: JCenter nggak menerima paket baru sejak 2021",
                    "  baris 2: Play: targetSdk 34 < 36 sejak 31 Agustus 2026",
                    "  baris 3: Electron: nodeIntegration harus mati",
                    "  baris 4: Firebase: modul KTX keluar dari BoM 34.0.0",
                    "  baris 5: React Native 0.72: sebelum era New Architecture saja",
                    "  baris 6: aman",
                    "",
                    "Tiap aturan adalah fungsi kecil yang mengembalikan pesan atau",
                    "false, lalu filter(Boolean) membuang yang false. Menambah tanda",
                    "basi baru cukup dengan menambah satu fungsi ke daftar.",
                ],
            },
            {
                "heading": "Cara menilai sebuah tutorial",
                "body": [
                    "Sebelum mengikuti tutorial mobile, cek empat hal ini:",
                    "  1. Kapan terbitnya, dan versi berapa yang dipakai. Cari angka",
                    "     seperti compileSdk, targetSdk, versi React Native di",
                    "     package.json, atau versi Xcode di videonya.",
                    "  2. Bandingkan versi itu dengan halaman rilis resmi. Selisih",
                    "     satu versi mayor biasanya masih bisa diikuti, selisih tiga",
                    "     tahun hampir pasti ada yang berubah.",
                    "  3. Cari tanda basi di kodenya: nodeIntegration: true,",
                    "     jcenter(), com.google.firebase.ktx, pod install untuk",
                    "     pustaka yang sudah mendukung SwiftPM, atau unggahan APK ke",
                    "     Play.",
                    "  4. Untuk aturan toko, percayai halaman resmi Play Console,",
                    "     Android Developers, dan Apple Developer, bukan video atau",
                    "     artikel pihak ketiga, termasuk materi ini. Tanggal di",
                    "     materi ini benar per Oktober 2026.",
                ],
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Forum tanya-jawab programmer penuh pertanyaan dari orang yang",
                    "mengikuti tutorial lama: unggahan ditolak karena targetSdk,",
                    "build iOS ditolak karena versi Xcode, atau aplikasi Firebase",
                    "yang gagal dibangun karena modul KTX. Jawabannya hampir selalu",
                    "sama: aturannya sudah berubah sejak tutorial itu dibuat.",
                    "",
                    "Kasus kecil: kamu menemukan video tutorial tahun 2022 berjudul",
                    "\"Bikin aplikasi catatan dan upload ke Play Store\". Isinya",
                    "memakai targetSdk 32, jcenter(), Firebase KTX, dan langsung",
                    "merilis ke produksi.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pakai tutorial itu untuk memahami alur besarnya saja,",
                    "     misalnya cara menyusun layar dan menyimpan catatan.",
                    "  2. Ganti targetSdk jadi 36 dan hapus jcenter() dari daftar",
                    "     repositori, sisakan google() dan mavenCentral().",
                    "  3. Ganti dependensi Firebase -ktx dengan modul utama lewat BoM",
                    "     terbaru, lalu ubah impornya.",
                    "  4. Untuk rilis, ikuti materi Google Play Console di bab ini:",
                    "     AAB, jalur internal, lalu uji tertutup 12 penguji selama",
                    "     14 hari kalau akunmu akun pribadi baru.",
                ],
            },
        ],
    },
]
