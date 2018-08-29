"""PASS statement

@see: https://docs.python.org/3/tutorial/controlflow.html

The pass statement does nothing. It can be used when a statement is required syntactically but
the program requires no action.
"""


def test_pass_in_function():
    """PASS statement in function

    "Pass" can be used as a place-holder for a function or conditional body when you are working on
    new code, allowing you to keep thinking at a more abstract level.

    The pass statement below is silently ignored but it makes current test_pass() function valid.
    """
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

    # Example above is quite useless but it was given just for illustration of the idea.
    # The more useful example might be:
    #
    # while True:
    #   pass  # Busy-wait for keyboard interrupt (Ctrl+C)


# pylint: disable=too-few-public-methods
class MyEmptyClass:
    """PASS statement in class

    "Pass" is commonly used for creating minimal classes like current one.
    """
    pass
