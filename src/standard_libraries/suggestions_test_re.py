"""String Pattern Matching.

@see: https://docs.python.org/3/tutorial/stdlib.html#string-pattern-matching

The re module provides regular expression tools for advanced string processing.
For complex matching and manipulation, regular expressions offer succinct, optimized solutions:
"""

import re


def test_NIC():
    """NIC matching by regular expression"""
    txt = "35201-2368626-7"
    x = re.search("\d\d\d\d\d-\d\d\d\d\d\d\d-\d", txt)
    assert x.string == '35201-2368626-7'
