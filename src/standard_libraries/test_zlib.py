"""Data Compression.

@see: https://docs.python.org/3/tutorial/stdlib.html#data-compression

Common data archiving and compression formats are directly supported by modules including: zlib,
gzip, bz2, lzma, zipfile and tarfile.
"""

import zlib


def test_zlib():
    """Tests compression, decompression, and CRC32 checksum using zlib."""
    string = b'witch which has which witches wrist watch'
    assert len(string) == 41

    zlib_compressed_string = zlib.compress(string)
    assert len(zlib_compressed_string) < len(string)
    
    original_data = b'witch which has which witches wrist watch'
    compressed_data = zlib.compress(original_data)
    decompressed_data = zlib.decompress(compressed_data)

    assert zlib.crc32(string) == 226805979
