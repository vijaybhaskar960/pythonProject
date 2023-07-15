
# Private methods can be access only within method
class A:

    __a = 10

    def display(self):
        print(self.__a)


obj = A()
obj.display()



class Myclass:

    def __test(self):
        print("This is test Method")

    def display(self):
        print("This is Display Method")
        self.__test()


obj = Myclass()
obj.display()

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
    #getter
    @property
    def fname(self):
        return self.__fname
    #setter
    @fname.setter
    def fname(self,fname):
        self.__fname=fname

    # getter
    @ property
    def lname(self):
        return self.__lname
    # setter
    @lname.setter
    def lname(self, fname):
        self.__lname = fname

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

"""
200 ok
201 created
202 accepted
 
400 Bad request
401 unauthrized
402 payment request
403 Forbidden
404 not found

500 internal server error
501 not implemented
502 Bad Gateway
503 service unavailable

"""