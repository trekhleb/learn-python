"""File Wildcards.

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

The glob module provides a function for making file lists from directory wildcard searches:
"""

import glob


def test_glob():
    """File Wildcards."""

    assert glob.glob('src/standard_libraries/glob_files/*.txt') == [
        'src/standard_libraries/glob_files/first_file.txt',
        'src/standard_libraries/glob_files/second_file.txt'
    ]
