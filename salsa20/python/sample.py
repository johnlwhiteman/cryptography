import salsa20
import sys

MSG = b"Cryptography is typically bypassed, not penetrated. - Adi Shamir"
KEY = "RHrz29NzfVBksS}Q}3ARAGwXbWe.q.Id"
NONCE = "7pwvG$T1"
COUNTER = 0

def toBytes(v):
    if not isinstance(v, bytes):
        return v.encode()
    return v

print("Encryption\n")
print(MSG)
c = salsa20.salsa20(toBytes(MSG),
                    toBytes(KEY),
                    toBytes(NONCE),
                    COUNTER)
print(c)
print("\nDecryption\n")
p = salsa20.salsa20(c,
                    toBytes(KEY),
                    toBytes(NONCE),
                    COUNTER)
print(p)
print("\nGenerator Encryption w/MSG * 2\n")
for c in salsa20.salsa20generator(toBytes(MSG*2),
                                  toBytes(KEY),
                                  toBytes(NONCE),
                                  COUNTER):
    print(c)
print("\nCounter Manipulation\n")
for counter in range(0, len(MSG)):
    c = salsa20.salsa20(toBytes(MSG),
                        toBytes(KEY),
                        toBytes(NONCE),
                        counter)
    p = salsa20.salsa20(c,
                        toBytes(KEY),
                        toBytes(NONCE),
                        0)
    print(f"----------")
    print(f"Block: {counter}")
    print(c)
    print(p)