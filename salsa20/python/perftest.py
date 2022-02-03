import secrets
import time
import sys
import salsa20

try:
    from memory_profiler import profile
except:
    print("You must run pip install -r requirements.txt first to use this.")
    sys.exit(1)

KEY     = b"_+92eF33yM1sj6Bx)q2(zFDh4*2zV#}*"
NONCE   = b"\xb8\xcf\xc1\x18w[\xdc\x89"
COUNTER = 0

def loadData():
    return secrets.token_bytes(999999)

@profile
def _salsa20():
    a = time.time()
    c = salsa20.salsa20(loadData(), KEY, NONCE, COUNTER)
    return time.time() - a

@profile
def _salsa20generator():
    a = time.time()
    x = []
    for c in salsa20.salsa20generator(loadData(), KEY, NONCE, COUNTER):
        x.append(x)
    return time.time() - a

def main():
    print("Hang out ... this may take up to a few minutes.")
    a = _salsa20()
    b = _salsa20generator()
    print(f"salsa20():          {a} secs")
    print(f"salsa20generator(): {b} secs")

if __name__ == '__main__':
    main()