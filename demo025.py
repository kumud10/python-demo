class MyClass:
    name = ""

    def __init__(self, name):
        self.name = name

    def func1(self):
        print('Name is :', self.name)

myc = MyClass("Kumud")

myc.func1()
