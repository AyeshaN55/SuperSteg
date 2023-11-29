"""
the module extract the message from a given image (of type carrier)
"""


def extract_msg(carrier):
    extracted_bytes = extract_bytes(carrier)
    msg = convert_to_txt(extracted_bytes)
    return msg


def extract_bytes(carrier):
    """
    :param carrier: obj of type Carrier representing the carrier image
    :return: extracted message (string)
    """
    byte_val = ''
    ascii_list = []
    bit_counter = 0
    for row in range(carrier.height):
        for col in range(carrier.width):
            for c in range(3):
                byte_val = byte_val + str(extract_LSB(carrier.mat[row][col][c]))
                bit_counter += 1
                if bit_counter == 8:
                    decimal_val = int(byte_val, 2)
                    if is_msg_end(decimal_val):
                        return ascii_list
                    else:
                        ascii_list.append(decimal_val)
                        byte_val = ''
                        bit_counter = 0


def is_msg_end(byte):
    return byte == ord('ÿ')


def extract_LSB(num):
    """
    :param num: decimal 8-bit integer
    :return: lsb
    """
    return 0 if num % 2 == 0 else 1


def convert_to_txt(ascii_list):
    """
    :param ascii_list: list of 8-bit integers representing ascii characters
    :return: extracted message (type string)
    """
    char_list = list(map(chr, ascii_list))
    return ''.join(char_list)
