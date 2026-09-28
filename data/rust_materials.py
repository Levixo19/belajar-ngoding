RUST_MATERIALS = [
    {
        "title": "1. Pengenalan Rust & Instalasi",
        "sections": [
            {
                "body": [
                    "Apa itu Rust?",
                    "  - Bahasa sistem buatan Mozilla, versi 1.0 rilis 2015.",
                    "  - Sekarang dikelola Rust Foundation.",
                    "  - Compiled: kode jadi binari mesin, tanpa runtime dan",
                    "    tanpa garbage collector.",
                    "  - Statically typed dengan inferensi tipe yang kuat.",
                    "",
                    "Janji utamanya satu kalimat: KECEPATAN C dengan KEAMANAN",
                    "MEMORI yang dijamin compiler.",
                    "",
                    "Kelas bug yang TIDAK BISA terjadi di Rust aman:",
                    "  - null pointer dereference",
                    "  - use-after-free (memakai memori yang sudah dilepas)",
                    "  - double free (melepas dua kali)",
                    "  - buffer overflow (indeks di luar batas diperiksa)",
                    "  - data race antar thread",
                    "",
                    "Itu bukan janji kosong: seluruh pemeriksaannya terjadi",
                    "saat KOMPILASI, jadi tidak ada ongkos saat program jalan.",
                    "Harganya juga nyata — compiler akan menolak kode yang",
                    "di bahasa lain diterima diam-diam, dan minggu pertama",
                    "belajar Rust hampir selalu terasa seperti berdebat dengan",
                    "mesin. Itu normal, dan yang sedang kamu lawan sebenarnya",
                    "adalah bug yang belum terjadi.",
                    "",
                    "Dipakai membangun: Firefox, Linux kernel (sebagian),",
                    "Deno, ripgrep, Discord backend, Cloudflare, dan bagian",
                    "inti Android serta Windows.",
                    "",
                    "Instalasi:",
                    "  - Cara resmi: https://rustup.rs",
                    "    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh",
                    "  - Fedora: sudo dnf install rust cargo",
                    "  - Cek   : rustc --version  dan  cargo --version",
                    "",
                    "Menjalankan program:",
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
                    "Penjelasan tiap bagian:",
                    "",
                    "  fn main()",
                    "    Titik masuk program. Setiap program Rust wajib",
                    "    punya tepat satu.",
                    "",
                    "  println!",
                    "    Tanda seru menandai MAKRO, bukan fungsi. Bedanya",
                    "    nyata: makro diperluas jadi kode saat kompilasi,",
                    "    sehingga ia bisa menerima jumlah argumen yang",
                    "    berbeda-beda dan MEMERIKSA format string-nya saat",
                    "    kompilasi. Salah jumlah argumen di println! adalah",
                    "    error kompilasi, bukan crash saat jalan.",
                    "",
                    "  Titik koma",
                    "    Mengakhiri pernyataan. Kehadiran atau ketiadaannya",
                    "    MENGUBAH ARTI di Rust — dibahas di materi Fungsi.",
                    "",
                    "Aturan penulisan Rust:",
                    "  1. Indentasi empat spasi, dirapikan `cargo fmt`.",
                    "  2. Nama fungsi dan variabel snake_case.",
                    "  3. Nama tipe dan trait PascalCase.",
                    "  4. Konstanta SCREAMING_SNAKE_CASE.",
                    "  5. Compiler MEMPERINGATKAN kalau kamu melanggarnya.",
                    "",
                    "Menyisipkan nilai ke dalam teks:",
                    "  let nama = \"Andi\";",
                    "  println!(\"Halo, {nama}!\");        sejak Rust 1.58",
                    "  println!(\"Halo, {}!\", nama);      bentuk lama, tetap sah",
                    "  println!(\"{:?}\", data);           bentuk debug",
                    "  println!(\"{:#?}\", data);          debug berbaris rapi",
                ]
            },
        ],
    },
    {
        "title": "2. Variabel, Mutabilitas & Tipe Data",
        "sections": [
            {
                "body": [
                    "Di Rust, variabel TIDAK BISA DIUBAH secara bawaan.",
                    "Ini kebalikan dari hampir semua bahasa lain, dan ia",
                    "keputusan desain, bukan kerewelan.",
                    "",
                    "  let x = 5;",
                    "  x = 6;          ERROR: cannot assign twice",
                    "",
                    "  let mut y = 5;",
                    "  y = 6;          boleh",
                    "",
                    "Kenapa begitu: data yang tidak berubah aman dibagi ke",
                    "banyak thread tanpa penguncian, dan sebagian besar",
                    "variabel memang tidak pernah perlu berubah. Menulis `mut`",
                    "memaksamu menyatakan niat itu, dan pembaca kode langsung",
                    "tahu variabel mana yang perlu diawasi.",
                    "",
                    "SHADOWING — membuat variabel BARU dengan nama yang sama:",
                    "",
                    "  let x = 5;",
                    "  let x = x + 1;        x baru, nilainya 6",
                    "  let x = \"enam\";       x baru lagi, sekarang &str",
                    "",
                    "Berbeda dari `mut`, shadowing boleh MENGUBAH TIPE. Ia",
                    "berguna persis saat mengubah bentuk data tanpa perlu",
                    "nama baru: `let umur = umur.trim().parse::<u32>()?;`",
                    "",
                    "Konstanta:",
                    "  const MAKS: u32 = 100_000;",
                    "",
                    "Beda dengan let: const wajib bertipe eksplisit, nilainya",
                    "dihitung saat kompilasi, dan boleh dideklarasikan di",
                    "level global.",
                    "",
                    "Tipe bilangan bulat, dan Rust tidak punya 'int' polos:",
                    "  i8  i16  i32  i64  i128  isize    bertanda",
                    "  u8  u16  u32  u64  u128  usize    tanpa tanda",
                    "",
                    "  i32 adalah bawaan kalau kamu tidak menulis tipenya.",
                    "  usize seukuran alamat memori mesin; ia tipe untuk",
                    "  INDEKS dan PANJANG, dan itu bukan pilihan bebas.",
                    "",
                    "Pecahan: f32 dan f64 (bawaan).",
                    "Lainnya: bool (true/false) dan char (satu karakter",
                    "Unicode, 4 byte, ditulis dengan kutip tunggal).",
                    "",
                    "Rust TIDAK PERNAH mengonversi tipe diam-diam. Bahkan",
                    "i32 ke i64 pun harus ditulis: `x as i64`.",
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
                    "Empat baris terakhir menunjukkan sesuatu yang khas Rust.",
                    "Di C, `250 + 10` pada u8 diam-diam jadi 4 dan program",
                    "berjalan terus dengan angka yang salah. Rust memaksamu",
                    "MEMILIH apa yang kamu maksud:",
                    "",
                    "  checked_add     -> Option: None kalau melimpah",
                    "  saturating_add  -> berhenti di batas (255)",
                    "  wrapping_add    -> melingkar (perilaku C)",
                    "  overflowing_add -> (hasil, apakah melimpah)",
                    "",
                    "Dan `besar + 10` polos? Di build debug ia PANIC dengan",
                    "pesan 'attempt to add with overflow'; di build release",
                    "ia melingkar. Itu satu-satunya tempat di Rust yang",
                    "perilakunya berbeda antara debug dan release, dan",
                    "alasannya pemeriksaan itu terlalu mahal untuk produksi.",
                    "",
                    "Garis bawah boleh dipakai sebagai pemisah ribuan:",
                    "1_000_000 sama dengan 1000000, dan jauh lebih terbaca.",
                ]
            },
        ],
    },
    {
        "title": "3. Fungsi, Ekspresi & Pernyataan",
        "sections": [
            {
                "body": [
                    "Fungsi:",
                    "",
                    "  fn tambah(a: i32, b: i32) -> i32 {",
                    "      a + b",
                    "  }",
                    "",
                    "Tipe parameter WAJIB ditulis. Tipe kembalian ditulis",
                    "sesudah panah; kalau tidak ada, fungsinya mengembalikan",
                    "`()` — tipe 'unit', setara void.",
                    "",
                    "Perhatikan `a + b` TANPA titik koma dan TANPA return.",
                    "Inilah perbedaan yang paling sering menjatuhkan pemula",
                    "Rust:",
                    "",
                    "  EKSPRESI    menghasilkan nilai        a + b",
                    "  PERNYATAAN  tidak menghasilkan apa-apa a + b;",
                    "",
                    "Titik koma MENGUBAH ekspresi jadi pernyataan, dan",
                    "nilainya dibuang. Jadi:",
                    "",
                    "  fn f() -> i32 { 5 }     mengembalikan 5",
                    "  fn f() -> i32 { 5; }    ERROR: mengembalikan ()",
                    "",
                    "Pesannya 'expected i32, found ()' dan penyebabnya satu",
                    "karakter titik koma. Sekali kamu tahu ini, kamu akan",
                    "mengenalinya seumur hidup.",
                    "",
                    "`return` tetap ada dan dipakai untuk KELUAR LEBIH AWAL:",
                    "",
                    "  fn cek(n: i32) -> &'static str {",
                    "      if n < 0 { return \"negatif\"; }",
                    "      if n == 0 { return \"nol\"; }",
                    "      \"positif\"",
                    "  }",
                    "",
                    "Hampir SEMUA hal di Rust adalah ekspresi, termasuk if",
                    "dan blok:",
                    "",
                    "  let status = if n >= 75 { \"lulus\" } else { \"ulang\" };",
                    "  let y = { let a = 3; a * a };      y bernilai 9",
                    "",
                    "Karena if adalah ekspresi, Rust tidak butuh operator",
                    "ternary sama sekali.",
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
                    "Fungsi `bagi` mengembalikan TUPLE — cara paling ringkas",
                    "mengembalikan beberapa nilai sekaligus. Menerimanya",
                    "dengan `let (hasil, sisa) = ...` disebut destructuring,",
                    "dan pola yang sama berlaku untuk struct dan enum nanti.",
                    "",
                    "Perhatikan juga: setiap cabang di `grade` TIDAK berakhir",
                    "titik koma, dan seluruh rantai if-else itulah yang jadi",
                    "nilai kembalian fungsi. Kalau salah satu cabang diberi",
                    "titik koma, compiler akan mengeluh bahwa cabang-cabangnya",
                    "punya tipe yang berbeda — pesan yang terdengar aneh tapi",
                    "artinya persis itu.",
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
        ],
    },
    {
        "title": "4. Percabangan & Perulangan",
        "sections": [
            {
                "body": [
                    "if di Rust:",
                    "  - Kondisinya WAJIB bool. `if x` dengan x bertipe angka",
                    "    adalah error kompilasi.",
                    "  - Kurung di sekitar kondisi TIDAK dipakai.",
                    "  - Kurung kurawal WAJIB, bahkan untuk satu pernyataan.",
                    "",
                    "  if nilai >= 75 {",
                    "      println!(\"lulus\");",
                    "  } else {",
                    "      println!(\"ulang\");",
                    "  }",
                    "",
                    "Tiga bentuk perulangan:",
                    "",
                    "  loop      ulang selamanya sampai break",
                    "  while     ulang selama syarat benar",
                    "  for       telusuri sebuah iterator",
                    "",
                    "  loop {",
                    "      hitung += 1;",
                    "      if hitung == 5 { break; }",
                    "  }",
                    "",
                    "`loop` bisa MENGEMBALIKAN NILAI lewat break — hal yang",
                    "tidak ada di kebanyakan bahasa:",
                    "",
                    "  let hasil = loop {",
                    "      n += 1;",
                    "      if n * n > 100 { break n; }",
                    "  };",
                    "",
                    "for adalah yang paling sering dipakai, dan bentuknya",
                    "SELALU 'for x in sesuatu':",
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
                    "Baris ketiga dari bawah penting dan akan dibahas tuntas",
                    "di materi Ownership: `for x in vec` MENGAMBIL vec, dan",
                    "sesudah perulangan itu vec tidak bisa dipakai lagi.",
                    "",
                    "LABEL untuk keluar dari perulangan bersarang:",
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
                    "`print!` tanpa `ln` mencetak tanpa pindah baris, sama",
                    "seperti di bahasa lain. `println!()` kosong cuma pindah",
                    "baris.",
                    "",
                    "Satu hal yang perlu diketahui tentang `print!`: keluaran",
                    "ke terminal disangga (buffered), dan penyangganya baru",
                    "dikosongkan saat ada baris baru. Kalau kamu mencetak",
                    "prompt dengan `print!` lalu langsung membaca masukan,",
                    "prompt-nya bisa belum muncul. Perbaikannya:",
                    "",
                    "  use std::io::Write;",
                    "  io::stdout().flush().unwrap();",
                    "",
                    "Rentang `1..20` pada contoh terakhir tidak memuat 20.",
                    "Kalau kamu lupa ini, pencarian yang seharusnya ketemu",
                    "bisa berakhir tanpa hasil tanpa satu pun error.",
                ]
            },
        ],
    },
    {
        "title": "5. Ownership: Aturan Inti Rust",
        "sections": [
            {
                "body": [
                    "Ownership adalah gagasan yang membuat Rust berbeda dari",
                    "semua bahasa lain. Ia yang menggantikan garbage collector",
                    "TANPA menyerahkan pelepasan memori ke tangan manusia.",
                    "",
                    "TIGA ATURANNYA, dan cuma tiga:",
                    "",
                    "  1. Setiap nilai punya satu variabel PEMILIK.",
                    "  2. Hanya boleh ada SATU pemilik pada satu waktu.",
                    "  3. Begitu pemiliknya keluar dari scope, nilainya",
                    "     DILEPAS.",
                    "",
                    "Aturan ketiga berarti tidak ada yang perlu memanggil",
                    "free(), dan tidak ada yang bisa melupakannya.",
                    "",
                    "MOVE — penugasan MEMINDAHKAN kepemilikan:",
                    "",
                    "  let a = String::from(\"halo\");",
                    "  let b = a;              kepemilikan pindah ke b",
                    "  println!(\"{a}\");        ERROR: value borrowed after move",
                    "",
                    "Di Java atau Python, baris itu membuat a dan b menunjuk",
                    "objek yang sama. Di C++, ia menyalin seluruh isinya. Rust",
                    "memilih jalan ketiga: a berhenti berlaku, dan compiler",
                    "menolak setiap pemakaian sesudahnya.",
                    "",
                    "Kenapa: kalau a dan b sama-sama pemilik, keduanya akan",
                    "melepas memori yang sama saat scope berakhir — double",
                    "free, salah satu bug paling berbahaya di C++.",
                    "",
                    "COPY — tipe kecil berukuran tetap disalin, bukan dipindah:",
                    "",
                    "  let a = 5;",
                    "  let b = a;",
                    "  println!(\"{a}\");        baik-baik saja",
                    "",
                    "Yang bersifat Copy: semua tipe angka, bool, char, dan",
                    "tuple yang seluruh isinya Copy. Aturan praktisnya: kalau",
                    "ukurannya diketahui saat kompilasi dan seluruhnya tinggal",
                    "di stack, ia Copy.",
                    "",
                    "String dan Vec TIDAK Copy karena isinya di heap, dan",
                    "menyalinnya berarti mengalokasikan memori baru — hal",
                    "yang terlalu mahal untuk terjadi diam-diam.",
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
                    "Tiga cara memberikan nilai ke fungsi, dan memilihnya",
                    "adalah keputusan desain yang kamu ambil setiap hari:",
                    "",
                    "  fn f(s: String)      AMBIL. Pemanggil kehilangan s.",
                    "                       Dipakai kalau fungsi memang jadi",
                    "                       pemilik barunya.",
                    "  fn f(s: &String)     PINJAM baca. Pemanggil tetap",
                    "                       memilikinya. Ini yang paling",
                    "                       sering benar.",
                    "  fn f(s: &mut String) PINJAM ubah. Boleh menyunting,",
                    "                       pemanggil tetap pemiliknya.",
                    "",
                    "`clone()` membuat salinan penuh dan selalu berhasil,",
                    "tapi ia mengalokasikan memori. Di Rust, clone yang",
                    "bertebaran di mana-mana biasanya tanda bahwa kepemilikan",
                    "belum dipikirkan — bukan dosa, tapi layak ditinjau ulang",
                    "sesudah kodenya berjalan.",
                    "",
                    "Yang perlu ditanam sekarang: pesan error 'borrow of",
                    "moved value' BUKAN hukuman. Ia memberi tahu bahwa ada",
                    "dua tempat di kodemu yang sama-sama mengira memiliki",
                    "sesuatu — pertanyaan yang di C++ baru terjawab saat",
                    "program sudah di tangan pengguna.",
                ]
            },
        ],
    },
    {
        "title": "6. Reference & Borrowing",
        "sections": [
            {
                "body": [
                    "Borrowing adalah memakai nilai TANPA mengambil",
                    "kepemilikannya. Tandanya `&`.",
                    "",
                    "  let s = String::from(\"halo\");",
                    "  let r = &s;             r meminjam s",
                    "  println!(\"{s} {r}\");    keduanya sah",
                    "",
                    "ATURAN BORROWING, dan ini yang paling sering dilanggar",
                    "pemula:",
                    "",
                    "  Pada satu waktu, kamu boleh punya SALAH SATU:",
                    "    - berapa pun banyaknya peminjam BACA (&T), ATAU",
                    "    - tepat SATU peminjam UBAH (&mut T)",
                    "  Tidak boleh keduanya sekaligus.",
                    "",
                    "Kenapa: kalau ada yang membaca sementara yang lain",
                    "mengubah, pembacanya bisa melihat data setengah jadi.",
                    "Itu definisi data race — dan Rust membuatnya mustahil",
                    "saat kompilasi, bukan cuma di antar-thread tapi juga",
                    "di dalam satu fungsi.",
                    "",
                    "  let mut v = vec![1, 2, 3];",
                    "  let a = &v;           pinjam baca",
                    "  let b = &v;           pinjam baca lagi -- boleh",
                    "  let c = &mut v;       ERROR: sudah ada peminjam baca",
                    "",
                    "NLL (Non-Lexical Lifetimes) membuat ini jauh lebih",
                    "longgar daripada kedengarannya: sebuah pinjaman berakhir",
                    "di PEMAKAIAN TERAKHIRNYA, bukan di akhir blok. Jadi ini",
                    "sah:",
                    "",
                    "  let a = &v;",
                    "  println!(\"{a:?}\");    pinjaman a berakhir di sini",
                    "  let c = &mut v;       boleh sekarang",
                    "",
                    "DANGLING REFERENCE tidak bisa terjadi:",
                    "",
                    "  fn buat() -> &String {",
                    "      let s = String::from(\"halo\");",
                    "      &s          ERROR: s mati saat fungsi selesai",
                    "  }",
                    "",
                    "Di C ini kompilasi tanpa keluhan dan menghasilkan",
                    "pointer ke memori yang sudah dilepas. Di Rust, compiler",
                    "menolaknya dan menyarankan mengembalikan String-nya",
                    "langsung.",
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
                    "Tanda bintang `*` disebut DEREFERENCE: ia menyentuh",
                    "nilai yang ditunjuk referensi. Di `*n += 1`, tanpa",
                    "bintang kamu akan mencoba menambah satu ke sebuah",
                    "alamat, bukan ke isinya.",
                    "",
                    "Kabar baiknya, Rust melakukan dereference OTOMATIS saat",
                    "kamu memanggil method: `s.len()` bekerja entah s itu",
                    "String atau &String atau &&String. Fitur ini disebut",
                    "auto-deref, dan ia yang membuat referensi jarang terasa",
                    "merepotkan dalam pemakaian sehari-hari.",
                    "",
                    "Kesalahan yang paling sering di awal, dan cara membaca",
                    "pesannya:",
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
        ],
    },
    {
        "title": "7. Slice & String",
        "sections": [
            {
                "body": [
                    "Slice adalah REFERENSI ke sebagian dari sebuah koleksi.",
                    "Ia tidak memiliki datanya dan tidak menyalin apa pun.",
                    "",
                    "  let v = vec![1, 2, 3, 4, 5];",
                    "  let potong = &v[1..4];       [2, 3, 4]",
                    "  let awal   = &v[..2];        [1, 2]",
                    "  let akhir  = &v[3..];        [4, 5]",
                    "  let semua  = &v[..];         seluruhnya",
                    "",
                    "Tipenya `&[i32]`, dibaca 'slice dari i32'.",
                    "",
                    "DUA TIPE TEKS di Rust, dan membedakannya adalah salah",
                    "satu rintangan pertama:",
                    "",
                    "  String   MEMILIKI teksnya, tersimpan di heap, bisa",
                    "           tumbuh. Setara StringBuilder.",
                    "  &str     PINJAMAN ke teks milik orang lain. Ukurannya",
                    "           tetap. Disebut 'string slice'.",
                    "",
                    "  let a: &str = \"halo\";              literal SELALU &str",
                    "  let b: String = String::from(\"halo\");",
                    "  let c: String = \"halo\".to_string();",
                    "  let d: &str = &b;                   pinjam dari String",
                    "  let e: &str = &b[0..2];             pinjam sebagian",
                    "",
                    "ATURAN PRAKTIS yang menyelesaikan 90% kebingungan:",
                    "  - Parameter fungsi: pakai &str. Ia menerima keduanya.",
                    "  - Field struct dan nilai kembalian: pakai String.",
                    "",
                    "  fn sapa(nama: &str) { ... }",
                    "  sapa(\"Andi\");        literal, langsung cocok",
                    "  sapa(&nama_string);  String otomatis jadi &str",
                    "",
                    "PERINGATAN UTF-8: String di Rust disimpan sebagai UTF-8,",
                    "dan satu karakter bisa memakan 1 sampai 4 byte.",
                    "Akibatnya:",
                    "  - `s.len()` memberi jumlah BYTE, bukan huruf.",
                    "  - `s[0]` TIDAK ADA — mengindeks string dilarang.",
                    "  - `&s[0..2]` PANIC kalau memotong di tengah karakter.",
                    "",
                    "Yang benar: `s.chars().count()` untuk jumlah huruf,",
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
                    "Byte dan huruf sama-sama 34 karena seluruhnya ASCII.",
                    "Coba ganti kalimatnya dengan yang memuat huruf beraksen",
                    "atau emoji, dan kedua angka itu akan berpisah — itulah",
                    "alasan Rust melarang `s[0]`.",
                    "",
                    "`find` mengembalikan `Option<usize>`: Some(posisi) kalau",
                    "ketemu, None kalau tidak. Rust tidak memakai -1 sebagai",
                    "penanda 'tidak ada', karena -1 adalah angka yang sah dan",
                    "gampang dipakai tanpa diperiksa. Option memaksa",
                    "pemeriksaannya — dibahas di materi berikutnya.",
                    "",
                    "`collect::<String>()` memakai turbofish `::<>` untuk",
                    "memberi tahu tipe yang diinginkan. Ia perlu di sini",
                    "karena `collect` bisa menghasilkan banyak tipe dan",
                    "compiler tidak punya petunjuk lain.",
                ]
            },
        ],
    },
    {
        "title": "8. Struct",
        "sections": [
            {
                "body": [
                    "Struct mengelompokkan beberapa nilai bernama jadi satu",
                    "tipe.",
                    "",
                    "  struct Murid {",
                    "      nama: String,",
                    "      nilai: u32,",
                    "      aktif: bool,",
                    "  }",
                    "",
                    "Membuatnya:",
                    "  let m = Murid {",
                    "      nama: String::from(\"Andi\"),",
                    "      nilai: 88,",
                    "      aktif: true,",
                    "  };",
                    "",
                    "SELURUH field wajib diisi. Tidak ada nilai bawaan",
                    "kecuali kamu mengimplementasi trait Default.",
                    "",
                    "Kalau nama variabel sama dengan nama field, ada",
                    "singkatan:",
                    "  fn buat(nama: String, nilai: u32) -> Murid {",
                    "      Murid { nama, nilai, aktif: true }",
                    "  }",
                    "",
                    "Menyalin sebagian dari struct lain:",
                    "  let m2 = Murid { nilai: 90, ..m };",
                    "",
                    "Hati-hati: `..m` MEMINDAHKAN field yang tidak Copy dari",
                    "m, sehingga m tidak bisa dipakai lagi seutuhnya.",
                    "",
                    "Tiga jenis struct:",
                    "",
                    "  BIASA        struct Titik { x: f64, y: f64 }",
                    "  TUPLE        struct Warna(u8, u8, u8);",
                    "               diakses dengan .0 .1 .2",
                    "  UNIT         struct Penanda;",
                    "               tanpa data, berguna untuk trait",
                    "",
                    "METHOD ditulis di blok `impl` yang TERPISAH dari",
                    "definisi datanya — pemisahan yang membuat satu struct",
                    "bisa punya beberapa blok impl, termasuk yang menambah",
                    "trait dari luar.",
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
                    "Empat bentuk parameter pertama method, dan memilihnya",
                    "adalah bagian dari desain API-mu:",
                    "",
                    "  &self       baca saja. Yang paling sering benar.",
                    "  &mut self   boleh mengubah objeknya.",
                    "  self        MENGAMBIL objeknya; pemanggil kehilangannya.",
                    "              Dipakai untuk method yang mengubah bentuk,",
                    "              misalnya `into_bytes()`.",
                    "  (tanpa self) fungsi terkait, dipanggil dengan ::",
                    "",
                    "`Self` dengan S besar adalah alias untuk tipe yang sedang",
                    "di-impl. Menulis `Self` alih-alih `Rekening` berarti",
                    "mengganti nama struct-nya nanti tidak menyentuh isi impl.",
                    "",
                    "`#[derive(Debug)]` menyuruh compiler menuliskan sendiri",
                    "kode untuk mencetak struct dengan `{:?}`. Tanpa itu,",
                    "`println!(\"{a:?}\")` adalah error. Derive lain yang",
                    "sering dipakai:",
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
                    "Menuliskannya satu baris menghemat puluhan baris kode",
                    "yang gampang salah satu-dua bagiannya.",
                ]
            },
        ],
    },
    {
        "title": "9. Enum & Option",
        "sections": [
            {
                "body": [
                    "Enum di Rust jauh lebih kuat daripada enum di C atau",
                    "Java: setiap variannya boleh MEMBAWA DATA, dan datanya",
                    "boleh berbeda bentuk di tiap varian.",
                    "",
                    "  enum Pesan {",
                    "      Keluar,                       tanpa data",
                    "      Pindah { x: i32, y: i32 },    seperti struct",
                    "      Tulis(String),                seperti tuple",
                    "      Warna(u8, u8, u8),",
                    "  }",
                    "",
                    "Ini yang di bahasa lain disebut 'tagged union' atau",
                    "'sum type'. Nilainya SELALU tepat satu varian, dan",
                    "compiler tahu itu.",
                    "",
                    "OPTION — jawaban Rust untuk null:",
                    "",
                    "  enum Option<T> {",
                    "      None,",
                    "      Some(T),",
                    "  }",
                    "",
                    "Rust TIDAK PUNYA null. Nilai yang mungkin kosong",
                    "dinyatakan lewat tipenya: `Option<i32>` berbeda dari",
                    "`i32`, dan compiler tidak akan mengizinkanmu memakai",
                    "Option seolah-olah ia angka biasa.",
                    "",
                    "Akibatnya: kelas bug null pointer LENYAP. Bukan berkurang",
                    "— lenyap. Kamu tidak bisa lupa memeriksa, karena kodenya",
                    "tidak akan dikompilasi.",
                    "",
                    "Mengambil isinya:",
                    "  o.unwrap()            ambil; PANIC kalau None",
                    "  o.expect(\"pesan\")     sama, dengan pesan sendiri",
                    "  o.unwrap_or(0)        ambil, atau 0 kalau None",
                    "  o.unwrap_or_else(|| hitung())",
                    "  o.unwrap_or_default() ambil, atau nilai bawaan tipenya",
                    "",
                    "Mengubah tanpa membuka:",
                    "  o.map(|x| x * 2)      Some(2x) kalau ada, None kalau tidak",
                    "  o.filter(|x| *x > 3)",
                    "  o.and_then(|x| f(x))  untuk fungsi yang balik Option juga",
                    "  o.is_some() / o.is_none()",
                    "  o.ok_or(\"galat\")      ubah jadi Result",
                    "",
                    "unwrap() cocok untuk contoh dan prototipe. Di kode yang",
                    "dipakai orang, tiap unwrap adalah janji 'ini tidak",
                    "mungkin None' — dan janji itu harus benar.",
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
                    "`Bentuk::PersegiPanjang { .. }` memakai dua titik untuk",
                    "berkata 'aku tidak peduli isinya'. Garis bawah tunggal",
                    "`_` melakukan hal yang sama untuk satu nilai.",
                    "",
                    "Bandingkan enum ini dengan pendekatan pewarisan di C#",
                    "atau Java. Keduanya menyelesaikan masalah yang sama,",
                    "tapi bertukar sifat:",
                    "",
                    "  ENUM + match  mudah menambah OPERASI baru (satu fungsi",
                    "                baru), sulit menambah VARIAN baru (semua",
                    "                match harus diperbarui -- dan compiler",
                    "                akan memberitahumu di mana saja).",
                    "  TRAIT/kelas   mudah menambah TIPE baru, sulit menambah",
                    "                operasi baru (semua tipe harus disunting).",
                    "",
                    "Rust punya keduanya. Yang menentukan pilihannya satu",
                    "pertanyaan: mana yang lebih sering berubah di masalahmu,",
                    "daftar bentuknya atau daftar operasinya?",
                ]
            },
        ],
    },
    {
        "title": "10. Pattern Matching: match & if let",
        "sections": [
            {
                "body": [
                    "`match` adalah percabangan berbasis POLA, dan ia salah",
                    "satu bagian terbaik dari Rust.",
                    "",
                    "  match nilai {",
                    "      1 => println!(\"satu\"),",
                    "      2 | 3 => println!(\"dua atau tiga\"),",
                    "      4..=6 => println!(\"empat sampai enam\"),",
                    "      n if n < 0 => println!(\"negatif {n}\"),",
                    "      _ => println!(\"lainnya\"),",
                    "  }",
                    "",
                    "SIFAT PALING PENTING: match wajib EXHAUSTIVE. Kalau ada",
                    "satu kemungkinan yang tidak tertangani, kodenya TIDAK",
                    "AKAN DIKOMPILASI.",
                    "",
                    "Ini bukan kerewelan, ini fitur utamanya. Saat kamu",
                    "menambah varian baru ke sebuah enum, compiler akan",
                    "menunjukkan SETIAP tempat di seluruh proyek yang perlu",
                    "diperbarui. Di bahasa tanpa sifat ini, yang terjadi",
                    "adalah cabang default diam-diam menelan varian baru",
                    "itu, dan bugnya muncul entah kapan.",
                    "",
                    "match adalah EKSPRESI, jadi ia menghasilkan nilai:",
                    "",
                    "  let label = match n {",
                    "      0 => \"nol\",",
                    "      n if n > 0 => \"positif\",",
                    "      _ => \"negatif\",",
                    "  };",
                    "",
                    "Semua cabang wajib bertipe sama.",
                    "",
                    "`if let` adalah match yang cuma peduli SATU pola:",
                    "",
                    "  if let Some(x) = hasil {",
                    "      println!(\"dapat {x}\");",
                    "  } else {",
                    "      println!(\"kosong\");",
                    "  }",
                    "",
                    "`let else` untuk pulang lebih awal:",
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
                    "Perhatikan `Perintah::Geser { x: 0, y: 0 }` ditulis",
                    "SEBELUM `Perintah::Geser { x, y }`. Pencocokan berhenti",
                    "di pola pertama yang cocok, jadi yang lebih sempit harus",
                    "lebih dulu. Kalau dibalik, cabang khususnya tidak akan",
                    "pernah tercapai — dan compiler memang akan",
                    "memperingatkan 'unreachable pattern'.",
                    "",
                    "Ringkasan bentuk pola yang tersedia:",
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
        ],
    },
    {
        "title": "11. Vec & HashMap",
        "sections": [
            {
                "body": [
                    "Vec<T> adalah array yang bisa tumbuh, tersimpan di heap.",
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
                    "DUA cara mengambil elemen, dan bedanya penting:",
                    "  v[0]        PANIC kalau di luar batas",
                    "  v.get(0)    -> Option<&T>, aman",
                    "",
                    "Untuk indeks yang datang dari luar (masukan pengguna,",
                    "berkas), selalu pakai `get`.",
                    "",
                    "HashMap<K, V> menyimpan pasangan kunci-nilai:",
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
                    "Pola penghitung yang sangat sering dipakai:",
                    "  *m.entry(kata).or_insert(0) += 1;",
                    "",
                    "`entry` mengembalikan tempat kuncinya; `or_insert(0)`",
                    "mengisinya dengan 0 kalau belum ada, lalu memberi",
                    "referensi ke nilainya. Bintang membukanya supaya bisa",
                    "ditambah. Satu baris menggantikan if-else lengkap.",
                    "",
                    "URUTAN HashMap TIDAK DIJAMIN — dan di Rust ia benar-",
                    "benar acak setiap kali program dijalankan, disengaja",
                    "sebagai pertahanan terhadap serangan hash collision.",
                    "Kalau urutan penting, urutkan eksplisit atau pakai",
                    "BTreeMap yang selalu terurut.",
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
                    "`sort_by(|a, b| b.1.cmp(a.1).then(a.0.cmp(b.0)))` membaca:",
                    "urutkan menurun berdasarkan jumlah (b sebelum a =",
                    "menurun), dan kalau sama, menaik berdasarkan kata.",
                    "`then` merangkai kunci urutan kedua.",
                    "",
                    "`dedup()` hanya membuang duplikat yang BERURUTAN, itu",
                    "sebabnya ia selalu dipanggil sesudah `sort()`. Kalau",
                    "dipanggil sendirian pada data acak, sebagian besar",
                    "duplikat lolos — bug yang tidak menghasilkan error apa",
                    "pun.",
                    "",
                    "`sum::<i32>()` memakai turbofish lagi: `sum` bisa",
                    "menjumlahkan ke banyak tipe, jadi tipenya harus",
                    "diberitahukan. Alternatifnya menuliskannya di variabel:",
                    "`let total: i32 = angka.iter().sum();`",
                ]
            },
        ],
    },
    {
        "title": "12. Penanganan Galat: panic! & Result",
        "sections": [
            {
                "body": [
                    "Rust membagi kegagalan jadi dua kategori, dan pembagian",
                    "itu tercermin di tipenya.",
                    "",
                    "TIDAK BISA DIPULIHKAN -> panic!",
                    "  Program berhenti. Dipakai untuk bug: indeks di luar",
                    "  batas, invariant yang dilanggar, keadaan yang mustahil.",
                    "",
                    "  panic!(\"ini seharusnya tidak pernah terjadi\");",
                    "  assert!(n > 0, \"n harus positif\");",
                    "  assert_eq!(hasil, 42);",
                    "  unreachable!();",
                    "  todo!();",
                    "",
                    "BISA DIPULIHKAN -> Result",
                    "  Berkas tidak ada, jaringan putus, masukan tidak sah.",
                    "  Hal-hal yang WAJAR terjadi dan program harus tahu apa",
                    "  yang dilakukan.",
                    "",
                    "  enum Result<T, E> {",
                    "      Ok(T),",
                    "      Err(E),",
                    "  }",
                    "",
                    "Result HARUS ditangani. Mengabaikannya memunculkan",
                    "peringatan `#[must_use]` — Rust tidak akan membiarkanmu",
                    "lupa bahwa sesuatu bisa gagal.",
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
                    "OPERATOR ? — yang membuat penanganan galat di Rust",
                    "enak dipakai:",
                    "",
                    "  fn baca(path: &str) -> Result<String, io::Error> {",
                    "      let isi = fs::read_to_string(path)?;",
                    "      Ok(isi.trim().to_string())",
                    "  }",
                    "",
                    "Tanda tanya berarti: kalau Ok, ambil isinya dan lanjut;",
                    "kalau Err, LANGSUNG kembalikan galat itu dari fungsi ini.",
                    "Ia menggantikan lima baris match dengan satu karakter,",
                    "dan tetap sepenuhnya eksplisit — kamu bisa MELIHAT di",
                    "mana kegagalan bisa terjadi, tidak seperti exception",
                    "yang bisa melompat dari mana saja.",
                    "",
                    "`?` hanya boleh di fungsi yang mengembalikan Result",
                    "atau Option. Sejak Rust 1.26, `fn main()` boleh",
                    "mengembalikan Result juga.",
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
                    "Perhatikan `rata_rata`: satu baris `parse_nilai(t)?` dan",
                    "seluruh penanganan kegagalannya selesai. Tanpa `?`,",
                    "fungsi itu butuh blok match lima baris di dalam",
                    "perulangan.",
                    "",
                    "`map_err` mengubah tipe galat dari ParseIntError jadi",
                    "GalatNilai. Ini perlu karena `?` menuntut tipe galatnya",
                    "bisa diubah ke tipe kembalian fungsinya.",
                    "",
                    "Dalam proyek nyata, dua crate membuat ini jauh lebih",
                    "ringkas:",
                    "  thiserror   untuk PUSTAKA: bikin enum galat sendiri",
                    "              dengan pesan, satu atribut per varian.",
                    "  anyhow      untuk APLIKASI: satu tipe galat untuk",
                    "              semuanya, dengan konteks berlapis.",
                    "",
                    "Aturan praktis memilih antara panic dan Result:",
                    "  - Salah pakai API oleh PROGRAMMER -> panic. Itu bug.",
                    "  - Salah masukan dari PENGGUNA atau dunia luar ->",
                    "    Result. Itu keadaan normal.",
                    "  - Di pustaka: hampir selalu Result. Biarkan pemakainya",
                    "    yang memutuskan apakah ini fatal.",
                ]
            },
        ],
    },
    {
        "title": "13. Generic",
        "sections": [
            {
                "body": [
                    "Generic membuat satu potong kode bekerja untuk banyak",
                    "tipe tanpa kehilangan pemeriksaan tipe dan tanpa ongkos",
                    "saat program jalan.",
                    "",
                    "Fungsi generic:",
                    "  fn terbesar<T: PartialOrd>(daftar: &[T]) -> &T {",
                    "      let mut hasil = &daftar[0];",
                    "      for x in daftar {",
                    "          if x > hasil { hasil = x; }",
                    "      }",
                    "      hasil",
                    "  }",
                    "",
                    "`<T: PartialOrd>` dibaca: untuk tipe T apa pun yang bisa",
                    "dibandingkan. Tanpa batasan itu, compiler menolak `x >",
                    "hasil` karena tidak setiap tipe bisa dibandingkan.",
                    "",
                    "Struct generic:",
                    "  struct Titik<T> { x: T, y: T }",
                    "  struct Pasangan<A, B> { kiri: A, kanan: B }",
                    "",
                    "Enum generic — dua yang paling penting sudah kamu pakai:",
                    "  Option<T>, Result<T, E>",
                    "",
                    "Batasan bisa ditulis dua cara, dan yang kedua lebih",
                    "terbaca saat batasannya banyak:",
                    "",
                    "  fn f<T: Clone + Debug>(x: T) { ... }",
                    "",
                    "  fn f<T>(x: T)",
                    "  where",
                    "      T: Clone + Debug,",
                    "  { ... }",
                    "",
                    "MONOMORPHIZATION: saat kompilasi, Rust menghasilkan",
                    "SALINAN kode khusus untuk setiap tipe yang benar-benar",
                    "dipakai. `terbesar::<i32>` dan `terbesar::<f64>` jadi",
                    "dua fungsi terpisah di binari.",
                    "",
                    "Akibatnya: generic di Rust GRATIS saat program jalan —",
                    "secepat kode yang ditulis khusus untuk tipe itu. Tidak",
                    "ada boxing, tidak ada pencarian tabel virtual. Harganya",
                    "binari yang lebih besar dan kompilasi yang lebih lama.",
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
                    "`for &x in daftar` memakai pola untuk MEMBUKA referensi",
                    "sekaligus: tanpa `&` di situ, x bertipe `&T` dan",
                    "perbandingannya jadi berbeda. Ini pemakaian pattern",
                    "matching di tempat yang tidak terlihat seperti match.",
                    "",
                    "`impl<T: Display> Kotak<T>` memberi method HANYA kepada",
                    "Kotak yang isinya bisa ditampilkan. Kotak<T> dengan T",
                    "yang tidak Display tetap bisa dibuat, ia cuma tidak",
                    "punya method-method ini. Teknik ini disebut conditional",
                    "implementation dan dipakai di seluruh pustaka standar.",
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
        ],
    },
    {
        "title": "14. Trait",
        "sections": [
            {
                "body": [
                    "Trait mendefinisikan PERILAKU yang bisa dimiliki banyak",
                    "tipe. Ia setara interface di bahasa lain, tapi lebih",
                    "kuat karena bisa diterapkan pada tipe yang bukan milikmu.",
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
                    "DUA CARA memakai trait sebagai tipe, dan bedanya nyata:",
                    "",
                    "  STATIC DISPATCH  fn f(x: &impl BisaSapa)",
                    "                   atau fn f<T: BisaSapa>(x: &T)",
                    "    Tipe dipilih saat kompilasi. Cepat, tanpa ongkos.",
                    "    Tapi satu pemanggilan = satu tipe.",
                    "",
                    "  DYNAMIC DISPATCH fn f(x: &dyn BisaSapa)",
                    "    Tipe dipilih saat program jalan lewat tabel virtual.",
                    "    Sedikit lebih lambat, tapi satu Vec bisa memuat",
                    "    BERBAGAI tipe sekaligus: Vec<Box<dyn BisaSapa>>.",
                    "",
                    "Aturan praktis: pakai `impl Trait` sampai kamu benar-",
                    "benar butuh menyimpan tipe yang berbeda-beda dalam satu",
                    "koleksi; baru pakai `dyn`.",
                    "",
                    "ATURAN KEYATIMAN (orphan rule): kamu boleh",
                    "mengimplementasi trait untuk tipe apa pun ASALKAN",
                    "trait-nya ATAU tipenya milikmu. Ini yang mencegah dua",
                    "crate berbeda memberi implementasi yang bertabrakan",
                    "untuk pasangan yang sama.",
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
                    "`Box<dyn Bangun>` dibaca: sebuah kotak di heap yang",
                    "berisi sesuatu yang mengimplementasi Bangun. Box perlu",
                    "karena ukuran tipe sesungguhnya tidak diketahui saat",
                    "kompilasi, sementara Vec menuntut semua elemennya",
                    "berukuran sama. Box selalu seukuran pointer, apa pun",
                    "isinya.",
                    "",
                    "Lingkaran menimpa `ringkas()` sementara Persegi memakai",
                    "yang bawaan. Ini kekuatan implementasi bawaan di trait:",
                    "kamu memberi perilaku yang masuk akal untuk semua, dan",
                    "yang butuh berbeda tinggal menuliskannya.",
                    "",
                    "Sekali kamu mengimplementasi `Display`, kamu mendapat",
                    "`.to_string()` GRATIS lewat blanket implementation di",
                    "pustaka standar. Pola 'implementasi satu, dapat banyak'",
                    "ini ada di mana-mana di Rust — implementasi `Iterator`",
                    "saja langsung memberimu map, filter, fold, dan puluhan",
                    "method lainnya.",
                ]
            },
        ],
    },
    {
        "title": "15. Lifetime",
        "sections": [
            {
                "body": [
                    "Lifetime adalah cara memberi tahu compiler BERAPA LAMA",
                    "sebuah referensi boleh hidup. Ia tidak mengubah apa pun",
                    "saat program jalan — ia murni pemeriksaan kompilasi.",
                    "",
                    "Kabar baiknya: 95% waktu kamu tidak perlu menuliskannya.",
                    "Compiler menyimpulkannya lewat tiga aturan elision:",
                    "",
                    "  1. Setiap parameter referensi dapat lifetime sendiri.",
                    "  2. Kalau parameternya cuma SATU referensi, kembaliannya",
                    "     memakai lifetime itu.",
                    "  3. Kalau ada &self, kembaliannya memakai lifetime self.",
                    "",
                    "Aturan 3 itulah kenapa method hampir tidak pernah butuh",
                    "anotasi.",
                    "",
                    "KAPAN kamu harus menulisnya: saat sebuah fungsi menerima",
                    "beberapa referensi dan mengembalikan referensi, sehingga",
                    "compiler tidak tahu yang mana sumbernya.",
                    "",
                    "  fn lebih_panjang(a: &str, b: &str) -> &str   ERROR",
                    "",
                    "  fn lebih_panjang<'a>(a: &'a str, b: &'a str) -> &'a str",
                    "  {",
                    "      if a.len() > b.len() { a } else { b }",
                    "  }",
                    "",
                    "`'a` dibaca 'tick a'. Artinya: kembaliannya hidup",
                    "SELAMA yang lebih pendek di antara a dan b. Itu bukan",
                    "perintah kepada compiler melainkan JANJI yang ia",
                    "periksa.",
                    "",
                    "Lifetime khusus `'static` berarti hidup selama program.",
                    "Semua literal string bertipe `&'static str`, karena",
                    "teksnya tertanam di binari.",
                    "",
                    "Struct yang MENYIMPAN referensi wajib beranotasi:",
                    "",
                    "  struct Kutipan<'a> {",
                    "      bagian: &'a str,",
                    "  }",
                    "",
                    "Artinya: sebuah Kutipan tidak boleh hidup lebih lama",
                    "daripada teks yang ditunjuknya. Kalau kamu merasa ini",
                    "merepotkan, seringkali jawabannya adalah menyimpan",
                    "`String` (yang memiliki datanya) alih-alih `&str`.",
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
                    "Blok terakhir menunjukkan cara paling umum keluar dari",
                    "kebuntuan lifetime: `.to_string()`. Dengan MEMILIKI",
                    "datanya sendiri, `hasil` tidak lagi bergantung pada umur",
                    "`sementara`. Ongkosnya satu alokasi memori; hasilnya",
                    "kode yang jauh lebih sederhana.",
                    "",
                    "Cara membaca pesan lifetime yang paling sering muncul:",
                    "",
                    "  'missing lifetime specifier'",
                    "    -> fungsi mengembalikan referensi tapi compiler",
                    "       tidak tahu dari parameter yang mana. Tulis 'a",
                    "       di parameter yang jadi sumbernya.",
                    "",
                    "  'borrowed value does not live long enough'",
                    "    -> datanya mati lebih dulu daripada referensinya.",
                    "       Pindahkan deklarasi datanya ke scope yang lebih",
                    "       luar, atau kembalikan nilai yang dimiliki.",
                    "",
                    "  'lifetime may not live long enough'",
                    "    -> biasanya di closure atau thread: sesuatu yang",
                    "       dipinjam dipakai di tempat yang hidup lebih lama.",
                    "       `move` pada closure sering jadi jawabannya.",
                ]
            },
        ],
    },
    {
        "title": "16. Closure & Iterator",
        "sections": [
            {
                "body": [
                    "CLOSURE adalah fungsi tanpa nama yang bisa menangkap",
                    "variabel di sekitarnya.",
                    "",
                    "  let tambah = |a, b| a + b;",
                    "  let kuadrat = |x: i32| -> i32 { x * x };",
                    "  let batas = 10;",
                    "  let kecil = |x: &i32| *x < batas;   menangkap batas",
                    "",
                    "Tipe parameter biasanya disimpulkan, berbeda dari fungsi",
                    "biasa yang wajib menuliskannya.",
                    "",
                    "Tiga trait closure, yang menentukan APA yang boleh",
                    "dilakukannya pada tangkapannya:",
                    "",
                    "  Fn        cuma membaca tangkapannya; bisa dipanggil",
                    "            berkali-kali",
                    "  FnMut     mengubah tangkapannya; berkali-kali juga",
                    "  FnOnce    MENGKONSUMSI tangkapannya; sekali saja",
                    "",
                    "Compiler memilihkan yang paling longgar secara otomatis.",
                    "Kata kunci `move` memaksa closure MENGAMBIL kepemilikan",
                    "tangkapannya — wajib saat closure dikirim ke thread lain",
                    "atau disimpan lebih lama daripada scope-nya.",
                    "",
                    "ITERATOR adalah rangkaian nilai yang bisa ditelusuri",
                    "satu per satu. Di Rust ia MALAS: tidak terjadi apa-apa",
                    "sampai ada yang benar-benar meminta nilainya.",
                    "",
                    "  let v = vec![1, 2, 3, 4, 5];",
                    "  let hasil: Vec<i32> = v.iter()",
                    "      .filter(|x| **x % 2 == 0)",
                    "      .map(|x| x * 10)",
                    "      .collect();",
                    "",
                    "Tanpa `.collect()` di akhir, TIDAK ADA satu pun elemen",
                    "yang diproses — dan compiler akan memperingatkan bahwa",
                    "iteratormu tidak dipakai.",
                    "",
                    "Tiga cara membuat iterator dari koleksi, dan bedanya",
                    "soal kepemilikan:",
                    "  .iter()       memberi &T      koleksinya tetap milikmu",
                    "  .iter_mut()   memberi &mut T  boleh diubah",
                    "  .into_iter()  memberi T       koleksinya DIKONSUMSI",
                    "",
                    "Adaptor (malas, mengembalikan iterator lagi):",
                    "  map filter enumerate zip rev skip take chain flat_map",
                    "  filter_map take_while skip_while step_by peekable",
                    "",
                    "Konsumen (memaksa iterator berjalan):",
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
                    "Yang layak dicatat: rantai iterator di Rust sama",
                    "cepatnya dengan perulangan for yang ditulis tangan.",
                    "Compiler membongkarnya habis lewat inlining, dan tidak",
                    "ada koleksi perantara yang dibuat di tengah rantai.",
                    "Inilah yang di Rust disebut ZERO-COST ABSTRACTION:",
                    "kode yang lebih terbaca tanpa harus membayarnya.",
                    "",
                    "`\"Andi\".into()` memakai trait Into untuk mengubah &str",
                    "jadi String. Ia lebih pendek daripada `String::from(...)`",
                    "dan sangat sering dipakai saat mengisi struct.",
                    "",
                    "Tanda bintang berlapis (`**x`) muncul karena `filter`",
                    "memberi referensi ke item iterator, dan item iterator",
                    "dari `.iter()` sudah berupa referensi. Kalau itu",
                    "mengganggu, `.copied()` atau `.cloned()` di awal rantai",
                    "membuatnya hilang.",
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
                    "Semua item bersifat PRIVAT secara bawaan. `pub`",
                    "membukanya.",
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
                    "`use` memendekkan jalurnya:",
                    "  use matematika::lanjut::pangkat;",
                    "  use std::collections::{HashMap, HashSet};",
                    "  use std::io::{self, Write};",
                    "  use std::fmt::Result as HasilFormat;",
                    "",
                    "Jalur relatif:",
                    "  crate::  dari akar crate",
                    "  super::  satu tingkat ke atas",
                    "  self::   modul ini sendiri",
                    "",
                    "CARGO adalah build tool sekaligus package manager:",
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
                    "`cargo check` adalah perintah yang paling sering dipakai",
                    "saat sedang menulis: ia menjalankan seluruh pemeriksaan",
                    "tipe dan borrow tanpa melewati tahap penghasilan kode.",
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
                    "EDITION bukan versi bahasa melainkan sekumpulan aturan",
                    "yang boleh berubah tanpa merusak kode lama. Yang ada:",
                    "2015, 2018, 2021, dan 2024. Crate ber-edition berbeda",
                    "bisa saling dipakai tanpa masalah — itulah seluruh",
                    "gunanya.",
                    "",
                    "Penomoran versi dependensi mengikuti semver:",
                    "  \"1\"       apa pun 1.x.y, asal bukan 2.0",
                    "  \"1.2\"     apa pun 1.2.x ke atas, di bawah 2.0",
                    "  \"=1.2.3\"  persis itu saja",
                    "",
                    "Cargo.lock mencatat versi yang BENAR-BENAR terpasang.",
                    "Untuk aplikasi, berkas ini WAJIB masuk ke git: itulah",
                    "yang membuat build hari ini dan build enam bulan lagi",
                    "menghasilkan binari yang sama. Untuk library, biasanya",
                    "tidak.",
                    "",
                    "Dokumentasi ditulis dengan tiga garis miring dan",
                    "mendukung Markdown:",
                    "",
                    "  /// Menjumlahkan dua bilangan.",
                    "  ///",
                    "  /// # Contoh",
                    "  /// ```",
                    "  /// assert_eq!(tambah(2, 3), 5);",
                    "  /// ```",
                    "  pub fn tambah(a: i32, b: i32) -> i32 { a + b }",
                    "",
                    "Yang istimewa: contoh di dalam blok kode itu IKUT",
                    "DIJALANKAN oleh `cargo test`. Dokumentasi yang bohong",
                    "jadi tes yang gagal — fitur yang tidak dimiliki",
                    "kebanyakan bahasa lain.",
                ]
            },
        ],
    },
    {
        "title": "18. Smart Pointer: Box, Rc & RefCell",
        "sections": [
            {
                "body": [
                    "Smart pointer adalah tipe yang berperilaku seperti",
                    "referensi tapi membawa kemampuan tambahan.",
                    "",
                    "BOX<T> — menaruh data di heap.",
                    "",
                    "  let b = Box::new(5);",
                    "  println!(\"{}\", *b);",
                    "",
                    "Tiga alasan memakainya:",
                    "  1. Tipe REKURSIF. Tanpa Box, ukurannya tak terhingga:",
                    "     enum Daftar { Isi(i32, Box<Daftar>), Habis }",
                    "  2. Memindahkan data besar tanpa menyalinnya.",
                    "  3. Menyimpan `dyn Trait`, yang ukurannya tidak",
                    "     diketahui saat kompilasi.",
                    "",
                    "RC<T> — Reference Counted, kepemilikan BERSAMA.",
                    "",
                    "  use std::rc::Rc;",
                    "  let a = Rc::new(vec![1, 2, 3]);",
                    "  let b = Rc::clone(&a);       hitungan naik jadi 2",
                    "  Rc::strong_count(&a)         2",
                    "",
                    "Rc melonggarkan aturan 'satu pemilik': datanya dilepas",
                    "saat pemilik TERAKHIR hilang. `Rc::clone` TIDAK menyalin",
                    "datanya — ia cuma menaikkan hitungan, jadi murah.",
                    "",
                    "Rc HANYA untuk satu thread. Versi antar-thread-nya",
                    "`Arc` (Atomic Rc), sedikit lebih lambat karena",
                    "hitungannya harus aman dari balapan.",
                    "",
                    "REFCELL<T> — memindahkan pemeriksaan borrow ke RUNTIME.",
                    "",
                    "  use std::cell::RefCell;",
                    "  let c = RefCell::new(5);",
                    "  *c.borrow_mut() += 1;",
                    "  println!(\"{}\", c.borrow());",
                    "",
                    "Aturannya sama persis (banyak pembaca ATAU satu penulis),",
                    "tapi pelanggarannya menghasilkan PANIC saat program",
                    "jalan, bukan error kompilasi. Itu pertukaran yang sadar,",
                    "bukan lubang: ia dipakai saat compiler tidak bisa",
                    "membuktikan sesuatu yang kamu tahu benar.",
                    "",
                    "Gabungan `Rc<RefCell<T>>` adalah idiom untuk data yang",
                    "dimiliki bersama DAN bisa diubah. Ia dipakai di graf,",
                    "pohon dengan tautan ke induk, dan pola observer.",
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
                    "Perhatikan hitungan Rc naik jadi 3 di dalam blok lalu",
                    "turun lagi jadi 1 begitu blok berakhir. Itulah",
                    "mekanismenya: data dilepas saat hitungannya mencapai nol.",
                    "",
                    "PERINGATAN — Rc bisa BOCOR. Dua objek yang saling",
                    "menunjuk dengan Rc membuat hitungan keduanya tidak",
                    "pernah nol, dan memorinya tidak pernah dilepas. Ini",
                    "satu-satunya kebocoran memori yang mungkin terjadi di",
                    "Rust aman, dan pemutusnya `Weak<T>`: referensi yang",
                    "TIDAK menaikkan hitungan.",
                    "",
                    "Pola yang lazim: anak memegang `Rc` ke datanya, dan",
                    "tautan balik ke induk memakai `Weak`.",
                    "",
                    "Kapan memakai apa:",
                    "  &T                 hampir selalu. Mulai dari sini.",
                    "  Box<T>             perlu heap, rekursif, atau dyn Trait",
                    "  Rc<T>              beberapa pemilik, satu thread",
                    "  Arc<T>             beberapa pemilik, antar thread",
                    "  RefCell<T>         perlu mengubah lewat &",
                    "  Rc<RefCell<T>>     dimiliki bersama dan bisa diubah",
                    "  Arc<Mutex<T>>      sama, tapi antar thread",
                ]
            },
        ],
    },
    {
        "title": "19. Concurrency: Thread & Channel",
        "sections": [
            {
                "body": [
                    "Janji Rust untuk concurrency disebut FEARLESS",
                    "CONCURRENCY, dan artinya harfiah: data race adalah",
                    "error KOMPILASI, bukan bug yang muncul sekali seminggu",
                    "di produksi.",
                    "",
                    "Yang menegakkannya dua trait penanda:",
                    "  Send   aman DIPINDAHKAN ke thread lain",
                    "  Sync   aman DIAKSES dari beberapa thread lewat &",
                    "",
                    "Compiler menyimpulkan keduanya otomatis. Rc BUKAN Send",
                    "(hitungannya tidak atomik), jadi mencoba mengirim Rc ke",
                    "thread lain gagal saat kompilasi — kesalahan yang di",
                    "C++ menghasilkan kerusakan memori acak.",
                    "",
                    "Membuat thread:",
                    "  use std::thread;",
                    "",
                    "  let h = thread::spawn(|| {",
                    "      println!(\"dari thread\");",
                    "  });",
                    "  h.join().unwrap();      tunggu selesai",
                    "",
                    "`move` hampir selalu diperlukan supaya closure memiliki",
                    "data yang dipakainya — compiler tidak bisa membuktikan",
                    "thread-nya selesai sebelum datanya mati.",
                    "",
                    "CHANNEL — berkirim pesan antar thread:",
                    "",
                    "  use std::sync::mpsc;",
                    "  let (kirim, terima) = mpsc::channel();",
                    "  kirim.send(nilai).unwrap();",
                    "  let x = terima.recv().unwrap();",
                    "",
                    "mpsc = multiple producer, single consumer: pengirimnya",
                    "boleh banyak (clone saja), penerimanya satu.",
                    "",
                    "Filosofinya: 'jangan berkomunikasi dengan berbagi memori;",
                    "berbagilah memori dengan berkomunikasi.'",
                    "",
                    "MUTEX — kalau memang harus berbagi:",
                    "",
                    "  use std::sync::{Arc, Mutex};",
                    "  let data = Arc::new(Mutex::new(0));",
                    "  *data.lock().unwrap() += 1;",
                    "",
                    "Di Rust, Mutex MEMBUNGKUS datanya, bukan berdiri di",
                    "sampingnya. Akibatnya kamu TIDAK BISA mengakses data",
                    "tanpa mengunci — kesalahan paling umum di C dan Java",
                    "dijadikan mustahil oleh tipenya.",
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
                    "DUA hal di kode itu yang wajib diperhatikan, dan keduanya",
                    "soal DETERMINISME:",
                    "",
                    "  1. Hasilnya DIURUTKAN sebelum dicetak. Urutan selesainya",
                    "     thread memang tidak pasti; program yang keluarannya",
                    "     berubah tiap kali dijalankan mustahil diuji.",
                    "",
                    "  2. `drop(kirim)` wajib. Perulangan `terima.iter()`",
                    "     berhenti saat SEMUA pengirim hilang. Pengirim asli",
                    "     masih hidup di main, jadi tanpa drop program",
                    "     menggantung selamanya — bug yang tidak menghasilkan",
                    "     error apa pun, cuma diam.",
                    "",
                    "Hitungan akhir 8000 dijamin persis. Di Java atau C tanpa",
                    "penguncian, angka itu akan meleset acak karena `+= 1`",
                    "sebenarnya tiga operasi (baca, tambah, tulis) yang bisa",
                    "disela. Rust tidak mengizinkanmu menulisnya tanpa lock.",
                    "",
                    "Untuk pekerjaan yang MENUNGGU (jaringan, berkas) alih-",
                    "alih MENGHITUNG, dunia Rust memakai async/await dengan",
                    "runtime seperti tokio. Bentuknya mirip, tapi tugasnya",
                    "ribuan sekaligus di atas segelintir thread.",
                ]
            },
        ],
    },
    {
        "title": "20. Testing & Dokumentasi",
        "sections": [
            {
                "body": [
                    "Testing bukan pustaka tambahan di Rust — ia bagian dari",
                    "bahasanya dan dari cargo.",
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
                    "`#[cfg(test)]` berarti modul itu HANYA dikompilasi saat",
                    "`cargo test`. Ia tidak ikut masuk ke binari rilis sama",
                    "sekali — nol ongkos.",
                    "",
                    "`use super::*;` mengimpor semua dari modul induknya,",
                    "termasuk yang privat. Tes di Rust boleh menguji fungsi",
                    "internal, berbeda dari kebanyakan bahasa.",
                    "",
                    "Makro assert:",
                    "  assert!(kondisi)",
                    "  assert!(kondisi, \"pesan {}\", x)",
                    "  assert_eq!(kiri, kanan)",
                    "  assert_ne!(kiri, kanan)",
                    "",
                    "Kalau gagal, assert_eq! mencetak KEDUA nilainya — jauh",
                    "lebih berguna daripada 'assertion failed' polos.",
                    "",
                    "Atribut tambahan:",
                    "  #[should_panic]                  tes lulus kalau panic",
                    "  #[should_panic(expected = \"..\")] panic dengan pesan itu",
                    "  #[ignore]                        dilewati kecuali diminta",
                    "",
                    "Tes yang mengembalikan Result boleh memakai `?`:",
                    "  #[test]",
                    "  fn parse_benar() -> Result<(), String> { ... }",
                    "",
                    "Menjalankan:",
                    "  cargo test",
                    "  cargo test nama_tes          hanya yang namanya cocok",
                    "  cargo test -- --nocapture    tampilkan println!",
                    "  cargo test -- --test-threads=1   berurutan",
                    "  cargo test -- --ignored      justru yang di-ignore",
                    "",
                    "Tes di src/ adalah tes UNIT (boleh menyentuh yang",
                    "privat). Tes di tests/ adalah tes INTEGRASI: tiap berkas",
                    "crate tersendiri yang cuma melihat API publik.",
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
                    "Perhatikan nilai yang dipilih di tes: 85 dan 84, 75 dan",
                    "74, 60 dan 59. Menguji tepat di batas adalah yang paling",
                    "berharga — di situlah `..=` versus `..` dan `>=` versus",
                    "`>` salah ketik. Nilai di tengah rentang hampir tidak",
                    "pernah menemukan bug.",
                    "",
                    "Blok ``` di dalam komentar dokumentasi adalah DOCTEST:",
                    "`cargo test` benar-benar mengompilasi dan menjalankannya.",
                    "Akibatnya contoh di dokumentasi tidak bisa membusuk",
                    "diam-diam — begitu API berubah, dokumentasinya gagal",
                    "sebagai tes. Ini salah satu hal terbaik di ekosistem",
                    "Rust dan jarang ada di bahasa lain.",
                    "",
                    "Untuk mengukur berapa banyak kode yang tersentuh tes:",
                    "  cargo install cargo-llvm-cov",
                    "  cargo llvm-cov --html",
                ]
            },
        ],
    },
    {
        "title": "21. Trait Standar & Konversi",
        "sections": [
            {
                "body": [
                    "Pustaka standar Rust menyediakan sekumpulan trait yang",
                    "menyambungkan tipe buatanmu ke seluruh ekosistem.",
                    "Mengimplementasi satu sering memberi banyak hal gratis.",
                    "",
                    "FROM & INTO — konversi antar tipe:",
                    "",
                    "  impl From<u32> for Nilai {",
                    "      fn from(n: u32) -> Self { Nilai(n) }",
                    "  }",
                    "",
                    "Dengan itu kamu dapat `Nilai::from(80)` DAN `80.into()`",
                    "sekaligus — Into diimplementasi otomatis dari From.",
                    "Jangan pernah mengimplementasi Into langsung.",
                    "",
                    "Pasangan yang gagal-mungkin: TryFrom / TryInto,",
                    "kembaliannya Result.",
                    "",
                    "DEFAULT — nilai bawaan:",
                    "  #[derive(Default)]",
                    "  struct Setelan { tebal: bool, ukuran: u32 }",
                    "",
                    "  let s = Setelan::default();",
                    "  let s = Setelan { ukuran: 14, ..Default::default() };",
                    "",
                    "Baris terakhir itu pola yang sangat berguna: isi yang",
                    "kamu pedulikan, sisanya bawaan.",
                    "",
                    "DISPLAY vs DEBUG, dan bedanya bukan gaya:",
                    "  Debug    {:?}  untuk PROGRAMMER. Bisa di-derive.",
                    "  Display  {}    untuk PENGGUNA. Harus ditulis tangan,",
                    "                 karena tidak ada yang bisa menebak",
                    "                 bagaimana tipemu sebaiknya dibaca orang.",
                    "",
                    "DROP — apa yang terjadi saat nilainya dilepas:",
                    "  impl Drop for Koneksi {",
                    "      fn drop(&mut self) { println!(\"koneksi ditutup\"); }",
                    "  }",
                    "",
                    "Ini padanan destructor, dan ia SELALU dipanggil — saat",
                    "scope berakhir, saat panic, saat apa pun. Kamu tidak",
                    "bisa memanggil `.drop()` langsung; pakai `drop(x)`.",
                    "",
                    "Trait perbandingan, dan urutan ketergantungannya:",
                    "  PartialEq  ==  dan  !=",
                    "  Eq         PartialEq + refleksif (butuh PartialEq)",
                    "  PartialOrd <  >  <=  >=  (butuh PartialEq)",
                    "  Ord        urutan total (butuh Eq + PartialOrd)",
                    "",
                    "f64 hanya PartialOrd, tidak Ord, karena NaN tidak bisa",
                    "dibandingkan dengan apa pun — termasuk dirinya sendiri.",
                    "Itu sebabnya `vec_f64.sort()` tidak bisa dikompilasi dan",
                    "kamu harus menulis `sort_by(|a, b| a.partial_cmp(b)",
                    ".unwrap())`.",
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
                    "`#[derive(Ord)]` mengurutkan field SESUAI URUTAN",
                    "PENULISANNYA: mayor dulu, baru minor, baru tambal.",
                    "Itulah kenapa v1.10.0 benar berada sesudah v1.4.2,",
                    "sesuatu yang akan salah kalau versi dibandingkan sebagai",
                    "teks.",
                    "",
                    "Trik yang layak diingat: `Result<Vec<u32>, _>` sebagai",
                    "target `collect()`. Sebuah iterator berisi Result bisa",
                    "dikumpulkan jadi SATU Result berisi Vec — kalau ada satu",
                    "saja yang Err, hasilnya Err. Satu baris menggantikan",
                    "perulangan dengan pemeriksaan di dalamnya.",
                    "",
                    "Kebiasaan yang bagus: `#[derive(Debug)]` di hampir",
                    "SEMUA tipe. Ongkosnya nol di rilis, dan tanpa itu kamu",
                    "tidak bisa mencetak tipemu saat sedang mencari bug —",
                    "persis saat kamu paling membutuhkannya.",
                ]
            },
        ],
    },
    {
        "title": "22. Membaca Masukan & Berkas",
        "sections": [
            {
                "body": [
                    "Membaca satu baris dari terminal:",
                    "",
                    "  use std::io;",
                    "",
                    "  let mut baris = String::new();",
                    "  io::stdin().read_line(&mut baris).unwrap();",
                    "  let n: i32 = baris.trim().parse().unwrap();",
                    "",
                    "`read_line` MENAMBAHKAN ke string, tidak menggantinya.",
                    "Kalau kamu memakainya berkali-kali tanpa mengosongkan,",
                    "isinya menumpuk — kesalahan yang sangat sering di awal.",
                    "",
                    "`.trim()` wajib: read_line menyertakan karakter baris",
                    "baru, dan `\"5\\n\".parse::<i32>()` adalah galat.",
                    "",
                    "Membaca SELURUH masukan sekaligus:",
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
                    "BERKAS — cara singkat, untuk yang muat di memori:",
                    "",
                    "  use std::fs;",
                    "  let isi = fs::read_to_string(\"data.txt\")?;",
                    "  fs::write(\"keluar.txt\", isi)?;",
                    "",
                    "Untuk berkas besar, jangan tarik seluruhnya:",
                    "",
                    "  use std::fs::File;",
                    "  use std::io::{BufRead, BufReader};",
                    "",
                    "  let f = File::open(\"besar.txt\")?;",
                    "  for baris in BufReader::new(f).lines() {",
                    "      ...",
                    "  }",
                    "",
                    "ARGUMEN baris perintah:",
                    "  use std::env;",
                    "  let arg: Vec<String> = env::args().collect();",
                    "  arg[0] selalu nama programnya sendiri.",
                    "",
                    "Untuk CLI sungguhan, crate `clap` menangani penguraian,",
                    "bantuan, dan validasi dengan satu derive.",
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
                    "`filter_map(|t| t.parse().ok())` adalah idiom yang layak",
                    "diingat: `parse()` memberi Result, `.ok()` mengubahnya",
                    "jadi Option, dan `filter_map` membuang yang None. Satu",
                    "baris untuk 'ambil yang bisa diurai, abaikan sisanya'.",
                    "",
                    "Hati-hati: membuang kegagalan diam-diam TIDAK selalu",
                    "benar. Kalau masukan yang salah seharusnya jadi keluhan,",
                    "kumpulkan ke `Result<Vec<_>, _>` seperti di materi trait",
                    "standar.",
                    "",
                    "`fn main() -> io::Result<()>` memungkinkan `?` dipakai",
                    "di dalam main. Kalau ada yang gagal, program keluar",
                    "dengan kode bukan-nol dan mencetak galatnya — persis",
                    "yang diharapkan sebuah program baris perintah.",
                    "",
                    "`std::env::temp_dir()` memberi folder sementara yang",
                    "benar di sistem operasi mana pun, dan `.join()`",
                    "menyambung path dengan pemisah yang tepat. Menulis",
                    "\"/tmp/berkas.txt\" langsung akan gagal di Windows.",
                ]
            },
        ],
    },
    {
        "title": "23. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan struct, enum, trait,",
                    "Result, iterator, dan pemisahan tanggung jawab dalam",
                    "satu program yang utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang sederhana.",
                    "Yang penting bukan fiturnya melainkan CARA bagiannya",
                    "dipisah.",
                    "",
                    "Tiga lapisan, panah ketergantungan satu arah:",
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
                    "Ujinya satu kalimat: kalau program ini diubah jadi",
                    "server web, berapa banyak kode yang harus disentuh?",
                    "Jawaban yang benar: hanya main.",
                    "",
                    "Di Rust, pemisahan ini punya bonus yang tidak ada di",
                    "bahasa lain: karena Gudang tidak pernah mencetak, tipe",
                    "kembaliannya WAJIB membawa seluruh informasi kegagalan.",
                    "Compiler-lah yang memaksamu merancang API yang bisa",
                    "diuji.",
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
                    "Empat keputusan di program itu yang layak ditiru:",
                    "",
                    "  1. GalatGudang adalah ENUM, bukan String. Pemanggil",
                    "     bisa MEMBEDAKAN kegagalan dan bereaksi berbeda, dan",
                    "     `match` atasnya diperiksa kelengkapannya oleh",
                    "     compiler. Galat berupa teks kehilangan keduanya.",
                    "",
                    "  2. `impl Display for GalatGudang` memisahkan BENTUK",
                    "     galat dari KALIMATNYA. Menerjemahkan pesan ke",
                    "     bahasa lain nanti cukup menyentuh satu fungsi.",
                    "",
                    "  3. `semua()` dan `stok_menipis()` MENGURUTKAN sebelum",
                    "     mengembalikan. HashMap tidak punya urutan, dan di",
                    "     Rust urutannya benar-benar berubah tiap kali",
                    "     program dijalankan. Tanpa pengurutan, keluarannya",
                    "     mustahil diuji.",
                    "",
                    "  4. Gudang tidak memanggil println! sama sekali. Itu",
                    "     yang membuat seluruh aturannya bisa diuji dengan",
                    "     `assert_eq!` tanpa membaca layar.",
                    "",
                    "Langkah berikutnya kalau kamu ingin melanjutkannya:",
                    "  - Simpan ke JSON dengan crate serde.",
                    "  - Terima perintah dari baris perintah dengan clap.",
                    "  - Sembunyikan penyimpanan di balik sebuah trait, supaya",
                    "    Gudang tidak tahu datanya di berkas, di database,",
                    "    atau cuma di memori saat tes.",
                    "  - Tulis modul #[cfg(test)] untuk Gudang — perhatikan",
                    "    ini langsung bisa dilakukan tanpa mengubah satu baris",
                    "    pun, justru karena keputusan nomor 4.",
                ]
            },
        ],
    },
]
