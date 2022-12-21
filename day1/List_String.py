# How to convert the list data one type to another type

# w = 'Reddy'
# rever = " "

# for i in w:
#     rever = i+rever
# print(rever)
# print(w)
#
# m = w[::-1]
# print(m)
#
# tup = ('vijay','reddy','prasad')
# print(tup)

# def greetings(name,greetingmsg):
#     print(greetingmsg+" "+name)
#
# greetings(name="john",greetingmsg="Hello")
#
# class name:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print(name)
#
# obj = name()
# obj.myfun()
# obj.display("Prasad Reddy")

#
# i,j = 45,56
#
# class myclass:
#     a,b = 12,3
#
#     def add(self, x,y):
#         print(x*y)
#         print(self.a+self.b)
#         print(i+j)

# mc = myclass()
# mc.add(4,6)

#
# class emp:
#     def __int__(self,eid,ename,sal):
#         self.eid = eid
#         self.ename = ename
#         self.sal = sal
#
#     def __str__(self):
#         return (self.ename)
#
# object = emp(10,"hii",23)
# print(object)
#
#
# class Car:
#     def __init__(self, price, color, mileage):
#         self.color = color
#         self.mileage = mileage
#         self.price = price
#
#     def __str__(self):
#         return (self.color)
#
# obj = Car(100000,"Red","15Kmhs")
# print(obj)
#
# class A:
#     def m1(self):
#         print("This is a m1 method from Class A")
#
# class B:
#     def m1(self):
#         print("This is a m1 method from class B ")
#         super().m1()
#
#
# obj = B()
# obj.m1()


# List = ["Monday","Tuseday","Wendesday","Thursday","Friday","Saturday","Sunday"]
#
#
# list  = int(input("Enter a week name:"))
#
# for i in List:
#     if List in ["Monday","Tuseday","Wendesday","Thursday","Friday"]:
#         print("Weekdays")
#     else:
#         print("Weekend")


days = int(input("Enter a day number "))
if days==1:
    print("Sunday")
elif days==2:
    print("Monday")
elif days==3:
    print("Tusday")
elif days==4:
    print("Wendsday")
elif days ==5:
    print('Thursday')
elif days ==6:
    print("Friday")
elif days ==7:
    print("Saturday")
else:
    print("invalid input")