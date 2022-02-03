import sys
import unittest
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import salsa20

# Optional crypto module to double check if my
# implementation results matches theirs. Disclaimer
# is that I am not sure how well vetted Cryptodome is
# except that it is active and relatively mature.
HAS_CRYPTO_MODULE = False
try:
    from Cryptodome.Cipher import Salsa20
    HAS_CRYPTO_MODULE = True
except ModuleNotFoundError as e:
    pass

class SalsaTest(unittest.TestCase):

    def test_quarterround(self):
        i0 = [0x00000000, 0x00000000, 0x00000000, 0x00000000]
        o0 = [0x00000000, 0x00000000, 0x00000000, 0x00000000]
        i1 = [0x00000001, 0x00000000, 0x00000000, 0x00000000]
        o1 = [0x08008145, 0x00000080, 0x00010200, 0x20500000]
        i2 = [0x00000000, 0x00000001, 0x00000000, 0x00000000]
        o2 = [0x88000100, 0x00000001, 0x00000200, 0x00402000]
        i3 = [0x00000000, 0x00000000, 0x00000001, 0x00000000]
        o3 = [0x80040000, 0x00000000, 0x00000001, 0x00002000]
        i4 = [0x00000000, 0x00000000, 0x00000000, 0x00000001]
        o4 = [0x00048044, 0x00000080, 0x00010000, 0x20100001]
        i5 = [0xe7e8c006, 0xc4f9417d, 0x6479b4b2, 0x68c67137]
        o5 = [0xe876d72b, 0x9361dfd5, 0xf1460244, 0x948541a3]
        i6 = [0xd3917c5b, 0x55f1c407, 0x52a58a7a, 0x8f887a3b]
        o6 = [0x3e2f308c, 0xd90a8f36, 0x6ab2a923, 0x2883524c]
        I = [i0, i1, i2, i3, i4, i5, i6]
        O = [o0, o1, o2, o3, o4, o5, o6]
        for idx, i in enumerate(I):
            o = salsa20.quarterround(i)
            self.assertEqual(o, O[idx])

    def test_columnround(self):
        i0 = [0x00000001, 0x00000000, 0x00000000, 0x00000000,
              0x00000001, 0x00000000, 0x00000000, 0x00000000,
              0x00000001, 0x00000000, 0x00000000, 0x00000000,
              0x00000001, 0x00000000, 0x00000000, 0x00000000]
        o0 = [0x10090288, 0x00000000, 0x00000000, 0x00000000,
              0x00000101, 0x00000000, 0x00000000, 0x00000000,
              0x00020401, 0x00000000, 0x00000000, 0x00000000,
              0x40a04001, 0x00000000, 0x00000000, 0x00000000]
        i1 = [0x08521bd6, 0x1fe88837, 0xbb2aa576, 0x3aa26365,
              0xc54c6a5b, 0x2fc74c2f, 0x6dd39cc3, 0xda0a64f6,
              0x90a2f23d, 0x067f95a6, 0x06b35f61, 0x41e4732e,
              0xe859c100, 0xea4d84b7, 0x0f619bff, 0xbc6e965a]
        o1 = [0x8c9d190a, 0xce8e4c90, 0x1ef8e9d3, 0x1326a71a,
              0x90a20123, 0xead3c4f3, 0x63a091a0, 0xf0708d69,
              0x789b010c, 0xd195a681, 0xeb7d5504, 0xa774135c,
              0x481c2027, 0x53a8e4b5, 0x4c1f89c5, 0x3f78c9c8]
        I = [i0, i1]
        O = [o0, o1]
        for idx, i in enumerate(I):
            o = salsa20.columnround(i)
            self.assertEqual(o, O[idx])

    def test_rowround(self):
        i0 = [0x00000001, 0x00000000, 0x00000000, 0x00000000,
              0x00000001, 0x00000000, 0x00000000, 0x00000000,
              0x00000001, 0x00000000, 0x00000000, 0x00000000,
              0x00000001, 0x00000000, 0x00000000, 0x00000000]
        o0 = [0x08008145, 0x00000080, 0x00010200, 0x20500000,
              0x20100001, 0x00048044, 0x00000080, 0x00010000,
              0x00000001, 0x00002000, 0x80040000, 0x00000000,
              0x00000001, 0x00000200, 0x00402000, 0x88000100]
        i1 = [0x08521bd6, 0x1fe88837, 0xbb2aa576, 0x3aa26365,
              0xc54c6a5b, 0x2fc74c2f, 0x6dd39cc3, 0xda0a64f6,
              0x90a2f23d, 0x067f95a6, 0x06b35f61, 0x41e4732e,
              0xe859c100, 0xea4d84b7, 0x0f619bff, 0xbc6e965a]
        o1 = [0xa890d39d, 0x65d71596, 0xe9487daa, 0xc8ca6a86,
              0x949d2192, 0x764b7754, 0xe408d9b9, 0x7a41b4d1,
              0x3402e183, 0x3c3af432, 0x50669f96, 0xd89ef0a8,
              0x0040ede5, 0xb545fbce, 0xd257ed4f, 0x1818882d]
        I = [i0, i1]
        O = [o0, o1]
        for idx, i in enumerate(I):
            o = salsa20.rowround(i)
            self.assertEqual(o, O[idx])

    def test_doubleround(self):
        i0 = [0x00000001, 0x00000000, 0x00000000, 0x00000000,
              0x00000000, 0x00000000, 0x00000000, 0x00000000,
              0x00000000, 0x00000000, 0x00000000, 0x00000000,
              0x00000000, 0x00000000, 0x00000000, 0x00000000]
        o0 = [0x8186a22d, 0x0040a284, 0x82479210, 0x06929051,
              0x08000090, 0x02402200, 0x00004000, 0x00800000,
              0x00010200, 0x20400000, 0x08008104, 0x00000000,
              0x20500000, 0xa0000040, 0x0008180a, 0x612a8020]
        i1 = [0xde501066, 0x6f9eb8f7, 0xe4fbbd9b, 0x454e3f57,
              0xb75540d3, 0x43e93a4c, 0x3a6f2aa0, 0x726d6b36,
              0x9243f484, 0x9145d1e8, 0x4fa9d247, 0xdc8dee11,
              0x054bf545, 0x254dd653, 0xd9421b6d, 0x67b276c1]
        o1 = [0xccaaf672, 0x23d960f7, 0x9153e63a, 0xcd9a60d0,
              0x50440492, 0xf07cad19, 0xae344aa0, 0xdf4cfdfc,
              0xca531c29, 0x8e7943db, 0xac1680cd, 0xd503ca00,
              0xa74b2ad6, 0xbc331c5c, 0x1dda24c7, 0xee928277]
        I = [i0, i1]
        O = [o0, o1]
        for idx, i in enumerate(I):
            o = salsa20.doubleround(i)
            self.assertEqual(o, O[idx])

    def test_littleendian(self):
        i0 = [0, 0, 0, 0]
        o0 = 0x00000000
        i1 = [86, 75, 30, 9]
        o1 = 0x091e4b56
        i2 = [255, 255, 255, 250]
        o2 = 0xfaffffff
        I = [i0, i1, i2]
        O = [o0, o1, o2]
        for idx, i in enumerate(I):
            o = salsa20.littleendian(i)
            self.assertEqual(o, O[idx])

    def test_littleendianinverse(self):
        i0 = 0
        o0 = [0, 0, 0, 0]
        i1 = 2830248557
        o1 = [109, 42, 178, 168]
        i2 = 4009291932
        o2 = [156, 240, 248, 238]
        I = [i0, i1, i2]
        O = [o0, o1, o2]
        for idx, i in enumerate(I):
            o = salsa20.littleendianinverse(i)
            self.assertEqual(o, O[idx])

    def test_salsa20hash(self):
        i0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        o0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        i1 = [211, 159, 13, 115, 76, 55, 82, 183, 3, 117, 222,
              37, 191, 187, 234, 136, 49, 237, 179, 48, 1, 106,
              178, 219, 175, 199, 166, 48, 86, 16, 179, 207,
              31, 240, 32, 63, 15, 83, 93, 161, 116, 147, 48,
              113, 238, 55, 204, 36, 79, 201, 235, 79, 3, 81,
              156, 47, 203, 26, 244, 243, 88, 118, 104, 54]
        o1 = [109, 42, 178, 168, 156, 240, 248, 238, 168, 196,
              190, 203, 26, 110, 170, 154, 29, 29, 150, 26, 150,
              30, 235, 249, 190, 163, 251, 48, 69, 144, 51, 57,
              118, 40, 152, 157, 180, 57, 27, 94, 107, 42, 236,
              35, 27, 111, 114, 114, 219, 236, 232, 135, 111,
              155, 110, 18, 24, 232, 95, 158, 179, 19, 48, 202]
        i2 = [88, 118, 104, 54, 79, 201, 235, 79, 3, 81, 156, 47,
              203, 26, 244, 243, 191, 187, 234, 136, 211, 159, 13,
              115, 76, 55, 82, 183, 3, 117, 222, 37, 86, 16, 179,
              207, 49, 237, 179, 48, 1, 106, 178, 219, 175, 199,
              166, 48, 238, 55, 204, 36, 31, 240, 32, 63, 15, 83,
              93, 161, 116, 147, 48, 113]
        o2 = [179, 19, 48, 202, 219, 236, 232, 135, 111, 155, 110,
              18, 24, 232, 95, 158, 26, 110, 170, 154, 109, 42, 178,
              168, 156, 240, 248, 238, 168, 196, 190, 203, 69, 144,
              51, 57, 29, 29, 150, 26, 150, 30, 235, 249, 190, 163,
              251, 48, 27, 111, 114, 114, 118, 40, 152, 157, 180,
              57, 27, 94, 107, 42, 236, 35]
        I = [i0, i1, i2]
        O = [o0, o1, o2]
        for idx, i in enumerate(I):
            o = salsa20.salsa20hash(i)
            self.assertEqual(o, O[idx])

    def test_salsa20_less_64(self):
        p = b"Don't roll your own Crypto! - Anonymous"
        k16 = b"[+6f%s@DOz1S)AIl"
        k32 = b"BFt%Am{_lszj0{^}mImc{H0fPO{(TI3y"
        n1 = b"U/\xf3\xa4\xd2\x00\xb2\xef"
        n2 = b" \xeb\x04\x1d%\xfe\x8c:"
        c1 = b'\xf7:\xb6\xd9\xe8\xa1\xff\x87P_\xdc\xfa\xd21\xb5q\xf6u\xa7n\xe1\xc4' + \
             b'\x0fMW!\x00K\x05\xdb"\x9d\xf39U&\x04\xa3c'
        c2 = b'j\xe1\xf6\x15\xb6\xf10,\xc1\x8b\xdf\xbe\xe6\x97\xab\xac\xb9\x96\x1e' + \
             b'\xe5\xd3\x97~\xba\xd6\xb1\\\x87wN|\xb0\xa8\x99\x9e\xc3\x91\x1fO'
        counter = 0
        K = [k16, k32]
        N = [n1, n2]
        C = [c1, c2]
        for i in range(len(K)):
            _c = salsa20.salsa20(p, K[i], N[i], counter)
            self.assertEqual(_c, C[i])
            _p = salsa20.salsa20(_c, K[i], N[i], counter)
            self.assertEqual(_p, p)
            if HAS_CRYPTO_MODULE:
                _cc = Salsa20.new(K[i], N[i]).encrypt(p)
                self.assertEqual(_cc, C[i])
                _pp = Salsa20.new(K[i], N[i]).decrypt(_cc)
                self.assertEqual(_pp, p)
                self.assertEqual(_pp, _p)
                self.assertEqual(_cc, _c)

    def test_salsa20_same_64(self):
        p = b"Cryptography is typically bypassed, not penetrated. - Adi Shamir"
        k16 = b"+7i7O_tLZ!%p_%Yw"
        k32 = b"_+92eF33yM1sj6Bx)q2(zFDh4*2zV#}*"
        n1 = b"\xb8\xcf\xc1\x18w[\xdc\x89"
        n2 = b"\xfb\x98\xc4x\x07m\xb8\xe2"
        c1 = b't\x9a\xa3\x86\xd56\xfb\xa5\x99\xb1\x8c\xa3\xe9\xa6\x8d$\x19>"6\xecXWU@' + \
             b'\x19\xb3\xa2\x0f\x0251R"\x1a}\xdc,\x10\xa9\xc8m\x95\xd7\xf1Z\xe9"&6_)' + \
             b'[v\xbd\xc0h$V\xac\n\xebv\xc4'
        c2 = b"\xcf\xf4wFb\x18\x13d\x9a\xa7\xb8l'\xa1YN\xc4{\x92IK\xd6y\xf6\xa7\xa0" + \
             b"\xdc\xe2\x03\x8e\xbcq\xd7G}J\x14\xb6\xed\x00\x0f\xcc\xc0K\x94\xd7\xc4" + \
             b"\xae$\x06\x9cwv=L\xeb4\xc0\x0c\x99\xf1\xc8\x06q"
        counter = 0
        K = [k16, k32]
        N = [n1, n2]
        C = [c1, c2]
        for i in range(len(K)):
            _c = salsa20.salsa20(p, K[i], N[i], counter)
            self.assertEqual(_c, C[i])
            _p = salsa20.salsa20(_c, K[i], N[i], counter)
            self.assertEqual(_p, p)
            if HAS_CRYPTO_MODULE:
                _cc = Salsa20.new(K[i], N[i]).encrypt(p)
                self.assertEqual(_cc, C[i])
                _pp = Salsa20.new(K[i], N[i]).decrypt(_cc)
                self.assertEqual(_pp, p)
                self.assertEqual(_pp, _p)
                self.assertEqual(_cc, _c)

    def test_salsa20_greater_64(self):
        p = b"Anyone who attempts to generate random numbers by deterministic means " + \
            b"is, of course, living in a state of sin. - John von Neumann"
        k16 = b"(8b#n[$6EY!{Ao&M"
        k32 = b"!(7sC!gaZgaMU)yteaj{#Jrr1ZpCFZWZ"
        n1 = b"_\xc6EP=\x1b\x82\x9d"
        n2 = b"\t\x15.R\xf7(a\xa0"
        counter = 0
        c1 = b"\xb9\xbd\x86\x92\xe4\xd7\x8d\xa11\xdej\x94\xd0\xb7{\x92\xe0A{\xa3" + \
             b"\xa3\xee\xcf#\xcdc\x95\xd3\x99\xe301\x03C\xe6\xf1\xf8\x04&f\xc1" + \
             b"\xe4\xa8\xf0H\x06\x08\xd9\x81J\x8f8k4M.\xfb_\xf6y\xe9\xb4xP3" + \
             b"\x8dVW\x1f\xfc#\x96_\x07\xacyJ\xf0\xa3\x93\xc4\xcek\xb2\x96" + \
             b"\xcf\x8f\x1a\x7f\xe8T\xe8K\x92n\xad\x8c+>d\x04\x9b&\xc43\xe6" + \
             b"\xce*o[8>H\xe3\xf4\xb0.\xb6ua\xda@Y7ti\x97\xd6\xe9"
        c2 = b'\x0fX|\xa5\x81{6ry\x14cD\xb7)H\r\xa4\t\xdd\xf8\xa7\x87\xbcz\xa6' + \
             b'\xb3{/\xed\xa9\xaa)\xee\xbc\xd12\xfb\x8d\x9a\x8c\x87I\xabs.Y\xbe' + \
             b'\xbc\xbc\x84\x1b^q\x8b\x94\x04\xd5\xeb\x84\xc7\xbc\xdf\xff\x14' + \
             b'\xaax\x19\xa8\x1dtW\x85.\x05\x04\x7f6Z\xa5\xe90~\x0b\xbag\xac7' + \
             b'\xb2\xd9\x8c\xbbJZv\xae\x0e"\x982u7\xa8\xf0IzR;\xb2\xad\xa4\x86' + \
             b'\x04\xf9k\x01m\xb9\xbc\x92\xd4\xd1\x11\xcf\xc6\xb9N\n\xac^'
        K = [k16, k32]
        N = [n1, n2]
        C = [c1, c2]
        for i in range(len(K)):
            _c = salsa20.salsa20(p, K[i], N[i], counter)
            self.assertEqual(_c, C[i])
            _p = salsa20.salsa20(_c, K[i], N[i], counter)
            self.assertEqual(_p, p)
            if HAS_CRYPTO_MODULE:
                _cc = Salsa20.new(K[i], N[i]).encrypt(p)
                self.assertEqual(_cc, C[i])
                _pp = Salsa20.new(K[i], N[i]).decrypt(_cc)
                self.assertEqual(_pp, p)
                self.assertEqual(_pp, _p)
                self.assertEqual(_cc, _c)

    def test_salsa20_greater_64_multiple(self):
        p = b"We shall go on to the end,we shall fight in France," + \
            b"we shall fight on the seas and oceans," + \
            b"we shall fight with growing confidence and growing " + \
            b"strength in the air,we shall defend our island,whatever " + \
            b"the cost may be,we shall fight on the beaches," + \
            b"we shall fight on the landing grounds," + \
            b"we shall fight in the fields and in the streets," + \
            b"we shall fight in the hills;" + \
            b"we shall never surrender. WC"
        k16 = b"y^SRv83pXYF89lV{"
        k32 = b"b@&hl3#64b^CoB(*7^H7[PMw@{P1[&R("
        n1 = b"\xde,\x0e\x15UeX\x12"
        n2 = b"z\n\xaf\x97\xd6[\xb20"
        c1 = b'2 ?E\x08\xb4\x11\x9e\xc8\xa5"\xc3]c\xa5\xe5\xc3\xf2\xcc\xdb\xeb' + \
             b'\xabf9X*\x84\xf87\xe1\x18Y\n\xcfO\xdf\xb7\x14\xd5r\xd1\xf7\x8c\xd7' + \
             b'\xb0JZNl\xaa\xaf\x94\x89\xbc?T\x90\xffRn6\xe1K\xa3\x7f\x8d\xe7\xdc' + \
             b'\xe9\xe4>\xb8\x99\xb15\xb5\x9b\xb5\x94\xc1\xef\xe3\x10U\x1e\x87{m@' + \
             b'\x82(\x16+^\xd7afd\x1e\x9cY\xd7\xdd\xaa\x01\x00b\x8c\xb3q\x80\x8b' + \
             b'\xf7\x0cT\xcb\x18y\x92\xb4\xfb$\xa9>3Mg\xee}\xdb\x02\xf9;\xa7\x01' + \
             b'\x92\xaa\x86\x7fS\xe5\xcc}\xbe\x19\xe4\xfc\xedi\x8d\xf58f\xd7\xce' + \
             b'\xcc\x0f\x17J\xb0@\x10^$ \xdc\xbf\xd3\x10!7E\xa5_\xa83E\xa1$&\xed5' + \
             b'\x16/\x00\x944\xc4\x9fE\x173\x15\xc9?\x1aO\x81\xd3\xc4\xe3\xc5^\xae' + \
             b'\xe8\xff\xed$\xa9\xa2HK\x96\n\xaf\xfa\xb0M\x90\x87vMy\xff\x86)g\xc4' + \
             b'\x8e/P\xd4\x846\x15\xef\xe2"\xfbi\xe3\x98\xd1\x04\xdd\xc5s\xf0\xc6m' + \
             b'\xb8\xa2\xbc\xb1sT\x15\xef5f\xbd\x9cX\x83\x90\xce\xdf\x95\xd7\xc8\x96' + \
             b'\xa7gy\xc7\xf8z!\xf1\xea}\xff-\xd9\xd9\xaf\xd7V\xf2A\x1b\xfeC\x1a\xa4' + \
             b'\xf0\xd1`\x176\xc4\x14\x82\xa3\x1eUx}_\xe2#:4}\x11x\xc69\x8e\xfd\x9c' + \
             b'\x05\x9f\xa2\xd5\x98c@\x10\x9f\xf2\xe9!\x80@6\x7fDm\xee3\x9bav.\xc1' + \
             b'\x1e\x1d\x84\xb3\xe8\x81&Sk\xf3\xda\x0c\x00\xf7\xef\x0c\xc8\x1f*f\xa7' + \
             b'\xb9\x9f\x11\x1f\x17\xa3\x8f\xc0\x8f|(\x04ZW\x17Fo'
        c2 = b' \xbf\x97\x82\x94\xee`G\xf76z_r9?\x98\x95H\x88\x0f|\x87P^F\xe7T\x8dY' + \
             b'\xaa\xcd\x88d\xbfY+\xc6\xcd\x1c\xc8\xcf\x06\x9bMl#~\x86\xd3\xec\xfa' + \
             b'\xbb\x12\xeez\xdc\xa06\xbc\xda_\x14k`\xfb\xc8U\xc4\xc8\x01\x03b&\xd8' + \
             b'\x16;x\xf9C\x84\x1e\xcc\xb1\xd2"7`\x83\x94\x8d\x81\xab\x8a\xd6\x97' + \
             b'\xa9>\xc0G\xa9\xc6\xad\x97#ANpY\xce\x05\xd9au\x84\xaaH\x0e:o\'\x1a' + \
             b'\xe7G\xa9\xbbm\xf0\xd7"~hk\xc7\xde\xa5\x85\xd8\x13\xc2\x99\x88>]\xeb' + \
             b'\xa6g\xc7\xf9\xf6\xebg\xd5\x1do\xcb\x84\x12j\xe6\x9c\xd2\xb3\x07:\xd2' + \
             b'\x18\xf8\x98gE\xee\x82\xb1\xb0\xf8"\x08\x038\xe1\xf1\x83\x90\x99\xad' + \
             b'\xbd`\xfaYv\xb0 \xe9{0m\x1a\x8d\x03\x1f3\xd5\x9b\x01\nty\x81\tqv\xe3' + \
             b'\x1cy\x1fH\x12\xf6\xbe\xe6.WR\xda\xbf\xf1\x0e\xbd\xe7\xe9\xf13V\x1d' + \
             b'\xfa\x9bO!\xb9\x0bq\\,#\x0c\xb5\xca\x9b2\x13\xf9A(jjY\xfa\xd5\'j\xc8' + \
             b'\xc1\x13\xa1|\xff\xe6\xcf\x96\xa36\x84\xd3{\xdf\xf0\xbfc\xd2\x83\xde1' + \
             b'\xfe\x81\x9c\x99\xf1\x89=\x87\x94\xab\xf7\xc9\xc8\xfd\xc7\xc6\xa0\x99' + \
             b'\xa5\x84x~>\xf9\xca\xc94\x15\xe5\r)\x89\x90\xf5\xb4\x8d\x0eY.\xed6\xf77' + \
             b'\xeb\xd9v\x82\'\x8bS%1Ekb\xf8dU\x83\xc9\xe4Q\xab\xf0\xf5\xbb\xc9\xd4' + \
             b'\xada\xd8s\x0e\x13\x05\x81\x95\xa1\x00\xaf\xd6\x03=\x85;\xa3\r' + \
             b'\x13[\\j!\xc8\xb1\xd7\xa0\x90^\xce\xcc\x119'
        counter = 0
        K = [k16, k32]
        N = [n1, n2]
        C = [c1, c2]
        for i in range(len(K)):
            _c = salsa20.salsa20(p, K[i], N[i], counter)
            self.assertEqual(_c, C[i])
            _p = salsa20.salsa20(_c, K[i], N[i], counter)
            self.assertEqual(_p, p)
            if HAS_CRYPTO_MODULE:
                _cc = Salsa20.new(K[i], N[i]).encrypt(p)
                self.assertEqual(_cc, C[i])
                _pp = Salsa20.new(K[i], N[i]).decrypt(_cc)
                self.assertEqual(_pp, p)
                self.assertEqual(_pp, _p)
                self.assertEqual(_cc, _c)

    def test_salsa20_greater_64_counter(self):
        p = b"A" * 10
        k16 = b"ZcFm#EaY42X#pXrv"
        k32 = b"iCX*4Mh@GXCo_g4hl(76OA}}yo]6Z2uv"
        n = b"F\xac\xa4\xa7\xc60L\xb6"
        c16 = [b'\xc8\x01!\xee\x99\xec\xa5\xf8\xa4\xcd',
               b'\xc8\x01!\xee\x99\xec\xa5\xf8\xa4',
               b'\xc8\x01!\xee\x99\xec\xa5\xf8',
               b'\xc8\x01!\xee\x99\xec\xa5',
               b'\xc8\x01!\xee\x99\xec',
               b'\xc8\x01!\xee\x99',
               b'\xc8\x01!\xee',
               b'\xc8\x01!',
               b'\xc8\x01',
               b'\xc8',
               b'']
        c32 = [b'#\xd5Q\xcaS[\xb2\xed\xf0J',
               b'#\xd5Q\xcaS[\xb2\xed\xf0',
               b'#\xd5Q\xcaS[\xb2\xed',
               b'#\xd5Q\xcaS[\xb2',
               b'#\xd5Q\xcaS[',
               b'#\xd5Q\xcaS',
               b'#\xd5Q\xca',
               b'#\xd5Q',
               b'#\xd5',
               b'#',
               b'']
        P = [b'AAAAAAAAAA',
             b'AAAAAAAAA',
             b'AAAAAAAA',
             b'AAAAAAA',
             b'AAAAAA',
             b'AAAAA',
             b'AAAA',
             b'AAA',
             b'AA',
             b'A',
             b'']
        K = [k16, k32]
        C = [c16, c32]
        print("")
        for i in range(len(K)):
            for counter in range(11):
                _c = salsa20.salsa20(p, K[i], n, counter)
                self.assertEqual(_c, C[i][counter])
                _p = salsa20.salsa20(_c, K[i], n, 0)
                self.assertEqual(_p, P[counter])

    def test_salsa20_generator(self):
        with open("shakespeare-plain.txt", "rb") as fd:
                p = fd.read()
        k = b"_+92eF33yM1sj6Bx)q2(zFDh4*2zV#}*"
        n = b"\xb8\xcf\xc1\x18w[\xdc\x89"
        for c in salsa20.salsa20generator(p, k, n, 0):
            pass

if __name__ == '__main__':
    unittest.main()
