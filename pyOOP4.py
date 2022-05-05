# class, instance and static methods
class Student:

    school ="UESTC"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self): # instance method uses instance variables
        return (self.m1 + self.m2 + self.m3)/3

    @classmethod
    def getSchool(cls): # class method uses class variables
        return cls.school

    @staticmethod
    def info(): # static method
        print("This is an OOP lesson in Python")


s1 = Student(88, 99, 79)
s2 = Student(78, 88, 94)

print(s1.avg(), s2.avg())
print(s1.getSchool())

Student.info()
