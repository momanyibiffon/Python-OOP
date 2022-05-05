# inheritance


class School:
    def __init__(self):
        self.school_name = "UESTC"
        self.location = "Chengdu"
        self.country = "China"

    def students_note(self):
        print("This method prints students note")


class Teacher(School):

    def __init__(self, teacher_name, school_name, age):
        self.teacher_name = teacher_name
        self.school_name = school_name
        self.age = age

    def studentNote(self):
        super().students_note()


sc = School()
print(sc.school_name)

tc1 = Teacher("Dou", sc.school_name, 22)
tc1.location = "Chengdu"
tc1.country = "China"
print(tc1.teacher_name, tc1.school_name, tc1.age, tc1.location, tc1.country)

tc2 = Teacher("Aqing", sc.school_name, 24)
tc2.location = "Xian"
tc2.country = "Kenya"
print(tc2.teacher_name, tc2.school_name, tc2.age, tc2.location, tc2.country)

tc2.studentNote()
