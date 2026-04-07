"""Class Definition Syntax.

@see: https://docs.python.org/3/tutorial/classes.html#class-objects

After defining the class attributes to a class, the class object can be created by assigning the
object to a variable. The created object would have instance attributes associated with it.
"""

def test_class_objects():
    """Class Objects.

    Class objects support two kinds of operations:
    - attribute references
    - instantiation.
    """

    class ComplexNumber:
        """Example of a complex number class"""

        def __init__(self, real=0, imaginary=0):
            """Initialize complex number with default values."""
            self.real = real
            self.imaginary = imaginary

        def get_real(self):
            """Return real part of complex number."""
            return self.real

        def get_imaginary(self):
            """Return imaginary part of complex number."""
            return self.imaginary

    assert ComplexNumber(0, 0).real == 0

    # __doc__ is also a valid attribute, returning the docstring belonging to the class
    assert ComplexNumber.__doc__ == "Example of a complex number class"

    # Class attributes can be changed dynamically
    ComplexNumber.real = 10
    assert ComplexNumber.real == 10

    # Creating an instance
    complex_number = ComplexNumber(10, -5)

    assert complex_number.real == 10
    assert complex_number.get_real() == 10

    # Reset real value to default
    ComplexNumber.real = 0
    assert ComplexNumber.real == 0

    # Using constructor-based initialization
    class ComplexNumberWithConstructor(ComplexNumber):
        """Example of a complex number class with constructor"""

        def __init__(self, real, imaginary):
            super().__init__(real, imaginary)  # Use super() to inherit from ComplexNumber

    complex_number = ComplexNumberWithConstructor(3.0, -4.5)

    # ✅ Fixed the assertion syntax here
    assert (complex_number.real, complex_number.imaginary) == (3.0, -4.5)
