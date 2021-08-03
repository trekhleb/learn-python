"""Strings.

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_strings.asp
@see: https://www.w3schools.com/python/python_ref_string.asp

Besides numbers, Python can also manipulate strings, which can be
expressed in several ways. They can be enclosed in single quotes ('...')
or double quotes ("...") with the same result.
"""

import pytest


def test_string_type():
    """String type"""

    # String with double quotes.
    name_1 = "John"
    # String with single quotes.
    name_2 = 'John'
    # Strings created with different kind of quotes are treated the same.
    assert name_1 == name_2
    assert isinstance(name_1, str)
    assert isinstance(name_2, str)

    # \ can be used to escape quotes.
    # use \' to escape the single quote or use double quotes instead.
    single_quote_string = 'Fareed\'s code'
    double_quote_string = "Fareed's code"

    assert single_quote_string == double_quote_string

    # \n means newline.
    multiline_string = 'First line.\nSecond line.'
    # Without print(), \n is included in the output.
    # But with print(), \n produces a new line.
    assert multiline_string == '''First line.
Second line.'''

    # Strings can be indexed, with the first character having index 0.
    # There is no separate character type; a character is simply a string
    # of size one. Note that since -0 is the same as 0, negative indices
    # start from -1.
    word = 'Fareed'
    assert word[0] == 'F'  # First character.
    assert word[5] == 'd'  # Fifth character.
    assert word[-1] == 'd'  # Last character.
    assert word[-2] == 'e'  # Second-last character.
    assert word[-6] == 'F'  # Sixth from the end or zeroth from the beginning.

    assert isinstance(word[0], str)

    # In addition to indexing, slicing is also supported. While indexing is
    # used to obtain individual characters, slicing allows you to obtain
    # substring:
    assert word[0:2] == 'Fa'  # Characters from position 0 (included) to 2 (excluded).
    assert word[2:5] == 'ree'  # Characters from position 2 (included) to 5 (excluded).

    # Note how the start is always included, and the end always excluded.
    # This makes sure that s[:i] + s[i:] is always equal to s:
    assert word[:3] + word[3:] == 'Fareed'
    assert word[:1] + word[1:] == 'Fareed'

    # Slice indices have useful defaults; an omitted first index defaults to
    # zero, an omitted second index defaults to the size of the string being
    # sliced.
    assert word[:2] == 'Fa'  # Character from the beginning to position 2 (excluded).
    assert word[4:] == 'ed'  # Characters from position 4 (included) to the end.
    assert word[-2:] == 'ed'  # Characters from the second-last (included) to the end.

    # One way to remember how slices work is to think of the indices as
    # pointing between characters, with the left edge of the first character
    # numbered 0. Then the right edge of the last character of a string of n
    # characters has index n, for example:
    #
    # +---+---+---+---+---+---+
    #  | F | a | r | e | e | d |
    #  +---+---+---+---+---+---+
    #  0   1   2   3   4   5   6
    # -6  -5  -4  -3  -2  -1

    # Attempting to use an index that is too large will result in an error.
    with pytest.raises(Exception):
        not_existing_character = word[42]
        assert not not_existing_character

    # However, out of range slice indexes are handled gracefully when used
    # for slicing:
    assert word[4:42] == 'ed'
    assert word[42:] == ''

    # Python strings cannot be changed; they are immutable. Therefore,
    # assigning to an indexed position in the string
    # results in an error:
    with pytest.raises(Exception):
        # pylint: disable=unsupported-assignment-operation
        word[0] = 'J'

    # If you need a different string, you should create a new one:
    assert 'J' + word[1:] == 'Jareed'
    assert word[:2] + 'py' == 'Fapy'

    # The built-in function len() returns the length of a string:
    characters = 'wordoflength14'
    assert len(characters) == 14

    multi_line_string = '''\
        First line
        Second line
    '''

    assert multi_line_string == '''\
        First line
        Second line
    '''


def test_string_operators():
    """Basic operations

    Strings can be concatenated (glued together) with the + operator,
    and repeated with *: 3 times 'un', followed by 'ium'
    """

    assert 3 * 'un' + 'ium' == 'unununium'

    # 'Py' 'thon'
    python = 'Py' 'thon'
    assert python == 'Python'

    # This feature is particularly useful when you want to break long strings:
    text = (
        'Put several strings within parentheses '
        'to have them joined together.'
    )
    assert text == 'Put several strings within parentheses to have them joined together.'

    # If you want to concatenate variables or a variable and a literal, use +:
    prefix = 'Py'
    assert prefix + 'thon' == 'Python'


def test_string_methods():
    """String methods"""

    hello_world_string = "Hello, World!"

    # The strip() method removes any whitespace from the beginning or the end.
    string_with_whitespaces = "              Hello, World!                 "
    assert string_with_whitespaces.strip() == "Hello, World!"

    # The len() method returns the length of a string.
    assert len(hello_world_string) == 13

    # The lower() method returns the string in lower case.
    assert hello_world_string.lower() == 'hello, world!'

    # The upper() method returns the string in upper case.
    assert hello_world_string.upper() == 'HELLO, WORLD!'

    # The replace() method replaces a string with another string.
    assert hello_world_string.replace('H', 'J') == 'Jello, World!'

    # The split() method splits the string into substrings if it finds instances of the separator.
    assert hello_world_string.split(',') == ['Hello', ' World!']

    # Converts the first character to upper case
    assert 'low letter at the beginning'.capitalize() == 'Low letter at the beginning'

    # Returns the number of times a specified value occurs in a string.
    assert 'low letter at the beginning'.count('n') == 3

    # Searches the string for a specified value and returns the position of where it was found.
    assert 'Hello, welcome to my world'.find('world') == 21

    # Converts the first character of each word to upper case
    assert 'course for basic python'.title() == 'Course For Basic Python'

    # Returns a string where a specified value is replaced with a specified value.
    assert 'I like bananas'.replace('bananas', 'apples') == 'I like apples'

    # Joins the elements of an iterable to the end of the string.
    my_tuple = ('My', 'name is', 'Fareed')
    assert ', '.join(my_tuple) == 'My, name is, Fareed'

    # Returns True if all characters in the string are upper case.
    assert 'ABC'.isupper()
    assert not 'AbC'.isupper()

    # Check if all the characters in the text are letters.
    assert 'CompanyX'.isalpha()
    assert not 'Company 23'.isalpha()

    # Returns True if all characters in the string are decimals.
    #assert '1234'.isdecimal()
    #assert not 'a21453'.isdecimal()


def test_string_formatting():
    """String formatting.

    Often you will want more control over the formatting of your output than simply printing
    space separated values. There are several ways to format output
    """

    # To use formatted string literals, begin a string with f or F before the opening quotation
    # mark or triple quotation mark. Inside this string, you can write a Python expression
    # between { and } characters that can refer to variables or literal values.
    year = 2018
    event = 'conference'

    #assert (f"Results of the {year} {event}") == 'Results of the 2018 conference'

    #yes_votes = 42_572_654  # equivalent of 42572654
    #no_votes = 43_132_495   # equivalent of 43132495
    #percentage = yes_votes / (yes_votes + no_votes)

    #assert '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage) == ' 42572654 YES votes  49.67%'

    # Many values, such as numbers or structures like lists and dictionaries, have the same
    # representation using either function. Strings, in particular, have two distinct
    # representations.

    greeting = 'Hello, world.'
    first_num = 10 * 3.25
    second_num = 200 * 200

    assert str(greeting) == 'Hello, world.'
    assert repr(greeting) == "'Hello, world.'"
    assert str(1.0/7) == '0.142857142857'
    assert not repr(1/7) == '1/7'

    # The argument to repr() may be any Python object:
    assert repr((first_num, second_num, ('spam', 'eggs'))) == "(32.5, 40000, ('spam', 'eggs'))"

    # Formatted String Literals

    # Formatted string literals (also called f-strings for short) let you include the value of
    # Python expressions inside a string by prefixing the string with f or F and writing
    # expressions as {expression}.

    # An optional format specifier can follow the expression. This allows greater control over how
    # the value is formatted. The following example rounds pi to three places after the decimal.
    pi_value = 3.14159
    #assert F'The value of pi is {pi_value:.3f}.' == 'The value of pi is 3.142.'

    # Passing an integer after the ':' will cause that field to be a minimum number of characters
    # wide. This is useful for making columns line up:
    table_data = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    table_string = ''
    #for name, phone in table_data.items():
    #    table_string += f'{name:7}==>{phone:7d}'

    #assert table_string == ('Sjoerd ==>   4127'
    #                        'Jack   ==>   4098'
    #                        'Dcab   ==>   7678')

    # The String format() Method

    # Basic usage of the str.format() method looks like this:
    assert 'We are {} who say "{}!"'.format('knights', 'Ni') == 'We are knights who say "Ni!"'

    # The brackets and characters within them (called format fields) are replaced with the objects
    # passed into the str.format() method. A number in the brackets can be used to refer to the
    # position of the object passed into the str.format() method
    assert '{0} and {1}'.format('spam', 'eggs') == 'spam and eggs'
    assert '{1} and {0}'.format('spam', 'eggs') == 'eggs and spam'

    # If keyword arguments are used in the str.format() method, their values are referred to by
    # using the name of the argument.
    formatted_string = 'This {food} is {adjective}.'.format(
        food='spam',
        adjective='absolutely horrible'
    )

    assert formatted_string == 'This spam is absolutely horrible.'

    # Positional and keyword arguments can be arbitrarily combined
    formatted_string = 'The story of {0}, {1}, and {other}.'.format(
        'Bill',
        'Manfred',
        other='Georg'
    )

    assert formatted_string == 'The story of Bill, Manfred, and Georg.'


    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
    formatted_string = 'Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'


    formatted_string = 'Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)

    assert formatted_string == 'Jack: 4098; Sjoerd: 4127; Dcab: 8637678'
