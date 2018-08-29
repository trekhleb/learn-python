"""Unpacking Argument Lists

@see: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists

Unpacking arguments may be executed via * and ** operators. See below for further details.
"""


def test_function_unpacking_arguments():
    """Unpacking Argument Lists"""

    # The situation may occur when the arguments are already in a list or tuple but need to be
    # unpacked for a function call requiring separate positional arguments. For instance, the
    # built-in range() function expects separate start and stop arguments. If they are not
    # available separately, write the function call with the *-operator to unpack the arguments out
    # of a list or tuple:

    # Normal call with separate arguments:
    assert list(range(3, 6)) == [3, 4, 5]

    # Call with arguments unpacked from a list.
    arguments_list = [3, 6]
    assert list(range(*arguments_list)) == [3, 4, 5]

    # In the same fashion, dictionaries can deliver keyword arguments with the **-operator:
    def function_that_receives_names_arguments(first_word, second_word):
        return first_word + ', ' + second_word + '!'

    arguments_dictionary = {'first_word': 'Hello', 'second_word': 'World'}
    assert function_that_receives_names_arguments(**arguments_dictionary) == 'Hello, World!'
