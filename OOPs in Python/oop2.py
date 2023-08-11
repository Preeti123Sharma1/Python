# Methods and constructors of OOP

class democlass:
    a = 20

    def __init__(self):                     # constructor, in this we don't need to call that.
        print("Welcome to Lucknow")

    def value(self):                    # method 1
        self.c = self.a * self.a
        print(self.c)

    def value2(self,a,b):               # method 2
        print(a + b)

    def value3(self):                   # method 3
        print("Hello friends, I'm Preeti")

obj = democlass()                       # create object
obj.value()                             # method 1 call 
obj.value2(12,14)                       # method 2 call
obj.value3()                            # method 3 call