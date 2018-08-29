"""String Pattern Matching.

@see: https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching

The re module provides regular expression tools for advanced string processing.
For complex matching and manipulation, regular expressions offer succinct, optimized solutions:
"""

import re


def test_re():
    """String Pattern Matching"""

    assert re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest') == [
        'foot',
        'fell',
        'fastest'
    ]

    assert re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat') == 'cat in the hat'

    # When only simple capabilities are needed, string methods are preferred because they are
    # easier to read and debug:
    assert 'tea for too'.replace('too', 'two') == 'tea for two'
