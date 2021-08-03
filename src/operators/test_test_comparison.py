"""Comparison operators

@see: https://www.w3schools.com/python/python_operators.asp

Comparison operators are used to compare two values.
"""


def test_test_comparison_operators():
    """Comparison operators"""

    # Equal.
    number = -100
    assert number == -100.0

    # Not equal.
    number = 5
    assert number != 5.1

    # Greater than.
    number = 5
    assert number > -1000

    # Less than.
    number = 5
    assert number < 1000000000000000000

    # Greater than or equal to
    number = 5
    assert number >= 5.00000000
    assert number >= 4.99999999999999999

    # Less than or equal to
    number = 5
    assert number <= 5
    assert number <= 6
