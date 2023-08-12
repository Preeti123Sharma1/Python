# Multiple inheritence, it is not support by java, PHP.

class A():
    a = 5
    def displayA(self):
        self.c = self.a * self.a
        print(self.c)
        print("Welcome to Lucknow")

class B():
    def displayB(self):
        print("Hello Everyone")

class C(A,B):
    def displayC(self):
        print("Good Morning Lucknow")

obj = C()
obj.displayA()
obj.displayB()
obj.displayC()