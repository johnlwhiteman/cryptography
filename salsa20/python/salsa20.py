import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

ROUNDS      = 20
BLOCK_BYTES = 64
WORD_BITS   = 32
MOD_N       = (1 << WORD_BITS)
SIG = [[101, 120, 112, 97], # expa
       [110, 100, 32, 51],  # nd 3
       [50, 45, 98, 121],   # 2-by
       [116, 101, 32, 107]] # te k
TAU = [[101, 120, 112, 97], # expa
       [110, 100, 32, 49],  # nd 1
       [54, 45, 98, 121],   # 6-by
       [116, 101, 32, 107]] # te k

def _add(a, b):
    """
    Helper function that adds bits while keeping values within % MOD_N.
    """
    return (a + b) % MOD_N

def columnround(x):
    """
    If x is a 16-word sequence then columnround(x) is a 16-word sequence.
    This works on the columns only during the odd rounds.
    """
    y = [None] * 16
    y[0], y[4], y[8], y[12] = quarterround([x[0], x[4], x[8], x[12]])
    y[5], y[9], y[13], y[1] = quarterround([x[5], x[9], x[13], x[1]])
    y[10], y[14], y[2], y[6] = quarterround([x[10], x[14], x[2], x[6]])
    y[15], y[3], y[7], y[11] = quarterround([x[15], x[3], x[7], x[11]])
    return y

def doubleround(x):
    """
    If x is a 16-word sequence then doubleround(x) is a 16-word sequence.
    As the title shows, it does two rounds, first for the columns then
    for the rows. This function was described in the specification.
    """
    return rowround(columnround(x))

def littleendian(b):
    """
    If b is a 4-byte sequence then littleendian(b) is a word.
    """
    return b[0] ^ (b[1] << 8) ^ (b[2] << 16) ^ (b[3] << 24)

def littleendianinverse(w):
    """
    If w is an integer then littleendianinverse is a 4-byte word.
    This function is not explicitly defined in the specification
    except that an inverse of littleendian() is called after the
    rounds have been performed in the salsa20hash() function.
    """
    return [w & 0xff, (w >> 8) & 0xff, (w >> 16) & 0xff, (w >> 24) & 0xff]

def quarterround(y):
    """
    If y is a 4-word sequence then quarterround(y) is a 4-word sequence.
    This is the workhorse function that uses fast add-rotate-XOR (ARX)
    operations.
    """
    z = [None] * 4
    z[1] = y[1] ^ (_rotl(_add(y[0], y[3]), 7))
    z[2] = y[2] ^ (_rotl(_add(z[1], y[0]), 9))
    z[3] = y[3] ^ (_rotl(_add(z[2], z[1]), 13))
    z[0] = y[0] ^ (_rotl(_add(z[3], z[2]), 18))
    return z

def _rotl(a, b):
    """
    Helper function that rotates bits to the left while keeping
    values within MOD_N -1.
    """
    return ((a << b) | (a >> (WORD_BITS - b))) & (MOD_N - 1)

def rowround(y):
    """
    If y is a 16-word sequence then rowround(y) is a 16-word sequence.
    This works on the rows only during the even rounds.
    """
    z = [None] * 16
    z[0], z[1], z[2], z[3] = quarterround([y[0], y[1], y[2], y[3]])
    z[5], z[6], z[7], z[4] = quarterround([y[5], y[6], y[7], y[4]])
    z[10], z[11], z[8], z[9] = quarterround([y[10], y[11], y[8], y[9]])
    z[15], z[12], z[13], z[14] = quarterround([y[15], y[12], y[13], y[14]])
    return z

def _setCounter(c):
    """
    64-bits can hold ~18 quintillion or 1.8×1019 or 18446744073709551616
    or 2^64 blocks. If each block is 64 bytes or 512 bits, then total
    data is (512 * 2^64 - 1) bits or
    18446744073709551616-1 = [255, 255, 255, 255, 255, 255, 255, 255]
    18446744073709551616 = [0, 0, 0, 0, 0, 0, 0, 0]
    Warning: The nonce needs to be refreshed before this counter reaches 2^64
    """
    return [(c) & 0xff, (c >> 8) & 0xff, (c >> 16) & 0xff,
            (c >> 24) & 0xff, (c >> 32) & 0xff, (c >> 40) & 0xff,
            (c >> 48) & 0xff, (c >> 56) & 0xff]

def _setinternalstate(k, n, c):
    """
    This is a helper function that handles state initialization and updates.
    There are better ways to implement this in python but I wanted to
    layout the structures in a visual way represented in the internal matrix.
    Salsa20 does not use a S-box component like AES.
    """
    if len(k) == 16:
        state = [TAU[0], k[:4], k[4:8], k[8:12],
                 k[12:16], TAU[1], n[:4], n[4:8],
                 c[:4], c[4:8], TAU[2], k[:4],
                 k[4:8], k[8:12], k[12:16], TAU[3]]
    else:
        state = [SIG[0], k[:4], k[4:8], k[8:12],
                 k[12:16], SIG[1], n[:4], n[4:8],
                 c[:4], c[4:8], SIG[2], k[16:20],
                 k[20:24], k[24:28], k[28:32], SIG[3]]
    return [ss for s in state for ss in s]

def salsa20(plaintext, key, nonce, counter=0):
    """
    Entry point for the cipher. The paper calls it the encryption
    function but by symmetric design it works for encryption and
    decryption when the same key, nonce and counter are used.
    Plaintext can be any size but works on 64-byte blocks of data.
    Key must be 16 bytes or 32 bytes. Other key sizes will fail here.
    Nonce is 8 bytes. Other nonce sizes will fail here. Keep your
    nonces randomly unique and you'll have no problems. The counter
    here refers to the block offset. This means that you can go
    directly to a given block by factor of 64 bytes. The default
    value is zero. There are no dependencies with the previous
    blocks. One can encrypt/decrypt starting anywhere within
    the length of the input. No checks are made if counter
    is greater than total 64-byte block size. All input
    values except the counter are Python bytes, not strings.
    Please see source examples in tests.py, client.py and
    sample.py to see how to properly call this function
    with the right data types. The counter is a simple
    integer of >= 0. One potential issue with this function
    is that the entire content is being stored in memory
    where ciphertext.extend() is being called. A better
    approach would be to use a python generator with yield
    to work on each block, one-by-one (max=64 bytes). The
    caller would have to handle the actual interation.
    """
    c = 0
    ciphertext = []
    for curBlk in range(counter, len(plaintext), BLOCK_BYTES):
        state = _setinternalstate(list(key), list(nonce), _setCounter(c))
        block = plaintext[curBlk:curBlk+BLOCK_BYTES]
        ciphertext.extend([k ^ p for k, p in zip(salsa20hash(state), block)])
        c += 1
    return bytes(ciphertext)

def salsa20generator(plaintext, key, nonce, counter=0):
    """
    An optional alternative to salsa20 where this reduces memory consumption.
    This is not really in the specification but for experimentation purposes.
    """
    c = 0
    ciphertext = []
    for curBlk in range(counter, len(plaintext), BLOCK_BYTES):
        state = _setinternalstate(list(key), list(nonce), _setCounter(c))
        block = plaintext[curBlk:curBlk+BLOCK_BYTES]
        yield bytes([k ^ p for k, p in zip(salsa20hash(state), block)])
        c += 1

def salsa20hash(x):
    """
    If x is a 64-byte sequence then salsa20hash(x) is a 64-byte sequence.
    This is not an actual hash function like a cryptographic digest. Notice
    that ROUNDS is divided by 2. ROUNDS equals 20. The doubleround()
    function does two round operations against the columns and rows so
    that is why we are iterating by half. Other rounds counts have
    not been tested. The global ROUND can be change internally.
    """
    h = [0] * 16
    j = 0
    for i in range(16):
        h[i] = littleendian([x[j], x[j + 1], x[j + 2], x[j + 3]])
        j += 4
    z = h
    for j in range(ROUNDS//2):
        z = doubleround(z)
    return [w for i in range(16) for w in littleendianinverse(z[i] + h[i])]

if __name__ == "__main__":
    pass