class A:
    def m2(self):
        print("this is m1 method")


class B(A):
    def m1(self):
        print("This is M2 Method")


obj = B()
obj.m1()
obj.m2()



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

year = int(input("Enter a year is :"))

if (year%4==0) and (year%100 !=0) or (year%400==0):
    print("Leap year")

else:
    print("Not a leap year")



num =19
for i in range(1,11):
    print(num,"X",i,"=",num*i)


for i in range(0,5):
    print(i,)



