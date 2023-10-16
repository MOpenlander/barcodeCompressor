def compress(pattern: str) -> str:
    """Return the compressed version of a Code 128 symbol pattern"""
    # Remove the first and last two digits
    return pattern[1:9] if len(pattern) == 11 else '00000000'


def compress_to_byte(pattern: str) -> bytes:
    """Return the compressed version of a Code 128 symbol pattern as a byte"""
    return bitstring_to_bytes(compress(pattern))


# https://stackoverflow.com/a/32676625/11102945
def bitstring_to_bytes(s: str) -> bytes:
    """Takes a bitstring of 1s and 0s and converts it into bytes object"""
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b[::-1])
