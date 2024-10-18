class Employee:
    __slots__ = ("name", "age", "salary")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

class Tester(Employee):
    def run_tests(self):
        print(f"Testing is started by {self.name}...")
        print("Tests are done.")


class SlotInspectorMixin:
    __slots__ = ()

    def has_slots(self):
        return hasattr(self, "__slots__")


class Developer(Employee, SlotInspectorMixin):
    __slots__ = ("framework")

    def __init__(self, name, age, salary, framework):
        super().__init__(name,age,salary)
        self.framework = framework

    def increase_salary(self, percent, bonus=0):
        super().increase_salary(percent)
        self.salary += bonus



employee1 = Developer("Lauren", 44, 1000, "Flask")
#employee2 = Developer("Ji-Soo", 38, 1000)

print(employee1.has_slots())