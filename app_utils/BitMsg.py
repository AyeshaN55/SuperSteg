import numpy as np


class BitMsg:
    def __init__(self, msg):
        char_list = [bin(ord(c))[2:].zfill(8) for c in msg]  # from char to decimal
        bit_list = ''.join(char_list)               # from decimal to binary
        self.bit_list = np.array([int(b) for b in bit_list])  # from binary to bits
        self.size = len(self.bit_list)
