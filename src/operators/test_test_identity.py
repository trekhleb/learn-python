"""Identity operators

@see: https://www.w3schools.com/python/python_operators.asp

Identity operators are used to compare the objects, not if they are equal, but if they are actually
the same object, with the same memory location.
"""


def test_test_identity_operators():
    """Identity operators"""

    # Let's illustrate identity operators based on the following lists.
    first_list = [1, 2, 3]
    second_list = [1, 2, 3]
    third_list = first_list
    fourth_list = [1, 2]

    # is
    # Returns true if both variables are the same object.

    # Example:
    # first_fruits_list and third_fruits_list are the same objects.
    assert first_list is third_list

    # is not
    # Returns true if both variables are not the same object.

    # Example:
    # first_fruits_list and second_fruits_list are not the same objects, even if they have
    # the same content
    assert first_list is not second_list

    # To demonstrate the difference between "is" and "==": this comparison returns True because
    # first_fruits_list is equal to second_fruits_list.
    assert first_list == second_list

    # To demonstrate that is == operator returns false if all entry of 2 lists are not same
    assert first_list != fourth_list
