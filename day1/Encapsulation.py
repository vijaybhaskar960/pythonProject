
# Private methods can be access only within method

class myClass:

    __a=10

    def display(self):
        print(self.__a)

obj = myClass()
obj.display()


class A:

    def __test(self):
        print("This is a test method")

    def test1(self):
        print("This is a test method1")
        self.__test()
obj = A()
obj.test1()

# we can access private variables outside the class indirectly using methods


class MyClass:
    __empid = 100

    def getempid(self,empid):
        self.__empid = empid

    def displayempid(self):
        print(self.__empid)

obj = MyClass()
obj.getempid(108)
obj.displayempid()






