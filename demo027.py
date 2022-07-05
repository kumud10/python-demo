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

c = Child()
c.childMethod()
c.parentMethod()
