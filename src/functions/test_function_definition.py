"""Function Definition

@see: https://docs.python.org/3/tutorial/controlflow.html#defining-functions
@see: https://www.thecodeship.com/patterns/guide-to-python-function-decorators/

The keyword def introduces a function definition. It must be followed by the function name and the
parenthesized list of formal parameters. The statements that form the body of the function start at
the next line, and must be indented.
"""


def fibonacci_function_example(number_limit):
    """Generate a Fibonacci series up to number_limit.

    The first statement of the function body can optionally be a string literal; this string
    literal is the function’s documentation string, or docstring. There are tools which use
    docstrings to automatically produce online or printed documentation, or to let the user
    interactively browse through code; it’s good practice to include docstrings in code that you
    write, so make a habit of it.
    """

    # The execution of a function introduces a new symbol table used for the local variables of the
    # function. More precisely, all variable assignments in a function store the value in the local
    # symbol table; whereas variable references first look in the local symbol table, then in the
    # local symbol tables of enclosing functions, then in the global symbol table, and finally in
    # the table of built-in names. Thus, global variables cannot be directly assigned a value
    # within a function (unless named in a global statement), although they may be referenced.
    fibonacci_list = []
    previous_number, current_number = 0, 1
    while previous_number < number_limit:
        # The statement result.append(a) calls a method of the list object result. A method is a
        # function that ‘belongs’ to an object and is named obj.methodname, where obj is some
        # object (this may be an expression), and methodname is the name of a method that is
        # defined by the object’s type. Different types define different methods. Methods of
        # different types may have the same name without causing ambiguity. (It is possible to
        # define your own object types and methods, using classes, see Classes) The method
        # append() shown in the example is defined for list objects; it adds a new element at
        # the end of the list. In this example it is equivalent to result = result + [a], but
        # more efficient.
        fibonacci_list.append(previous_number)
        # This is multiple assignment statement. We make current number to be previous one and the
        # sum of previous and current to be a new current.
        previous_number, current_number = current_number, previous_number + current_number

    # The return statement returns with a value from a function. return without an expression
    # argument returns None. Falling off the end of a function also returns None.
    return fibonacci_list


def test_function_definition():
    """Function Definition"""

    # Now call the function we just defined.
    assert fibonacci_function_example(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # A function definition introduces the function name in the current symbol table. The value of
    # the function name has a type that is recognized by the interpreter as a user-defined function.
    # This value can be assigned to another name which can then also be used as a function. This
    # serves as a general renaming mechanism
    fibonacci_function_clone = fibonacci_function_example
    assert fibonacci_function_clone(300) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233]

    # In Python, functions are first class citizens, they are objects and that means we can do a
    # lot of useful stuff with them.

    # Assign functions to variables.

    def greet(name):
        return 'Hello, ' + name

    greet_someone = greet

    assert greet_someone('John') == 'Hello, John'

    # Define functions inside other functions.

    def greet_again(name):
        def get_message():
            return 'Hello, '

        result = get_message() + name
        return result

    assert greet_again('John') == 'Hello, John'

    # Functions can be passed as parameters to other functions.

    def greet_one_more(name):
        return 'Hello, ' + name

    def call_func(func):
        other_name = 'John'
        return func(other_name)

    assert call_func(greet_one_more) == 'Hello, John'

    # Functions can return other functions. In other words, functions generating other functions.

    def compose_greet_func():
        def get_message():
            return 'Hello there!'

        return get_message

    greet_function = compose_greet_func()
    assert greet_function() == 'Hello there!'

    # Inner functions have access to the enclosing scope.

    # More commonly known as a closure. A very powerful pattern that we will come across while
    # building decorators. Another thing to note, Python only allows read access to the outer
    # scope and not assignment. Notice how we modified the example above to read a "name" argument
    # from the enclosing scope of the inner function and return the new function.

    def compose_greet_func_with_closure(name):
        def get_message():
            return 'Hello there, ' + name + '!'

        return get_message

    greet_with_closure = compose_greet_func_with_closure('John')

    assert greet_with_closure() == 'Hello there, John!'
