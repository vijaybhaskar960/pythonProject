# Overloading
class Bird:

    def fly(self,name=None):
        if name =="parrot":
            print("Parrot can fly")
        if name =="penguin":
            print("can't fly")
        if name is None:
            print("No input")

obj = Bird()

obj.fly()
obj.fly('parrot')
obj.fly('penguin')
