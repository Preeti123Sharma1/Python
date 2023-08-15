## Polymorphism, means same functtion name (but different signatures) being uses for different types.
# 1. Overloading      2. Overriding

# Overloding :- function name is same but we don't pass parameter.

class hello:
    def displayinfo(self,name=""):                  # diplayinfo is function, name is parameter
        print("Hello, How are you "+name)

obj = hello()
obj.displayinfo()               # Without Argument
obj.displayinfo('Nidhi')        # with Argument