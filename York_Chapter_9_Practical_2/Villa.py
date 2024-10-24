from Asset import Asset

class Villa(Asset):

    """Creating variable for number of apartments, and it inherits attributes from Asset"""

    def __init__(self, name, address, rent, maintenance):
        super().__init__(name, address)
        self.__rent = rent
        self.maintenance = float(maintenance)
        self.__revenue = self._revenue

    """Allows you call on the private variables"""

    @property
    def rent(self):
        return format(self.__rent, '.2f')

    @property
    def revenue__(self):
        return format(self.__revenue, '.2f')

    """Calculates revenue"""

    def revenue(self):
        self.__revenue = self.__rent - self.maintenance

    """Displays the ren, maintenance, and revenue"""

    def display(self):
        print(f"\nThe name of the villa is {self.name}. "
              f"\nThe address is {self.address}. "
              f"\nThe revenue is ${format(self.__revenue, '.2f')}.")