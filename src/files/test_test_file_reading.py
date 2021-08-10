"""Reading and Writing Files

@see: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

The process of reading and writing to a file is like finding a book and opening a book.
First, the file is located, opened to the first page, then reading/writing begins until it reaches
the end of the file.
"""


def test_files_open():
    """Open files

    open() returns a file object, and is most commonly used with two arguments:
    open(filename, mode).

    The first argument is a string containing the filename. The second argument is another string
    containing a few characters describing the way in which the file will be used. mode can be:

    - 'r' when the file will only be read,
    - 'w' for only writing (an existing file with the same name will be erased),
    - 'a' opens the file for appending; any data written to the file is automatically added to end.
    - 'r+' opens the file for both reading and writing.

    The mode argument is optional; 'r' will be assumed if it’s omitted.
    """

    # Open files without using 'with' statement.
    file = open('src/files/test_multi_line_file.txt', 'r')

    assert not file.closed

    read_data = file.read()

    assert read_data == (
        'first line1\n'
        'second line2\n'
        'third line3\n'
    )

    file.close()

    assert file.closed

    # Open file using with.
    with open('src/files/test_multi_line_file.txt', 'r') as file2:
        read_data = file2.read()

        assert read_data == (
            'first line1\n'
            'second line2\n'
            'third line3\n'
        )

    assert file2.closed
