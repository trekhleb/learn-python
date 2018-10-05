"""Modules.

@see: https://docs.python.org/3/tutorial/modules.html

As your program gets longer, you may want to split it into several files for easier maintenance.
You may also want to use a handy function that you’ve written in several programs without copying
its definition into each program.

To support this, Python has a way to put definitions in a file and use them in a script or in an
interactive instance of the interpreter. Such a file is called a module; definitions from a module
can be imported into other modules or into the main module (the collection of variables that you
have access to in a script executed at the top level and in calculator mode).

A module is a file containing Python definitions and statements. The file name is the module name
with the suffix .py appended. Within a module, the module’s name (as a string) is available as the
value of the global variable __name__.

When the interpreter executes the import statement, it searches for module in a list of
directories assembled from the following sources:

- The directory from which the input script was run or the current directory if the interpreter is
being run interactively
- The list of directories contained in the PYTHONPATH environment variable, if it is set. (The
format for PYTHONPATH is OS-dependent but should mimic the PATH environment variable.)
- An installation-dependent list of directories configured at the time Python is installed

The resulting search path is accessible in the Python variable sys.path, which is obtained from a
module named sys:

>>> import sys
>>> sys.path

@see: https://realpython.com/python-modules-packages/
"""

# This does not enter the names of the functions defined in fibonacci_module directly in the
# current symbol table; it only enters the module name fibonacci_module there.
import fibonacci_module

# There is a variant of the import statement that imports names from a module directly into the
# importing module’s symbol table. For example:

# pylint: disable=reimported
from fibonacci_module import fibonacci_at_position, fibonacci_smaller_than

# There is even a variant to import all names that a module defines. This imports all names except
# those beginning with an underscore (_). In most cases Python programmers do not use this facility
# since it introduces an unknown set of names into the interpreter, possibly hiding some things you
# have already defined.
# >>> from fibonacci_module import *

# If the module name is followed by as, then the name following as is bound directly to the
# imported module:
import fibonacci_module as fibonacci_module_renamed

# It can also be used when utilising from with similar effects:
from fibonacci_module import fibonacci_at_position as fibonacci_at_position_renamed

# When a module named spam is imported, the interpreter first searches for a built-in module with
# that name. If not found, it then searches for a file named spam.py in a list of directories
# given by the variable sys.path. sys.path is initialized from these locations:
#
# - The directory containing the input script (or the current directory when no file is specified).
# - PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
# - The installation-dependent default.


def test_modules():
    """Modules"""

    assert fibonacci_module.fibonacci_at_position(7) == 13
    assert fibonacci_at_position(7) == 13
    assert fibonacci_module_renamed.fibonacci_at_position(7) == 13
    assert fibonacci_at_position_renamed(7) == 13

    assert fibonacci_module.fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_smaller_than(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert fibonacci_module_renamed.fibonacci_smaller_than(10) == [0, 1, 1, 2, 3, 5, 8]

    # If you intend to use a function often you can assign it to a local name.
    fibonacci = fibonacci_module.fibonacci_smaller_than
    assert fibonacci(100) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

    # The built-in function dir() is used to find out which names a module defines. It returns a
    # sorted list of strings.
    assert dir(fibonacci_module) == [
        '__builtins__',
        '__cached__',
        '__doc__',
        '__file__',
        '__loader__',
        '__name__',
        '__package__',
        '__spec__',
        'fibonacci_at_position',
        'fibonacci_smaller_than',
    ]
