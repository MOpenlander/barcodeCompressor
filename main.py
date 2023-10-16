from compress import compress_to_byte
from decompress import decompress_from_byte

if __name__ == '__main__':
    with open('128Patterns.txt', 'r') as f:
        for pat in f:
            pat = pat.strip()
            compressed = compress_to_byte(pat)
            decompressed = decompress_from_byte(compressed)
            print(f'{pat}, {compressed.hex()}, {decompressed}, {pat == decompressed}')
