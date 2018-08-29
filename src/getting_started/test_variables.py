"""Variables

@see: https://docs.python.org/3/tutorial/introduction.html
@see: https://www.w3schools.com/python/python_variables.asp
@see: https://www.learnpython.org/en/Variables_and_Types

Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare
their type. Every variable in Python is an object.

Unlike other programming languages, Python has no command for
declaring a variable. A variable is created the moment you first assign
a value to it.

A variable can have a short name (like x and y) or a more descriptive name
(age, carname, total_volume).

Rules for Python variables:
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
- Variable names are case-sensitive (age, Age and AGE are three different variables).
"""


def test_variables():
    """Test variables"""

    integer_variable = 5
    string_variable = 'John'

    assert integer_variable == 5
    assert string_variable == 'John'

    variable_with_changed_type = 4  # x is of type int
    variable_with_changed_type = 'Sally'  # x is now of type str

    assert variable_with_changed_type == 'Sally'
