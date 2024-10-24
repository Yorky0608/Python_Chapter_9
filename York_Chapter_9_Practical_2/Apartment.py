class Apartment:

    """Defining variables and setting a private variable"""

    def __init__(self, rent, maintenance):
        self.__apartment_rent = float(rent)
        self.maintenance = maintenance

    """Allowing private variable to be accessed"""

    @property
    def rent_getter(self):
        return format(self.__apartment_rent, '.2f')

    """Displays the rent and maintenance of the apartment"""

    def display(self):
        print(f"\nThe rent of this apartment is ${format(self.__apartment_rent, '.2f')}."
              f"\nThe maintenance cost is ${format(self.maintenance, '.2f')}.")