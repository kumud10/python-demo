class MyParentClass1():

    def method_Parent1(self):
        print("Parent1 method calling ")

class MyParentClass2():

    def method_Parent2(self):
        print("Parent2 method calling")

class ChildClass(MyParentClass1, MyParentClass2):

    def child_method(self):
        print("Child method")

c = ChildClass()
c.method_Parent1()
c.method_Parent2()
c.child_method()