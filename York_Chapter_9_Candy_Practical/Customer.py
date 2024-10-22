from Candy import candy_list
class Customer:

    '''Defining the variables to be used with in the class'''

    def __init__(self):
        self.customer_dict = {}
        self.total_cost = 0

    '''Order allows users to pick candies they want to order. If that candy in not in the dictionary, they can add the price
       of the candy.'''

    def order(self):
        while True:
            print("\nEnter no whenever you are finished selecting candies.  ")

            c_candy = input("What kind of candy do you want?  ")
            if c_candy.lower() == "no":
                break

            c_type = input("What type of candy is this?  ")
            if c_type.lower() == "no":
                break

            c_color = input("What color is this candy?  ")
            if c_color.lower() == "no":
                break

            if c_candy.title() not in candy_list.candy_dict:
                c_cost = float(input("This candy was not found. What is the price of this candy?  $"))
            else:
                c_cost = candy_list.candy_dict[c_candy.title()][1]

            self.customer_dict[c_candy] = [c_type, c_cost, c_color]

    '''Prints a receipt of what the customer bought'''

    def checkout(self):
        print("\nReceipt:\n")

        for key, values in self.customer_dict.items():
            print(f"{key.title()} "
                  f"\n\tType: {values[0].title()}"
                  f"\n\tColor: {values[2].title()}"
                  f"\n\tPrice: ${format(values[1],'.2f')}")
            self.total_cost += values[1]

        print(f"\nTotal Price: ${format(self.total_cost, '.2f')}")