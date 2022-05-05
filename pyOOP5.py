# class inside another class
class Student:

    def __init__(self, name, snum):
        self.name = name
        self.snum = snum
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.snum)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("DouDou", 2)
s2 = Student("Biffon", 4)

s1.show()
s2.show()
# print(s1.lap.brand)

