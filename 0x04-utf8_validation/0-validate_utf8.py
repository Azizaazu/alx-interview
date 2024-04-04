#!/usr/bin/python3
""" UTF-8 Validation module"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    bytes_left = 0

    for num in data:
        if bytes_left == 0:
            if (num >> 5) == 0b110:
                bytes_left = 1
            elif (num >> 4) == 0b1110:
                bytes_left = 2
            elif (num >> 3) == 0b11110:
                bytes_left = 3
            elif (num >> 7) == 0b0:
                bytes_left = 0
            else:
                return False
        else:
            if (num >> 6) != 0b10:
                return False
            bytes_left -= 1

    return bytes_left == 0
