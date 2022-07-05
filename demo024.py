class MyClass:
    name=""

    def func1(self):
        print("Hey there")

    def func2(self, name):
        self.name=name

    def func3(self):
        print("Value is ", self.name)

m1 = MyClass()
m1.func1()
m1.func2("Kumud")
m1.func3()