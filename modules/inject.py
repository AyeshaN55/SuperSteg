import numpy as np


def inject(carrier, msg):
    bit_counter = 0
    for row in range(carrier.height):
        for col in range(carrier.width):
            if bit_counter >= msg.size:
                # run as long as there are bits to inject
                return
            carrier.mat[row][col] = set_pixel(carrier.mat[row][col], msg.bit_list[bit_counter:bit_counter + 3])
            bit_counter += 3


def set_pixel(pixel, bits):
    while bits.size < 3:
        bits = np.append(bits, 1)
    new_pixel = (pixel & 0b11111110) | bits
    # new_pixel = (pixel & 0b01111111) | bits << 7  # uncomment for setting MSBs (for testing)
    return new_pixel
