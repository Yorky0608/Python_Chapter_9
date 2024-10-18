from User import User

class Admin(User):

    def __init__(self, first_name, last_name, age=None, location=None, color=None):
        super().__init__(first_name, last_name, age, location, color)
        self.privileges = Privileges()


class Privileges:

    def __init__(self):
        self.privileges = ["Can add post", "Can delete post", "Can ban user"]

    def show_privileges(self):
        for priv in self.privileges:
            print(priv)