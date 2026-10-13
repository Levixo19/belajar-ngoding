PHP_EXERCISES = [
    {
        "title": "Latihan 1: Perkenalan Diri",
        "difficulty": "Mudah",
        "question": [
            "Buat program PHP yang menampilkan tepat tiga baris:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar PHP.",
            "  PHP 8 jauh berbeda dari PHP 5.",
        ],
        "hints": [
            "Berkas PHP dibuka dengan tag <?php",
            "Pakai echo untuk mencetak.",
            "Karakter baris baru \\n hanya berlaku di dalam kutip GANDA.",
            "Jangan tulis tag penutup ?> di berkas yang isinya hanya PHP.",
        ],
        "solution": """<?php

echo "Halo, namaku Andi!\\n";
echo "Aku sedang belajar PHP.\\n";
echo "PHP 8 jauh berbeda dari PHP 5.\\n";""",
    },
    {
        "title": "Latihan 2: Kalkulator Dua Bilangan",
        "difficulty": "Mudah",
        "question": [
            "Buat dua variabel $a = 17 dan $b = 5.",
            "Tampilkan hasil operasi dengan format persis:",
            "",
            "  17 + 5 = 22",
            "  17 - 5 = 12",
            "  17 * 5 = 85",
            "  17 / 5 = 3.4",
            "  17 % 5 = 2",
            "  intdiv(17, 5) = 3",
            "  17 ** 2 = 289",
        ],
        "hints": [
            "Di PHP, pembagian selalu menghasilkan float kalau tidak habis dibagi.",
            "Untuk pembagian bulat pakai intdiv($a, $b).",
            "Operator pangkat adalah **",
            "Variabel di dalam kutip ganda langsung diganti nilainya.",
        ],
        "solution": """<?php

$a = 17;
$b = 5;

echo "$a + $b = " . ($a + $b) . "\\n";
echo "$a - $b = " . ($a - $b) . "\\n";
echo "$a * $b = " . ($a * $b) . "\\n";
echo "$a / $b = " . ($a / $b) . "\\n";
echo "$a % $b = " . ($a % $b) . "\\n";
echo "intdiv($a, $b) = " . intdiv($a, $b) . "\\n";
echo "$a ** 2 = " . ($a ** 2) . "\\n";""",
    },
    {
        "title": "Latihan 3: Konversi Suhu",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka suhu Celsius dari input.",
            "Tampilkan konversinya ke Fahrenheit dan Kelvin.",
            "",
            "Rumus:",
            "  F = C * 9 / 5 + 32",
            "  K = C + 273.15",
            "",
            "Untuk input 25, keluaran yang diharapkan:",
            "",
            "  Celsius    : 25.00",
            "  Fahrenheit : 77.00",
            "  Kelvin     : 298.15",
        ],
        "hints": [
            "Baca satu baris dari stdin: trim(fgets(STDIN))",
            "Ubah ke float dengan (float) atau floatval().",
            "printf(\"%.2f\", $x) mencetak dua desimal.",
            "Jangan mencetak apa pun sebelum membaca input.",
        ],
        "stdin": "25\n",
        "solution": """<?php

$c = (float) trim(fgets(STDIN));

$f = $c * 9 / 5 + 32;
$k = $c + 273.15;

printf("Celsius    : %.2f\\n", $c);
printf("Fahrenheit : %.2f\\n", $f);
printf("Kelvin     : %.2f\\n", $k);""",
    },
    {
        "title": "Latihan 4: Grade & Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Baca satu angka nilai (0-100) dari input.",
            "Tampilkan grade sesuai aturan:",
            "  >= 85 : A",
            "  >= 75 : B",
            "  >= 60 : C",
            "  >= 40 : D",
            "  selain itu : E",
            "",
            "Lalu tampilkan status Lulus kalau nilai >= 75,",
            "atau Tidak Lulus kalau kurang.",
            "",
            "Untuk input 78, keluaran yang diharapkan:",
            "",
            "  Grade: B",
            "  Status: Lulus",
        ],
        "hints": [
            "Pakai match(true) { $n >= 85 => 'A', ... default => 'E' };",
            "match adalah ekspresi, jadi hasilnya langsung bisa ditugaskan.",
            "Jangan pakai switch: perbandingannya longgar dan butuh break.",
            "Untuk status, operator ternary sudah cukup.",
        ],
        "stdin_list": ["92\n", "78\n", "65\n", "45\n", "12\n"],
        "solution": """<?php

$nilai = (int) trim(fgets(STDIN));

$grade = match (true) {
    $nilai >= 85 => 'A',
    $nilai >= 75 => 'B',
    $nilai >= 60 => 'C',
    $nilai >= 40 => 'D',
    default => 'E',
};

echo "Grade: $grade\\n";
echo 'Status: ' . ($nilai >= 75 ? 'Lulus' : 'Tidak Lulus') . "\\n";""",
    },
    {
        "title": "Latihan 5: Tabel Perkalian",
        "difficulty": "Mudah",
        "question": [
            "Tampilkan tabel perkalian 1 sampai 5.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  1 x 1 =  1   1 x 2 =  2   1 x 3 =  3   1 x 4 =  4   1 x 5 =  5",
            "  2 x 1 =  2   2 x 2 =  4   2 x 3 =  6   2 x 4 =  8   2 x 5 = 10",
            "  3 x 1 =  3   3 x 2 =  6   3 x 3 =  9   3 x 4 = 12   3 x 5 = 15",
            "  4 x 1 =  4   4 x 2 =  8   4 x 3 = 12   4 x 4 = 16   4 x 5 = 20",
            "  5 x 1 =  5   5 x 2 = 10   5 x 3 = 15   5 x 4 = 20   5 x 5 = 25",
            "",
            "Tiap baris diawali dua spasi. Hasil perkaliannya rata kanan",
            "selebar 2 karakter, dan tiap sel dipisah tiga spasi.",
        ],
        "hints": [
            "Dua perulangan for bersarang.",
            "printf(\"%2d\", $n) mencetak rata kanan selebar 2.",
            "Pemisah ditulis sesudah tiap sel kecuali yang terakhir.",
            "echo \"\\n\" di akhir tiap baris luar.",
        ],
        "solution": """<?php

for ($b = 1; $b <= 5; $b++) {
    echo '  ';
    for ($k = 1; $k <= 5; $k++) {
        printf('%d x %d = %2d', $b, $k, $b * $k);
        if ($k < 5) {
            echo '   ';
        }
    }
    echo "\\n";
}""",
    },
    {
        "title": "Latihan 6: Statistik Nilai",
        "difficulty": "Menengah",
        "question": [
            "Diberikan array nilai berikut di dalam kodemu:",
            "  78, 92, 65, 88, 71, 95, 59, 83",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Data      : 78, 92, 65, 88, 71, 95, 59, 83",
            "  Terurut   : 59, 65, 71, 78, 83, 88, 92, 95",
            "  Jumlah    : 8",
            "  Total     : 631",
            "  Rata-rata : 78.88",
            "  Tertinggi : 95",
            "  Terendah  : 59",
            "  Di atas rata-rata: 92, 88, 95, 83",
        ],
        "hints": [
            "implode(', ', $arr) menggabungkan array jadi teks.",
            "sort() MENGUBAH array aslinya: salin dulu ke variabel lain.",
            "array_sum, count, max, dan min sudah tersedia.",
            "array_filter mempertahankan kunci — bungkus dengan array_values.",
        ],
        "solution": """<?php

$nilai = [78, 92, 65, 88, 71, 95, 59, 83];

$urut = $nilai;
sort($urut);

$total = array_sum($nilai);
$rata = $total / count($nilai);
$diAtas = array_values(array_filter($nilai, fn($n) => $n > $rata));

echo 'Data      : ' . implode(', ', $nilai) . "\\n";
echo 'Terurut   : ' . implode(', ', $urut) . "\\n";
echo 'Jumlah    : ' . count($nilai) . "\\n";
echo "Total     : $total\\n";
printf("Rata-rata : %.2f\\n", $rata);
echo 'Tertinggi : ' . max($nilai) . "\\n";
echo 'Terendah  : ' . min($nilai) . "\\n";
echo 'Di atas rata-rata: ' . implode(', ', $diAtas) . "\\n";""",
    },
    {
        "title": "Latihan 7: Balik Teks & Palindrom",
        "difficulty": "Menengah",
        "question": [
            "Baca satu baris teks dari input, lalu tampilkan:",
            "  Asli    : teks aslinya",
            "  Dibalik : teksnya dibalik",
            "  Huruf   : jumlah huruf tanpa spasi",
            "  Palindrom: ya / bukan (abaikan spasi dan besar-kecil huruf)",
            "",
            "Untuk input 'Kasur ini rusak', keluaran yang diharapkan:",
            "",
            "  Asli    : Kasur ini rusak",
            "  Dibalik : kasur ini rusaK",
            "  Huruf   : 13",
            "  Palindrom: ya",
        ],
        "hints": [
            "strrev() membalik string.",
            "str_replace(' ', '', $s) membuang spasi.",
            "strtolower() untuk mengabaikan besar-kecil huruf.",
            "Jangan mencetak apa pun sebelum fgets(STDIN) pertama.",
        ],
        "stdin_list": ["Kasur ini rusak\n", "Belajar PHP\n", "Ini\n"],
        "solution": """<?php

$teks = rtrim(fgets(STDIN), "\\r\\n");

$rapat = str_replace(' ', '', $teks);
$bersih = strtolower($rapat);
$palindrom = $bersih === strrev($bersih);

echo "Asli    : $teks\\n";
echo 'Dibalik : ' . strrev($teks) . "\\n";
echo 'Huruf   : ' . strlen($rapat) . "\\n";
echo 'Palindrom: ' . ($palindrom ? 'ya' : 'bukan') . "\\n";""",
    },
    {
        "title": "Latihan 8: Menghitung Frekuensi Kata",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat berikut di dalam kodemu:",
            "  \"kucing makan ikan kucing tidur ikan kucing\"",
            "",
            "Hitung berapa kali tiap kata muncul, lalu tampilkan",
            "terurut dari yang paling sering. Kalau jumlahnya sama,",
            "urutkan berdasarkan abjad.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  kucing : 3",
            "  ikan   : 2",
            "  makan  : 1",
            "  tidur  : 1",
            "  ---",
            "  Kata unik  : 4",
            "  Total kata : 7",
            "",
            "Nama kata rata kiri selebar 7 karakter.",
        ],
        "hints": [
            "explode(' ', $kalimat) memecah jadi array.",
            "array_count_values() menghitung frekuensi dalam satu panggilan.",
            "uksort/uasort bisa mengurutkan sambil mempertahankan kunci.",
            "Untuk dua kunci urutan: bandingkan jumlah dulu, lalu nama.",
        ],
        "solution": """<?php

$kalimat = 'kucing makan ikan kucing tidur ikan kucing';
$kata = explode(' ', $kalimat);

$hitung = array_count_values($kata);

uksort($hitung, function (string $a, string $b) use ($hitung): int {
    return ($hitung[$b] <=> $hitung[$a]) ?: ($a <=> $b);
});

foreach ($hitung as $k => $n) {
    printf("%-7s: %d\\n", $k, $n);
}

echo "---\\n";
echo 'Kata unik  : ' . count($hitung) . "\\n";
echo 'Total kata : ' . count($kata) . "\\n";""",
    },
    {
        "title": "Latihan 9: Class Murid dengan Validasi",
        "difficulty": "Menengah",
        "question": [
            "Buat class Murid dengan:",
            "  - property readonly $nama (string)",
            "  - property private $nilai (int) yang diisi lewat constructor",
            "  - method nilai(): int",
            "  - method setNilai(int) yang MENOLAK di luar 0..100 dengan",
            "    InvalidArgumentException",
            "  - method grade(): string -> >=85 A, >=75 B, >=60 C, sisanya D",
            "  - method __toString() berbentuk \"Andi     92 A\"",
            "    (nama rata kiri 8, nilai rata kanan 3, spasi, grade)",
            "",
            "Di bagian utama, buat tiga murid: Andi 92, Budi 78, Cici 64.",
            "Cetak ketiganya, lalu coba setNilai(150) pada Andi dan",
            "tangkap exception-nya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Andi     92 A",
            "  Budi     78 B",
            "  Cici     64 C",
            "  Ditolak: nilai di luar 0..100",
        ],
        "hints": [
            "Constructor property promotion: __construct(public readonly string $nama, ...)",
            "__toString() membuat objek bisa langsung di-echo.",
            "printf/sprintf dengan %-8s dan %3d untuk perataannya.",
            "declare(strict_types=1); di baris pertama sesudah <?php.",
        ],
        "solution": """<?php

declare(strict_types=1);

final class Murid
{
    private int $nilai;

    public function __construct(
        public readonly string $nama,
        int $nilai,
    ) {
        $this->setNilai($nilai);
    }

    public function nilai(): int
    {
        return $this->nilai;
    }

    public function setNilai(int $nilai): void
    {
        if ($nilai < 0 || $nilai > 100) {
            throw new InvalidArgumentException('nilai di luar 0..100');
        }
        $this->nilai = $nilai;
    }

    public function grade(): string
    {
        return match (true) {
            $this->nilai >= 85 => 'A',
            $this->nilai >= 75 => 'B',
            $this->nilai >= 60 => 'C',
            default => 'D',
        };
    }

    public function __toString(): string
    {
        return sprintf('%-8s%3d %s', $this->nama, $this->nilai, $this->grade());
    }
}

$kelas = [
    new Murid('Andi', 92),
    new Murid('Budi', 78),
    new Murid('Cici', 64),
];

foreach ($kelas as $m) {
    echo $m . "\\n";
}

try {
    $kelas[0]->setNilai(150);
} catch (InvalidArgumentException $e) {
    echo 'Ditolak: ' . $e->getMessage() . "\\n";
}""",
    },
    {
        "title": "Latihan 10: Interface, Abstract & Trait",
        "difficulty": "Lanjut",
        "question": [
            "Buat interface Bangun dengan method luas(): float dan nama(): string.",
            "Buat trait BisaDiringkas dengan method ringkas(): string yang",
            "menghasilkan sprintf('%-16s%8.2f', nama, luas).",
            "Buat abstract class BangunDasar yang mengimplementasi Bangun,",
            "memakai trait itu, dan menyimpan namanya.",
            "",
            "Turunkan Persegi(sisi), Lingkaran(jari), dan",
            "PersegiPanjang(panjang, lebar). Pakai PI = 3.14159.",
            "",
            "Masukkan Persegi(4), Lingkaran(3), PersegiPanjang(6, 3) ke",
            "dalam satu array, telusuri sekali, lalu cetak totalnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Persegi            16.00",
            "  Lingkaran          28.27",
            "  PersegiPanjang     18.00",
            "  TOTAL              62.27",
        ],
        "hints": [
            "Trait disisipkan dengan `use NamaTrait;` di dalam badan class.",
            "parent::__construct('Persegi') memanggil constructor induk —",
            "PHP tidak memanggilnya otomatis.",
            "Constructor turunan boleh memakai property promotion sekaligus.",
            "Konstanta class diakses dengan self::PI.",
        ],
        "solution": """<?php

declare(strict_types=1);

interface Bangun
{
    public function luas(): float;
    public function nama(): string;
}

trait BisaDiringkas
{
    public function ringkas(): string
    {
        return sprintf('%-16s%8.2f', $this->nama(), $this->luas());
    }
}

abstract class BangunDasar implements Bangun
{
    use BisaDiringkas;

    public function __construct(private string $nama) {}

    public function nama(): string
    {
        return $this->nama;
    }
}

final class Persegi extends BangunDasar
{
    public function __construct(private float $sisi)
    {
        parent::__construct('Persegi');
    }

    public function luas(): float
    {
        return $this->sisi ** 2;
    }
}

final class Lingkaran extends BangunDasar
{
    private const PI = 3.14159;

    public function __construct(private float $jari)
    {
        parent::__construct('Lingkaran');
    }

    public function luas(): float
    {
        return self::PI * $this->jari ** 2;
    }
}

final class PersegiPanjang extends BangunDasar
{
    public function __construct(
        private float $panjang,
        private float $lebar,
    ) {
        parent::__construct('PersegiPanjang');
    }

    public function luas(): float
    {
        return $this->panjang * $this->lebar;
    }
}

$semua = [
    new Persegi(4),
    new Lingkaran(3),
    new PersegiPanjang(6, 3),
];

$total = 0.0;
foreach ($semua as $b) {
    echo $b->ringkas() . "\\n";
    $total += $b->luas();
}

printf("%-16s%8.2f\\n", 'TOTAL', $total);""",
    },
    {
        "title": "Latihan 11: Enum Status Dokumen",
        "difficulty": "Lanjut",
        "question": [
            "Buat backed enum Status: string dengan kasus:",
            "  Draf='draf', Ditinjau='ditinjau', Disetujui='disetujui',",
            "  Ditolak='ditolak', Terbit='terbit'",
            "",
            "Tambahkan tiga method:",
            "  label(): string        -> Konsep, Sedang ditinjau, Disetujui,",
            "                            Ditolak, Sudah terbit",
            "  bisaDisunting(): bool  -> true hanya untuk Draf dan Ditolak",
            "  berikutnya(): array    -> Draf->[Ditinjau],",
            "                            Ditinjau->[Disetujui, Ditolak],",
            "                            Disetujui->[Terbit],",
            "                            Ditolak->[Draf], Terbit->[]",
            "",
            "Telusuri Status::cases() dan cetak tabelnya, lalu uji",
            "Status::from('terbit') dan Status::tryFrom('tidak-ada').",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Draf        draf      Konsep            ya     Ditinjau",
            "  Ditinjau    ditinjau  Sedang ditinjau   tidak  Disetujui, Ditolak",
            "  Disetujui   disetujui Disetujui         tidak  Terbit",
            "  Ditolak     ditolak   Ditolak           ya     Draf",
            "  Terbit      terbit    Sudah terbit      tidak  -",
            "  ---",
            "  from('terbit')       : Terbit",
            "  tryFrom('tidak-ada') : null",
            "",
            "Kolom: name rata kiri 12, value rata kiri 10, label rata kiri 18,",
            "sunting rata kiri 7, lalu daftar berikutnya.",
        ],
        "hints": [
            "Backed enum ditulis: enum Status: string { case Draf = 'draf'; ... }",
            "Method di dalam enum memakai match($this) TANPA default supaya "
            "varian baru yang belum ditangani langsung ketahuan.",
            "$s->name memberi nama kasusnya, $s->value memberi nilainya.",
            "tryFrom mengembalikan null, bukan melempar — cetak dengan ?? 'null'.",
        ],
        "solution": """<?php

declare(strict_types=1);

enum Status: string
{
    case Draf = 'draf';
    case Ditinjau = 'ditinjau';
    case Disetujui = 'disetujui';
    case Ditolak = 'ditolak';
    case Terbit = 'terbit';

    public function label(): string
    {
        return match ($this) {
            Status::Draf => 'Konsep',
            Status::Ditinjau => 'Sedang ditinjau',
            Status::Disetujui => 'Disetujui',
            Status::Ditolak => 'Ditolak',
            Status::Terbit => 'Sudah terbit',
        };
    }

    public function bisaDisunting(): bool
    {
        return match ($this) {
            Status::Draf, Status::Ditolak => true,
            default => false,
        };
    }

    /** @return Status[] */
    public function berikutnya(): array
    {
        return match ($this) {
            Status::Draf => [Status::Ditinjau],
            Status::Ditinjau => [Status::Disetujui, Status::Ditolak],
            Status::Disetujui => [Status::Terbit],
            Status::Ditolak => [Status::Draf],
            Status::Terbit => [],
        };
    }
}

foreach (Status::cases() as $s) {
    $lanjut = array_map(fn(Status $x): string => $x->name, $s->berikutnya());
    printf(
        "%-12s%-10s%-18s%-7s%s\\n",
        $s->name,
        $s->value,
        $s->label(),
        $s->bisaDisunting() ? 'ya' : 'tidak',
        $lanjut === [] ? '-' : implode(', ', $lanjut),
    );
}

echo "---\\n";
printf("%-21s: %s\\n", "from('terbit')", Status::from('terbit')->name);
printf("%-21s: %s\\n", "tryFrom('tidak-ada')", Status::tryFrom('tidak-ada')?->name ?? 'null');""",
    },
    {
        "title": "Latihan 12: Exception Berantai",
        "difficulty": "Lanjut",
        "question": [
            "Buat class SaldoKurangException extends RuntimeException dengan",
            "property readonly $kurang (int) dan pesan \"saldo kurang <n>\".",
            "",
            "Buat class Dompet dengan saldo awal dan method bayar(int):",
            "  - jumlah <= 0 -> InvalidArgumentException \"jumlah <n> tidak sah\"",
            "  - jumlah > saldo -> SaldoKurangException",
            "  - selain itu saldo berkurang",
            "",
            "Mulai dengan saldo 50000 lalu bayar berurutan:",
            "  20000, -5, 100000, 30000",
            "",
            "Lalu buat fungsi bacaKonfigurasi(string $json): array yang",
            "menangkap JsonException dan melemparkan ulang sebagai",
            "RuntimeException('konfigurasi tidak bisa dibaca', 0, $e).",
            "Uji dengan '{rusak}' lalu cetak pesan luar dan dalamnya.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  bayar   20000 -> sisa 30000",
            "  bayar      -5 -> DITOLAK: jumlah -5 tidak sah",
            "  bayar  100000 -> GAGAL, kurang 70000",
            "  bayar   30000 -> sisa 0",
            "  ---",
            "  luar  : konfigurasi tidak bisa dibaca",
            "  dalam : Syntax error",
            "",
            "Angka tagihan dicetak rata kanan selebar 7.",
        ],
        "hints": [
            "json_decode dengan flag JSON_THROW_ON_ERROR melempar JsonException.",
            "Argumen KETIGA new Exception(...) adalah exception sebelumnya.",
            "getPrevious() membacanya kembali; pakai ?-> supaya aman kalau null.",
            "Tangkap yang PALING SPESIFIK lebih dulu.",
        ],
        "solution": """<?php

declare(strict_types=1);

final class SaldoKurangException extends RuntimeException
{
    public function __construct(public readonly int $kurang)
    {
        parent::__construct("saldo kurang $kurang");
    }
}

final class Dompet
{
    public function __construct(private int $saldo) {}

    public function saldo(): int
    {
        return $this->saldo;
    }

    public function bayar(int $jumlah): void
    {
        if ($jumlah <= 0) {
            throw new InvalidArgumentException("jumlah $jumlah tidak sah");
        }
        if ($jumlah > $this->saldo) {
            throw new SaldoKurangException($jumlah - $this->saldo);
        }
        $this->saldo -= $jumlah;
    }
}

function bacaKonfigurasi(string $json): array
{
    try {
        return json_decode($json, true, 512, JSON_THROW_ON_ERROR);
    } catch (JsonException $e) {
        throw new RuntimeException('konfigurasi tidak bisa dibaca', 0, $e);
    }
}

$d = new Dompet(50000);

foreach ([20000, -5, 100000, 30000] as $tagihan) {
    try {
        $d->bayar($tagihan);
        printf("bayar %7d -> sisa %d\\n", $tagihan, $d->saldo());
    } catch (SaldoKurangException $e) {
        printf("bayar %7d -> GAGAL, kurang %d\\n", $tagihan, $e->kurang);
    } catch (InvalidArgumentException $e) {
        printf("bayar %7d -> DITOLAK: %s\\n", $tagihan, $e->getMessage());
    }
}

echo "---\\n";

try {
    bacaKonfigurasi('{rusak}');
} catch (RuntimeException $e) {
    echo 'luar  : ' . $e->getMessage() . "\\n";
    echo 'dalam : ' . ($e->getPrevious()?->getMessage() ?? '-') . "\\n";
}""",
    },
    {
        "title": "Latihan 13: Laporan Penjualan",
        "difficulty": "Lanjut",
        "question": [
            "Diberikan daftar transaksi berikut (barang, kategori, jumlah, harga):",
            "  Kopi  Minuman  3  25000",
            "  Teh   Minuman  5  15000",
            "  Roti  Makanan  2  20000",
            "  Nasi  Makanan  4  30000",
            "  Jus   Minuman  1  35000",
            "",
            "Tampilkan semua transaksi bersubtotal, terurut subtotal MENURUN.",
            "Kalau subtotalnya sama, urutkan nama barang MENAIK. Lalu total,",
            "rekap per kategori (terurut abjad), dan barang termahal.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Nasi       Makanan     4 x  30000 =   120000",
            "  Kopi       Minuman     3 x  25000 =    75000",
            "  Teh        Minuman     5 x  15000 =    75000",
            "  Roti       Makanan     2 x  20000 =    40000",
            "  Jus        Minuman     1 x  35000 =    35000",
            "  ---",
            "  Total     : 345000",
            "  Makanan   : 160000 (2 transaksi)",
            "  Minuman   : 185000 (3 transaksi)",
            "  Termahal  : Nasi",
            "",
            "Kolom: barang rata kiri 11, kategori rata kiri 11, jumlah rata",
            "kanan 2, harga rata kanan 6, subtotal rata kanan 8.",
        ],
        "hints": [
            "Hitung subtotal sekali lalu simpan ke tiap baris dengan array_map.",
            "usort dengan operator spaceship: ($b['sub'] <=> $a['sub']) ?: ...",
            "Untuk rekap, kumpulkan ke array berkunci kategori lalu ksort.",
            "array_column + array_search bisa mencari yang subtotalnya tertinggi.",
        ],
        "solution": """<?php

declare(strict_types=1);

$data = [
    ['barang' => 'Kopi', 'kategori' => 'Minuman', 'jumlah' => 3, 'harga' => 25000],
    ['barang' => 'Teh',  'kategori' => 'Minuman', 'jumlah' => 5, 'harga' => 15000],
    ['barang' => 'Roti', 'kategori' => 'Makanan', 'jumlah' => 2, 'harga' => 20000],
    ['barang' => 'Nasi', 'kategori' => 'Makanan', 'jumlah' => 4, 'harga' => 30000],
    ['barang' => 'Jus',  'kategori' => 'Minuman', 'jumlah' => 1, 'harga' => 35000],
];

$data = array_map(
    fn(array $t): array => $t + ['sub' => $t['jumlah'] * $t['harga']],
    $data,
);

$baris = $data;
usort($baris, fn(array $a, array $b): int =>
    ($b['sub'] <=> $a['sub']) ?: ($a['barang'] <=> $b['barang']));

foreach ($baris as $t) {
    printf(
        "%-11s%-11s%2d x %6d = %8d\\n",
        $t['barang'], $t['kategori'], $t['jumlah'], $t['harga'], $t['sub'],
    );
}

echo "---\\n";
printf("%-10s: %d\\n", 'Total', array_sum(array_column($data, 'sub')));

$rekap = [];
foreach ($data as $t) {
    $rekap[$t['kategori']]['total'] = ($rekap[$t['kategori']]['total'] ?? 0) + $t['sub'];
    $rekap[$t['kategori']]['n'] = ($rekap[$t['kategori']]['n'] ?? 0) + 1;
}
ksort($rekap);

foreach ($rekap as $kategori => $r) {
    printf("%-10s: %d (%d transaksi)\\n", $kategori, $r['total'], $r['n']);
}

$sub = array_column($data, 'sub');
$termahal = $data[array_search(max($sub), $sub, true)];
printf("%-10s: %s\\n", 'Termahal', $termahal['barang']);""",
    },
    {
        "title": "Latihan 14: Validasi Masukan yang Aman",
        "difficulty": "Sulit",
        "question": [
            "Buat fungsi validasi(array $data): array yang memeriksa",
            "sebuah 'form' dan mengembalikan daftar galat per field:",
            "",
            "  nama  : wajib, maksimal 20 karakter",
            "  umur  : wajib, bilangan bulat 1..120",
            "  email : wajib, harus berformat email yang sah",
            "",
            "Buat juga fungsi e(?string): string yang melarikan teks untuk",
            "HTML dengan htmlspecialchars(ENT_QUOTES, 'UTF-8').",
            "",
            "Uji dengan empat data:",
            "  1. nama='Andi', umur='20', email='andi@contoh.id'",
            "  2. nama='', umur='abc', email='bukan-email'",
            "  3. nama='<script>alert(1)</script>', umur='150', email='a@b.id'",
            "  4. nama='Budi', umur='0', email=''",
            "",
            "Cetak hasilnya. Untuk data yang sah, tampilkan namanya SETELAH",
            "dilarikan.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  data 1: SAH -> Andi",
            "  data 2: nama=wajib diisi | umur=harus 1..120 | email=format tidak sah",
            "  data 3: nama=maksimal 20 karakter | umur=harus 1..120",
            "  data 4: umur=harus 1..120 | email=wajib diisi",
            "  ---",
            "  nama data 3 sesudah dilarikan:",
            "  &lt;script&gt;alert(1)&lt;/script&gt;",
        ],
        "hints": [
            "filter_var($x, FILTER_VALIDATE_INT, ['options' => ['min_range'=>1,",
            "'max_range'=>120]]) mengembalikan false kalau di luar rentang.",
            "filter_var($x, FILTER_VALIDATE_EMAIL) untuk email.",
            "mb_strlen menghitung KARAKTER, bukan byte — yang benar untuk "
            "membatasi panjang masukan pengguna.",
            "Gabungkan galat dengan implode(' | ', ...).",
        ],
        "solution": """<?php

declare(strict_types=1);

function e(?string $s): string
{
    return htmlspecialchars($s ?? '', ENT_QUOTES, 'UTF-8');
}

function validasi(array $data): array
{
    $galat = [];

    $nama = trim((string) ($data['nama'] ?? ''));
    if ($nama === '') {
        $galat['nama'] = 'wajib diisi';
    } elseif (mb_strlen($nama) > 20) {
        $galat['nama'] = 'maksimal 20 karakter';
    }

    $umurMentah = trim((string) ($data['umur'] ?? ''));
    if ($umurMentah === '') {
        $galat['umur'] = 'wajib diisi';
    } else {
        $umur = filter_var($umurMentah, FILTER_VALIDATE_INT, [
            'options' => ['min_range' => 1, 'max_range' => 120],
        ]);
        if ($umur === false) {
            $galat['umur'] = 'harus 1..120';
        }
    }

    $email = trim((string) ($data['email'] ?? ''));
    if ($email === '') {
        $galat['email'] = 'wajib diisi';
    } elseif (filter_var($email, FILTER_VALIDATE_EMAIL) === false) {
        $galat['email'] = 'format tidak sah';
    }

    return $galat;
}

$semua = [
    ['nama' => 'Andi', 'umur' => '20', 'email' => 'andi@contoh.id'],
    ['nama' => '', 'umur' => 'abc', 'email' => 'bukan-email'],
    ['nama' => '<script>alert(1)</script>', 'umur' => '150', 'email' => 'a@b.id'],
    ['nama' => 'Budi', 'umur' => '0', 'email' => ''],
];

foreach ($semua as $i => $data) {
    $galat = validasi($data);
    $nomor = $i + 1;

    if ($galat === []) {
        echo "data $nomor: SAH -> " . e($data['nama']) . "\\n";
        continue;
    }

    $pesan = [];
    foreach ($galat as $field => $isi) {
        $pesan[] = "$field=$isi";
    }
    echo "data $nomor: " . implode(' | ', $pesan) . "\\n";
}

echo "---\\n";
echo "nama data 3 sesudah dilarikan:\\n";
echo e($semua[2]['nama']) . "\\n";""",
    },
    {
        "title": "Latihan 15: PDO & Prepared Statement",
        "difficulty": "Sulit",
        "question": [
            "Pakai PDO dengan SQLite di memori ('sqlite::memory:').",
            "Setel ERRMODE_EXCEPTION dan DEFAULT_FETCH_MODE => FETCH_ASSOC.",
            "",
            "Buat tabel murid(id INTEGER PRIMARY KEY, nama TEXT NOT NULL,",
            "kelas TEXT NOT NULL, nilai INTEGER NOT NULL).",
            "",
            "Sisipkan dengan PREPARED STATEMENT:",
            "  Andi A 88, Budi B 72, Cici A 95, Dedi B 64",
            "",
            "Lalu tampilkan:",
            "  1. Murid dengan nilai >= 75, terurut nilai menurun",
            "  2. Rekap per kelas: jumlah dan rata-rata, terurut kelas",
            "  3. Total murid",
            "  4. Buktikan prepared statement menahan injeksi dengan mencari",
            "     nama berisi  ' OR '1'='1  -- hasilnya harus 0 baris",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Lulus (>= 75):",
            "    Cici   A  95",
            "    Andi   A  88",
            "  Rekap per kelas:",
            "    Kelas A: 2 murid, rata-rata 91.5",
            "    Kelas B: 2 murid, rata-rata 68.0",
            "  Total murid: 4",
            "  Cari nama \" OR \"1\"=\"1 -> 0 baris",
        ],
        "hints": [
            "PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION wajib: tanpa itu "
            "query yang gagal cuma mengembalikan false.",
            "$pdo->prepare(...)->execute([...]) lalu fetchAll().",
            "fetchColumn() mengambil satu nilai saja.",
            "Nilai yang dikirim lewat execute() TIDAK PERNAH bisa jadi perintah.",
        ],
        "solution": """<?php

declare(strict_types=1);

$pdo = new PDO('sqlite::memory:', null, null, [
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
]);

$pdo->exec('
    CREATE TABLE murid (
        id    INTEGER PRIMARY KEY,
        nama  TEXT    NOT NULL,
        kelas TEXT    NOT NULL,
        nilai INTEGER NOT NULL
    )
');

$sisip = $pdo->prepare(
    'INSERT INTO murid (nama, kelas, nilai) VALUES (:nama, :kelas, :nilai)'
);

foreach ([
    ['Andi', 'A', 88],
    ['Budi', 'B', 72],
    ['Cici', 'A', 95],
    ['Dedi', 'B', 64],
] as [$nama, $kelas, $nilai]) {
    $sisip->execute(['nama' => $nama, 'kelas' => $kelas, 'nilai' => $nilai]);
}

$cari = $pdo->prepare(
    'SELECT nama, kelas, nilai FROM murid WHERE nilai >= ? ORDER BY nilai DESC'
);
$cari->execute([75]);

echo "Lulus (>= 75):\\n";
foreach ($cari->fetchAll() as $m) {
    printf("  %-6s %s %3d\\n", $m['nama'], $m['kelas'], $m['nilai']);
}

echo "Rekap per kelas:\\n";
$rekap = $pdo->query(
    'SELECT kelas, COUNT(*) AS jumlah, AVG(nilai) AS rata
     FROM murid GROUP BY kelas ORDER BY kelas'
);
foreach ($rekap as $r) {
    printf("  Kelas %s: %d murid, rata-rata %.1f\\n",
           $r['kelas'], $r['jumlah'], $r['rata']);
}

echo 'Total murid: ' . $pdo->query('SELECT COUNT(*) FROM murid')->fetchColumn() . "\\n";

$jahat = "' OR '1'='1";
$uji = $pdo->prepare('SELECT COUNT(*) FROM murid WHERE nama = ?');
$uji->execute([$jahat]);
printf("Cari nama %s -> %d baris\\n", str_replace("'", '"', $jahat), $uji->fetchColumn());""",
    },
    {
        "title": "Latihan 16: Proyek Akhir - Inventaris Gudang",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Bangun sistem inventaris yang MEMISAHKAN tiga lapisan:",
            "model (data), layanan (aturan), dan antarmuka (cetak).",
            "",
            "MODEL",
            "  final class Barang dengan readonly kode, nama, dan harga,",
            "  serta stok yang bisa berubah.",
            "  enum Gerak: string { Masuk='Masuk'; Keluar='Keluar'; }",
            "  Exception: KodeSudahAdaException, KodeTidakDikenalException,",
            "  JumlahTidakSahException, StokTidakCukupException",
            "  (semuanya turunan RuntimeException, dengan pesan sendiri).",
            "",
            "LAYANAN  final class Gudang",
            "  - daftar(Barang): void  -> tolak kode kembar",
            "  - catat(string $kode, Gerak, int $jumlah): int",
            "      urutan periksa: kode dulu, lalu jumlah, baru kecukupan stok",
            "  - semua(): array  terurut kode",
            "  - nilaiPersediaan(): int",
            "  - stokMenipis(int $batas): array  terurut stok naik",
            "  Gudang TIDAK BOLEH memakai echo atau printf sama sekali.",
            "",
            "ANTARMUKA",
            "  Daftarkan B01 Kabel 10 15000, B02 Adaptor 4 85000,",
            "            B03 Mouse 25 120000",
            "  Jalankan: Masuk B01 15, Keluar B02 10, Keluar B03 5,",
            "            Masuk B09 1, Keluar B03 0",
            "  Lalu cetak tabel, nilai persediaan, dan stok menipis <10.",
            "",
            "Keluaran yang diharapkan:",
            "",
            "  Masuk B01 15 -> stok 25",
            "  Keluar B02 10 -> DITOLAK: stok cuma 4, diminta 10",
            "  Keluar B03 5 -> stok 20",
            "  Masuk B09 1 -> DITOLAK: kode B09 tidak dikenal",
            "  Keluar B03 0 -> DITOLAK: jumlah 0 tidak sah",
            "  ---",
            "  B01  Kabel       25     15000      375000",
            "  B02  Adaptor      4     85000      340000",
            "  B03  Mouse       20    120000     2400000",
            "  ---",
            "  nilai persediaan: 3115000",
            "  stok menipis (<10): B02 Adaptor (4)",
            "",
            "Kolom tabel: kode rata kiri 5, nama rata kiri 12, stok rata",
            "kanan 2, harga rata kanan 10, subtotal rata kanan 12.",
        ],
        "hints": [
            "Simpan barang di array berkunci kode; isset() memeriksa kode kembar.",
            "usort pada array_values untuk mengurutkan hasil semua().",
            "Satu try/catch per langkah di antarmuka membuat outputnya rapi;",
            "tangkap RuntimeException lalu cetak getMessage().",
            "Gudang yang tidak pernah mencetak bisa diuji tanpa membaca layar — "
            "itu seluruh gunanya pemisahan ini.",
        ],
        "solution": """<?php

declare(strict_types=1);

// ---------------------------------------------------------------- MODEL
final class Barang
{
    public function __construct(
        public readonly string $kode,
        public readonly string $nama,
        public int $stok,
        public readonly int $harga,
    ) {}

    public function subtotal(): int
    {
        return $this->stok * $this->harga;
    }
}

enum Gerak: string
{
    case Masuk = 'Masuk';
    case Keluar = 'Keluar';
}

final class KodeSudahAdaException extends RuntimeException
{
    public function __construct(string $kode)
    {
        parent::__construct("kode $kode sudah ada");
    }
}

final class KodeTidakDikenalException extends RuntimeException
{
    public function __construct(string $kode)
    {
        parent::__construct("kode $kode tidak dikenal");
    }
}

final class JumlahTidakSahException extends RuntimeException
{
    public function __construct(int $jumlah)
    {
        parent::__construct("jumlah $jumlah tidak sah");
    }
}

final class StokTidakCukupException extends RuntimeException
{
    public function __construct(int $punya, int $diminta)
    {
        parent::__construct("stok cuma $punya, diminta $diminta");
    }
}

// -------------------------------------------------------------- LAYANAN
final class Gudang
{
    /** @var array<string, Barang> */
    private array $isi = [];

    public function daftar(Barang $b): void
    {
        if (isset($this->isi[$b->kode])) {
            throw new KodeSudahAdaException($b->kode);
        }
        $this->isi[$b->kode] = $b;
    }

    public function catat(string $kode, Gerak $gerak, int $jumlah): int
    {
        if (!isset($this->isi[$kode])) {
            throw new KodeTidakDikenalException($kode);
        }
        if ($jumlah <= 0) {
            throw new JumlahTidakSahException($jumlah);
        }

        $b = $this->isi[$kode];
        $baru = $gerak === Gerak::Masuk ? $b->stok + $jumlah : $b->stok - $jumlah;

        if ($baru < 0) {
            throw new StokTidakCukupException($b->stok, $jumlah);
        }

        $b->stok = $baru;
        return $baru;
    }

    /** @return Barang[] */
    public function semua(): array
    {
        $v = array_values($this->isi);
        usort($v, fn(Barang $a, Barang $b): int => $a->kode <=> $b->kode);
        return $v;
    }

    public function nilaiPersediaan(): int
    {
        $total = 0;
        foreach ($this->isi as $b) {
            $total += $b->subtotal();
        }
        return $total;
    }

    /** @return Barang[] */
    public function stokMenipis(int $batas): array
    {
        $v = array_values(array_filter($this->isi, fn(Barang $b): bool => $b->stok < $batas));
        usort($v, fn(Barang $a, Barang $b): int =>
            ($a->stok <=> $b->stok) ?: ($a->kode <=> $b->kode));
        return $v;
    }
}

// ------------------------------------------------------------ ANTARMUKA
$g = new Gudang();

$g->daftar(new Barang('B01', 'Kabel', 10, 15000));
$g->daftar(new Barang('B02', 'Adaptor', 4, 85000));
$g->daftar(new Barang('B03', 'Mouse', 25, 120000));

$langkah = [
    ['B01', Gerak::Masuk, 15],
    ['B02', Gerak::Keluar, 10],
    ['B03', Gerak::Keluar, 5],
    ['B09', Gerak::Masuk, 1],
    ['B03', Gerak::Keluar, 0],
];

foreach ($langkah as [$kode, $gerak, $n]) {
    $label = "{$gerak->value} $kode $n";
    try {
        $stok = $g->catat($kode, $gerak, $n);
        echo "$label -> stok $stok\\n";
    } catch (RuntimeException $e) {
        echo "$label -> DITOLAK: " . $e->getMessage() . "\\n";
    }
}

echo "---\\n";
foreach ($g->semua() as $b) {
    printf("%-5s%-12s%2d%10d%12d\\n",
           $b->kode, $b->nama, $b->stok, $b->harga, $b->subtotal());
}

echo "---\\n";
echo 'nilai persediaan: ' . $g->nilaiPersediaan() . "\\n";

$menipis = array_map(
    fn(Barang $b): string => "{$b->kode} {$b->nama} ({$b->stok})",
    $g->stokMenipis(10),
);
echo 'stok menipis (<10): ' . implode(', ', $menipis) . "\\n";""",
    },
]
