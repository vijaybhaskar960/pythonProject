# import turtle
# import time
# m = turtle.Turtle()
# m.shape("turtle")
# time.sleep(10)
# m.color("bule")
#
# time.sleep(10)

i = 0
while i<11:
    print(i)
    i = i+1


# i = 10
# while i>=1:
#     if i == 6:
#         continue
#     print(i)
#     i = i-1


num = int(input("Enter a table number :"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)


for i in range(1,101):
    print(i,end=",")
