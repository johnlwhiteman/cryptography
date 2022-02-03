import argparse
import os
import secrets
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import salsa20

MSG    = "Don't roll your own Crypto!"
KEY16  = "Qk1gJ4[,wK84f7YN"
KEY32  = "RHrz29NzfVBksS}Q}3ARAGwXbWe.q.Id"
NONCE  = "7pwvG$T1"
BLKCNT = 0

parser = argparse.ArgumentParser( \
    prog = os.path.basename(__file__),
    description = "This script is used for testing salsa20.py",
    formatter_class = argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument("-c", "--counter", type=int, required=False,
                    default=BLKCNT,
                    help="Start block counter value")
parser.add_argument("-i", "--input", type=str,
                    help="Path to an input data file (optional)")
parser.add_argument("-K16", action="store_true",
                    help=f"Use the default 16-byte key: \"{KEY16}\"")
parser.add_argument("-K32", action="store_true",
                    help=f"Use the default 32-byte key: \"{KEY32}\"")
parser.add_argument("-k", "--key", type=str, required=False,
                    help="Supply your own secret 16/32 byte key")
parser.add_argument("-m", "--msg", type=str, required=False,
                    default=MSG,
                    help="Input plaintext/ciphertext")
parser.add_argument("-n", "--nonce", type=str, required=False,
                    default=NONCE,
                    help="Supply your own 8-byte nonce")
parser.add_argument("-o", "--output", type=str, required=False,
                    help="Path to an utput data file (optional)")
parser.add_argument("-r", "--rmsg", type=int, required=False,
                    help="Generate an auto random input message of -r [bytes]")
args = parser.parse_args()

def genRandomBytes(n):
    return secrets.token_bytes(n)

def toBytes(v):
    if not isinstance(v, bytes):
        return v.encode()
    return v

if __name__ == '__main__':
    n = args.nonce
    k = args.key
    if args.key:
        k = args.key
    elif args.K16:
        k = KEY16
    elif args.K32:
        k = KEY32
    else:
        print("You must provide a 16/32-byte -key or use the default -K16/K32 keys.")
        parser.print_usage()

        sys.exit(1)
    if args.rmsg:
        m = genRandomBytes(args.rmsg)
    elif args.input:
        with open(args.input, "rb") as fd:
            m = fd.read()
    else:
        m = args.msg
    c = int(args.counter)
    _m = salsa20.salsa20(toBytes(m),
                         toBytes(k),
                         toBytes(n),
                         c)
    if args.output:
        with open(args.output, "wb") as fd:
            m = fd.write(_m)
    print(f"""
[Input]:

{m}

[Output]:

{_m}

[Key]:     {k}
[Nonce]:   {n}
[Counter]: {c}
""")