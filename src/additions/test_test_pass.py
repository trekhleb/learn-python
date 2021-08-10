"""PASS statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The pass statement does nothing. It can be used when a statement is required syntactically but
the program requires no action.
"""


def test_pass_function():
    pass


def test_pass_in_loop():
    """PASS in loops.

    "Pass" can be used when a statement is required syntactically but the program requires no
    action. For example:
    """

    # pylint: disable=unused-variable
    for number in range(100):
        # It just don't do anything but for loop is still valid.
        pass

    if 2 < 5:
        pass

    try:
        pass
    except:
        pass

    try:
        assert True == False
    except Exception:
        pass


# pylint: disable=too-few-public-methods
class MyEmptyClass:
    pass
