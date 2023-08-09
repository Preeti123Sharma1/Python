class DemoClass:
    a = 25          # variable
    b = 15

    def sumvalue(self):         # this function in class and if we create function in class the we define argument(self) i.e any name.
        print(10 + 20)

demoobject = DemoClass()
demoobject1 = DemoClass()

print(demoobject.a)
print(demoobject1.b)

demoobject.sumvalue();          # call the sumvalue