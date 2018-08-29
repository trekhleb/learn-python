"""CONTINUE statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The continue statement is borrowed from C, continues with the next iteration of the loop.
"""


def test_continue_statement():
    """CONTINUE statement in FOR loop"""

    # Let's

    # This list will contain only even numbers from the range.
    even_numbers = []
    # This list will contain every other numbers (in this case - ods).
    rest_of_the_numbers = []

    for number in range(0, 10):
        # Check if remainder after division is zero (which would mean that number is even).
        if number % 2 == 0:
            even_numbers.append(number)
            # Stop current loop iteration and go to the next one immediately.
            continue

        rest_of_the_numbers.append(number)

    assert even_numbers == [0, 2, 4, 6, 8]
    assert rest_of_the_numbers == [1, 3, 5, 7, 9]
