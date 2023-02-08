from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def display(self):
        pass


class B(A):
    def display(self):
        print("This is Display method from Class B")


obj = B()
obj.display()


# Approach 2


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass


class Tiger(Animal):
    def eat(self):
        print("eat Non Veg")


class cow(Animal):
    def eat(self):
        print("eat veg")


t = Tiger()
t.eat()

c = cow()
c.eat()


# Approach 3

class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass


class Y(X):

    def m1(self):
        print("This is M1 method")

    def m2(self):
        print("This is M2 method")


y = Y()
y.m1()
y.m2()


# Approach 4

class cal(ABC):

    def __init__(self, value):
        self.value = value

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass


class C(cal):
    def add(self):
        print(self.value + 100)

    def sub(self):
        print(self.value - 100)


obj = C(100)
obj.add()
obj.sub()


class Student(ABC):
    @abstractmethod
    def add(self,a,b):
        pass


class Teacher(Student):

    def add(self,a,b):
        print(a*b)


obj = Teacher()
obj.add(5,8)


