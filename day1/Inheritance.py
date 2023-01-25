# Single Inheritance
class A:
    def m1(self):
        print("This is m1 method")


class B(A):
    def m2(self):
        print("This is m2 method")


b = A()
b.m1()

obj = B()
obj.m1()
obj.m2()


# Example 2

class Addition:
    a, b = 10, 200

    def addition(self):
        print(self.a + self.b)


class Multiplication(Addition):
    x, y = 10, 5

    def mul(self):
        print(self.x * self.y)


obj = Multiplication()
obj.addition()
obj.mul()


# Mult-inheritance Inheritance

class Addition:

    def addition(self):
        print("This is Addition Method")


class Multiplication(Addition):

    def mul(self):
        print("This is Multiplication Method")


class Subtraction(Multiplication):

    def sub(self):
        print("This is Subtraction method")


obj = Subtraction()
obj.mul()
obj.addition()
obj.sub()


# Hierarchical Inheritance


class A:

    def m1(self):
        print("This is M1 Method")


class B(A):

    def m2(self):
        print("This is m2 Method")


class C(A):

    def m3(self):
        print("This is m3 Method")


obj = C()
obj.m1()
obj.m3()

obj = B()
obj.m2()
obj.m1()


# Multiple Inheritance


class A:

    def m1(self):
        print("This is M1 Method")


class B:

    def m2(self):
        print("This is m2 Method")


class C(A, B):

    def m3(self):
        print("This is m3 Method")


obj = C()
obj.m1()
obj.m2()
obj.m3()


# Super method

class A:

    def add(self):
        print("This is add Method")


class B(A):

    def sub(self):
        print("This is sub Method")
        super().add()


obj = B()
obj.sub()


# Example 2

class Add:
    a, b = 10, 20


class Sub(Add):
    i, j = 500, 100

    def m1(self, x, y):
        print(x + y)
        print(self.i - self.j)
        print(self.a + self.b)


obj = Sub()
obj.m1(20, 30)

# example 3
# If all variables is same condition

a, b = 80, 10


class Add:
    a, b = 10, 20


class Sub(Add):
    a, b = 5000, 1000

    def m1(self, a, b):
        print("local Variables is :", a + b)  # local Variables
        print("class Variables is :", self.a + self.b)  # class Variables
        print("Parent class Variables is :", super().a + super().b)  # parent class Variables
        print("global class Variables is :", globals()['a'] + globals()['b'])  # global Variables


obj = Sub()
obj.m1(50, 25)


# example 4

class D:

    def __init__(self):
        print("This is class D Method")

class E:

    def __init__(self):
        print("This is class E Method")

    def display(self):
        print("This is display method")

class F(D,E):

    def __init__(self):
        print("This is class F Method")
        super().__init__()
        super().display()
        # D.__init__(self)
        # E.__init__(self)


obj = F()
