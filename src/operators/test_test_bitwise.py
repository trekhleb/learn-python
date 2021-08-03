"""Bitwise operators

@see: https://www.w3schools.com/python/python_operators.asp

Bitwise operators manipulate numbers on bit level.
"""


def test_test_bitwise_operators():
    """Bitwise operators"""

    # AND
    # Sets each bit to 1 if both bits are 1.
    #
    # Example:
    # 7 = 0b1111
    # 3 = 0b0011
    assert 7 & 3 == 3  # 0b0011

    # OR
    # Sets each bit to 1 if one of two bits is 1.
    #
    # Example:
    # 7 = 0b1111
    # 5 = 0b0101
    assert 7 | 5 == 7  # 0b1111

    # NOT
    # Inverts all the bits.
    # 3 = 0b0011
    # ~3 = 0b1100 = -4
    assert ~3 == -4

    # XOR
    # Sets each bit to 1 if only one of two bits is 1.
    #
    # Example:
    # 5 = 0b0101
    # 3 = 0b0011
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert 5 ^ 3 == 6  # 0b0110

    # Signed right shift
    # Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost
    # bits fall off.
    #
    # Example:
    # 8 = 0b1000
    assert 8 >> 1 == 4  # 0b0100
    assert 8 >> 2 == 2  # 0b0010

    # Zero fill left shift
    # Shift left by pushing zeros in from the right and let the leftmost bits fall off.
    #
    # Example:
    # 2 = 0b0010
    assert 2 << 1 == 4  # 0b0100
    assert 2 << 2 == 8  # 0b1000
