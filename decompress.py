def decompress(pattern: str) -> str:
    """Return the decompressed version of a Code 128 symbol pattern"""
    # Special case for the stop sequence
    if pattern == '00000000':
        return '1100011101011'

    # Start with a 1
    d = "1"

    # Append the compressed pattern
    d += pattern

    # Count the number of 1s in the string
    num = d.count('1')

    # Append the next digit
    d += "0" if num % 2 == 0 else "1"

    # Append the trailing 0
    d += "0"

    return d


def decompress_from_byte(b: bytes) -> str:
    """Return the decompressed version of a Code 128 symbol pattern"""
    if b == b'':
        return decompress('00000000')

    p = ''
    for i in b:
        p += int_to_binary(i)

    return decompress(p)


def int_to_binary(n: int) -> str:
    """Converts an int to an 8-digit binary string"""
    binary_string = bin(n)[2:]

    while len(binary_string) < 8:
        binary_string = '0' + binary_string

    return binary_string
