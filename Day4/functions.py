xy =100 # Global Variable

def cool():
    global xy
    xy=200
    print(xy)
cool()
print(xy)


xy =100 # Global Variable

def cool():
    xy=200  # Local Variable
    print(xy)
cool()
print(xy)

class MyClass:

    def __init__(self):
        print("This is Constructor...........")

    def m1(self):
        print("This is M1 method")

obj = MyClass()
obj.m1()

class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name=name
        self.sal=sal

    def __str__(self):
        return (self.name)

m = Emp(100,'vijay',10000)


print(m)

