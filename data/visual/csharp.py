"""Gambar konsep kurikulum C#. Skema: inti/visual.py."""

VISUAL = {
    "Pengenalan C# & .NET": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "Dari kode C# sampai teks muncul di layar",
            "ket": "Compiler cuma menghasilkan IL. Instruksi mesinnya baru dibuat "
                   "JIT waktu program jalan, sesuai prosesor yang sedang dipakai.",
            "langkah": [
                {"jenis": "masukan", "teks": "Program.cs (kode C#)"},
                {"jenis": "proses", "teks": "compiler C# (dotnet build)"},
                {"jenis": "proses", "teks": "IL di dalam berkas .dll"},
                {"jenis": "proses", "teks": "JIT menerjemahkan ke mesin"},
                {"jenis": "keluaran", "teks": "Halo Dunia!"},
            ],
        },
    ],
    "Variabel, Tipe Data & Konversi": [
        {
            "setelah": 0,
            "jenis": "variabel",
            "judul": "Empat variabel dari contoh pertama, tiap nilai dengan tipenya",
            "ket": "Tipe ditulis di depan nama dan nggak bisa berubah lagi. "
                   "Dengan var, compiler menyimpulkan tipe yang sama dari nilai awalnya.",
            "isi": [
                ["umur", "20", "int"],
                ["nama", "\"Andi\"", "string"],
                ["tinggi", "172.5", "double"],
                ["lulus", "true", "bool"],
            ],
        },
    ],
    "Operator & Ekspresi": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Jalannya kosong?.Length ?? -1 waktu kosong berisi null",
            "ket": "?. berhenti di tempat dan menghasilkan null tanpa memanggil "
                   "Length. Lalu ?? mengganti null itu dengan -1.",
            "langkah": [
                {"jenis": "mulai", "teks": "kosong?.Length ?? -1"},
                {"jenis": "keputusan", "teks": "kosong bukan null?", "tidak": 3},
                {"jenis": "proses", "teks": "ambil kosong.Length", "ke": 4},
                {"jenis": "proses", "teks": "?. jadi null, ?? pakai -1"},
                {"jenis": "keluaran", "teks": "cetak hasilnya (di sini -1)"},
            ],
        },
    ],
    "Input, Output & String": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "nama = nama.ToUpper() membuat string baru, yang lama ditinggal",
            "ket": "String immutable, jadi ToUpper nggak mengubah \"Andi\". "
                   "Variabel nama dialihkan ke objek baru. Nilai \"Andi\" dipakai "
                   "sebagai contoh.",
            "tumpukan": [["nama", "@S2"]],
            "heap": [
                {"id": "S1", "isi": "\"Andi\" (string lama)"},
                {"id": "S2", "isi": "\"ANDI\" (hasil ToUpper)"},
            ],
            "label_tumpukan": "variabel",
            "label_heap": "objek string",
        },
    ],
    "Percabangan: if, switch & Pattern Matching": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Switch expression Grade dicocokkan dari pola paling atas",
            "ket": "Pencocokan berhenti di pola pertama yang cocok. Nilai 78 "
                   "gagal di >= 85, lalu cocok di >= 75 dan menghasilkan B.",
            "langkah": [
                {"jenis": "keputusan", "teks": "nilai >= 85?", "tidak": 2},
                {"jenis": "keluaran", "teks": "\"A\"", "ke": 9},
                {"jenis": "keputusan", "teks": "nilai >= 75?", "tidak": 4},
                {"jenis": "keluaran", "teks": "\"B\"", "ke": 9},
                {"jenis": "keputusan", "teks": "nilai >= 60?", "tidak": 6},
                {"jenis": "keluaran", "teks": "\"C\"", "ke": 9},
                {"jenis": "keputusan", "teks": "nilai >= 40?", "tidak": 8},
                {"jenis": "keluaran", "teks": "\"D\"", "ke": 9},
                {"jenis": "keluaran", "teks": "\"E\" (pola _)"},
                {"jenis": "selesai", "teks": "kembalikan hasilnya"},
            ],
        },
    ],
    "Perulangan: for, while, foreach": [
        {
            "setelah": 0,
            "jenis": "alur",
            "judul": "for (int i = 0; i < 5; i++) dijalankan langkah demi langkah",
            "ket": "Nilai awal cuma sekali. Syarat dicek sebelum tiap putaran, "
                   "dan i++ jalan sesudah badan perulangan. Hasilnya 0 1 2 3 4.",
            "langkah": [
                {"jenis": "mulai", "teks": "int i = 0"},
                {"jenis": "keputusan", "teks": "i < 5?", "tidak": 4},
                {"jenis": "keluaran", "teks": "Console.WriteLine(i)"},
                {"jenis": "proses", "teks": "i++", "ke": 1},
                {"jenis": "selesai", "teks": "keluar dari for"},
            ],
        },
    ],
    "Array & Indeks": [
        {
            "setelah": 2,
            "jenis": "larik",
            "judul": "Array urut sesudah Array.Sort, dan rentang urut[^2..]",
            "ket": "^2 artinya dua dari akhir, yaitu index 5. Rentang sampai "
                   "habis mengambil index 5 dan 6: dua nilai terbesar, 92 dan 95.",
            "nama": "urut",
            "isi": ["59", "65", "71", "78", "88", "92", "95"],
            "penunjuk": {"^2": 5, "^1": 6},
            "rentang": [5, 7],
        },
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "int disalin isinya, int[] cuma disalin alamatnya",
            "ket": "b = a menyalin angka 5, jadi mengubah b nggak menyentuh a. "
                   "y = x menyalin alamat, jadi y[0] = 9 ikut mengubah x[0].",
            "tumpukan": [["a", "5"], ["b", "9"], ["x", "@A1"], ["y", "@A1"]],
            "heap": [{"id": "A1", "isi": "int[] { 9 }"}],
            "label_tumpukan": "variabel",
            "label_heap": "objek array",
        },
    ],
    "List, Dictionary & Koleksi Generik": [
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "mode": "antrean",
            "judul": "Queue sesudah tiga Enqueue lalu satu Dequeue",
            "ket": "Andi datang duluan, jadi Andi yang dilayani duluan. "
                   "Peek sekarang melihat Budi tanpa mengambilnya.",
            "isi": ["Budi", "Cici"],
            "operasi": "Dequeue() -> Andi",
        },
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "judul": "Stack sesudah tiga Push lalu satu Pop",
            "ket": "halaman-3 ditaruh terakhir, jadi dia yang diambil duluan, "
                   "persis tombol Back di browser.",
            "isi": ["halaman-1", "halaman-2"],
            "label": "tumpuk (bawah ke atas)",
            "operasi": "Pop() -> halaman-3",
        },
    ],
    "Method, Parameter & Overloading": [
        {
            "setelah": 4,
            "jenis": "tumpukan",
            "judul": "Tumpukan pemanggilan Faktorial(3) waktu sampai di kasus dasar",
            "ket": "Tiap panggilan menunggu panggilan di atasnya. Faktorial(1) "
                   "mengembalikan 1, lalu tumpukannya dibongkar: 2 * 1, lalu 3 * 2.",
            "isi": ["Main()", "Faktorial(3)", "Faktorial(2)", "Faktorial(1)"],
            "label": "bawah ke atas",
            "operasi": "n <= 1, kembalikan 1",
        },
    ],
    "Nullable & Null-Safety": [
        {
            "setelah": 0,
            "jenis": "memori",
            "judul": "Tipe nilai menyimpan isinya, tipe referensi menyimpan alamat",
            "ket": "umur (int?) dan pasti (int) menyimpan nilainya langsung. kota dan "
                   "masukan (string?) menyimpan alamat, dan alamat kota kosong (null).",
            "tumpukan": [
                ["umur", "null"],
                ["pasti", "0"],
                ["kota", "null"],
                ["masukan", "@S1"],
            ],
            "heap": [{"id": "S1", "isi": "\"  andi \""}],
            "label_tumpukan": "variabel",
            "label_heap": "objek",
        },
    ],
    "Class & Objek": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Satu class Murid, tiga objek dengan isinya masing-masing",
            "ket": "Di contoh, ketiga objek dipegang array kelas. Di sini "
                   "disederhanakan jadi tiga variabel supaya panahnya kelihatan.",
            "tumpukan": [["andi", "@M1"], ["budi", "@M2"], ["cici", "@M3"]],
            "heap": [
                {"id": "M1", "isi": "Murid _nama=Andi _nilai=92"},
                {"id": "M2", "isi": "Murid _nama=Budi _nilai=78"},
                {"id": "M3", "isi": "Murid _nama=Cici _nilai=64"},
            ],
            "label_tumpukan": "variabel",
            "label_heap": "objek",
        },
    ],
    "Property, Constructor & Inisialisasi": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Dua objek Rekening, satu _urutan milik class",
            "ket": "Nomor, Pemilik, dan Saldo ada di tiap objek. _urutan yang "
                   "static cuma satu dan ikut class-nya, jadi nilainya 2 sesudah "
                   "dua rekening dibuat.",
            "tumpukan": [["a", "@R1"], ["b", "@R2"]],
            "heap": [
                {"id": "R1", "isi": "AC0001 Andi saldo 450000"},
                {"id": "R2", "isi": "AC0002 Budi saldo 100000"},
                {"id": "Rekening", "isi": "static _urutan = 2"},
            ],
            "label_tumpukan": "variabel",
            "label_heap": "objek dan class",
        },
    ],
    "Pewarisan & Polimorfisme": [
        {
            "setelah": 2,
            "jenis": "pohon",
            "judul": "Bangun sebagai induk abstract, dua turunan dengan rumusnya",
            "ket": "Bangun cuma berjanji punya Luas dan Keliling. Tiap turunan "
                   "mengisi rumusnya, dan b.Luas() memilih rumus milik objeknya.",
            "akar": {"teks": "Bangun (abstract)", "anak": [
                {"teks": "Persegi", "anak": [
                    {"teks": "Luas: sisi*sisi"},
                    {"teks": "Keliling: 4*sisi"},
                ]},
                {"teks": "Lingkaran", "anak": [
                    {"teks": "Luas: PI*r*r"},
                    {"teks": "Keliling: 2*PI*r"},
                    {"teks": "Ringkas + (r=..)"},
                ]},
            ]},
        },
    ],
    "Interface": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "rak.Sort() mengurutkan buku lewat CompareTo",
            "ket": "Tahun dibandingkan dulu. Dua buku tahun 2021 diurutkan "
                   "menurut judulnya, jadi Basis Data mendahului Pemrograman C#.",
            "panah": "rak.Sort() memanggil CompareTo",
            "tabel": [
                {"nama": "sebelum Sort", "kolom": ["Tahun", "Judul"],
                 "baris": [[2021, "Pemrograman C#"], [2018, "Algoritma"],
                           [2021, "Basis Data"]]},
                {"nama": "sesudah Sort", "kolom": ["Tahun", "Judul"],
                 "baris": [[2018, "Algoritma"], [2021, "Basis Data"],
                           [2021, "Pemrograman C#"]],
                 "sorot_kolom": ["Tahun"]},
            ],
        },
    ],
    "Struct, Record & Tipe Nilai": [
        {
            "setelah": 2,
            "jenis": "memori",
            "judul": "Struct disalin isinya, class disalin alamatnya",
            "ket": "s2 punya salinan sendiri, jadi s1.X tetap 1. c1 dan c2 "
                   "menunjuk objek yang sama, jadi c2.X = 99 ikut terlihat dari c1.",
            "tumpukan": [
                ["s1", "{X=1, Y=2}"],
                ["s2", "{X=99, Y=2}"],
                ["c1", "@C1"],
                ["c2", "@C1"],
            ],
            "heap": [{"id": "C1", "isi": "TitikC {X=99, Y=2}"}],
            "label_tumpukan": "variabel",
            "label_heap": "objek class",
        },
    ],
    "Enum & Konstanta Bernama": [
        {
            "setelah": 2,
            "jenis": "bit",
            "judul": "Izin.Baca | Izin.Tulis disimpan sebagai bit 0011",
            "ket": "Baca bit paling kanan (1), Tulis bit kedua (2). Digabung "
                   "dengan | jadi 3, dan HasFlag(Izin.Tulis) bernilai True.",
            "angka": 3,
            "lebar": 4,
            "label": "editor = Baca | Tulis (3)",
        },
        {
            "setelah": 2,
            "jenis": "bit",
            "judul": "Sesudah |= Izin.Hapus lalu &= ~Izin.Baca",
            "ket": "|= menyalakan bit Hapus (4) jadi 0111. &= ~Baca mematikan "
                   "bit paling kanan, jadi tinggal Tulis, Hapus: 0110, yaitu 6.",
            "angka": 6,
            "lebar": 4,
            "label": "editor = Tulis, Hapus (6)",
        },
    ],
    "Exception & Penanganan Galat": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Satu putaran foreach: d.Bayar(t) di dalam try",
            "ket": "Begitu throw terjadi, sisa Bayar dilewati dan catch yang "
                   "tipenya cocok yang jalan. Perulangan tetap lanjut ke tagihan "
                   "berikutnya.",
            "langkah": [
                {"jenis": "mulai", "teks": "try: d.Bayar(t)"},
                {"jenis": "keputusan", "teks": "t lebih dari 0?", "tidak": 5},
                {"jenis": "keputusan", "teks": "t <= Saldo?", "tidak": 6},
                {"jenis": "proses", "teks": "Saldo -= t"},
                {"jenis": "keluaran", "teks": "Bayar ... -> sisa ...", "ke": 7},
                {"jenis": "keluaran", "teks": "catch ArgumentOutOfRange", "ke": 7},
                {"jenis": "keluaran", "teks": "catch SaldoKurangException"},
                {"jenis": "selesai", "teks": "tagihan berikutnya"},
            ],
        },
    ],
    "Generic: Tipe sebagai Parameter": [
        {
            "setelah": 2,
            "jenis": "tumpukan",
            "judul": "Kotak<string>(2) sesudah apel dan jeruk masuk, lalu Ambil()",
            "ket": "Ambil mengambil isi terakhir (_isi[^1]), jadi jeruk keluar "
                   "duluan. Isinya tinggal apel, 1/2.",
            "isi": ["apel"],
            "label": "Kotak<string>",
            "operasi": "Ambil() -> jeruk",
        },
    ],
    "Delegate, Event & Lambda": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Saring(angka, n => n % 2 == 0) bertanya ke lambda tiap angka",
            "ket": "Saring nggak tahu syaratnya. Dia cuma memanggil syarat(n) dan "
                   "memasukkan angka yang dijawab true. Diringkas untuk angka 1 dan 2.",
            "pelaku": ["Main", "Saring", "lambda"],
            "pesan": [
                [0, 1, "Saring(angka, lambda)"],
                [1, 2, "syarat(1)"],
                [2, 1, "false, dilewati"],
                [1, 2, "syarat(2)"],
                [2, 1, "true, masuk hasil"],
                [1, 2, "... sampai syarat(10)"],
                [1, 0, "2 4 6 8 10"],
            ],
        },
    ],
    "LINQ: Bertanya pada Data": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Where lalu OrderByDescending pada data murid",
            "ket": "Where menyaring empat murid yang nilainya minimal 75 (baris "
                   "yang disorot). OrderByDescending mengurutkannya dari nilai tertinggi.",
            "panah": "Where(Nilai >= 75), urut Nilai turun",
            "tabel": [
                {"nama": "data", "kolom": ["Nama", "Kelas", "Nilai"],
                 "baris": [["Andi", "A", 88], ["Budi", "B", 72], ["Cici", "A", 95],
                           ["Dedi", "B", 64], ["Euis", "A", 79], ["Fajar", "B", 91]],
                 "sorot_baris": [0, 2, 4, 5]},
                {"nama": "hasil", "kolom": ["Nama", "Nilai"],
                 "baris": [["Cici", 95], ["Fajar", 91], ["Andi", 88], ["Euis", 79]]},
            ],
        },
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "GroupBy(m => m.Kelas) memecah enam murid jadi dua kelompok",
            "ket": "Tiap kelompok punya Key (A atau B) dan isinya sendiri, jadi "
                   "bisa ditanya Count, Average, dan murid terbaiknya.",
            "panah": "GroupBy(Kelas), lalu ringkas tiap kelompok",
            "tabel": [
                {"nama": "data", "kolom": ["Nama", "Kelas", "Nilai"],
                 "baris": [["Andi", "A", 88], ["Budi", "B", 72], ["Cici", "A", 95],
                           ["Dedi", "B", 64], ["Euis", "A", 79], ["Fajar", "B", 91]],
                 "sorot_kolom": ["Kelas"]},
                {"nama": "per kelas", "kolom": ["Key", "Count", "Rata-rata", "Terbaik"],
                 "baris": [["A", 3, "87,3", "Cici"], ["B", 3, "75,7", "Fajar"]]},
            ],
        },
    ],
    "Bekerja dengan Berkas": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Baris teks CSV jadi data bertipe lewat Skip, Split, dan int.Parse",
            "ket": "Baris judul dilewati Skip(1). Tiap baris lain dipecah di koma, "
                   "dan kolom nilai diubah dari teks jadi int.",
            "panah": "Skip(1), Split(','), int.Parse",
            "tabel": [
                {"nama": "nilai-belajar.csv", "kolom": ["baris teks"],
                 "baris": [["nama,kelas,nilai"], ["Andi,A,88"], ["Budi,B,72"],
                           ["Cici,A,95"]],
                 "sorot_baris": [0]},
                {"nama": "data", "kolom": ["Nama", "Kelas", "Nilai"],
                 "baris": [["Andi", "A", 88], ["Budi", "B", 72], ["Cici", "A", 95]],
                 "sorot_kolom": ["Nilai"]},
            ],
        },
    ],
    "IDisposable & using": [
        {
            "setelah": 2,
            "jenis": "alur",
            "judul": "Blok using di contoh Pencatat, sampai Dispose dipanggil",
            "ket": "Kurawal tutup memanggil Dispose, berhasil atau gagal. Penjaga "
                   "_sudah membuat panggilan kedua langsung pulang.",
            "langkah": [
                {"jenis": "mulai", "teks": "using (var p = new Pencatat(..))"},
                {"jenis": "proses", "teks": "p.Catat(\"mulai menghitung\")"},
                {"jenis": "proses", "teks": "p.Catat(\"selesai\")"},
                {"jenis": "proses", "teks": "kurawal tutup: p.Dispose()"},
                {"jenis": "keputusan", "teks": "_sudah masih false?", "tidak": 6},
                {"jenis": "proses", "teks": "Catat(\"ditutup\"), tutup writer"},
                {"jenis": "selesai", "teks": "berkas sudah tertutup"},
            ],
        },
    ],
    "async & await": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Berurutan: await di tiap panggilan, B baru mulai sesudah A selesai",
            "ket": "Dua kali 200 ms ditunggu bergantian, jadi totalnya sekitar 400 ms.",
            "pelaku": ["Main", "AmbilAsync A", "AmbilAsync B"],
            "pesan": [
                [0, 1, "await AmbilAsync(\"A\", 200)"],
                [1, 0, "A selesai (200ms)"],
                [0, 2, "await AmbilAsync(\"B\", 200)"],
                [2, 0, "B selesai (200ms)"],
                [0, 0, "Berurutan ~400 ms"],
            ],
        },
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Bersamaan: C dan D dimulai dulu, lalu ditunggu dengan WhenAll",
            "ket": "Kedua task sudah jalan sebelum ada yang ditunggu, jadi waktu "
                   "tunggunya tumpang tindih dan totalnya sekitar 200 ms.",
            "pelaku": ["Main", "AmbilAsync C", "AmbilAsync D"],
            "pesan": [
                [0, 1, "mulai t1, tanpa await"],
                [0, 2, "mulai t2, tanpa await"],
                [0, 0, "await Task.WhenAll(t1, t2)"],
                [1, 0, "C selesai (200ms)"],
                [2, 0, "D selesai (200ms)"],
                [0, 0, "Bersamaan ~200 ms"],
            ],
        },
    ],
    "Unit Test & Debugging": [
        {
            "setelah": 2,
            "jenis": "tabel",
            "judul": "Lima pemeriksaan di program uji, dua di antaranya tepat di batas",
            "ket": "85 dan 84 mengapit batas >= 85. Salah ketik >= jadi > cuma "
                   "ketahuan di baris yang disorot.",
            "tabel": [
                {"kolom": ["masukan", "harap", "aktual", "hasil"],
                 "baris": [["85", "A", "A", "OK"], ["84", "B", "B", "OK"],
                           ["60", "C", "C", "OK"], ["0", "D", "D", "OK"],
                           ["101", "melempar", "melempar", "OK"]],
                 "sorot_baris": [0, 1]},
            ],
        },
    ],
    "Konvensi Kode & Kualitas": [
        {
            "setelah": 0,
            "jenis": "tabel",
            "judul": "Konvensi penamaan .NET dengan contoh dari materi",
            "ket": "Konstanta juga PascalCase, beda dengan kebiasaan Java.",
            "tabel": [
                {"kolom": ["dipakai untuk", "gaya", "contoh"],
                 "baris": [["class", "PascalCase", "PesananPembelian"],
                           ["interface", "IPascalCase", "IBisaSimpan"],
                           ["property", "PascalCase", "TotalHarga"],
                           ["field privat", "_camelCase", "_jumlah"],
                           ["parameter", "camelCase", "jumlahItem"],
                           ["konstanta", "PascalCase", "MaxRetry"]]},
            ],
        },
    ],
    "Membangun Aplikasi Konsol Utuh": [
        {
            "setelah": 2,
            "jenis": "urutan",
            "judul": "Main cuma menyuruh, BukuKas yang memeriksa dan menghitung",
            "ket": "Validasi dan hitungan tinggal di BukuKas. Main nggak pernah "
                   "menyentuh _catatan langsung, karena Semua cuma IReadOnlyList.",
            "pelaku": ["Main", "BukuKas", "_catatan"],
            "pesan": [
                [0, 1, "Tambah(Kopi pagi, 25000)"],
                [1, 2, "Add(p) sesudah validasi"],
                [0, 1, "Tambah(\"\", Lain, 1000)"],
                [1, 0, "ArgumentException: ditolak"],
                [0, 1, "Total()"],
                [1, 2, "Sum(p => p.Jumlah)"],
                [1, 0, "298000"],
            ],
        },
    ],
}
