VB_MATERIALS = [
    {
        "title": "1. Pengenalan Visual Basic .NET",
        "sections": [
            {
                "body": [
                    "Ada tiga hal berbeda yang sama-sama disebut Visual Basic, dan ini",
                    "sumber kebingungan terbesar. Jadi kita luruskan dulu dari awal:",
                    "  - VB6 (1998): bahasa lama untuk aplikasi Windows. Udah nggak didukung",
                    "    lagi, dan kode VB6 nggak bisa jalan di VB.NET tanpa ditulis ulang.",
                    "  - VBA (Visual Basic for Applications): versi yang ada di dalam Excel",
                    "    dan Word. Turunan VB6, bukan VB.NET.",
                    "  - VB.NET (2002): bahasa modern di atas platform .NET. Yang ini yang",
                    "    dipelajari di sini.",
                    "",
                    "Ciri gampangnya: kalau sebuah tutorial memakai `Set obj = New ...` atau",
                    "Variant, berarti yang dipakai VB6 atau turunannya, bukan VB.NET.",
                    "`On Error Goto` juga ciri kode gaya lama. VB.NET masih menerimanya demi",
                    "kode lama, tapi di VB.NET error ditangani dengan Try...Catch.",
                    "",
                    "VB.NET itu saudara C#. Keduanya jalan di runtime yang sama, yaitu mesin",
                    "yang menjalankan program .NET. Keduanya juga memakai pustaka yang sama,",
                    "dan menghasilkan IL yang hampir sama. IL adalah kode perantara yang",
                    "dijalankan runtime itu. Yang beda cuma cara menulisnya:",
                    "",
                    "  C#              VB.NET",
                    "  int x = 5;      Dim x As Integer = 5",
                    "  { }             Sub ... End Sub",
                    "  //              '",
                    "  ==              =",
                    "  &&  ||          AndAlso  OrElse",
                    "  null            Nothing",
                    "",
                    "Karena keduanya setara, pustaka .NET apa pun bisa dipakai dari VB.NET.",
                    "Begitu juga sebaliknya: class buatan VB.NET bisa dipakai dari C#.",
                    "",
                    "Status VB.NET sekarang perlu kamu tahu sebelum menghabiskan waktu",
                    "untuknya. Microsoft menyebut VB.NET bahasa yang stabil. Artinya, VB.NET",
                    "tetap didukung penuh, tapi nggak lagi dapat fitur besar. Fitur bahasa",
                    "yang baru diarahkan ke C# dan F#.",
                    "",
                    "Jadi VB.NET masih masuk akal untuk:",
                    "  - Merawat aplikasi bisnis yang udah ada.",
                    "  - Tim yang semua anggotanya udah terbiasa dengan VB.",
                    "  - Belajar konsep .NET dengan sintaks yang gampang dibaca.",
                    "",
                    "Untuk proyek baru yang besar, VB.NET kurang cocok. Contoh kode dan",
                    "orang yang bisa C# jauh lebih gampang dicari.",
                    "",
                    "Memasang .NET SDK, yaitu paket alat untuk membuat program .NET:",
                    "  - Fedora  : sudo dnf install dotnet-sdk-8.0",
                    "  - Windows : Visual Studio, atau .NET SDK saja",
                    "  - Cek     : dotnet --version",
                    "",
                    "sudo artinya perintah itu dijalankan sebagai administrator, karena",
                    "programnya dipasang untuk seluruh sistem.",
                    "",
                    "Menjalankan:",
                    "  dotnet new console -lang VB -o latihan",
                    "  cd latihan && dotnet run",
                    "",
                    "Perintah pertama membuat proyek konsol VB baru di folder latihan.",
                    "dotnet run mengompilasi proyek itu lalu menjalankannya.",
                ]
            },
            {
                "heading": "Program pertama",
                "code": """Imports System

Module Program

    Sub Main()
        Console.WriteLine("Halo Dunia!")
        Console.WriteLine("Aku sedang belajar Visual Basic .NET.")

        Dim nama As String = "Andi"
        Dim umur As Integer = 20

        Console.WriteLine($"Halo, {nama}! Umurmu {umur} tahun.")
        Console.WriteLine("Sambung pakai & : " & nama & ", " & umur.ToString())
    End Sub

End Module"""
            },
            {
                "body": [
                    "Kita bahas bagian demi bagian:",
                    "",
                    "  Imports System",
                    "    Memuat namespace System supaya Console bisa ditulis tanpa awalan.",
                    "    Namespace adalah kelompok nama, mirip folder. Padanannya using di",
                    "    C#.",
                    "",
                    "  Module Program",
                    "    Module adalah wadah untuk kode yang nggak butuh objek. Semua isinya",
                    "    otomatis Shared, artinya statis: milik wadahnya, bukan milik",
                    "    objek. Padanannya di C# adalah class statis.",
                    "",
                    "  Sub Main()",
                    "    Titik masuk program, tempat program mulai jalan. Sub adalah",
                    "    prosedur yang nggak mengembalikan nilai. Prosedur yang",
                    "    mengembalikan nilai disebut Function.",
                    "",
                    "  End Sub / End Module",
                    "    VB menutup blok dengan kata, bukan dengan kurung kurawal.",
                    "",
                    "Beberapa aturan dasar VB:",
                    "  1. Nggak ada titik koma di akhir baris.",
                    "  2. Huruf besar dan kecil nggak dibedakan. Console dan console",
                    "     dianggap sama, dan editor biasanya merapikannya otomatis ke bentuk",
                    "     baku.",
                    "  3. Satu pernyataan, satu baris. Untuk memecah baris yang panjang,",
                    "     akhiri barisnya dengan spasi lalu garis bawah (_). Sejak VB 2010,",
                    "     kebanyakan baris bisa dipecah tanpa garis bawah.",
                    "  4. Komentar diawali kutip tunggal (').",
                    "  5. Nama ditulis PascalCase, yaitu tiap kata diawali huruf besar.",
                    "     Kecualinya variabel lokal dan parameter, yang memakai camelCase:",
                    "     kata pertamanya huruf kecil.",
                    "",
                    "Untuk menyambung teks, pakai &, jangan +. Tanda plus memang bisa",
                    "dipakai untuk string, tapi artinya ambigu: kalau salah satu sisinya",
                    "angka, VB mencoba menjumlahkannya. Jadi biasakan & untuk teks.",
                    "",
                    "String interpolation, yaitu `$\"...{x}...\"`, tersedia sejak VB 2015.",
                    "Bentuk ini lebih gampang dibaca daripada rantai &.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Di kantor, VB.NET biasanya kamu temui di aplikasi bisnis yang udah lama",
                    "dipakai: program kasir, penggajian, atau stok barang yang jalan di",
                    "Windows. Contoh kode di internet sering mencampur VB6, VBA, dan VB.NET,",
                    "jadi kemampuan membedakan ketiganya langsung terpakai waktu kamu",
                    "mencari bantuan.",
                    "",
                    "Kasus kecil: kamu mencari contoh \"hitung kembalian VB\" dan menemukan",
                    "kode yang memakai `Dim total As Variant` dan `Set kasir = New Kasir`.",
                    "Ditempel ke proyek dotnet, kode itu langsung error. Belanjanya 47500,",
                    "uangnya 50000, dan kamu cuma butuh kembaliannya.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Kenali dulu asal kodenya. Variant dan `Set ... = New` adalah ciri",
                    "     VB6 atau VBA, jadi kode itu nggak jalan di VB.NET walaupun sebagian",
                    "     kelihatan mirip. Compiler pun bilang begitu: \"'Variant' is no",
                    "     longer a supported type; use the 'Object' type instead\".",
                    "  2. Ambil logikanya, lalu tulis ulang dengan bentuk VB.NET:",
                    "      Dim total As Integer = 47500",
                    "      Dim bayar As Integer = 50000",
                    "      Console.WriteLine($\"Kembalian: {bayar - total}\")",
                    "  3. Taruh baris itu di dalam Sub Main, lalu jalankan dengan dotnet run.",
                    "     Hasilnya satu baris: Kembalian: 2500.",
                    "  4. Periksa cara menyambung teksnya. `\"Kembalian: \" + (bayar - total)`",
                    "     ditolak aplikasi ini dengan pesan \"Option Strict On disallows",
                    "     implicit conversions from 'String' to 'Double'\", karena + mencoba",
                    "     menjumlahkan. Pakai interpolasi atau &. Option Strict dibahas di",
                    "     materi berikutnya.",
                ]
            },
        ],
    },
    {
        "title": "2. Option Strict & Tipe Data",
        "sections": [
            {
                "body": [
                    "Di kepala berkas ada tiga saklar yang menentukan seberapa ketat VB",
                    "memeriksa kodemu. Yang pertama jauh lebih penting daripada dua",
                    "lainnya.",
                    "",
                    "  Option Strict On      tolak konversi tipe yang nggak ditulis",
                    "  Option Explicit On    variabel wajib dideklarasikan",
                    "  Option Infer On       tipe boleh disimpulkan dari nilainya",
                    "",
                    "Aturan: Option Strict On wajib dinyalakan. Alasannya bisa kamu lihat",
                    "langsung:",
                    "",
                    "  Dim n As Integer = \"7\"",
                    "",
                    "  Strict Off  -> diterima, n bernilai 7",
                    "  Strict On   -> ERROR kompilasi",
                    "",
                    "Dengan Strict Off, \"abc\" juga diterima, lalu baru gagal waktu program",
                    "jalan. Kalau begitu, manfaat bahasa bertipe hilang.",
                    "",
                    "Cara menyalakannya:",
                    "  - Di berkas: tulis `Option Strict On` di baris pertama.",
                    "  - Di proyek: tulis `<OptionStrict>On</OptionStrict>` di berkas",
                    "    .vbproj.",
                    "",
                    "Kalau keduanya ada, yang di berkas menang. Aplikasi ini menjalankan",
                    "semua contoh VB dengan Option Strict, Option Explicit, dan Option Infer",
                    "menyala.",
                    "",
                    "Tipe bilangan bulat:",
                    "  SByte    -128 .. 127                1 byte",
                    "  Byte     0 .. 255                   1 byte",
                    "  Short    -32.768 .. 32.767          2 byte",
                    "  Integer  -2,1 miliar .. 2,1 miliar  4 byte  <- bawaan",
                    "  Long     sekitar ±9,2 juta triliun  8 byte",
                    "",
                    "Hati-hati: Integer di VB.NET berukuran 32 bit. Di VB6, Integer cuma 16",
                    "bit, dan yang 32 bit justru Long. Ini sering bikin bingung orang yang",
                    "pindah dari VB6.",
                    "",
                    "Tipe pecahan:",
                    "  Single   ~7 digit presisi     ditulis 3.14F",
                    "  Double   ~15 digit presisi    ditulis 3.14   <- bawaan",
                    "  Decimal  ~28 digit presisi    ditulis 3.14D",
                    "",
                    "Pilihannya gampang: uang pakai Decimal, sisanya Double. Double",
                    "menyimpan pecahan dalam basis dua, jadi 0.1 nggak pernah tersimpan",
                    "persis.",
                    "",
                    "Tipe lain:",
                    "  Boolean  True / False",
                    "  Char     satu karakter, ditulis \"A\"c",
                    "  String   teks",
                    "  Date     tanggal dan waktu, ditulis #2026-09-22#",
                    "  Object   apa pun; hindari kecuali terpaksa",
                    "",
                    "Konversi tipe di VB punya tiga keluarga:",
                    "  CInt(x)  CDbl(x)  CStr(x)  CDec(x)  CBool(x)",
                    "  CType(x, Integer)",
                    "  Integer.Parse(s)         melempar kalau gagal",
                    "  Integer.TryParse(s, n)   mengembalikan Boolean",
                    "",
                    "Melempar artinya menghentikan program dengan exception, yaitu error",
                    "yang bikin program berhenti kalau nggak ditangkap. Untuk masukan dari",
                    "pengguna, TryParse hampir selalu pilihan yang benar.",
                ]
            },
            {
                "heading": "Tipe, batas, dan konversi",
                "code": """Option Strict On

Imports System
Imports System.Globalization

Module Program

    Sub Main()
        Dim umur As Integer = 20
        Dim tinggi As Double = 172.5
        Dim harga As Decimal = 25000D
        Dim aktif As Boolean = True
        Dim huruf As Char = "V"c

        Console.WriteLine($"Integer : {Integer.MinValue} .. {Integer.MaxValue}")
        Console.WriteLine($"Byte    : {Byte.MinValue} .. {Byte.MaxValue}")
        Console.WriteLine($"nilai   : {umur} {tinggi} {harga} {aktif} {huruf}")

        ' Konversi WAJIB ditulis karena Option Strict On
        Dim sebagaiDouble As Double = CDbl(umur)
        Dim sebagaiTeks As String = CStr(umur)
        Console.WriteLine($"konversi: {sebagaiDouble} '{sebagaiTeks}'")

        ' Pembagian: VB punya DUA operator
        Console.WriteLine($"7 / 2   = {7 / 2}")
        Console.WriteLine($"7 \\ 2   = {7 \\ 2}")
        Console.WriteLine($"7 Mod 2 = {7 Mod 2}")
        Console.WriteLine($"2 ^ 10  = {2 ^ 10}")

        ' Decimal tidak kehilangan presisi, Double bisa
        Console.WriteLine($"0.1 + 0.2 = 0.3 (Double) : {0.1 + 0.2 = 0.3}")
        Console.WriteLine($"0.1 + 0.2 = 0.3 (Decimal): {0.1D + 0.2D = 0.3D}")

        ' TryParse: tidak melempar
        For Each teks As String In New String() {"42", "3.5", "abc", ""}
            Dim n As Integer
            Dim berhasil As Boolean = Integer.TryParse(teks, n)
            Console.WriteLine($"TryParse(""{teks}"") = {berhasil}, hasil {n}")
        Next
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Integer : -2147483648 .. 2147483647",
                    "  Byte    : 0 .. 255",
                    "  nilai   : 20 172.5 25000 True V",
                    "  konversi: 20 '20'",
                    "  7 / 2   = 3.5",
                    "  7 \\ 2   = 3",
                    "  7 Mod 2 = 1",
                    "  2 ^ 10  = 1024",
                    "  0.1 + 0.2 = 0.3 (Double) : False",
                    "  0.1 + 0.2 = 0.3 (Decimal): True",
                    "  TryParse(\"42\") = True, hasil 42",
                    "  TryParse(\"3.5\") = False, hasil 0",
                    "  TryParse(\"abc\") = False, hasil 0",
                    "  TryParse(\"\") = False, hasil 0",
                    "",
                    "VB punya dua operator pembagian, dan C# nggak punya yang seperti ini:",
                    "",
                    "  /   pembagian pecahan; untuk bilangan bulat hasilnya Double",
                    "  \\   pembagian bulat, sisanya dibuang",
                    "",
                    "Jadi `7 / 2` menghasilkan 3.5, sedangkan `7 \\ 2` menghasilkan 3. Nggak",
                    "ada kejutan \"kok hasilnya bulat?\" seperti di C, Java, atau C#, karena",
                    "kamu sendiri yang memilih.",
                    "",
                    "^ adalah operator pangkat. Operator ini juga nggak ada di C#.",
                    "",
                    "Lihat `0.1 + 0.2 = 0.3` yang memakai satu tanda sama dengan. Di VB,",
                    "tanda = punya dua peran: penugasan di awal pernyataan, dan perbandingan",
                    "di dalam ekspresi. VB nggak punya == sama sekali.",
                    "",
                    "Ini kebalikan dari jebakan di C. Di sana, `if (x = 5)` adalah penugasan",
                    "yang nggak disengaja. Di VB hal itu mustahil, karena penugasan nggak",
                    "bisa muncul di dalam ekspresi.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi gudang dan distributor sering menghitung kemasan: berapa dus",
                    "penuh yang bisa dikirim dan berapa botol sisa yang dijual eceran.",
                    "Hitungan seperti ini butuh bilangan bulat, dan VB menyediakan dua alat",
                    "khusus untuknya, yaitu \\ untuk pembagian bulat dan Mod untuk sisanya.",
                    "",
                    "Kasus kecil: gudang punya 250 botol air mineral, dan satu dus berisi",
                    "24 botol. Surat jalan harus menulis 10 dus dan sisa 10 botol.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukan dan keluarannya: dua bilangan bulat masuk, dua",
                    "     bilangan bulat keluar. Pakai Integer untuk semuanya.",
                    "  2. Hitung dus dengan \\ dan sisanya dengan Mod:",
                    "      Dim botol As Integer = 250",
                    "      Dim isi As Integer = 24      ' botol per dus",
                    "      Console.WriteLine($\"{botol \\ isi} dus, sisa {botol Mod isi} botol\")",
                    "  3. Hindari / di sini. `Dim dus As Integer = botol / isi` ditolak",
                    "     Option Strict, karena / menghasilkan Double. Kalau dipaksa dengan",
                    "     CInt, hasilnya dibulatkan: 260 botol jadi 11 dus, padahal yang",
                    "     penuh cuma 10.",
                    "  4. Periksa kasus pinggir: stok yang kurang dari satu dus, misalnya 20",
                    "     botol. Hasilnya 0 dus dan sisa 20, dan surat jalan harus tetap",
                    "     masuk akal untuk angka itu.",
                ]
            },
        ],
    },
    {
        "title": "3. Operator & Perbandingan",
        "sections": [
            {
                "body": [
                    "Operator aritmetika:",
                    "  +    tambah",
                    "  -    kurang",
                    "  *    kali",
                    "  /    bagi pecahan (untuk bilangan bulat hasilnya Double)",
                    "  \\    bagi bulat, sisanya dibuang",
                    "  Mod  sisa bagi",
                    "  ^    pangkat",
                    "",
                    "Penugasan gabungan: += -= *= /= \\= ^= &=",
                    "",
                    "VB nggak punya operator ++ dan --, jadi tulis i += 1.",
                    "",
                    "Menyambung teks:",
                    "  &    selalu menyambung sebagai teks",
                    "  +    ambigu; hindari untuk teks",
                    "",
                    "  \"1\" & 2     -> \"12\"",
                    "  \"1\" + 2     -> dengan Option Strict On: ERROR",
                    "",
                    "Perbandingan:",
                    "  =    sama dengan   (bukan ==)",
                    "  <>   tidak sama    (bukan !=)",
                    "  <  >  <=  >=",
                    "  Is / IsNot         perbandingan referensi",
                    "  Like               pencocokan pola sederhana",
                    "",
                    "Perbandingan referensi artinya ngecek apakah dua variabel menunjuk",
                    "objek yang sama. Is dan IsNot dipakai untuk objek dan untuk Nothing,",
                    "yaitu nilai kosong di VB (padanan null):",
                    "  If obj Is Nothing Then",
                    "  If obj IsNot Nothing Then",
                    "",
                    "Jangan menulis `If obj = Nothing`. Untuk tipe referensi, baris itu",
                    "memanggil operator kesetaraan yang belum tentu ada. Untuk tipe nilai,",
                    "artinya lain sama sekali: nilainya dibandingkan dengan nilai bawaan",
                    "tipenya, misalnya 0.",
                    "",
                    "Operator logika",
                    "",
                    "Bagian ini yang paling penting di materi ini:",
                    "",
                    "  AndAlso   dan, dengan hubung-singkat",
                    "  OrElse    atau, dengan hubung-singkat",
                    "  And       dan, tanpa hubung-singkat",
                    "  Or        atau, tanpa hubung-singkat",
                    "  Not       negasi",
                    "  Xor       salah satu, tapi tidak keduanya",
                    "",
                    "Hubung-singkat (short-circuit) artinya sisi kanan nggak dievaluasi",
                    "kalau hasilnya udah pasti dari sisi kiri. Pakai AndAlso dan OrElse",
                    "hampir di semua kondisi. Tanpa hubung-singkat, sisi kanan tetap",
                    "dievaluasi walaupun hasilnya udah pasti:",
                    "",
                    "  If nama IsNot Nothing And nama.Length > 0 Then",
                    "      ' MELEDAK kalau nama Nothing: sisi kanan tetap jalan",
                    "",
                    "  If nama IsNot Nothing AndAlso nama.Length > 0 Then",
                    "      ' aman",
                    "",
                    "And dan Or tetap ada karena keduanya juga dipakai sebagai operator bit",
                    "pada bilangan. Untuk kondisi logika, hampir nggak pernah keduanya yang",
                    "kamu maksud.",
                    "",
                    "Operator lain:",
                    "  If(a, b)          pakai a kalau bukan Nothing",
                    "  If(syarat, a, b)  ternary",
                    "  ?.  ?()           null-conditional",
                    "  TypeOf x Is T     periksa tipe",
                    "  AddressOf f       referensi ke prosedur",
                    "",
                    "`If(syarat, a, b)` memilih a kalau syaratnya True, dan b kalau False.",
                    "Operator ?. berhenti dan menghasilkan Nothing kalau objek di sebelah",
                    "kirinya Nothing.",
                ]
            },
            {
                "heading": "Operator yang khas VB",
                "code": """Option Strict On

Imports System

Module Program

    Sub Main()
        ' --- Dua pembagian ---
        Console.WriteLine($"17 / 5   = {17 / 5}")
        Console.WriteLine($"17 \\ 5   = {17 \\ 5}")
        Console.WriteLine($"17 Mod 5 = {17 Mod 5}")
        Console.WriteLine($"2 ^ 8    = {2 ^ 8}")

        Console.WriteLine("---")

        ' --- Penyambung teks ---
        Dim nama As String = "Andi"
        Dim umur As Integer = 20
        Console.WriteLine("dengan & : " & nama & " (" & umur.ToString() & ")")
        Console.WriteLine($"interpol : {nama} ({umur})")

        Console.WriteLine("---")

        ' --- Is / IsNot untuk objek dan Nothing ---
        Dim kosong As String = Nothing
        Dim isi As String = "ada"
        Console.WriteLine($"kosong Is Nothing    : {kosong Is Nothing}")
        Console.WriteLine($"isi IsNot Nothing    : {isi IsNot Nothing}")

        Console.WriteLine("---")

        ' --- AndAlso menyelamatkan, And tidak ---
        Console.WriteLine($"aman   : {kosong IsNot Nothing AndAlso kosong.Length > 0}")
        Try
            ' Tanpa hubung-singkat, sisi kanan TETAP dievaluasi
            Console.WriteLine(kosong IsNot Nothing And kosong.Length > 0)
        Catch ex As NullReferenceException
            Console.WriteLine("bahaya : And tanpa hubung-singkat -> NullReferenceException")
        End Try

        Console.WriteLine("---")

        ' --- If() sebagai ternary dan sebagai pengganti Nothing ---
        Dim nilai As Integer = 78
        Console.WriteLine($"ternary  : {If(nilai >= 75, "Lulus", "Ulang")}")
        Console.WriteLine($"cadangan : {If(kosong, "(tidak diisi)")}")

        Console.WriteLine("---")

        ' --- Like: pencocokan pola sederhana ---
        For Each teks As String In New String() {"B01", "B123", "X01", "b01"}
            Console.WriteLine($"{teks,-6} Like ""B##"" -> {teks Like "B##"}")
        Next
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  17 / 5   = 3.4",
                    "  17 \\ 5   = 3",
                    "  17 Mod 5 = 2",
                    "  2 ^ 8    = 256",
                    "  ---",
                    "  dengan & : Andi (20)",
                    "  interpol : Andi (20)",
                    "  ---",
                    "  kosong Is Nothing    : True",
                    "  isi IsNot Nothing    : True",
                    "  ---",
                    "  aman   : False",
                    "  bahaya : And tanpa hubung-singkat -> NullReferenceException",
                    "  ---",
                    "  ternary  : Lulus",
                    "  cadangan : (tidak diisi)",
                    "  ---",
                    "  B01    Like \"B##\" -> True",
                    "  B123   Like \"B##\" -> False",
                    "  X01    Like \"B##\" -> False",
                    "  b01    Like \"B##\" -> False",
                    "",
                    "Bagian AndAlso dan And itu pelajaran terpentingnya. Keduanya kelihatan",
                    "setara, dan hasilnya sama di hampir semua kasus. Bedanya baru muncul",
                    "kalau sisi kiri bernilai False dan sisi kanan nggak aman dijalankan.",
                    "And tetap menjalankan sisi kanan lalu error, sedangkan AndAlso nggak.",
                    "",
                    "Like memakai pola sederhana, dan pola ini bukan regex (bahasa pola teks",
                    "yang lebih lengkap):",
                    "  ?        satu karakter apa pun",
                    "  *        berapa pun karakter",
                    "  #        satu angka",
                    "  [a-z]    satu karakter dari rentang",
                    "  [!a-z]   satu karakter di luar rentang",
                    "",
                    "Dengan Option Compare Binary, setelan bawaannya, Like membedakan huruf",
                    "besar dan kecil. Karena itu \"b01\" nggak cocok. Option Compare Text",
                    "mengubah perilaku itu.",
                    "",
                    "Untuk pola yang lebih rumit, pakai System.Text.RegularExpressions.Regex,",
                    "yang sama persis dengan yang dipakai C#.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir dan toko online memeriksa beberapa syarat sekaligus",
                    "sebelum memberi potongan: kodenya diisi, bentuknya benar, dan",
                    "belanjanya cukup. Syarat yang digabung dengan AndAlso berhenti di",
                    "syarat pertama yang gagal, jadi pemeriksaan berikutnya nggak sempat",
                    "menyentuh nilai yang kosong.",
                    "",
                    "Kasus kecil: voucher toko berbentuk \"VC\" diikuti empat angka, misalnya",
                    "VC2026, dan cuma berlaku untuk belanja minimal 50000. Untuk pembeli",
                    "yang nggak punya voucher, kodenya bernilai Nothing.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis syaratnya satu per satu: kode ada, bentuknya cocok, dan",
                    "     belanjanya cukup. Ketiganya harus True bersamaan.",
                    "  2. Gabungkan dengan AndAlso, dan periksa bentuknya dengan Like:",
                    "      Dim berlaku As Boolean = kode IsNot Nothing AndAlso",
                    "          kode Like \"VC####\" AndAlso belanja >= 50000",
                    "      Console.WriteLine(If(berlaku, \"Potongan 10000\", \"Voucher ditolak\"))",
                    "  3. Uji beberapa masukan. VC2026 dengan belanja 62000 dapat potongan.",
                    "     VC20A6 ditolak karena # cuma cocok dengan angka, dan vc2026 juga",
                    "     ditolak karena Like membedakan huruf besar dan kecil.",
                    "  4. Periksa pembeli tanpa voucher. Kalau kamu menambah kode.ToUpper()",
                    "     supaya huruf kecil diterima, AndAlso jadi wajib. Dengan And, sisi",
                    "     kanan tetap dijalankan, dan ToUpper() pada Nothing melempar",
                    "     NullReferenceException.",
                ]
            },
        ],
    },
    {
        "title": "4. Percabangan: If & Select Case",
        "sections": [
            {
                "body": [
                    "Percabangan memilih kode mana yang dijalankan berdasarkan sebuah",
                    "kondisi. Bentuk dasarnya begini:",
                    "",
                    "  If nilai >= 75 Then",
                    "      Console.WriteLine(\"Lulus\")",
                    "  ElseIf nilai >= 60 Then",
                    "      Console.WriteLine(\"Mengulang\")",
                    "  Else",
                    "      Console.WriteLine(\"Tidak Lulus\")",
                    "  End If",
                    "",
                    "ElseIf ditulis sebagai satu kata. `Else If` dua kata juga diterima VB",
                    "dan artinya sama, tapi bentuk bakunya ElseIf, jadi biasakan yang itu.",
                    "",
                    "Ada juga bentuk satu baris, tanpa End If:",
                    "  If nilai >= 75 Then Console.WriteLine(\"Lulus\")",
                    "",
                    "Pakai seperlunya aja. Bentuk ini nggak bisa diberi ElseIf, dan gampang",
                    "terlewat waktu membaca cepat.",
                    "",
                    "Select Case",
                    "",
                    "Select Case jauh lebih kuat daripada switch di C:",
                    "",
                    "  Select Case nilai",
                    "      Case 90 To 100",
                    "          grade = \"A\"",
                    "      Case 75, 80, 85",
                    "          grade = \"B\"",
                    "      Case Is >= 60",
                    "          grade = \"C\"",
                    "      Case Else",
                    "          grade = \"D\"",
                    "  End Select",
                    "",
                    "Tiga bentuk Case yang nggak ada di switch gaya C:",
                    "  Case 90 To 100      rentang",
                    "  Case 75, 80, 85     beberapa nilai",
                    "  Case Is >= 60       perbandingan",
                    "",
                    "Select Case nggak punya fall-through sama sekali, artinya eksekusi",
                    "nggak pernah \"jatuh\" ke Case berikutnya. Jadi kamu nggak perlu menulis",
                    "Break. Begitu satu Case cocok, cuma isi Case itu yang dijalankan, lalu",
                    "program lanjut ke sesudah End Select.",
                    "",
                    "`Select Case True` adalah cara yang lazim untuk menulis rantai kondisi:",
                    "",
                    "  Select Case True",
                    "      Case nilai >= 85 : grade = \"A\"",
                    "      Case nilai >= 75 : grade = \"B\"",
                    "      Case Else        : grade = \"C\"",
                    "  End Select",
                    "",
                    "Titik dua memisahkan dua pernyataan di satu baris.",
                    "",
                    "Kondisi di VB harus bertipe Boolean. Dengan Option Strict Off, angka",
                    "juga diterima, dan nol dianggap False. Dengan Strict On, kamu harus",
                    "menulis perbandingannya sendiri, misalnya `If n <> 0 Then`.",
                ]
            },
            {
                "heading": "Select Case dan semua bentuknya",
                "code": """Option Strict On

Imports System

Module Program

    Function Grade(nilai As Integer) As String
        Select Case nilai
            Case Is >= 85
                Return "A"
            Case 75 To 84
                Return "B"
            Case 60 To 74
                Return "C"
            Case 40 To 59
                Return "D"
            Case Else
                Return "E"
        End Select
    End Function

    Function Jenis(hari As Integer) As String
        Select Case hari
            Case 1, 2, 3, 4, 5
                Return "hari kerja"
            Case 6, 7
                Return "akhir pekan"
            Case Else
                Return "bukan hari yang sah"
        End Select
    End Function

    Function Suhu(derajat As Integer) As String
        ' Select Case True: rantai kondisi bebas
        Select Case True
            Case derajat < 15 : Return "dingin"
            Case derajat < 25 : Return "nyaman"
            Case derajat < 33 : Return "panas"
            Case Else         : Return "sangat panas"
        End Select
    End Function

    Sub Main()
        For Each n As Integer In New Integer() {92, 78, 65, 45, 12}
            Console.WriteLine($"{n,3} -> {Grade(n)}")
        Next

        Console.WriteLine("---")
        For Each h As Integer In New Integer() {1, 6, 9}
            Console.WriteLine($"hari {h} -> {Jenis(h)}")
        Next

        Console.WriteLine("---")
        For Each d As Integer In New Integer() {10, 22, 31, 40}
            Console.WriteLine($"{d,3} derajat -> {Suhu(d)}")
        Next

        Console.WriteLine("---")
        ' If satu baris, dan If() sebagai ekspresi
        Dim nilai As Integer = 78
        If nilai >= 75 Then Console.WriteLine("lulus (If satu baris)")
        Console.WriteLine($"status: {If(nilai >= 75, "Lulus", "Tidak Lulus")}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "   92 -> A",
                    "   78 -> B",
                    "   65 -> C",
                    "   45 -> D",
                    "   12 -> E",
                    "  ---",
                    "  hari 1 -> hari kerja",
                    "  hari 6 -> akhir pekan",
                    "  hari 9 -> bukan hari yang sah",
                    "  ---",
                    "   10 derajat -> dingin",
                    "   22 derajat -> nyaman",
                    "   31 derajat -> panas",
                    "   40 derajat -> sangat panas",
                    "  ---",
                    "  lulus (If satu baris)",
                    "  status: Lulus",
                    "",
                    "`Case 75 To 84` adalah bentuk yang paling sering berguna. C# baru punya",
                    "padanannya sejak ada pattern matching. Dengan bentuk ini, tabel",
                    "penilaian di kode terbaca seperti tabel sungguhan.",
                    "",
                    "`Function Grade(...) As String` memakai Return untuk mengembalikan",
                    "nilai. VB juga menerima bentuk lama, `Grade = \"A\"`, yang artinya",
                    "mengisi nama fungsinya sendiri. Bentuk itu warisan VB6 dan sebaiknya",
                    "nggak kamu pakai. Dia nggak menghentikan fungsinya, jadi kode di",
                    "bawahnya tetap jalan.",
                    "",
                    "`{n,3}` di dalam interpolasi meratakan ke kanan selebar 3 karakter.",
                    "Untuk rata kiri, pakai angka negatif: `{n,-3}`. Penulisan ini sama",
                    "persis dengan C#.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Tarif bertingkat ada di banyak aplikasi: ongkir menurut berat paket,",
                    "denda menurut lama terlambat, predikat rapor menurut nilai. Select Case",
                    "dengan Case Is menuliskan tabel tarif seperti itu baris demi baris, dan",
                    "yang dipakai selalu baris pertama yang cocok.",
                    "",
                    "Kasus kecil: kurir lokal menarik 9000 untuk paket sampai 1 kg, 15000",
                    "sampai 3 kg, 22000 sampai 5 kg, dan 30000 untuk yang lebih berat.",
                    "Paket 0,8 kg, 2,5 kg, 3 kg, dan 7,2 kg harus kena tarif yang benar.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis tabelnya dulu, lengkap dengan batasnya: tepat 1 kg masih",
                    "     tarif pertama, dan tepat 3 kg masih tarif kedua.",
                    "  2. Pindahkan tabel itu ke sebuah Function, misalnya",
                    "     `Function Ongkir(berat As Double) As Integer`, dengan Case Is yang",
                    "     urut dari batas terkecil:",
                    "      Select Case berat",
                    "          Case Is <= 1 : Return 9000",
                    "          Case Is <= 3 : Return 15000",
                    "          Case Is <= 5 : Return 22000",
                    "          Case Else : Return 30000",
                    "      End Select",
                    "  3. Cocokkan hasilnya dengan tabel: 0,8 kg kena 9000, 2,5 kg dan 3 kg",
                    "     kena 15000, dan 7,2 kg kena 30000.",
                    "  4. Periksa berat pecahan di antara dua rentang. Kalau ditulis",
                    "     `Case 2 To 3` lalu `Case 4 To 5`, paket 3,5 kg nggak masuk rentang",
                    "     mana pun dan jatuh ke Case Else, jadi kena 30000.",
                    "",
                    "Ingat: berat 0 atau minus harus ditolak sebelum masuk Select Case,",
                    "karena `Case Is <= 1` menerimanya dengan tarif 9000.",
                ]
            },
        ],
    },
    {
        "title": "5. Perulangan",
        "sections": [
            {
                "body": [
                    "Ada empat bentuk perulangan:",
                    "",
                    "  For i As Integer = 1 To 5",
                    "      ...",
                    "  Next",
                    "",
                    "  For i As Integer = 10 To 1 Step -2",
                    "      ...",
                    "  Next",
                    "",
                    "  For Each x As String In daftar",
                    "      ...",
                    "  Next",
                    "",
                    "  While syarat",
                    "      ...",
                    "  End While",
                    "",
                    "  Do While syarat ... Loop",
                    "  Do Until syarat ... Loop",
                    "  Do ... Loop While syarat      jalan minimal sekali",
                    "  Do ... Loop Until syarat      jalan minimal sekali",
                    "",
                    "Step menentukan langkahnya; `Step -2` berarti turun dua-dua. Do While",
                    "jalan selama syaratnya True, sedangkan Do Until jalan sampai syaratnya",
                    "True.",
                    "",
                    "Jebakan: `For i = 1 To 5` berjalan lima kali, yaitu 1, 2, 3, 4, 5.",
                    "Batas akhirnya ikut dihitung (inklusif). Di C,",
                    "`for (i = 0; i < 5; i++)` nggak menyertakan batas akhirnya (eksklusif).",
                    "",
                    "Ini sumber kesalahan \"lebih satu\" bagi yang pindah dari bahasa",
                    "berkurung kurawal. Untuk menelusuri array yang indeksnya mulai dari 0,",
                    "tulis `For i = 0 To a.Length - 1`.",
                    "",
                    "Mengendalikan perulangan:",
                    "  Exit For / Exit While / Exit Do",
                    "  Continue For / Continue While / Continue Do",
                    "  Exit Sub / Exit Function",
                    "",
                    "Exit keluar dari blok, sedangkan Continue langsung lompat ke putaran",
                    "berikutnya. Beda dengan C#, kata keluarnya menyebut jenis blok yang",
                    "ditinggalkan, jadi perulangan bersarang lebih jelas dibaca. Exit Do",
                    "keluar dari Do terdekat, walaupun ditulis di dalam For yang ada di",
                    "dalam Do itu. Tapi dua perulangan yang sejenis, misalnya For di dalam",
                    "For, tetap nggak bisa ditinggalkan sekaligus.",
                    "",
                    "Untuk keluar dari perulangan bersarang, pindahkan bagian dalamnya ke",
                    "sebuah Function, lalu pakai Return. Cara ini hampir selalu lebih",
                    "gampang dibaca daripada variabel penanda Boolean.",
                    "",
                    "For Each nggak mengizinkan koleksinya diubah selama penelusuran.",
                    "Menambah atau menghapus isi koleksi di tengah For Each bikin program",
                    "berhenti dengan InvalidOperationException.",
                ]
            },
            {
                "heading": "Semua bentuk perulangan",
                "code": """Option Strict On

Imports System

Module Program

    Sub Main()
        ' --- For dengan batas INKLUSIF ---
        Console.Write("1 To 5      : ")
        For i As Integer = 1 To 5
            Console.Write($"{i} ")
        Next
        Console.WriteLine()

        Console.Write("10 To 1 -2  : ")
        For i As Integer = 10 To 1 Step -2
            Console.Write($"{i} ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Tabel perkalian: For bersarang ---
        For b As Integer = 1 To 3
            For k As Integer = 1 To 5
                Console.Write($"{b * k,4}")
            Next
            Console.WriteLine()
        Next

        Console.WriteLine("---")

        ' --- For Each ---
        Dim nama() As String = {"Andi", "Budi", "Cici"}
        For Each n As String In nama
            Console.Write($"{n} ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Do Until dan Exit Do ---
        Dim sisa As Integer = 27
        Dim langkah As Integer = 0
        Do Until sisa = 1
            sisa = If(sisa Mod 2 = 0, sisa \\ 2, 3 * sisa + 1)
            langkah += 1
            If langkah > 1000 Then Exit Do
        Loop
        Console.WriteLine($"27 sampai 1 dalam {langkah} langkah")

        Console.WriteLine("---")

        ' --- Continue For: melewati sebagian ---
        Console.Write("ganjil 1-10 : ")
        For i As Integer = 1 To 10
            If i Mod 2 = 0 Then Continue For
            Console.Write($"{i} ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Keluar dari dua perulangan lewat Function ---
        Dim hasil = CariFaktor(143)
        Console.WriteLine($"143 = {hasil.Item1} x {hasil.Item2}")
    End Sub

    Function CariFaktor(n As Integer) As Tuple(Of Integer, Integer)
        For i As Integer = 2 To n
            For j As Integer = i To n
                If i * j = n Then Return Tuple.Create(i, j)
            Next
        Next
        Return Tuple.Create(1, n)
    End Function

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  1 To 5      : 1 2 3 4 5",
                    "  10 To 1 -2  : 10 8 6 4 2",
                    "  ---",
                    "     1   2   3   4   5",
                    "     2   4   6   8  10",
                    "     3   6   9  12  15",
                    "  ---",
                    "  Andi Budi Cici",
                    "  ---",
                    "  27 sampai 1 dalam 111 langkah",
                    "  ---",
                    "  ganjil 1-10 : 1 3 5 7 9",
                    "  ---",
                    "  143 = 11 x 13",
                    "",
                    "Fungsi CariFaktor nunjukin cara yang benar untuk keluar dari",
                    "perulangan bersarang di VB: pindahkan ke Function, lalu Return. VB",
                    "nggak punya break berlabel seperti di Go atau Kotlin. Variabel penanda",
                    "Boolean yang dicek di dua tempat jauh lebih gampang salah.",
                    "",
                    "`Tuple.Create(a, b)` mengembalikan dua nilai sekaligus. Sejak VB 15,",
                    "VB juga mendukung tuple bernama:",
                    "",
                    "  Function Bagi(a As Integer, b As Integer) _",
                    "      As (hasil As Integer, sisa As Integer)",
                    "      Return (a \\ b, a Mod b)",
                    "  End Function",
                    "",
                    "  Dim r = Bagi(17, 5)",
                    "  Console.WriteLine(r.hasil & \" sisa \" & r.sisa)",
                    "",
                    "Bentuk ini jauh lebih gampang dibaca daripada Item1 dan Item2, dan",
                    "layak dipakai di kode baru.",
                    "",
                    "Lihat juga garis bawah di ujung baris pertama. Begitulah cara memecah",
                    "satu pernyataan panjang jadi beberapa baris di VB. Sejak VB 2010",
                    "garis bawah jarang diperlukan, tapi di deklarasi seperti di atas, dia",
                    "masih wajib.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Koperasi sekolah atau toko yang menjual barang secara kredit mencetak",
                    "jadwal angsuran bulan demi bulan. Jadwal itu hasil satu perulangan For",
                    "yang jumlah putarannya sama dengan jumlah bulan cicilan.",
                    "",
                    "Kasus kecil: HP seharga 1850000 dicicil 6 bulan. Harga itu nggak habis",
                    "dibagi 6, jadi lima bulan pertama membayar 308333 dan bulan terakhir",
                    "menutup sisanya, yaitu 308335. Jadwalnya harus enam baris dan berakhir",
                    "di sisa 0.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami keluarannya: satu baris per bulan, berisi bayar dan sisa",
                    "     utang. Jumlah barisnya tetap, jadi pakai For.",
                    "  2. Hitung cicilan dasar dengan pembagian bulat, `harga \\ 6`, lalu",
                    "     biarkan bulan keenam membayar selisihnya:",
                    "      For bulan As Integer = 1 To 6",
                    "          Dim bayar As Integer = If(bulan = 6, harga - cicilan * 5, cicilan)",
                    "          sisa -= bayar",
                    "          Console.WriteLine($\"Bulan {bulan}: bayar {bayar}, sisa {sisa}\")",
                    "      Next",
                    "  3. Periksa baris terakhir: sisanya harus tepat 0. Kalau bulan keenam",
                    "     ikut membayar 308333, masih tersisa 2 rupiah yang nggak pernah",
                    "     ditagih.",
                    "  4. Periksa batas perulangannya. `For bulan = 1 To 6` jalan enam kali",
                    "     karena batas akhirnya ikut dihitung. Kalau ditulis `0 To 6`,",
                    "     jadwalnya jadi tujuh baris.",
                ]
            },
        ],
    },
    {
        "title": "6. Array & Koleksi",
        "sections": [
            {
                "body": [
                    "Array di VB punya satu kejutan besar yang perlu kamu tahu dari awal:",
                    "",
                    "  Dim a(4) As Integer",
                    "",
                    "Baris itu membuat array berisi lima elemen, dengan indeks 0 sampai 4.",
                    "Angka di dalam kurung adalah batas atas, yaitu indeks terakhir, bukan",
                    "jumlah elemen. Ini warisan dari VB6.",
                    "",
                    "Hampir semua bahasa lain nggak begitu, jadi ini sumber kesalahan",
                    "\"lebih satu\" yang sering banget terjadi.",
                    "",
                    "Bentuk lain yang lebih jelas:",
                    "  Dim a() As Integer = {10, 20, 30}",
                    "  Dim a As Integer() = New Integer() {10, 20, 30}",
                    "  Dim a = New Integer(4) {}        lima elemen, semua 0",
                    "",
                    "Mengakses dan mengukur:",
                    "  a(0)                elemen pertama; kurung biasa,",
                    "                      bukan kurung siku",
                    "  a.Length            jumlah elemen",
                    "  UBound(a)           indeks tertinggi",
                    "  a(a.Length - 1)     elemen terakhir",
                    "",
                    "Karena indeks memakai kurung biasa, a(0) kelihatan sama dengan",
                    "pemanggilan fungsi. VB memang sengaja begitu, dan kadang ini",
                    "membingungkan waktu membaca kode orang lain.",
                    "",
                    "Mengubah ukuran:",
                    "  ReDim a(9)                buat ulang, isinya hilang",
                    "  ReDim Preserve a(9)       isinya dipertahankan",
                    "",
                    "ReDim Preserve itu mahal: dia membuat array baru, lalu menyalin",
                    "seluruh isi yang lama. Kalau kamu sering menambah isi, pakai List,",
                    "jangan array.",
                    "",
                    "Koleksi generik",
                    "",
                    "Yang dipakai sehari-hari adalah koleksi generik, yaitu koleksi yang",
                    "tipe isinya ditentukan waktu koleksinya dibuat:",
                    "",
                    "  Imports System.Collections.Generic",
                    "",
                    "  Dim daftar As New List(Of String)",
                    "  daftar.Add(\"Andi\")",
                    "  daftar.Insert(0, \"Ani\")",
                    "  daftar.Remove(\"Andi\")",
                    "  daftar.RemoveAt(0)",
                    "  daftar.Count",
                    "  daftar.Contains(\"Andi\")",
                    "  daftar.Sort()",
                    "",
                    "  Dim umur As New Dictionary(Of String, Integer)",
                    "  umur(\"Andi\") = 20",
                    "  umur.TryGetValue(\"Andi\", n)",
                    "  umur.ContainsKey(\"Andi\")",
                    "",
                    "  Dim unik As New HashSet(Of Integer)",
                    "  Dim antre As New Queue(Of String)",
                    "  Dim tumpuk As New Stack(Of String)",
                    "",
                    "List adalah daftar yang bisa bertambah dan berkurang. Dictionary",
                    "menyimpan pasangan kunci dan nilai. HashSet menyimpan nilai yang unik.",
                    "Queue adalah antrean: yang masuk duluan keluar duluan. Stack adalah",
                    "tumpukan: yang masuk terakhir keluar duluan.",
                    "",
                    "`(Of T)` adalah cara VB menulis generic. Padanannya `<T>` di C#.",
                ]
            },
            {
                "heading": "Array, List, dan Dictionary",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Linq

Module Program

    Sub Main()
        ' --- Array: angka dalam kurung adalah BATAS ATAS ---
        Dim kosong(4) As Integer
        Console.WriteLine($"Dim kosong(4) -> {kosong.Length} elemen, indeks 0..{UBound(kosong)}")

        Dim nilai() As Integer = {78, 92, 65, 88, 71, 95, 59, 83}
        Console.WriteLine($"Data      : {String.Join(", ", nilai)}")

        Dim urut() As Integer = CType(nilai.Clone(), Integer())
        Array.Sort(urut)
        Console.WriteLine($"Terurut   : {String.Join(", ", urut)}")

        Dim total As Integer = 0
        For Each n As Integer In nilai
            total += n
        Next
        Console.WriteLine($"Jumlah    : {nilai.Length}")
        Console.WriteLine($"Total     : {total}")
        Console.WriteLine($"Rata-rata : {CDbl(total) / nilai.Length:F2}")
        Console.WriteLine($"Tertinggi : {nilai.Max()}")
        Console.WriteLine($"Terendah  : {nilai.Min()}")

        Console.WriteLine("---")

        ' --- List(Of T) ---
        Dim nama As New List(Of String) From {"Budi", "Andi", "Cici"}
        nama.Add("Dedi")
        nama.Sort()
        Console.WriteLine($"List      : {String.Join(", ", nama)}")
        Console.WriteLine($"Count     : {nama.Count}")
        Console.WriteLine($"Ada Andi? : {nama.Contains("Andi")}")

        Console.WriteLine("---")

        ' --- Dictionary(Of K, V): menghitung frekuensi ---
        Dim kalimat As String = "kucing makan ikan kucing tidur ikan kucing"
        Dim hitung As New Dictionary(Of String, Integer)

        For Each kata As String In kalimat.Split(" "c)
            Dim n As Integer
            hitung.TryGetValue(kata, n)
            hitung(kata) = n + 1
        Next

        For Each pasangan In hitung.OrderByDescending(Function(p) p.Value).
                                     ThenBy(Function(p) p.Key, StringComparer.Ordinal)
            Console.WriteLine($"{pasangan.Key,-7}: {pasangan.Value}")
        Next
        Console.WriteLine($"Kata unik  : {hitung.Count}")

        Console.WriteLine("---")

        ' --- HashSet, Queue, Stack ---
        Dim unik As New HashSet(Of Integer) From {1, 2, 2, 3, 3, 3}
        Console.WriteLine($"HashSet   : {String.Join(",", unik)}")
        Console.WriteLine($"Add 2 lagi: {unik.Add(2)}")

        Dim antre As New Queue(Of String)
        antre.Enqueue("Andi")
        antre.Enqueue("Budi")
        Console.WriteLine($"Dilayani  : {antre.Dequeue()}")

        Dim tumpuk As New Stack(Of String)
        tumpuk.Push("hal-1")
        tumpuk.Push("hal-2")
        Console.WriteLine($"Kembali   : {tumpuk.Pop()}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Dim kosong(4) -> 5 elemen, indeks 0..4",
                    "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
                    "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
                    "  Jumlah    : 8",
                    "  Total     : 631",
                    "  Rata-rata : 78.88",
                    "  Tertinggi : 95",
                    "  Terendah  : 59",
                    "  ---",
                    "  List      : Andi, Budi, Cici, Dedi",
                    "  Count     : 4",
                    "  Ada Andi? : True",
                    "  ---",
                    "  kucing : 3",
                    "  ikan   : 2",
                    "  makan  : 1",
                    "  tidur  : 1",
                    "  Kata unik  : 4",
                    "  ---",
                    "  HashSet   : 1,2,3",
                    "  Add 2 lagi: False",
                    "  Dilayani  : Andi",
                    "  Kembali   : hal-2",
                    "",
                    "Baris pertama jadi buktinya: `Dim kosong(4)` menghasilkan lima elemen.",
                    "Kalau kamu datang dari bahasa lain lalu menulis `Dim a(n)` dengan",
                    "anggapan itu n elemen, semua hitunganmu bakal meleset satu.",
                    "",
                    "Array.Sort mengubah array aslinya. Karena itu nilai.Clone() dipanggil",
                    "dulu sebelum mengurutkan. Di C# juga begitu, karena pustakanya memang",
                    "sama.",
                    "",
                    "Titik di ujung baris, seperti di `.OrderByDescending(...).`, adalah",
                    "cara merangkai method di beberapa baris tanpa garis bawah. Bentuk ini",
                    "ada sejak VB 2010. Dengan bentuk ini, rantai LINQ jauh lebih gampang",
                    "dibaca. LINQ adalah cara mengolah koleksi yang dibahas di materi",
                    "LINQ & Lambda.",
                    "",
                    "`\" \"c` dengan akhiran c adalah literal Char, yaitu satu karakter, bukan",
                    "String. Split menerima keduanya, tapi versi Char lebih cepat dan",
                    "maksudnya lebih jelas.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Rekap nilai rapor, daftar hadir, dan daftar harga semuanya berbentuk",
                    "kumpulan data. Array cocok kalau jumlahnya tetap, List kalau datanya",
                    "bertambah, dan Dictionary kalau kamu perlu mencari lewat kunci seperti",
                    "nomor induk siswa atau kode barang.",
                    "",
                    "Kasus kecil: guru menyimpan lima nilai ulangan harian Andi, yaitu 80,",
                    "75, 90, 85, dan 70. Rata-ratanya harus 80. Kode temanmu memakai",
                    "`Dim nilai(5) As Integer`, mengisi indeks 0 sampai 4, dan rata-ratanya",
                    "keluar 66.67.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari sumber selisihnya. `Dim nilai(5)` membuat enam elemen, indeks",
                    "     0 sampai 5. Elemen keenam bernilai 0 dan ikut dibagi.",
                    "  2. Tulis array beserta isinya sekaligus, supaya panjangnya pasti sama",
                    "     dengan jumlah data:",
                    "      Dim nilai() As Integer = {80, 75, 90, 85, 70}",
                    "      Dim total As Integer = 0",
                    "      For Each n As Integer In nilai",
                    "          total += n",
                    "      Next",
                    "      Console.WriteLine($\"Rata-rata: {total / nilai.Length:F2}\")",
                    "  3. Bagi dengan nilai.Length, jangan dengan angka 5 yang diketik",
                    "     sendiri. Hasilnya 80.00, dan ulangan keenam nanti ikut terhitung",
                    "     tanpa mengubah rumusnya.",
                    "  4. Kalau nilainya bertambah tiap minggu, ganti array dengan",
                    "     List(Of Integer) dan bagi dengan Count. ReDim Preserve di tiap",
                    "     tambahan menyalin seluruh isi array setiap kali.",
                ]
            },
        ],
    },
    {
        "title": "7. Sub, Function & Parameter",
        "sections": [
            {
                "body": [
                    "VB membedakan dua jenis prosedur, dan bedanya kelihatan langsung dari",
                    "kata kuncinya:",
                    "",
                    "  Sub       tidak mengembalikan nilai",
                    "  Function  mengembalikan nilai",
                    "",
                    "  Sub Sapa(nama As String)",
                    "      Console.WriteLine(\"Halo, \" & nama)",
                    "  End Sub",
                    "",
                    "  Function Tambah(a As Integer, b As Integer) As Integer",
                    "      Return a + b",
                    "  End Function",
                    "",
                    "Cara mengoper parameter",
                    "",
                    "  ByVal   salinan nilainya. Bawaan sejak VB.NET.",
                    "  ByRef   referensi ke variabel aslinya.",
                    "",
                    "Dengan ByVal, prosedur menerima salinan, jadi mengubah parameternya",
                    "nggak mengubah variabel milik pemanggil. Dengan ByRef, yang diubah",
                    "variabel aslinya.",
                    "",
                    "Di VB6, bawaannya justru ByRef, dan itu sumber bug yang sering muncul",
                    "di kode lama. Di VB.NET bawaannya ByVal, dan itu yang benar.",
                    "",
                    "Hati-hati: ByVal pada tipe referensi (String, array, class) menyalin",
                    "referensinya, bukan objeknya. Jadi kalau kamu mengubah isi array yang",
                    "dioper ByVal, perubahannya tetap kelihatan di pemanggil. Yang nggak",
                    "kelihatan cuma kalau variabel parameternya diisi ulang dengan array",
                    "lain.",
                    "",
                    "Parameter opsional:",
                    "  Sub Sapa(nama As String, Optional salam As String = \"Halo\")",
                    "",
                    "Parameter opsional wajib punya nilai bawaan, dan harus ditaruh di",
                    "akhir.",
                    "",
                    "Parameter yang jumlahnya bebas:",
                    "  Function Total(ParamArray angka() As Integer) As Integer",
                    "",
                    "Argumen bernama memakai tanda titik dua dan sama dengan (:=):",
                    "  Sapa(salam:=\"Hai\", nama:=\"Andi\")",
                    "",
                    "Tandanya :=, bukan =, karena tanda = udah dipakai untuk perbandingan di",
                    "dalam ekspresi.",
                    "",
                    "Overload adalah beberapa prosedur dengan nama yang sama tapi parameter",
                    "yang berbeda. Overload boleh ditandai kata Overloads (opsional):",
                    "  Function Luas(sisi As Double) As Double",
                    "  Function Luas(p As Double, l As Double) As Double",
                    "",
                    "Yang membedakan overload adalah jumlah dan tipe parameternya. Tipe",
                    "kembalian nggak ikut membedakan.",
                    "",
                    "Prosedur di dalam Module otomatis Shared, dan bisa dipanggil tanpa",
                    "menyebut nama modulnya. Itulah gunanya Module.",
                ]
            },
            {
                "heading": "Semua bentuk parameter",
                "code": """Option Strict On

Imports System

Module Program

    ' ByVal (bawaan): salinan
    Sub NaikkanSalinan(ByVal n As Integer)
        n += 100
    End Sub

    ' ByRef: menyentuh variabel aslinya
    Sub NaikkanAsli(ByRef n As Integer)
        n += 100
    End Sub

    Sub Tukar(ByRef a As Integer, ByRef b As Integer)
        Dim sementara As Integer = a
        a = b
        b = sementara
    End Sub

    ' Optional dan ParamArray
    Function Garis(isi As String,
                   Optional lebar As Integer = 30,
                   Optional pengisi As Char = "-"c) As String
        Dim sisa As Integer = Math.Max(lebar - isi.Length, 0)
        Dim kiri As Integer = sisa \\ 2
        Return New String(pengisi, kiri) & isi & New String(pengisi, sisa - kiri)
    End Function

    Function Total(ParamArray angka() As Integer) As Integer
        Dim jumlah As Integer = 0
        For Each n As Integer In angka
            jumlah += n
        Next
        Return jumlah
    End Function

    ' Overload: satu nama, beberapa bentuk
    Function Luas(sisi As Double) As Double
        Return sisi * sisi
    End Function

    Function Luas(panjang As Double, lebar As Double) As Double
        Return panjang * lebar
    End Function

    ' Tuple bernama: mengembalikan dua nilai
    Function Bagi(a As Integer, b As Integer) As (hasil As Integer, sisa As Integer)
        Return (a \\ b, a Mod b)
    End Function

    Sub Main()
        Dim x As Integer = 5
        NaikkanSalinan(x)
        Console.WriteLine($"sesudah ByVal : {x}")
        NaikkanAsli(x)
        Console.WriteLine($"sesudah ByRef : {x}")

        Dim a As Integer = 3, b As Integer = 8
        Tukar(a, b)
        Console.WriteLine($"sesudah Tukar : a={a} b={b}")

        Console.WriteLine("---")
        Console.WriteLine(Garis(" REKAP "))
        Console.WriteLine(Garis(" KECIL ", 20))
        Console.WriteLine(Garis(" TEBAL ", pengisi:="="c))
        Console.WriteLine(Garis(lebar:=24, isi:=" BERNAMA ", pengisi:="*"c))

        Console.WriteLine("---")
        Console.WriteLine($"Total()       = {Total()}")
        Console.WriteLine($"Total(1,2,3)  = {Total(1, 2, 3)}")

        Console.WriteLine("---")
        Console.WriteLine($"Luas(5)       = {Luas(5)}")
        Console.WriteLine($"Luas(4, 6)    = {Luas(4, 6)}")

        Console.WriteLine("---")
        Dim r = Bagi(17, 5)
        Console.WriteLine($"17 / 5        = {r.hasil} sisa {r.sisa}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  sesudah ByVal : 5",
                    "  sesudah ByRef : 105",
                    "  sesudah Tukar : a=8 b=3",
                    "  ---",
                    "  ----------- REKAP ------------",
                    "  ------ KECIL -------",
                    "  =========== TEBAL ============",
                    "  ******* BERNAMA ********",
                    "  ---",
                    "  Total()       = 0",
                    "  Total(1,2,3)  = 6",
                    "  ---",
                    "  Luas(5)       = 25",
                    "  Luas(4, 6)    = 24",
                    "  ---",
                    "  17 / 5        = 3 sisa 2",
                    "",
                    "Dua baris pertama menunjukkan beda ByVal dan ByRef sekaligus. Yang",
                    "pertama nggak mengubah apa pun di pemanggil, yang kedua mengubah.",
                    "",
                    "`pengisi:=\"=\"c` memakai argumen bernama untuk melompati parameter lebar",
                    "yang ada di tengah. Tanpa argumen bernama, kamu harus menulis ulang",
                    "nilai bawaan lebar cuma supaya bisa sampai ke parameter ketiga.",
                    "",
                    "`New String(pengisi, kiri)` membuat string berisi karakter yang sama",
                    "sebanyak kiri kali. Padanannya `\"-\".repeat(n)` di bahasa lain.",
                    "",
                    "Tuple bernama `(hasil As Integer, sisa As Integer)` bikin dua nilai",
                    "kembalian bisa dibaca lewat namanya sendiri, nggak lagi lewat Item1 dan",
                    "Item2. Fitur ini ada sejak VB 15, dan layak dipakai di kode baru.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Hitungan yang dipakai di banyak layar, seperti gaji, diskon, atau",
                    "ongkir, ditulis sekali sebagai Function. Parameter Optional menampung",
                    "nilai yang biasanya kosong, dan tuple bernama mengembalikan beberapa",
                    "angka sekaligus tanpa perlu ByRef.",
                    "",
                    "Kasus kecil: toko memotong iuran koperasi 2 persen dari gaji pokok.",
                    "Sari bergaji pokok 3000000 tanpa tunjangan, jadi potongannya 60000 dan",
                    "gaji bersihnya 2940000. Budi bergaji pokok 3200000 dengan tunjangan",
                    "transport 400000, jadi potongannya 64000 dan bersihnya 3536000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami masukan dan keluarannya: gaji pokok dan tunjangan yang boleh",
                    "     nggak diisi masuk, gaji bersih dan potongan keluar. Uang selalu",
                    "     Decimal.",
                    "  2. Jadikan tunjangan parameter Optional, dan kembalikan dua angka",
                    "     lewat tuple bernama:",
                    "      Function Gaji(pokok As Decimal, Optional tunjangan As Decimal = 0D) _",
                    "              As (bersih As Decimal, potongan As Decimal)",
                    "          Dim potongan As Decimal = pokok * 0.02D",
                    "          Return (pokok + tunjangan - potongan, potongan)",
                    "      End Function",
                    "  3. Panggil Gaji(3000000D) untuk Sari dan",
                    "     `Gaji(3200000D, tunjangan:=400000D)` untuk Budi, lalu baca hasilnya",
                    "     lewat .bersih dan .potongan.",
                    "  4. Periksa gaji yang menghasilkan sen. Untuk pokok 3333333, potongannya",
                    "     66666.66. Bulatkan dengan Math.Round(potongan, 0) sebelum",
                    "     dikurangkan, supaya slip gaji nggak memuat pecahan rupiah.",
                ]
            },
        ],
    },
    {
        "title": "8. Teks & Format",
        "sections": [
            {
                "body": [
                    "String di VB.NET adalah System.String, sama persis dengan di C#.",
                    "Termasuk sifatnya yang immutable, artinya isinya nggak bisa diubah",
                    "sesudah dibuat. Setiap method mengembalikan string baru:",
                    "",
                    "  nama.ToUpper()          tidak mengubah nama",
                    "  nama = nama.ToUpper()   ini yang benar",
                    "",
                    "Method yang paling sering dipakai:",
                    "  Length                  property, bukan method",
                    "  ToUpper / ToLower",
                    "  Trim / TrimStart / TrimEnd",
                    "  Substring(2, 4)",
                    "  IndexOf(\"abc\")          -1 kalau tidak ada",
                    "  Contains / StartsWith / EndsWith",
                    "  Replace(\"a\", \"b\")",
                    "  Split(\",\"c)",
                    "  String.Join(\", \", arr)",
                    "  PadLeft(10) / PadRight(10)",
                    "  String.IsNullOrEmpty(s)",
                    "  String.IsNullOrWhiteSpace(s)",
                    "",
                    "VB juga masih punya fungsi warisan dari VB6:",
                    "  Len(s)  UCase(s)  LCase(s)  Mid(s, 2, 3)",
                    "  Left(s, 3)  Right(s, 3)  InStr(s, \"x\")  Trim(s)",
                    "",
                    "Fungsi-fungsi itu nggak salah dipakai. Tapi untuk kode baru, ada dua",
                    "alasan memilih method .NET:",
                    "  - Method .NET sama dengan yang dipakai C#, jadi contoh dan",
                    "    dokumentasinya berlimpah.",
                    "  - Mid dan InStr mulai menghitung dari 1, sedangkan Substring dan",
                    "    IndexOf mulai dari 0. Mencampur keduanya di satu berkas gampang",
                    "    bikin kesalahan \"lebih satu\".",
                    "",
                    "Format angka memakai penentu format yang sama dengan C#:",
                    "  {n:C}      mata uang",
                    "  {n:N0}     angka, 0 desimal",
                    "  {n:F2}     dua desimal",
                    "  {n:P1}     persen",
                    "  {n:X}      heksadesimal",
                    "  {t:yyyy-MM-dd}  tanggal",
                    "",
                    "Perataan memakai koma di dalam interpolasi:",
                    "  {nama,-15}   rata kiri selebar 15",
                    "  {harga,10}   rata kanan selebar 10",
                    "",
                    "VB nggak punya raw string seperti C#, yaitu teks yang ditulis apa",
                    "adanya tanpa aturan khusus. Untuk teks yang berbaris-baris, biasanya",
                    "dipakai vbCrLf, vbLf, atau Environment.NewLine, yang disambung dengan",
                    "&. Sejak VB 14, string biasa juga boleh ditulis langsung di beberapa",
                    "baris, dan pindah barisnya ikut tersimpan.",
                    "",
                    "Konstanta bawaan yang sering dipakai: vbCrLf, vbTab, vbNullString, dan",
                    "ControlChars.Quote untuk tanda kutip.",
                ]
            },
            {
                "heading": "Mengolah teks dan menyusun tabel",
                "code": """Option Strict On

Imports System
Imports System.Globalization
Imports System.Text

Module Program

    Sub Main()
        Dim kalimat As String = "Visual Basic membuat kode bisnis mudah dibaca"

        Console.WriteLine($"asli       : {kalimat}")
        Console.WriteLine($"panjang    : {kalimat.Length}")
        Console.WriteLine($"kata       : {kalimat.Split(" "c).Length}")
        Console.WriteLine($"besar      : {kalimat.ToUpper()}")
        Console.WriteLine($"ganti      : {kalimat.Replace("bisnis", "apa pun")}")
        Console.WriteLine($"mulai?     : {kalimat.StartsWith("Visual")}")
        Console.WriteLine($"posisi     : {kalimat.IndexOf("kode")}")

        Dim terpanjang As String = ""
        For Each kata As String In kalimat.Split(" "c)
            If kata.Length > terpanjang.Length Then terpanjang = kata
        Next
        Console.WriteLine($"terpanjang : {terpanjang}")

        Console.WriteLine("---")

        ' Membangun teks bertahap dengan StringBuilder
        Dim sb As New StringBuilder()
        For i As Integer = 1 To 5
            sb.Append(i).Append(" ")
        Next
        Console.WriteLine($"builder    : {sb.ToString().Trim()}")

        Console.WriteLine("---")

        ' Tabel dengan perataan
        Dim barang() As String = {"Keyboard", "Mouse", "Monitor"}
        Dim jumlah() As Integer = {3, 12, 2}
        Dim harga() As Integer = {350000, 85000, 1750000}

        Console.WriteLine($"{"Barang",-12}{"Qty",5}{"Harga",15}")
        Console.WriteLine(New String("-"c, 32))

        Dim total As Integer = 0
        For i As Integer = 0 To barang.Length - 1
            Dim sub_ As Integer = jumlah(i) * harga(i)
            total += sub_
            Console.WriteLine($"{barang(i),-12}{jumlah(i),5}{sub_,15:N0}")
        Next

        Console.WriteLine(New String("-"c, 32))
        Console.WriteLine($"{"TOTAL",-12}{"",5}{total,15:N0}")

        Console.WriteLine("---")

        ' Teks multi-baris: VB memakai vbCrLf, bukan raw string
        Dim surat As String =
            "Halo Andi," & vbCrLf &
            vbCrLf &
            "Baris ini disambung dengan vbCrLf."
        Console.WriteLine(surat)
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  asli       : Visual Basic membuat kode bisnis mudah dibaca",
                    "  panjang    : 45",
                    "  kata       : 7",
                    "  besar      : VISUAL BASIC MEMBUAT KODE BISNIS MUDAH DIBACA",
                    "  ganti      : Visual Basic membuat kode apa pun mudah dibaca",
                    "  mulai?     : True",
                    "  posisi     : 21",
                    "  terpanjang : membuat",
                    "  ---",
                    "  builder    : 1 2 3 4 5",
                    "  ---",
                    "  Barang        Qty          Harga",
                    "  --------------------------------",
                    "  Keyboard        3      1,050,000",
                    "  Mouse          12      1,020,000",
                    "  Monitor         2      3,500,000",
                    "  --------------------------------",
                    "  TOTAL                  5,570,000",
                    "  ---",
                    "  Halo Andi,",
                    "",
                    "Pemisah ribuan yang muncul tergantung setelan wilayah komputernya. Di",
                    "aplikasi ini setelannya dipatok ke budaya invariant (netral), jadi",
                    "pemisahnya koma. Di komputer dengan setelan Indonesia, pemisahnya jadi",
                    "titik. Untuk keluaran yang harus sama di mana pun, oper",
                    "CultureInfo.InvariantCulture secara langsung.",
                    "",
                    "Variabel sub_ memakai garis bawah karena Sub adalah kata kunci di VB.",
                    "Cara lain: bungkus namanya dengan kurung siku, `[Sub]`, supaya VB",
                    "menganggapnya nama biasa. Cara ini berguna kalau kamu memakai pustaka",
                    "yang punya anggota bernama sama dengan kata kunci VB.",
                    "",
                    "`New String(\"-\"c, 32)` membuat garis pemisah. Padanannya",
                    "`\"-\".repeat(32)` di bahasa lain, dan bentuknya sama persis dengan C#.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Teks dari kotak isian sering nggak rapi: ada spasi di ujung, tanda",
                    "hubung, atau awalan yang beda-beda. Aplikasi klinik, sekolah, dan toko",
                    "merapikannya dulu sebelum menyimpan, supaya pencarian nggak meleset",
                    "dan pesan pengingat terkirim ke nomor yang benar.",
                    "",
                    "Kasus kecil: pelanggan menulis nomor HP dengan tiga gaya, yaitu",
                    "0812-3456-7890, 0812 3456 7890, dan +6281234567890. Layanan pengirim",
                    "pesan butuh satu bentuk saja, yaitu 6281234567890.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami keluarannya: cuma angka, diawali 62. Bedanya ada di tanda",
                    "     hubung, spasi, tanda plus, dan angka 0 di depan.",
                    "  2. Tangani satu perbedaan per langkah dengan method String:",
                    "      Function RapikanHp(teks As String) As String",
                    "          Dim n As String = teks.Replace(\"-\", \"\").Replace(\" \", \"\").Trim()",
                    "          If n.StartsWith(\"+\") Then n = n.Substring(1)",
                    "          If n.StartsWith(\"0\") Then n = \"62\" & n.Substring(1)",
                    "          Return n",
                    "      End Function",
                    "  3. Uji ketiga gaya tadi. Semuanya menghasilkan 6281234567890.",
                    "  4. Periksa isian kosong. Untuk teks bernilai Nothing, teks.Replace",
                    "     melempar NullReferenceException, sedangkan isian yang cuma berisi",
                    "     spasi menghasilkan teks kosong. Tolak keduanya lebih dulu dengan",
                    "     String.IsNullOrWhiteSpace(teks).",
                    "",
                    "Ingat: Substring(1) membuang karakter pertama karena indeksnya mulai",
                    "dari 0. Kalau dicampur dengan Mid, yang mulai dari 1, gampang meleset",
                    "satu.",
                ]
            },
        ],
    },
    {
        "title": "9. Class, Property & Constructor",
        "sections": [
            {
                "body": [
                    "Class adalah cetakan untuk membuat objek. Isinya data, yang disimpan",
                    "di field dan property, dan perilaku, yang ditulis sebagai method.",
                    "Property adalah anggota yang dipakai seperti variabel, tapi isinya",
                    "dijaga lewat getter (waktu dibaca) dan setter (waktu diisi). Contoh",
                    "class di VB:",
                    "",
                    "  Class Murid",
                    "      Private _nilai As Integer",
                    "",
                    "      Public Property Nama As String",
                    "",
                    "      Public Property Nilai As Integer",
                    "          Get",
                    "              Return _nilai",
                    "          End Get",
                    "          Set(value As Integer)",
                    "              If value < 0 OrElse value > 100 Then",
                    "                  Throw New ArgumentOutOfRangeException()",
                    "              End If",
                    "              _nilai = value",
                    "          End Set",
                    "      End Property",
                    "",
                    "      Public Sub New(nama As String, nilai As Integer)",
                    "          Me.Nama = nama",
                    "          Me.Nilai = nilai",
                    "      End Sub",
                    "  End Class",
                    "",
                    "Beberapa hal yang khas VB:",
                    "",
                    "  Public Property Nama As String",
                    "    Auto-property. Satu baris ini menghasilkan property lengkap dengan",
                    "    getter, setter, dan field tersembunyi bernama _Nama.",
                    "",
                    "  Public Sub New(...)",
                    "    Constructor, yaitu prosedur yang jalan waktu objek dibuat.",
                    "    Namanya selalu New, beda dengan C# dan Java yang memakai nama",
                    "    class-nya.",
                    "",
                    "  Me",
                    "    Menunjuk objek yang sedang dikerjakan. Padanan this di C#.",
                    "",
                    "  Set(value As Integer)",
                    "    Menurut kebiasaan, parameter setter dinamai value.",
                    "",
                    "Modifier akses:",
                    "  Public      siapa pun",
                    "  Friend      hanya di dalam assembly ini (bawaan untuk class);",
                    "              padanan internal di C#",
                    "  Protected   class ini dan turunannya",
                    "  Private     hanya class ini (bawaan untuk variabel Dim di class)",
                    "  Protected Friend / Private Protected",
                    "",
                    "Assembly adalah hasil kompilasi satu proyek, misalnya satu berkas .dll",
                    "atau .exe.",
                    "",
                    "Jebakan: Sub, Function, dan Property yang ditulis tanpa modifier",
                    "justru Public. Jadi tulis Private secara jelas untuk anggota yang",
                    "memang harus tersembunyi.",
                    "",
                    "Anggota statis memakai kata Shared, bukan static:",
                    "  Private Shared _urutan As Integer",
                    "  Public Shared Function Buat(...) As Murid",
                    "",
                    "Property hanya-baca:",
                    "  Public ReadOnly Property Grade As String",
                    "      Get",
                    "          Return If(_nilai >= 85, \"A\", \"B\")",
                    "      End Get",
                    "  End Property",
                    "",
                    "Sejak VB 14 ada bentuk singkatnya:",
                    "  Public ReadOnly Property Grade As String =",
                    "      If(_nilai >= 85, \"A\", \"B\")",
                    "",
                    "Hati-hati: bentuk singkat itu dihitung sekali, waktu objek dibuat. Dia",
                    "nggak dihitung ulang setiap kali dibaca. Untuk nilai yang bisa",
                    "berubah, pakai bentuk Get.",
                    "",
                    "`Overrides Function ToString()` menentukan bagaimana objek dicetak.",
                    "Tanpa itu, yang muncul cuma nama tipenya.",
                ]
            },
            {
                "heading": "Class lengkap",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic

Class Rekening

    Private Shared _urutan As Integer = 0
    Private _saldo As Long

    Public ReadOnly Property Nomor As String
    Public ReadOnly Property Pemilik As String

    Public ReadOnly Property Saldo As Long
        Get
            Return _saldo
        End Get
    End Property

    Public ReadOnly Property Kosong As Boolean
        Get
            Return _saldo = 0
        End Get
    End Property

    Public Sub New(pemilik As String, Optional saldoAwal As Long = 0)
        If String.IsNullOrWhiteSpace(pemilik) Then
            Throw New ArgumentException("pemilik wajib diisi", NameOf(pemilik))
        End If

        _urutan += 1
        Me.Nomor = $"AC{_urutan:D4}"
        Me.Pemilik = pemilik
        _saldo = saldoAwal
    End Sub

    Public Function Setor(jumlah As Long) As Rekening
        If jumlah <= 0 Then
            Throw New ArgumentOutOfRangeException(NameOf(jumlah))
        End If
        _saldo += jumlah
        Return Me
    End Function

    Public Function Tarik(jumlah As Long) As Boolean
        If jumlah <= 0 OrElse jumlah > _saldo Then Return False
        _saldo -= jumlah
        Return True
    End Function

    Public Shared Function BuatBanyak(ParamArray nama() As String) As List(Of Rekening)
        Dim hasil As New List(Of Rekening)
        For Each n As String In nama
            hasil.Add(New Rekening(n))
        Next
        Return hasil
    End Function

    Public Overrides Function ToString() As String
        Return $"{Nomor} {Pemilik,-8}{_saldo,12}"
    End Function

End Class

Module Program

    Sub Main()
        Dim a As New Rekening("Andi", 500000)
        Dim b As New Rekening("Budi")

        a.Setor(250000)
        Console.WriteLine($"tarik 900rb: {a.Tarik(900000)}")
        Console.WriteLine($"tarik 300rb: {a.Tarik(300000)}")
        b.Setor(100000)

        Console.WriteLine(a.ToString())
        Console.WriteLine(b.ToString())
        Console.WriteLine($"b kosong?  : {b.Kosong}")

        Console.WriteLine("---")
        For Each r As Rekening In Rekening.BuatBanyak("Cici", "Dedi")
            Console.WriteLine(r.ToString())
        Next

        Try
            Dim salah As New Rekening("   ")
        Catch ex As ArgumentException
            Console.WriteLine($"Ditolak: {ex.Message.Split(vbLf)(0)}")
        End Try
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  tarik 900rb: False",
                    "  tarik 300rb: True",
                    "  AC0001 Andi          450000",
                    "  AC0002 Budi          100000",
                    "  b kosong?  : False",
                    "  ---",
                    "  AC0003 Cici               0",
                    "  AC0004 Dedi               0",
                    "  Ditolak: pemilik wajib diisi",
                    "",
                    "Dari contoh itu, ada empat hal yang perlu kamu lihat:",
                    "  1. `Public ReadOnly Property Nomor As String` adalah auto-property",
                    "     hanya-baca. Dia boleh diisi di dalam constructor, dan terkunci",
                    "     sesudahnya.",
                    "  2. _saldo dibuat Private, dan property Saldo dipakai untuk",
                    "     membacanya. Kalau _saldo dibuat Public, semua aturan di Setor dan",
                    "     Tarik bisa dilewati dengan satu baris.",
                    "  3. `Private Shared _urutan` milik class, bukan milik objek. Cuma ada",
                    "     satu untuk seluruh program, dan itu yang bikin penomoran otomatis",
                    "     jalan.",
                    "  4. Setor mengembalikan Me, jadi pemanggilannya bisa dirangkai.",
                    "",
                    "NameOf(pemilik) menghasilkan string \"pemilik\", dan ikut berubah kalau",
                    "nama parameternya diganti. Nama yang ditulis sebagai teks biasa nggak",
                    "punya sifat itu.",
                    "",
                    "`ex.Message.Split(vbLf)(0)` mengambil baris pertama dari pesan error.",
                    "ArgumentException menambahkan nama parameter ke pesannya. Di .NET",
                    "Framework yang lama, tambahan itu ada di baris kedua, jadi baris ini",
                    "memotongnya. Di .NET modern, yang dipakai aplikasi ini, tambahannya",
                    "ditempel di baris yang sama: (Parameter 'pemilik'). Jadi di sini baris",
                    "yang tercetak diakhiri tambahan itu.",
                    "",
                    "Lihat juga Split(...)(0) yang memakai kurung biasa untuk mengindeks",
                    "hasilnya. Di VB, indeks dan pemanggilan fungsi memakai tanda yang",
                    "sama.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Data yang punya aturan, seperti anggota perpustakaan, rekening",
                    "koperasi, atau stok barang, biasanya dibuat jadi class. Nomor otomatis,",
                    "isian wajib, dan batas jumlah dijaga di constructor dan method, jadi",
                    "layar mana pun yang memakai class itu nggak bisa melanggarnya.",
                    "",
                    "Kasus kecil: perpustakaan sekolah memberi nomor anggota otomatis P0001,",
                    "P0002, dan seterusnya. Nama anggota wajib diisi, dan satu anggota",
                    "paling banyak meminjam tiga buku sekaligus.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pisahkan data dan aturannya. Nomor dan nama nggak berubah sesudah",
                    "     anggota dibuat, jadi keduanya ReadOnly Property. Jumlah buku yang",
                    "     dipinjam disimpan di field Private bernama _dipinjam.",
                    "  2. Di constructor, tolak nama kosong dengan ArgumentException, naikkan",
                    "     Private Shared _urutan, lalu isi Nomor dengan `$\"P{_urutan:D4}\"`.",
                    "  3. Tulis aturan pinjamnya di method:",
                    "      Public Function Pinjam() As Boolean",
                    "          If _dipinjam >= 3 Then Return False",
                    "          _dipinjam += 1",
                    "          Return True",
                    "      End Function",
                    "     Kembalikan() menurunkan _dipinjam, tapi nggak sampai minus.",
                    "  4. Uji pinggirnya: anggota ketiga mendapat P0003, pinjaman keempat",
                    "     ditolak dengan False, dan Kembalikan() untuk anggota yang belum",
                    "     meminjam apa pun tetap menyisakan 0.",
                ]
            },
        ],
    },
    {
        "title": "10. Pewarisan, Interface & MustInherit",
        "sections": [
            {
                "body": [
                    "Pewarisan artinya sebuah class mendapat semua isi class lain, lalu",
                    "boleh menambah atau mengubahnya. Di VB, pewarisan ditulis dengan kata",
                    "Inherits, di baris tersendiri sesudah nama class:",
                    "",
                    "  Class Kucing",
                    "      Inherits Hewan",
                    "  End Class",
                    "",
                    "Kata kunci yang mengatur penimpaan (override):",
                    "  Overridable   di induk: boleh ditimpa",
                    "  Overrides     di turunan: aku menimpanya",
                    "  MustOverride  di induk: turunan wajib mengisinya",
                    "  NotOverridable di turunan: berhenti di sini",
                    "  MustInherit   class yang tidak bisa di-New (abstract)",
                    "  NotInheritable class yang tidak bisa diturunkan (sealed)",
                    "  Shadows       menyembunyikan, bukan menimpa",
                    "",
                    "Sama seperti C#, method nggak bisa ditimpa secara bawaan. Kamu harus",
                    "menulis Overridable dulu di induknya.",
                    "",
                    "MyBase menunjuk induk:",
                    "  MyBase.New(nama)      panggil constructor induk",
                    "  MyBase.Ringkas()      panggil versi induk",
                    "",
                    "MyClass menunjuk versi di class ini sendiri, dan mengabaikan penimpaan",
                    "oleh turunan. Jarang dipakai, tapi berguna kalau sebuah method harus",
                    "memakai versinya sendiri.",
                    "",
                    "Constructor induk selalu dijalankan lebih dulu. Kalau induknya nggak",
                    "punya constructor tanpa parameter, kamu wajib memanggil",
                    "MyBase.New(...) di baris pertama constructor turunan.",
                    "",
                    "Interface",
                    "",
                    "Interface adalah daftar anggota yang wajib dimiliki class yang",
                    "memakainya. Cara VB mengimplementasikannya beda dari C#, dan ini",
                    "sering bikin kaget:",
                    "",
                    "  Interface IBangun",
                    "      Function Luas() As Double",
                    "      ReadOnly Property Nama As String",
                    "  End Interface",
                    "",
                    "  Class Persegi",
                    "      Implements IBangun",
                    "",
                    "      Public Function Luas() As Double Implements IBangun.Luas",
                    "          ...",
                    "      End Function",
                    "  End Class",
                    "",
                    "Setiap anggota wajib menyebut `Implements IBangun.Luas` secara jelas.",
                    "Untungnya, nama methodmu boleh beda dari nama di interface, dan satu",
                    "method bisa mengimplementasikan beberapa anggota sekaligus.",
                    "",
                    "Satu class boleh mengimplementasikan banyak interface, tapi cuma boleh",
                    "punya satu induk.",
                ]
            },
            {
                "heading": "Abstract, interface, dan polimorfisme",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic

Interface IBangun
    ReadOnly Property Nama As String
    Function Luas() As Double
    Function Keliling() As Double
End Interface

MustInherit Class BangunDasar
    Implements IBangun

    Public ReadOnly Property Nama As String Implements IBangun.Nama

    Protected Sub New(nama As String)
        Me.Nama = nama
    End Sub

    Public MustOverride Function Luas() As Double Implements IBangun.Luas
    Public MustOverride Function Keliling() As Double Implements IBangun.Keliling

    Public Overridable Function Ringkas() As String
        Return $"{Nama,-16}{Luas(),8:F2}{Keliling(),10:F2}"
    End Function
End Class

Class Persegi
    Inherits BangunDasar

    Private ReadOnly _sisi As Double

    Public Sub New(sisi As Double)
        MyBase.New("Persegi")
        _sisi = sisi
    End Sub

    Public Overrides Function Luas() As Double
        Return _sisi * _sisi
    End Function

    Public Overrides Function Keliling() As Double
        Return 4 * _sisi
    End Function
End Class

Class Lingkaran
    Inherits BangunDasar

    Private Const PI As Double = 3.14159
    Private ReadOnly _jari As Double

    Public Sub New(jari As Double)
        MyBase.New("Lingkaran")
        _jari = jari
    End Sub

    Public Overrides Function Luas() As Double
        Return PI * _jari * _jari
    End Function

    Public Overrides Function Keliling() As Double
        Return 2 * PI * _jari
    End Function

    Public Overrides Function Ringkas() As String
        Return MyBase.Ringkas() & $"  (r={_jari})"
    End Function
End Class

Module Program

    Sub Main()
        Dim semua As New List(Of IBangun) From {
            New Persegi(4),
            New Lingkaran(3),
            New Persegi(2.5)
        }

        Dim totalLuas As Double = 0
        For Each b As IBangun In semua
            Dim baris As String = If(TypeOf b Is BangunDasar,
                                     CType(b, BangunDasar).Ringkas(),
                                     b.Nama)
            Console.WriteLine(baris)
            totalLuas += b.Luas()
        Next

        Console.WriteLine($"{"TOTAL",-16}{totalLuas,8:F2}")

        Console.WriteLine("---")
        Console.WriteLine($"semua(0) IBangun?     : {TypeOf semua(0) Is IBangun}")
        Console.WriteLine($"semua(1) Lingkaran?   : {TypeOf semua(1) Is Lingkaran}")
        Console.WriteLine($"semua(1) BangunDasar? : {TypeOf semua(1) Is BangunDasar}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Persegi            16.00     16.00",
                    "  Lingkaran          28.27     18.85  (r=3)",
                    "  Persegi             6.25     10.00",
                    "  TOTAL              50.52",
                    "  ---",
                    "  semua(0) IBangun?     : True",
                    "  semua(1) Lingkaran?   : True",
                    "  semua(1) BangunDasar? : True",
                    "",
                    "Ini yang disebut polimorfisme: `b.Luas()` di dalam For Each memanggil",
                    "method yang beda di tiap putaran, padahal kodenya cuma satu baris dan",
                    "tipe variabelnya cuma IBangun.",
                    "",
                    "Akibatnya, menambah bangun baru nggak menyentuh satu baris pun di",
                    "Main. Desain berorientasi objek yang baik diukur dari situ: seberapa",
                    "sedikit kode lama yang perlu disunting waktu ada tambahan. Jumlah",
                    "class-nya nggak jadi ukuran.",
                    "",
                    "`Public MustOverride Function Luas() As Double Implements IBangun.Luas`",
                    "mengerjakan dua hal sekaligus. Dia menyatakan method itu abstrak",
                    "(wajib diisi turunan), dan mengaitkannya ke anggota interface. Di C#,",
                    "dua hal itu terjadi tanpa perlu ditulis.",
                    "",
                    "`TypeOf x Is T` memeriksa tipe waktu program jalan, dan `CType(x, T)`",
                    "mengonversinya. Ada juga `TryCast(x, T)`, yang mengembalikan Nothing",
                    "kalau tipenya nggak cocok, alih-alih melempar exception. Padanannya as",
                    "di C#.",
                    "",
                    "`Protected Sub New(...)` mencegah `New BangunDasar(...)` dari luar,",
                    "tapi class turunannya tetap boleh memanggil MyBase.New.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi penggajian di toko atau pabrik menangani beberapa jenis",
                    "pekerja. Karyawan tetap digaji bulanan, pekerja harian dibayar per hari",
                    "masuk, dan siswa magang dapat uang saku. Dengan MustInherit, layar",
                    "penggajian cukup memanggil Gaji() tanpa tahu jenis pekerjanya.",
                    "",
                    "Kasus kecil: bulan ini toko punya Rina (tetap, 3500000), Dodi (harian,",
                    "22 hari kali 120000), dan Sari (magang, uang saku 1000000). Total yang",
                    "harus disiapkan bendahara adalah 7140000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Cari bagian yang sama: semua pekerja punya nama dan gaji, tapi",
                    "     rumus gajinya beda. Jadikan `MustInherit Class Karyawan` dengan",
                    "     `Public MustOverride Function Gaji() As Decimal`.",
                    "  2. Tiap jenis jadi class turunan yang mengisi rumusnya sendiri. Untuk",
                    "     pekerja harian:",
                    "      Public Overrides Function Gaji() As Decimal",
                    "          Return HariKerja * 120000D",
                    "      End Function",
                    "  3. Simpan semuanya di List(Of Karyawan), lalu jumlahkan:",
                    "      For Each k As Karyawan In semua",
                    "          total += k.Gaji()",
                    "      Next",
                    "  4. Periksa jenis baru. Kalau bulan depan ada pekerja lepas, cukup",
                    "     tambah satu class turunan, dan perulangan di langkah 3 nggak",
                    "     berubah. Class baru yang lupa mengisi Gaji() langsung ditolak",
                    "     compiler.",
                ]
            },
        ],
    },
    {
        "title": "11. Structure, Enum & Module",
        "sections": [
            {
                "body": [
                    "Structure adalah tipe nilai. Menyalinnya berarti menyalin seluruh",
                    "isinya, bukan alamatnya. Class sebaliknya: yang disalin alamatnya,",
                    "jadi dua variabel bisa menunjuk objek yang sama.",
                    "",
                    "  Structure Titik",
                    "      Public X As Integer",
                    "      Public Y As Integer",
                    "  End Structure",
                    "",
                    "Pakai Structure kalau:",
                    "  - Ukurannya kecil, kira-kira di bawah 16 byte.",
                    "  - Isinya nggak berubah sesudah dibuat.",
                    "  - Dia berperilaku seperti angka, misalnya titik koordinat, rentang",
                    "    tanggal, atau jumlah uang.",
                    "",
                    "Kalau ragu, pakai Class. Structure yang besar justru lebih lambat,",
                    "karena seluruh isinya disalin setiap kali dioper.",
                    "",
                    "Structure nggak bisa:",
                    "  - mewarisi structure lain",
                    "  - punya constructor tanpa parameter buatan sendiri",
                    "  - memberi nilai awal pada field-nya (kecuali field Shared)",
                    "",
                    "Tapi Structure bisa mengimplementasikan interface.",
                    "",
                    "Enum adalah sekumpulan konstanta yang diberi nama:",
                    "",
                    "  Enum Status",
                    "      Draf",
                    "      Ditinjau",
                    "      Terbit",
                    "  End Enum",
                    "",
                    "  Enum Prioritas",
                    "      Rendah = 1",
                    "      Sedang = 5",
                    "      Tinggi = 10",
                    "  End Enum",
                    "",
                    "Kalau angkanya nggak ditulis, anggota enum otomatis bernomor 0, 1, 2,",
                    "dan seterusnya.",
                    "",
                    "Operasi yang berguna:",
                    "  CInt(s)                       jadi angka",
                    "  CType(3, Status)              dari angka",
                    "  s.ToString()                  namanya",
                    "  [Enum].GetValues(GetType(Status))",
                    "  [Enum].IsDefined(GetType(Status), n)",
                    "  [Enum].TryParse(Of Status)(teks, hasil)",
                    "",
                    "[Enum] ditulis dalam kurung siku karena Enum adalah kata kunci VB.",
                    "Untuk memakai class yang namanya sama, namanya harus dikurung.",
                    "",
                    "Enum yang diberi atribut `<Flags>` bisa menyimpan banyak pilihan dalam",
                    "satu angka, dengan memakai bit:",
                    "",
                    "  <Flags>",
                    "  Enum Izin",
                    "      Tidak = 0",
                    "      Baca = 1",
                    "      Tulis = 2",
                    "      Hapus = 4",
                    "  End Enum",
                    "",
                    "Nilainya sengaja 1, 2, 4, dan seterusnya, supaya tiap pilihan punya",
                    "bit sendiri dan bisa digabung dengan Or.",
                    "",
                    "Module",
                    "",
                    "Module adalah wadah untuk kode tanpa objek. Semua isinya otomatis",
                    "Shared, dan bisa dipanggil tanpa menyebut nama modulnya dari mana pun",
                    "di proyek yang sama.",
                    "",
                    "Karena itu Module cocok untuk fungsi bantu, konstanta, dan extension",
                    "method, yaitu method tambahan untuk tipe yang udah ada. Tapi Module",
                    "juga gampang jadi tempat buang segala macam fungsi. Kalau sebuah",
                    "Module udah berisi tiga puluh fungsi yang nggak saling berhubungan,",
                    "yang kamu butuhkan adalah beberapa class.",
                ]
            },
            {
                "heading": "Structure, Enum, dan Flags",
                "code": """Option Strict On

Imports System

Structure Titik
    Public ReadOnly X As Integer
    Public ReadOnly Y As Integer

    Public Sub New(x As Integer, y As Integer)
        Me.X = x
        Me.Y = y
    End Sub

    Public Function Jarak() As Double
        Return Math.Sqrt(X * X + Y * Y)
    End Function

    Public Overrides Function ToString() As String
        Return $"({X}, {Y})"
    End Function
End Structure

Class TitikKelas
    Public X As Integer
    Public Y As Integer
End Class

Enum Status
    Draf
    Ditinjau
    Disetujui
    Terbit
End Enum

<Flags>
Enum Izin
    Tidak = 0
    Baca = 1
    Tulis = 2
    Hapus = 4
    Jalan = 8
    Penuh = Baca Or Tulis Or Hapus Or Jalan
End Enum

Module Program

    Sub Main()
        ' --- Structure: DISALIN isinya ---
        Dim s1 As New Titik(1, 2)
        Dim s2 As Titik = s1
        Console.WriteLine($"structure : s1={s1} s2={s2} jarak={s1.Jarak():F3}")

        ' --- Class: disalin ALAMATNYA ---
        Dim c1 As New TitikKelas With {.X = 1, .Y = 2}
        Dim c2 As TitikKelas = c1
        c2.X = 99
        Console.WriteLine($"class     : c1.X={c1.X} c2.X={c2.X}  <- ikut berubah")

        Console.WriteLine("---")

        ' --- Enum ---
        Dim st As Status = Status.Ditinjau
        Console.WriteLine($"nama      : {st}")
        Console.WriteLine($"angka     : {CInt(st)}")
        Console.WriteLine($"dari 3    : {CType(3, Status)}")
        Console.WriteLine($"sah 9?    : {[Enum].IsDefined(GetType(Status), 9)}")

        Console.Write("semua     : ")
        For Each nilai As Status In [Enum].GetValues(GetType(Status))
            Console.Write($"{nilai}({CInt(nilai)}) ")
        Next
        Console.WriteLine()

        Console.WriteLine("---")

        ' --- Flags: banyak pilihan dalam satu angka ---
        Dim editor As Izin = Izin.Baca Or Izin.Tulis
        Console.WriteLine($"editor    : {editor} = {CInt(editor)}")
        Console.WriteLine($"boleh tulis? {editor.HasFlag(Izin.Tulis)}")
        Console.WriteLine($"boleh hapus? {editor.HasFlag(Izin.Hapus)}")

        editor = editor Or Izin.Hapus
        Console.WriteLine($"+hapus    : {editor}")

        editor = editor And Not Izin.Baca
        Console.WriteLine($"-baca     : {editor}")
        Console.WriteLine($"penuh     : {Izin.Penuh} = {CInt(Izin.Penuh)}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  structure : s1=(1, 2) s2=(1, 2) jarak=2.236",
                    "  class     : c1.X=99 c2.X=99  <- ikut berubah",
                    "  ---",
                    "  nama      : Ditinjau",
                    "  angka     : 1",
                    "  dari 3    : Terbit",
                    "  sah 9?    : False",
                    "  semua     : Draf(0) Ditinjau(1) Disetujui(2) Terbit(3)",
                    "  ---",
                    "  editor    : Baca, Tulis = 3",
                    "  boleh tulis? True",
                    "  boleh hapus? False",
                    "  +hapus    : Baca, Tulis, Hapus",
                    "  -baca     : Tulis, Hapus",
                    "  penuh     : Penuh = 15",
                    "",
                    "Baris kedua adalah bug yang paling sering ditemui pemula. Mengubah c2",
                    "ternyata ikut mengubah c1, karena keduanya nama untuk objek yang sama.",
                    "Dengan Structure, hal itu nggak terjadi.",
                    "",
                    "`With {.X = 1, .Y = 2}` adalah object initializer di VB, yaitu cara",
                    "mengisi property sekaligus waktu objek dibuat. Padanannya",
                    "`{ X = 1, Y = 2 }` di C#. Lihat titik di depan nama propertinya.",
                    "",
                    "Hati-hati dengan enum: `CType(9, Status)` nggak divalidasi. Hasilnya",
                    "enum bernilai 9 yang nggak punya nama. Kalau nilainya datang dari",
                    "database atau masukan pengguna, periksa dulu dengan [Enum].IsDefined.",
                    "",
                    "Atribut `<Flags>` nggak mengubah perilaku operasi bit. Operator Or dan",
                    "And bekerja pada enum apa pun. Yang diubahnya cuma ToString: tanpa",
                    "`<Flags>`, editor di atas bakal dicetak sebagai 3, bukan Baca, Tulis.",
                    "",
                    "`And Not Izin.Baca` membuang satu izin. Di sinilah And dan Or tanpa",
                    "hubung-singkat memang yang benar. Untuk bilangan, keduanya bekerja",
                    "sebagai operator bit, bukan operator logika.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Status pesanan, jenis pembayaran, dan level akses biasanya disimpan di",
                    "database sebagai angka kecil, lalu dibaca kembali sebagai Enum supaya",
                    "kodenya menulis Status.Dikirim alih-alih angka 2. Di titik baca itulah",
                    "angka yang nggak dikenal bisa masuk.",
                    "",
                    "Kasus kecil: toko online menyimpan status pesanan sebagai angka 0",
                    "sampai 3. Pesanan berangka 1 harus tampil Dibayar, berangka 3 tampil",
                    "Selesai, dan satu baris rusak berangka 7 harus tampil sebagai status",
                    "yang nggak dikenal.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tulis daftar statusnya sebagai Enum, dengan angka yang ditulis",
                    "     jelas supaya cocok dengan isi database:",
                    "      Enum Status",
                    "          Baru = 0",
                    "          Dibayar = 1",
                    "          Dikirim = 2",
                    "          Selesai = 3",
                    "      End Enum",
                    "  2. Ubah angka dari database dengan CType(angka, Status), lalu cetak",
                    "     dengan ToString(). Angka 1 jadi Dibayar, angka 3 jadi Selesai.",
                    "  3. Periksa angka 7. CType nggak memvalidasi apa pun, dan ToString()",
                    "     cuma mencetak 7. Tanya dulu [Enum].IsDefined(GetType(Status),",
                    "     angka), dan kalau hasilnya False, tampilkan \"status tidak dikenal",
                    "     (7)\".",
                    "  4. Hindari menyisipkan anggota baru di tengah tanpa angka eksplisit.",
                    "     Anggota sesudahnya ikut bergeser nomornya, dan pesanan lama di",
                    "     database mendadak berganti status.",
                ]
            },
        ],
    },
    {
        "title": "12. Exception & Penanganan Galat",
        "sections": [
            {
                "body": [
                    "Exception adalah error yang terjadi waktu program jalan. Kalau nggak",
                    "ditangkap, program berhenti. Cara menangkapnya:",
                    "",
                    "  Try",
                    "      ... kode yang mungkin gagal",
                    "  Catch ex As FormatException",
                    "      ... tangani yang spesifik dulu",
                    "  Catch ex As Exception",
                    "      ... jaring terakhir",
                    "  Finally",
                    "      ... SELALU dijalankan",
                    "  End Try",
                    "",
                    "Urutan Catch penting: yang paling spesifik ditulis paling atas. Kalau",
                    "`Catch ex As Exception` ditulis lebih dulu, Catch di bawahnya nggak",
                    "pernah tercapai, dan compiler bakal memperingatkanmu.",
                    "",
                    "Klausa When",
                    "",
                    "VB punya klausa When, yang baru ada di C# sejak versi 6:",
                    "",
                    "  Catch ex As IOException When ex.HResult = -2147024864",
                    "      ...",
                    "",
                    "When menyaring exception tanpa menangkapnya lebih dulu. Bedanya dengan",
                    "memeriksa di dalam blok Catch: kalau syaratnya nggak terpenuhi,",
                    "exception itu lanjut naik ke pemanggil dengan jejak tumpukan yang",
                    "masih utuh. Jejak tumpukan (stack trace) adalah catatan urutan",
                    "pemanggilan yang sedang berjalan waktu error terjadi.",
                    "",
                    "Melempar exception:",
                    "  Throw New ArgumentException(\"pesan\")",
                    "  Throw                             lempar ulang yang sama",
                    "",
                    "Throw polos mempertahankan jejak tumpukan aslinya. `Throw ex`",
                    "menghapusnya, jadi yang tercatat di log adalah baris Catch-mu, dan",
                    "baris tempat error-nya terjadi hilang dari catatan. Selalu pakai Throw",
                    "polos.",
                    "",
                    "On Error GoTo",
                    "",
                    "On Error GoTo adalah warisan VB6 yang masih ada di VB.NET, dan",
                    "sebaiknya nggak kamu pakai:",
                    "",
                    "  On Error Resume Next      lanjutkan saja, abaikan galat",
                    "  On Error Goto Penanganan",
                    "",
                    "Jangan pakai On Error Resume Next. Perintah itu menelan setiap error,",
                    "dan program jalan terus dalam keadaan rusak. On Error juga nggak bisa",
                    "dicampur dengan Try/Catch di prosedur yang sama.",
                    "",
                    "Exception bawaan yang sering muncul:",
                    "  NullReferenceException     memakai objek Nothing",
                    "  IndexOutOfRangeException   indeks di luar batas",
                    "  ArgumentException          argumen tidak masuk akal",
                    "  ArgumentNullException      argumen Nothing",
                    "  ArgumentOutOfRangeException",
                    "  InvalidOperationException  objek sedang tidak siap",
                    "  InvalidCastException       konversi tipe gagal",
                    "  FormatException            teks tidak sesuai format",
                    "  OverflowException          hasil melewati batas tipe",
                    "  DivideByZeroException      pembagian bulat atau Decimal oleh nol",
                    "  IOException / FileNotFoundException",
                    "",
                    "Catatan: pembagian Double oleh nol nggak melempar exception. Hasilnya",
                    "Infinity, atau NaN (bukan angka). Yang melempar DivideByZeroException",
                    "adalah pembagian bilangan bulat dengan \\ atau Mod, dan juga pembagian",
                    "Decimal.",
                ]
            },
            {
                "heading": "Exception sendiri, When, dan Finally",
                "code": """Option Strict On

Imports System

Class SaldoKurangException
    Inherits Exception

    Public ReadOnly Property Kurang As Long

    Public Sub New(kurang As Long)
        MyBase.New($"saldo kurang {kurang}")
        Me.Kurang = kurang
    End Sub
End Class

Class Dompet
    Private _saldo As Long

    Public Sub New(saldo As Long)
        _saldo = saldo
    End Sub

    Public ReadOnly Property Saldo As Long
        Get
            Return _saldo
        End Get
    End Property

    Public Sub Bayar(jumlah As Long)
        If jumlah <= 0 Then
            Throw New ArgumentOutOfRangeException(NameOf(jumlah),
                                                  $"jumlah {jumlah} tidak sah")
        End If
        If jumlah > _saldo Then Throw New SaldoKurangException(jumlah - _saldo)
        _saldo -= jumlah
    End Sub
End Class

Module Program

    Function DenganPengukur(nama As String, kerja As Func(Of Integer)) As Integer?
        Console.WriteLine($"mulai {nama}")
        Try
            Dim hasil As Integer = kerja()
            Console.WriteLine($"selesai {nama}")
            Return hasil
        Catch ex As InvalidOperationException
            Console.WriteLine($"galat: {ex.Message}")
            Return Nothing
        Finally
            Console.WriteLine($"(bersih {nama})")
        End Try
    End Function

    Sub Main()
        Dim d As New Dompet(50000)

        For Each tagihan As Long In New Long() {20000, -5, 100000, 30000}
            Try
                d.Bayar(tagihan)
                Console.WriteLine($"bayar {tagihan,7} -> sisa {d.Saldo}")
            Catch ex As SaldoKurangException
                Console.WriteLine($"bayar {tagihan,7} -> GAGAL, kurang {ex.Kurang}")
            Catch ex As ArgumentOutOfRangeException
                Console.WriteLine($"bayar {tagihan,7} -> DITOLAK: jumlah tidak sah")
            End Try
        Next

        Console.WriteLine("---")
        Console.WriteLine($"hasil: {DenganPengukur("hitung", Function() 6 * 7)}")
        Dim gagal As Integer? = DenganPengukur("gagal",
            Function() As Integer
                Throw New InvalidOperationException("rusak")
            End Function)
        Console.WriteLine($"hasil: {If(gagal.HasValue, gagal.ToString(), "Nothing")}")

        Console.WriteLine("---")

        ' Catch ... When: menyaring TANPA menangkap lebih dulu
        For Each teks As String In New String() {"42", "abc"}
            Try
                Console.WriteLine($"{teks} -> {Integer.Parse(teks)}")
            Catch ex As FormatException When teks = ""
                Console.WriteLine("teks kosong")
            Catch ex As FormatException
                Console.WriteLine($"{teks} -> bukan angka")
            End Try
        Next

        Console.WriteLine("---")
        Console.WriteLine($"1.0 / 0 = {1.0 / 0}")
        Dim nol As Integer = 0
        Try
            Console.WriteLine(1 \\ nol)
        Catch ex As DivideByZeroException
            Console.WriteLine("1 \\ 0 -> DivideByZeroException")
        End Try
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  bayar   20000 -> sisa 30000",
                    "  bayar      -5 -> DITOLAK: jumlah tidak sah",
                    "  bayar  100000 -> GAGAL, kurang 70000",
                    "  bayar   30000 -> sisa 0",
                    "  ---",
                    "  mulai hitung",
                    "  selesai hitung",
                    "  (bersih hitung)",
                    "  hasil: 42",
                    "  mulai gagal",
                    "  galat: rusak",
                    "  (bersih gagal)",
                    "  hasil: Nothing",
                    "  ---",
                    "  42 -> 42",
                    "  abc -> bukan angka",
                    "  ---",
                    "  1.0 / 0 = Infinity",
                    "  1 \\ 0 -> DivideByZeroException",
                    "",
                    "Dua baris terakhir nunjukin hal yang sering bikin kaget. Pembagian",
                    "Double oleh nol nggak melempar apa pun, hasilnya Infinity. Yang",
                    "melempar cuma pembagian bulat (dan pembagian Decimal). Kalau kamu",
                    "mengandalkan exception untuk menangkap pembagian nol pada Double,",
                    "exception itu nggak akan pernah datang.",
                    "",
                    "Finally tetap dijalankan walaupun bloknya melempar exception. Di kasus",
                    "kedua, \"selesai gagal\" nggak tercetak, tapi \"(bersih gagal)\" tetap",
                    "tercetak. Karena itu Finally bisa menjamin berkas ditutup dan koneksi",
                    "dilepas.",
                    "",
                    "`Function() As Integer ... End Function` adalah lambda multi-baris.",
                    "Lambda adalah fungsi tanpa nama yang ditulis langsung di tempat",
                    "dipakai. VB butuh bentuk panjang ini untuk lambda yang isinya lebih",
                    "dari satu ekspresi, sedangkan C# cukup memakai kurung kurawal.",
                    "",
                    "`Integer?` adalah `Nullable(Of Integer)`, yaitu Integer yang boleh",
                    "bernilai Nothing. Untuk tipe nilai, tanda tanya itu wajib. Tipe",
                    "referensi memang boleh Nothing sejak awal.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi yang dipakai orang lain harus tahan terhadap masukan yang",
                    "aneh. Fungsi hitung melempar exception waktu aturannya dilanggar, lalu",
                    "layar menangkapnya dan menampilkan pesan yang bisa dimengerti, alih-alih",
                    "jendela error yang menutup aplikasi.",
                    "",
                    "Kasus kecil: aplikasi patungan makan membagi tagihan 150000 rata ke",
                    "semua orang. Untuk 4 orang, tiap orang membayar 37500. Kalau jumlah",
                    "orangnya diisi 0, aplikasi harus menolak dengan pesan yang jelas.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan siapa yang memeriksa aturan \"minimal 1 orang\". Fungsi",
                    "     hitungnya yang paling tahu, jadi dia yang melempar:",
                    "      Function Bagian(total As Decimal, orang As Integer) As Decimal",
                    "          If orang < 1 Then Throw New ArgumentException(\"minimal 1 orang\")",
                    "          Return Math.Round(total / orang, 0)",
                    "      End Function",
                    "  2. Di layar, bungkus pemanggilannya dengan Try, lalu tangkap dengan",
                    "     `Catch ex As ArgumentException` dan tampilkan ex.Message.",
                    "  3. Uji kedua jalurnya. Bagian(150000D, 4) menghasilkan 37500, dan",
                    "     Bagian(150000D, 0) berakhir di Catch dengan pesan \"minimal 1",
                    "     orang\".",
                    "  4. Bandingkan dengan membiarkan pembagiannya apa adanya. Decimal",
                    "     melempar DivideByZeroException dengan pesan \"Attempted to divide by",
                    "     zero\", yang nggak menjelaskan apa-apa ke pengguna. Kalau totalnya",
                    "     Double, nggak ada exception sama sekali, dan layar menulis",
                    "     Infinity.",
                ]
            },
        ],
    },
    {
        "title": "13. LINQ & Lambda",
        "sections": [
            {
                "body": [
                    "LINQ (Language Integrated Query) adalah cara mengolah koleksi data,",
                    "misalnya menyaring, mengurutkan, dan menghitung, langsung di dalam",
                    "bahasa. LINQ tersedia penuh di VB, dan sintaks query-nya malah lebih",
                    "lengkap daripada di C#.",
                    "",
                    "  Imports System.Linq",
                    "",
                    "Ada dua bentuk penulisan, dan hasilnya sama persis:",
                    "",
                    "  ' Query syntax",
                    "  Dim lulus = From m In murid",
                    "              Where m.Nilai >= 75",
                    "              Order By m.Nilai Descending",
                    "              Select m.Nama",
                    "",
                    "  ' Method syntax",
                    "  Dim lulus = murid.Where(Function(m) m.Nilai >= 75).",
                    "                    OrderByDescending(Function(m) m.Nilai).",
                    "                    Select(Function(m) m.Nama)",
                    "",
                    "Kata kunci query VB: From, Where, Select, Order By, Group By, Join,",
                    "Let, Distinct, Take, Skip, Aggregate.",
                    "",
                    "Aggregate adalah kata kunci yang nggak ada di C#. Dengan Aggregate,",
                    "perhitungan ringkasan bisa ditulis sebagai query:",
                    "",
                    "  Dim total = Aggregate m In murid Into Sum(m.Nilai)",
                    "  Dim rata = Aggregate m In murid Into Average(m.Nilai)",
                    "",
                    "Lambda",
                    "",
                    "Lambda di VB ditulis dengan Function atau Sub:",
                    "",
                    "  Function(x) x * x                satu ekspresi",
                    "  Sub(x) Console.WriteLine(x)      tanpa kembalian",
                    "",
                    "  Function(x As Integer) As Integer",
                    "      Dim h = x * x",
                    "      Return h",
                    "  End Function",
                    "",
                    "Bentuk multi-baris butuh End Function. Memang lebih panjang daripada",
                    "C#, tapi batasnya lebih jelas.",
                    "",
                    "Tipe delegate, yaitu tipe untuk variabel yang isinya fungsi:",
                    "  Func(Of Integer, Integer)         (Int) -> Int",
                    "  Func(Of Integer, Integer, Integer)",
                    "  Action(Of String)                 tanpa kembalian",
                    "  Predicate(Of Integer)             -> Boolean",
                    "",
                    "Di `Func(Of ...)`, tipe yang terakhir adalah tipe kembaliannya.",
                    "",
                    "Deferred execution, atau eksekusi yang ditunda, berlaku sama seperti",
                    "di C#. Query baru dijalankan waktu hasilnya ditelusuri, bukan waktu",
                    "query-nya ditulis. Panggil .ToList() untuk membekukan hasilnya.",
                ]
            },
            {
                "heading": "LINQ pada data nyata",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Globalization
Imports System.Linq

Class Murid
    Public Property Nama As String
    Public Property Kelas As String
    Public Property Nilai As Integer

    Public Sub New(nama As String, kelas As String, nilai As Integer)
        Me.Nama = nama
        Me.Kelas = kelas
        Me.Nilai = nilai
    End Sub
End Class

Module Program

    Sub Main()
        Dim data As New List(Of Murid) From {
            New Murid("Andi", "A", 88),
            New Murid("Budi", "B", 72),
            New Murid("Cici", "A", 95),
            New Murid("Dedi", "B", 64),
            New Murid("Euis", "A", 79),
            New Murid("Fajar", "B", 91)
        }

        Console.WriteLine("-- Lulus, nilai tertinggi dulu --")
        Dim lulus = From m In data
                    Where m.Nilai >= 75
                    Order By m.Nilai Descending
                    Select m

        For Each m As Murid In lulus
            Console.WriteLine($"  {m.Nama,-6}{m.Kelas} {m.Nilai}")
        Next

        Console.WriteLine("---")
        Console.WriteLine($"rata-rata : {data.Average(Function(m) m.Nilai):F2}")
        Console.WriteLine($"tertinggi : {data.Max(Function(m) m.Nilai)}")
        ' List(Of T) punya PROPERTY Count, yang MENUTUPI extension Count(...)
        ' dari LINQ. Menulis data.Count(...) membuat VB mengira itu
        ' pengindeksan properti, bukan pemanggilan method.
        Console.WriteLine($"lulus     : {data.Where(Function(m) m.Nilai >= 75).Count}")
        Console.WriteLine($"ada <65?  : {data.Any(Function(m) m.Nilai < 65)}")
        Console.WriteLine($"semua >60?: {data.All(Function(m) m.Nilai > 60)}")

        Console.WriteLine("---")
        Console.WriteLine("-- Per kelas --")
        Dim perKelas = From m In data
                       Group m By kelas = m.Kelas Into Grup = Group
                       Order By kelas
                       Select kelas, Jumlah = Grup.Count,
                              Rata = Grup.Average(Function(x) x.Nilai)

        For Each g In perKelas
            Console.WriteLine($"  Kelas {g.kelas}: {g.Jumlah} murid, rata-rata {g.Rata:F1}")
        Next

        Console.WriteLine("---")
        ' Aggregate: kata kunci yang tidak ada di C#
        Dim total = Aggregate m In data Into Sum(m.Nilai)
        Console.WriteLine($"total nilai : {total}")

        Console.WriteLine("---")
        ' Lambda disimpan di dalam Dictionary
        Dim operasi As New Dictionary(Of String, Func(Of Integer, Integer, Integer)) From {
            {"tambah", Function(a, b) a + b},
            {"kurang", Function(a, b) a - b},
            {"kali", Function(a, b) a * b}
        }

        For Each pasangan In operasi
            Console.WriteLine($"{pasangan.Key,-7}(9, 4) = {pasangan.Value(9, 4)}")
        Next
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  -- Lulus, nilai tertinggi dulu --",
                    "    Cici  A 95",
                    "    Fajar B 91",
                    "    Andi  A 88",
                    "    Euis  A 79",
                    "  ---",
                    "  rata-rata : 81.50",
                    "  tertinggi : 95",
                    "  lulus     : 4",
                    "  ada <65?  : True",
                    "  semua >60?: True",
                    "  ---",
                    "  -- Per kelas --",
                    "    Kelas A: 3 murid, rata-rata 87.3",
                    "    Kelas B: 3 murid, rata-rata 75.7",
                    "  ---",
                    "  total nilai : 489",
                    "  ---",
                    "  tambah (9, 4) = 13",
                    "  kurang (9, 4) = 5",
                    "  kali   (9, 4) = 36",
                    "",
                    "`Group m By kelas = m.Kelas Into Grup = Group` adalah bentuk",
                    "pengelompokan di VB. Kata Group di ujung adalah kata kunci yang artinya",
                    "\"seluruh anggota kelompok ini\".",
                    "",
                    "Hasil `Select kelas, Jumlah = ..., Rata = ...` adalah tipe anonim,",
                    "yaitu class yang dibuatkan compiler dengan property persis seperti yang",
                    "kamu sebutkan. Karena itu g.Jumlah dan g.Rata langsung bisa dipakai",
                    "tanpa mendeklarasikan class apa pun.",
                    "",
                    "Lihat `Dim perKelas = ...` yang ditulis tanpa As. Itu inferensi tipe,",
                    "dan di sini dia wajib, karena tipe anonim nggak punya nama yang bisa",
                    "kamu tulis. Inferensi aktif kalau Option Infer On, yang jadi bawaan di",
                    "proyek baru.",
                    "",
                    "Jebakan khas VB yang nggak ada di C#: List(Of T) punya property",
                    "bernama Count, dan property itu menutupi extension method Count(...)",
                    "milik LINQ. Kalau kamu menulis `data.Count(Function(m) ...)`, VB",
                    "mengira kamu mau mengindeks property Count. Pesan errornya berbunyi",
                    "\"its return type cannot be indexed\", tanpa menyebut LINQ sama sekali.",
                    "Jalan keluarnya: saring dulu, lalu baca property-nya, seperti",
                    "`data.Where(...).Count`.",
                    "",
                    "`pasangan.Value(9, 4)` memanggil delegate yang tersimpan di",
                    "Dictionary. Di VB, memanggil delegate memakai kurung biasa, sama",
                    "seperti mengindeks array, karena keduanya memang memakai tanda yang",
                    "sama.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Laporan di aplikasi kasir, seperti penjualan per kasir, per kategori,",
                    "atau per hari, biasanya berupa pengelompokan lalu penjumlahan. Dengan",
                    "LINQ, laporan seperti itu ditulis sebagai satu query, dan Group By di",
                    "VB bisa langsung menghitung Sum dan Count untuk tiap kelompok.",
                    "",
                    "Kasus kecil: hari ini minimarket mencatat enam transaksi, yaitu",
                    "Rina 85000, Dodi 120000, Rina 45000, Sari 150000, Dodi 30000, dan",
                    "Rina 110000. Manajer minta total per kasir dari yang terbesar,",
                    "ditambah jumlah transaksi di atas 100000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Pahami keluarannya: satu baris per kasir berisi total dan jumlah",
                    "     transaksinya. Itu bentuk Group By.",
                    "  2. Kelompokkan per kasir, hitung Sum dan Count di klausa Into, lalu",
                    "     urutkan:",
                    "      Dim perKasir =",
                    "          From t In data",
                    "          Group t By t.Kasir Into Total = Sum(t.Total), Jumlah = Count()",
                    "          Order By Total Descending, Kasir",
                    "  3. Hasilnya Rina 240000 dari 3 transaksi, Dodi 150000 dari 2, dan Sari",
                    "     150000 dari 1. Transaksi di atas 100000 dihitung dengan",
                    "     `data.Where(Function(t) t.Total > 100000).Count`, hasilnya 3.",
                    "  4. Periksa total yang kembar. Dodi dan Sari sama-sama 150000. Tanpa",
                    "     Kasir sebagai patokan kedua, urutan keduanya cuma ikut urutan",
                    "     kemunculan di data, jadi laporan bisa berganti urutan kalau datanya",
                    "     dibaca dari sumber lain.",
                    "",
                    "Ingat: `data.Count(Function(t) ...)` ditolak VB karena List punya",
                    "property Count, jadi saring dulu dengan Where.",
                ]
            },
        ],
    },
    {
        "title": "14. Berkas, Data & Using",
        "sections": [
            {
                "body": [
                    "Untuk berkas, VB memakai pustaka .NET yang sama dengan C#:",
                    "",
                    "  Imports System.IO",
                    "",
                    "  File.WriteAllText(path, isi)",
                    "  File.AppendAllText(path, isi)",
                    "  File.ReadAllText(path)",
                    "  File.ReadAllLines(path)",
                    "  File.WriteAllLines(path, baris)",
                    "  File.ReadLines(path)       baca bertahap, hemat memori",
                    "",
                    "  File.Exists(path)  File.Delete(path)",
                    "  File.Copy(a, b, True)  File.Move(a, b)",
                    "  Directory.CreateDirectory(path)",
                    "  Directory.GetFiles(path, \"*.txt\")",
                    "",
                    "ReadLines membaca baris satu per satu waktu dibutuhkan, jadi isi",
                    "berkasnya nggak dimuat ke memori sekaligus.",
                    "",
                    "Menyusun path, yaitu jalur berkas, yang jalan di semua sistem operasi:",
                    "  Path.Combine(folder, \"data\", \"murid.txt\")",
                    "  Path.GetFileName / GetExtension / GetDirectoryName",
                    "  Path.GetTempPath()",
                    "",
                    "Jangan menyambung path dengan garis miring sendiri. Pemisah folder di",
                    "tiap sistem operasi beda-beda.",
                    "",
                    "Using",
                    "",
                    "Using melepas sumber daya secara otomatis. Sumber daya di sini artinya",
                    "hal yang dipinjam dari sistem operasi, seperti berkas yang sedang",
                    "dibuka:",
                    "",
                    "  Using penulis As New StreamWriter(path)",
                    "      penulis.WriteLine(\"baris\")",
                    "  End Using          ' ditutup di sini, GAGAL ATAU TIDAK",
                    "",
                    "Using setara dengan Try/Finally yang memanggil Dispose, dan wajib",
                    "dipakai untuk apa pun yang memegang berkas, koneksi, atau soket. Tanpa",
                    "Using, satu exception di tengah bikin baris penutupnya nggak pernah",
                    "tercapai, dan berkasnya tetap terbuka.",
                    "",
                    "Satu Using boleh memuat beberapa sumber daya:",
                    "  Using a As New StreamReader(p1),",
                    "        b As New StreamWriter(p2)",
                    "",
                    "Namespace My",
                    "",
                    "Namespace My adalah fitur khas VB yang nggak ada di C#. Isinya jalan",
                    "pintas ke hal-hal yang sering dipakai:",
                    "",
                    "  My.Computer.FileSystem.ReadAllText(path)",
                    "  My.Computer.FileSystem.WriteAllText(path, isi, False)",
                    "  My.Application.Info.Version",
                    "  My.Settings.NamaSetelan",
                    "",
                    "My nyaman untuk skrip kecil dan aplikasi Windows Forms. Untuk pustaka",
                    "dan aplikasi lintas platform, pakai API .NET biasa. API itu lebih",
                    "portabel, dan contohnya lebih gampang dicari karena sama dengan yang",
                    "dipakai C#.",
                    "",
                    "Untuk CSV sungguhan, jangan pakai `Split(\",\")`, karena kolom yang",
                    "dikutip boleh berisi koma. VB menyediakan TextFieldParser di namespace",
                    "Microsoft.VisualBasic.FileIO.",
                ]
            },
            {
                "heading": "Menulis, membaca, dan mengolah berkas",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Globalization
Imports System.IO
Imports System.Linq

Module Program

    Sub Main()
        Dim berkas As String = Path.Combine(Path.GetTempPath(), "belajar-vb.csv")

        ' --- Tulis dengan Using: ditutup apa pun yang terjadi ---
        Using penulis As New StreamWriter(berkas, append:=False)
            penulis.WriteLine("nama,kelas,nilai")
            penulis.WriteLine("Andi,A,88")
            penulis.WriteLine("Budi,B,72")
            penulis.WriteLine("Cici,A,95")
        End Using

        Console.WriteLine($"ditulis   : {Path.GetFileName(berkas)}")

        ' --- Baca kembali dan urai ---
        Dim baris() As String = File.ReadAllLines(berkas)
        Dim data = baris.Skip(1).
                         Select(Function(b) b.Split(","c)).
                         Select(Function(k) New With {
                             .Nama = k(0),
                             .Kelas = k(1),
                             .Nilai = CInt(k(2))
                         }).ToList()

        For Each m In data.OrderByDescending(Function(x) x.Nilai)
            Console.WriteLine($"  {m.Nama,-6}{m.Kelas} {m.Nilai,3}")
        Next

        Console.WriteLine($"rata-rata : {data.Average(Function(x) x.Nilai):F2}")

        Console.WriteLine("---")

        ' --- Baca baris demi baris, hemat memori ---
        Dim nomor As Integer = 0
        For Each b As String In File.ReadLines(berkas)
            nomor += 1
            Console.WriteLine($"{nomor,2}| {b}")
        Next

        Console.WriteLine("---")
        Console.WriteLine($"ukuran    : {New FileInfo(berkas).Length} byte")

        File.Delete(berkas)
        Console.WriteLine($"masih ada?: {File.Exists(berkas)}")

        Console.WriteLine("---")

        ' --- Menangani kegagalan berkas dengan jujur ---
        Try
            File.ReadAllText(Path.Combine(Path.GetTempPath(), "tidak-ada-xyz.txt"))
        Catch ex As FileNotFoundException
            Console.WriteLine("FileNotFoundException tertangkap")
        Catch ex As IOException
            Console.WriteLine($"IOException: {ex.Message}")
        End Try
    End Sub

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  ditulis   : belajar-vb.csv",
                    "    Cici  A  95",
                    "    Andi  A  88",
                    "    Budi  B  72",
                    "  rata-rata : 85.00",
                    "  ---",
                    "   1| nama,kelas,nilai",
                    "   2| Andi,A,88",
                    "   3| Budi,B,72",
                    "   4| Cici,A,95",
                    "  ---",
                    "  ukuran    : 47 byte",
                    "  masih ada?: False",
                    "  ---",
                    "  FileNotFoundException tertangkap",
                    "",
                    "`New With { .Nama = ..., .Kelas = ... }` membuat tipe anonim, yaitu",
                    "class sekali pakai yang dibuatkan compiler. Ini berguna persis di",
                    "situasi seperti ini, waktu bentuk datanya cuma dipakai di dalam satu",
                    "prosedur.",
                    "",
                    "Lihat urutan Catch: FileNotFoundException ditulis sebelum IOException.",
                    "FileNotFoundException adalah turunan IOException, jadi kalau urutannya",
                    "dibalik, Catch untuk FileNotFoundException nggak pernah tercapai.",
                    "Kalau itu terjadi, compiler VB memperingatkanmu.",
                    "",
                    "`append:=False` memakai argumen bernama. Tanpa nama itu, pembaca kode",
                    "harus ingat arti False di posisi kedua. Kalau salah tebak, berkasnya",
                    "ditimpa padahal seharusnya ditambahi, atau sebaliknya.",
                    "",
                    "Ukuran 47 byte berlaku kalau berkasnya memakai akhiran baris satu",
                    "karakter. Di Windows, StreamWriter menulis dua karakter per baris,",
                    "jadi ukurannya beda. Ingat ini waktu membandingkan berkas antar sistem",
                    "operasi.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi kasir sederhana sering menyimpan catatan transaksi di berkas",
                    "teks per hari, misalnya transaksi-2026-10-17.csv, yang bisa dibuka di",
                    "Excel dan sekaligus jadi cadangan. Satu baris ditambahkan tiap ada",
                    "transaksi, dan di akhir hari berkas itu dibaca ulang untuk menghitung",
                    "omzet.",
                    "",
                    "Kasus kecil: hari ini ada tiga transaksi, yaitu 47500 pukul 08.15,",
                    "120000 pukul 09.02, dan 15500 pukul 10.40. Tiap transaksi harus",
                    "langsung masuk berkas hari itu, dan laporan sore harus menulis omzet",
                    "183000.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Susun nama berkasnya dari tanggal dengan Path.Combine, jangan",
                    "     dengan garis miring yang diketik sendiri.",
                    "  2. Tambahkan satu baris tiap transaksi dengan Using, supaya berkasnya",
                    "     tertutup walaupun ada exception di tengah jalan:",
                    "      Using penulis As New StreamWriter(berkas, append:=True)",
                    "          penulis.WriteLine($\"{jam},{total}\")",
                    "      End Using",
                    "  3. Untuk laporan sore, baca dengan File.ReadLines, pecah tiap baris",
                    "     dengan Split(\",\"c), lalu jumlahkan CDec dari kolom kedua. Tiga",
                    "     baris tadi menghasilkan 183000.",
                    "  4. Periksa hari tanpa transaksi. StreamWriter dengan append:=True",
                    "     membuat berkasnya sendiri di transaksi pertama, tapi File.ReadLines",
                    "     melempar FileNotFoundException kalau berkasnya belum ada. Cek",
                    "     File.Exists dulu, lalu laporkan omzet 0.",
                ]
            },
        ],
    },
    {
        "title": "15. Praktik Baik & Jebakan Umum",
        "sections": [
            {
                "body": [
                    "Saklar yang wajib dinyalakan di setiap proyek:",
                    "",
                    "  Option Strict On      tolak konversi tipe yang nggak ditulis",
                    "  Option Explicit On    wajib deklarasikan variabel",
                    "  Option Infer On       boleh menyimpulkan tipe",
                    "",
                    "Yang pertama jauh lebih penting daripada dua lainnya. Tanpa Option",
                    "Strict, VB menerima hampir semua kode, lalu kode itu baru gagal waktu",
                    "program jalan.",
                    "",
                    "Di berkas .vbproj:",
                    "  <OptionStrict>On</OptionStrict>",
                    "  <OptionExplicit>On</OptionExplicit>",
                    "  <OptionInfer>On</OptionInfer>",
                    "",
                    "Daftar jebakan yang paling sering:",
                    "  1. `Dim a(4)` menghasilkan lima elemen, bukan empat. Angkanya batas",
                    "     atas, bukan jumlah.",
                    "  2. `For i = 1 To 5` berjalan lima kali. Batasnya inklusif, beda",
                    "     dengan `i < 5` di bahasa lain.",
                    "  3. And dan Or nggak hubung-singkat. Pakai AndAlso dan OrElse untuk",
                    "     kondisi logika.",
                    "  4. `= Nothing` bukan cara memeriksa objek kosong. Pakai Is Nothing",
                    "     dan IsNot Nothing.",
                    "  5. Tanda + pada teks itu ambigu. Pakai & untuk menyambung teks.",
                    "  6. Mengisi nama fungsi (`Grade = \"A\"`) nggak menghentikan fungsinya.",
                    "     Pakai Return.",
                    "  7. On Error Resume Next menelan setiap error dan membiarkan program",
                    "     jalan dalam keadaan rusak.",
                    "  8. Nama nggak membedakan huruf besar-kecil, jadi nilai dan Nilai",
                    "     adalah variabel yang sama. Kalau kamu mau membedakan field dari",
                    "     property, pakai awalan garis bawah untuk field-nya.",
                    "",
                    "Penamaan menurut kebiasaan .NET:",
                    "  PascalCase  class, method, property, event, konstanta",
                    "  camelCase   parameter dan variabel lokal",
                    "  _camelCase  field privat",
                    "  I di depan  interface",
                    "",
                    "Beda dengan Java, konstanta di .NET memakai PascalCase (MaksCoba),",
                    "bukan huruf besar semua.",
                    "",
                    "Kebiasaan yang bikin kode VB enak dirawat:",
                    "  - Keluar lebih awal dari fungsi dengan Return, daripada menumpuk If",
                    "    bertingkat.",
                    "  - Pakai field ReadOnly kalau isinya nggak pernah berubah sesudah",
                    "    constructor.",
                    "  - Kembalikan koleksi kosong, jangan Nothing.",
                    "  - Satu prosedur, satu pekerjaan.",
                    "  - Nyalakan analyzer .NET, yaitu pemeriksa kode otomatis, dan jadikan",
                    "    peringatannya error di berkas proyek.",
                ]
            },
            {
                "heading": "Melihat jebakannya sendiri",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic

Module Program

    Function GayaLama(nilai As Integer) As String
        ' Gaya VB6: menugaskan ke nama fungsi TIDAK menghentikannya
        GayaLama = "A"
        If nilai < 85 Then GayaLama = "B"
        ' baris di bawah ini TETAP dijalankan
        If nilai < 75 Then GayaLama = "C"
    End Function

    Function GayaBaru(nilai As Integer) As String
        If nilai >= 85 Then Return "A"
        If nilai >= 75 Then Return "B"
        Return "C"
    End Function

    Sub Main()
        ' --- 1. Batas atas array, bukan jumlah ---
        Dim a(4) As Integer
        Console.WriteLine($"Dim a(4)      -> {a.Length} elemen (indeks 0..{UBound(a)})")

        ' --- 2. For inklusif ---
        Dim hitung As Integer = 0
        For i As Integer = 1 To 5
            hitung += 1
        Next
        Console.WriteLine($"For 1 To 5    -> {hitung} kali")

        Console.WriteLine("---")

        ' --- 3. AndAlso versus And ---
        Dim teks As String = Nothing
        Console.WriteLine($"AndAlso aman  : {teks IsNot Nothing AndAlso teks.Length > 0}")
        Try
            Console.WriteLine(teks IsNot Nothing And teks.Length > 0)
        Catch ex As NullReferenceException
            Console.WriteLine("And bahaya    : NullReferenceException")
        End Try

        Console.WriteLine("---")

        ' --- 4. Is Nothing, bukan = Nothing ---
        Console.WriteLine($"Is Nothing    : {teks Is Nothing}")

        ' --- 5. & versus + untuk teks ---
        Console.WriteLine("& selalu teks : " & "1" & 2)

        Console.WriteLine("---")

        ' --- 6. Gaya lama versus Return ---
        For Each n As Integer In New Integer() {92, 80, 70}
            Console.WriteLine($"{n,3}: lama={GayaLama(n)} baru={GayaBaru(n)}")
        Next

        Console.WriteLine("---")

        ' --- 8. Nama tidak membedakan huruf besar-kecil ---
        Dim nilai As Integer = 10
        NILAI = 20                       ' variabel yang SAMA
        Console.WriteLine($"nilai sesudah : {nilai}")

        Console.WriteLine("---")

        ' Kembalikan koleksi KOSONG, bukan Nothing
        Console.WriteLine($"kosong bukan Nothing: {Kosong().Count} elemen")
    End Sub

    Function Kosong() As List(Of String)
        Return New List(Of String)
    End Function

End Module"""
            },
            {
                "body": [
                    "Keluaran:",
                    "  Dim a(4)      -> 5 elemen (indeks 0..4)",
                    "  For 1 To 5    -> 5 kali",
                    "  ---",
                    "  AndAlso aman  : False",
                    "  And bahaya    : NullReferenceException",
                    "  ---",
                    "  Is Nothing    : True",
                    "  & selalu teks : 12",
                    "  ---",
                    "   92: lama=A baru=A",
                    "   80: lama=B baru=B",
                    "   70: lama=C baru=C",
                    "  ---",
                    "  nilai sesudah : 20",
                    "  ---",
                    "  kosong bukan Nothing: 0 elemen",
                    "",
                    "Fungsi GayaLama kebetulan memberi jawaban yang benar di sini, dan",
                    "justru itu yang berbahaya. Dia tetap benar sampai seseorang menambah",
                    "satu baris di bawahnya tanpa sadar bahwa fungsinya belum berhenti.",
                    "Bentuk Return nggak punya masalah itu.",
                    "",
                    "Lihat baris ini di contoh:",
                    "",
                    "  NILAI = 20                       ' variabel yang SAMA",
                    "",
                    "VB nggak membedakan huruf besar-kecil, jadi baris itu mengubah",
                    "variabel nilai yang sama. Editor biasanya merapikan ejaannya otomatis.",
                    "Tapi di kode yang disunting lewat alat lain, dua ejaan untuk satu",
                    "variabel bikin pembacanya bingung.",
                    "",
                    "Kosong() mengembalikan List kosong, bukan Nothing. Pemanggilnya jadi",
                    "bisa langsung memakai For Each tanpa memeriksa apa pun. Kalau koleksi",
                    "dikembalikan sebagai Nothing, setiap pemanggil harus menulis",
                    "pemeriksaan, dan satu yang lupa menghasilkan NullReferenceException.",
                    "",
                    "Untuk memeriksa kualitas kode secara otomatis:",
                    "  dotnet build -warnaserror",
                    "  <EnableNETAnalyzers>true</EnableNETAnalyzers>",
                    "  <TreatWarningsAsErrors>true</TreatWarningsAsErrors>",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Kalau kamu PKL atau mulai kerja di kantor yang memakai VB, tugas",
                    "pertamamu kemungkinan merawat kode lama. Banyak bug di kode seperti itu",
                    "nggak menggagalkan kompilasi, padahal compiler VB udah memberi",
                    "peringatan yang tinggal dibaca.",
                    "",
                    "Kasus kecil: laporan koperasi kadang berhenti dengan",
                    "NullReferenceException, dan cuma untuk sebagian anggota. Laporannya",
                    "memanggil Kategori(belanja).ToUpper() untuk tiap anggota.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Baca fungsi yang dipanggil, lalu cari jalur yang nggak berakhir di",
                    "     Return:",
                    "      Function Kategori(belanja As Decimal) As String",
                    "          If belanja >= 100000 Then Return \"besar\"",
                    "          If belanja >= 50000 Then Return \"sedang\"",
                    "      End Function",
                    "  2. Cari masukan yang lewat jalur itu: belanja di bawah 50000. Untuk",
                    "     20000, fungsinya selesai tanpa Return dan mengembalikan Nothing",
                    "     tanpa error, lalu ToUpper() melempar NullReferenceException.",
                    "  3. Betulkan di sumbernya dengan Return terakhir, misalnya",
                    "     `Return \"kecil\"`. Semua pemanggil langsung aman tanpa diubah.",
                    "  4. Cegah terulang. Compiler udah memberi peringatan BC42105,",
                    "     \"Function 'Kategori' doesn't return a value on all code paths\".",
                    "     Dengan `<TreatWarningsAsErrors>true</TreatWarningsAsErrors>` di",
                    "     berkas proyek, peringatan itu jadi error dan build berhenti.",
                ]
            },
        ],
    },
    {
        "title": "16. Proyek Utuh: Menggabungkan Semuanya",
        "sections": [
            {
                "body": [
                    "Materi penutup ini menggabungkan class, property, enum, exception,",
                    "LINQ, dan pemisahan tanggung jawab dalam satu program utuh.",
                    "",
                    "Yang dibangun: sistem inventaris gudang. Fiturnya sendiri nggak",
                    "penting. Yang penting cara bagian-bagiannya dipisah.",
                    "",
                    "Ada tiga lapisan, dan arah ketergantungannya cuma satu:",
                    "",
                    "  Antarmuka  ->  Layanan  ->  Model",
                    "",
                    "  - Model: Class Barang, Enum Gerak, dan keluarga exception-nya.",
                    "    Bagian ini nggak tahu apa-apa soal layar.",
                    "  - Layanan: Class Gudang beserta semua aturannya. Bagian ini nggak",
                    "    pernah memanggil Console.",
                    "  - Antarmuka: Module Program. Bagian ini memanggil layanan, mencetak",
                    "    hasilnya, dan nggak menghitung apa pun.",
                    "",
                    "Cara ngujinya gampang. Bayangkan program ini diubah jadi aplikasi web",
                    "ASP.NET. Kalau pemisahannya benar, yang harus disentuh cuma Module",
                    "Program.",
                    "",
                    "Kesalahan yang paling sering di program VB pemula adalah mencampur",
                    "ketiganya, misalnya menghitung total di tengah Console.WriteLine.",
                    "Programnya tetap jalan. Masalahnya baru muncul waktu ada yang minta",
                    "total yang sama juga tampil di laporan lain.",
                ]
            },
            {
                "heading": "Program lengkap",
                "code": """Option Strict On

Imports System
Imports System.Collections.Generic
Imports System.Linq

' ---------------------------------------------------------------- MODEL
Public Enum Gerak
    Masuk
    Keluar
End Enum

Public Class Barang
    Public ReadOnly Property Kode As String
    Public ReadOnly Property Nama As String
    Public ReadOnly Property Harga As Long
    Public Property Stok As Integer

    Public Sub New(kode As String, nama As String, stok As Integer, harga As Long)
        Me.Kode = kode
        Me.Nama = nama
        Me.Stok = stok
        Me.Harga = harga
    End Sub

    Public ReadOnly Property Subtotal As Long
        Get
            Return Stok * Harga
        End Get
    End Property

    Public Overrides Function ToString() As String
        Return $"{Kode,-5}{Nama,-12}{Stok,2}{Harga,10}{Subtotal,12}"
    End Function
End Class

Public Class GudangException
    Inherits Exception

    Public Sub New(pesan As String)
        MyBase.New(pesan)
    End Sub
End Class

Public Class KodeSudahAdaException
    Inherits GudangException

    Public Sub New(kode As String)
        MyBase.New($"kode {kode} sudah ada")
    End Sub
End Class

Public Class KodeTidakDikenalException
    Inherits GudangException

    Public Sub New(kode As String)
        MyBase.New($"kode {kode} tidak dikenal")
    End Sub
End Class

Public Class JumlahTidakSahException
    Inherits GudangException

    Public Sub New(jumlah As Integer)
        MyBase.New($"jumlah {jumlah} tidak sah")
    End Sub
End Class

Public Class StokTidakCukupException
    Inherits GudangException

    Public Sub New(punya As Integer, diminta As Integer)
        MyBase.New($"stok cuma {punya}, diminta {diminta}")
    End Sub
End Class

' -------------------------------------------------------------- LAYANAN
Public Class Gudang

    Private ReadOnly _isi As New Dictionary(Of String, Barang)

    Public Sub Daftar(b As Barang)
        If _isi.ContainsKey(b.Kode) Then Throw New KodeSudahAdaException(b.Kode)
        _isi(b.Kode) = b
    End Sub

    Public Function Catat(kode As String, gerak As Gerak, jumlah As Integer) As Integer
        Dim b As Barang = Nothing
        If Not _isi.TryGetValue(kode, b) Then Throw New KodeTidakDikenalException(kode)
        If jumlah <= 0 Then Throw New JumlahTidakSahException(jumlah)

        Dim baru As Integer = If(gerak = Gerak.Masuk, b.Stok + jumlah, b.Stok - jumlah)
        If baru < 0 Then Throw New StokTidakCukupException(b.Stok, jumlah)

        b.Stok = baru
        Return baru
    End Function

    Public Function Semua() As List(Of Barang)
        Return _isi.Values.OrderBy(Function(b) b.Kode, StringComparer.Ordinal).ToList()
    End Function

    Public Function NilaiPersediaan() As Long
        Return _isi.Values.Sum(Function(b) b.Subtotal)
    End Function

    Public Function StokMenipis(batas As Integer) As List(Of Barang)
        Return _isi.Values.
            Where(Function(b) b.Stok < batas).
            OrderBy(Function(b) b.Stok).
            ThenBy(Function(b) b.Kode, StringComparer.Ordinal).ToList()
    End Function

End Class

' ------------------------------------------------------------ ANTARMUKA
Module Program

    Sub Main()
        Dim gudang As New Gudang()

        gudang.Daftar(New Barang("B01", "Kabel", 10, 15000))
        gudang.Daftar(New Barang("B02", "Adaptor", 4, 85000))
        gudang.Daftar(New Barang("B03", "Mouse", 25, 120000))

        Dim langkah = {
            Tuple.Create("B01", Gerak.Masuk, 15),
            Tuple.Create("B02", Gerak.Keluar, 10),
            Tuple.Create("B03", Gerak.Keluar, 5),
            Tuple.Create("B09", Gerak.Masuk, 1),
            Tuple.Create("B03", Gerak.Keluar, 0)
        }

        For Each l In langkah
            Dim label As String = $"{l.Item2} {l.Item1} {l.Item3}"
            Try
                Console.WriteLine($"{label} -> stok {gudang.Catat(l.Item1, l.Item2, l.Item3)}")
            Catch ex As GudangException
                Console.WriteLine($"{label} -> DITOLAK: {ex.Message}")
            End Try
        Next

        Console.WriteLine("---")
        For Each b As Barang In gudang.Semua()
            Console.WriteLine(b.ToString())
        Next

        Console.WriteLine("---")
        Console.WriteLine($"nilai persediaan: {gudang.NilaiPersediaan()}")

        Dim menipis = gudang.StokMenipis(10).
            Select(Function(b) $"{b.Kode} {b.Nama} ({b.Stok})")
        Console.WriteLine($"stok menipis (<10): {String.Join(", ", menipis)}")
    End Sub

End Module"""
            },
            {
                "body": [
                    "Empat keputusan yang layak ditiru:",
                    "  1. Semua exception buatan sendiri mewarisi satu induk,",
                    "     GudangException. Antarmuka cukup menulis satu",
                    "     `Catch ex As GudangException` dan tetap dapat pesan yang tepat",
                    "     untuk tiap kasus. Error lain, yang berarti bug sungguhan, tetap",
                    "     naik dan kelihatan.",
                    "  2. `Semua()` dan `StokMenipis()` mengurutkan hasilnya sebelum",
                    "     dikembalikan. Dictionary nggak menjamin urutan, dan keluaran yang",
                    "     urutannya nggak pasti mustahil diuji.",
                    "  3. Kode, Nama, dan Harga dibuat ReadOnly. Cuma Stok yang boleh",
                    "     berubah, dan di program ini Stok cuma diubah lewat Catat, yang",
                    "     memvalidasi jumlahnya dulu. Setter Stok memang masih Public, jadi",
                    "     kalau mau dikunci rapat, akses setter itu perlu dibatasi.",
                    "  4. Gudang nggak memanggil Console sama sekali. Karena itu seluruh",
                    "     aturannya bisa diuji tanpa membaca layar.",
                    "",
                    "`If Not _isi.TryGetValue(kode, b) Then` menggabungkan pencarian dan",
                    "pemeriksaan dalam satu langkah. Kalau pakai ContainsKey dulu lalu",
                    "mengambil isinya, Dictionary mencari kunci yang sama dua kali di tabel",
                    "hash-nya, yaitu struktur yang dipakai Dictionary untuk menyimpan isi.",
                    "",
                    "Kalau kamu mau melanjutkannya:",
                    "  - Simpan ke JSON dengan System.Text.Json.",
                    "  - Pisahkan penyimpanan di balik sebuah Interface, supaya Gudang",
                    "    nggak tahu datanya disimpan di berkas, di database, atau cuma di",
                    "    memori waktu tes.",
                    "  - Tambahkan menu interaktif dan penyaringan tanggal.",
                    "  - Tulis tes MSTest atau xUnit untuk Gudang. Ini bisa langsung",
                    "    dikerjakan tanpa mengubah satu baris pun, berkat keputusan nomor 4.",
                ]
            },
            {
                "heading": "Di dunia nyata",
                "body": [
                    "Aplikasi stok sungguhan terus dapat permintaan baru dari pemiliknya.",
                    "Dengan lapisan yang terpisah dan keluarga exception yang berinduk satu,",
                    "aturan baru cukup ditambah di Gudang dan Model, dan penanganan galat di",
                    "Antarmuka nggak perlu diubah.",
                    "",
                    "Kasus kecil: pemilik minta fitur hapus barang dari daftar. Barang yang",
                    "masih punya stok nggak boleh dihapus, supaya nilai persediaannya nggak",
                    "hilang dari catatan.",
                    "",
                    "Cara memecahkannya:",
                    "  1. Tentukan lapisannya. Aturannya tinggal di Gudang, sedangkan jenis",
                    "     kegagalannya jadi exception baru di Model, turunan GudangException:",
                    "      Public Class MasihAdaStokException",
                    "          Inherits GudangException",
                    "          Public Sub New(kode As String, stok As Integer)",
                    "              MyBase.New($\"{kode} masih punya stok {stok}\")",
                    "          End Sub",
                    "      End Class",
                    "  2. Tulis `Sub Hapus(kode As String)` di Gudang. Pakai TryGetValue",
                    "     seperti di Catat, lempar KodeTidakDikenalException kalau kodenya",
                    "     nggak ada, lempar MasihAdaStokException kalau stoknya di atas 0,",
                    "     dan baru panggil _isi.Remove(kode) kalau lolos.",
                    "  3. Di Antarmuka, panggil gudang.Hapus(kode) di dalam Try yang sama.",
                    "     `Catch ex As GudangException` yang sudah ada langsung menangkap",
                    "     exception baru itu, tanpa Catch tambahan.",
                    "  4. Uji urutannya: menghapus B02 yang masih punya stok 4 ditolak,",
                    "     menghapus B09 ditolak karena kodenya nggak dikenal, dan sesudah",
                    "     stok B02 dikeluarkan sampai 0, hapusnya berhasil.",
                ]
            },
        ],
    },
]
