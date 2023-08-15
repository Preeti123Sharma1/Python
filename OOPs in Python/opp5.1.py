class Goa:
    def displayinfo(self):
        print("Welcome to Goa")

class Lucknow(Goa):
    def displayinfo(self):
        super().displayinfo()                       # function name is same in both classes so we use 'super key' for print both results.
        print("Welcome to Lucknow")

obj = Lucknow()
obj.displayinfo()