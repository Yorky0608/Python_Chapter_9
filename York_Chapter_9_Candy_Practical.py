class Candy:
    
    def __init__(self):
        self.candy_dict = {}
        self.customer_dict = {}
        self.total_cost = []
        self.sweet_candy = Sweet_Candy()
        
    def c_dict(self):
        while True:
            name = self.sweet_candy.sweet()
            type = input("What kind of candy is it?  ")
            cost = float(input("What is the cost of the candy?  $"))
            color = input("What color is the candy?  ")
            
            self.candy_dict[name] = [type.title(), cost, color.title()]
            
            if input("Do you want to add more candies to sell? y/n  ").lower() == 'n':
                break
        
    def order(self):
        while True:
            print("Enter no whenever you are finished selecting candies.  ")
            c_candy = input("What kind of candy do you want?  ")
            c_type = input("What type of candy is this?  ")
            c_color = input("What color of candy do you want?  ")
            
            if c_candy.lower() == "no" or c_type.lower() == "no" or c_color.lower() == "no":
                break
            
            if c_candy not in self.candy_dict:
                c_cost = float(input("What is the price of this candy?  $"))
                self.c_dict[c_candy] = [c_type, c_cost, c_color]
                
            self.customer_dict[c_candy] = [c_type, c_cost, c_color]
            
    def checktout(self):
        for key, values in self.customer_dict.items():
            print(f"\n{key}: {values[1]}")
            self.total_cost += values[1]
        print(f"${self.total_cost}")
        

class Sweet_Candy:
    
    def sweet(self):
        while True:
            name = input("Do you want to add a sweet version of a candy? y/n  ")
            
            if name.lower() == 'n':
                name = input("What kind of candy would you like?  ")
                return name.title()
            else:
                name = "sweet " + input("What kind of candy would you like to make sweet?  ")
                return name.title()
            
            
a = Candy()

a.c_dict()
print(a.candy_dict)