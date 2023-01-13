class A:
    def display(self):
        print("This is a display Method")

obj = A()
obj.display()

x,y = 10,50
class One:
    name = "Vijay and Vishu "
    def __int__(self,a):
        self.a = a

    def add(self):
        print("Instance variables:",self.a)
        print("Static variable:",self.name)
obj1 = One()
print(obj1.name)

'''
1. self is used to reffer the instance of the class to the method.
2. Based on self only the method will get to know for which instace it has to responce.
3. We can give any name in place of self.
'''
# class One():
#     def sub(self,a, b):
#         print(' \n ID of self is : ', id(a))
#         print(' \n A value is :', a)
#         print(' \n A value is :', b)
#
#
#
# ins1 = One()
# ins2 = One()
#
# print(' \n ID of ins1 is  : ', id(ins1))
# ins1.sub(10,5)
# ins2.sub(100,200)
'''
Using __init__ we can create constructor.
Using constructor we can create instance varables.
Constructor method will call when calling class.
'''
class One:

    def __init__(self, name, eid):
        self.name = name
        self.eid  = eid
        print('__init__')

    def add(self):
        print(' Add ', self.name)

    def sub(self):
        print(' SUB ', self.name)
        print(' SUB EID ', self.eid)


inst = One('vijay', 999)
inst.add()
inst.sub()
inst.sub()

'''
1. Using inheritance we can get parent class properties into child class.
'''

class A:
    name = "Prasad Reddy"
    def m1(self):
        print("This is m1 for class A Method")

    def m2(self):
        print("This is m2 for class A Method")
class B(A):
   def add(self):
       a = 10
       b = 5
       c = a+b
       print(c)

obj = B()
obj.m1()
# obj.m2()
# obj.add()
# print(obj.name)

'''
1. We can inherit a derived class from another derived class, this process is known as multilevel inheritance
2. Example :- We have three classes A, B and C, If you inheritance class A into class B and class B into class C This is called Multi Level inheritance.
'''


class C:
    def display(self):
        print(" This is the Display Method")

class D(C):

    def add(self):
        print("This is the Add Method")

class E(D):

    def sub(self):
        print("This is the Sub Method")

obj = E()
obj.display()
obj.sub()
obj.add()

'''
1. If you have same method names in class A and class B, then if you Inheritence class A into class B then Class A method will override with class B method.
'''

class A:
    def add(self):
        print("This is a Add method")

class B:
    def add(self):
        print("This is a Add Method")

class C(A,B):
    def add(self):
        print("\n C class")

obj =C()
obj.add()

class Car:
    def color(self):
        print("Red color")

    def music(self):
        print("Sony")

    def brand(self):
        print("Audi")

class Audi(Car):
    def color(self):
        print("White Color")

    def music(self,a):
        print("Philips",a)

    def interior(self):
        print("Vishu interior")

class Volvo(Car):
    def color(self):
        print("Orange")
    def music(self):
        print("JBL")

    def brand(self):
        print("Volvo")

inst = Car()
inst1 =Audi()
inst2 = Volvo()
inst.music()
inst1.music("Yellow")
inst2.music()

''' Using the @classmethod decorator we can create a class method.
1. For class method we have to give a cls arugments.
2. Using the class method we can change attributes.
3. class method we can call through instance or without instance.
'''


class One():
    name = 'Vishu'
    @classmethod
    def add(cls):
        print("Id of One",id(One))
        print("Id of One",id(cls))
        # cls.name = r
        print("\n Class Variables",One.name)

obj = One()
obj.add()
print(obj.name)

''' Using the @staticmethod decorator we can create a static method.
1. For static method does not requried self arugments
2. Using Static method we can provide a same behaviour to the all the instances of class.
3. static method we can call through instance or without instance.
'''

class One():
    @staticmethod
    def add():
        print('\n staticmethod')
inst = One()
inst.add()
One.add()

# Global variable access scenario
x,y = 10,50
name = "Reddy"
class global_var:
    i,j = 20,5
    def display(self):
        a,b = 20,50
        print("display method")
        print(self.i*self.j)
        print(a+b)
        print(globals()['x']-globals()['y'])
        print(globals()['name'])

obj = global_var()
obj.display()













