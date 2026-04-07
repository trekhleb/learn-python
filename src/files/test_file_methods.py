"""Methods of File Objects

@see: https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

Reading from a file does not always have to be sequential. There are methods to look for
specific locations in the file, much like flipping to a page in a book.
"""


def test_file_methods():
    """Methods of File Objects"""

    # Using `with` ensures files are properly closed after their suite finishes execution
    with open('src/files/multi_line_file.txt', 'r') as multi_line_file:
        with open('src/files/binary_file', 'rb') as binary_file:  # Open binary file in binary mode ('rb')

            # Reading the entire content of the multi_line_file
            read_data = multi_line_file.read()
            # Assert to check the file's content
            assert read_data == 'first line\nsecond line\nthird line'

            # Changing file position in binary_file using seek
            assert binary_file.seek(0) == 0  # Go to the 0th byte in the file
            assert binary_file.seek(6) == 6  # Go to the 6th byte in the file

            # Reading one byte and decoding to match comparison (since file is opened in binary mode)
            assert binary_file.read(1).decode('utf-8') == '6'

            # Resetting position of multi_line_file to beginning for readline operations
            multi_line_file.seek(0)

            # Reading lines one by one
            assert multi_line_file.readline() == 'first line\n'
            assert multi_line_file.readline() == 'second line\n'
            assert multi_line_file.readline() == 'third line'
            assert multi_line_file.readline() == ''  # Ensure end of file returns an empty string

    multi_line_file.close()
    binary_file.close()
