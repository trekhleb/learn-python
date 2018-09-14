"""Tuples.

@see: https://www.w3schools.com/python/python_tuples.asp
@see: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

A tuple is a collection which is ordered and unchangeable. In Python tuples are written with
round brackets.

The Tuples have following properties:
- You cannot change values in a tuple.
- You cannot remove items in a tuple.
"""

import pytest


def test_tuples():
    """Tuples"""
    fruits_tuple = ("apple", "banana", "cherry")

    assert isinstance(fruits_tuple, tuple)
    assert fruits_tuple[0] == "apple"
    assert fruits_tuple[1] == "banana"
    assert fruits_tuple[2] == "cherry"

    # You cannot change values in a tuple.
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        fruits_tuple[0] = "pineapple"

    # It is also possible to use the tuple() constructor to make a tuple (note the double
    # round-brackets).
    # The len() function returns the length of the tuple.
    fruits_tuple_via_constructor = tuple(("apple", "banana", "cherry"))

    assert isinstance(fruits_tuple_via_constructor, tuple)
    assert len(fruits_tuple_via_constructor) == 3

    # It is also possible to omit brackets when initializing tuples.
    another_tuple = 12345, 54321, 'hello!'
    assert another_tuple == (12345, 54321, 'hello!')

    # Tuples may be nested:
    nested_tuple = another_tuple, (1, 2, 3, 4, 5)
    assert nested_tuple == ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

    # As you see, on output tuples are always enclosed in parentheses, so that nested tuples are
    # interpreted correctly; they may be input with or without surrounding parentheses, although
    # often parentheses are necessary anyway (if the tuple is part of a larger expression). It is
    # not possible to assign to the individual items of a tuple, however it is possible to create
    # tuples which contain mutable objects, such as lists.

    # A special problem is the construction of tuples containing 0 or 1 items: the syntax has some
    # extra quirks to accommodate these. Empty tuples are constructed by an empty pair of
    # parentheses; a tuple with one item is constructed by following a value with a comma (it is
    # not sufficient to enclose a single value in parentheses). Ugly, but effective. For example:
    empty_tuple = ()
    # pylint: disable=len-as-condition
    assert len(empty_tuple) == 0

    # pylint: disable=trailing-comma-tuple
    singleton_tuple = 'hello',  # <-- note trailing comma
    assert len(singleton_tuple) == 1
    assert singleton_tuple == ('hello',)

    # The following example is called tuple packing:
    packed_tuple = 12345, 54321, 'hello!'

    # The reverse operation is also possible.
    first_tuple_number, second_tuple_number, third_tuple_string = packed_tuple
    assert first_tuple_number == 12345
    assert second_tuple_number == 54321
    assert third_tuple_string == 'hello!'

    # This is called, appropriately enough, sequence unpacking and works for any sequence on the
    # right-hand side. Sequence unpacking requires that there are as many variables on the left
    # side of the equals sign as there are elements in the sequence. Note that multiple assignment
    # is really just a combination of tuple packing and sequence unpacking.

    # Swapping using tuples.
    # Data can be swapped from one variable to another in python using
    # tuples. This eliminates the need to use a 'temp' variable.
    first_number = 123
    second_number = 456
    first_number, second_number = second_number, first_number

    assert first_number == 456
    assert second_number == 123
