# Overloading Example
class Area:
    def find_area(self, x=None, y=None):

        if x!=None and y!=None:
            print("Ractangle Area : ", x * y)

        elif x!=None:
            print("Square Area : ", x * x)

        else:
            print("Nothing to find")

obj = Area()
obj.find_area()
obj.find_area(20)
obj.find_area(20,30)

