class Restaurant:
    """Creating a restaurant with a menu"""

    def __init__(self, restaurant_name, cuisine_type):
        """Setting variables for the class"""

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        """Prints the name and cuisine"""

        print(f"{self.restaurant_name} has a cuisine called {self.cuisine_type}.")

    def open_restaurant(self):
        """Prints the restaurant is open"""

        print(f"{self.restaurant_name} is now open.")

    def number_served(self):
        """Keeps track of people served"""

        print(f"{self.restaurant_name} has served {self.served} people.")