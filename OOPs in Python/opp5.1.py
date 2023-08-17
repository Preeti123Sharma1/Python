# Overriding in Polymorphism
# By the help of super key we print the parent values in the child class.
# In this child function does not overring the parent function.

class Goa:
    def displayinfo(self):
        print("Welcome to Goa")

class Lucknow(Goa):
    def displayinfo(self):
        super().displayinfo()                       # function name is same in both classes so we use 'super key' for print both results.
        print("Welcome to Lucknow")

obj = Lucknow()
obj.displayinfo()