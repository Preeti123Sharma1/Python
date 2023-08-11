#### Inheritance, in this a child class inherit the property of parent class.

class A:
    def display1(self):
        print("Welcome to Lucknow A ")

class B(A):
    def display2(self):
        print("Welcome to Lucknow B ")

obj = B()
obj.display1()
obj.display2()