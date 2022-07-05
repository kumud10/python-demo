class MyParentClass1():

    def method_Parent1(self):
        print("Parent1 method called ")

class MyParentClass2():

    def method_Parent2(self):
        print("Parent2 method called")

class ChildClass(MyParentClass1, MyParentClass2):

    def child_method(self):
        print("Child method")

class ChildClass2(MyParentClass1):

    def Child_method2(self):
        print("child method2")

c = ChildClass()
c.method_Parent1()
c.method_Parent2()
c.child_method()

c2 = ChildClass2()
c2.Child_method2()
c2.method_Parent1()