# Inheritance

class A:

    def m1(self):
        print("This is m1 Method")

class B(A):

    def m2(self):
        print("This is m2 Method")
        super().m1()
       # A.m1(self)

obj = B()
obj.m2()

# Multi-Inheritance

class Fly:

    def fly(self):
        print("Parrot can fly")

class Non_Fly(Fly):

    def NotFly(self):
        print("Hen can't Fly")

class Live(Non_Fly):

    def live(self):
        print("Live the method")

obj = Live()
obj.live()
obj.NotFly()

# Multiple Inheritance

class X:

    def add(self):
        print("This is Add Method")

class Y:

    def sub(self):
        print("This is Sub Method")

class Z(X,Y):

    def mul(self):
        print("This is Mul Method")


obj = Z()
obj.mul()
obj.sub()
obj.add()

# Hierarchy

class Amazon:

    def big_billion(self):
        print("This is Big Billion Method")

class Flipkart(Amazon):

    def flipkart(self):
        print("This is Flipkart Method")

class Myntra(Amazon):

    def Myntra(self):
        print("This is Myntra Method")


obj = Myntra()
obj.Myntra()
obj.big_billion()

obj = Flipkart()
obj.big_billion()
obj.flipkart()

# If all variables is same condition

a, b = 10, 20

class Add:
    a, b = 50, 30

class Sub(Add):
    a, b = 2000, 1000

    def display(self,a, b):
        print("local variables is:",a + b)
        print("class variables is:",self.a+self.b)
        print("Parent class variables is:", super().a + super().b)
        print("global variables is:",globals()['a'] + globals()['b'])


obj = Sub()
obj.display(80,10)


# example 4

class D:

    def __init__(self):
        print("This is class D Method")


class E:

    def __init__(self):
        print("This is class E Method")

    def display(self):
        print("This is display method")


class F(D, E):

    def __init__(self):
        print("This is class F Method")
        super().__init__()
        super().display()
        # D.__init__(self)
        E.__init__(self)

obj = F()

# Example

i, j = 3, 4

class Myclass:
    a, b = 50, 10

    def __int__(self):
        self.a = 1
        self.b = 2
        print(self.a + self.b)


    def add(self,a,b):
        print(a-b)
        print(self.a+self.b)
        print(globals()['i']+globals()['j'])
        super().__init__()


obj1 = Myclass()
obj1.add(2,3)











