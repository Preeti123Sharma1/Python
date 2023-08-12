### Encapsulation, we use Getter and Setter for setting the value in private section and after we getting the value.

class Student:

    def __init__(self):
        self.___testing=""

    def gethello(self):
        return self.___testing

    def sethello(self,name):
        self.___testing = name

obj = Student()
obj.sethello("Preeti")
name = obj.gethello()
print(name)