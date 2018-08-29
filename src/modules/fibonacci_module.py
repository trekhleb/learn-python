"""Fibonacci numbers module.

@see: https://docs.python.org/3/tutorial/modules.html

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.
"""


def fibonacci_at_position(position):
    """Return Fibonacci number at specified position"""
    current_position = 0
    previous_number, current_number = 0, 1
    while current_position < position:
        current_position += 1
        previous_number, current_number = current_number, previous_number + current_number
    return previous_number


def fibonacci_smaller_than(limit):
    """Return Fibonacci series up to limit"""
    result = []
    previous_number, current_number = 0, 1
    while previous_number < limit:
        result.append(previous_number)
        previous_number, current_number = current_number, previous_number + current_number
    return result


# When you run a Python module with:
#
# >>> python fibonacci.py <arguments>
#
# the code in the module will be executed, just as if you imported it, but with
# the __name__ set to "__main__". That means that by adding this code at the end of your module
# you can make the file usable as a script as well as an importable module, because the code that
# parses the command line only runs if the module is executed as the “main” file:
#
# >>> python fibonacci.py 50
if __name__ == '__main__':
    import sys
    print(fibonacci_smaller_than(int(sys.argv[1])))
