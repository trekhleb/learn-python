"""Class and Instance Variables.

@see: https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

Generally speaking, instance variables are for data unique to each instance and class variables are
for attributes and methods shared by all instances of the class.
"""


def test_class_and_instance_variables():
    """Class and Instance Variables."""

    # pylint: disable=too-few-public-methods
    class Dog:
        """Dog class example"""
        kind = 'canine'  # Class variable shared by all instances.

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

    fido = Dog('Fido')
    buddy = Dog('Buddy')

    # Shared by all dogs.
    assert fido.kind == 'canine'
    assert buddy.kind == 'canine'

    # Unique to fido.
    assert fido.name == 'Fido'

    # Unique to buddy.
    assert buddy.name == 'Buddy'

    # Shared data can have possibly surprising effects with involving mutable objects such as lists
    # and dictionaries. For example, the tricks list in the following code should not be used as a
    # class variable because just a single list would be shared by all Dog instances.

    # pylint: disable=too-few-public-methods
    class DogWithSharedTricks:
        """Dog class example with wrong shared variable usage"""
        tricks = []  # Mistaken use of a class variable (see below) for mutable objects.

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.

        def add_trick(self, trick):
            """Add trick to the dog

            This function illustrate mistaken use of mutable class variable tricks (see below).
            """
            self.tricks.append(trick)

    fido = DogWithSharedTricks('Fido')
    buddy = DogWithSharedTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs
    assert buddy.tricks == ['roll over', 'play dead']  # unexpectedly shared by all dogs

    # Correct design of the class should use an instance variable instead:

    # pylint: disable=too-few-public-methods
    class DogWithTricks:
        """Dog class example"""

        def __init__(self, name):
            self.name = name  # Instance variable unique to each instance.
            self.tricks = []  # creates a new empty list for each dog

        def add_trick(self, trick):
            """Add trick to the dog

            This function illustrate a correct use of mutable class variable tricks (see below).
            """
            self.tricks.append(trick)

    fido = DogWithTricks('Fido')
    buddy = DogWithTricks('Buddy')

    fido.add_trick('roll over')
    buddy.add_trick('play dead')

    assert fido.tricks == ['roll over']
    assert buddy.tricks == ['play dead']
