#!/usr/bin/python3
"""UTF-8 validation module"""

# format -> [bit_mask, value_after_masking, num_of_cont_bits_to_validate]
head_bit_mask = [[128, 0, 0], [224, 192, 1], [240, 224, 2], [248, 240, 3],
                 [252, 248, 4], [254, 252, 5], 0]


def validUTF8(data):
    """UTF-8 validation function"""
    if len(data) == 0:
        return True

    def valid_continuation_bits(num):
        nonlocal byte_index
        for count in range(num):
            byte_index += 1
            if byte_index >= len(data) or 192 & data[byte_index] != 128:
                return False
        return True

    byte_index = 0
    while byte_index < len(data):
        for item in head_bit_mask:
            if item == 0:
                return False
            if data[byte_index] & item[0] == item[1]:
                if not valid_continuation_bits(item[2]):
                    return False
                break
        byte_index += 1
    return True
