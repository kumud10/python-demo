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

class SubChild(Child):
    def __init__(self):
        print("Calling sub child constructor")

    def subchildMethod(self):
        print("Calling subchild method")

sc = SubChild()
sc.subchildMethod()
sc.childMethod()
sc.parentMethod()
