"""Keyword Arguments

@see: https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments

Functions can be called using keyword arguments of the form kwarg=value.
"""

import pytest


def parrot(voltage, state='a stiff', action='voom', parrot_type='Norwegian Blue'):
    """Example of multi-argument function

    This function accepts one required argument (voltage) and three optional arguments
    (state, action, and type).
    """

    message = 'This parrot wouldn\'t ' + action + ' '
    message += 'if you put ' + str(voltage) + ' volts through it. '
    message += 'Lovely plumage, the ' + parrot_type + '. '
    message += 'It\'s ' + state + '!'

    return message


def test_function_keyword_arguments():
    """Test calling function with specifying keyword arguments"""

    # The parrot function accepts one required argument (voltage) and three optional arguments
    # (state, action, and type). This function can be called in any of the following ways:

    message = (
        "This parrot wouldn't voom if you put 1000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's a stiff!"
    )
    # 1 positional argument
    assert parrot(1000) == message
    # 1 keyword argument
    assert parrot(voltage=1000) == message

    message = (
        "This parrot wouldn't VOOOOOM if you put 1000000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's a stiff!"
    )
    # 2 keyword arguments
    assert parrot(voltage=1000000, action='VOOOOOM') == message
    # 2 keyword arguments
    assert parrot(action='VOOOOOM', voltage=1000000) == message

    # 3 positional arguments
    message = (
        "This parrot wouldn't jump if you put 1000000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's bereft of life!"
    )
    assert parrot(1000000, 'bereft of life', 'jump') == message

    # 1 positional, 1 keyword
    message = (
        "This parrot wouldn't voom if you put 1000 volts through it. "
        "Lovely plumage, the Norwegian Blue. "
        "It's pushing up the daisies!"
    )
    assert parrot(1000, state='pushing up the daisies') == message

    # But all the following calls would be invalid.

    with pytest.raises(Exception):
        # Required argument missing.
        # pylint: disable=no-value-for-parameter
        parrot()

    # Non-keyword argument after a keyword argument.
    # parrot(voltage=5.0, 'dead')

    with pytest.raises(Exception):
        # pylint: disable=redundant-keyword-arg
        parrot(110, voltage=220)

    with pytest.raises(Exception):
        # unknown keyword argument
        # pylint: disable=unexpected-keyword-arg,no-value-for-parameter
        parrot(actor='John Cleese')

    # In a function call, keyword arguments must follow positional arguments. All the keyword
    # arguments passed must match one of the arguments accepted by the function (e.g. actor is not
    # a valid argument for the parrot function), and their order is not important. This also
    # includes non-optional arguments (e.g. parrot(voltage=1000) is valid too). No argument may
    # receive a value more than once. Here’s an example that fails due to this restriction:
    def function_with_one_argument(number):
        return number

    with pytest.raises(Exception):
        # pylint: disable=redundant-keyword-arg
        function_with_one_argument(0, number=0)

    # When a final formal parameter of the form **name is present, it receives a dictionary
    # containing all keyword arguments except for those corresponding to a formal parameter.
    # This may be combined with a formal parameter of the form *name which receives a tuple
    # containing the positional arguments beyond the formal parameter list.
    # (*name must occur before **name.) For example, if we define a function like this:
    def test_function(first_param, *arguments, **keywords):
        """This function accepts its arguments through "arguments" tuple amd keywords dictionary."""
        assert first_param == 'first param'
        assert arguments == ('second param', 'third param')
        assert keywords == {
            'fourth_param_name': 'fourth named param',
            'fifth_param_name': 'fifth named param'
        }

    test_function(
        'first param',
        'second param',
        'third param',
        fourth_param_name='fourth named param',
        fifth_param_name='fifth named param',
    )
