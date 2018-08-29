"""Data Compression.

@see: https://docs.python.org/3/tutorial/stdlib.html#data-compression

Common data archiving and compression formats are directly supported by modules including: zlib,
gzip, bz2, lzma, zipfile and tarfile.
"""

import zlib


def test_zlib():
    """zlib."""
    string = b'witch which has which witches wrist watch'
    assert len(string) == 41

    zlib_compressed_string = zlib.compress(string)
    assert len(zlib_compressed_string) == 37

    zlib_decompressed_string = zlib.decompress(zlib_compressed_string)
    assert zlib_decompressed_string == b'witch which has which witches wrist watch'

    assert zlib.crc32(string) == 226805979
