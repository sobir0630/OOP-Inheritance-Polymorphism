class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self):
        return "Bonus hisoblash usuli aniqlanmagan."

class Developer(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.10
        return f"{self.name} uchun bonus: {bonus} som"

class Manager(Employee):
    def calculate_bonus(self):
        bonus = self.salary * 0.20
        return f"{self.name} uchun bonus: {bonus} som"

dev = Developer("Ali", 8_000_000)
mgr = Manager("Dilshod", 12_000_000)

print(dev.calculate_bonus())
print(mgr.calculate_bonus())
