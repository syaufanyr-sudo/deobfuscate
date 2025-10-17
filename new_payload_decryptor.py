import base64
import zlib

# ==============================================================================
# SCRIPT INI AMAN. SCRIPT INI HANYA MENDEKODE DAN MENULIS TEKS KE FILE,
# TIDAK MENJALANKAN LOGIKA BERBAHAYANYA.
# ==============================================================================

# 1. Salin string payload yang sangat panjang dari variabel I11IlIl1lI1
# di kode asli Anda.
payload_compressed_b64 = "eJwkmkdv81BzRv/Kt8uCL3DZC4IsJFHsT..........................................."

# Nama file output untuk menyimpan payload yang telah didekripsi
output_filename = "decrypt_payload_new"

try:
    # 2. Decode string dari Base64 menjadi bytes
    payload_compressed_bytes = base64.b64decode(payload_compressed_b64)

    # 3. Dekompres bytes menggunakan zlib untuk mendapatkan kode asli (string)
    payload_code = zlib.decompress(payload_compressed_bytes).decode()

    # 4. Tulis kode payload yang sebenarnya ke dalam file
    # Menggunakan 'with open' adalah cara yang aman untuk menangani file
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(payload_code)

    # 5. Tampilkan pesan sukses di konsol
    print(f"✅ Payload berhasil didekripsi dan disimpan ke file: '{output_filename}'")

except Exception as e:
    print(f"❌ Terjadi kesalahan saat mendekode atau menulis payload: {e}")
