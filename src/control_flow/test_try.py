"""TRY statement

@see: https://www.w3schools.com/python/python_try_except.asp

"try" statement is used for exception handling.
When an error occurs, or exception as we call it, Python will normally stop and generate an error
message. These exceptions can be handled using the try statement.

The "try" block lets you test a block of code for errors.
The "except" block lets you handle the error.
The "else" block lets you execute the code if no errors were raised.
The "finally" block lets you execute code, regardless of the result of the try- and except blocks.
"""


def test_try():
    """TRY statement"""

    # The try block will generate an error, because x is not defined:
    exception_has_been_caught = False

    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except NameError:
        exception_has_been_caught = True

    assert exception_has_been_caught

    # You can define as many exception blocks as you want, e.g. if you want to execute a special
    # block of code for a special kind of error:
    exception_message = ''

    try:
        # pylint: disable=undefined-variable
        print(not_existing_variable)
    except NameError:
        exception_message = 'Variable is not defined'

    assert exception_message == 'Variable is not defined'

    # You can use the else keyword to define a block of code to be executed
    # if no errors were raised.
    message = ''
    # pylint: disable=broad-except
    try:
        message += 'Success.'
    except NameError:
        message += 'Something went wrong.'
    else:
        message += 'Nothing went wrong.'

    assert message == 'Success.Nothing went wrong.'

    # The finally block, if specified, will be executed regardless if the try block raises an
    # error or not.
    message = ''
    try:
        # pylint: undefined-variable
        print(not_existing_variable)  # noqa: F821
    except NameError:
        message += 'Something went wrong.'
    finally:
        message += 'The "try except" is finished.'

    assert message == 'Something went wrong.The "try except" is finished.'
