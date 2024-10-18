class User:
    def __init__(self, first_name, last_name, age=None, location=None, color=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.color = color

    def __repr__(self):
        return f"\nWelcome {self.first_name} {self.last_name}. Hope you are having a great day!"

    def description(self):
        print(f"The user's name is {self.first_name} {self.last_name}.")
        if self.age:
            print(f"Their age is {self.age}.")
        if self.location:
            print(f"They live in {self.location}.")
        if self.color:
            print(f"Their favorite color is {self.color}.")


user1 = User("Jack", "Lux", color="Blue")
user2 = User("Paul", "Talon", 23, "Indie")
user3 = User("Jose", "Martinez", 19, "Fort Wayne", "Red")
user4 = User("Webby", "Webster", "Fort Wayne", "Gold")
user5 = User("Owen", "Sleech", 18, "Leo")
user6 = User("Luke", "Jaxon", location="Bloomington")
user7 = User("Carl", "Rodston", 55)

print(user1)
user1.description()

print(user2)
user2.description()

print(user3)
user3.description()

print(user4)
user4.description()

print(user5)
user5.description()

print(user6)
user6.description()

print(user7)
user7.description()