class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} has a cuisine called {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is now open.")

restaurant1 = Restaurant("Lemo", "Chicken")
restaurant2 = Restaurant("Polo", "Chili")
restaurant3 = Restaurant("NYC Dogs", "Hot Dogs")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
