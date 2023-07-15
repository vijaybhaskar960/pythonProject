
class Animal:

    def fly(self, name):
        if name == "Parrot":
            print("Can fly")
        if name == "Cow":
            print("Can't Fly")
        if name == "Dolphin":
            print("Sea Bird")


obj = Animal()
obj.fly("Parrot")

import multipledispatch  # Using the multipledispatch module we can achieve the method overloading

class A:

    @multipledispatch.dispatch(int, int)
    def add(self, a, b):
        return a + b

    @multipledispatch.dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c


obj1 = A()
print(obj1.add(1, 2, 3))
print(obj1.add(9, 80))


