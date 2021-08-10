"""Generators.

@see: https://www.learnpython.org/en/Generators

Generators are used to create iterators, but with a different approach. Generators are simple
functions which return an iterable set of items, one at a time, in a special way.

When an iteration over a set of item starts using the for statement, the generator is run. Once the
generator's function code reaches a "yield" statement, the generator yields its execution back to
the for loop, returning a new value from the set. The generator function can generate as many
values (possibly infinite) as it wants, yielding each one in its turn.
"""

import random


def even_number_generator():
    """Generator function example.

    Here is a simple example of a generator function which returns random integers.
    This function decides how to generate the random numbers on its own, and executes the yield
    statements one at a time, pausing in between to yield execution back to the main for loop.
    """
    # pylint: disable=unused-variable
    for i in range(20):
        if i % 2 == 0:
            yield i


def test_generators():
    """Yield statement"""
    for number_index, random_number in enumerate(even_number_generator()):
        if number_index < 5:
            assert 0 <= random_number <= 10 and (random_number % 2) == 0
        else:
            assert 10 <= random_number <= 20 and (random_number % 2) == 0
