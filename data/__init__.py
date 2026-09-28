"""Kumpulan konten kurikulum per bahasa.

Setiap bahasa punya tiga file: materi, kuis, dan latihan.
Menambah bahasa baru = tambah tiga file di sini, ekspor di bawah,
lalu daftarkan satu entri di LANGUAGES pada main.py.
"""

from data.normalisasi import seimbangkan_kuis

from data.aplikasi_materials import APLIKASI_MATERIALS
from data.aplikasi_quizzes import APLIKASI_QUIZZES as _APLIKASI_QUIZZES
from data.aplikasi_exercises import APLIKASI_EXERCISES

from data.java_materials import JAVA_MATERIALS
from data.java_quizzes import JAVA_QUIZZES as _JAVA_QUIZZES
from data.java_exercises import JAVA_EXERCISES

from data.sql_materials import SQL_MATERIALS
from data.sql_quizzes import SQL_QUIZZES as _SQL_QUIZZES
from data.sql_exercises import SQL_EXERCISES

from data.python_materials import PYTHON_MATERIALS
from data.python_quizzes import PYTHON_QUIZZES as _PYTHON_QUIZZES
from data.python_exercises import PYTHON_EXERCISES

from data.javascript_materials import JAVASCRIPT_MATERIALS
from data.javascript_quizzes import JAVASCRIPT_QUIZZES as _JAVASCRIPT_QUIZZES
from data.javascript_exercises import JAVASCRIPT_EXERCISES

from data.c_materials import C_MATERIALS
from data.c_quizzes import C_QUIZZES as _C_QUIZZES
from data.c_exercises import C_EXERCISES

from data.cpp_materials import CPP_MATERIALS
from data.cpp_quizzes import CPP_QUIZZES as _CPP_QUIZZES
from data.cpp_exercises import CPP_EXERCISES

from data.bash_materials import BASH_MATERIALS
from data.bash_quizzes import BASH_QUIZZES as _BASH_QUIZZES
from data.bash_exercises import BASH_EXERCISES

from data.go_materials import GO_MATERIALS
from data.go_quizzes import GO_QUIZZES as _GO_QUIZZES
from data.go_exercises import GO_EXERCISES

from data.html_materials import HTML_MATERIALS
from data.html_quizzes import HTML_QUIZZES as _HTML_QUIZZES
from data.html_exercises import HTML_EXERCISES

from data.css_materials import CSS_MATERIALS
from data.css_quizzes import CSS_QUIZZES as _CSS_QUIZZES
from data.css_exercises import CSS_EXERCISES

from data.csharp_materials import CSHARP_MATERIALS
from data.csharp_quizzes import CSHARP_QUIZZES as _CSHARP_QUIZZES
from data.csharp_exercises import CSHARP_EXERCISES

from data.rust_materials import RUST_MATERIALS
from data.rust_quizzes import RUST_QUIZZES as _RUST_QUIZZES
from data.rust_exercises import RUST_EXERCISES

from data.php_materials import PHP_MATERIALS
from data.php_quizzes import PHP_QUIZZES as _PHP_QUIZZES
from data.php_exercises import PHP_EXERCISES

from data.ruby_materials import RUBY_MATERIALS
from data.ruby_quizzes import RUBY_QUIZZES as _RUBY_QUIZZES
from data.ruby_exercises import RUBY_EXERCISES

from data.kotlin_materials import KOTLIN_MATERIALS
from data.kotlin_quizzes import KOTLIN_QUIZZES as _KOTLIN_QUIZZES
from data.kotlin_exercises import KOTLIN_EXERCISES

from data.typescript_materials import TYPESCRIPT_MATERIALS
from data.typescript_quizzes import TYPESCRIPT_QUIZZES as _TYPESCRIPT_QUIZZES
from data.typescript_exercises import TYPESCRIPT_EXERCISES

from data.vb_materials import VB_MATERIALS
from data.vb_quizzes import VB_QUIZZES as _VB_QUIZZES
from data.vb_exercises import VB_EXERCISES

from data.fedora_materials import FEDORA_MATERIALS
from data.fedora_quizzes import FEDORA_QUIZZES as _FEDORA_QUIZZES
from data.fedora_exercises import FEDORA_EXERCISES

# Posisi jawaban diratakan supaya kuis tidak bisa ditebak dari polanya.
# Lihat data/normalisasi.py untuk alasan lengkapnya.
APLIKASI_QUIZZES = seimbangkan_kuis(_APLIKASI_QUIZZES)
JAVA_QUIZZES = seimbangkan_kuis(_JAVA_QUIZZES)
SQL_QUIZZES = seimbangkan_kuis(_SQL_QUIZZES)
PYTHON_QUIZZES = seimbangkan_kuis(_PYTHON_QUIZZES)
JAVASCRIPT_QUIZZES = seimbangkan_kuis(_JAVASCRIPT_QUIZZES)
C_QUIZZES = seimbangkan_kuis(_C_QUIZZES)
CPP_QUIZZES = seimbangkan_kuis(_CPP_QUIZZES)
BASH_QUIZZES = seimbangkan_kuis(_BASH_QUIZZES)
GO_QUIZZES = seimbangkan_kuis(_GO_QUIZZES)
HTML_QUIZZES = seimbangkan_kuis(_HTML_QUIZZES)
CSS_QUIZZES = seimbangkan_kuis(_CSS_QUIZZES)
CSHARP_QUIZZES = seimbangkan_kuis(_CSHARP_QUIZZES)
RUST_QUIZZES = seimbangkan_kuis(_RUST_QUIZZES)
PHP_QUIZZES = seimbangkan_kuis(_PHP_QUIZZES)
RUBY_QUIZZES = seimbangkan_kuis(_RUBY_QUIZZES)
KOTLIN_QUIZZES = seimbangkan_kuis(_KOTLIN_QUIZZES)
TYPESCRIPT_QUIZZES = seimbangkan_kuis(_TYPESCRIPT_QUIZZES)
VB_QUIZZES = seimbangkan_kuis(_VB_QUIZZES)
FEDORA_QUIZZES = seimbangkan_kuis(_FEDORA_QUIZZES)

__all__ = [
    "APLIKASI_MATERIALS", "APLIKASI_QUIZZES", "APLIKASI_EXERCISES",
    "JAVA_MATERIALS", "JAVA_QUIZZES", "JAVA_EXERCISES",
    "SQL_MATERIALS", "SQL_QUIZZES", "SQL_EXERCISES",
    "PYTHON_MATERIALS", "PYTHON_QUIZZES", "PYTHON_EXERCISES",
    "JAVASCRIPT_MATERIALS", "JAVASCRIPT_QUIZZES", "JAVASCRIPT_EXERCISES",
    "C_MATERIALS", "C_QUIZZES", "C_EXERCISES",
    "CPP_MATERIALS", "CPP_QUIZZES", "CPP_EXERCISES",
    "BASH_MATERIALS", "BASH_QUIZZES", "BASH_EXERCISES",
    "GO_MATERIALS", "GO_QUIZZES", "GO_EXERCISES",
    "HTML_MATERIALS", "HTML_QUIZZES", "HTML_EXERCISES",
    "CSS_MATERIALS", "CSS_QUIZZES", "CSS_EXERCISES",
    "CSHARP_MATERIALS", "CSHARP_QUIZZES", "CSHARP_EXERCISES",
    "RUST_MATERIALS", "RUST_QUIZZES", "RUST_EXERCISES",
    "PHP_MATERIALS", "PHP_QUIZZES", "PHP_EXERCISES",
    "RUBY_MATERIALS", "RUBY_QUIZZES", "RUBY_EXERCISES",
    "KOTLIN_MATERIALS", "KOTLIN_QUIZZES", "KOTLIN_EXERCISES",
    "TYPESCRIPT_MATERIALS", "TYPESCRIPT_QUIZZES", "TYPESCRIPT_EXERCISES",
    "VB_MATERIALS", "VB_QUIZZES", "VB_EXERCISES",
    "FEDORA_MATERIALS", "FEDORA_QUIZZES", "FEDORA_EXERCISES",
]
