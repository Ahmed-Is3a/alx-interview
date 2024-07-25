#!/usr/bin/python3
""" UTF-8 falidation """


def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # For each integer in the data list
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of 1's at the beginning of the byte
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character
            if num_bytes == 0:
                continue

            # If the byte indicates a character longer than 4 bytes
            # or only 10xxxxxx is invalid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte is of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1
    return num_bytes == 0
