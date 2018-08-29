"""Raising Exceptions.

@see: https://docs.python.org/3/tutorial/errors.html#raising-exceptions

The raise statement allows the programmer to force a specified exception to occur.
"""


def test_raise_exception():
    """Raising Exceptions.

    The raise statement allows the programmer to force a specified exception to occur.
    """
    exception_is_caught = False

    try:
        # The sole argument to raise indicates the exception to be raised. This must be either an
        # exception instance or an exception class (a class that derives from Exception). If an
        # exception class is passed, it will be implicitly instantiated by calling its constructor
        # with no arguments
        raise NameError('HiThere')  # shorthand for 'raise ValueError()'
    except NameError:
        exception_is_caught = True

    assert exception_is_caught


def test_user_defined_exception():
    """User-defined Exceptions"""

    # Programs may name their own exceptions by creating a new exception class. Exceptions should
    # typically be derived from the Exception class, either directly or indirectly.
    # Most exceptions are defined with names that end in “Error,” similar to the naming of the
    # standard exceptions. Many standard modules define their own exceptions to report errors
    # that may occur in functions they define.
    class MyCustomError(Exception):
        """Example of MyCustomError exception."""
        def __init__(self, message):
            super().__init__(message)
            self.message = message

    custom_exception_is_caught = False

    try:
        raise MyCustomError('My custom message')
    except MyCustomError:
        custom_exception_is_caught = True

    assert custom_exception_is_caught
