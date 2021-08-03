"""Assignment operators

@see: https://www.w3schools.com/python/python_operators.asp

Assignment operators are used to assign values to variables
"""


def test_test_assignment_operator():
    """Assignment operator """

    # Assignment: =
    number = -500
    assert number == -500

    # Multiple assignment.
    # The variables first_variable and second_variable simultaneously get the new values 0 and 1.
    first_variable, second_variable = 2220222.2002, 2
    assert first_variable == 2220222.2002
    assert second_variable == 2

    # You may even switch variable values using multiple assignment.
    first_variable, second_variable = second_variable, first_variable
    assert first_variable == 2
    assert second_variable == 2220222.2002


def test_test_augmented_assignment_operators():
    """Assignment operator combined with arithmetic and bitwise operators"""

    # Assignment: +=
    number = 5.2
    number += 3
    assert number == 8.2

    # Assignment: -=
    number = 5
    number -= 3
    assert number == 2.0

    # Assignment: *=
    number = 5.0
    number *= 3
    assert number == 15

    # Assignment: /=
    number = 8
    number /= 4
    assert number == 2

    # Assignment: %=
    number = 8
    number %= 3
    assert number == 2

    # Assignment: //=
    number = 99
    number //= 10
    assert number == 9

    # Assignment: **=
    number = 2
    number **= 5
    assert number == 32

    # Assignment: &=
    number = 5  # 0b0101
    number &= 3  # 0b0011
    assert number == 1  # 0b0001

    # Assignment: |=
    number = 5  # 0b0101
    number |= 3  # 0b0011
    assert number == 7  # 0b0111

    # Assignment: ^=
    number = 5  # 0b0101
    number ^= 3  # 0b0011
    assert number == 6  # 0b0110

    # Assignment: >>=
    number = 5
    number >>= 3
    assert number == 0  # (((5 // 2) // 2) // 2)

    # Assignment: <<=
    number = 5
    number <<= 3
    assert number == 40  # 5 * 2 * 2 * 2
