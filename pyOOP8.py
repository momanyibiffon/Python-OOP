class Person:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school

    def member(self):
        # return f"My name is {self.name} amd I am {self.age} years old, I study in {self.school}."
        print("My name is {} amd I am {} years old, I study in {}.".format(self.name, self.age, self.school))


member1 = Person("Biffon", 27, "UESTC")

# print("Name:", member1.name, "\nAge:", member1.age, "\nSchool:", member1.school)

print(member1.member())
