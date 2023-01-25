class A:

    def m1(self):
        print("This is m1 method")

class B(A):

    def m1(self):
        print("This is m1 method for class B")


obj = B()
obj.m1()
obj.m1()