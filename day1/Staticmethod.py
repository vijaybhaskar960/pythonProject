
class Test:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def mul(i,j):
        return i*j

obj = Test()
print(obj.add(10,50))
print(Test.add(25,80))

print(Test.mul(20,5))
print(Test.mul(20,50))

class A:
    def __init__(self,a):
        self.a = a
    @staticmethod
    def method(x):
        return x*2

obj = A(10)
print(A.method(8)) # 16

