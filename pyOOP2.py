class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


# child classes
class MilesRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class Dachshund(Dog):
    def speak(self, sound="Wolooooff"):
        return super().speak(sound)


class Bulldog(Dog):
    pass


miles = MilesRussellTerrier("Miles", 2)
buddy = Dachshund("Buddy", 3)
jicy = Dog("Jicy", 4)
beike = Dog("Beike", 1)

print(beike.speak("Woof"))
print(type(jicy))
print(isinstance(miles, Bulldog))
print(miles.speak())
print(buddy.speak())
