"""Math.

@see: https://docs.python.org/3/tutorial/stdlib.html#mathematics

Math module is useful as many math functions are already implemented and optimized.
"""

import math
import random
import statistics


def test_math():
    """Math.

    The math module gives access to the underlying C library functions for floating point math.
    """
    assert math.cos(math.pi / 4) == 0.70710678118654757
    assert math.log(1024, 2) == 10.0


def test_random():
    """Random.

    The random module provides tools for making random selections.
    """

    # Choose from the list randomly.
    random_options = ['apple', 'pear', 'banana']
    random_choice = random.choice(random_options)  # i.e. 'apple'
    assert random_choice in random_options

    # Sampling without replacement.
    random_sample = random.sample(range(100), 10)  # i.e. [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
    for sample in random_sample:
        assert 0 <= sample <= 100

    # Choose random number.
    random_float = random.random()  # i.e. 0.17970987693706186
    assert 0 <= random_float <= 1

    # Random integer chosen from range(6)
    random_integer = random.randrange(6)  # i.e. 4
    assert 0 <= random_integer <= 6


def test_statistics():
    """Statistics.

    The statistics module calculates basic statistical properties (the mean, median,
    variance, etc.) of numeric data.
    """

    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

    assert statistics.mean(data) == 1.6071428571428572
    assert statistics.median(data) == 1.25
    assert statistics.variance(data) == 1.3720238095238095
