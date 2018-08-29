"""Arithmetic operators

@see: https://www.w3schools.com/python/python_operators.asp

Arithmetic operators are used with numeric values to perform common mathematical operations
"""


def test_arithmetic_operators():
    """Arithmetic operators"""

    # Addition.
    assert 5 + 3 == 8

    # Subtraction.
    assert 5 - 3 == 2

    # Multiplication.
    assert 5 * 3 == 15
    assert isinstance(5 * 3, int)

    # Division.
    # Result of division is float number.
    assert 5 / 3 == 1.6666666666666667
    assert 8 / 4 == 2
    assert isinstance(5 / 3, float)
    assert isinstance(8 / 4, float)

    # Modulus.
    assert 5 % 3 == 2

    # Exponentiation.
    assert 5 ** 3 == 125
    assert 2 ** 3 == 8
    assert 2 ** 4 == 16
    assert 2 ** 5 == 32
    assert isinstance(5 ** 3, int)

    # Floor division.
    assert 5 // 3 == 1
    assert 6 // 3 == 2
    assert 7 // 3 == 2
    assert 9 // 3 == 3
    assert isinstance(5 // 3, int)
