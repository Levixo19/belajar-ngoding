# Semua latihan bekerja di direktori sementara hasil mktemp -d, dengan hak
# pengguna biasa, dan membersihkannya sendiri lewat trap. Tidak satu pun
# menyentuh repositori milik pelajar, dan tidak satu pun butuh jaringan: remote
# di latihan ini adalah folder lain di disk yang sama.
#
# Keluaran yang dinilai sengaja TANPA hash, tanggal, dan jalur absolut --
# ketiganya berbeda di tiap mesin dan tiap detik. Identitas pembuat commit
# disetel sendiri oleh tiap skrip (git -c / git config lokal) supaya skripnya
# berjalan di komputer yang belum pernah diatur user.name sekalipun.

_KEPALA = """#!/usr/bin/env bash
#
# {judul}

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"

git init -q -b main
git config user.name "Pelajar"
git config user.email "pelajar@contoh.com"
"""

_KEPALA_KOSONG = """#!/usr/bin/env bash
#
# {judul}

set -euo pipefail

kerja="$(mktemp -d)"
trap 'rm -rf "$kerja"' EXIT
cd "$kerja"
"""

GIT_EXERCISES = [
    {
        "title": "Latihan 1: Repositori dan Commit Pertama",
        "difficulty": "Mudah",
        "question": [
            "Buat skrip bash yang bekerja di direktori sementara hasil mktemp -d.",
            "Di dalamnya: jalankan git init dengan cabang awal bernama main, atur",
            "user.name dan user.email LOKAL (tanpa --global), buat berkas catatan.txt",
            "berisi satu baris apa pun, lalu add dan commit dengan pesan",
            "\"Tambah catatan pertama\".",
            "",
            "Tampilkan nama cabang saat ini, jumlah commit, dan pesan commit terakhir.",
            "Jangan menampilkan hash: ia berbeda di tiap komputer.",
            "",
            "Keluaran yang diharapkan:",
            "  Cabang : main",
            "  Commit : 1",
            "  Pesan  : Tambah catatan pertama",
        ],
        "hints": [
            "git init -q -b main membuat repositori dengan cabang awal main tanpa pesan apa pun.",
            "git branch --show-current mencetak nama cabang yang sedang dipijak.",
            "git rev-list --count HEAD menghitung commit yang bisa dicapai dari HEAD.",
            "git log -1 --format=%s mencetak subjek commit terakhir saja.",
        ],
        "solution": _KEPALA.format(judul="Latihan 1: Repositori dan Commit Pertama") + """
echo "Hari 1: belajar git" > catatan.txt
git add catatan.txt
git commit -q -m "Tambah catatan pertama"

printf 'Cabang : %s\\n' "$(git branch --show-current)"
printf 'Commit : %s\\n' "$(git rev-list --count HEAD)"
printf 'Pesan  : %s\\n' "$(git log -1 --format=%s)"
""",
    },
    {
        "title": "Latihan 2: Tiga Area Kerja",
        "difficulty": "Mudah",
        "question": [
            "Di repositori sementara yang baru di-init, buat dua berkas: a.txt dan",
            "b.txt. Masukkan HANYA a.txt ke staging, lalu tampilkan git status --short.",
            "",
            "Kemudian commit a.txt dengan pesan \"Tambah a\", ubah isi a.txt, dan",
            "tampilkan status ringkas sekali lagi. Dua keadaan itu harus terlihat",
            "berbeda di kolom status: A untuk berkas baru yang di-stage, M di kolom",
            "kanan untuk berkas terlacak yang berubah tapi belum di-stage.",
            "",
            "Keluaran yang diharapkan:",
            "  Sebelum commit:",
            "  A  a.txt",
            "  ?? b.txt",
            "  Sesudah commit dan sunting:",
            "   M a.txt",
            "  ?? b.txt",
        ],
        "hints": [
            "git status --short mencetak dua kolom: kiri keadaan staging, kanan keadaan folder kerja.",
            "Hanya add berkas yang disebut soal; git add . akan ikut memasukkan b.txt.",
            "Sesudah commit, menulis ulang isi a.txt dengan echo sudah cukup untuk membuatnya berubah.",
            "Status untuk berkas yang berubah tapi belum di-add berawal dengan satu spasi lalu M.",
        ],
        "solution": _KEPALA.format(judul="Latihan 2: Tiga Area Kerja") + """
echo "satu" > a.txt
echo "dua" > b.txt
git add a.txt
echo "Sebelum commit:"
git status --short

git commit -q -m "Tambah a"
echo "satu diubah" > a.txt
echo "Sesudah commit dan sunting:"
git status --short
""",
    },
    {
        "title": "Latihan 3: .gitignore yang Bekerja",
        "difficulty": "Mudah",
        "question": [
            "Di repositori sementara, buat berkas .gitignore yang mengabaikan semua",
            "berkas berakhiran .log dan seluruh isi folder build/. Lalu buat berkas",
            "app.log, build/keluaran.txt, dan main.py.",
            "",
            "Tampilkan git status --short (hanya berkas yang TIDAK diabaikan yang",
            "boleh muncul), lalu untuk app.log dan build/keluaran.txt cetak baris",
            "\"diabaikan: <nama>\" dengan bantuan git check-ignore.",
            "",
            "Keluaran yang diharapkan:",
            "  ?? .gitignore",
            "  ?? main.py",
            "  diabaikan: app.log",
            "  diabaikan: build/keluaran.txt",
        ],
        "hints": [
            "Pola *.log menangkap semua berkas berakhiran .log di folder mana pun.",
            "Pola build/ dengan garis miring di akhir hanya cocok dengan folder bernama build.",
            "mkdir -p build sebelum menulis berkas di dalamnya.",
            "git check-ignore mencetak nama berkas yang cocok dengan sebuah pola, satu per baris.",
        ],
        "solution": _KEPALA.format(judul="Latihan 3: .gitignore yang Bekerja") + """
printf '*.log\\nbuild/\\n' > .gitignore
mkdir -p build
echo "catatan" > app.log
echo "hasil" > build/keluaran.txt
echo 'print("halo")' > main.py

git status --short
for berkas in $(git check-ignore app.log build/keluaran.txt); do
    echo "diabaikan: $berkas"
done
""",
    },
    {
        "title": "Latihan 4: Membaca Diff dan Riwayat",
        "difficulty": "Menengah",
        "question": [
            "Di repositori sementara, buat menu.txt berisi tiga baris: Kopi, Teh,",
            "Susu. Commit dengan pesan \"Tambah menu\". Lalu ubah baris Teh menjadi",
            "Teh Tarik dan tambahkan baris keempat Cokelat.",
            "",
            "Sebelum commit kedua, tampilkan ringkasan diff dalam bentuk",
            "\"tambah=<n> hapus=<n> berkas=<nama>\" memakai git diff --numstat.",
            "Kemudian commit dengan pesan \"Perbarui menu\" dan tampilkan seluruh",
            "pesan commit dari yang paling lama ke yang paling baru.",
            "",
            "Keluaran yang diharapkan:",
            "  tambah=2 hapus=1 berkas=menu.txt",
            "  Riwayat:",
            "  Tambah menu",
            "  Perbarui menu",
        ],
        "hints": [
            "git diff --numstat mencetak tiga kolom dipisah tab: baris ditambah, baris dihapus, nama berkas.",
            "Bagi Git, mengubah satu baris berarti satu baris hilang dan satu baris muncul.",
            "awk membaca kolom pertama sebagai $1, kedua $2, ketiga $3.",
            "git log --format=%s --reverse mencetak subjek commit dari yang tertua.",
        ],
        "solution": _KEPALA.format(judul="Latihan 4: Membaca Diff dan Riwayat") + """
printf 'Kopi\\nTeh\\nSusu\\n' > menu.txt
git add menu.txt
git commit -q -m "Tambah menu"

printf 'Kopi\\nTeh Tarik\\nSusu\\nCokelat\\n' > menu.txt
git diff --numstat | awk '{ print "tambah=" $1 " hapus=" $2 " berkas=" $3 }'

git commit -q -a -m "Perbarui menu"
echo "Riwayat:"
git log --format=%s --reverse
""",
    },
    {
        "title": "Latihan 5: Pesan Commit Konvensional",
        "difficulty": "Menengah",
        "question": [
            "Buat tiga commit berurutan di repositori sementara, masing-masing",
            "menyentuh berkas apa pun, dengan subjek bergaya Conventional Commits:",
            "",
            "  feat(menu): tambah halaman menu",
            "  fix(menu): perbaiki harga kopi",
            "  docs: tulis cara menjalankan",
            "",
            "Tampilkan ketiga subjek dari yang tertua, lalu hitung berapa commit",
            "untuk tiap jenis (feat, fix, docs) dengan membaca awalan subjeknya.",
            "",
            "Keluaran yang diharapkan:",
            "  feat(menu): tambah halaman menu",
            "  fix(menu): perbaiki harga kopi",
            "  docs: tulis cara menjalankan",
            "  feat: 1",
            "  fix: 1",
            "  docs: 1",
        ],
        "hints": [
            "Satu commit butuh satu perubahan; menulis ulang berkas yang sama tiga kali sudah cukup.",
            "git commit -q -a -m hanya bekerja untuk berkas yang sudah dilacak; berkas baru tetap perlu add.",
            "Jenis commit adalah teks sebelum tanda kurung atau titik dua pertama di subjek.",
            "grep -c menghitung baris yang cocok; pola ^feat menangkap subjek yang diawali feat.",
        ],
        "solution": _KEPALA.format(judul="Latihan 5: Pesan Commit Konvensional") + """
echo "menu" > menu.txt
git add menu.txt
git commit -q -m "feat(menu): tambah halaman menu"

echo "kopi 12000" > menu.txt
git commit -q -a -m "fix(menu): perbaiki harga kopi"

echo "jalankan: python3 app.py" > README.md
git add README.md
git commit -q -m "docs: tulis cara menjalankan"

git log --format=%s --reverse
for jenis in feat fix docs; do
    printf '%s: %s\\n' "$jenis" "$(git log --format=%s | grep -c "^$jenis")"
done
""",
    },
    {
        "title": "Latihan 6: Membatalkan dengan Aman",
        "difficulty": "Menengah",
        "question": [
            "Di repositori sementara, buat halo.txt berisi \"Halo\" dan commit dengan",
            "pesan \"Tulis sapaan\". Lalu:",
            "",
            "  1. Ubah isinya jadi \"Halo dunia\" TANPA add, lalu batalkan dengan",
            "     git restore. Cetak isinya.",
            "  2. Ubah isinya jadi \"Pergi!\" dan commit dengan pesan \"Ubah sapaan\".",
            "     Batalkan commit itu dengan git revert tanpa membuka editor. Cetak",
            "     isinya lagi, lalu seluruh subjek commit dari yang tertua.",
            "",
            "Keluaran yang diharapkan:",
            "  Sesudah restore: Halo",
            "  Sesudah revert : Halo",
            "  Riwayat:",
            "  Tulis sapaan",
            "  Ubah sapaan",
            "  Revert \"Ubah sapaan\"",
        ],
        "hints": [
            "git restore halo.txt mengembalikan berkas ke versi di HEAD selama perubahannya belum di-add.",
            "git revert --no-edit HEAD membuat commit pembalik dengan pesan bawaan tanpa membuka editor.",
            "Pesan bawaan revert berbentuk Revert diikuti subjek commit yang dibatalkan dalam tanda kutip.",
            "Alihkan keluaran revert ke /dev/null supaya baris ringkasannya yang memuat hash tidak ikut tercetak.",
        ],
        "solution": _KEPALA.format(judul="Latihan 6: Membatalkan dengan Aman") + """
echo "Halo" > halo.txt
git add halo.txt
git commit -q -m "Tulis sapaan"

echo "Halo dunia" > halo.txt
git restore halo.txt
printf 'Sesudah restore: %s\\n' "$(cat halo.txt)"

echo "Pergi!" > halo.txt
git commit -q -a -m "Ubah sapaan"
git revert --no-edit HEAD > /dev/null
printf 'Sesudah revert : %s\\n' "$(cat halo.txt)"

echo "Riwayat:"
git log --format=%s --reverse
""",
    },
    {
        "title": "Latihan 7: Branch dan Fast-forward",
        "difficulty": "Menengah",
        "question": [
            "Di repositori sementara dengan satu commit \"Awal\", buat cabang fitur,",
            "pindah ke sana, dan buat dua commit: \"Tambah menu\" lalu \"Tambah ulasan\".",
            "Kembali ke main dan merge cabang fitur. Karena main belum bergerak,",
            "merge-nya harus fast-forward: tidak ada merge commit yang terbentuk.",
            "",
            "Tampilkan daftar nama cabang dalam satu baris, seluruh subjek commit di",
            "main dari yang tertua, dan jumlah merge commit.",
            "",
            "Keluaran yang diharapkan:",
            "  Cabang: fitur main",
            "  Riwayat main:",
            "  Awal",
            "  Tambah menu",
            "  Tambah ulasan",
            "  Merge commit: 0",
        ],
        "hints": [
            "git switch -c fitur membuat cabang sekaligus pindah ke sana.",
            "git branch --format='%(refname:short)' mencetak nama cabang saja, tanpa tanda bintang.",
            "git merge -q fitur dari main menggabungkan tanpa mencetak ringkasan.",
            "git log --merges mencetak hanya merge commit; hitung barisnya dengan wc -l.",
        ],
        "solution": _KEPALA.format(judul="Latihan 7: Branch dan Fast-forward") + """
echo "awal" > awal.txt
git add awal.txt
git commit -q -m "Awal"

git switch -q -c fitur
echo "menu" > menu.txt
git add menu.txt
git commit -q -m "Tambah menu"
echo "ulasan" > ulasan.txt
git add ulasan.txt
git commit -q -m "Tambah ulasan"

git switch -q main
git merge -q fitur

printf 'Cabang: %s\\n' "$(git branch --format='%(refname:short)' | tr '\\n' ' ' | sed 's/ $//')"
echo "Riwayat main:"
git log --format=%s --reverse
printf 'Merge commit: %s\\n' "$(git log --merges --format=%s | wc -l)"
""",
    },
    {
        "title": "Latihan 8: Merge Commit dan Graf Riwayat",
        "difficulty": "Lanjut",
        "question": [
            "Di repositori sementara dengan commit \"Awal\", buat cabang fitur berisi",
            "dua commit (\"Buat halaman ulasan\", \"Tambah ulasan\"). Kembali ke main",
            "dan buat satu commit \"Perbaiki tautan\" supaya kedua garis bercabang.",
            "Lalu merge fitur ke main TANPA membuka editor, dengan pesan bawaan.",
            "",
            "Tampilkan graf riwayat memakai git log --graph dengan format subjek saja,",
            "dan buang spasi di ujung tiap baris. Kemudian cetak jumlah orang tua",
            "commit terbaru.",
            "",
            "Keluaran yang diharapkan:",
            "  *   Merge branch 'fitur'",
            "  |\\",
            "  | * Tambah ulasan",
            "  | * Buat halaman ulasan",
            "  * | Perbaiki tautan",
            "  |/",
            "  * Awal",
            "  Orang tua HEAD: 2",
        ],
        "hints": [
            "Commit di main sesudah cabang dibuat memaksa Git membuat merge commit, bukan fast-forward.",
            "git merge --no-edit fitur memakai pesan bawaan Merge branch 'fitur' tanpa membuka editor.",
            "git log --graph --format=%s menggambar garis percabangan di kiri subjek.",
            "git rev-list --parents -n 1 HEAD mencetak hash HEAD diikuti hash orang tuanya; jumlah kata dikurangi satu adalah jumlah orang tuanya.",
        ],
        "solution": _KEPALA.format(judul="Latihan 8: Merge Commit dan Graf Riwayat") + """
echo "awal" > awal.txt
git add awal.txt
git commit -q -m "Awal"

git switch -q -c fitur
echo "ulasan" > ulasan.txt
git add ulasan.txt
git commit -q -m "Buat halaman ulasan"
echo "ulasan kedua" >> ulasan.txt
git commit -q -a -m "Tambah ulasan"

git switch -q main
echo "tautan diperbaiki" > awal.txt
git commit -q -a -m "Perbaiki tautan"

git merge -q --no-edit fitur

git log --graph --format=%s | sed 's/[[:space:]]*$//'
jumlah="$(git rev-list --parents -n 1 HEAD | wc -w)"
printf 'Orang tua HEAD: %s\\n' "$((jumlah - 1))"
""",
    },
    {
        "title": "Latihan 9: Menyelesaikan Konflik",
        "difficulty": "Lanjut",
        "question": [
            "Di repositori sementara, buat menu.txt berisi satu baris \"harga: 10000\"",
            "dan commit \"Awal\". Buat cabang diskon yang mengubah baris itu jadi",
            "\"harga: 8000\" (commit \"Beri diskon\"). Kembali ke main dan ubah baris",
            "yang sama jadi \"harga: 12000\" (commit \"Naikkan harga\").",
            "",
            "Merge diskon ke main. Merge-nya HARUS berhenti karena konflik; tangkap",
            "kegagalannya tanpa menghentikan skrip, cetak nama berkas yang berkonflik,",
            "lalu selesaikan dengan menulis \"harga: 9000\", add, dan commit dengan pesan",
            "\"Gabungkan diskon dengan harga baru\". Terakhir cetak isi berkas dan",
            "riwayat garis utama main (orang tua pertama saja) dari yang tertua.",
            "",
            "Keluaran yang diharapkan:",
            "  Konflik di: menu.txt",
            "  Isi akhir: harga: 9000",
            "  Garis utama:",
            "  Awal",
            "  Naikkan harga",
            "  Gabungkan diskon dengan harga baru",
        ],
        "hints": [
            "Dua cabang yang mengubah baris yang sama dengan isi berbeda memaksa Git menyerahkan keputusannya kepadamu.",
            "Merge yang berkonflik keluar dengan kode 1; letakkan di dalam if supaya set -e tidak menghentikan skrip, dan alihkan keluarannya ke /dev/null.",
            "git diff --name-only --diff-filter=U mencetak berkas yang masih berstatus unmerged.",
            "Menulis ulang berkas dengan isi akhir lalu git add menandai konfliknya selesai; commit sesudahnya menjadi merge commit.",
            "git log --first-parent hanya mengikuti orang tua pertama tiap commit, jadi commit di cabang diskon tidak ikut tercetak.",
        ],
        "solution": _KEPALA.format(judul="Latihan 9: Menyelesaikan Konflik") + """
echo "harga: 10000" > menu.txt
git add menu.txt
git commit -q -m "Awal"

git switch -q -c diskon
echo "harga: 8000" > menu.txt
git commit -q -a -m "Beri diskon"

git switch -q main
echo "harga: 12000" > menu.txt
git commit -q -a -m "Naikkan harga"

if git merge -q diskon > /dev/null 2>&1; then
    echo "Merge mulus (seharusnya tidak terjadi)"
else
    printf 'Konflik di: %s\\n' "$(git diff --name-only --diff-filter=U)"
fi

echo "harga: 9000" > menu.txt
git add menu.txt
git commit -q -m "Gabungkan diskon dengan harga baru"

printf 'Isi akhir: %s\\n' "$(cat menu.txt)"
echo "Garis utama:"
git log --first-parent --format=%s --reverse
""",
    },
    {
        "title": "Latihan 10: Remote Lokal: clone, push, fetch",
        "difficulty": "Lanjut",
        "question": [
            "Remote tidak harus di internet. Di direktori sementara, buat repositori",
            "BARE bernama pusat.git dengan cabang awal main (git init --bare). Clone",
            "ke folder laptop, atur identitas lokal di sana, commit README.md dengan",
            "pesan \"Mulai proyek\", dan push ke origin sambil memasang upstream.",
            "Dari laptop buat juga cabang fitur berisi satu commit dan push cabang itu.",
            "",
            "Lalu clone pusat.git sekali lagi ke folder kantor. Dari kantor cetak nama",
            "remote-nya, jumlah commit di main, dan daftar cabang remote yang terlihat",
            "(tanpa baris origin/HEAD dan tanpa spasi di depan).",
            "",
            "Keluaran yang diharapkan:",
            "  Remote: origin",
            "  Commit di main: 1",
            "  Cabang di remote:",
            "  origin/fitur",
            "  origin/main",
        ],
        "hints": [
            "git init -q --bare -b main pusat.git membuat repositori tanpa folder kerja, persis seperti yang disimpan GitHub.",
            "git clone -q pusat.git laptop memakai jalur folder sebagai alamat remote; origin-nya terpasang otomatis.",
            "Identitas harus diatur di tiap clone yang membuat commit, karena git config tanpa --global hanya berlaku untuk satu repositori.",
            "git push -q -u origin main mengirim cabang sekaligus mengingat pasangannya.",
            "git branch -r mencetak cabang remote dengan dua spasi di depan; buang baris origin/HEAD dengan grep -v dan spasinya dengan sed.",
        ],
        "solution": _KEPALA_KOSONG.format(judul="Latihan 10: Remote Lokal: clone, push, fetch") + """
git init -q --bare -b main pusat.git

git clone -q pusat.git laptop 2> /dev/null
cd laptop
git config user.name "Pelajar"
git config user.email "pelajar@contoh.com"
echo "# Proyek" > README.md
git add README.md
git commit -q -m "Mulai proyek"
git push -q -u origin main

git switch -q -c fitur
echo "fitur" > fitur.txt
git add fitur.txt
git commit -q -m "Mulai fitur"
git push -q -u origin fitur
cd ..

git clone -q pusat.git kantor
cd kantor
printf 'Remote: %s\\n' "$(git remote)"
printf 'Commit di main: %s\\n' "$(git rev-list --count HEAD)"
echo "Cabang di remote:"
git branch -r | grep -v HEAD | sed 's/^ *//'
""",
    },
    {
        "title": "Latihan 11: Stash untuk Pekerjaan Setengah Jadi",
        "difficulty": "Menengah",
        "question": [
            "Di repositori sementara, commit kerja.txt berisi \"v1\" dengan pesan",
            "\"Awal\". Ubah isinya jadi \"setengah jadi\" tapi JANGAN commit. Simpan",
            "perubahan itu dengan git stash, cetak isi berkas dan jumlah stash.",
            "",
            "Kerjakan hal mendesak: buat darurat.txt, add, commit \"Perbaikan darurat\".",
            "Lalu ambil kembali pekerjaanmu dengan git stash pop, cetak isi berkas dan",
            "jumlah stash lagi, dan tutup dengan git status --short.",
            "",
            "Keluaran yang diharapkan:",
            "  Sesudah stash: v1",
            "  Stash tersimpan: 1",
            "  Sesudah pop: setengah jadi",
            "  Stash tersimpan: 0",
            "   M kerja.txt",
        ],
        "hints": [
            "git stash -q menyimpan perubahan folder kerja dan staging, lalu mengembalikan berkas ke versi HEAD.",
            "git stash list mencetak satu baris per simpanan; wc -l menghitungnya.",
            "git stash pop -q menerapkan simpanan teratas sekaligus menghapusnya dari daftar.",
            "Sesudah pop, kerja.txt kembali berubah tapi belum di-stage, jadi statusnya spasi lalu M.",
        ],
        "solution": _KEPALA.format(judul="Latihan 11: Stash untuk Pekerjaan Setengah Jadi") + """
echo "v1" > kerja.txt
git add kerja.txt
git commit -q -m "Awal"

echo "setengah jadi" > kerja.txt
git stash -q
printf 'Sesudah stash: %s\\n' "$(cat kerja.txt)"
printf 'Stash tersimpan: %s\\n' "$(git stash list | wc -l)"

echo "perbaikan" > darurat.txt
git add darurat.txt
git commit -q -m "Perbaikan darurat"

git stash pop -q
printf 'Sesudah pop: %s\\n' "$(cat kerja.txt)"
printf 'Stash tersimpan: %s\\n' "$(git stash list | wc -l)"
git status --short
""",
    },
    {
        "title": "Latihan 12: Tag dan Cherry-pick",
        "difficulty": "Lanjut",
        "question": [
            "Di repositori sementara, commit versi.txt berisi \"1.0\" dengan pesan",
            "\"Rilis awal\" dan beri tag beranotasi v1.0 berpesan \"Versi 1.0\".",
            "",
            "Buat cabang eksperimen dengan dua commit: \"Fitur besar (belum siap)\"",
            "yang menambah besar.txt, lalu \"Perbaiki typo README\" yang menambah",
            "README.md. Hanya commit kedua yang layak masuk main sekarang: kembali ke",
            "main dan cherry-pick commit TERAKHIR eksperimen, lalu beri tag v1.0.1",
            "berpesan \"Versi 1.0.1\".",
            "",
            "Cetak daftar tag, riwayat main dari yang tertua, berkas yang dilacak di",
            "main dalam satu baris, dan pesan tag v1.0.1.",
            "",
            "Keluaran yang diharapkan:",
            "  Tag:",
            "  v1.0",
            "  v1.0.1",
            "  Riwayat main:",
            "  Rilis awal",
            "  Perbaiki typo README",
            "  Berkas di main: README.md versi.txt",
            "  Pesan v1.0.1: Versi 1.0.1",
        ],
        "hints": [
            "git tag -a v1.0 -m \"Versi 1.0\" membuat tag beranotasi yang menyimpan pesan dan pembuatnya.",
            "Nama cabang menunjuk commit ujungnya, jadi git cherry-pick eksperimen menyalin commit terakhir cabang itu saja.",
            "cherry-pick mencetak ringkasan berisi hash ke stdout; alihkan ke /dev/null supaya keluarannya bersih.",
            "git ls-files mencetak berkas terlacak, satu per baris; tr dan sed merapikannya jadi satu baris.",
            "git tag -l --format='%(contents:subject)' v1.0.1 mencetak baris pertama pesan tag.",
        ],
        "solution": _KEPALA.format(judul="Latihan 12: Tag dan Cherry-pick") + """
echo "1.0" > versi.txt
git add versi.txt
git commit -q -m "Rilis awal"
git tag -a v1.0 -m "Versi 1.0"

git switch -q -c eksperimen
echo "fitur besar" > besar.txt
git add besar.txt
git commit -q -m "Fitur besar (belum siap)"
echo "# Proyek" > README.md
git add README.md
git commit -q -m "Perbaiki typo README"

git switch -q main
git cherry-pick eksperimen > /dev/null
git tag -a v1.0.1 -m "Versi 1.0.1"

echo "Tag:"
git tag
echo "Riwayat main:"
git log --format=%s --reverse
printf 'Berkas di main: %s\\n' "$(git ls-files | tr '\\n' ' ' | sed 's/ $//')"
printf 'Pesan v1.0.1: %s\\n' "$(git tag -l --format='%(contents:subject)' v1.0.1)"
""",
    },
    {
        "title": "Latihan 13: Tiga Wajah reset",
        "difficulty": "Lanjut",
        "question": [
            "Di repositori sementara, buat tiga commit berurutan: \"Satu\" (a.txt),",
            "\"Dua\" (b.txt), \"Tiga\" (c.txt). Tandai ujungnya dengan tag ringan",
            "bernama puncak supaya kamu bisa kembali ke sana.",
            "",
            "Lalu peragakan tiga jenis reset, masing-masing dari keadaan puncak",
            "(kembalikan dulu dengan git reset --hard puncak sebelum percobaan",
            "berikutnya): --soft HEAD~1, --mixed HEAD~1, dan --hard HEAD~1. Untuk",
            "tiap jenis cetak jumlah commit dan git status --short dalam kurung",
            "siku. Tutup dengan daftar berkas yang tersisa di folder kerja sesudah",
            "--hard.",
            "",
            "Keluaran yang diharapkan:",
            "  soft  : commit=2 status=[A  c.txt]",
            "  mixed : commit=2 status=[?? c.txt]",
            "  hard  : commit=2 status=[]",
            "  Berkas tersisa: a.txt b.txt",
        ],
        "hints": [
            "git tag puncak tanpa -a membuat tag ringan: sekadar nama untuk commit saat ini.",
            "--soft memundurkan HEAD saja, jadi c.txt tetap di staging dan statusnya A.",
            "--mixed (bawaan) juga mengosongkan staging; c.txt masih ada di folder kerja tapi tidak dilacak.",
            "--hard ikut menghapus perubahan di folder kerja, sehingga c.txt lenyap dan statusnya kosong.",
            "Pakai git reset -q supaya ringkasan berisi hash tidak tercetak, dan ls untuk daftar berkasnya.",
        ],
        "solution": _KEPALA.format(judul="Latihan 13: Tiga Wajah reset") + """
for nama in a b c; do
    echo "$nama" > "$nama.txt"
    git add "$nama.txt"
done
git reset -q
git add a.txt && git commit -q -m "Satu"
git add b.txt && git commit -q -m "Dua"
git add c.txt && git commit -q -m "Tiga"
git tag puncak

lapor() {
    printf '%-6s: commit=%s status=[%s]\\n' "$1" "$(git rev-list --count HEAD)" "$(git status --short | tr -d '\\n')"
}

git reset -q --soft HEAD~1
lapor soft
git reset -q --hard puncak

git reset -q --mixed HEAD~1
lapor mixed
git reset -q --hard puncak

git reset -q --hard HEAD~1
lapor hard
printf 'Berkas tersisa: %s\\n' "$(ls | tr '\\n' ' ' | sed 's/ $//')"
""",
    },
    {
        "title": "Latihan 14: Rebase untuk Riwayat Lurus",
        "difficulty": "Lanjut",
        "question": [
            "Di repositori sementara dengan commit \"Awal\", buat cabang fitur berisi",
            "commit \"Tambah fitur\" (berkas fitur.txt). Kembali ke main dan buat",
            "commit \"Perbaiki bug\" (berkas bug.txt) supaya keduanya bercabang.",
            "",
            "Cetak apakah main sudah menjadi leluhur fitur. Lalu rebase fitur ke atas",
            "main, cetak pertanyaan yang sama lagi, merge fitur ke main (harus",
            "fast-forward), dan tampilkan graf riwayat subjek saja plus jumlah merge",
            "commit.",
            "",
            "Keluaran yang diharapkan:",
            "  main leluhur fitur sebelum rebase: tidak",
            "  main leluhur fitur sesudah rebase: ya",
            "  * Tambah fitur",
            "  * Perbaiki bug",
            "  * Awal",
            "  Merge commit: 0",
        ],
        "hints": [
            "git merge-base --is-ancestor main fitur keluar dengan kode 0 kalau main leluhur fitur; pakai di dalam if.",
            "git rebase -q main dijalankan DARI cabang fitur: commit fitur disalin ulang di atas ujung main.",
            "Sesudah rebase, main tinggal dimajukan, jadi git merge fitur menjadi fast-forward tanpa merge commit.",
            "git log --graph --format=%s menggambar riwayat; sesudah rebase garisnya lurus.",
        ],
        "solution": _KEPALA.format(judul="Latihan 14: Rebase untuk Riwayat Lurus") + """
echo "awal" > awal.txt
git add awal.txt
git commit -q -m "Awal"

git switch -q -c fitur
echo "fitur" > fitur.txt
git add fitur.txt
git commit -q -m "Tambah fitur"

git switch -q main
echo "bug" > bug.txt
git add bug.txt
git commit -q -m "Perbaiki bug"

leluhur() {
    if git merge-base --is-ancestor main fitur; then echo "ya"; else echo "tidak"; fi
}

printf 'main leluhur fitur sebelum rebase: %s\\n' "$(leluhur)"
git switch -q fitur
git rebase -q main
printf 'main leluhur fitur sesudah rebase: %s\\n' "$(leluhur)"

git switch -q main
git merge -q fitur
git log --graph --format=%s | sed 's/[[:space:]]*$//'
printf 'Merge commit: %s\\n' "$(git log --merges --format=%s | wc -l)"
""",
    },
    {
        "title": "Latihan 15: Reflog: Menyelamatkan Commit yang Hilang",
        "difficulty": "Sulit",
        "question": [
            "Di repositori sementara, buat tiga commit: \"Satu\", \"Dua\", \"Tiga\".",
            "Hancurkan dua commit terakhir dengan git reset --hard HEAD~2 dan cetak",
            "jumlah commit yang tersisa. Cetak juga baris reflog teratas (subjeknya",
            "saja) untuk membuktikan Git masih ingat apa yang baru terjadi.",
            "",
            "Lalu pulihkan: cari posisi HEAD SEBELUM reset lewat reflog (HEAD@{1}) dan",
            "reset --hard ke sana. Cetak jumlah commit sesudah pulih dan seluruh",
            "subjeknya dari yang tertua.",
            "",
            "Keluaran yang diharapkan:",
            "  Sesudah reset: 1 commit",
            "  Reflog teratas: reset: moving to HEAD~2",
            "  Sesudah pulih: 3 commit",
            "  Satu",
            "  Dua",
            "  Tiga",
        ],
        "hints": [
            "reset --hard memindahkan cabang, tapi commit yang ditinggalkannya masih ada di basis data objek selama belum dibersihkan.",
            "git reflog -1 --format=%gs mencetak subjek entri reflog teratas, yaitu tindakan yang paling baru.",
            "HEAD@{1} berarti \"posisi HEAD satu langkah sebelum sekarang\" menurut reflog.",
            "git reset -q --hard HEAD@{1} mengembalikan cabang ke posisi itu; pakai tanda kutip supaya shell tidak mengolah kurung kurawalnya.",
        ],
        "solution": _KEPALA.format(judul="Latihan 15: Reflog: Menyelamatkan Commit yang Hilang") + """
for pesan in Satu Dua Tiga; do
    echo "$pesan" > "$pesan.txt"
    git add "$pesan.txt"
    git commit -q -m "$pesan"
done

git reset -q --hard HEAD~2
printf 'Sesudah reset: %s commit\\n' "$(git rev-list --count HEAD)"
printf 'Reflog teratas: %s\\n' "$(git reflog -1 --format=%gs)"

git reset -q --hard 'HEAD@{1}'
printf 'Sesudah pulih: %s commit\\n' "$(git rev-list --count HEAD)"
git log --format=%s --reverse
""",
    },
    {
        "title": "Latihan 16: Proyek Akhir: Simulasi Tim dengan Remote",
        "difficulty": "Sulit",
        "proyek": True,
        "question": [
            "Peragakan alur kerja tim dua orang tanpa internet. Di direktori",
            "sementara, buat repositori bare pusat.git (cabang awal main) sebagai",
            "pengganti GitHub, lalu dua clone: ani dan budi, masing-masing dengan",
            "identitas lokal bernama Ani dan Budi.",
            "",
            "Alurnya:",
            "  1. Ani commit menu.txt berisi dua baris (Kopi, Teh) dengan pesan",
            "     \"Mulai proyek warung\", lalu push. Budi baru clone SESUDAH itu.",
            "  2. Ani membuat cabang fitur/teh-manis yang mengubah baris Teh jadi",
            "     \"Teh Manis\" (pesan \"feat(menu): tambah varian teh manis\"), push",
            "     cabangnya, lalu memerankan tombol Merge di GitHub: merge --no-ff ke",
            "     main dengan pesan \"Merge PR #1: feat(menu): tambah varian teh manis\",",
            "     push main, dan hapus cabang fitur di remote maupun lokal.",
            "  3. Sementara itu Budi mengubah baris Teh jadi \"Teh Tarik\" di main",
            "     lokalnya (pesan \"fix(menu): perjelas nama teh\") dan mencoba push.",
            "     Cetak apakah push-nya diterima atau ditolak.",
            "  4. Budi pull (mode merge) dan mendapat konflik; cetak nama berkasnya.",
            "     Selesaikan dengan tiga baris: Kopi, Teh Tarik, Teh Manis; commit",
            "     \"Gabungkan teh tarik dan teh manis\"; push. Lalu beri tag beranotasi",
            "     v1.0 (pesan \"Rilis pertama\") dan push tag itu.",
            "  5. Ani pull, lalu cetak isi menu, daftar tag, graf riwayat berformat",
            "     \"subjek (penulis)\", dan jumlah commit tiap orang.",
            "",
            "Keluaran yang diharapkan:",
            "  Push Budi: ditolak",
            "  Konflik di: menu.txt",
            "  Menu akhir:",
            "  Kopi",
            "  Teh Tarik",
            "  Teh Manis",
            "  Tag: v1.0",
            "  Graf:",
            "  *   Gabungkan teh tarik dan teh manis (Budi)",
            "  |\\",
            "  | *   Merge PR #1: feat(menu): tambah varian teh manis (Ani)",
            "  | |\\",
            "  | | * feat(menu): tambah varian teh manis (Ani)",
            "  | |/",
            "  * / fix(menu): perjelas nama teh (Budi)",
            "  |/",
            "  * Mulai proyek warung (Ani)",
            "  Commit Ani: 3",
            "  Commit Budi: 2",
        ],
        "hints": [
            "Susun skripnya mengikuti nomor langkah di soal, dan pindah folder dengan cd ke clone yang sedang bekerja.",
            "Push yang ditolak keluar dengan kode bukan nol; bungkus dalam if dan alihkan pesannya ke /dev/null.",
            "git pull --no-rebase -q harus disebut eksplisit: tanpa pilihan itu Git menolak menggabungkan cabang yang bercabang.",
            "Pull yang berkonflik juga keluar dengan kode bukan nol, jadi tangkap dengan if dan baca berkasnya lewat git diff --name-only --diff-filter=U.",
            "git log --graph --format='%s (%an)' menggambar riwayat dengan nama penulis; git log --author=Ani --format=%s | wc -l menghitung commit Ani.",
        ],
        "solution": _KEPALA_KOSONG.format(judul="Latihan 16: Proyek Akhir: Simulasi Tim dengan Remote") + """
kenalkan() {
    git config user.name "$1"
    git config user.email "$2"
}

git init -q --bare -b main pusat.git

# 1. Ani memulai proyek
git clone -q pusat.git ani 2> /dev/null
cd ani
kenalkan "Ani" "ani@contoh.com"
printf 'Kopi\\nTeh\\n' > menu.txt
git add menu.txt
git commit -q -m "Mulai proyek warung"
git push -q -u origin main
cd ..

git clone -q pusat.git budi
cd budi
kenalkan "Budi" "budi@contoh.com"
cd ..

# 2. Ani: cabang fitur, "pull request", merge ke main
cd ani
git switch -q -c fitur/teh-manis
printf 'Kopi\\nTeh Manis\\n' > menu.txt
git commit -q -a -m "feat(menu): tambah varian teh manis"
git push -q -u origin fitur/teh-manis
git switch -q main
git merge -q --no-ff -m "Merge PR #1: feat(menu): tambah varian teh manis" fitur/teh-manis
git push -q origin main
git push -q -d origin fitur/teh-manis
git branch -q -d fitur/teh-manis
cd ..

# 3. Budi: mengubah baris yang sama, push ditolak
cd budi
printf 'Kopi\\nTeh Tarik\\n' > menu.txt
git commit -q -a -m "fix(menu): perjelas nama teh"
if git push -q origin main > /dev/null 2>&1; then
    echo "Push Budi: diterima"
else
    echo "Push Budi: ditolak"
fi

# 4. Budi: pull, konflik, selesaikan, push, tag
if ! git pull --no-rebase -q > /dev/null 2>&1; then
    printf 'Konflik di: %s\\n' "$(git diff --name-only --diff-filter=U)"
fi
printf 'Kopi\\nTeh Tarik\\nTeh Manis\\n' > menu.txt
git add menu.txt
git commit -q -m "Gabungkan teh tarik dan teh manis"
git push -q origin main
git tag -a v1.0 -m "Rilis pertama"
git push -q origin v1.0
cd ..

# 5. Ani menarik hasil akhir
cd ani
git pull -q
echo "Menu akhir:"
cat menu.txt
printf 'Tag: %s\\n' "$(git tag)"
echo "Graf:"
git log --graph --format='%s (%an)' | sed 's/[[:space:]]*$//'
printf 'Commit Ani: %s\\n' "$(git log --author=Ani --format=%s | wc -l)"
printf 'Commit Budi: %s\\n' "$(git log --author=Budi --format=%s | wc -l)"
""",
    },
]
