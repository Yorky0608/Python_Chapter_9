from Asset import Asset
from Apartment import Apartment

class Building(Asset):

    """Creating variable for number of apartments, and it inherits attributes from Asset"""

    def __init__(self, name, address, num_apartments, rent, maintenance):
        super().__init__(name, address)
        self.num_apartments = num_apartments
        self.__revenue = float(self._revenue)
        self.apart = Apartment(rent, maintenance)

    """Allows you to call and see what __revenue is but not change it"""

    @property
    def revenue__(self):
        return self.__revenue

    """Calculates the revenue of the building"""

    def revenue(self):
        self.__revenue = (self.num_apartments * float(self.apart.rent_getter)) - (self.apart.maintenance * self.num_apartments)
        return self.__revenue

    """Displays the name, address, and revenue"""
    
    def display(self):
        print(f"\nThe name of the building is {self.name}. "
              f"\nThe address is {self.address}. "
              f"\nThe revenue is ${format(self.__revenue, '.2f')}.")