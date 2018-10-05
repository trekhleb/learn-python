"""Methods of File Objects

@see: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

Reading from a file does not always have to be sequential. There are methods to look for
specific locations in the file, much like flipping to a page in a book.
"""


def test_file_methods():
    """Methods of File Objects"""

    multi_line_file = open('src/files/multi_line_file.txt', 'r')
    binary_file = open('src/files/binary_file', 'r')

    # To read a file’s contents, call f.read(size), which reads some quantity of data and returns
    # it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric
    # argument. When size is omitted or negative, the entire contents of the file will be read and
    # returned; it’s your problem if the file is twice as large as your machine’s memory. Otherwise,
    # at most size bytes are read and returned. If the end of the file has been reached, f.read()
    # will return an empty string ('').
    read_data = multi_line_file.read()

    # pylint: disable=duplicate-code
    assert read_data == 'first line\nsecond line\nthird line'

    # To change the file object’s position, use f.seek(offset, from_what). The position is computed
    # from adding offset to a reference point; the reference point is selected by the from_what
    # argument. A from_what value of 0 measures from the beginning of the file, 1 uses the current
    # file position, and 2 uses the end of the file as the reference point. from_what can be omitted
    # and defaults to 0, using the beginning of the file as the reference point.
    assert binary_file.seek(0) == 0  # Go to the 0th byte in the file
    assert binary_file.seek(6) == 6  # Go to the 6th byte in the file

    assert binary_file.read(1) == '6'

    # f.readline() reads a single line from the file; a newline character (\n) is left at the end
    # of the string, and is only omitted on the last line of the file if the file doesn’t end in a
    # newline. This makes the return value unambiguous; if f.readline() returns an empty string,
    # the end of the file has been reached, while a blank line is represented by '\n', a string
    # containing only a single newline.
    multi_line_file.seek(0)

    assert multi_line_file.readline() == 'first line\n'
    assert multi_line_file.readline() == 'second line\n'
    assert multi_line_file.readline() == 'third line'
    assert multi_line_file.readline() == ''

    multi_line_file.close()
    binary_file.close()
