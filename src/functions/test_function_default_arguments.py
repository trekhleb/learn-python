"""Default Argument Values

@see: https://docs.python.org/3/tutorial/controlflow.html#default-argument-values

The most useful form is to specify a default value for one or more arguments. This creates a
function that can be called with fewer arguments than it is defined to allow.
"""


def power_of(number, power=2):
    """ Raises number to specific power.

    You may notice that by default the function raises number to the power of two.
    """
    return number ** power


def test_default_function_arguments():
    """Test default function arguments"""

    # This function power_of can be called in several ways because it has default value for
    # the second argument. First we may call it omitting the second argument at all.
    assert power_of(3) == 9
    # We may also want to override the second argument by using the following function calls.
    assert power_of(3, 2) == 9
    assert power_of(3, 3) == 27
