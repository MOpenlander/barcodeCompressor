def compress(pattern: str) -> str:
    """Return the compressed version of a Code 128 symbol pattern"""
    # Remove the first and last two digits
    return pattern[1:9]


def decompress(pattern: str) -> str:
    """Return the decompressed version of a Code 128 symbol pattern"""
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


if __name__ == '__main__':
    with open('128Patterns.txt', 'r') as f:
        for pat in f:
            pat = pat.strip()
            compressed = compress(pat)
            decompressed = decompress(compressed)
            print(f'{pat}, {compressed}, {decompressed}, {pat == decompressed}')
