RUST_MATERIALS = [
    {
        "title": "1. Pengenalan Rust & Instalasi",
        "sections": [
            {
                "body": [
                    "Rust itu bahasa pemrograman sistem, yaitu bahasa untuk bikin program",
                    "yang dekat dengan mesin: sistem operasi, browser, server. Rust dibikin",
                    "Mozilla, versi 1.0-nya rilis tahun 2015, dan sekarang dikelola Rust",
                    "Foundation.",
                    "",
                    "Beberapa sifat dasarnya:",
                    "  - Compiled. Kodemu diterjemahkan dulu jadi binari mesin, berkas yang",
                    "    langsung dijalankan prosesor. Programnya nggak butuh runtime dan",
                    "    nggak pakai garbage collector, yaitu bagian program yang bersih-bersih",
                    "    memori secara otomatis.",
                    "  - Statically typed. Tipe tiap variabel udah pasti sebelum program",
                    "    jalan. Tapi kamu jarang perlu nulis tipenya, karena compiler jago",
                    "    nebak sendiri. Kemampuan nebak ini namanya inferensi tipe.",
                    "",
                    "Janji utamanya bisa diringkas jadi satu kalimat: secepat C, dan",
                    "memorinya dijamin aman oleh compiler.",
                    "",
                    "Selama kamu nulis Rust biasa (yang disebut Rust aman), bug di bawah ini",
                    "nggak bisa terjadi:",
                    "  - null pointer dereference, yaitu memakai penunjuk yang nggak nunjuk",
                    "    ke mana-mana",
                    "  - use-after-free, memakai memori yang udah dilepas",
                    "  - double free, melepas memori yang sama dua kali",
                    "  - buffer overflow, nulis di luar batas; indeks di Rust selalu dicek",
                    "  - data race antar thread, dua thread ngubah data yang sama di waktu",
                    "    yang sama",
                    "",
                    "Hampir semua pemeriksaan itu dikerjakan compiler waktu kompilasi, jadi",
                    "programmu nggak jadi lambat karenanya. Pengecualiannya indeks: batas",
                    "array dicek waktu program jalan. Kalau indeksnya kelewatan, program",
                    "berhenti dengan pesan error, dan memori di sebelahnya nggak tersentuh.",
                    "",
                    "Harganya juga ada. Compiler bakal menolak kode yang di bahasa lain",
                    "diterima begitu aja. Minggu pertama belajar Rust biasanya kerasa kayak",
                    "debat sama mesin. Itu wajar. Yang kamu lawan itu bug yang belum sempat",
                    "terjadi.",
                    "",
                    "Rust dipakai untuk bikin Firefox, sebagian kernel Linux, Deno, ripgrep,",
                    "backend Discord, Cloudflare, dan bagian inti Android serta Windows.",
                    "",
                    "Cara memasang:",
                    "  - Cara resmi lewat https://rustup.rs:",
                    "      curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
                    "  - Di Fedora: sudo dnf install rust cargo",
                    "  - Cek hasilnya: rustc --version dan cargo --version",
                    "",
                    "Cara menjalankan program:",
                    "  rustc main.rs && ./main    satu berkas",
                    "  cargo new proyek           proyek baru",
                    "  cargo run                  kompilasi & jalankan",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """fn main() {
    println!("Halo Dunia!");
    println!("Aku sedang belajar Rust.");
}"""
            },
            {
                "body": [
                    "Kita bahas bagian-bagiannya:",
                    "",
                    "  fn main()",
                    "    Titik masuk program, tempat program mulai jalan. Setiap program",
                    "    Rust wajib punya tepat satu.",
                    "",
                    "  println!",
                    "    Tanda seru artinya ini makro, bukan fungsi biasa. Makro itu kode",
                    "    yang dikembangkan jadi kode lain waktu kompilasi. Karena itu",
                    "    println! bisa menerima jumlah argumen yang beda-beda, dan format",
                    "    teksnya dicek waktu kompilasi juga. Kalau jumlah argumennya salah,",
                    "    kamu dapat error kompilasi. Programnya nggak sempat jalan lalu",
                    "    crash.",
                    "",
                    "  Titik koma",
                    "    Menandai akhir pernyataan. Di Rust, ada atau nggaknya titik koma",
                    "    bisa mengubah arti kode. Soal ini dibahas di materi \"Fungsi,",
                    "    Ekspresi & Pernyataan\".",
                    "",
                    "Aturan penulisan yang dipakai programmer Rust:",
                    "  1. Indentasi empat spasi. Perintah `cargo fmt` merapikannya otomatis.",
                    "  2. Nama fungsi dan variabel pakai snake_case.",
                    "  3. Nama tipe dan trait pakai PascalCase.",
                    "  4. Konstanta pakai SCREAMING_SNAKE_CASE.",
                    "",
                    "Kalau kamu melanggar aturan nama (nomor 2 sampai 4), compiler ngasih",
                    "peringatan. Programnya tetap jalan, tapi peringatannya muncul tiap kali",
                    "dikompilasi.",
                    "",
                    "Cara nyisipin nilai ke dalam teks:",
                    "  let nama = \"Andi\";",
                    "  println!(\"Halo, {nama}!\");        sejak Rust 1.58",
                    "  println!(\"Halo, {}!\", nama);      bentuk lama, tetap sah",
                    "  println!(\"{:?}\", data);           bentuk debug",
                    "  println!(\"{:#?}\", data);          debug berbaris rapi",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program pertama di Rust biasanya program baris perintah, dan bentuk itu",
                    "juga yang dipakai alat sungguhan seperti ripgrep, pencari teks yang",
                    "menjalankan fitur pencarian di VS Code. Hasil `rustc main.rs` berupa",
                    "satu berkas binari. Berkas itu bisa disalin ke komputer lain dengan",
                    "sistem operasi dan jenis prosesor yang sama, lalu langsung jalan tanpa",
                    "memasang Rust di sana.",
                    "",
                    "Kasus kecil: Warung Bu Sri minta program yang mencetak kop struk tiga",
                    "baris: nama warung, alamat \"Jl. Melati 5, Bogor\", dan nama kasir yang",
                    "bertugas hari itu, misalnya Rina.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis dulu di kertas persis teks yang mau muncul, baris demi baris.",
                    "     Itu target keluaranmu.",
                    "  2. Satu baris keluaran sama dengan satu `println!` di dalam `fn main()`.",
                    "     Bagian yang berganti tiap hari, yaitu nama kasir, disimpan di",
                    "     variabel lalu disisipkan dengan `{kasir}`:",
                    "      let kasir = \"Rina\";",
                    "      println!(\"Warung Bu Sri\");",
                    "      println!(\"Jl. Melati 5, Bogor\");",
                    "      println!(\"Kasir: {kasir}\");",
                    "  3. Simpan sebagai `main.rs`, lalu jalankan `rustc main.rs && ./main`.",
                    "     Hasilnya tiga baris, dan baris terakhir berbunyi \"Kasir: Rina\".",
                    "  4. Coba kasus pinggir: kop struk yang memuat kurung kurawal, misalnya",
                    "     tulisan {member}. Di dalam `println!`, satu kurung kurawal berarti",
                    "     tempat sisipan, jadi tulis `{{member}}`. Kalau ditulis `{member}` dan",
                    "     nggak ada variabel bernama member, rustc menolak programnya.",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Mutabilitas & Tipe Data",
        "sections": [
            {
                "body": [
                    "Di Rust, variabel nggak bisa diubah, kecuali kamu bilang sebaliknya.",
                    "Ini kebalikan dari hampir semua bahasa lain, dan memang disengaja.",
                    "",
                    "  let x = 5;",
                    "  x = 6;          ERROR: cannot assign twice",
                    "",
                    "  let mut y = 5;",
                    "  y = 6;          boleh",
                    "",
                    "Kata `mut` (dari mutable, artinya bisa diubah) yang membuka izinnya.",
                    "Alasannya ada dua. Data yang nggak berubah aman dibagi ke banyak thread",
                    "tanpa perlu dikunci. Selain itu, sebagian besar variabel memang nggak",
                    "pernah perlu berubah. Dengan wajib nulis `mut`, kamu menyatakan niatmu,",
                    "dan orang yang membaca kodemu langsung tahu variabel mana yang perlu",
                    "diawasi.",
                    "",
                    "Shadowing artinya bikin variabel baru dengan nama yang sama:",
                    "",
                    "  let x = 5;",
                    "  let x = x + 1;        x baru, nilainya 6",
                    "  let x = \"enam\";       x baru lagi, sekarang &str",
                    "",
                    "Bedanya dengan `mut`: shadowing boleh mengganti tipe. Ini berguna waktu",
                    "kamu mengubah bentuk data tapi nggak mau mikirin nama baru, misalnya",
                    "teks umur yang diubah jadi angka:",
                    "`let umur = umur.trim().parse::<u32>()?;`",
                    "",
                    "Konstanta ditulis begini:",
                    "  const MAKS: u32 = 100_000;",
                    "",
                    "Bedanya dengan let: const wajib ditulis tipenya, nilainya dihitung",
                    "waktu kompilasi, dan boleh ditaruh di luar fungsi (level global).",
                    "",
                    "Untuk bilangan bulat, Rust nggak punya tipe `int` polos. Yang ada:",
                    "  i8  i16  i32  i64  i128  isize    bertanda",
                    "  u8  u16  u32  u64  u128  usize    tanpa tanda",
                    "",
                    "Huruf i artinya bisa negatif, u artinya cuma nol dan positif. Angkanya",
                    "jumlah bit.",
                    "  - i32 dipakai kalau kamu nggak nulis tipenya.",
                    "  - usize ukurannya sama dengan alamat memori di mesinmu. Tipe ini",
                    "    wajib dipakai untuk indeks dan panjang. Kamu nggak bisa milih tipe",
                    "    lain di situ.",
                    "",
                    "Bilangan pecahan: f32 dan f64. Bawaannya f64.",
                    "",
                    "Tipe lain: bool (true atau false), dan char. Satu char berisi satu",
                    "karakter Unicode, ukurannya 4 byte, dan ditulis pakai kutip tunggal,",
                    "misalnya 'R'.",
                    "",
                    "Rust nggak pernah mengubah tipe tanpa kamu minta. Dari i32 ke i64 pun",
                    "harus kamu tulis sendiri: `x as i64`.",
                ]
            },
            {
                "heading": "Angka, batas, dan konversi",
                "code": """fn main() {
    let a: i32 = 42;
    let b: f64 = 3.75;
    let c: char = 'R';
    let d: bool = true;

    println!("i32  : {} .. {}", i32::MIN, i32::MAX);
    println!("u8   : {} .. {}", u8::MIN, u8::MAX);
    println!("nilai: {a} {b} {c} {d}");

    // Konversi WAJIB eksplisit
    let e = a as f64 / 4.0;
    println!("{a} / 4 = {e}");

    // Pembagian bilangan bulat memotong
    println!("7 / 2 = {}", 7 / 2);
    println!("7.0 / 2.0 = {}", 7.0 / 2.0);

    // Penambahan yang melimpah ditangkap, bukan dibiarkan melingkar
    let besar: u8 = 250;
    println!("250 + 10 (checked) = {:?}", besar.checked_add(10));
    println!("250 + 10 (saturating) = {}", besar.saturating_add(10));
    println!("250 + 10 (wrapping) = {}", besar.wrapping_add(10));
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  i32  : -2147483648 .. 2147483647",
                    "  u8   : 0 .. 255",
                    "  nilai: 42 3.75 R true",
                    "  42 / 4 = 10.5",
                    "  7 / 2 = 3",
                    "  7.0 / 2.0 = 3.5",
                    "  250 + 10 (checked) = None",
                    "  250 + 10 (saturating) = 255",
                    "  250 + 10 (wrapping) = 4",
                    "",
                    "Lihat empat baris terakhir. u8 cuma muat sampai 255, jadi 250 + 10",
                    "kelewatan. Kejadian ini namanya overflow (melimpah). Di C, hasilnya",
                    "jadi 4 tanpa peringatan apa pun, dan program jalan terus pakai angka",
                    "yang salah. Rust minta kamu milih sendiri maksudmu:",
                    "",
                    "  checked_add     -> Option: None kalau melimpah",
                    "  saturating_add  -> berhenti di batas (255)",
                    "  wrapping_add    -> melingkar (perilaku C)",
                    "  overflowing_add -> (hasil, apakah melimpah)",
                    "",
                    "Lalu gimana kalau kamu nulis `besar + 10` biasa? Di build debug,",
                    "program berhenti (panic) dengan pesan 'attempt to add with overflow'.",
                    "Di build release, angkanya melingkar. Perilaku debug dan release",
                    "dibedakan di sini karena pemeriksaan di setiap penjumlahan dianggap",
                    "terlalu mahal untuk program yang udah dirilis.",
                    "",
                    "Garis bawah boleh dipakai sebagai pemisah ribuan: 1_000_000 sama",
                    "dengan 1000000, dan lebih gampang dibaca.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Memilih tipe angka itu pekerjaan sehari-hari di aplikasi kasir dan",
                    "laporan keuangan UMKM. Rupiah disimpan sebagai bilangan bulat, dan tipe",
                    "yang terlalu kecil bikin total penjualan melimpah begitu angkanya",
                    "membesar, misalnya saat laporan bulanan digabung jadi laporan tahunan.",
                    "",
                    "Kasus kecil: sebuah toko rata-rata menjual Rp 7.500.000 per hari, dan",
                    "pemiliknya minta total setahun (365 hari). Tipe apa yang dipakai?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami datanya. Rupiah di sini selalu bulat, jadi pilih bilangan",
                    "     bulat. Pakai tipe bertanda (awalan i), karena retur bisa bikin",
                    "     angkanya minus.",
                    "  2. Perkirakan angka terbesarnya sebelum menulis kode:",
                    "     7.500.000 x 365 = 2.737.500.000.",
                    "  3. Bandingkan dengan batas tipe. `i32::MAX` cuma 2.147.483.647, jadi",
                    "     i32 kekecilan. Pilih i64:",
                    "      let harian: i64 = 7_500_000;",
                    "      let setahun = harian * 365;",
                    "      println!(\"{setahun}\");",
                    "  4. Periksa akibatnya kalau salah pilih. Dengan i32 dan angka yang",
                    "     ditulis langsung di kode, compiler menolak dengan pesan 'this",
                    "     arithmetic operation will overflow'. Kalau angkanya datang dari",
                    "     masukan, build debug panic. `checked_mul(365)`, saudara",
                    "     `checked_add`, mengembalikan None untuk i32 di kasus ini.",
                    "",
                    "Ingat: jangan simpan uang di f64. Di Rust, `0.1 + 0.2` menghasilkan",
                    "0.30000000000000004, dan selisih kecil begitu menumpuk di laporan.",
                ]
            },
        ],
    },
    {
        "title": "3. Fungsi, Ekspresi & Pernyataan",
        "sections": [
            {
                "body": [
                    "Fungsi di Rust ditulis pakai kata `fn`:",
                    "",
                    "  fn tambah(a: i32, b: i32) -> i32 {",
                    "      a + b",
                    "  }",
                    "",
                    "Tipe tiap parameter wajib ditulis. Tipe hasilnya ditulis sesudah tanda",
                    "panah. Kalau nggak ada panahnya, fungsi itu mengembalikan `()`. Tipe ini",
                    "namanya unit, artinya \"nggak ada nilai\", mirip void di Java atau C.",
                    "",
                    "Coba lihat `a + b` di atas. Nggak ada titik koma dan nggak ada return.",
                    "Ini bagian yang paling sering bikin pemula Rust kesandung, jadi kita",
                    "pelan-pelan:",
                    "",
                    "  EKSPRESI    menghasilkan nilai        a + b",
                    "  PERNYATAAN  tidak menghasilkan apa-apa a + b;",
                    "",
                    "Ekspresi itu potongan kode yang menghasilkan nilai. Pernyataan itu",
                    "perintah yang dikerjakan, tapi nggak menghasilkan nilai. Titik koma",
                    "mengubah ekspresi jadi pernyataan, dan nilainya dibuang. Jadi:",
                    "",
                    "  fn f() -> i32 { 5 }     mengembalikan 5",
                    "  fn f() -> i32 { 5; }    ERROR: mengembalikan ()",
                    "",
                    "Pesan error-nya 'expected i32, found ()', dan penyebabnya cuma satu",
                    "titik koma. Begitu kamu tahu ini, pesan itu bakal langsung kamu kenali",
                    "tiap kali muncul.",
                    "",
                    "`return` tetap ada. Biasanya dipakai untuk keluar dari fungsi lebih",
                    "awal:",
                    "",
                    "  fn cek(n: i32) -> &'static str {",
                    "      if n < 0 { return \"negatif\"; }",
                    "      if n == 0 { return \"nol\"; }",
                    "      \"positif\"",
                    "  }",
                    "",
                    "Hampir semua hal di Rust itu ekspresi, termasuk if dan blok kurung",
                    "kurawal:",
                    "",
                    "  let status = if n >= 75 { \"lulus\" } else { \"ulang\" };",
                    "  let y = { let a = 3; a * a };      y bernilai 9",
                    "",
                    "Karena if menghasilkan nilai, Rust nggak butuh operator ternary",
                    "(`syarat ? a : b` di bahasa lain).",
                ]
            },
            {
                "heading": "Fungsi, blok, dan nilai kembalian",
                "code": """fn luas_persegi(sisi: f64) -> f64 {
    sisi * sisi
}

fn bagi(a: i32, b: i32) -> (i32, i32) {
    (a / b, a % b)          // tuple: dua nilai sekaligus
}

fn grade(nilai: u32) -> char {
    if nilai >= 85 {
        'A'
    } else if nilai >= 75 {
        'B'
    } else if nilai >= 60 {
        'C'
    } else {
        'D'
    }
}

fn main() {
    println!("luas    = {}", luas_persegi(2.5));

    let (hasil, sisa) = bagi(17, 5);
    println!("17 / 5  = {hasil} sisa {sisa}");

    for n in [92, 78, 64, 40] {
        println!("{n:3} -> {}", grade(n));
    }

    let kuadrat = { let a = 7; a * a };
    println!("blok    = {kuadrat}");
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  luas    = 6.25",
                    "  17 / 5  = 3 sisa 2",
                    "   92 -> A",
                    "   78 -> B",
                    "   64 -> C",
                    "   40 -> D",
                    "  blok    = 49",
                    "",
                    "Fungsi `bagi` mengembalikan tuple, yaitu beberapa nilai yang dibungkus",
                    "jadi satu, ditulis dalam kurung: `(a / b, a % b)`. Ini cara paling",
                    "ringkas kalau fungsi perlu ngasih lebih dari satu hasil.",
                    "",
                    "Cara menerimanya, `let (hasil, sisa) = ...`, namanya destructuring,",
                    "artinya membongkar isinya langsung ke beberapa variabel. Pola yang sama",
                    "nanti dipakai juga untuk struct dan enum.",
                    "",
                    "Coba perhatikan fungsi `grade`. Nggak ada satu cabang pun yang diakhiri",
                    "titik koma, dan seluruh rantai if-else itu jadi nilai kembalian fungsi.",
                    "Kalau salah satu cabang dikasih titik koma, cabang itu menghasilkan",
                    "`()`, sementara cabang lain menghasilkan char. Compiler lalu bilang",
                    "cabang-cabangnya punya tipe yang beda. Pesannya kedengaran aneh, tapi",
                    "artinya persis begitu.",
                    "",
                    "Format angka di println!:",
                    "  {n:3}       rata kanan selebar 3",
                    "  {n:<3}      rata kiri",
                    "  {n:^3}      rata tengah",
                    "  {n:03}      diisi nol di depan",
                    "  {n:.2}      dua desimal",
                    "  {n:8.2}     lebar 8, dua desimal",
                    "  {n:+}       selalu tampilkan tanda",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aturan tarif di aplikasi sungguhan, seperti biaya parkir mal, ongkos",
                    "kirim, atau denda telat bayar, biasanya dibungkus jadi satu fungsi. Layar",
                    "kasir, struk, dan laporan memanggil fungsi yang sama. Kalau tarifnya",
                    "berubah, cukup satu tempat yang disunting.",
                    "",
                    "Kasus kecil: parkir motor di sebuah mal tarifnya Rp 5.000 untuk dua jam",
                    "pertama, lalu Rp 2.000 untuk tiap jam berikutnya. Berapa biaya untuk 1, 2,",
                    "3, dan 5 jam?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan masukan dan keluaran: lama parkir dalam jam, hasilnya",
                    "     rupiah. Itu jadi tanda tangan fungsinya:",
                    "     `fn biaya_parkir(jam: u32) -> u32`.",
                    "  2. Pecah aturannya jadi dua keadaan: sampai 2 jam, dan lebih dari 2 jam.",
                    "  3. Karena `if` adalah ekspresi, dua keadaan itu langsung jadi nilai",
                    "     kembalian, tanpa titik koma di ujung cabangnya:",
                    "      fn biaya_parkir(jam: u32) -> u32 {",
                    "          if jam <= 2 { 5_000 } else { 5_000 + (jam - 2) * 2_000 }",
                    "      }",
                    "  4. Cek dengan angka di batas: 1 dan 2 jam harus Rp 5.000, 3 jam",
                    "     Rp 7.000, dan 5 jam Rp 11.000. Perhatikan juga `jam - 2`. Tipe u32",
                    "     nggak bisa negatif, dan cabang `jam <= 2` yang menjaga supaya 0 atau",
                    "     1 jam nggak pernah sampai ke pengurangan itu.",
                    "",
                    "Jebakan: menulis `5_000;` dengan titik koma bikin cabang itu menghasilkan",
                    "`()`, dan compiler menolak dengan pesan 'mismatched types'.",
                ]
            },
        ],
    },
    {
        "title": "4. Percabangan & Perulangan",
        "sections": [
            {
                "body": [
                    "Aturan if di Rust:",
                    "  - Kondisinya wajib bertipe bool. Nulis `if x` dengan x berupa angka",
                    "    bikin error kompilasi. Di C, angka bukan nol dianggap benar; di",
                    "    Rust nggak.",
                    "  - Kondisinya nggak dikurung.",
                    "  - Kurung kurawal wajib ada, walaupun isinya cuma satu baris.",
                    "",
                    "  if nilai >= 75 {",
                    "      println!(\"lulus\");",
                    "  } else {",
                    "      println!(\"ulang\");",
                    "  }",
                    "",
                    "Ada tiga cara mengulang:",
                    "",
                    "  loop      ulang selamanya sampai break",
                    "  while     ulang selama syarat benar",
                    "  for       telusuri sebuah iterator",
                    "",
                    "Iterator itu sesuatu yang isinya bisa diambil satu per satu, misalnya",
                    "rentang angka atau isi sebuah vec.",
                    "",
                    "  loop {",
                    "      hitung += 1;",
                    "      if hitung == 5 { break; }",
                    "  }",
                    "",
                    "`loop` bisa mengembalikan nilai lewat break. Kebanyakan bahasa lain",
                    "nggak punya fitur ini:",
                    "",
                    "  let hasil = loop {",
                    "      n += 1;",
                    "      if n * n > 100 { break n; }",
                    "  };",
                    "",
                    "for yang paling sering dipakai, dan bentuknya selalu `for x in",
                    "sesuatu`:",
                    "",
                    "  for i in 0..5      0,1,2,3,4      (akhir eksklusif)",
                    "  for i in 0..=5     0,1,2,3,4,5    (akhir inklusif)",
                    "  for i in (0..5).rev()             4,3,2,1,0",
                    "  for i in (0..10).step_by(2)       0,2,4,6,8",
                    "  for x in &vec                     pinjam tiap elemen",
                    "  for x in &mut vec                 pinjam dan boleh ubah",
                    "  for x in vec                      PINDAHKAN kepemilikan",
                    "  for (i, x) in vec.iter().enumerate()",
                    "",
                    "Perhatikan baris `for x in vec` tanpa tanda &. Perulangan itu mengambil",
                    "vec-nya, dan sesudah perulangan selesai, vec nggak bisa dipakai lagi.",
                    "Penjelasan lengkapnya ada di materi \"Ownership: Aturan Inti Rust\".",
                    "",
                    "Kalau perulangannya bersarang (ada perulangan di dalam perulangan),",
                    "kamu bisa kasih label untuk keluar dari yang luar sekaligus:",
                    "",
                    "  'luar: for i in 0..5 {",
                    "      for j in 0..5 {",
                    "          if i * j > 6 { break 'luar; }",
                    "      }",
                    "  }",
                ]
            },
            {
                "heading": "Perulangan dalam praktik",
                "code": """fn main() {
    // Tabel perkalian
    for b in 1..=3 {
        for k in 1..=5 {
            print!("{:4}", b * k);
        }
        println!();
    }

    // loop yang mengembalikan nilai
    let mut n = 0;
    let pertama = loop {
        n += 1;
        if n * n > 100 {
            break n;
        }
    };
    println!("kuadrat pertama > 100 dimiliki {pertama}");

    // while dengan syarat
    let mut sisa = 27;
    let mut langkah = 0;
    while sisa != 1 {
        sisa = if sisa % 2 == 0 { sisa / 2 } else { 3 * sisa + 1 };
        langkah += 1;
    }
    println!("27 sampai 1 dalam {langkah} langkah");

    // Label untuk keluar dari dua perulangan
    let mut ketemu = (0, 0);
    'luar: for i in 1..20 {
        for j in 1..20 {
            if i * j == 143 {
                ketemu = (i, j);
                break 'luar;
            }
        }
    }
    println!("143 = {} x {}", ketemu.0, ketemu.1);
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "     1   2   3   4   5",
                    "     2   4   6   8  10",
                    "     3   6   9  12  15",
                    "  kuadrat pertama > 100 dimiliki 11",
                    "  27 sampai 1 dalam 111 langkah",
                    "  143 = 11 x 13",
                    "",
                    "`print!` tanpa `ln` mencetak tanpa pindah baris, sama kayak di bahasa",
                    "lain. `println!()` yang kosong cuma pindah baris.",
                    "",
                    "Jebakan: keluaran `print!` ke terminal ditampung dulu (buffered), dan",
                    "tampungannya baru dikirim ke layar waktu ada baris baru. Kalau kamu",
                    "mencetak pertanyaan pakai `print!` lalu langsung membaca ketikan",
                    "pengguna, pertanyaannya bisa belum muncul. Cara memperbaikinya:",
                    "",
                    "  use std::io::Write;",
                    "  io::stdout().flush().unwrap();",
                    "",
                    "Rentang `1..20` di contoh terakhir nggak memuat angka 20. Kalau kamu",
                    "lupa ini, pencarian yang harusnya ketemu bisa selesai tanpa hasil, dan",
                    "nggak ada error apa pun yang muncul.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Perulangan dengan syarat berhenti dipakai di simulasi cicilan, tabungan,",
                    "dan target penjualan: ulangi bulan demi bulan sampai angkanya tercapai.",
                    "Pertanyaan \"berapa bulan lagi tabunganku cukup?\" bisa dijawab dengan cara",
                    "ini, terutama kalau setorannya nggak tetap.",
                    "",
                    "Kasus kecil: Dina mau beli laptop Rp 4.200.000. Bulan pertama ia",
                    "menabung Rp 300.000, dan setorannya naik Rp 50.000 tiap bulan. Di bulan",
                    "ke berapa uangnya cukup?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami kenapa pembagian biasa nggak cukup: setorannya berubah tiap",
                    "     bulan, jadi totalnya harus dihitung bulan demi bulan.",
                    "  2. Siapkan tiga variabel yang berubah: total tabungan, setoran bulan",
                    "     ini, dan nomor bulan. Ketiganya butuh `mut`. Nilai awalnya: total 0,",
                    "     setoran 300_000, dan bulan 0.",
                    "  3. Pakai `while` dengan syarat \"belum cukup\":",
                    "      while total < 4_200_000 {",
                    "          total += setoran;",
                    "          setoran += 50_000;",
                    "          bulan += 1;",
                    "      }",
                    "  4. Hasilnya bulan ke-9, dengan total Rp 4.500.000. Periksa syaratnya:",
                    "     `<` berhenti tepat saat total sama dengan harga laptop. Kalau",
                    "     tertulis `<=` dan totalnya kebetulan pas Rp 4.200.000, Dina disuruh",
                    "     menabung sebulan lagi padahal uangnya udah cukup.",
                    "",
                    "Jebakan: kalau setoran awalnya 0 dan kenaikannya juga 0, syarat",
                    "`total < 4_200_000` nggak pernah salah, dan programnya jalan terus tanpa",
                    "berhenti.",
                ]
            },
        ],
    },
    {
        "title": "5. Ownership: Aturan Inti Rust",
        "sections": [
            {
                "body": [
                    "Ownership artinya kepemilikan: setiap nilai di memori punya satu",
                    "variabel yang memilikinya. Gagasan ini yang bikin Rust beda dari bahasa",
                    "lain. Rust nggak pakai garbage collector, tapi kamu juga nggak perlu",
                    "melepas memori sendiri. Ownership yang mengurusnya.",
                    "",
                    "Aturannya cuma tiga:",
                    "  1. Setiap nilai punya satu variabel pemilik.",
                    "  2. Pada satu waktu, pemiliknya cuma boleh satu.",
                    "  3. Begitu pemiliknya keluar dari scope, nilainya dilepas.",
                    "",
                    "Scope itu wilayah tempat sebuah variabel berlaku, biasanya dari baris",
                    "dia dibuat sampai kurung kurawal penutup bloknya.",
                    "",
                    "Berkat aturan ketiga, nggak ada yang perlu manggil free() untuk melepas",
                    "memori, jadi nggak ada juga yang bisa lupa.",
                    "",
                    "Move: memberikan nilai ke variabel lain memindahkan kepemilikannya.",
                    "",
                    "  let a = String::from(\"halo\");",
                    "  let b = a;              kepemilikan pindah ke b",
                    "  println!(\"{a}\");        ERROR: value borrowed after move",
                    "",
                    "Di Java atau Python, baris kedua bikin a dan b nunjuk ke objek yang",
                    "sama. Di C++, seluruh isinya disalin. Rust ambil jalan ketiga: a nggak",
                    "berlaku lagi, dan compiler menolak setiap pemakaian a sesudahnya.",
                    "",
                    "Alasannya begini. Kalau a dan b sama-sama jadi pemilik, dua-duanya bakal",
                    "melepas memori yang sama waktu scope selesai. Itu namanya double free,",
                    "salah satu bug paling berbahaya di C++.",
                    "",
                    "Copy: tipe kecil yang ukurannya tetap disalin, nggak dipindah.",
                    "",
                    "  let a = 5;",
                    "  let b = a;",
                    "  println!(\"{a}\");        baik-baik saja",
                    "",
                    "Yang termasuk Copy: semua tipe angka, bool, char, dan tuple yang",
                    "isinya Copy semua. Patokan gampangnya: kalau ukurannya udah diketahui",
                    "waktu kompilasi dan seluruh isinya tinggal di stack, tipe itu Copy.",
                    "",
                    "Stack dan heap itu dua tempat menyimpan data di memori. Stack untuk",
                    "data yang ukurannya tetap dan cepat diambil. Heap untuk data yang",
                    "ukurannya bisa berubah, misalnya teks yang terus bertambah.",
                    "",
                    "String dan Vec nggak termasuk Copy, karena isinya ada di heap.",
                    "Menyalinnya berarti minta memori baru, dan itu terlalu mahal untuk",
                    "dilakukan tanpa kamu sadari.",
                ]
            },
            {
                "heading": "Melihat move terjadi",
                "code": """fn ambil_alih(s: String) -> usize {
    s.len()
}   // s dilepas di sini

fn pinjam(s: &String) -> usize {
    s.len()
}   // s cuma dipinjam, tidak dilepas

fn main() {
    // Copy: angka disalin
    let a = 5;
    let b = a;
    println!("copy   : a={a} b={b}");

    // Move: String berpindah
    let s1 = String::from("halo");
    let s2 = s1.clone();          // clone = salinan penuh, s1 tetap sah
    println!("clone  : s1={s1} s2={s2}");

    let s3 = String::from("dunia");
    let panjang = ambil_alih(s3);  // s3 PINDAH ke dalam fungsi
    println!("pindah : panjang={panjang}");
    // println!("{s3}");           <- ini tidak akan dikompilasi

    let s4 = String::from("rust");
    let panjang = pinjam(&s4);     // s4 cuma dipinjam
    println!("pinjam : {s4} panjangnya {panjang}");

    // Scope: nilai dilepas di akhir blok
    {
        let sementara = String::from("hidup sebentar");
        println!("blok   : {sementara}");
    }   // sementara dilepas persis di sini
    println!("selesai");
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  copy   : a=5 b=5",
                    "  clone  : s1=halo s2=halo",
                    "  pindah : panjang=5",
                    "  pinjam : rust panjangnya 4",
                    "  blok   : hidup sebentar",
                    "  selesai",
                    "",
                    "Ada tiga cara ngasih nilai ke fungsi. Kamu bakal milih salah satunya",
                    "setiap kali nulis fungsi:",
                    "",
                    "  fn f(s: String)      AMBIL. Pemanggil kehilangan s.",
                    "                       Dipakai kalau fungsi memang jadi",
                    "                       pemilik barunya.",
                    "  fn f(s: &String)     PINJAM baca. Pemanggil tetap",
                    "                       memilikinya.",
                    "  fn f(s: &mut String) PINJAM ubah. Boleh menyunting,",
                    "                       pemanggil tetap pemiliknya.",
                    "",
                    "Dari ketiganya, pinjam baca yang paling sering kamu pakai. Untuk teks,",
                    "bentuk yang paling sering benar adalah `fn f(s: &str)`, bukan",
                    "`&String`, karena `&str` bisa menerima `&String` maupun literal seperti",
                    "\"halo\". Apa itu `&str` dibahas di materi Slice & String. Untuk",
                    "sekarang, pegang dulu idenya: kalau fungsi cuma perlu membaca, pinjam.",
                    "",
                    "`clone()` bikin salinan penuh. Dia selalu berhasil, tapi selalu minta",
                    "memori baru. Kalau kodemu penuh clone di mana-mana, biasanya itu tanda",
                    "soal kepemilikannya belum dipikirkan. Nggak salah, tapi layak dicek",
                    "ulang sesudah kodenya jalan.",
                    "",
                    "Pesan error 'borrow of moved value' itu bukan hukuman. Artinya ada dua",
                    "tempat di kodemu yang sama-sama merasa memiliki satu nilai. Di C++,",
                    "masalah seperti itu baru ketahuan waktu program udah dipakai orang.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aturan kepemilikan paling terasa di aplikasi yang mengoper data antar",
                    "bagian, misalnya kasir yang mengirim daftar belanja ke fungsi cetak struk",
                    "lalu masih mau menghitung jumlah barangnya. Di Rust, tiap fungsi yang",
                    "kamu tulis harus memutuskan: ia memiliki data itu, atau cuma membacanya.",
                    "",
                    "Kasus kecil: fungsi `cetak_struk(daftar: Vec<String>)` mencetak isi",
                    "daftar belanja. Sesudah memanggilnya, kode kasir menulis `daftar.len()`",
                    "untuk mencetak jumlah item, dan compiler menolak dengan pesan 'borrow of",
                    "moved value: `daftar`'.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca pesannya sampai habis. Compiler menunjuk dua tempat: baris",
                    "     `cetak_struk(daftar)`, tempat daftar pindah, dan baris `daftar.len()`",
                    "     yang memakainya sesudah pindah.",
                    "  2. Tanya dirimu: perlukah fungsi cetak memiliki daftarnya? Ia cuma",
                    "     membaca isinya, jadi parameternya cukup pinjaman:",
                    "      fn cetak_struk(daftar: &Vec<String>) {",
                    "          for item in daftar {",
                    "              println!(\"- {item}\");",
                    "          }",
                    "      }",
                    "  3. Ubah pemanggilannya jadi `cetak_struk(&daftar)`. Sekarang",
                    "     `daftar.len()` jalan, dan untuk daftar beras, minyak, dan gula",
                    "     hasilnya 3.",
                    "  4. Pertimbangkan jalan lain. `cetak_struk(daftar.clone())` juga lolos,",
                    "     tapi menyalin seluruh daftar cuma untuk dibaca. Parameter",
                    "     `Vec<String>` cocok untuk fungsi yang memang menyimpan datanya,",
                    "     misalnya fungsi yang memasukkan transaksi ke arsip.",
                ]
            },
        ],
    },
    {
        "title": "6. Reference & Borrowing",
        "sections": [
            {
                "body": [
                    "Borrowing artinya meminjam: memakai sebuah nilai tanpa mengambil",
                    "kepemilikannya. Tandanya `&`. Hasil pinjamannya disebut reference",
                    "(referensi), semacam penunjuk ke nilai milik orang lain.",
                    "",
                    "  let s = String::from(\"halo\");",
                    "  let r = &s;             r meminjam s",
                    "  println!(\"{s} {r}\");    keduanya sah",
                    "",
                    "Aturan meminjam ini yang paling sering dilanggar pemula. Pada satu",
                    "waktu, kamu cuma boleh punya salah satu dari dua ini:",
                    "  - berapa pun banyaknya peminjam yang cuma membaca (&T), atau",
                    "  - tepat satu peminjam yang boleh mengubah (&mut T).",
                    "",
                    "Dua-duanya sekaligus nggak boleh.",
                    "",
                    "Alasannya: kalau ada yang membaca sementara yang lain mengubah,",
                    "pembacanya bisa dapat data yang setengah jadi. Itu definisi data race.",
                    "Rust mencegahnya waktu kompilasi, dan aturan ini berlaku di mana aja,",
                    "termasuk di dalam satu fungsi tanpa thread sama sekali.",
                    "",
                    "  let mut v = vec![1, 2, 3];",
                    "  let a = &v;           pinjam baca",
                    "  let b = &v;           pinjam baca lagi -- boleh",
                    "  let c = &mut v;       ERROR: sudah ada peminjam baca",
                    "",
                    "Aturan ini lebih longgar daripada kedengarannya, berkat fitur NLL",
                    "(Non-Lexical Lifetimes). Sebuah pinjaman berakhir di tempat terakhir",
                    "dia dipakai, nggak harus nunggu akhir blok. Jadi kode ini sah:",
                    "",
                    "  let a = &v;",
                    "  println!(\"{a:?}\");    pinjaman a berakhir di sini",
                    "  let c = &mut v;       boleh sekarang",
                    "",
                    "Dangling reference juga nggak bisa terjadi. Dangling reference itu",
                    "referensi yang nunjuk ke data yang udah dilepas:",
                    "",
                    "  fn buat() -> &String {",
                    "      let s = String::from(\"halo\");",
                    "      &s          ERROR: s mati saat fungsi selesai",
                    "  }",
                    "",
                    "Di C, kode seperti ini lolos kompilasi tanpa keluhan dan menghasilkan",
                    "pointer ke memori yang udah dilepas. Di Rust, compiler menolaknya dan",
                    "menyarankan kamu mengembalikan String-nya langsung.",
                ]
            },
            {
                "heading": "Meminjam untuk membaca dan untuk mengubah",
                "code": """fn total(angka: &Vec<i32>) -> i32 {
    let mut t = 0;
    for n in angka {
        t += n;
    }
    t
}

fn tambah_satu(angka: &mut Vec<i32>) {
    for n in angka.iter_mut() {
        *n += 1;              // * untuk menyentuh nilai di balik referensi
    }
}

fn main() {
    let mut data = vec![10, 20, 30];

    // Banyak peminjam BACA sekaligus: boleh
    let a = &data;
    let b = &data;
    println!("a={a:?} b={b:?} total={}", total(&data));

    // Peminjam UBAH: harus sendirian
    tambah_satu(&mut data);
    println!("sesudah diubah: {data:?}");

    // Referensi ke elemen
    let pertama = &data[0];
    println!("elemen pertama: {pertama}");

    // Tukar dua nilai lewat referensi
    let mut x = 3;
    let mut y = 8;
    std::mem::swap(&mut x, &mut y);
    println!("x={x} y={y}");
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  a=[10, 20, 30] b=[10, 20, 30] total=60",
                    "  sesudah diubah: [11, 21, 31]",
                    "  elemen pertama: 11",
                    "  x=8 y=3",
                    "",
                    "Tanda bintang `*` disebut dereference. Artinya \"ambil nilai yang",
                    "ditunjuk referensi ini\". Di `*n += 1`, kalau bintangnya hilang, kamu",
                    "mencoba menambah satu ke referensinya, padahal yang mau ditambah itu",
                    "isinya.",
                    "",
                    "Kabar baiknya, waktu kamu memanggil method, Rust melakukan dereference",
                    "sendiri. `s.len()` tetap jalan, entah s itu String, &String, atau",
                    "&&String. Fitur ini namanya auto-deref, dan karena dia, referensi",
                    "jarang terasa merepotkan sehari-hari.",
                    "",
                    "Pesan error yang paling sering muncul di awal, dan cara membacanya:",
                    "",
                    "  'cannot borrow as mutable more than once'",
                    "    -> ada dua &mut hidup bersamaan. Persempit scope",
                    "       salah satunya.",
                    "",
                    "  'cannot borrow as mutable because also borrowed as",
                    "   immutable'",
                    "    -> masih ada & yang dipakai SESUDAH titik ini.",
                    "       Pindahkan pemakaiannya ke atas.",
                    "",
                    "  'does not live long enough'",
                    "    -> referensinya hidup lebih lama daripada datanya.",
                    "       Biasanya jawabannya: kembalikan nilainya, jangan",
                    "       referensinya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Fitur flash sale di toko online punya dua jenis pekerjaan: satu fungsi",
                    "memotong harga semua barang di keranjang, fungsi lain cuma membaca untuk",
                    "menghitung total. Memisahkan keduanya lewat `&mut` dan `&` bikin jelas",
                    "fungsi mana yang boleh mengubah data.",
                    "",
                    "Kasus kecil: keranjang berisi tiga harga, Rp 50.000, Rp 120.000, dan",
                    "Rp 35.000. Semuanya dapat diskon 10%, lalu totalnya ditampilkan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan pekerjaannya. `diskon` mengubah isi keranjang, jadi",
                    "     menerima `&mut Vec<i64>`. `total` cuma membaca, jadi menerima",
                    "     `&Vec<i64>`.",
                    "  2. Ubah tiap harga lewat `iter_mut()` dan tanda bintang, karena yang",
                    "     diubah nilai di balik referensinya:",
                    "      fn diskon(harga: &mut Vec<i64>, persen: i64) {",
                    "          for h in harga.iter_mut() {",
                    "              *h = *h * (100 - persen) / 100;",
                    "          }",
                    "      }",
                    "  3. Panggil `diskon(&mut keranjang, 10)` dulu, baru `total(&keranjang)`.",
                    "     Hasilnya [45000, 108000, 31500] dengan total 184500.",
                    "  4. Perhatikan urutan kali dan bagi. Untuk harga Rp 12.345,",
                    "     `*h / 100 * 90` menghasilkan 11070, karena pembagian bulat membuang",
                    "     sisanya lebih dulu. `*h * 90 / 100` menghasilkan 11110.",
                    "",
                    "Jebakan: kalau kamu menyimpan `let t = &keranjang;`, memanggil `diskon`,",
                    "lalu memakai t sesudahnya, compiler menolak dengan pesan 'cannot borrow",
                    "`keranjang` as mutable because it is also borrowed as immutable'.",
                ]
            },
        ],
    },
    {
        "title": "7. Slice & String",
        "sections": [
            {
                "body": [
                    "Slice itu referensi ke sebagian isi sebuah koleksi, misalnya elemen",
                    "kedua sampai keempat dari sebuah vec. Slice nggak memiliki datanya dan",
                    "nggak menyalin apa pun.",
                    "",
                    "  let v = vec![1, 2, 3, 4, 5];",
                    "  let potong = &v[1..4];       [2, 3, 4]",
                    "  let awal   = &v[..2];        [1, 2]",
                    "  let akhir  = &v[3..];        [4, 5]",
                    "  let semua  = &v[..];         seluruhnya",
                    "",
                    "Tipenya `&[i32]`, dibaca \"slice dari i32\".",
                    "",
                    "Rust punya dua tipe teks. Membedakan keduanya biasanya jadi rintangan",
                    "pertama:",
                    "",
                    "  String   MEMILIKI teksnya, tersimpan di heap, bisa",
                    "           tumbuh. Setara StringBuilder.",
                    "  &str     PINJAMAN ke teks milik orang lain. Ukurannya",
                    "           tetap. Disebut 'string slice'.",
                    "",
                    "String mirip StringBuilder di Java: isinya bisa ditambah. &str cuma",
                    "pinjaman, jadi isinya nggak bisa kamu ubah.",
                    "",
                    "  let a: &str = \"halo\";              literal SELALU &str",
                    "  let b: String = String::from(\"halo\");",
                    "  let c: String = \"halo\".to_string();",
                    "  let d: &str = &b;                   pinjam dari String",
                    "  let e: &str = &b[0..2];             pinjam sebagian",
                    "",
                    "Patokan praktis yang menyelesaikan sebagian besar kebingungan:",
                    "  - Untuk parameter fungsi, pakai &str. Parameter ini bisa menerima",
                    "    dua-duanya.",
                    "  - Untuk field struct dan nilai kembalian, pakai String.",
                    "",
                    "  fn sapa(nama: &str) { ... }",
                    "  sapa(\"Andi\");        literal, langsung cocok",
                    "  sapa(&nama_string);  String otomatis jadi &str",
                    "",
                    "Hati-hati dengan UTF-8. String di Rust disimpan dalam format UTF-8, dan",
                    "di format itu satu karakter bisa makan 1 sampai 4 byte. Akibatnya:",
                    "  - `s.len()` ngasih jumlah byte, belum tentu jumlah huruf.",
                    "  - `s[0]` nggak ada. Mengambil satu karakter pakai indeks dilarang.",
                    "  - `&s[0..2]` bikin panic kalau potongannya jatuh di tengah sebuah",
                    "    karakter.",
                    "",
                    "Yang benar: `s.chars().count()` untuk jumlah huruf, dan",
                    "`s.chars().nth(0)` untuk huruf pertama.",
                ]
            },
            {
                "heading": "Mengolah teks",
                "code": """fn kata_terpanjang(kalimat: &str) -> &str {
    let mut terbaik = "";
    for kata in kalimat.split_whitespace() {
        if kata.len() > terbaik.len() {
            terbaik = kata;
        }
    }
    terbaik
}

fn main() {
    let kalimat = "Rust membuat kode sistem jadi aman";

    println!("asli      : {kalimat}");
    println!("byte      : {}", kalimat.len());
    println!("huruf     : {}", kalimat.chars().count());
    println!("kata      : {}", kalimat.split_whitespace().count());
    println!("terpanjang: {}", kata_terpanjang(kalimat));
    println!("besar     : {}", kalimat.to_uppercase());
    println!("ganti     : {}", kalimat.replace("aman", "cepat"));
    println!("mulai     : {}", kalimat.starts_with("Rust"));
    println!("posisi    : {:?}", kalimat.find("kode"));
    println!("balik     : {}", kalimat.chars().rev().collect::<String>());

    // Membangun String secara bertahap
    let mut sapaan = String::new();
    sapaan.push_str("Halo");
    sapaan.push(',');
    sapaan.push_str(" dunia");
    sapaan += "!";
    println!("dibangun  : {sapaan}");

    // Slice pada vektor
    let angka = vec![10, 20, 30, 40, 50];
    println!("tengah    : {:?}", &angka[1..4]);
    println!("dua akhir : {:?}", &angka[angka.len() - 2..]);
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  asli      : Rust membuat kode sistem jadi aman",
                    "  byte      : 34",
                    "  huruf     : 34",
                    "  kata      : 6",
                    "  terpanjang: membuat",
                    "  besar     : RUST MEMBUAT KODE SISTEM JADI AMAN",
                    "  ganti     : Rust membuat kode sistem jadi cepat",
                    "  mulai     : true",
                    "  posisi    : Some(13)",
                    "  balik     : nama idaj metsis edok taubmem tsuR",
                    "  dibangun  : Halo, dunia!",
                    "  tengah    : [20, 30, 40]",
                    "  dua akhir : [40, 50]",
                    "",
                    "Jumlah byte dan huruf sama-sama 34, karena semua hurufnya ASCII (satu",
                    "huruf satu byte). Coba ganti kalimatnya dengan yang ada huruf beraksen",
                    "atau emoji. Dua angka itu bakal beda, dan karena itulah Rust melarang",
                    "`s[0]`.",
                    "",
                    "`find` mengembalikan `Option<usize>`: Some(posisi) kalau ketemu, None",
                    "kalau nggak. Rust nggak pakai -1 untuk \"nggak ada\". Masalahnya, -1 itu",
                    "angka yang sah, jadi gampang kepakai tanpa dicek dulu. Option memaksa",
                    "kamu ngecek. Option dibahas lengkap di materi \"Enum & Option\".",
                    "",
                    "`collect::<String>()` pakai tanda `::<>` yang dijuluki turbofish. Tanda",
                    "ini ngasih tahu tipe hasil yang kamu mau. Di sini dia perlu, karena",
                    "`collect` bisa menghasilkan banyak tipe, dan compiler nggak punya",
                    "petunjuk lain.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Formulir pendaftaran di aplikasi toko online, ojek online, atau klinik",
                    "menerima nomor HP dalam macam-macam bentuk: pakai strip, pakai spasi,",
                    "diawali angka 0. Sebelum disimpan atau dipakai untuk tautan WhatsApp,",
                    "nomor itu dirapikan dulu dengan method string.",
                    "",
                    "Kasus kecil: tautan `wa.me/` butuh nomor format internasional tanpa",
                    "tanda plus, misalnya 6281234567890. Pengguna mengetik \"0812-3456-7890\"",
                    "atau \"0812 3456 7890\". Ubah keduanya jadi bentuk yang sama.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya teks pinjaman, jadi parameternya `&str`. Keluarannya teks",
                    "     baru milik pemanggil, jadi kembaliannya `String`.",
                    "  2. Buang pengganggunya dulu:",
                    "     `let bersih = nomor.replace(\"-\", \"\").replace(\" \", \"\");`",
                    "  3. Kalau diawali \"0\", ganti angka itu dengan \"62\". Potongan",
                    "     `&bersih[1..]` aman di sini, karena angka 0 cuma satu byte:",
                    "      if !bersih.starts_with(\"0\") {",
                    "          return bersih;",
                    "      }",
                    "      let mut hasil = String::from(\"62\");",
                    "      hasil.push_str(&bersih[1..]);",
                    "      hasil",
                    "     Dua masukan tadi sama-sama jadi 6281234567890.",
                    "  4. Uji kasus pinggir. Nomor yang udah berbentuk 6281... lolos apa",
                    "     adanya. Teks kosong juga aman, karena `starts_with(\"0\")` gagal lebih",
                    "     dulu. Tanpa pemeriksaan itu, `&bersih[1..]` pada teks kosong bikin",
                    "     panic.",
                ]
            },
        ],
    },
    {
        "title": "8. Struct",
        "sections": [
            {
                "body": [
                    "Struct itu cara mengelompokkan beberapa nilai yang masing-masing punya",
                    "nama jadi satu tipe baru. Misalnya data seorang murid: nama, nilai, dan",
                    "status aktif.",
                    "",
                    "  struct Murid {",
                    "      nama: String,",
                    "      nilai: u32,",
                    "      aktif: bool,",
                    "  }",
                    "",
                    "Tiap nilai di dalamnya disebut field. Cara membuatnya:",
                    "  let m = Murid {",
                    "      nama: String::from(\"Andi\"),",
                    "      nilai: 88,",
                    "      aktif: true,",
                    "  };",
                    "",
                    "Semua field wajib diisi. Nggak ada nilai bawaan, kecuali kamu",
                    "mengimplementasi trait Default.",
                    "",
                    "Kalau nama variabel sama dengan nama field, kamu boleh nyingkat:",
                    "  fn buat(nama: String, nilai: u32) -> Murid {",
                    "      Murid { nama, nilai, aktif: true }",
                    "  }",
                    "",
                    "Kamu juga bisa nyalin sebagian isi dari struct lain:",
                    "  let m2 = Murid { nilai: 90, ..m };",
                    "",
                    "Hati-hati: `..m` memindahkan field yang nggak Copy dari m (di sini",
                    "nama). Sesudahnya, m nggak bisa dipakai lagi secara utuh.",
                    "",
                    "Ada tiga jenis struct:",
                    "",
                    "  BIASA        struct Titik { x: f64, y: f64 }",
                    "  TUPLE        struct Warna(u8, u8, u8);",
                    "               diakses dengan .0 .1 .2",
                    "  UNIT         struct Penanda;",
                    "               tanpa data, berguna untuk trait",
                    "",
                    "Method, yaitu fungsi milik sebuah tipe, ditulis di blok `impl` yang",
                    "terpisah dari definisi datanya. Karena terpisah, satu struct boleh punya",
                    "beberapa blok impl, termasuk blok yang menambahkan trait dari luar.",
                ]
            },
            {
                "heading": "Struct dengan method",
                "code": """#[derive(Debug, Clone)]
struct Rekening {
    pemilik: String,
    saldo: i64,
}

impl Rekening {
    // Fungsi terkait (associated function): TANPA self.
    // Ini yang biasa disebut "constructor" di bahasa lain.
    fn baru(pemilik: &str, saldo: i64) -> Self {
        Self {
            pemilik: pemilik.to_string(),
            saldo,
        }
    }

    // Method: parameter pertama self. &self = meminjam untuk MEMBACA.
    fn ringkas(&self) -> String {
        format!("{:<8}{:>10}", self.pemilik, self.saldo)
    }

    // &mut self = meminjam untuk MENGUBAH
    fn setor(&mut self, jumlah: i64) {
        self.saldo += jumlah;
    }

    fn tarik(&mut self, jumlah: i64) -> bool {
        if jumlah <= 0 || jumlah > self.saldo {
            return false;
        }
        self.saldo -= jumlah;
        true
    }
}

fn main() {
    let mut a = Rekening::baru("Andi", 500_000);
    let mut b = Rekening::baru("Budi", 0);

    a.setor(250_000);
    println!("tarik 900rb dari Andi: {}", a.tarik(900_000));
    println!("tarik 300rb dari Andi: {}", a.tarik(300_000));
    b.setor(100_000);

    println!("{}", a.ringkas());
    println!("{}", b.ringkas());
    println!("{a:?}");
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tarik 900rb dari Andi: false",
                    "  tarik 300rb dari Andi: true",
                    "  Andi        450000",
                    "  Budi        100000",
                    "  Rekening { pemilik: \"Andi\", saldo: 450000 }",
                    "",
                    "Parameter pertama sebuah method punya empat kemungkinan bentuk, dan",
                    "pilihanmu menentukan apa yang boleh dilakukan method itu:",
                    "",
                    "  &self       baca saja. Yang paling sering benar.",
                    "  &mut self   boleh mengubah objeknya.",
                    "  self        MENGAMBIL objeknya; pemanggil kehilangannya.",
                    "              Dipakai untuk method yang mengubah bentuk,",
                    "              misalnya `into_bytes()`.",
                    "  (tanpa self) fungsi terkait, dipanggil dengan ::",
                    "",
                    "`Self` dengan S besar itu nama lain untuk tipe yang lagi kamu tulis",
                    "impl-nya. Kalau kamu nulis `Self` dan bukan `Rekening`, nanti waktu",
                    "nama struct-nya diganti, isi impl nggak perlu ikut diubah.",
                    "",
                    "`#[derive(Debug)]` nyuruh compiler nulis sendiri kode untuk mencetak",
                    "struct pakai `{:?}`. Tanpa baris itu, `println!(\"{a:?}\")` jadi error.",
                    "Derive lain yang sering dipakai:",
                    "",
                    "  Debug        bisa dicetak dengan {:?}",
                    "  Clone        punya method .clone()",
                    "  Copy         disalin, bukan dipindah (butuh Clone)",
                    "  PartialEq    bisa dibandingkan dengan == dan !=",
                    "  Eq           kesetaraan penuh (butuh PartialEq)",
                    "  PartialOrd   bisa dibandingkan dengan < dan >",
                    "  Ord          urutan total (butuh Eq + PartialOrd)",
                    "  Hash         bisa jadi kunci HashMap",
                    "  Default      punya Titik::default()",
                    "",
                    "Satu baris derive menggantikan puluhan baris kode yang gampang salah",
                    "kalau ditulis tangan.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data kartu member minimarket cocok jadi struct: nama dan poin selalu",
                    "berjalan bersama, dan aturan menambah atau menukar poin ditulis sebagai",
                    "method. Layar kasir dan aplikasi HP cukup memanggil method itu, tanpa",
                    "menghitung poin sendiri-sendiri.",
                    "",
                    "Kasus kecil: tiap kelipatan Rp 10.000 dalam satu struk dapat 1 poin. Sari",
                    "belanja dua kali, Rp 57.500 dan Rp 42.500. Berapa poinnya?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kumpulkan data yang selalu bareng jadi field: `nama: String` dan",
                    "     `poin: u32`.",
                    "  2. Tentukan method dan jenis `self`-nya. Menambah poin mengubah data,",
                    "     jadi `&mut self`. Menampilkan ringkasan cuma membaca, jadi `&self`:",
                    "      impl Member {",
                    "          fn belanja(&mut self, rupiah: u32) {",
                    "              self.poin += rupiah / 10_000;",
                    "          }",
                    "      }",
                    "  3. Pembagian bilangan bulat membuang sisanya, dan itu pas dengan aturan",
                    "     \"per kelipatan\": Rp 57.500 jadi 5 poin, Rp 42.500 jadi 4 poin. Total",
                    "     Sari 9 poin.",
                    "  4. Periksa pinggirnya. Total belanja Sari tepat Rp 100.000, jadi kalau",
                    "     poin dihitung dari total, hasilnya 10. Selisih satu poin ini soal",
                    "     aturan bisnis, jadi tanyakan ke pemilik toko sebelum menulis kodenya.",
                    "",
                    "Jebakan: tanpa `mut` di `let mut sari = Member { ... };`, panggilan",
                    "`sari.belanja(...)` ditolak dengan pesan 'cannot borrow `sari` as",
                    "mutable, as it is not declared as mutable'.",
                ]
            },
        ],
    },
    {
        "title": "9. Enum & Option",
        "sections": [
            {
                "body": [
                    "Enum itu tipe yang nilainya dipilih dari daftar kemungkinan yang udah",
                    "ditentukan. Di Rust, enum jauh lebih kuat daripada enum di C atau Java.",
                    "Setiap variannya boleh membawa data, dan bentuk datanya boleh beda-beda",
                    "di tiap varian.",
                    "",
                    "  enum Pesan {",
                    "      Keluar,                       tanpa data",
                    "      Pindah { x: i32, y: i32 },    seperti struct",
                    "      Tulis(String),                seperti tuple",
                    "      Warna(u8, u8, u8),",
                    "  }",
                    "",
                    "Di bahasa lain, konsep ini disebut 'tagged union' atau 'sum type'.",
                    "Sebuah nilai Pesan selalu berisi tepat satu varian, dan compiler tahu",
                    "itu.",
                    "",
                    "Option: cara Rust menggantikan null",
                    "",
                    "  enum Option<T> {",
                    "      None,",
                    "      Some(T),",
                    "  }",
                    "",
                    "Huruf T di situ artinya \"tipe apa pun\". `Option<i32>` berarti: mungkin",
                    "ada sebuah i32 di dalamnya (Some), mungkin kosong (None).",
                    "",
                    "Rust nggak punya null. Nilai yang mungkin kosong ditandai lewat tipenya.",
                    "`Option<i32>` itu tipe yang beda dari `i32`, dan compiler nggak ngizinin",
                    "kamu memakai Option seolah-olah itu angka biasa.",
                    "",
                    "Akibatnya, bug null pointer hilang sama sekali, nggak cuma berkurang.",
                    "Kamu nggak mungkin lupa memeriksa, karena kode yang lupa memeriksa nggak",
                    "bakal dikompilasi.",
                    "",
                    "Cara mengambil isinya:",
                    "  o.unwrap()            ambil; PANIC kalau None",
                    "  o.expect(\"pesan\")     sama, dengan pesan sendiri",
                    "  o.unwrap_or(0)        ambil, atau 0 kalau None",
                    "  o.unwrap_or_else(|| hitung())",
                    "  o.unwrap_or_default() ambil, atau nilai bawaan tipenya",
                    "",
                    "Cara mengubah isinya tanpa membuka bungkusnya:",
                    "  o.map(|x| x * 2)      Some(2x) kalau ada, None kalau tidak",
                    "  o.filter(|x| *x > 3)",
                    "  o.and_then(|x| f(x))  untuk fungsi yang balik Option juga",
                    "  o.is_some() / o.is_none()",
                    "  o.ok_or(\"galat\")      ubah jadi Result",
                    "",
                    "Tulisan seperti `|x| x * 2` itu closure, fungsi kecil tanpa nama.",
                    "Detailnya ada di materi \"Closure & Iterator\". Untuk sekarang, cukup",
                    "baca sebagai \"ambil x, hasilkan x * 2\".",
                    "",
                    "unwrap() cocok untuk contoh dan prototipe. Di kode yang dipakai orang",
                    "lain, setiap unwrap itu janji bahwa nilainya nggak mungkin None. Janji",
                    "itu harus benar, karena kalau ternyata None, programnya panic dan",
                    "berhenti.",
                ]
            },
            {
                "heading": "Enum berdata dan Option dalam praktik",
                "code": """#[derive(Debug)]
enum Bentuk {
    Lingkaran(f64),
    Persegi(f64),
    PersegiPanjang { p: f64, l: f64 },
}

impl Bentuk {
    fn luas(&self) -> f64 {
        match self {
            Bentuk::Lingkaran(r) => 3.14159 * r * r,
            Bentuk::Persegi(s) => s * s,
            Bentuk::PersegiPanjang { p, l } => p * l,
        }
    }

    fn nama(&self) -> &'static str {
        match self {
            Bentuk::Lingkaran(_) => "Lingkaran",
            Bentuk::Persegi(_) => "Persegi",
            Bentuk::PersegiPanjang { .. } => "PersegiPanjang",
        }
    }
}

fn cari(data: &[i32], target: i32) -> Option<usize> {
    for (i, n) in data.iter().enumerate() {
        if *n == target {
            return Some(i);
        }
    }
    None
}

fn main() {
    let semua = vec![
        Bentuk::Lingkaran(2.0),
        Bentuk::Persegi(4.0),
        Bentuk::PersegiPanjang { p: 6.0, l: 3.0 },
    ];

    let mut total = 0.0;
    for b in &semua {
        println!("{:<16}{:8.2}", b.nama(), b.luas());
        total += b.luas();
    }
    println!("{:<16}{:8.2}", "TOTAL", total);

    let data = [10, 20, 30, 40];
    println!("cari 30 -> {:?}", cari(&data, 30));
    println!("cari 99 -> {:?}", cari(&data, 99));
    println!("cari 99 atau 0 -> {}", cari(&data, 99).unwrap_or(0));
    println!("posisi x2 -> {:?}", cari(&data, 20).map(|i| i * 2));
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Lingkaran          12.57",
                    "  Persegi            16.00",
                    "  PersegiPanjang     18.00",
                    "  TOTAL              46.57",
                    "  cari 30 -> Some(2)",
                    "  cari 99 -> None",
                    "  cari 99 atau 0 -> 0",
                    "  posisi x2 -> Some(2)",
                    "",
                    "`Bentuk::PersegiPanjang { .. }` pakai dua titik untuk bilang \"isinya",
                    "nggak penting buatku\". Garis bawah tunggal `_` melakukan hal yang sama",
                    "untuk satu nilai.",
                    "",
                    "Coba bandingkan enum ini dengan pewarisan (class induk dan class anak)",
                    "di C# atau Java. Dua-duanya menyelesaikan masalah yang sama, tapi",
                    "kelebihan dan kekurangannya bertukar:",
                    "  - Enum + match: gampang nambah operasi baru, cukup tulis satu fungsi",
                    "    baru. Nambah varian baru lebih repot, karena semua match harus",
                    "    diperbarui. Untungnya compiler nunjukin di mana aja tempatnya.",
                    "  - Trait atau class: gampang nambah tipe baru, tapi nambah operasi",
                    "    baru berarti menyunting semua tipe. Trait dibahas di materi",
                    "    \"Trait\".",
                    "",
                    "Rust punya dua-duanya. Untuk memilih, tanya satu hal: di masalahmu,",
                    "mana yang lebih sering berubah, daftar bentuknya atau daftar",
                    "operasinya?",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Cara bayar di aplikasi kasir cocok jadi enum: pilihannya terbatas, dan",
                    "sebagian membawa data sendiri. Voucher membawa nilai potongannya,",
                    "sedangkan tunai dan transfer nggak membawa apa-apa. Dengan enum, kasir",
                    "nggak mungkin mencatat cara bayar yang nggak ada di daftar.",
                    "",
                    "Kasus kecil: total belanja Rp 50.000. Bayar tunai dapat potongan",
                    "Rp 2.000, transfer nggak dapat potongan, dan voucher memotong sesuai",
                    "nilainya. Hitung yang harus dibayar untuk tiap cara.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Daftar semua kemungkinannya dulu, lalu tulis jadi varian:",
                    "     `enum Bayar { Tunai, Transfer, Voucher(u32) }`.",
                    "  2. Hitung potongannya dengan `match` di dalam",
                    "     `fn potongan(b: &Bayar) -> u32`. Compiler memastikan tiap varian",
                    "     punya jawaban:",
                    "      match b {",
                    "          Bayar::Tunai => 2_000,",
                    "          Bayar::Transfer => 0,",
                    "          Bayar::Voucher(n) => *n,",
                    "      }",
                    "     Bintang di `*n` perlu karena b dipinjam, jadi n juga referensi.",
                    "  3. Kurangkan dari total: tunai jadi 48000, transfer 50000, dan voucher",
                    "     Rp 15.000 jadi 35000.",
                    "  4. Kasus pinggir: voucher Rp 60.000 untuk belanja Rp 50.000.",
                    "     Pengurangan biasa di u32 bikin build debug panic dengan pesan",
                    "     'attempt to subtract with overflow'. Pakai",
                    "     `total.saturating_sub(potongan(&b))`, saudara `saturating_add`,",
                    "     supaya hasilnya berhenti di 0.",
                    "",
                    "Ingat: kalau kode voucher dicari di daftar dan bisa nggak ketemu, hasil",
                    "pencariannya Option. `unwrap_or(0)` bikin voucher yang nggak dikenal",
                    "bernilai nol.",
                ]
            },
        ],
    },
    {
        "title": "10. Pattern Matching: match & if let",
        "sections": [
            {
                "body": [
                    "`match` itu percabangan berdasarkan pola. Kamu kasih sebuah nilai, lalu",
                    "Rust mencocokkannya dengan pola-pola di bawahnya satu per satu, mulai",
                    "dari atas. Ini salah satu bagian Rust yang paling enak dipakai.",
                    "",
                    "  match nilai {",
                    "      1 => println!(\"satu\"),",
                    "      2 | 3 => println!(\"dua atau tiga\"),",
                    "      4..=6 => println!(\"empat sampai enam\"),",
                    "      n if n < 0 => println!(\"negatif {n}\"),",
                    "      _ => println!(\"lainnya\"),",
                    "  }",
                    "",
                    "Sifat yang paling penting: match wajib exhaustive, artinya semua",
                    "kemungkinan harus tertangani. Kalau ada satu yang ketinggalan, kodenya",
                    "nggak bakal dikompilasi.",
                    "",
                    "Aturan ini justru fitur utamanya. Waktu kamu nambah varian baru ke",
                    "sebuah enum, compiler nunjukin setiap tempat di seluruh proyek yang",
                    "perlu diperbarui. Di bahasa yang nggak punya aturan ini, varian baru",
                    "itu biasanya ketelan cabang default tanpa ada yang sadar, dan bugnya",
                    "baru muncul entah kapan.",
                    "",
                    "match juga ekspresi, jadi dia menghasilkan nilai:",
                    "",
                    "  let label = match n {",
                    "      0 => \"nol\",",
                    "      n if n > 0 => \"positif\",",
                    "      _ => \"negatif\",",
                    "  };",
                    "",
                    "Semua cabang wajib bertipe sama.",
                    "",
                    "`if let` itu match yang cuma peduli satu pola:",
                    "",
                    "  if let Some(x) = hasil {",
                    "      println!(\"dapat {x}\");",
                    "  } else {",
                    "      println!(\"kosong\");",
                    "  }",
                    "",
                    "`let else` dipakai untuk keluar lebih awal kalau polanya nggak cocok:",
                    "",
                    "  let Some(x) = hasil else {",
                    "      return;",
                    "  };",
                    "  // di sini x sudah pasti ada",
                    "",
                    "`while let` mengulang selama polanya masih cocok:",
                    "",
                    "  while let Some(atas) = tumpukan.pop() {",
                    "      println!(\"{atas}\");",
                    "  }",
                ]
            },
            {
                "heading": "Pola-pola yang sering dipakai",
                "code": """#[derive(Debug)]
enum Perintah {
    Berhenti,
    Geser { x: i32, y: i32 },
    Tulis(String),
    Warna(u8, u8, u8),
}

fn jalankan(p: &Perintah) -> String {
    match p {
        Perintah::Berhenti => "berhenti".to_string(),
        Perintah::Geser { x: 0, y: 0 } => "tidak bergerak".to_string(),
        Perintah::Geser { x, y } => format!("geser ke ({x}, {y})"),
        Perintah::Tulis(t) if t.is_empty() => "tulis kosong".to_string(),
        Perintah::Tulis(t) => format!("tulis \\"{t}\\""),
        Perintah::Warna(r, g, b) => format!("warna #{r:02x}{g:02x}{b:02x}"),
    }
}

fn main() {
    let daftar = vec![
        Perintah::Berhenti,
        Perintah::Geser { x: 0, y: 0 },
        Perintah::Geser { x: 3, y: -2 },
        Perintah::Tulis(String::new()),
        Perintah::Tulis("halo".to_string()),
        Perintah::Warna(255, 128, 0),
    ];

    for p in &daftar {
        println!("{}", jalankan(p));
    }

    // Destructuring tuple dan slice
    let titik = (3, -7);
    let arah = match titik {
        (0, 0) => "pusat",
        (_, 0) => "sumbu x",
        (0, _) => "sumbu y",
        (x, y) if x > 0 && y > 0 => "kuadran I",
        (x, y) if x > 0 && y < 0 => "kuadran IV",
        _ => "kiri",
    };
    println!("{titik:?} ada di {arah}");

    let angka = [1, 2, 3, 4, 5];
    match angka {
        [pertama, .., terakhir] => println!("{pertama} .. {terakhir}"),
    }

    // while let pada tumpukan
    let mut tumpuk = vec![1, 2, 3];
    while let Some(atas) = tumpuk.pop() {
        print!("{atas} ");
    }
    println!();
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  berhenti",
                    "  tidak bergerak",
                    "  geser ke (3, -2)",
                    "  tulis kosong",
                    "  tulis \"halo\"",
                    "  warna #ff8000",
                    "  (3, -7) ada di kuadran IV",
                    "  1 .. 5",
                    "  3 2 1",
                    "",
                    "Lihat urutan dua cabang Geser. `Perintah::Geser { x: 0, y: 0 }` ditulis",
                    "sebelum `Perintah::Geser { x, y }`. Rust berhenti di pola pertama yang",
                    "cocok, jadi pola yang lebih sempit harus ditaruh lebih dulu. Kalau",
                    "urutannya dibalik, cabang khusus itu nggak akan pernah kepakai, dan",
                    "compiler ngasih peringatan 'unreachable pattern'.",
                    "",
                    "Ringkasan bentuk pola yang bisa kamu pakai:",
                    "",
                    "  1, \"teks\", true      literal",
                    "  n                    ikat ke variabel baru",
                    "  _                    abaikan satu nilai",
                    "  ..                   abaikan sisanya",
                    "  a | b                salah satu",
                    "  1..=5                rentang inklusif",
                    "  Some(x)              varian enum berdata",
                    "  Titik { x, y }       struct",
                    "  (a, b)               tuple",
                    "  [a, .., z]           slice",
                    "  n @ 1..=5            ikat SEKALIGUS batasi",
                    "  pola if syarat       guard tambahan",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tabel tarif, misalnya ongkos kirim paket menurut zona dan berat, bisa",
                    "ditulis hampir apa adanya sebagai `match` atas tuple. Tiap baris tabel",
                    "jadi satu cabang, dan compiler menuntut semua kemungkinan tertangani,",
                    "termasuk zona yang nggak dilayani.",
                    "",
                    "Kasus kecil: jasa kirim memakai aturan ini. Zona 1 (dalam kota) Rp 8.000",
                    "untuk kilo pertama dan Rp 3.000 per kilo berikutnya. Zona 2 (luar pulau)",
                    "Rp 25.000 per kilo. Zona lain nggak dilayani, dan paket 0 kg ditolak.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua angka, zona dan berat, jadi cocokkan tuple",
                    "     `(zona, berat)`. Keluarannya `Option<u32>`, karena ada kiriman yang",
                    "     nggak punya tarif.",
                    "  2. Sederhanakan rumus zona 1: 8.000 untuk kilo pertama plus 3.000 per",
                    "     kilo berikutnya sama dengan 5.000 + 3.000 x berat.",
                    "  3. Tulis cabangnya mulai dari yang paling sempit:",
                    "      match (zona, berat) {",
                    "          (_, 0) => None,",
                    "          (1, b) => Some(5_000 + b * 3_000),",
                    "          (2, b) => Some(b * 25_000),",
                    "          _ => None,",
                    "      }",
                    "  4. Uji tiap baris tabel: (1, 3) jadi Some(14000), (2, 2) jadi",
                    "     Some(50000), dan (3, 1) jadi None. Lalu coba pindahkan `(_, 0)` ke",
                    "     bawah `(1, b)`. Paket 0 kg di zona 1 jadi ditagih Rp 5.000, karena",
                    "     `(1, b)` cocok lebih dulu, dan compiler nggak memperingatkan apa pun.",
                ]
            },
        ],
    },
    {
        "title": "11. Vec & HashMap",
        "sections": [
            {
                "body": [
                    "Vec<T> itu array yang bisa tumbuh. Isinya disimpan di heap, yaitu",
                    "bagian memori untuk data yang ukurannya bisa berubah waktu program",
                    "jalan.",
                    "",
                    "  let mut v: Vec<i32> = Vec::new();",
                    "  let mut v = vec![1, 2, 3];        makro vec!",
                    "  let v = vec![0; 5];               [0,0,0,0,0]",
                    "",
                    "  v.push(4);            tambah di akhir",
                    "  v.pop()               ambil terakhir -> Option<T>",
                    "  v.insert(0, 9);       sisipkan di index 0",
                    "  v.remove(0)           hapus index 0, kembalikan nilainya",
                    "  v.len()               jumlah isi",
                    "  v.is_empty()",
                    "  v.contains(&3)        perhatikan &",
                    "  v.sort()              urutkan di tempat",
                    "  v.dedup()             buang duplikat BERURUTAN",
                    "  v.reverse()",
                    "  v.clear()",
                    "",
                    "Ada dua cara mengambil elemen, dan bedanya penting:",
                    "  v[0]        PANIC kalau di luar batas",
                    "  v.get(0)    -> Option<&T>, aman",
                    "",
                    "Kalau indeksnya datang dari luar, misalnya dari masukan pengguna atau",
                    "isi berkas, selalu pakai `get`.",
                    "",
                    "HashMap<K, V> nyimpen pasangan kunci dan nilai. Mirip kamus: kamu cari",
                    "pakai kuncinya, lalu dapat nilainya.",
                    "",
                    "  use std::collections::HashMap;",
                    "",
                    "  let mut m = HashMap::new();",
                    "  m.insert(\"andi\", 88);",
                    "  m.get(\"andi\")            -> Option<&V>",
                    "  m.contains_key(\"andi\")",
                    "  m.remove(\"andi\")         -> Option<V>",
                    "  m.len()",
                    "",
                    "Pola penghitung yang paling sering dipakai:",
                    "  *m.entry(kata).or_insert(0) += 1;",
                    "",
                    "Cara bacanya: `entry` ngasih tempat untuk kunci itu. `or_insert(0)`",
                    "mengisinya dengan 0 kalau kuncinya belum ada, lalu ngasih referensi ke",
                    "nilainya. Bintang di depan membuka referensi itu supaya nilainya bisa",
                    "ditambah. Satu baris ini menggantikan if-else lengkap.",
                    "",
                    "Jebakan: urutan isi HashMap nggak dijamin. Di Rust, urutannya bahkan",
                    "diacak tiap kali program dijalankan. Ini disengaja, sebagai pertahanan",
                    "terhadap serangan hash collision, yaitu penyerang yang sengaja ngirim",
                    "kunci-kunci yang bikin HashMap jadi lambat. Kalau urutan penting,",
                    "urutkan sendiri, atau pakai BTreeMap yang isinya selalu terurut.",
                ]
            },
            {
                "heading": "Menghitung frekuensi kata",
                "code": """use std::collections::HashMap;

fn main() {
    let kalimat = "kucing makan ikan kucing tidur ikan kucing";

    let mut hitung: HashMap<&str, u32> = HashMap::new();
    for kata in kalimat.split_whitespace() {
        *hitung.entry(kata).or_insert(0) += 1;
    }

    // HashMap tidak punya urutan, jadi urutkan eksplisit sebelum dicetak.
    let mut pasangan: Vec<(&&str, &u32)> = hitung.iter().collect();
    pasangan.sort_by(|a, b| b.1.cmp(a.1).then(a.0.cmp(b.0)));

    for (kata, n) in &pasangan {
        println!("{kata:<7}: {n}");
    }
    println!("---");
    println!("kata unik  : {}", hitung.len());
    println!("total kata : {}", kalimat.split_whitespace().count());

    // Vec: operasi sehari-hari
    let mut angka = vec![5, 3, 9, 1, 7, 3];
    angka.sort();
    angka.dedup();
    println!("terurut unik: {angka:?}");
    println!("terbesar    : {:?}", angka.iter().max());
    println!("ambil ke-99 : {:?}", angka.get(99));
    println!("jumlah      : {}", angka.iter().sum::<i32>());
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "  ---",
                    "  kata unik  : 4",
                    "  total kata : 7",
                    "  terurut unik: [1, 3, 5, 7, 9]",
                    "  terbesar    : Some(9)",
                    "  ambil ke-99 : None",
                    "  jumlah      : 25",
                    "",
                    "Baris `sort_by(|a, b| b.1.cmp(a.1).then(a.0.cmp(b.0)))` dibaca begini:",
                    "urutkan menurun berdasarkan jumlah, lalu kalau jumlahnya sama, urutkan",
                    "menaik berdasarkan kata. Hasilnya menurun karena yang dibandingkan b",
                    "dengan a, kebalikan dari biasanya. `then` menyambungkan kunci urutan",
                    "kedua.",
                    "",
                    "`dedup()` cuma membuang duplikat yang letaknya bersebelahan. Makanya",
                    "dia hampir selalu dipanggil sesudah `sort()`. Kalau dipanggil sendirian",
                    "di data yang acak, sebagian besar duplikat lolos, dan kamu nggak dapat",
                    "error apa pun.",
                    "",
                    "`sum::<i32>()` lagi-lagi pakai turbofish. `sum` bisa menjumlahkan ke",
                    "banyak tipe, jadi tipenya harus kamu sebut. Cara lain, tulis tipenya di",
                    "variabel: `let total: i32 = angka.iter().sum();`",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rekap penjualan per produk dari daftar transaksi kasir dikerjakan dengan",
                    "HashMap: kuncinya nama produk, nilainya jumlah yang terjual. Bentuk yang",
                    "sama dipakai untuk rekap absensi per siswa atau jumlah pesanan per",
                    "kecamatan.",
                    "",
                    "Kasus kecil: transaksi warung kopi hari ini (kopi, 2), (teh, 1),",
                    "(kopi, 3), (roti, 4), dan (teh, 2). Pemilik minta total per produk, dari",
                    "yang paling laku.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya daftar pasangan (produk, jumlah). Keluarannya satu baris",
                    "     per produk, terurut dari jumlah terbesar.",
                    "  2. Kumpulkan dengan pola penghitung, lalu pindahkan ke Vec supaya bisa",
                    "     diurutkan:",
                    "      let mut total: HashMap<&str, u32> = HashMap::new();",
                    "      for (produk, n) in penjualan {",
                    "          *total.entry(produk).or_insert(0) += n;",
                    "      }",
                    "      let mut urut: Vec<(&str, u32)> = total.into_iter().collect();",
                    "      urut.sort_by(|a, b| b.1.cmp(&a.1));",
                    "  3. Hasilnya kopi 5, roti 4, teh 3. Pengurutan wajib, karena urutan",
                    "     HashMap berubah tiap program dijalankan.",
                    "  4. Kasus pinggir: kasir mengetik \"Kopi\" di satu transaksi dan \"kopi\" di",
                    "     transaksi lain, dan HashMap menganggapnya dua produk. Seragamkan dulu",
                    "     dengan `to_lowercase()`, pasangan `to_uppercase()`. Kalau dua produk",
                    "     jumlahnya sama, tambahkan `.then(a.0.cmp(b.0))` di `sort_by` supaya",
                    "     urutannya tetap.",
                ]
            },
        ],
    },
    {
        "title": "12. Penanganan Galat: panic! & Result",
        "sections": [
            {
                "body": [
                    "Rust membagi kegagalan jadi dua jenis, dan pembagian itu kelihatan di",
                    "tipenya.",
                    "",
                    "Jenis pertama: kegagalan yang nggak bisa dipulihkan. Untuk ini Rust",
                    "pakai panic!, dan programnya langsung berhenti. Ini dipakai untuk bug:",
                    "indeks di luar batas, invariant yang dilanggar (syarat yang menurut",
                    "programmernya selalu benar), atau keadaan yang mustahil.",
                    "",
                    "  panic!(\"ini seharusnya tidak pernah terjadi\");",
                    "  assert!(n > 0, \"n harus positif\");",
                    "  assert_eq!(hasil, 42);",
                    "  unreachable!();",
                    "  todo!();",
                    "",
                    "Jenis kedua: kegagalan yang bisa dipulihkan. Untuk ini Rust pakai",
                    "Result. Contohnya berkas nggak ada, jaringan putus, atau masukan nggak",
                    "sah. Hal-hal begini wajar terjadi, dan programmu harus tahu apa yang",
                    "dilakukan kalau itu terjadi.",
                    "",
                    "  enum Result<T, E> {",
                    "      Ok(T),",
                    "      Err(E),",
                    "  }",
                    "",
                    "Result itu enum dengan dua varian. Ok berisi hasilnya, Err berisi",
                    "keterangan galatnya.",
                    "",
                    "Result harus ditangani. Kalau kamu mengabaikannya, compiler ngasih",
                    "peringatan, karena Result ditandai `#[must_use]`. Rust nggak ngebiarin",
                    "kamu lupa bahwa sesuatu bisa gagal.",
                    "",
                    "Cara menanganinya:",
                    "",
                    "  match hasil {",
                    "      Ok(n) => ...,",
                    "      Err(e) => ...,",
                    "  }",
                    "",
                    "  hasil.unwrap()              ambil; panic kalau Err",
                    "  hasil.expect(\"pesan\")       sama, pesannya sendiri",
                    "  hasil.unwrap_or(0)",
                    "  hasil.unwrap_or_else(|e| ...)",
                    "  hasil.is_ok() / is_err()",
                    "  hasil.ok()                  ubah jadi Option",
                    "  hasil.map_err(|e| ...)      ubah tipe galatnya",
                    "",
                    "Operator ? yang bikin penanganan galat di Rust enak dipakai:",
                    "",
                    "  fn baca(path: &str) -> Result<String, io::Error> {",
                    "      let isi = fs::read_to_string(path)?;",
                    "      Ok(isi.trim().to_string())",
                    "  }",
                    "",
                    "Tanda tanya itu artinya: kalau hasilnya Ok, ambil isinya dan lanjut.",
                    "Kalau Err, galat itu langsung dikembalikan dari fungsi ini. Satu",
                    "karakter menggantikan lima baris match.",
                    "",
                    "Semuanya juga tetap kelihatan. Kamu bisa lihat di baris mana kegagalan",
                    "bisa terjadi, karena ada tanda ? di situ. Exception di bahasa lain bisa",
                    "melompat dari mana aja tanpa tanda apa pun di kodenya.",
                    "",
                    "`?` cuma boleh dipakai di fungsi yang mengembalikan Result atau Option.",
                    "Sejak Rust 1.26, `fn main()` juga boleh mengembalikan Result.",
                ]
            },
            {
                "heading": "Result dan operator ?",
                "code": """#[derive(Debug)]
enum GalatNilai {
    BukanAngka(String),
    DiLuarRentang(i32),
}

fn parse_nilai(teks: &str) -> Result<i32, GalatNilai> {
    let n: i32 = teks
        .trim()
        .parse()
        .map_err(|_| GalatNilai::BukanAngka(teks.to_string()))?;

    if !(0..=100).contains(&n) {
        return Err(GalatNilai::DiLuarRentang(n));
    }
    Ok(n)
}

fn rata_rata(semua: &[&str]) -> Result<f64, GalatNilai> {
    let mut total = 0;
    for t in semua {
        total += parse_nilai(t)?;      // gagal satu -> seluruh fungsi gagal
    }
    Ok(total as f64 / semua.len() as f64)
}

fn main() {
    for t in ["88", " 92 ", "abc", "150", "-3"] {
        match parse_nilai(t) {
            Ok(n) => println!("{t:>5} -> {n}"),
            Err(GalatNilai::BukanAngka(s)) => println!("{t:>5} -> bukan angka: {s}"),
            Err(GalatNilai::DiLuarRentang(n)) => println!("{t:>5} -> di luar 0..100: {n}"),
        }
    }

    println!("rata-rata baik : {:?}", rata_rata(&["80", "90", "100"]));
    println!("rata-rata rusak: {:?}", rata_rata(&["80", "xx", "100"]));
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "     88 -> 88",
                    "    92  -> 92",
                    "    abc -> bukan angka: abc",
                    "    150 -> di luar 0..100: 150",
                    "     -3 -> di luar 0..100: -3",
                    "  rata-rata baik : Ok(90.0)",
                    "  rata-rata rusak: Err(BukanAngka(\"xx\"))",
                    "",
                    "Lihat `rata_rata`. Cukup satu baris `parse_nilai(t)?`, dan seluruh",
                    "penanganan kegagalannya beres. Tanpa `?`, fungsi itu butuh blok match",
                    "lima baris di dalam perulangan.",
                    "",
                    "`map_err` mengubah tipe galat dari ParseIntError jadi GalatNilai.",
                    "Langkah ini perlu karena `?` menuntut tipe galatnya bisa diubah ke tipe",
                    "galat yang dikembalikan fungsinya.",
                    "",
                    "Di proyek nyata, ada dua crate (pustaka Rust yang bisa dipasang lewat",
                    "Cargo) yang bikin ini jauh lebih ringkas:",
                    "  - thiserror, untuk pustaka. Kamu bikin enum galat sendiri lengkap",
                    "    dengan pesannya, cukup satu atribut per varian.",
                    "  - anyhow, untuk aplikasi. Satu tipe galat untuk semuanya, dengan",
                    "    konteks yang bisa ditumpuk berlapis.",
                    "",
                    "Aturan praktis memilih panic atau Result:",
                    "  - Programmer salah pakai API: panic. Itu bug.",
                    "  - Masukan salah dari pengguna atau dunia luar: Result. Itu keadaan",
                    "    normal.",
                    "  - Di pustaka: hampir selalu Result. Biarkan pemakainya yang",
                    "    memutuskan apakah galatnya fatal.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kolom nominal di aplikasi top up atau transfer menerima apa saja yang",
                    "diketik pengguna. Masukan yang salah di situ hal biasa, jadi fungsinya",
                    "mengembalikan Result. Aplikasi bisa menampilkan pesan yang jelas, dan",
                    "programnya nggak berhenti mendadak.",
                    "",
                    "Kasus kecil: aplikasi menetapkan top up minimal Rp 10.000. Pengguna",
                    "mengetik \"50000\", \"50.000\", \"5000\", dan \"lima puluh ribu\". Mana yang",
                    "diterima, dan apa pesan untuk yang ditolak?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan bentuk hasilnya: `Result<u32, String>`. Ok membawa nominal,",
                    "     Err membawa pesan untuk pengguna.",
                    "  2. Pecah jadi dua pemeriksaan: bisa diurai jadi angka, lalu memenuhi",
                    "     batas minimal. Pemeriksaan pertama cukup satu baris berkat `?`:",
                    "      let rapi = teks.trim().replace(\".\", \"\");",
                    "      let n: u32 = rapi.parse().map_err(|_| format!(\"bukan angka: {teks}\"))?;",
                    "      if n < 10_000 {",
                    "          return Err(format!(\"minimal 10000, dapat {n}\"));",
                    "      }",
                    "      Ok(n)",
                    "  3. Hasilnya, \"50000\" dan \"50.000\" sama-sama Ok(50000), \"5000\" ditolak",
                    "     karena di bawah minimal, dan \"lima puluh ribu\" ditolak sebagai bukan",
                    "     angka.",
                    "  4. Baris `replace(\".\", \"\")` menangani kasus pinggir khas Indonesia:",
                    "     orang menulis titik sebagai pemisah ribuan. Tanpa baris itu,",
                    "     `\"50.000\".parse::<u32>()` gagal dengan InvalidDigit.",
                    "",
                    "Jebakan: \"-20000\" ikut ditolak sebagai bukan angka, karena u32 nggak",
                    "menerima tanda minus. Kalau perlu pesan yang lebih tepat, urai dulu ke",
                    "i64, lalu periksa tandanya.",
                ]
            },
        ],
    },
    {
        "title": "13. Generic",
        "sections": [
            {
                "body": [
                    "Generic bikin satu potong kode bisa dipakai untuk banyak tipe.",
                    "Pemeriksaan tipenya tetap jalan, dan programnya nggak jadi lambat waktu",
                    "dijalankan.",
                    "",
                    "Contoh fungsi generic:",
                    "  fn terbesar<T: PartialOrd>(daftar: &[T]) -> &T {",
                    "      let mut hasil = &daftar[0];",
                    "      for x in daftar {",
                    "          if x > hasil { hasil = x; }",
                    "      }",
                    "      hasil",
                    "  }",
                    "",
                    "Huruf T itu nama sementara untuk \"tipe apa pun\". `<T: PartialOrd>`",
                    "dibaca: untuk tipe T apa pun yang bisa dibandingkan. Tanpa batasan itu,",
                    "compiler menolak `x > hasil`, karena nggak semua tipe bisa",
                    "dibandingkan. PartialOrd itu sebuah trait; trait dibahas di materi",
                    "\"Trait\".",
                    "",
                    "Struct generic:",
                    "  struct Titik<T> { x: T, y: T }",
                    "  struct Pasangan<A, B> { kiri: A, kanan: B }",
                    "",
                    "Enum generic juga ada, dan dua yang paling penting udah kamu pakai:",
                    "Option<T> dan Result<T, E>.",
                    "",
                    "Batasan bisa ditulis dengan dua cara. Cara kedua, pakai where, lebih",
                    "gampang dibaca kalau batasannya banyak:",
                    "",
                    "  fn f<T: Clone + Debug>(x: T) { ... }",
                    "",
                    "  fn f<T>(x: T)",
                    "  where",
                    "      T: Clone + Debug,",
                    "  { ... }",
                    "",
                    "Waktu kompilasi, Rust bikin salinan kode khusus untuk setiap tipe yang",
                    "beneran dipakai. Proses ini namanya monomorphization.",
                    "`terbesar::<i32>` dan `terbesar::<f64>` jadi dua fungsi terpisah di",
                    "binari.",
                    "",
                    "Akibatnya, generic di Rust gratis waktu program jalan. Kodenya secepat",
                    "kode yang ditulis khusus untuk tipe itu. Nggak ada boxing (membungkus",
                    "nilai lalu menaruhnya di heap) dan nggak ada pencarian di tabel",
                    "virtual. Harganya: binari jadi lebih besar dan kompilasi lebih lama.",
                ]
            },
            {
                "heading": "Generic dengan batasan",
                "code": """use std::fmt::Display;

fn terbesar<T: PartialOrd + Copy>(daftar: &[T]) -> T {
    let mut hasil = daftar[0];
    for &x in daftar {
        if x > hasil {
            hasil = x;
        }
    }
    hasil
}

fn cetak_semua<T: Display>(judul: &str, daftar: &[T]) {
    print!("{judul:<8}:");
    for x in daftar {
        print!(" {x}");
    }
    println!();
}

struct Kotak<T> {
    isi: Vec<T>,
    muat: usize,
}

impl<T: Display> Kotak<T> {
    fn baru(muat: usize) -> Self {
        Kotak { isi: Vec::new(), muat }
    }

    fn masuk(&mut self, x: T) -> bool {
        if self.isi.len() >= self.muat {
            return false;
        }
        self.isi.push(x);
        true
    }

    fn ringkas(&self) -> String {
        let daftar: Vec<String> = self.isi.iter().map(|x| x.to_string()).collect();
        format!("[{}] {}/{}", daftar.join(", "), self.isi.len(), self.muat)
    }
}

fn main() {
    let angka = [3, 9, 1, 7];
    let pecahan = [2.5, 8.1, 4.4];
    let huruf = ['r', 'u', 's', 't'];

    println!("terbesar i32  : {}", terbesar(&angka));
    println!("terbesar f64  : {}", terbesar(&pecahan));
    println!("terbesar char : {}", terbesar(&huruf));

    cetak_semua("angka", &angka);
    cetak_semua("huruf", &huruf);

    let mut kotak = Kotak::baru(3);
    for n in [10, 20, 30, 40] {
        println!("masuk {n}: {}", kotak.masuk(n));
    }
    println!("{}", kotak.ringkas());
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  terbesar i32  : 9",
                    "  terbesar f64  : 8.1",
                    "  terbesar char : u",
                    "  angka   : 3 9 1 7",
                    "  huruf   : r u s t",
                    "  masuk 10: true",
                    "  masuk 20: true",
                    "  masuk 30: true",
                    "  masuk 40: false",
                    "  [10, 20, 30] 3/3",
                    "",
                    "`for &x in daftar` memakai pola untuk membuka referensinya sekalian.",
                    "Tanpa `&` di situ, x bertipe `&T` dan perbandingannya jadi beda. Ini",
                    "juga pattern matching, cuma di tempat yang nggak kelihatan seperti",
                    "match.",
                    "",
                    "`impl<T: Display> Kotak<T>` ngasih method hanya ke Kotak yang isinya",
                    "bisa ditampilkan. Kotak<T> dengan T yang nggak Display tetap bisa",
                    "dibikin, cuma nggak punya method-method ini. Teknik ini namanya",
                    "conditional implementation, dan dipakai di seluruh pustaka standar.",
                    "",
                    "Batasan yang paling sering kamu tulis:",
                    "  Clone         bisa disalin dengan .clone()",
                    "  Copy          disalin otomatis",
                    "  Debug         bisa dicetak {:?}",
                    "  Display       bisa dicetak {}",
                    "  PartialEq     bisa dibandingkan ==",
                    "  PartialOrd    bisa dibandingkan <",
                    "  Default       punya nilai bawaan",
                    "  Into<T>       bisa diubah jadi T",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Paginasi, yaitu membagi daftar panjang jadi halaman berisi 10 atau 20",
                    "item, dipakai di toko online dan panel admin. Logika memotongnya sama",
                    "persis untuk daftar produk, daftar pesanan, atau daftar pelanggan, jadi",
                    "cukup ditulis sekali sebagai fungsi generic.",
                    "",
                    "Kasus kecil: ada 23 produk dan 23 harga, ditampilkan 10 per halaman.",
                    "Halaman 3 harus berisi 3 item, dan halaman 4 harus kosong tanpa bikin",
                    "program panic.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya slice berisi tipe apa pun, nomor halaman, dan jumlah per",
                    "     halaman. Keluarannya potongan dari slice yang sama, jadi `&[T]`.",
                    "  2. Hitung indeks awal dan akhir, lalu potong:",
                    "      fn halaman<T>(data: &[T], ke: usize, per: usize) -> &[T] {",
                    "          let awal = (ke - 1) * per;",
                    "          if awal >= data.len() { return &[]; }",
                    "          let akhir = (awal + per).min(data.len());",
                    "          &data[awal..akhir]",
                    "      }",
                    "     `.min(data.len())` mengambil yang lebih kecil, supaya halaman",
                    "     terakhir nggak melewati ujung data.",
                    "  3. `T` di sini nggak butuh batasan, karena fungsinya nggak membandingkan",
                    "     atau mencetak isinya. Fungsi yang sama langsung jalan untuk",
                    "     `Vec<String>` maupun `Vec<u32>`.",
                    "  4. Kasus pinggir: halaman 4 berangkat dari indeks 30, lebih dari 23,",
                    "     jadi hasilnya slice kosong. Halaman 0 berbahaya, karena `0 - 1` pada",
                    "     usize bikin panic. Tolak nomor 0 sebelum memanggil fungsinya.",
                ]
            },
        ],
    },
    {
        "title": "14. Trait",
        "sections": [
            {
                "body": [
                    "Trait itu kumpulan perilaku yang bisa dimiliki banyak tipe. Mirip",
                    "interface di bahasa lain. Bedanya, trait bisa kamu terapkan juga ke",
                    "tipe yang bukan buatanmu.",
                    "",
                    "  trait BisaSapa {",
                    "      fn nama(&self) -> String;",
                    "",
                    "      // Implementasi BAWAAN: boleh dipakai apa adanya",
                    "      fn sapa(&self) -> String {",
                    "          format!(\"Halo, {}!\", self.nama())",
                    "      }",
                    "  }",
                    "",
                    "  impl BisaSapa for Murid {",
                    "      fn nama(&self) -> String { self.nama.clone() }",
                    "  }",
                    "",
                    "`nama` cuma ditulis tanda tangannya, jadi setiap tipe wajib mengisinya",
                    "sendiri. `sapa` udah punya isi. Itu namanya implementasi bawaan: tipe",
                    "yang menerapkan BisaSapa langsung dapat `sapa` tanpa nulis apa-apa.",
                    "",
                    "Trait yang paling sering kamu implementasi:",
                    "",
                    "  Display     bagaimana tipe ini dicetak dengan {}",
                    "  Debug       bagaimana dicetak dengan {:?} (biasanya derive)",
                    "  Default     nilai bawaannya apa",
                    "  From<T>     bagaimana membuatnya dari T",
                    "  Iterator    bagaimana ia ditelusuri",
                    "  PartialOrd  bagaimana ia diurutkan",
                    "  Drop        apa yang terjadi saat ia dilepas",
                    "",
                    "Ada dua cara memakai trait sebagai tipe, dan bedanya terasa:",
                    "  - Static dispatch: `fn f(x: &impl BisaSapa)`, atau",
                    "    `fn f<T: BisaSapa>(x: &T)`. Tipenya dipilih waktu kompilasi. Cepat",
                    "    dan tanpa ongkos tambahan, tapi satu pemanggilan cuma bisa untuk",
                    "    satu tipe.",
                    "  - Dynamic dispatch: `fn f(x: &dyn BisaSapa)`. Tipenya dipilih waktu",
                    "    program jalan, lewat tabel virtual, yaitu daftar alamat method yang",
                    "    dicari pas method itu dipanggil. Sedikit lebih lambat, tapi satu",
                    "    Vec bisa memuat berbagai tipe sekaligus: `Vec<Box<dyn BisaSapa>>`.",
                    "",
                    "Aturan praktisnya: pakai `impl Trait` dulu. Pindah ke `dyn` cuma kalau",
                    "kamu perlu menyimpan tipe yang beda-beda dalam satu koleksi.",
                    "",
                    "Ada juga aturan keyatiman (orphan rule). Kamu boleh menerapkan trait ke",
                    "tipe apa pun, asalkan trait-nya atau tipenya milikmu. Aturan ini",
                    "mencegah dua crate yang berbeda ngasih implementasi yang bertabrakan",
                    "untuk pasangan trait dan tipe yang sama.",
                ]
            },
            {
                "heading": "Trait, Display, dan dynamic dispatch",
                "code": """use std::fmt;

trait Bangun {
    fn luas(&self) -> f64;
    fn nama(&self) -> String;

    // Implementasi bawaan, boleh ditimpa
    fn ringkas(&self) -> String {
        format!("{:<12}{:8.2}", self.nama(), self.luas())
    }
}

struct Persegi { sisi: f64 }
struct Lingkaran { jari: f64 }

impl Bangun for Persegi {
    fn luas(&self) -> f64 { self.sisi * self.sisi }
    fn nama(&self) -> String { "Persegi".to_string() }
}

impl Bangun for Lingkaran {
    fn luas(&self) -> f64 { 3.14159 * self.jari * self.jari }
    fn nama(&self) -> String { "Lingkaran".to_string() }
    fn ringkas(&self) -> String {
        format!("{:<12}{:8.2}  (r={})", self.nama(), self.luas(), self.jari)
    }
}

// Display: mengatur bagaimana tipe ini dicetak dengan {}
impl fmt::Display for Persegi {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "Persegi bersisi {}", self.sisi)
    }
}

// impl Trait: satu tipe, dipilih saat kompilasi
fn jelaskan(b: &impl Bangun) -> String {
    b.ringkas()
}

fn main() {
    let p = Persegi { sisi: 4.0 };
    let l = Lingkaran { jari: 3.0 };

    println!("{}", jelaskan(&p));
    println!("{}", jelaskan(&l));
    println!("display : {p}");

    // dyn Trait: banyak tipe berbeda dalam SATU koleksi
    let semua: Vec<Box<dyn Bangun>> = vec![
        Box::new(Persegi { sisi: 2.0 }),
        Box::new(Lingkaran { jari: 1.0 }),
        Box::new(Persegi { sisi: 5.0 }),
    ];

    let total: f64 = semua.iter().map(|b| b.luas()).sum();
    for b in &semua {
        println!("{}", b.ringkas());
    }
    println!("{:<12}{:8.2}", "TOTAL", total);
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Persegi        16.00",
                    "  Lingkaran      28.27  (r=3)",
                    "  display : Persegi bersisi 4",
                    "  Persegi         4.00",
                    "  Lingkaran       3.14  (r=1)",
                    "  Persegi        25.00",
                    "  TOTAL          32.14",
                    "",
                    "`Box<dyn Bangun>` dibaca: sebuah kotak di heap yang isinya sesuatu yang",
                    "menerapkan Bangun. Box perlu karena ukuran tipe aslinya nggak diketahui",
                    "waktu kompilasi, padahal Vec menuntut semua elemennya berukuran sama.",
                    "Ukuran Box selalu sama apa pun isinya. Untuk `dyn`, Box berisi dua",
                    "penunjuk: satu ke datanya, satu ke tabel virtualnya.",
                    "",
                    "Lingkaran menimpa `ringkas()`, sedangkan Persegi memakai yang bawaan.",
                    "Ini gunanya implementasi bawaan di trait. Kamu ngasih perilaku yang",
                    "masuk akal untuk semua tipe, dan tipe yang butuh beda tinggal nulis",
                    "versinya sendiri.",
                    "",
                    "Begitu kamu menerapkan `Display`, kamu dapat `.to_string()` gratis.",
                    "Asalnya dari blanket implementation di pustaka standar, yaitu",
                    "implementasi yang otomatis berlaku untuk semua tipe yang memenuhi",
                    "syarat tertentu. Pola \"terapkan satu, dapat banyak\" ini ada di mana-mana",
                    "di Rust. Menerapkan `Iterator` aja langsung ngasih kamu map, filter,",
                    "fold, dan puluhan method lainnya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Pengingat jadwal di aplikasi antrean puskesmas bisa dikirim lewat SMS,",
                    "WhatsApp, atau email, tergantung pilihan pasien. Kode pemanggilnya cukup",
                    "tahu satu hal, yaitu \"kirim pesan ini\", dan trait yang menyatukan",
                    "cara-cara kirim yang berbeda itu.",
                    "",
                    "Kasus kecil: dua pasien memilih saluran berbeda, satu SMS dan satu",
                    "WhatsApp. Saat nomor antrean A-12 dipanggil, keduanya harus dapat pesan",
                    "lewat salurannya masing-masing, dalam satu perulangan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari yang sama dan yang beda. Sama: semuanya mengirim pesan. Beda:",
                    "     format dan batasnya. Yang sama jadi trait, yang beda jadi struct.",
                    "  2. Tulis trait-nya, lalu terapkan ke `Sms` dan `WhatsApp` dengan",
                    "     `impl Pengingat for ...`:",
                    "      trait Pengingat {",
                    "          fn kirim(&self, pesan: &str) -> String;",
                    "      }",
                    "  3. Tipenya beda-beda, padahal harus masuk satu daftar, jadi pakai `dyn`:",
                    "      let semua: Vec<Box<dyn Pengingat>> = vec![Box::new(sms), Box::new(wa)];",
                    "      for p in &semua { println!(\"{}\", p.kirim(\"Antrean A-12 dipanggil\")); }",
                    "  4. Kasus pinggir: satu SMS standar muat 160 karakter teks biasa. Potong",
                    "     pesannya di `impl` milik `Sms` saja, dengan",
                    "     `pesan.chars().take(160).collect::<String>()`. `take(160)` mengambil",
                    "     160 karakter pertama. Hitungannya per karakter, jadi potongannya",
                    "     nggak jatuh di tengah huruf beraksen seperti kalau dipotong per",
                    "     byte. Saluran lain nggak ikut terpotong.",
                ]
            },
        ],
    },
    {
        "title": "15. Lifetime",
        "sections": [
            {
                "body": [
                    "Lifetime itu cara ngasih tahu compiler berapa lama sebuah referensi",
                    "boleh hidup. Referensi itu penunjuk ke data milik variabel lain, yang",
                    "ditulis pakai tanda &. Lifetime nggak mengubah apa pun waktu program",
                    "jalan. Semuanya cuma pemeriksaan waktu kompilasi.",
                    "",
                    "Kabar baiknya, sekitar 95% waktu kamu nggak perlu menulisnya. Compiler",
                    "menyimpulkannya sendiri lewat tiga aturan elision (aturan yang",
                    "membolehkan anotasinya dihilangkan):",
                    "  1. Setiap parameter referensi dapat lifetime sendiri.",
                    "  2. Kalau parameter referensinya cuma satu, nilai kembaliannya memakai",
                    "     lifetime itu.",
                    "  3. Kalau ada &self, nilai kembaliannya memakai lifetime self.",
                    "",
                    "Aturan nomor 3 yang bikin method hampir nggak pernah butuh anotasi.",
                    "",
                    "Kapan kamu harus menulisnya? Waktu sebuah fungsi menerima beberapa",
                    "referensi dan mengembalikan referensi. Di situ compiler nggak tahu",
                    "referensi yang dikembalikan berasal dari parameter yang mana.",
                    "",
                    "  fn lebih_panjang(a: &str, b: &str) -> &str   ERROR",
                    "",
                    "  fn lebih_panjang<'a>(a: &'a str, b: &'a str) -> &'a str",
                    "  {",
                    "      if a.len() > b.len() { a } else { b }",
                    "  }",
                    "",
                    "`'a` dibaca \"tick a\". Artinya: nilai kembaliannya hidup selama yang",
                    "lebih pendek di antara a dan b. Anotasi ini nggak memerintah compiler",
                    "dan nggak mengubah umur data. Dia janji, dan compiler yang memeriksa",
                    "janji itu.",
                    "",
                    "Lifetime khusus `'static` artinya hidup selama program jalan. Semua",
                    "literal string bertipe `&'static str`, karena teksnya tertanam di dalam",
                    "binari.",
                    "",
                    "Struct yang menyimpan referensi wajib diberi anotasi:",
                    "",
                    "  struct Kutipan<'a> {",
                    "      bagian: &'a str,",
                    "  }",
                    "",
                    "Artinya, sebuah Kutipan nggak boleh hidup lebih lama daripada teks yang",
                    "ditunjuknya. Kalau ini terasa merepotkan, sering kali jalan keluarnya",
                    "adalah menyimpan `String` (yang memiliki datanya sendiri) sebagai ganti",
                    "`&str`.",
                ]
            },
            {
                "heading": "Lifetime dalam praktik",
                "code": """// Dua referensi masuk, satu keluar: lifetime WAJIB ditulis.
fn lebih_panjang<'a>(a: &'a str, b: &'a str) -> &'a str {
    if a.len() > b.len() { a } else { b }
}

// Satu referensi masuk: elision menanganinya, tanpa anotasi.
fn kata_pertama(s: &str) -> &str {
    match s.find(' ') {
        Some(i) => &s[..i],
        None => s,
    }
}

// Struct yang menyimpan referensi wajib beranotasi.
struct Pengutip<'a> {
    sumber: &'a str,
}

impl<'a> Pengutip<'a> {
    fn baru(sumber: &'a str) -> Self {
        Pengutip { sumber }
    }

    // Aturan ke-3: &self, jadi kembaliannya ikut lifetime self.
    fn awal(&self, n: usize) -> &str {
        let batas = self.sumber.char_indices().nth(n).map(|(i, _)| i);
        match batas {
            Some(i) => &self.sumber[..i],
            None => self.sumber,
        }
    }
}

fn main() {
    let a = String::from("pemrograman");
    let b = String::from("rust");
    println!("lebih panjang : {}", lebih_panjang(&a, &b));

    let kalimat = "Rust menjamin keamanan memori";
    println!("kata pertama  : {}", kata_pertama(kalimat));

    let p = Pengutip::baru(kalimat);
    println!("10 huruf awal : {}", p.awal(10));
    println!("999 huruf awal: {}", p.awal(999));

    // Lifetime 'static: literal hidup selama program
    let tetap: &'static str = "aku hidup sampai akhir";
    println!("static        : {tetap}");

    // Scope: referensi tidak boleh hidup lebih lama dari datanya
    let hasil;
    {
        let sementara = String::from("pendek");
        hasil = lebih_panjang(&a, &sementara).to_string();
        // kalau `hasil` menyimpan &str, baris ini tidak akan dikompilasi
    }
    println!("hasil         : {hasil}");
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  lebih panjang : pemrograman",
                    "  kata pertama  : Rust",
                    "  10 huruf awal : Rust menja",
                    "  999 huruf awal: Rust menjamin keamanan memori",
                    "  static        : aku hidup sampai akhir",
                    "  hasil         : pemrograman",
                    "",
                    "Blok terakhir di contoh nunjukin cara paling umum keluar dari kebuntuan",
                    "lifetime: `.to_string()`. Karena `hasil` memiliki datanya sendiri, dia",
                    "nggak lagi bergantung pada umur `sementara`. Ongkosnya satu alokasi",
                    "memori. Gantinya, kodenya jauh lebih sederhana.",
                    "",
                    "Pesan lifetime yang paling sering muncul, dan cara membacanya:",
                    "",
                    "  'missing lifetime specifier'",
                    "    Fungsimu mengembalikan referensi, tapi compiler nggak tahu",
                    "    referensi itu berasal dari parameter yang mana. Tulis 'a di",
                    "    parameter yang jadi sumbernya.",
                    "",
                    "  'borrowed value does not live long enough'",
                    "    Datanya mati lebih dulu daripada referensinya. Pindahkan",
                    "    deklarasi datanya ke scope yang lebih luar, atau kembalikan nilai",
                    "    yang dimiliki.",
                    "",
                    "  'lifetime may not live long enough'",
                    "    Biasanya muncul di closure atau thread: sesuatu yang dipinjam",
                    "    dipakai di tempat yang hidup lebih lama. `move` pada closure sering",
                    "    jadi jawabannya.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Halaman checkout toko online punya aturan seperti \"kalau alamat kirim",
                    "kosong, pakai alamat rumah\". Fungsi yang memilih salah satu dari dua teks",
                    "lalu mengembalikannya tanpa menyalin butuh anotasi lifetime, karena",
                    "compiler perlu tahu hasilnya meminjam dari parameter yang mana.",
                    "",
                    "Kasus kecil: pembeli mengosongkan kolom alamat kirim, dan alamat rumahnya",
                    "\"Jl. Kenanga 7, Depok\". Fungsi harus mengembalikan alamat rumah tanpa",
                    "membuat String baru.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya dua `&str`, keluarannya salah satunya. Tanpa anotasi,",
                    "     compiler menolak dengan 'missing lifetime specifier', karena aturan",
                    "     elision nggak bisa memilih di antara dua parameter.",
                    "  2. Beri lifetime yang sama ke dua parameter dan hasilnya:",
                    "      fn alamat_kirim<'a>(kirim: &'a str, rumah: &'a str) -> &'a str {",
                    "          if kirim.trim().is_empty() { rumah } else { kirim }",
                    "      }",
                    "  3. Baca anotasinya: hasilnya boleh dipakai selama kedua alamat masih",
                    "     hidup. Untuk kolom kosong, hasilnya \"Jl. Kenanga 7, Depok\".",
                    "  4. Kasus pinggir: pembeli yang cuma mengetik beberapa spasi.",
                    "     `is_empty()` saja menganggap kolom itu berisi, padahal bagi manusia",
                    "     kolom itu kosong. `trim()` sebelum `is_empty()` menutup celah itu.",
                    "",
                    "Ingat: kalau hasilnya perlu disimpan lebih lama daripada kedua teks",
                    "asalnya, kembalikan `String` lewat `.to_string()`, dan anotasinya nggak",
                    "perlu lagi.",
                ]
            },
        ],
    },
    {
        "title": "16. Closure & Iterator",
        "sections": [
            {
                "body": [
                    "Closure itu fungsi tanpa nama yang bisa memakai variabel di sekitar",
                    "tempat dia ditulis. Istilahnya, closure menangkap variabel itu.",
                    "",
                    "  let tambah = |a, b| a + b;",
                    "  let kuadrat = |x: i32| -> i32 { x * x };",
                    "  let batas = 10;",
                    "  let kecil = |x: &i32| *x < batas;   menangkap batas",
                    "",
                    "Parameternya ditulis di antara dua garis tegak `| |`. Tipenya biasanya",
                    "nggak perlu ditulis, karena compiler bisa nebak. Ini beda dengan fungsi",
                    "biasa, yang tipe parameternya wajib ditulis.",
                    "",
                    "Ada tiga trait closure. Trait itu semacam daftar kemampuan yang dimiliki",
                    "sebuah tipe (dibahas di materi \"Trait\"). Di sini, trait-nya menentukan",
                    "apa yang boleh dilakukan closure terhadap variabel yang dia tangkap:",
                    "",
                    "  Fn        cuma membaca tangkapannya; bisa dipanggil",
                    "            berkali-kali",
                    "  FnMut     mengubah tangkapannya; berkali-kali juga",
                    "  FnOnce    MENGKONSUMSI tangkapannya; sekali saja",
                    "",
                    "Kamu nggak perlu milih sendiri. Compiler melihat apa yang dilakukan",
                    "closure-nya, lalu memilih yang paling longgar yang masih cocok.",
                    "",
                    "Kata kunci `move` memaksa closure mengambil kepemilikan variabel yang",
                    "dia tangkap. Ini wajib kalau closure-nya dikirim ke thread lain, atau",
                    "disimpan lebih lama daripada scope tempat variabelnya dibuat.",
                    "",
                    "Iterator itu rangkaian nilai yang bisa diambil satu per satu. Di Rust,",
                    "iterator itu malas: nggak ada yang dikerjakan sampai ada yang betul-betul",
                    "minta nilainya.",
                    "",
                    "  let v = vec![1, 2, 3, 4, 5];",
                    "  let hasil: Vec<i32> = v.iter()",
                    "      .filter(|x| **x % 2 == 0)",
                    "      .map(|x| x * 10)",
                    "      .collect();",
                    "",
                    "Kalau `.collect()` di akhir dihapus, nggak ada satu elemen pun yang",
                    "diproses. Compiler juga bakal ngasih peringatan bahwa iteratormu nggak",
                    "dipakai.",
                    "",
                    "Ada tiga cara bikin iterator dari koleksi. Bedanya ada di soal",
                    "kepemilikan:",
                    "  .iter()       memberi &T      koleksinya tetap milikmu",
                    "  .iter_mut()   memberi &mut T  boleh diubah",
                    "  .into_iter()  memberi T       koleksinya DIKONSUMSI",
                    "",
                    "Method iterator terbagi dua kelompok. Adaptor itu yang malas: dia",
                    "mengembalikan iterator lagi, jadi bisa dirangkai.",
                    "  map filter enumerate zip rev skip take chain flat_map",
                    "  filter_map take_while skip_while step_by peekable",
                    "",
                    "Konsumen itu yang memaksa iterator betul-betul jalan dan menghasilkan",
                    "nilai akhir:",
                    "  collect sum product count last nth fold reduce",
                    "  for_each any all find position max min max_by_key",
                ]
            },
            {
                "heading": "Rantai iterator",
                "code": """#[derive(Debug)]
struct Murid {
    nama: String,
    kelas: char,
    nilai: u32,
}

fn main() {
    let data = vec![
        Murid { nama: "Andi".into(),  kelas: 'A', nilai: 88 },
        Murid { nama: "Budi".into(),  kelas: 'B', nilai: 72 },
        Murid { nama: "Cici".into(),  kelas: 'A', nilai: 95 },
        Murid { nama: "Dedi".into(),  kelas: 'B', nilai: 64 },
        Murid { nama: "Euis".into(),  kelas: 'A', nilai: 79 },
    ];

    // Saring, urutkan, tampilkan
    let mut lulus: Vec<&Murid> = data.iter().filter(|m| m.nilai >= 75).collect();
    lulus.sort_by(|a, b| b.nilai.cmp(&a.nilai));
    for m in &lulus {
        println!("{:<6}{}  {}", m.nama, m.kelas, m.nilai);
    }

    // Ringkasan
    let total: u32 = data.iter().map(|m| m.nilai).sum();
    let rata = total as f64 / data.len() as f64;
    println!("---");
    println!("rata-rata : {rata:.2}");
    println!("tertinggi : {:?}", data.iter().map(|m| m.nilai).max());
    println!("lulus     : {}", data.iter().filter(|m| m.nilai >= 75).count());
    println!("ada <65?  : {}", data.iter().any(|m| m.nilai < 65));
    println!("semua >60?: {}", data.iter().all(|m| m.nilai > 60));

    // Ambil nama saja, gabungkan
    let nama: Vec<&str> = data.iter().map(|m| m.nama.as_str()).collect();
    println!("nama      : {}", nama.join(", "));

    // Closure yang menangkap variabel
    let batas = 80;
    let di_atas = |m: &&Murid| m.nilai > batas;
    println!("di atas {batas}: {}", data.iter().filter(di_atas).count());

    // fold: melipat jadi satu nilai
    let terpanjang = data
        .iter()
        .fold(String::new(), |akhir, m| {
            if m.nama.len() > akhir.len() { m.nama.clone() } else { akhir }
        });
    println!("nama terpanjang: {terpanjang}");
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Cici  A  95",
                    "  Andi  A  88",
                    "  Euis  A  79",
                    "  ---",
                    "  rata-rata : 79.60",
                    "  tertinggi : Some(95)",
                    "  lulus     : 3",
                    "  ada <65?  : true",
                    "  semua >60?: true",
                    "  nama      : Andi, Budi, Cici, Dedi, Euis",
                    "  di atas 80: 2",
                    "  nama terpanjang: Andi",
                    "",
                    "Rantai iterator di Rust sama cepatnya dengan perulangan for yang kamu",
                    "tulis sendiri. Compiler membongkar rantainya lewat inlining (menempelkan",
                    "isi fungsi langsung ke tempat pemanggilnya), dan nggak ada koleksi",
                    "perantara yang dibuat di tengah rantai. Di Rust ini disebut zero-cost",
                    "abstraction: kodenya lebih gampang dibaca, tapi programnya nggak jadi",
                    "lebih lambat.",
                    "",
                    "`\"Andi\".into()` memakai trait Into untuk mengubah &str jadi String.",
                    "Tulisannya lebih pendek daripada `String::from(...)`, dan sering banget",
                    "dipakai waktu mengisi struct.",
                    "",
                    "Kenapa ada bintang dua (`**x`)? `filter` memberi referensi ke tiap item",
                    "iterator. Padahal item dari `.iter()` sendiri udah berupa referensi,",
                    "jadi hasilnya referensi ke referensi. Kalau itu mengganggu, tambahkan",
                    "`.copied()` atau `.cloned()` di awal rantai, dan bintangnya hilang.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Dasbor admin toko online menampilkan angka seperti omzet hari ini dan",
                    "daftar pesanan yang belum dibayar. Angka-angka itu hasil menyaring dan",
                    "menjumlahkan daftar pesanan, persis pekerjaan rantai iterator `filter`,",
                    "`map`, dan `sum`.",
                    "",
                    "Kasus kecil: lima pesanan hari ini berupa tuple (nomor, total, lunas):",
                    "(1, 85000, true), (2, 150000, false), (3, 230000, true), (4, 40000,",
                    "false), dan (5, 120000, false). Pemilik minta omzet dari yang lunas, dan",
                    "nomor pesanan di atas Rp 100.000 yang belum lunas untuk ditagih.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pecah jadi dua pertanyaan, masing-masing satu rantai. Omzet: saring",
                    "     yang lunas, ambil totalnya, jumlahkan. Tagihan: saring, ambil",
                    "     nomornya, kumpulkan.",
                    "  2. Tulis rantainya. Batas tagihan disimpan di variabel, dan closure",
                    "     `filter` menangkapnya:",
                    "      let omzet: u32 = pesanan.iter().filter(|p| p.2).map(|p| p.1).sum();",
                    "      let batas = 100_000;",
                    "      let tagih: Vec<u32> = pesanan.iter()",
                    "          .filter(|p| !p.2 && p.1 > batas)",
                    "          .map(|p| p.0)",
                    "          .collect();",
                    "  3. Hasilnya omzet 315000 dan daftar tagihan [2, 5].",
                    "  4. Kasus pinggir: rata-rata pesanan lunas. Kalau hari itu belum ada",
                    "     yang lunas, `omzet / jumlah_lunas` membagi dengan nol, dan programnya",
                    "     panic. Hitung dulu jumlahnya dengan `count()`, lalu bagi hanya kalau",
                    "     hasilnya lebih dari nol.",
                ]
            },
        ],
    },
    {
        "title": "17. Modul, Crate & Cargo",
        "sections": [
            {
                "body": [
                    "Rust menyusun kode dalam tiga tingkat:",
                    "",
                    "  CRATE    satu unit kompilasi. Binary (punya main) atau",
                    "           library (dipakai crate lain).",
                    "  MODUL    pengelompokan di dalam crate.",
                    "  ITEM     fungsi, struct, trait, konstanta.",
                    "",
                    "Crate itu satu paket kode yang dikompilasi sekaligus. Bentuknya program",
                    "yang bisa dijalankan (binary) atau pustaka untuk dipakai crate lain",
                    "(library). Modul itu laci-laci di dalam crate. Item itu isi lacinya.",
                    "",
                    "Semua item bersifat privat kalau kamu nggak bilang apa-apa, artinya",
                    "cuma bisa dipakai dari dalam modulnya sendiri. Kata `pub` (public)",
                    "membukanya untuk luar.",
                    "",
                    "  mod matematika {",
                    "      pub fn tambah(a: i32, b: i32) -> i32 { a + b }",
                    "      fn rahasia() {}          tidak terlihat dari luar",
                    "",
                    "      pub mod lanjut {",
                    "          pub fn pangkat(a: i32, n: u32) -> i32 {",
                    "              a.pow(n)",
                    "          }",
                    "      }",
                    "  }",
                    "",
                    "  matematika::tambah(2, 3);",
                    "  matematika::lanjut::pangkat(2, 8);",
                    "",
                    "`use` bikin jalurnya lebih pendek, jadi kamu nggak perlu nulis nama",
                    "lengkapnya tiap kali:",
                    "  use matematika::lanjut::pangkat;",
                    "  use std::collections::{HashMap, HashSet};",
                    "  use std::io::{self, Write};",
                    "  use std::fmt::Result as HasilFormat;",
                    "",
                    "Jalur juga bisa ditulis relatif terhadap posisi sekarang:",
                    "  crate::  dari akar crate",
                    "  super::  satu tingkat ke atas",
                    "  self::   modul ini sendiri",
                    "",
                    "Cargo itu build tool (alat untuk mengompilasi proyek) sekaligus package",
                    "manager (alat untuk memasang pustaka orang lain):",
                    "",
                    "  cargo new nama            proyek binary baru",
                    "  cargo new nama --lib      proyek library",
                    "  cargo build               kompilasi (debug)",
                    "  cargo build --release     kompilasi teroptimasi",
                    "  cargo run                 kompilasi & jalankan",
                    "  cargo test                jalankan tes",
                    "  cargo check               periksa TANPA menghasilkan",
                    "                            binari -- jauh lebih cepat",
                    "  cargo add serde           tambah dependensi",
                    "  cargo fmt                 rapikan kode",
                    "  cargo clippy              linter, sangat berguna",
                    "  cargo doc --open          hasilkan dokumentasi",
                    "",
                    "`cargo check` yang paling sering dipakai selagi kamu nulis kode. Dia",
                    "menjalankan semua pemeriksaan tipe dan aturan pinjam, tapi melewatkan",
                    "tahap membuat binari, jadi hasilnya keluar jauh lebih cepat.",
                ]
            },
            {
                "heading": "Struktur proyek",
                "code": """proyekku/
├── Cargo.toml          nama, versi, dependensi
├── Cargo.lock          versi persis yang terpasang, jangan disunting
├── src/
│   ├── main.rs         crate binary, berisi fungsi main
│   ├── lib.rs          crate library, opsional
│   ├── model.rs        modul `model`
│   └── layanan/
│       ├── mod.rs      modul `layanan`
│       └── gudang.rs   modul `layanan::gudang`
├── tests/              tes integrasi, tiap berkas crate sendiri
└── benches/            tolok ukur"""
            },
            {
                "heading": "Cargo.toml",
                "code": """[package]
name = "proyekku"
version = "0.1.0"
edition = "2021"

[dependencies]
serde = { version = "1", features = ["derive"] }
rand = "0.8"

[dev-dependencies]
criterion = "0.5"

[profile.release]
opt-level = 3
lto = true"""
            },
            {
                "body": [
                    "Edition itu kumpulan aturan bahasa yang boleh berubah tanpa merusak",
                    "kode lama. Edition yang ada: 2015, 2018, 2021, dan 2024. Crate dengan",
                    "edition yang beda tetap bisa saling dipakai tanpa masalah, dan memang",
                    "untuk itu edition dibuat.",
                    "",
                    "Versi dependensi ditulis mengikuti aturan semver (major.minor.patch):",
                    "  \"1\"       apa pun 1.x.y, asal bukan 2.0",
                    "  \"1.2\"     apa pun 1.2.x ke atas, di bawah 2.0",
                    "  \"=1.2.3\"  persis itu saja",
                    "",
                    "Cargo.lock mencatat versi yang betul-betul terpasang. Untuk aplikasi,",
                    "berkas ini wajib dimasukkan ke git. Dengan begitu, build hari ini dan",
                    "build enam bulan lagi menghasilkan binari yang sama. Untuk library,",
                    "dulu biasanya nggak dimasukkan. Sejak 2023, panduan resmi Cargo",
                    "menyerahkan keputusannya ke pemilik proyek, dan banyak library sekarang",
                    "ikut memasukkannya.",
                    "",
                    "Dokumentasi ditulis dengan tiga garis miring, dan boleh pakai format",
                    "Markdown:",
                    "",
                    "  /// Menjumlahkan dua bilangan.",
                    "  ///",
                    "  /// # Contoh",
                    "  /// ```",
                    "  /// assert_eq!(tambah(2, 3), 5);",
                    "  /// ```",
                    "  pub fn tambah(a: i32, b: i32) -> i32 { a + b }",
                    "",
                    "Yang menarik: contoh di dalam blok kode itu ikut dijalankan oleh",
                    "`cargo test`. Kalau dokumentasinya udah nggak sesuai dengan kodenya,",
                    "tesnya gagal. Banyak bahasa lain nggak punya fitur ini.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Program kasir yang terus ditambah fiturnya bisa tumbuh jadi ribuan baris,",
                    "dan timnya membagi kode per tugas: hitung harga, cetak struk, simpan data.",
                    "Di Rust pembagian itu dikerjakan dengan modul, dan `pub` menentukan fungsi",
                    "mana yang boleh dipanggil dari luar modulnya.",
                    "",
                    "Kasus kecil: `main.rs` milik sebuah program kasir udah 600 baris, dan",
                    "aturan harga member (diskon 5%) tercampur dengan kode cetak struk.",
                    "Pindahkan aturan harga ke modulnya sendiri.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kelompokkan fungsi menurut tugasnya. Semua yang menghitung harga",
                    "     pindah ke berkas `src/harga.rs`.",
                    "  2. Daftarkan modulnya di `main.rs` dengan baris `mod harga;`, lalu",
                    "     panggil fungsinya lewat jalur, misalnya `harga::harga_member(80_000)`.",
                    "  3. Beri `pub` hanya pada fungsi yang dipanggil dari luar. Fungsi",
                    "     pembantu tetap privat:",
                    "      // src/harga.rs",
                    "      pub fn harga_member(n: u32) -> u32 {",
                    "          n - diskon(n)",
                    "      }",
                    "      fn diskon(n: u32) -> u32 { n * 5 / 100 }",
                    "     Untuk 80000, hasilnya 76000.",
                    "  4. Jalankan `cargo check` tiap kali selesai memindahkan satu fungsi.",
                    "     Pesan 'function `diskon` is private' berarti ada kode di luar modul",
                    "     yang masih memanggil pembantu itu. Putuskan apakah ia memang perlu",
                    "     `pub`, atau pemanggilnya yang ikut pindah ke modul harga.",
                    "",
                    "Ingat: untuk program seperti ini, `Cargo.lock` ikut dimasukkan ke git,",
                    "supaya komputer kasir di cabang lain dikompilasi dengan versi crate yang",
                    "sama.",
                ]
            },
        ],
    },
    {
        "title": "18. Smart Pointer: Box, Rc & RefCell",
        "sections": [
            {
                "body": [
                    "Smart pointer itu tipe yang dipakai seperti referensi, tapi punya",
                    "kemampuan tambahan. Ada tiga yang paling sering dipakai.",
                    "",
                    "Box<T> menaruh data di heap.",
                    "",
                    "  let b = Box::new(5);",
                    "  println!(\"{}\", *b);",
                    "",
                    "Alasan memakainya ada tiga:",
                    "  1. Tipe rekursif, yaitu tipe yang di dalamnya memuat dirinya sendiri.",
                    "     Tanpa Box, ukurannya nggak terhingga:",
                    "       enum Daftar { Isi(i32, Box<Daftar>), Habis }",
                    "  2. Memindahkan data besar tanpa menyalinnya.",
                    "  3. Menyimpan `dyn Trait`, yang ukurannya belum diketahui waktu",
                    "     kompilasi.",
                    "",
                    "Rc<T> (Reference Counted) memungkinkan satu data punya beberapa pemilik.",
                    "Rc menghitung ada berapa pemilik yang masih memegang datanya.",
                    "",
                    "  use std::rc::Rc;",
                    "  let a = Rc::new(vec![1, 2, 3]);",
                    "  let b = Rc::clone(&a);       hitungan naik jadi 2",
                    "  Rc::strong_count(&a)         2",
                    "",
                    "Rc melonggarkan aturan \"satu pemilik\". Datanya baru dilepas waktu",
                    "pemilik terakhirnya hilang. `Rc::clone` nggak menyalin datanya. Dia",
                    "cuma menaikkan hitungan, jadi murah.",
                    "",
                    "Rc cuma boleh dipakai di satu thread. Versi untuk banyak thread namanya",
                    "`Arc` (Atomic Rc). Arc sedikit lebih lambat, karena hitungannya harus",
                    "aman walaupun diubah beberapa thread sekaligus.",
                    "",
                    "RefCell<T> memindahkan pemeriksaan aturan pinjam ke waktu program",
                    "jalan (runtime).",
                    "",
                    "  use std::cell::RefCell;",
                    "  let c = RefCell::new(5);",
                    "  *c.borrow_mut() += 1;",
                    "  println!(\"{}\", c.borrow());",
                    "",
                    "Aturannya tetap sama: banyak pembaca, atau satu pengubah. Bedanya,",
                    "pelanggaran nggak lagi jadi error kompilasi. Programnya panic waktu",
                    "jalan. Ini pertukaran yang disengaja. RefCell dipakai kalau kamu tahu",
                    "kodemu benar, tapi compiler nggak bisa membuktikannya.",
                    "",
                    "Gabungan `Rc<RefCell<T>>` dipakai untuk data yang dimiliki bersama dan",
                    "juga bisa diubah. Contoh pemakaiannya: graf, pohon yang tiap anaknya",
                    "punya tautan ke induk, dan pola observer.",
                ]
            },
            {
                "heading": "Box untuk tipe rekursif, Rc untuk berbagi",
                "code": """use std::cell::RefCell;
use std::rc::Rc;

// Tanpa Box, ukuran Daftar tak terhingga: compiler menolaknya.
#[derive(Debug)]
enum Daftar {
    Isi(i32, Box<Daftar>),
    Habis,
}

use Daftar::{Habis, Isi};

fn jumlah(d: &Daftar) -> i32 {
    match d {
        Isi(n, sisa) => n + jumlah(sisa),
        Habis => 0,
    }
}

fn main() {
    let rantai = Isi(1, Box::new(Isi(2, Box::new(Isi(3, Box::new(Habis))))));
    println!("rantai  : {rantai:?}");
    println!("jumlah  : {}", jumlah(&rantai));

    // Rc: banyak pemilik untuk data yang sama
    let bersama = Rc::new(vec![10, 20, 30]);
    println!("hitungan: {}", Rc::strong_count(&bersama));
    {
        let _a = Rc::clone(&bersama);
        let _b = Rc::clone(&bersama);
        println!("di blok : {}", Rc::strong_count(&bersama));
    }
    println!("sesudah : {}", Rc::strong_count(&bersama));

    // Rc<RefCell<T>>: dimiliki bersama DAN bisa diubah
    let catatan = Rc::new(RefCell::new(Vec::<String>::new()));

    let penulis_a = Rc::clone(&catatan);
    penulis_a.borrow_mut().push("dari A".to_string());

    let penulis_b = Rc::clone(&catatan);
    penulis_b.borrow_mut().push("dari B".to_string());

    catatan.borrow_mut().push("dari utama".to_string());

    println!("catatan : {:?}", catatan.borrow());
    println!("pemilik : {}", Rc::strong_count(&catatan));
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  rantai  : Isi(1, Isi(2, Isi(3, Habis)))",
                    "  jumlah  : 6",
                    "  hitungan: 1",
                    "  di blok : 3",
                    "  sesudah : 1",
                    "  catatan : [\"dari A\", \"dari B\", \"dari utama\"]",
                    "  pemilik : 3",
                    "",
                    "Lihat hitungan Rc: naik jadi 3 di dalam blok, lalu turun lagi jadi 1",
                    "begitu bloknya selesai. Begitulah cara kerjanya. Datanya dilepas waktu",
                    "hitungannya sampai nol.",
                    "",
                    "Jebakan: Rc bisa bocor. Kalau dua objek saling menunjuk pakai Rc,",
                    "hitungan keduanya nggak pernah sampai nol, dan memorinya nggak pernah",
                    "dilepas. Ini salah satu cara memori bisa bocor di Rust aman; jaminan",
                    "Rust itu memori aman dipakai, belum tentu semuanya dilepas. Pemutusnya",
                    "`Weak<T>`, referensi yang nggak menaikkan hitungan.",
                    "",
                    "Pola yang biasa dipakai: anak memegang `Rc` ke datanya, dan tautan",
                    "balik ke induk pakai `Weak`.",
                    "",
                    "Kapan pakai yang mana:",
                    "  &T                 hampir selalu. Mulai dari sini.",
                    "  Box<T>             perlu heap, rekursif, atau dyn Trait",
                    "  Rc<T>              beberapa pemilik, satu thread",
                    "  Arc<T>             beberapa pemilik, antar thread",
                    "  RefCell<T>         perlu mengubah lewat &",
                    "  Rc<RefCell<T>>     dimiliki bersama dan bisa diubah",
                    "  Arc<Mutex<T>>      sama, tapi antar thread",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kadang satu data dipegang beberapa bagian program sekaligus, misalnya",
                    "stok barang yang dibaca dan dikurangi oleh dua objek kasir di satu",
                    "aplikasi toko. Referensi biasa nggak cukup, karena keduanya perlu",
                    "mengubah data yang sama dan nggak ada satu pemilik yang jelas. Untuk",
                    "program satu thread, jawabannya `Rc<RefCell<T>>`.",
                    "",
                    "Kasus kecil: stok kopi sachet ada 20. Kasir A menjual 3, kasir B menjual",
                    "5, dan keduanya harus melihat sisa yang sama.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali masalahnya: dua pemilik sama-sama mengubah satu nilai. `&mut`",
                    "     cuma boleh satu pada satu waktu, jadi perlu kepemilikan bersama",
                    "     (`Rc`) dan izin mengubah lewat pinjaman bersama (`RefCell`).",
                    "  2. Bungkus stoknya sekali, lalu bagikan dengan `Rc::clone`:",
                    "      let stok = Rc::new(RefCell::new(20));",
                    "      let kasir_a = Rc::clone(&stok);",
                    "      let kasir_b = Rc::clone(&stok);",
                    "      *kasir_a.borrow_mut() -= 3;",
                    "      *kasir_b.borrow_mut() -= 5;",
                    "      println!(\"sisa {}\", stok.borrow());",
                    "  3. Hasilnya \"sisa 12\". `Rc::clone` nggak menyalin angka 20; ketiga",
                    "     variabel menunjuk satu stok yang sama.",
                    "  4. Kasus pinggir: jangan memegang `borrow()` sambil memanggil",
                    "     `borrow_mut()`. Kode yang menyimpan `let lihat = stok.borrow();`",
                    "     lalu mengurangi stok sebelum `lihat` selesai dipakai lolos",
                    "     kompilasi, tapi panic waktu jalan karena RefCell-nya masih dipinjam.",
                    "",
                    "Ingat: kalau kasirnya jalan di thread berbeda, ganti dengan",
                    "`Arc<Mutex<T>>`. Rc nggak boleh dikirim ke thread lain.",
                ]
            },
        ],
    },
    {
        "title": "19. Concurrency: Thread & Channel",
        "sections": [
            {
                "body": [
                    "Concurrency artinya beberapa pekerjaan jalan bersamaan, biasanya di",
                    "beberapa thread. Thread itu jalur kerja di dalam satu program.",
                    "",
                    "Rust menjuluki pendekatannya fearless concurrency, artinya kamu nggak",
                    "perlu takut nulis kode yang jalan bersamaan. Maksudnya harfiah: data",
                    "race jadi error kompilasi. Di bahasa lain, data race sering baru muncul",
                    "sekali seminggu di server produksi.",
                    "",
                    "Yang menjaga ini dua trait penanda:",
                    "  Send   aman DIPINDAHKAN ke thread lain",
                    "  Sync   aman DIAKSES dari beberapa thread lewat &",
                    "",
                    "Compiler menentukan keduanya sendiri. Rc nggak termasuk Send, karena",
                    "hitungannya nggak atomik (nggak aman diubah dua thread sekaligus). Jadi",
                    "kalau kamu mencoba mengirim Rc ke thread lain, kompilasinya gagal. Di",
                    "C++, kesalahan yang sama menghasilkan kerusakan memori yang muncul",
                    "acak.",
                    "",
                    "Cara bikin thread:",
                    "  use std::thread;",
                    "",
                    "  let h = thread::spawn(|| {",
                    "      println!(\"dari thread\");",
                    "  });",
                    "  h.join().unwrap();      tunggu selesai",
                    "",
                    "Closure yang dikirim ke thread hampir selalu butuh `move`, supaya dia",
                    "memiliki data yang dipakainya. Alasannya, compiler nggak bisa",
                    "membuktikan thread-nya selesai sebelum data itu dilepas.",
                    "",
                    "Channel itu saluran untuk berkirim pesan antar thread:",
                    "",
                    "  use std::sync::mpsc;",
                    "  let (kirim, terima) = mpsc::channel();",
                    "  kirim.send(nilai).unwrap();",
                    "  let x = terima.recv().unwrap();",
                    "",
                    "mpsc singkatan dari multiple producer, single consumer: pengirimnya",
                    "boleh banyak (cukup di-clone), penerimanya cuma satu.",
                    "",
                    "Prinsip yang dipegang: \"jangan berkomunikasi dengan berbagi memori;",
                    "berbagilah memori dengan berkomunikasi.\"",
                    "",
                    "Kalau data memang harus dipakai bersama, pakai Mutex. Mutex itu kunci",
                    "yang memastikan cuma satu thread yang memegang data pada satu waktu:",
                    "",
                    "  use std::sync::{Arc, Mutex};",
                    "  let data = Arc::new(Mutex::new(0));",
                    "  *data.lock().unwrap() += 1;",
                    "",
                    "Di Rust, Mutex membungkus datanya. Data itu nggak bisa disentuh tanpa",
                    "membuka kuncinya lebih dulu. Lupa mengunci, kesalahan yang paling umum",
                    "di C dan Java, jadi nggak mungkin terjadi karena tipenya melarang.",
                ]
            },
            {
                "heading": "Thread, channel, dan mutex",
                "code": """use std::sync::mpsc;
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
    // --- Thread dengan hasil kembalian ---
    let mut tugas = Vec::new();
    for i in 1..=4 {
        tugas.push(thread::spawn(move || {
            let hasil: u64 = (1..=i as u64 * 1000).sum();
            (i, hasil)
        }));
    }

    // Kumpulkan lalu URUTKAN: urutan selesainya thread tidak pasti,
    // dan itu sifat concurrency, bukan bug yang bisa diperbaiki.
    let mut hasil: Vec<(i32, u64)> = tugas
        .into_iter()
        .map(|h| h.join().unwrap())
        .collect();
    hasil.sort();
    for (i, n) in &hasil {
        println!("tugas {i}: {n}");
    }

    // --- Channel ---
    let (kirim, terima) = mpsc::channel();
    for nama in ["A", "B", "C"] {
        let k = kirim.clone();
        thread::spawn(move || {
            k.send(format!("pesan dari {nama}")).unwrap();
        });
    }
    drop(kirim);   // tanpa ini, perulangan di bawah tidak pernah berhenti

    let mut pesan: Vec<String> = terima.iter().collect();
    pesan.sort();
    for p in &pesan {
        println!("{p}");
    }

    // --- Mutex + Arc ---
    let hitungan = Arc::new(Mutex::new(0));
    let mut pekerja = Vec::new();
    for _ in 0..8 {
        let h = Arc::clone(&hitungan);
        pekerja.push(thread::spawn(move || {
            for _ in 0..1000 {
                *h.lock().unwrap() += 1;
            }
        }));
    }
    for p in pekerja {
        p.join().unwrap();
    }
    println!("hitungan akhir: {}", *hitungan.lock().unwrap());
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tugas 1: 500500",
                    "  tugas 2: 2001000",
                    "  tugas 3: 4501500",
                    "  tugas 4: 8002000",
                    "  pesan dari A",
                    "  pesan dari B",
                    "  pesan dari C",
                    "  hitungan akhir: 8000",
                    "",
                    "Ada dua hal di kode itu yang wajib kamu perhatikan. Dua-duanya soal",
                    "determinisme, artinya program yang sama selalu menghasilkan keluaran",
                    "yang sama:",
                    "  1. Hasilnya diurutkan dulu sebelum dicetak. Urutan selesainya thread",
                    "     memang nggak pasti. Kalau keluarannya berubah tiap kali program",
                    "     dijalankan, program itu nggak bisa diuji.",
                    "  2. `drop(kirim)` wajib ada. Perulangan `terima.iter()` baru berhenti",
                    "     waktu semua pengirim udah hilang. Pengirim yang asli masih hidup",
                    "     di main, jadi tanpa drop programnya menunggu selamanya. Bug ini",
                    "     nggak menghasilkan error apa pun. Programnya cuma diam.",
                    "",
                    "Hitungan akhir 8000 dijamin pas. Di Java atau C tanpa kunci, angka itu",
                    "bakal meleset acak. Alasannya, `+= 1` itu terdiri dari tiga langkah",
                    "(baca, tambah, tulis), dan thread lain bisa menyela di antaranya. Rust",
                    "nggak mengizinkan kamu nulis itu tanpa lock.",
                    "",
                    "Untuk pekerjaan yang lebih banyak menunggu (jaringan, berkas)",
                    "ketimbang menghitung, programmer Rust pakai async/await dengan runtime",
                    "seperti tokio. Bentuk kodenya mirip, tapi ribuan tugas bisa jalan di",
                    "atas segelintir thread.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Toko yang punya beberapa cabang biasanya merekap penjualan tiap cabang",
                    "lalu menggabungkannya. Rekap tiap cabang nggak saling bergantung, jadi",
                    "bisa dikerjakan di thread terpisah, dan hasilnya dikirim ke thread utama",
                    "lewat channel.",
                    "",
                    "Kasus kecil: penjualan hari ini di Bogor 120000, 75000, dan 210000; di",
                    "Depok 98000 dan 150000; di Bekasi 300000, 45000, 60000, dan 15000. Hitung",
                    "total per cabang secara bersamaan, lalu total semuanya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pastikan pekerjaannya memang bisa dipisah. Tiap cabang cuma butuh",
                    "     datanya sendiri, jadi tiap thread menerima datanya lewat `move` dan",
                    "     nggak berbagi apa pun dengan thread lain.",
                    "  2. Buat channel. Di dalam perulangan per cabang, beri tiap thread",
                    "     salinan pengirim:",
                    "      let k = kirim.clone();",
                    "      thread::spawn(move || {",
                    "          let total: u32 = data.iter().sum();",
                    "          k.send((cabang, total)).unwrap();",
                    "      });",
                    "  3. Sesudah perulangan, panggil `drop(kirim)`, kumpulkan `terima.iter()`",
                    "     ke Vec, lalu urutkan. Hasilnya Bekasi 420000, Bogor 405000, dan Depok",
                    "     248000, dengan total semuanya 1073000.",
                    "  4. Periksa dua jebakan dari materi ini. Tanpa `drop(kirim)`, programnya",
                    "     menunggu selamanya. Tanpa pengurutan, urutan cabang berubah-ubah",
                    "     tiap dijalankan, tergantung thread mana yang selesai duluan.",
                ]
            },
        ],
    },
    {
        "title": "20. Testing & Dokumentasi",
        "sections": [
            {
                "body": [
                    "Di Rust, testing udah jadi bagian dari bahasanya dan dari cargo. Kamu",
                    "nggak perlu memasang pustaka tambahan.",
                    "",
                    "  #[cfg(test)]",
                    "  mod tes {",
                    "      use super::*;",
                    "",
                    "      #[test]",
                    "      fn tambah_dua_positif() {",
                    "          assert_eq!(tambah(2, 3), 5);",
                    "      }",
                    "  }",
                    "",
                    "`#[cfg(test)]` artinya modul itu cuma dikompilasi waktu kamu",
                    "menjalankan `cargo test`. Modul itu nggak ikut masuk ke binari rilis,",
                    "jadi nggak nambah beban sama sekali.",
                    "",
                    "`use super::*;` mengambil semua isi modul induknya, termasuk yang",
                    "privat. Jadi tes di Rust boleh menguji fungsi internal. Di kebanyakan",
                    "bahasa, hal ini nggak bisa dilakukan semudah itu.",
                    "",
                    "Makro assert, untuk memastikan sesuatu bernilai benar:",
                    "  assert!(kondisi)",
                    "  assert!(kondisi, \"pesan {}\", x)",
                    "  assert_eq!(kiri, kanan)",
                    "  assert_ne!(kiri, kanan)",
                    "",
                    "Kalau gagal, assert_eq! mencetak dua nilainya, jadi kamu langsung tahu",
                    "bedanya di mana. Itu jauh lebih membantu daripada pesan 'assertion",
                    "failed' saja.",
                    "",
                    "Atribut tambahan:",
                    "  #[should_panic]                  tes lulus kalau panic",
                    "  #[should_panic(expected = \"..\")] panic dengan pesan itu",
                    "  #[ignore]                        dilewati kecuali diminta",
                    "",
                    "Tes yang mengembalikan Result boleh pakai `?`:",
                    "  #[test]",
                    "  fn parse_benar() -> Result<(), String> { ... }",
                    "",
                    "Cara menjalankan:",
                    "  cargo test",
                    "  cargo test nama_tes          hanya yang namanya cocok",
                    "  cargo test -- --nocapture    tampilkan println!",
                    "  cargo test -- --test-threads=1   berurutan",
                    "  cargo test -- --ignored      justru yang di-ignore",
                    "",
                    "Tes di folder src/ disebut tes unit, dan boleh menyentuh yang privat.",
                    "Tes di folder tests/ disebut tes integrasi. Tiap berkasnya jadi crate",
                    "sendiri yang cuma bisa melihat bagian publik (API publik).",
                ]
            },
            {
                "heading": "Modul lengkap dengan tesnya",
                "code": """/// Menghitung grade dari nilai 0..100.
///
/// # Panics
/// Panic kalau nilai di luar 0..=100.
///
/// # Contoh
/// ```
/// assert_eq!(grade(85), 'A');
/// ```
pub fn grade(nilai: u32) -> char {
    assert!(nilai <= 100, "nilai harus 0..=100, dapat {nilai}");
    match nilai {
        85..=100 => 'A',
        75..=84 => 'B',
        60..=74 => 'C',
        _ => 'D',
    }
}

/// Rata-rata sebuah slice. None kalau slice-nya kosong.
pub fn rata_rata(data: &[u32]) -> Option<f64> {
    if data.is_empty() {
        return None;
    }
    let total: u32 = data.iter().sum();
    Some(total as f64 / data.len() as f64)
}

#[cfg(test)]
mod tes {
    use super::*;

    #[test]
    fn grade_di_batas_bawah_tiap_huruf() {
        // Menguji tepat DI BATAS: di situlah >= versus > salah ketik.
        assert_eq!(grade(85), 'A');
        assert_eq!(grade(84), 'B');
        assert_eq!(grade(75), 'B');
        assert_eq!(grade(74), 'C');
        assert_eq!(grade(60), 'C');
        assert_eq!(grade(59), 'D');
        assert_eq!(grade(0), 'D');
    }

    #[test]
    #[should_panic(expected = "nilai harus")]
    fn grade_menolak_di_atas_seratus() {
        grade(101);
    }

    #[test]
    fn rata_rata_kosong_menghasilkan_none() {
        assert_eq!(rata_rata(&[]), None);
    }

    #[test]
    fn rata_rata_biasa() {
        assert_eq!(rata_rata(&[80, 90, 100]), Some(90.0));
    }
}

fn main() {
    for n in [92, 84, 60, 12] {
        println!("{n:3} -> {}", grade(n));
    }
    println!("rata-rata : {:?}", rata_rata(&[80, 90, 100]));
    println!("kosong    : {:?}", rata_rata(&[]));
    println!();
    println!("Jalankan `cargo test` untuk menjalankan modul tes di atas.");
}"""
            },
            {
                "body": [
                    "Keluaran saat dijalankan biasa:",
                    "   92 -> A",
                    "   84 -> B",
                    "   60 -> C",
                    "   12 -> D",
                    "  rata-rata : Some(90.0)",
                    "  kosong    : None",
                    "",
                    "  Jalankan `cargo test` untuk menjalankan modul tes di atas.",
                    "",
                    "Coba lihat nilai yang dipilih di tes: 85 dan 84, 75 dan 74, 60 dan 59.",
                    "Nilai tepat di batas itu yang paling berguna untuk diuji, karena di",
                    "situ salah ketik `..=` dengan `..`, atau `>=` dengan `>`, biasanya",
                    "terjadi. Nilai di tengah rentang hampir nggak pernah menemukan bug.",
                    "",
                    "Blok ``` di dalam komentar dokumentasi disebut doctest. `cargo test`",
                    "betul-betul mengompilasi dan menjalankannya. Akibatnya, contoh di",
                    "dokumentasi nggak bisa basi tanpa ketahuan. Begitu API-nya berubah,",
                    "dokumentasinya gagal sebagai tes. Nggak semua bahasa punya fitur ini.",
                    "",
                    "Untuk mengukur berapa banyak kode yang tersentuh tes:",
                    "  cargo install cargo-llvm-cov",
                    "  cargo llvm-cov --html",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kesalahan di aturan denda, diskon, atau potongan gaji langsung terasa di",
                    "uang orang, dan aturannya sering berubah. Tes otomatis memastikan aturan",
                    "yang lama tetap benar setiap kali ada yang menyunting kodenya, misalnya",
                    "di aplikasi perpustakaan sekolah atau sistem penggajian.",
                    "",
                    "Kasus kecil: perpustakaan sekolah mendenda Rp 500 per hari telat, paling",
                    "banyak Rp 10.000. Fungsinya ditulis",
                    "`fn denda(hari: u32) -> u32 { (hari * 500).min(10_000) }`, dengan",
                    "`.min(10_000)` mengambil yang lebih kecil. Nilai apa saja yang perlu",
                    "diuji?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis aturannya jadi tabel hari dan denda, lalu cari titik tempat",
                    "     perilakunya berubah. Di sini titiknya hari ke-20, saat denda",
                    "     menyentuh Rp 10.000.",
                    "  2. Pilih nilai di sekitar titik itu: 1, 20, dan 21. Hari 0 juga layak",
                    "     diuji, karena siswa yang tepat waktu nggak boleh didenda.",
                    "  3. Tulis tesnya di modul `#[cfg(test)]`:",
                    "      #[test]",
                    "      fn denda_di_batas() {",
                    "          assert_eq!(denda(1), 500);",
                    "          assert_eq!(denda(20), 10_000);",
                    "          assert_eq!(denda(21), 10_000);",
                    "      }",
                    "  4. Jalankan `cargo test`. Kalau suatu hari ada yang menghapus",
                    "     `.min(10_000)`, tes hari ke-21 gagal, dan `assert_eq!` mencetak left",
                    "     10500 dan right 10000. Letak salahnya langsung kelihatan.",
                ]
            },
        ],
    },
    {
        "title": "21. Trait Standar & Konversi",
        "sections": [
            {
                "body": [
                    "Pustaka standar Rust menyediakan sejumlah trait yang menyambungkan tipe",
                    "buatanmu ke fitur-fitur bawaan. Mengimplementasi satu trait sering",
                    "bikin tipemu langsung bisa dipakai di banyak tempat.",
                    "",
                    "From dan Into dipakai untuk konversi antar tipe:",
                    "",
                    "  impl From<u32> for Nilai {",
                    "      fn from(n: u32) -> Self { Nilai(n) }",
                    "  }",
                    "",
                    "Dengan itu kamu dapat `Nilai::from(80)` dan `80.into()` sekaligus,",
                    "karena Into dibuatkan otomatis dari From. Jadi cukup tulis From, dan",
                    "jangan pernah mengimplementasi Into langsung.",
                    "",
                    "Untuk konversi yang bisa gagal, pasangannya TryFrom dan TryInto. Hasil",
                    "keduanya berupa Result.",
                    "",
                    "Default memberi nilai bawaan:",
                    "  #[derive(Default)]",
                    "  struct Setelan { tebal: bool, ukuran: u32 }",
                    "",
                    "  let s = Setelan::default();",
                    "  let s = Setelan { ukuran: 14, ..Default::default() };",
                    "",
                    "Baris terakhir itu pola yang sering dipakai: isi yang kamu pedulikan,",
                    "sisanya pakai nilai bawaan.",
                    "",
                    "Display dan Debug sama-sama untuk mencetak, tapi pembacanya beda:",
                    "  Debug    {:?}  untuk PROGRAMMER. Bisa di-derive.",
                    "  Display  {}    untuk PENGGUNA. Harus ditulis tangan,",
                    "                 karena tidak ada yang bisa menebak",
                    "                 bagaimana tipemu sebaiknya dibaca orang.",
                    "",
                    "Drop menentukan apa yang terjadi waktu sebuah nilai dilepas:",
                    "  impl Drop for Koneksi {",
                    "      fn drop(&mut self) { println!(\"koneksi ditutup\"); }",
                    "  }",
                    "",
                    "Drop itu padanan destructor di C++. Rust memanggilnya otomatis waktu",
                    "scope selesai, dan juga waktu program panic. Pengecualiannya ada,",
                    "misalnya nilai yang sengaja dilupakan dengan `std::mem::forget`, atau",
                    "Rc yang saling menunjuk. Kamu nggak bisa memanggil `.drop()` langsung;",
                    "pakai `drop(x)`.",
                    "",
                    "Trait untuk membandingkan, dan saling ketergantungannya:",
                    "  PartialEq  ==  dan  !=",
                    "  Eq         PartialEq + refleksif (butuh PartialEq)",
                    "  PartialOrd <  >  <=  >=  (butuh PartialEq)",
                    "  Ord        urutan total (butuh Eq + PartialOrd)",
                    "",
                    "f64 cuma punya PartialOrd, nggak punya Ord. Alasannya NaN (Not a",
                    "Number, hasil hitungan seperti 0.0 / 0.0) nggak bisa dibandingkan",
                    "dengan apa pun, termasuk dengan dirinya sendiri. Karena itu",
                    "`vec_f64.sort()` nggak bisa dikompilasi, dan kamu harus nulis",
                    "`sort_by(|a, b| a.partial_cmp(b).unwrap())`.",
                ]
            },
            {
                "heading": "Mengimplementasi trait standar",
                "code": """use std::fmt;

#[derive(Debug, Clone, PartialEq, Eq, PartialOrd, Ord, Default)]
struct Versi {
    mayor: u32,
    minor: u32,
    tambal: u32,
}

impl Versi {
    fn baru(mayor: u32, minor: u32, tambal: u32) -> Self {
        Versi { mayor, minor, tambal }
    }
}

// Display: bagaimana manusia membacanya
impl fmt::Display for Versi {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "v{}.{}.{}", self.mayor, self.minor, self.tambal)
    }
}

// From: konversi yang tidak pernah gagal
impl From<(u32, u32, u32)> for Versi {
    fn from(t: (u32, u32, u32)) -> Self {
        Versi::baru(t.0, t.1, t.2)
    }
}

// TryFrom: konversi yang BISA gagal
impl TryFrom<&str> for Versi {
    type Error = String;

    fn try_from(s: &str) -> Result<Self, Self::Error> {
        let bagian: Vec<&str> = s.trim_start_matches('v').split('.').collect();
        if bagian.len() != 3 {
            return Err(format!("format salah: {s}"));
        }
        let angka: Result<Vec<u32>, _> = bagian.iter().map(|b| b.parse()).collect();
        match angka {
            Ok(a) => Ok(Versi::baru(a[0], a[1], a[2])),
            Err(_) => Err(format!("bukan angka: {s}")),
        }
    }
}

fn main() {
    let a = Versi::baru(1, 4, 2);
    let b: Versi = (1, 10, 0).into();
    let c = Versi::default();

    println!("display : {a}  {b}  {c}");
    println!("debug   : {a:?}");
    println!("a < b?  : {}", a < b);

    let mut daftar = vec![Versi::baru(2, 0, 0), a.clone(), b.clone(), c.clone()];
    daftar.sort();
    let teks: Vec<String> = daftar.iter().map(|v| v.to_string()).collect();
    println!("terurut : {}", teks.join(" "));

    for s in ["v1.2.3", "2.0", "v1.x.3"] {
        match Versi::try_from(s) {
            Ok(v) => println!("parse {s:<8} -> {v}"),
            Err(e) => println!("parse {s:<8} -> galat: {e}"),
        }
    }
}"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  display : v1.4.2  v1.10.0  v0.0.0",
                    "  debug   : Versi { mayor: 1, minor: 4, tambal: 2 }",
                    "  a < b?  : true",
                    "  terurut : v0.0.0 v1.4.2 v1.10.0 v2.0.0",
                    "  parse v1.2.3   -> v1.2.3",
                    "  parse 2.0      -> galat: format salah: 2.0",
                    "  parse v1.x.3   -> galat: bukan angka: v1.x.3",
                    "",
                    "`#[derive(Ord)]` mengurutkan berdasarkan field, sesuai urutan field itu",
                    "ditulis: mayor dulu, lalu minor, lalu tambal. Karena itu v1.10.0 benar",
                    "ada sesudah v1.4.2. Kalau versinya dibandingkan sebagai teks, urutannya",
                    "bakal salah.",
                    "",
                    "Trik yang layak diingat: `Result<Vec<u32>, _>` sebagai tipe tujuan",
                    "`collect()`. Iterator yang isinya Result bisa dikumpulkan jadi satu",
                    "Result yang isinya Vec. Kalau ada satu aja yang Err, hasil akhirnya",
                    "Err. Satu baris ini menggantikan perulangan yang ngecek tiap elemen.",
                    "",
                    "Biasakan nulis `#[derive(Debug)]` di hampir semua tipe. Di build rilis",
                    "ongkosnya nol. Tanpa itu, kamu nggak bisa mencetak tipemu waktu lagi",
                    "nyari bug, padahal justru di saat itu kamu paling butuh.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Harga di toko online Indonesia ditampilkan seperti Rp1.250.000, dengan",
                    "titik tiap tiga angka. Membungkus angka rupiah jadi tipe sendiri lalu",
                    "menerapkan `Display` bikin format itu otomatis berlaku di setiap `{}` dan",
                    "setiap `.to_string()`.",
                    "",
                    "Kasus kecil: buat tipe `struct Rupiah(u64)` yang tercetak sebagai",
                    "Rp1.250.000 untuk 1250000, Rp950 untuk 950, dan Rp0 untuk 0.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami pola titiknya: titik muncul tiap tiga digit dihitung dari",
                    "     kanan, dan nggak pernah ada di depan digit pertama.",
                    "  2. Ubah angkanya ke teks, lalu susun ulang sambil menyisipkan titik:",
                    "      let s = self.0.to_string();",
                    "      let mut hasil = String::new();",
                    "      for (i, c) in s.chars().enumerate() {",
                    "          if i > 0 && (s.len() - i) % 3 == 0 { hasil.push('.'); }",
                    "          hasil.push(c);",
                    "      }",
                    "  3. Taruh kode itu di `impl fmt::Display for Rupiah`, ditutup",
                    "     `write!(f, \"Rp{hasil}\")`. Tambahkan juga `impl From<u64> for Rupiah`,",
                    "     jadi `let r: Rupiah = 1_250_000.into();` langsung bisa.",
                    "  4. Uji di batas jumlah digit: 950 tanpa titik, 1000 jadi Rp1.000,",
                    "     100000 jadi Rp100.000, dan 0 jadi Rp0. `s.len()` aman dipakai di",
                    "     sini, karena semua digit itu ASCII, jadi jumlah byte sama dengan",
                    "     jumlah huruf.",
                ]
            },
        ],
    },
    {
        "title": "22. Membaca Masukan & Berkas",
        "sections": [
            {
                "body": [
                    "Cara membaca satu baris yang diketik di terminal:",
                    "",
                    "  use std::io;",
                    "",
                    "  let mut baris = String::new();",
                    "  io::stdin().read_line(&mut baris).unwrap();",
                    "  let n: i32 = baris.trim().parse().unwrap();",
                    "",
                    "Jebakan: `read_line` menambahkan ke isi string, nggak menggantinya.",
                    "Kalau kamu memakainya berkali-kali tanpa mengosongkan string-nya",
                    "dulu, isinya numpuk. Ini kesalahan yang sering banget terjadi di awal.",
                    "",
                    "`.trim()` wajib ada. read_line ikut menyimpan karakter baris baru",
                    "(`\\n`), dan `\"5\\n\".parse::<i32>()` menghasilkan galat.",
                    "",
                    "Membaca semua masukan sekaligus:",
                    "",
                    "  use std::io::Read;",
                    "  let mut semua = String::new();",
                    "  io::stdin().read_to_string(&mut semua).unwrap();",
                    "",
                    "Membaca baris demi baris:",
                    "",
                    "  use std::io::BufRead;",
                    "  for baris in io::stdin().lock().lines() {",
                    "      let baris = baris.unwrap();",
                    "      ...",
                    "  }",
                    "",
                    "Untuk berkas yang muat di memori, ada cara singkat:",
                    "",
                    "  use std::fs;",
                    "  let isi = fs::read_to_string(\"data.txt\")?;",
                    "  fs::write(\"keluar.txt\", isi)?;",
                    "",
                    "Untuk berkas besar, jangan baca semuanya sekaligus. Baca baris demi",
                    "baris:",
                    "",
                    "  use std::fs::File;",
                    "  use std::io::{BufRead, BufReader};",
                    "",
                    "  let f = File::open(\"besar.txt\")?;",
                    "  for baris in BufReader::new(f).lines() {",
                    "      ...",
                    "  }",
                    "",
                    "Argumen baris perintah, yaitu kata-kata yang diketik sesudah nama",
                    "program waktu menjalankannya:",
                    "  use std::env;",
                    "  let arg: Vec<String> = env::args().collect();",
                    "",
                    "`arg[0]` selalu berisi nama programnya sendiri.",
                    "",
                    "Untuk program baris perintah yang serius, crate `clap` mengurus",
                    "penguraian argumen, teks bantuan, dan validasinya cukup dengan satu",
                    "derive.",
                ]
            },
            {
                "heading": "Membaca masukan dan mengolah berkas",
                "code": """use std::fs;
use std::io::{self, Read};

fn main() -> io::Result<()> {
    // --- Baca seluruh stdin lalu olah ---
    let mut masukan = String::new();
    io::stdin().read_to_string(&mut masukan)?;

    let angka: Vec<i32> = masukan
        .split_whitespace()
        .filter_map(|t| t.parse().ok())     // yang gagal dilewati diam-diam
        .collect();

    if angka.is_empty() {
        println!("tidak ada angka di masukan");
    } else {
        let total: i32 = angka.iter().sum();
        println!("data      : {angka:?}");
        println!("jumlah    : {}", angka.len());
        println!("total     : {total}");
        println!("rata-rata : {:.2}", total as f64 / angka.len() as f64);
        println!("terbesar  : {:?}", angka.iter().max());
    }

    // --- Tulis, baca, lalu hapus sebuah berkas ---
    let path = std::env::temp_dir().join("belajar-rust.txt");
    fs::write(&path, "baris satu\\nbaris dua\\nbaris tiga\\n")?;

    let isi = fs::read_to_string(&path)?;
    for (i, baris) in isi.lines().enumerate() {
        println!("{:>2}| {baris}", i + 1);
    }

    fs::remove_file(&path)?;
    println!("berkas masih ada? {}", path.exists());

    Ok(())
}"""
            },
            {
                "body": [
                    "Dengan masukan \"12 7 abc 30 5\", keluarannya:",
                    "  data      : [12, 7, 30, 5]",
                    "  jumlah    : 4",
                    "  total     : 54",
                    "  rata-rata : 13.50",
                    "  terbesar  : Some(30)",
                    "   1| baris satu",
                    "   2| baris dua",
                    "   3| baris tiga",
                    "  berkas masih ada? false",
                    "",
                    "`filter_map(|t| t.parse().ok())` itu pola yang layak diingat.",
                    "`parse()` menghasilkan Result, `.ok()` mengubahnya jadi Option, dan",
                    "`filter_map` membuang yang None. Satu baris untuk \"ambil yang bisa",
                    "diurai, abaikan sisanya\". Di contoh tadi, \"abc\" ikut terbuang.",
                    "",
                    "Hati-hati: membuang kegagalan tanpa bilang apa-apa nggak selalu benar.",
                    "Kalau masukan yang salah harusnya dilaporkan, kumpulkan hasilnya ke",
                    "`Result<Vec<_>, _>` seperti di materi \"Trait Standar & Konversi\".",
                    "",
                    "`fn main() -> io::Result<()>` bikin `?` bisa dipakai di dalam main.",
                    "Kalau ada yang gagal, program keluar dengan kode keluar bukan nol dan",
                    "mencetak galatnya. Itu perilaku yang diharapkan dari program baris",
                    "perintah.",
                    "",
                    "`std::env::temp_dir()` memberi folder sementara yang benar di sistem",
                    "operasi apa pun, dan `.join()` menyambung jalur berkas dengan pemisah",
                    "yang tepat. Kalau kamu nulis \"/tmp/berkas.txt\" langsung, programnya",
                    "gagal di Windows.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Banyak mesin absensi sidik jari bisa mengekspor catatannya jadi berkas",
                    "teks. Program kecil yang membaca berkas itu baris demi baris bisa langsung",
                    "menyusun daftar pegawai yang datang telat, tanpa menyalinnya manual ke",
                    "spreadsheet.",
                    "",
                    "Kasus kecil: berkas `absen.txt` berisi satu baris per pegawai, nomor dan",
                    "jam masuk, misalnya \"1001 07:45\" dan \"1002 08:10\". Di tengahnya ada baris",
                    "kosong. Jam masuk kantor 08:00. Siapa saja yang telat?",
                    "",
                    "Cara memecahkannya:",
                    "  1. Masukannya teks berbaris, dua kolom dipisah spasi. Keluarannya nomor",
                    "     pegawai yang jamnya lewat dari 08:00.",
                    "  2. Baca seluruh berkas di dalam `fn main() -> io::Result<()>` dengan",
                    "     `let isi = fs::read_to_string(\"absen.txt\")?;`, lalu pecah tiap baris",
                    "     jadi kolom:",
                    "      for baris in isi.lines() {",
                    "          let kolom: Vec<&str> = baris.split_whitespace().collect();",
                    "          if kolom.len() == 2 && kolom[1] > \"08:00\" {",
                    "              println!(\"telat: {}\", kolom[0]);",
                    "          }",
                    "      }",
                    "  3. Urutan di `&&` itu penting. Baris kosong punya nol kolom, dan",
                    "     `kolom.len() == 2` yang dicek duluan mencegah `kolom[1]` bikin panic.",
                    "  4. Jam dibandingkan sebagai teks, dan itu benar selama formatnya selalu",
                    "     dua digit: \"08:10\" lebih besar dari \"08:00\". Kasus pinggirnya jam",
                    "     tanpa nol di depan. \"7:59\" dianggap lebih besar dari \"08:00\", karena",
                    "     perbandingan teks melihat karakter pertama dulu, '7' lawan '0'.",
                    "     Periksa format dari mesinnya, atau ubah jam jadi menit sebelum",
                    "     membandingkan.",
                ]
            },
        ],
    },
    {
        "title": "23. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan struct, enum, trait, Result, iterator,",
                    "dan pembagian tugas antar bagian program dalam satu program utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang sederhana. Fiturnya sengaja",
                    "sedikit. Yang perlu kamu perhatikan adalah cara bagian-bagiannya",
                    "dipisah.",
                    "",
                    "Programnya dibagi tiga lapisan, dan panah ketergantungannya cuma satu",
                    "arah:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "  (main)         (aturan)     (data)",
                    "",
                    "  MODEL     struct Barang, enum Gerak, enum GalatGudang.",
                    "            Tidak tahu apa-apa tentang layar.",
                    "  LAYANAN   struct Gudang dengan semua aturannya.",
                    "            TIDAK PERNAH memanggil println!.",
                    "  ANTARMUKA main: memanggil layanan, mencetak hasil.",
                    "            Tidak menghitung apa pun.",
                    "",
                    "Cara ngetes pembagiannya cukup satu pertanyaan: kalau program ini",
                    "diubah jadi server web, berapa banyak kode yang harus diganti?",
                    "Jawaban yang benar: cuma main.",
                    "",
                    "Di Rust, pemisahan ini dapat bonus. Karena Gudang nggak pernah",
                    "mencetak apa pun, tipe hasil fungsinya wajib membawa semua informasi",
                    "kegagalan. Hasilnya, kamu terdorong merancang fungsi yang gampang diuji.",
                ]
            },
            {
                "heading": "Program lengkap",
                "code": """use std::collections::HashMap;
use std::fmt;

// ---------------------------------------------------------------- MODEL
#[derive(Debug, Clone, PartialEq)]
struct Barang {
    kode: String,
    nama: String,
    stok: i64,
    harga: i64,
}

#[derive(Debug, Clone, Copy, PartialEq)]
enum Gerak {
    Masuk,
    Keluar,
}

#[derive(Debug, PartialEq)]
enum GalatGudang {
    KodeSudahAda(String),
    KodeTidakDikenal(String),
    JumlahTidakSah(i64),
    StokTidakCukup { punya: i64, diminta: i64 },
}

impl fmt::Display for GalatGudang {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            GalatGudang::KodeSudahAda(k) => write!(f, "kode {k} sudah ada"),
            GalatGudang::KodeTidakDikenal(k) => write!(f, "kode {k} tidak dikenal"),
            GalatGudang::JumlahTidakSah(n) => write!(f, "jumlah {n} tidak sah"),
            GalatGudang::StokTidakCukup { punya, diminta } => {
                write!(f, "stok cuma {punya}, diminta {diminta}")
            }
        }
    }
}

// -------------------------------------------------------------- LAYANAN
struct Gudang {
    isi: HashMap<String, Barang>,
}

impl Gudang {
    fn baru() -> Self {
        Gudang { isi: HashMap::new() }
    }

    fn daftar(&mut self, b: Barang) -> Result<(), GalatGudang> {
        if self.isi.contains_key(&b.kode) {
            return Err(GalatGudang::KodeSudahAda(b.kode));
        }
        self.isi.insert(b.kode.clone(), b);
        Ok(())
    }

    fn catat(&mut self, kode: &str, gerak: Gerak, jumlah: i64)
        -> Result<i64, GalatGudang>
    {
        let b = self
            .isi
            .get_mut(kode)
            .ok_or_else(|| GalatGudang::KodeTidakDikenal(kode.to_string()))?;

        if jumlah <= 0 {
            return Err(GalatGudang::JumlahTidakSah(jumlah));
        }

        let baru = match gerak {
            Gerak::Masuk => b.stok + jumlah,
            Gerak::Keluar => b.stok - jumlah,
        };
        if baru < 0 {
            return Err(GalatGudang::StokTidakCukup { punya: b.stok, diminta: jumlah });
        }

        b.stok = baru;
        Ok(baru)
    }

    fn semua(&self) -> Vec<&Barang> {
        let mut v: Vec<&Barang> = self.isi.values().collect();
        v.sort_by(|a, b| a.kode.cmp(&b.kode));
        v
    }

    fn nilai_persediaan(&self) -> i64 {
        self.isi.values().map(|b| b.stok * b.harga).sum()
    }

    fn stok_menipis(&self, batas: i64) -> Vec<&Barang> {
        let mut v: Vec<&Barang> =
            self.isi.values().filter(|b| b.stok < batas).collect();
        v.sort_by(|a, b| a.stok.cmp(&b.stok).then(a.kode.cmp(&b.kode)));
        v
    }
}

// ------------------------------------------------------------ ANTARMUKA
fn main() {
    let mut g = Gudang::baru();

    for (kode, nama, stok, harga) in [
        ("B01", "Kabel", 10, 15_000),
        ("B02", "Adaptor", 4, 85_000),
        ("B03", "Mouse", 25, 120_000),
    ] {
        g.daftar(Barang {
            kode: kode.to_string(),
            nama: nama.to_string(),
            stok,
            harga,
        })
        .unwrap();
    }

    // Langkah yang sengaja campur berhasil dan gagal
    let langkah: Vec<(&str, Gerak, i64)> = vec![
        ("B01", Gerak::Masuk, 15),
        ("B02", Gerak::Keluar, 10),
        ("B03", Gerak::Keluar, 5),
        ("B09", Gerak::Masuk, 1),
        ("B03", Gerak::Keluar, 0),
    ];

    for (kode, gerak, n) in langkah {
        match g.catat(kode, gerak, n) {
            Ok(stok) => println!("{gerak:?} {kode} {n} -> stok {stok}"),
            Err(e) => println!("{gerak:?} {kode} {n} -> DITOLAK: {e}"),
        }
    }

    println!("---");
    for b in g.semua() {
        println!("{:<5}{:<10}{:>4}{:>10}{:>12}",
                 b.kode, b.nama, b.stok, b.harga, b.stok * b.harga);
    }

    println!("---");
    println!("nilai persediaan: {}", g.nilai_persediaan());

    let menipis: Vec<String> = g
        .stok_menipis(10)
        .iter()
        .map(|b| format!("{} {} ({})", b.kode, b.nama, b.stok))
        .collect();
    println!("stok menipis (<10): {}", menipis.join(", "));
}"""
            },
            {
                "body": [
                    "Ada empat keputusan di program itu yang layak ditiru:",
                    "  1. GalatGudang itu enum, bukan String. Pemanggil bisa membedakan",
                    "     jenis kegagalannya dan menanganinya dengan cara yang beda. Selain",
                    "     itu, compiler mengecek apakah `match` atasnya udah menangani semua",
                    "     kemungkinan. Galat berupa teks nggak punya dua kelebihan itu.",
                    "  2. `impl Display for GalatGudang` memisahkan jenis galat dari kalimat",
                    "     pesannya. Kalau nanti pesannya mau diterjemahkan ke bahasa lain,",
                    "     cukup satu fungsi yang diubah.",
                    "  3. `semua()` dan `stok_menipis()` mengurutkan hasilnya sebelum",
                    "     mengembalikannya. HashMap nggak punya urutan, dan di Rust urutannya",
                    "     betul-betul berubah tiap kali program dijalankan. Tanpa",
                    "     pengurutan, keluarannya nggak bisa diuji.",
                    "  4. Gudang nggak memanggil println! sama sekali. Karena itu semua",
                    "     aturannya bisa diuji pakai `assert_eq!`, tanpa perlu membaca",
                    "     layar.",
                    "",
                    "Kalau kamu mau melanjutkannya:",
                    "  - Simpan datanya ke JSON pakai crate serde.",
                    "  - Terima perintah dari baris perintah pakai clap.",
                    "  - Sembunyikan cara penyimpanan di balik sebuah trait. Dengan begitu",
                    "    Gudang nggak perlu tahu datanya ada di berkas, di database, atau",
                    "    cuma di memori waktu tes.",
                    "  - Tulis modul #[cfg(test)] untuk Gudang. Kamu bisa langsung",
                    "    melakukannya tanpa mengubah satu baris pun, berkat keputusan nomor",
                    "    4.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi gudang, kasir, atau antrean di tempat kerja sering dipisah jadi",
                    "lapisan seperti program tadi, karena satu aturan dipakai banyak layar:",
                    "layar kasir, laporan harian, dan mungkin nanti aplikasi HP. Fitur baru",
                    "biasanya berupa satu method baru di lapisan layanan, ditambah beberapa",
                    "baris tampilan di main.",
                    "",
                    "Kasus kecil: pemilik gudang minta daftar pesan ulang, yaitu barang yang",
                    "stoknya di bawah 20 beserta jumlah yang harus dipesan supaya stoknya",
                    "kembali jadi 20. Di akhir program tadi stoknya B01 25, B02 4, dan B03 20,",
                    "jadi jawabannya cuma B02, pesan 16.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan lapisannya. Menghitung daftar itu aturan, jadi tempatnya di",
                    "     `impl Gudang`. Mencetaknya urusan main.",
                    "  2. Tentukan bentuk hasilnya: `Vec<(String, i64)>`, berisi kode barang",
                    "     dan jumlah pesanan. Method ini nggak memanggil println! sama sekali:",
                    "      fn pesan_ulang(&self, target: i64) -> Vec<(String, i64)> {",
                    "          let mut v: Vec<_> = self.isi.values().filter(|b| b.stok < target)",
                    "              .map(|b| (b.kode.clone(), target - b.stok)).collect();",
                    "          v.sort();",
                    "          v",
                    "      }",
                    "  3. `v.sort()` wajib, karena isinya berasal dari HashMap. Tanpa itu,",
                    "     urutan daftarnya berubah tiap program dijalankan.",
                    "  4. Putuskan kasus pinggirnya bersama pemilik: B03 stoknya tepat 20.",
                    "     Dengan `<`, B03 nggak ikut dipesan. Kunci keputusan itu dengan tes:",
                    "     `assert_eq!(g.pesan_ulang(20), vec![(\"B02\".to_string(), 16)]);`.",
                ]
            },
        ],
    },
]
