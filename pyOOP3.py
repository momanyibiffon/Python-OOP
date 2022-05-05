class Computer:
    def __init__(self):
        self.name = "DouDou"
        self.age = 26

    def update(self):
        self.age = 27

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


class Car:

    wheels = 4

    def __init__(self):
        self.company = "BMW"
        self.milage = 10


com1 = Computer()
com2 = Computer()

com1.name = "Biff"

com1.update()

if com1.compare(com2):
    print("Same age")
else:
    print("Different age")


print(com1.name, ",", com1.age)
print(com2.name, ", ", com2.age)


car1 = Car()
car2 = Car()

print(car1.company, car1.milage, car1.wheels)
print(car2.company, car2.milage, car2.wheels)
