
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

class A:
    def __init__(self):
        self.__fname="vijay"
        self.__lname="bashker"
    # #getter
    # @property
    # def fname(self):
    #     return self.__fname
    # #setter
    # @fname.setter
    # def fname(self,fname):
    #     self.__fname=fname
    #
    # # getter
    # @ property
    # def lname(self):
    #     return self.__lname
    # # setter
    # @lname.setter
    # def lname(self, fname):
    #     self.__lname = fname

    def display(self):
        print(self.__fname,self.__lname)

a=A()

a.display()
a.__fname = "Raju"
print(a.__fname)
# a.fname="gangadhar"
#
# print(a.fname)
# print(a.lname)
# a.lname="koudk"
# print(a.lname)