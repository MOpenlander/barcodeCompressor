from compress import compress_to_byte
from decompress import decompress_from_byte


def run_tests():
    failed_tests = []
    with open('128Patterns.txt', 'r') as f:
        for pat in f:
            pat = pat.strip()
            compressed = compress_to_byte(pat)
            decompressed = decompress_from_byte(compressed)

            if not pat == decompressed:
                failed_tests.append(f'{pat}, {compressed.hex()}, {decompressed}, {pat == decompressed}')

    if len(failed_tests) <= 0:
        print('All tests passed')
    else:
        print(f'{len(failed_tests)} tests failed:')

        for f in failed_tests:
            print(f)


def print_compressed_table():
    with open('128Patterns.txt', 'r') as f:
        for pat in f:
            pat = pat.strip()
            compressed = compress_to_byte(pat)

            print(compressed.hex())


if __name__ == '__main__':
    run_tests()
    print_compressed_table()
