JAVASCRIPT_EXERCISES = [
    {
        "title": "Latihan 1: Halo, Nama!",
        "difficulty": "Mudah",
        "question": [
            "Buat program yang menampilkan:",
            "  Halo, namaku Andi!",
            "  Aku sedang belajar JavaScript.",
            "",
            "Tulis PERSIS seperti di atas, termasuk nama Andi -- penilaian",
            "membandingkan outputmu huruf demi huruf.",
        ],
        "hints": [
            "Gunakan console.log() untuk tiap baris.",
            "Teks diapit tanda kutip ', \", atau backtick `.",
        ],
        "solution": """console.log("Halo, namaku Andi!");
console.log("Aku sedang belajar JavaScript.");""",
    },
    {
        "title": "Latihan 2: Kalkulator Sederhana",
        "difficulty": "Mudah",
        "question": [
            "Buat program dengan 2 variabel (misal 15 dan 4).",
            "Tampilkan hasil: penjumlahan, pengurangan, perkalian,",
            "pembagian, dan sisa bagi menggunakan template literal.",
        ],
        "hints": [
            "const a = 15; const b = 4;",
            "Gunakan template literal `${a} + ${b} = ${a+b}`.",
        ],
        "solution": """const a = 15;
const b = 4;

console.log(`${a} + ${b} = ${a + b}`);
console.log(`${a} - ${b} = ${a - b}`);
console.log(`${a} * ${b} = ${a * b}`);
console.log(`${a} / ${b} = ${a / b}`);
console.log(`${a} % ${b} = ${a % b}`);""",
    },
    {
        "title": "Latihan 3: Cek Kelulusan",
        "difficulty": "Mudah",
        "question": [
            "Buat fungsi cekKelulusan(nilai) yang mengembalikan 'Lulus'",
            "jika nilai >= 75, selain itu 'Tidak Lulus'.",
            "Uji dengan beberapa nilai berbeda.",
        ],
        "hints": [
            "function cekKelulusan(nilai) { ... return ...; }",
            "Bisa pakai if-else atau ternary satu baris.",
        ],
        "solution": """function cekKelulusan(nilai) {
    return nilai >= 75 ? "Lulus" : "Tidak Lulus";
}

console.log(cekKelulusan(80));   // Lulus
console.log(cekKelulusan(60));   // Tidak Lulus""",
    },
    {
        "title": "Latihan 4: Deret Angka Genap",
        "difficulty": "Menengah",
        "question": [
            "Tampilkan semua bilangan genap dari 1 sampai 20",
            "beserta total jumlahnya menggunakan array method.",
        ],
        "hints": [
            "Buat array dari 1-20 dengan Array.from({length:20}, (_, i) => i+1)",
            "Gunakan .filter() untuk ambil genap, .reduce() untuk total.",
        ],
        "solution": """const angka = Array.from({ length: 20 }, (_, i) => i + 1);
const genap = angka.filter(n => n % 2 === 0);
const total = genap.reduce((acc, n) => acc + n, 0);

console.log(genap.join(" "));
console.log(`Total: ${total}`);""",
    },
    {
        "title": "Latihan 5: Pola Bintang",
        "difficulty": "Menengah",
        "question": [
            "Buat pola segitiga siku-siku dari bintang:",
            "  *",
            "  **",
            "  ***",
            "  ****",
            "  *****",
        ],
        "hints": [
            "Gunakan for loop dan method String.repeat().",
            "\"*\".repeat(i) mengulang karakter * sebanyak i kali.",
        ],
        "solution": """for (let i = 1; i <= 5; i++) {
    console.log("*".repeat(i));
}""",
    },
    {
        "title": "Latihan 6: Statistik Nilai dengan Array",
        "difficulty": "Menengah",
        "question": [
            "Diberikan array nilai = [80, 90, 75, 85, 60, 95, 70].",
            "Tampilkan: nilai terbesar, terkecil, rata-rata, dan",
            "array yang sudah diurutkan dari terbesar ke terkecil.",
        ],
        "hints": [
            "Math.max(...nilai) dan Math.min(...nilai) dengan spread operator.",
            "reduce() untuk total, lalu bagi length untuk rata-rata.",
            "[...nilai].sort((a,b) => b-a) agar tidak mengubah array asli.",
        ],
        "solution": """const nilai = [80, 90, 75, 85, 60, 95, 70];

const terbesar = Math.max(...nilai);
const terkecil = Math.min(...nilai);
const rata = nilai.reduce((a, b) => a + b, 0) / nilai.length;
const urutMenurun = [...nilai].sort((a, b) => b - a);

console.log(`Terbesar: ${terbesar}`);
console.log(`Terkecil: ${terkecil}`);
console.log(`Rata-rata: ${rata.toFixed(2)}`);
console.log(`Urutan menurun: ${urutMenurun}`);""",
    },
    {
        "title": "Latihan 7: Fungsi Hitung Luas",
        "difficulty": "Menengah",
        "question": [
            "Buat 3 fungsi (arrow function):",
            "  1. luasPersegi(sisi)          -> sisi * sisi",
            "  2. luasPersegiPanjang(p, l)   -> p * l",
            "  3. luasLingkaran(r)           -> Math.PI * r * r",
            "Panggil ketiganya dan tampilkan hasilnya.",
        ],
        "hints": [
            "const luasPersegi = (sisi) => sisi * sisi;",
            "Math.PI sudah tersedia bawaan JavaScript.",
        ],
        "solution": """const luasPersegi = (sisi) => sisi * sisi;
const luasPersegiPanjang = (p, l) => p * l;
const luasLingkaran = (r) => Math.PI * r * r;

console.log(`Persegi (5): ${luasPersegi(5)}`);
console.log(`Persegi Panjang (4x6): ${luasPersegiPanjang(4, 6)}`);
console.log(`Lingkaran (r=7): ${luasLingkaran(7).toFixed(2)}`);""",
    },
    {
        "title": "Latihan 8: Manipulasi String",
        "difficulty": "Menengah",
        "question": [
            "Diberikan kalimat = '  Belajar JavaScript itu Menyenangkan  '.",
            "Tampilkan:",
            "  1. Kalimat tanpa spasi di ujung.",
            "  2. Kalimat dalam huruf besar semua.",
            "  3. Jumlah kata dalam kalimat.",
            "  4. Kalimat dengan kata 'JavaScript' diganti 'Coding'.",
        ],
        "hints": [
            "trim() untuk buang spasi ujung.",
            "split(' ') memecah jadi array kata, .length untuk menghitung.",
            "replace(lama, baru) untuk mengganti kata.",
        ],
        "solution": """const kalimat = "  Belajar JavaScript itu Menyenangkan  ";

const bersih = kalimat.trim();
console.log(`1. '${bersih}'`);
console.log(`2. ${bersih.toUpperCase()}`);
console.log(`3. Jumlah kata: ${bersih.split(" ").length}`);
console.log(`4. ${bersih.replace("JavaScript", "Coding")}`);""",
    },
    {
        "title": "Latihan 9: Object Buku Kontak",
        "difficulty": "Menengah",
        "question": [
            "Buat object kontak kosong. Tambahkan 3 kontak",
            "(nama sebagai key, nomor telepon sebagai value).",
            "Tampilkan semua kontak dengan format 'nama: nomor'.",
            "Cari satu kontak yang mungkin tidak ada dengan aman",
            "menggunakan optional chaining atau pengecekan 'in'.",
        ],
        "hints": [
            "const kontak = {};",
            "kontak['Andi'] = '0812xxxx';",
            "for (const [nama, no] of Object.entries(kontak)) {...}",
            "'Zaki' in kontak untuk cek keberadaan key.",
        ],
        "solution": """const kontak = {};
kontak["Andi"] = "0812-1111-1111";
kontak["Budi"] = "0813-2222-2222";
kontak["Citra"] = "0812-3333-3333";

for (const [nama, nomor] of Object.entries(kontak)) {
    console.log(`${nama}: ${nomor}`);
}

const hasil = "Zaki" in kontak ? kontak["Zaki"] : "Kontak tidak ditemukan";
console.log(hasil);""",
    },
    {
        "title": "Latihan 10: Filter & Transform dengan Method Chaining",
        "difficulty": "Lanjut",
        "question": [
            "Diberikan array mahasiswa berisi object {nama, nilai}:",
            "  [{nama:'Andi',nilai:80}, {nama:'Budi',nilai:65},",
            "   {nama:'Citra',nilai:92}, {nama:'Dedi',nilai:70}]",
            "Menggunakan method chaining (filter/map/sort):",
            "  1. Ambil hanya mahasiswa dengan nilai >= 75.",
            "  2. Urutkan berdasarkan nilai tertinggi ke terendah.",
            "  3. Ambil HANYA nama-nya saja jadi array string.",
        ],
        "hints": [
            "mahasiswa.filter(m => m.nilai >= 75)",
            ".sort((a,b) => b.nilai - a.nilai)",
            ".map(m => m.nama)",
        ],
        "solution": """const mahasiswa = [
    { nama: "Andi", nilai: 80 },
    { nama: "Budi", nilai: 65 },
    { nama: "Citra", nilai: 92 },
    { nama: "Dedi", nilai: 70 },
];

const namaLulusUrut = mahasiswa
    .filter(m => m.nilai >= 75)
    .sort((a, b) => b.nilai - a.nilai)
    .map(m => m.nama);

console.log(namaLulusUrut);   // ['Citra', 'Andi']""",
    },
    {
        "title": "Latihan 11: Class Rekening Bank",
        "difficulty": "Lanjut",
        "question": [
            "Buat class Rekening dengan:",
            "  - private field #saldo (ES2022+)",
            "  - constructor mengisi pemilik dan saldo awal",
            "  - getter saldo",
            "  - method setor(jumlah) dan tarik(jumlah)",
            "    (tarik hanya boleh jika saldo cukup, kembalikan true/false)",
        ],
        "hints": [
            "class Rekening { #saldo; constructor(pemilik, saldo) {...} }",
            "get saldo() { return this.#saldo; }",
            "tarik(jumlah) { if (jumlah > 0 && jumlah <= this.#saldo) {...} }",
        ],
        "solution": """class Rekening {
    #saldo;

    constructor(pemilik, saldo) {
        this.pemilik = pemilik;
        this.#saldo = saldo;
    }

    get saldo() {
        return this.#saldo;
    }

    setor(jumlah) {
        if (jumlah > 0) {
            this.#saldo += jumlah;
            return true;
        }
        return false;
    }

    tarik(jumlah) {
        if (jumlah > 0 && jumlah <= this.#saldo) {
            this.#saldo -= jumlah;
            return true;
        }
        return false;
    }
}

const r = new Rekening("Andi", 100000);
r.setor(50000);
console.log(`Tarik 20000 berhasil? ${r.tarik(20000)}`);
console.log(`Tarik 999999 berhasil? ${r.tarik(999999)}`);
console.log(`Saldo akhir: ${r.saldo}`);""",
    },
    {
        "title": "Latihan 12: Pewarisan Hewan",
        "difficulty": "Lanjut",
        "question": [
            "Buat class Hewan (nama, method bersuara()).",
            "Buat subclass Kucing dan Anjing yang meng-override bersuara().",
            "Buat array berisi objek keduanya, lalu panggil bersuara()",
            "untuk semua (polymorphism) dengan forEach.",
        ],
        "hints": [
            "class Kucing extends Hewan { bersuara() {...} }",
            "super(nama) di constructor jika ada tambahan property.",
            "daftarHewan.forEach(h => h.bersuara());",
        ],
        "solution": """class Hewan {
    constructor(nama) {
        this.nama = nama;
    }
    bersuara() {
        console.log(`${this.nama} bersuara.`);
    }
}

class Kucing extends Hewan {
    bersuara() {
        console.log(`${this.nama}: Meong!`);
    }
}

class Anjing extends Hewan {
    bersuara() {
        console.log(`${this.nama}: Guk!`);
    }
}

const daftarHewan = [new Kucing("Tom"), new Anjing("Bobby")];
daftarHewan.forEach(h => h.bersuara());""",
    },
    {
        "title": "Latihan 13: Exception Handling Kalkulator",
        "difficulty": "Lanjut",
        "question": [
            "Buat fungsi bagi(a, b) yang melempar Error jika b === 0,",
            "dan melempar TypeError jika a atau b bukan bertipe number.",
            "Uji dengan try-catch untuk beberapa kasus termasuk error.",
        ],
        "hints": [
            "if (typeof a !== 'number' || typeof b !== 'number') throw new TypeError(...)",
            "if (b === 0) throw new Error('Tidak boleh bagi nol')",
            "catch (error) { if (error instanceof TypeError) {...} }",
        ],
        "solution": """function bagi(a, b) {
    if (typeof a !== "number" || typeof b !== "number") {
        throw new TypeError("Kedua argumen harus berupa angka!");
    }
    if (b === 0) {
        throw new Error("Tidak bisa membagi dengan nol!");
    }
    return a / b;
}

function ujiBagi(a, b) {
    try {
        console.log(`Hasil: ${bagi(a, b)}`);
    } catch (error) {
        if (error instanceof TypeError) {
            console.log("Error tipe:", error.message);
        } else {
            console.log("Error:", error.message);
        }
    } finally {
        console.log("-- selesai mencoba --");
    }
}

ujiBagi(10, 2);
ujiBagi(10, 0);
ujiBagi(10, "a");""",
    },
    {
        "title": "Latihan 14: Closure Counter & Module Pattern",
        "difficulty": "Lanjut",
        "question": [
            "Buat fungsi buatCounter() yang mengembalikan object dengan",
            "3 method: increment(), decrement(), dan getValue().",
            "Nilai counter harus TERSEMBUNYI (private, tidak bisa diakses",
            "langsung dari luar), hanya bisa lewat ketiga method tersebut.",
        ],
        "hints": [
            "Gunakan closure: variabel 'let hitung' di dalam buatCounter().",
            "Kembalikan object literal berisi 3 fungsi yang mengakses 'hitung'.",
        ],
        "solution": """function buatCounter() {
    let hitung = 0;   // private, hanya bisa diakses lewat closure di bawah

    return {
        increment: () => ++hitung,
        decrement: () => --hitung,
        getValue: () => hitung,
    };
}

const counter = buatCounter();
counter.increment();
counter.increment();
counter.increment();
counter.decrement();
console.log(counter.getValue());   // 2
// console.log(counter.hitung);    // undefined - tidak bisa diakses langsung!""",
    },
    {
        "title": "Latihan 15: Promise & async/await Simulasi API",
        "difficulty": "Sulit",
        "question": [
            "Buat fungsi ambilProduk(id) yang mengembalikan Promise",
            "(pakai setTimeout untuk simulasi delay 500ms). Jika id > 0",
            "resolve dengan object produk, jika id <= 0 reject dengan Error.",
            "Buat fungsi async ambilBeberapaProduk() yang mengambil 3 produk",
            "SECARA PARALEL dengan Promise.all, lalu cetak hasilnya.",
        ],
        "hints": [
            "return new Promise((resolve, reject) => { setTimeout(() => {...}, 500); });",
            "async function ambilBeberapaProduk() { const hasil = await Promise.all([...]); }",
            "Tangani error dengan try-catch di dalam fungsi async.",
        ],
        "solution": """function ambilProduk(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id > 0) {
                resolve({ id, nama: `Produk-${id}`, harga: id * 10000 });
            } else {
                reject(new Error(`ID produk tidak valid: ${id}`));
            }
        }, 500);
    });
}

async function ambilBeberapaProduk() {
    try {
        const hasil = await Promise.all([
            ambilProduk(1),
            ambilProduk(2),
            ambilProduk(3),
        ]);
        console.log("Semua produk berhasil diambil:");
        hasil.forEach(p => console.log(p));
    } catch (error) {
        console.log("Gagal mengambil produk:", error.message);
    }
}

ambilBeberapaProduk();""",
    },
    {
        "title": "Latihan 16: Debounce Function (Closure Lanjutan)",
        "difficulty": "Sulit",
        "question": [
            "Buat fungsi higher-order debounce(fungsi, delay) yang",
            "mengembalikan versi 'ditunda' dari fungsi tersebut - jika",
            "dipanggil berkali-kali dalam rentang waktu < delay, HANYA",
            "panggilan TERAKHIR yang benar-benar dieksekusi.",
            "(Pola ini umum dipakai untuk search input agar tidak",
            "memanggil API di setiap ketikan.)",
        ],
        "hints": [
            "Simpan referensi timer dengan closure (let timer di luar fungsi return).",
            "Tiap dipanggil: clearTimeout(timer) dulu, baru setTimeout baru.",
            "Gunakan ...args dan apply/spread agar argumen asli diteruskan.",
        ],
        "solution": """function debounce(fungsi, delay) {
    let timer;
    return function (...args) {
        clearTimeout(timer);           // batalkan panggilan sebelumnya
        timer = setTimeout(() => {
            fungsi(...args);
        }, delay);
    };
}

function cariProduk(kataKunci) {
    console.log(`Mencari: ${kataKunci}`);
}

const cariDebounced = debounce(cariProduk, 300);

// Simulasi user mengetik cepat - hanya panggilan TERAKHIR yang jalan
cariDebounced("a");
cariDebounced("ap");
cariDebounced("ape");
cariDebounced("apel");   // hanya ini yang akan benar-benar dieksekusi setelah 300ms diam""",
    },
    {
        "title": "Latihan 17: Custom Iterator dengan Generator",
        "difficulty": "Sulit",
        "question": [
            "Buat generator function range(awal, akhir, step) yang",
            "menghasilkan urutan angka dari awal sampai akhir (exclusive)",
            "dengan interval 'step', menggunakan 'yield'. Gunakan dengan",
            "for...of untuk mencetak hasilnya.",
        ],
        "hints": [
            "function* range(awal, akhir, step) { ... }",
            "Gunakan while di dalam generator, yield nilai saat ini, lalu increment.",
            "for (const n of range(0, 10, 2)) { console.log(n); }",
        ],
        "solution": """function* range(awal, akhir, step = 1) {
    let current = awal;
    while (current < akhir) {
        yield current;
        current += step;
    }
}

for (const n of range(0, 10, 2)) {
    console.log(n);
}
// 0 2 4 6 8

// Generator juga bisa dikonversi langsung ke array
const hasil = [...range(1, 6)];
console.log(hasil);   // [1, 2, 3, 4, 5]""",
    },
    {
        "title": "Latihan 18: Fetch API dengan Error Handling Lengkap",
        "difficulty": "Sulit",
        "question": [
            "Buat fungsi async ambilDataUser(id) yang:",
            "  1. Melakukan fetch ke 'https://api.contoh.com/users/{id}'.",
            "  2. Melempar Error kustom jika response.ok bernilai false,",
            "     dengan pesan yang menyertakan response.status.",
            "  3. Mengembalikan hasil .json() jika berhasil.",
            "  4. Di pemanggil, tangani error dengan try-catch dan",
            "     tampilkan pesan yang ramah untuk pengguna.",
        ],
        "hints": [
            "const response = await fetch(url);",
            "if (!response.ok) throw new Error(`HTTP ${response.status}`);",
            "return await response.json();",
        ],
        "solution": """async function ambilDataUser(id) {
    const url = `https://api.contoh.com/users/${id}`;
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`Gagal mengambil data user (HTTP ${response.status})`);
    }

    return await response.json();
}

async function tampilkanUser(id) {
    try {
        const user = await ambilDataUser(id);
        console.log("Data user:", user);
    } catch (error) {
        console.log("Maaf, terjadi kesalahan:", error.message);
    }
}

tampilkanUser(1);
// Catatan: kode ini butuh koneksi internet & API sungguhan untuk benar-benar
// mengembalikan data - fokus latihan ini pada POLA error handling-nya.""",
    },
]
