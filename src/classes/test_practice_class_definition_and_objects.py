"""
Practing  the Class Definition and objects
"""


def test_class_and_instance_variable():
    """ Testing class definition """
    class Car:
        """Car class example"""
        # pylint: disbale= too-few-public-methods
        name = 'Sports Car'

        def __init__(self, owner_name, model):
            self.owner_name = owner_name
            self.model = model

    assert Car.name == 'Sports Car'

    assert Car.__doc__ == 'Car class example'

    car1 = Car('Ali',2019)

    assert car1.name, car1.model == ('Ali',2019)
