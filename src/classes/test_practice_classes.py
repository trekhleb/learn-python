"""
Practing  the classes tasks
"""

def test_class_and_instance_variable():
    """ Testing class and  instance variable """
    class Car:
        """ Car class example"""

        #pylint: disbale= too-few-public-methods
        name = 'Sports Car'

        def __init__(self,owner_name):
            self.owner_name=owner_name

    car1 = Car('Ali')
    car2 = Car('Hamza')

    assert car1.name == "Sports Car"
    assert car2.name == "Sports Car"

    assert car1.owner_name == 'Ali'
    assert car2.owner_name == "Hamza"

    Car.name = 'MiniVan'

    assert car1.name == 'MiniVan'

    car3 = Car('Raza')
    
    assert car3.name == 'MiniVan'


    class CarWithSharedFeatures:

        """ Car class example with wrong shared variable usage"""
        features=[]

        def __init__(self, owner_name):
            self.name = owner_name  # Instance variable unique to each instance.

        def add_feature(self, feature):
            """Add feature to the car
            This function illustrate mistaken use of mutable class variable features.
            """
            self.features.append(feature)

    car1 = CarWithSharedFeatures('Ali')
    car2 = CarWithSharedFeatures ('Hamza')

    car1.add_feature("Back Camera")
    car2.add_feature("Leather seats")

    #All cars are sharing same mutable object
    assert car1.features == ["Back Camera","Leather seats"]

    class CarWithSeperateFeatures:

        """ Car class example with correct shared variable usage"""
        
        def __init__(self, owner_name):
            self.name = owner_name  # Instance variable unique to each instance.
            self.features=[]

        def add_feature(self, feature):
            """Add feature to the car
            This function illustrate mistaken use of mutable class variable features.
            """
            self.features.append(feature)

    car1 = CarWithSeperateFeatures('Ali')
    car2 = CarWithSeperateFeatures ('Hamza')

    car1.add_feature("Back Camera")
    car2.add_feature("Leather_seats")

    # Each car has separate features list
    assert car1.features == ["Back Camera"]






        