def compress(pattern: str) -> str:
    """Return the compressed version of a Code 128 symbol pattern"""
    # Remove the first and last two digits
    return pattern[1:9] if len(pattern) == 11 else '00000000'


def compress_to_byte(pattern: str) -> bytes:
    """Return the compressed version of a Code 128 symbol pattern as a byte"""
    return bitstring_to_bytes(compress(pattern))


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
    p = ''
    for i in b:
        p += int_to_binary(i)

    return decompress(p)


# https://stackoverflow.com/a/32676625/11102945
def bitstring_to_bytes(s: str) -> bytes:
    """Takes a bitstring of 1s and 0s and converts it into bytes object"""
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])


def int_to_binary(n: int) -> str:
    """Converts an int to an 8-digit binary string"""
    binary_string = bin(n)[2:]

    while len(binary_string) < 8:
        binary_string = '0' + binary_string

    return binary_string


if __name__ == '__main__':
    with open('128Patterns.txt', 'r') as f:
        for pat in f:
            pat = pat.strip()
            compressed = compress_to_byte(pat)
            decompressed = decompress_from_byte(compressed)
            print(f'{pat}, {compressed.hex()}, {decompressed}, {pat == decompressed}')
