"""WHILE statement

@see: https://docs.python.org/3/tutorial/controlflow.html
@see: https://docs.python.org/3/reference/compound_stmts.html#the-while-statement

The while loop executes as long as the condition remains true. In Python, like in C, any
non-zero integer value is true; zero is false. The condition may also be a string or list
value, in fact any sequence; anything with a non-zero length is true, empty sequences are
false.

The test used in the example is a simple comparison. The standard comparison operators are
written the same as in C: < (less than), > (greater than), == (equal to), <= (less than or
equal to), >= (greater than or equal to) and != (not equal to).
"""


def test_while_statement():
    """WHILE statement"""

    # Let's raise the number to certain power using while loop.
    number = 2
    power = 5

    result = 1

    while power > 0:
        result *= number
        power -= 1

    # 2^5 = 32
    assert result == 32
