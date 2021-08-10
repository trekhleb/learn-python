"""Dates and Times.

@see: https://docs.python.org/3/tutorial/stdlib.html#dates-and-times

The datetime module supplies classes for manipulating dates and times in both simple and complex
ways. While date and time arithmetic is supported, the focus of the implementation is on efficient
member extraction for output formatting and manipulation. The module also supports objects that
are timezone aware.
"""

from datetime import date


def test_datetime():
    """Dates and Times"""

    real_now = date.today()
    assert real_now

    fake_now = date(2018, 8, 29)

    assert fake_now.ctime() == 'Wed Aug 29 00:00:00 2018'
    assert fake_now.strftime(
        '%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'
    ) == '08-29-18. 29 Aug 2018 is a Wednesday on the 29 day of August.'

    # Dates support calendar arithmetic.
    birthday = date(1998, 11, 28)
    age = real_now.year - birthday.year

    assert age == 23
