class Asset:

    """Creating variable name, address, and _revenue <---(protected but not private)"""

    def __init__(self, name, address, rent=0):
        self.name = name
        self.address = address
        self._revenue = float(rent)

    """Prints the variables"""

    def display(self):
        print(f"\nThe name of this asset is {self.name}."
              f"\nThe address of this asset is {self.address}."
              f"\nThe revenue of this asset is ${format(self._revenue, '.2f')}.")