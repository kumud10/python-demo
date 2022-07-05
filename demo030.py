class Parent:

    def __init__(self):
        print("Calling patrent constructor")

    def parentMethod(self):
        print("Calling parent method")

class Child(Parent):
    def __init__(self):
        print("Calling child constructot")

    def childMethod(self):
        print("Calling child method")

class Child2(Parent):
    def __init__(self):
        print("Calling child2 constructor")

    def childMethod2(self):
        print("Calling child method")

sc = Child2()
sc.childMethod2()
sc.parentMethod()