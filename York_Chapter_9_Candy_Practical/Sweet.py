class Sweet_Candy:

    def sweet(self):
        while True:
            name = input("\nDo you want to add a sweet version of a candy? y/n  ")

            if name.lower() == 'n':
                name = input("What kind of candy would you like?  ")
                return name.title()
            else:
                name = "sweet " + input("What kind of candy would you like to make sweet?  ")
                return name.title()