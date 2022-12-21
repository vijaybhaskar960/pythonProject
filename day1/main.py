h ="Hello World"
print(h)

# for i in range(2,10,2):
#     print(i)
#
#
# for i in range(1,10):
#     if i==5 or i==4:
#         break
#
#     print(i)

# Swaping the two numbers

x = 5
y = 9
x,y = y,x

print("x :",x)
print("y :",y)

# Find out given number is Odd or Even

# number = int(input("Enter a any number :"))
number = 45
if number%2 ==0:
    print("Even number")
else:
    print("Odd Number")

#
# Factorial of a number

num = 4

factor = 1
for i in range(1,num+1):
    factor = factor*i
print("The factorial of ",num,'is',factor)

#
# How to find out list of a lenth

""" Search in element in list """

list = [3,4,5,6,78,8,9,9,78]

print(len(list))

D = ['amazon','flipkart','myntra','ajio','netflix']

platform = "ajio"

if platform in D:
    print("This is fashon business app")
else:
    print("Not work properly")

"Palindrome"

string = "Welcome"

if(string == string[::-1]):

    print("The string is a palindrome")
else:
    print("This is not a Palindrome")

"Separate the String and numbers in given list"

names = []
numbers = []

l = ['vijaya',34547,'amazon',456283,'flipkart',78906,'myntra', 65547]

for i in l:
    if type(i)==str:
        names.append(i)
    if type(i)==int:
        numbers.append(i)
print("Separaion of numbers are:",numbers,"\nSeparation of names :",names)

"Write a python program to print duplicates present in list"

list = ['hello',20,90,89,78,56,45,20,90]

d = []
for i in list:
    if list.count(i)>1:
        d.append(i)
print(d)


class A:
    def test(self):
        print("This One Method")

    def exam(self):
        print("this second method")

class B:
    def study(self):
        print("This is new world")

    def evning(self):
        print("This not new world")

obj = A()
obj1 = B()
obj.test()
obj1.evning()

# How to convert the list data one type to another type

list = ['2','5','6','8','9']

list = [int(i)for i in list]
list.sort()
print(list)

list = [float(i)for i in list]
list.sort()
print(list)

# Pattern type list

# list = [5,1,7,3]
# string = ""
#
# for i in list:
#     string += str(i)
#     print(string)


num = int(input("enter a vale :"))

print("Even Number") if num%2 ==0 else print("Odd Number")


names = ['vijay','roji','joshnna','reddy']

l = [i for i in names if i.startswith('r')]

print(l)


str1 = "Vijay"
str2 = "Bhavani"

str = str1+str2
print(str)
def printvowels(str):
    for char in str:
        if char in "aeiouAEIOU":
            print(char,end=" ")
    return char
printvowels(str)


# Second Method
vowels =[i for i in str if i in "aeiou"]
print(vowels)


A = "Vijaya"
B = "Vishu"
c = ' '.join([A+B])
print(c)

def printvowels(c):
    for char in c:
        if char in "aeiouAEIOU":
            print(char,end=" ")
    return char
printvowels(c)






rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

list = ['hello',20,90,89,78,56,45,20,90]

d = []
for i in list:
    if list.count(i)>1:
        d.append(i)
print(d)