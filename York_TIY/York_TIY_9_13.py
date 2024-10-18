import random as r

class Die:

    def __init__(self):
        self.sides = 6

    def roll_die(self):
        return r.randint(1,6)


die = Die()

print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())
print(die.roll_die())