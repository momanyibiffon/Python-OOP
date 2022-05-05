class Person:
    profession = "Teacher"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def country(self, cty):
        return f"{self.name} is from {cty}"


class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"{self.color} car has {self.mileage} miles"


# Person objects
psn = Person("Dou Dou", 22)
# print(psn.description())
print(psn.country("China"))
print(psn)
print("*******************************************")
# Car objects
bc = Car("Blue", 25000)
rc = Car("Red", 35000)
print(bc)
print(rc)
