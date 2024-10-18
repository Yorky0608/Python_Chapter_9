class User:
    def __init__(self, first_name, last_name, age=None, location=None, color=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.color = color
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1
        return self.login_attempts

    def reset_login_attempts(self):
        self.login_attempts = 0
        return self.login_attempts





user1 = User("Jack", "Lux", color="Blue")

print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())
print(user1.increment_login_attempts())

user1.reset_login_attempts()

print(user1.login_attempts)