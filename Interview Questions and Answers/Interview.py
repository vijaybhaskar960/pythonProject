class A:
    def m2(self):
        print("this is m1 method")


class B(A):
    def m1(self):
        print("This is M2 Method")


obj = B()
obj.m1()
obj.m2()

s = "The network vlan is 10.234.23.41 8080"

import re

p = '\d+[.]\d+[.]\d+[.]\d+\s\d+'
l = re.findall(p, s)
for i in l:
    print(i)

# Output :10.234.23.41 8080

s = "aabbbccddaa"
c = 1
x = " "
print(len(s))
for i in range(len(s) - 1):
    # print(i)
    if s[i] == s[i + 1]:
        c += 1
    else:
        x = x + str(c) + s[i]
        c = 1
x = x + str(c) + s[i + 1]
print(x)

# output :2a3b2c2d2a


String = "PrasadReddy"

print(String[0:2], String[-2:])


def add(String):
    if len(String) < 2:
        return " "
    return String[0:2] + String[-2:]


print(add("PrasadReddy"))

# Sum of a list values
l = [45, 78, 2, 39, 6, 45, 82, 31, 93]


def sum():
    sum_num = 0
    for i in l:
        sum_num = sum_num + i
    print(sum_num)


sum()

#
# # num = int(input("Enter a number is :"))
#
# if num>0:
#     print("Positive Number")
# elif num==0:
#     print("Zero")
# else:
#     print("Negative number")

num = 96
print("Even Number") if num % 2 == 0 else print("Odd Number")

# Python Program to Check Leap Year
#
# year = int(input("Enter a year is :"))
#
# if (year%4==0) and (year%100 !=0) or (year%400==0):
#     print("Leap year")
#
# else:
#     print("Not a leap year")


String = "python is very easy Language"

print(String[0].upper()+String[1:])

num =19
for i in range(1,11):
    print(num,"X",i,"=",num*i)


for i in range(0,5):
    print(i,)



