s = "the Sky is blue"

l = s.split()
print(l)
l = l[::-1]
l = " ".join(l)
print(l)



l = [42,75,89,32,4,6,98,21]

maximum = l[0]
minimum = l[0]

for i in l:
    if i>maximum:
        maximum = i
    if i<minimum:
        minimum = i
print("maximum is :",maximum)
print("Minimum is :",minimum)


l = "Vijayreddy"
m = "Vishu"
n = l+m
print(n)

n = "VijayreddyVishu"

vowels = [i for i in n if i in "aeiou"]
print(vowels)

list = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

weekdays = [i for i in list if i in ["Monday","Tuesday","Wednesday","Thursday","Friday"]]
print(weekdays)
weekends= [i for i in list if i in ["Saturday","Sunday"]]
print("\n",weekends)

dict = {"name":"Vijaya","Dep":"IT","Salary":"50K"}
print(dict)

for i in dict:
    print(i) # Print only keys from dictionary

for i in dict:
    print(dict[i]) # Print Only Values from dictionary

for x,y in dict.items():
    print(x,y) # Print keys along with values

for i in dict.values():
    print(i) # print values only

def greeting(name,greetingmsg):
    print(greetingmsg+" "+name)

greeting(name="Vishureddy",greetingmsg="Hello")


def display(a,b,**c):
    print("A value is :",a)
    print("B value is :",b)
    print("C value is :",c)

display(10,56,)
display(15,45,name="vijaya",occupation= "Software Engineer")

def display(a,b,*c):
    print("A value is :",a)
    print("B value is :",b)
    print("C value is :",c)

display(10,56,99,56,2,3,7,89,10,23)


# Patterns

num = 1
for i in range(5):
    for j in range(i+1):
        print(num,end=" ")
        num = num+1
    num = 1
    print()

'''
output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''

for i in range(5):
    num =1
    for j in range(5,i,-1):
        print(num,end=" ")
        num = num+1
    print()

'''
Output:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

for i in range(5):
    for j in range(i,5):
        print("*",end=" ")
    print()

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''
* 
* * 
* * * 
* * * * 
* * * * * 
'''

row = 6

for i in range(row):
    for j in range(i):
        print(i,end=" ")
    print()

'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
'''

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(1,10,2):
    if i==7:
        continue
    print(i)

s = "Welcome"
Rever = " "
for i in s:
    Rever = i+ Rever
print(Rever)

print(s[::-1])


def largest(a,b):
    if a>b:
        return a,b
    else:
        return b,a
print(largest(100,45))
print(largest(200,50))

def add (a,b,**c):
    print("A value is ",a)
    print("B value is ",b)
    print("C value is ",c)

print(add(5,8,name="Vijay",dep="IT"))

class Calculator:

    # create addNumbers static method
    @staticmethod
    def addNumbers(x, y):
        return x + y

obj = Calculator()
print("Results is :",obj.addNumbers(78,40))
print('Product:', Calculator.addNumbers(15, 110))


class Addition:
    @classmethod
    def sub(cls,x,y):
        print("Multiplication results is:",x*y)

Addition.sub(4,8)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
# even_numbers = list(even_numbers_iterator)

# print(even_numbers)

names = ['vijay','roji','joshnna','reddy']

l = [i for i in names if i.startswith('r')]
print(l)

n = [i for i in names if i.startswith("j")]
print(n)


b = "welcome"

if (b==b[::-1]):
    print("Palidrome")
else:
    print("Not a palidrom")

for i in range(1,6):
    print('*'*i)
