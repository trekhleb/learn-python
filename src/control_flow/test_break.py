"""BREAK statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The break statement, like in C, breaks out of the innermost enclosing "for" or "while" loop.
"""


def test_break_statement():
    """BREAK statement"""

    # Let's terminate the loop in case if we've found the number we need in a range from 0 to 100.
    number_to_be_found = 42
    # This variable will record how many time we've entered the "for" loop.
    number_of_iterations = 0

    for number in range(100):
        if number == number_to_be_found:
            # Break here and don't continue the loop.
            break
        else:
            number_of_iterations += 1

    # We need to make sure that break statement has terminated the loop once it found the number.
    assert number_of_iterations == 42
