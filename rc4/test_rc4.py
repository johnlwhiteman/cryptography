from Crypto.Cipher import ARC4
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chisquare

matplotlib.use('Agg')

def analyze_rc4_bias(num_samples=1000, stream_length=256, key_length=16):

    def generate_keystreams(num_samples, stream_length, key_length):
        keystreams = []
        for _ in range(0, num_samples):
            key = np.random.bytes(key_length)
            cipher = ARC4.new(key)
            keystreams.append(cipher.encrypt(b'\x00' * stream_length))
        return keystreams

    def get_byte_bit_count(keystreams, byte_position):
        byte_bit_count = np.zeros(256)
        for stream in keystreams:
            byte_bit_count[stream[byte_position]] += 1
        return byte_bit_count

    keystreams = generate_keystreams(num_samples, stream_length, key_length)
    for byte_position in range(0, 3):
        byte_bit_count = get_byte_bit_count(keystreams, byte_position)
        chi2, p_value = chisquare(byte_bit_count, f_exp=[num_samples / 256] * 256)
        chi2 = "{:2e}".format(chi2)
        p_value = "{:2e}".format(p_value)
        print(f"Chi_square [{byte_position}]: {chi2}, p-value: {p_value}")
        plt.figure()  
        plt.bar(range(256), byte_bit_count)
        plt.ylim(top=1000)
        plt.title(f"Freq Distribution @ Byte Pos {byte_position+1} ({num_samples:,} samples)\nChi-Square: {chi2}, p-value: {p_value}")
        plt.xlabel("Byte Value")
        plt.ylabel("Frequecy")
        plt.savefig(f"plot_byte_pos_{byte_position+1}.png")

NUM_SAMPLES = 100000
STREAM_LENGTH = 256
KEY_LENGTH = 16

analyze_rc4_bias(num_samples=NUM_SAMPLES, stream_length=STREAM_LENGTH, key_length=KEY_LENGTH)
