def add():
    a = 10
    b = 50
    c = a+b
    print(c)
add()


def mul(a,b):
    print("A value is :", a)
    print("B value is :", b)

mul(5,8)

def sub(x,y):
    x=x
    y=y
    z =x-y
    print(z)
sub(200,50)


def sum(a,b,c):
    print("a value is :",a)
    print("b value is :",b)
    print("c value is :",c)
sum(5,8,3)
sum(c=45,a=89,b=42)

'''
1. using args(*) we can takes N number of arguments
2. it will take 0 to many values in tuple format
'''


def display(x,y,*z):
    print("X value is :",x)
    print("Y value is :",y)
    print("Z value is :",z)

display(4,7,3,"vijay",45,89,100,32)

'''
1. using kwargs(**) we can take values in dictionary format
'''
def add(a, b=5,*c, **d):
    print(' A value is : ', a)
    print(' B value is : ', b)
    print(' C value is : ', c)
    print(' D value is : ', d)

add(6,7,3,67,9, name='Vijay', eid=56, empsal="90k",edep="IT")

print("Vijay,Vishu")




