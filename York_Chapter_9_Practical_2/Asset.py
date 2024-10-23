class Asset:

    """Creating variable name, address, and _revenue <---(protected but not private)"""

    def __init__(self, name, address, rent=0):
        self.name = name
        self.address = address
        self._revenue = float(rent)