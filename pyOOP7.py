# Polymorphism
# duck typing


class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")


class MyIDE:

    def execute(self):
        print("Spell checking")
        print("Rearranging")
        print("Compiling")
        print("Running")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = MyIDE()
lap1 = Laptop()

lap1.code(ide)


