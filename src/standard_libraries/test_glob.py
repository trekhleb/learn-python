"""File Wildcards.

@see: https://docs.python.org/3/tutorial/stdlib.html#file-wildcards

The glob module provides a function for making file lists from directory wildcard searches:
"""

import glob


def test_glob():
    """File Wildcards."""

    # == operator for lists relies on the order of elements in the list.
    # In some cases (like on Linux Mint, python3.6) the glob() function returns list
    # in reverse order then  it might be expected. Thus lets sort both lists before comparison
    # using sorted() built-in function.
    assert sorted(glob.glob('src/standard_libraries/glob_files/*.txt')) == sorted([
        'src/standard_libraries/glob_files/first_file.txt',
        'src/standard_libraries/glob_files/second_file.txt'
    ])
