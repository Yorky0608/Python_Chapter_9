from Sweet import Sweet_Candy

class Candy:
    
    candy_dict = {}

    def __init__(self):
        self.sweet_candy = Sweet_Candy()
        
    def c_dict(self):
        while True:
            name = self.sweet_candy.sweet()
            type = input("What kind of candy is it?  ")
            cost = float(input("What is the cost of the candy?  $"))
            color = input("What color is the candy?  ")

            self.candy_dict[name] = [type.title(), cost, color.title()]
            
            if input("\nDo you want to add more candies to sell? y/n  ").lower() == 'n':
                break



candy_list = Candy()