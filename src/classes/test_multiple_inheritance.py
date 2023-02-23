"""Multiple Inheritance

@see: https://docs.python.org/3/tutorial/classes.html#multiple-inheritance

Some classes may derive from multiple classes. This means that the derived class would have
its attributes, along with the attributes of all the classes that it was derived from.
"""


def test_multiple_inheritance():
    """Multiple Inheritance"""

    # pylint: disable=too-few-public-methods
    class Clock:
        """Clock class"""

        time = '11:23 PM'

        def get_time(self):
            """Get current time

            Method is hardcoded just for multiple inheritance illustration.
            """
            return self.time

    # pylint: disable=too-few-public-methods
    class Calendar:
        """Calendar class"""

        date = '12/08/2018'

        def get_date(self):
            """Get current date

            Method is hardcoded just for multiple inheritance illustration.
            """
            return self.date

    # Python supports a form of multiple inheritance as well. A class definition with multiple
    # base classes looks like this.
    class CalendarClock(Clock, Calendar):
        """Class that uses multiple inheritance.

        For most purposes, in the simplest cases, you can think of the search for attributes
        inherited from a parent class as depth-first, left-to-right, not searching twice in the same
        class where there is an overlap in the hierarchy. Thus, if an attribute is not found in
        CalendarClock, it is searched for in Clock, then (recursively) in the base classes of
        Clock, and if it was not found there, it was searched for in Calendar, and so on.

        In fact, it is slightly more complex than that; the method resolution order changes
        dynamically to support cooperative calls to super(). This approach is known in some other
        multiple-inheritance languages as call-next-method and is more powerful than the super call
        found in single-inheritance languages.

        Dynamic ordering is necessary because all cases of multiple inheritance exhibit one or more
        diamond relationships (where at least one of the parent classes can be accessed through
        multiple paths from the bottommost class). For example, all classes inherit from object,
        so any case of multiple inheritance provides more than one path to reach object. To keep
        the base classes from being accessed more than once, the dynamic algorithm linearizes the
        search order in a way that preserves the left-to-right ordering specified in each class,
        that calls each parent only once, and that is monotonic (meaning that a class can be
        subclassed without affecting the precedence order of its parents).
        """

    calendar_clock = CalendarClock()

    assert calendar_clock.get_date() == '12/08/2018'
    assert calendar_clock.get_time() == '11:23 PM'
