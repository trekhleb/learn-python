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

    Normally, files are opened in text mode, that means, you read and write strings from and to the
    file, which are encoded in a specific encoding. If encoding is not specified, the default is
    platform dependent (see open()). 'b' appended to the mode opens the file in binary mode: now
    the data is read and written in the form of bytes objects. This mode should be used for all
    files that don’t contain text.

    In text mode, the default when reading is to convert platform-specific line endings (\n on
    Unix, \r\n on Windows) to just \n. When writing in text mode, the default is to convert
    occurrences of \n back to platform-specific line endings. This behind-the-scenes modification
    to file data is fine for text files, but will corrupt binary data like that in JPEG or EXE
    files. Be very careful to use binary mode when reading and writing such files.

    It is good practice to use the with keyword when dealing with file objects. The advantage is
    that the file is properly closed after its suite finishes, even if an exception is raised at
    some point. Using with is also much shorter than writing equivalent try-finally blocks:
    """

    # Open files without using 'with' statement.
    file = open('src/files/multi_line_file.txt', 'r')

    assert not file.closed

    read_data = file.read()

    assert read_data == (
        'first line\n'
        'second line\n'
        'third line'
    )

    file.close()

    assert file.closed

    # Open file using with.
    with open('src/files/multi_line_file.txt', 'r') as file:
        read_data = file.read()

        assert read_data == (
            'first line\n'
            'second line\n'
            'third line'
        )

    assert file.closed

    # If you’re not using the with keyword, then you should call f.close() to close the file and
    # immediately free up any system resources used by it. If you don’t explicitly close a file,
    # Python’s garbage collector will eventually destroy the object and close the open file for you,
    # but the file may stay open for a while. Another risk is that different Python implementations
    # will do this clean-up at different times.
