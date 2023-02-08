
# Write a Python function to sum all the numbers in a list.
def sum_list(list):
    sum = 0
    for i in list:
        sum = sum+i
    print("Sum of list is:",sum)

(sum_list([45,78,45,1,200]))

# Python: Add two given lists using map and lambda
l1 =[1,5,6]
l2 = [2,5,8]

result = map(lambda x,y:x+y,l1,l2)
print(list(result))

#  Multiplication table (from 1 to 10) in Python
num = 12
for i in range(1,11):
    print(num,"*",i,"=",num*i)


s = "Welcome"
if s==s[::-1]:
    print("This is palidrome")
else:
    print("Not a palidrome")

# Python Program to Remove Punctuation from a String
punctuations="''''''!@#$%^&*()_+,."
# mystr=input("Enter the string:")
#
# new_str = " "
#
# for c in mystr:
#     if c not in punctuations:
#         new_str+=c
# print(new_str)

# Program to print half pyramid using *
rows = 5
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print()

dic = {"name":"Vijay","Another_name":"Vishu Reddy", "Dep":"Civil"}

# Access both key and value using items() from dict
for i,j in dic.items():
    print(i,j,sep=":")

# Python program to reverse a number
num =8074517920
c= str(num)[::-1]
print(c)

# Write a NumPy program to generate random integers between 1 and 300.
import numpy as np
x = np.random.randint(low=1,high=300,size=10)
print(x)

# Write a Python program to detect the number of local variables declared in a function.

# local variable inside func
# global variable outside func

c=10
def vijay():
    x=2
    y=89
    z=40
    v = "Reddy"
print(vijay.__code__.co_nlocals)


# Python: Remove all whitespaces from a string
s = "Python is My Life"
m = re.sub("\s+",'',s)
print(m)

#Python: Get the current time
import datetime
print(datetime.datetime.now().today())

# Check if the first and last number of a list is the same

number = [2,45,23,89,2]
def first_last_number(number):
    first = number[0]
    last = number[-1]
    if first==last:
        return True
    else:
        return False

print(first_last_number(number))

#Python: Get the smallest number from a list
f = [1,2,3,4,5,-1]
print(min(f))
#Second Method

def smallest(f):
    min = f[0]
    for i in f:
        if i<min:
            min=i
    return min
print(smallest(f))

my_list = [1, 2, 3, 4, 5, 6]
for i in my_list:
    print(i,end=" ")


print([{} for i in range(0,10)])

#Python: Extend a list without append
l1=[1,2,3]
l2=[3,4,5]
l1[:0]=l2
print(l1)

l1 = l1.append(l2)
print(l1)


'''
find all numbers which are divisible by 7 but are not a multiple of 5.
'''

l = []
for i in range(1,1000):
    if i%7==0 and i%5!=0:
        l.append(str(i))
print(",".join(l))


# Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def upper_lower_cases(s):
    d={"Upper case":0,"Lower case":0}
    for i in s:
        if i.isupper():
            d["Upper case"]+=1
        elif i.islower():
            d["Lower case"]+=1
        else:
            pass
    print("Upper case letters is :",d["Upper case"])
    print("Lower case letters is :",d["Lower case"])

upper_lower_cases("This is Python Life Channel")


#Python program to triple all numbers of a given list of integers. Use Python map.
num =(1,2,3,4,5,6,7,8)
result=map(lambda x:x+x+x,num)
print(list(result))




my_string = '''The only way to
learn to programing is
by writing codes.'''

print(my_string)

# Python Program to Trim Whitespace From a String
# Using strip()

M = " This is my new world "
print(M)
print(M.strip())

# Python Program to Iterate Through Two Lists in Parallel
# Using zip (Python 3+)

list_1 = [1, 2, 3, 4, 5]
list_2 = ['a', 'b', 'c']

for i, j in zip(list_1, list_2):
    print(i, j)

num = '963969'
n = num.count(num)
print(n)

# Python Program to Capitalize the First Character of a String
# Using list slicing

String = "python is very easy Language"

print(String[0].upper()+String[1:])


my_string = "Python4DataScience"
print(my_string.count("a"))

count = 0
my_string1 = "Python4DataSciencennn"
char = "n"

for i in my_string1:
    if i==char:
        count = count+1
print(count)

# Delete a Particular file Using the OS Module
import os

# file = os.remove(r'C:\Users\Vijay Bhaskar Reddy\PycharmProjects\pythonProject\Unknown\reddy.py')
# print(file)

# write a program to count a number repeat a word in give dictionary

def count_word(dictionary, word):
    count = 0
    for key, value in dictionary.items():
        if key == word:
            count += 1
        elif value == word:
            count += 1
    return count

example_dictionary = {'apple': 'red', 'banana': 'yellow', 'apple': 'green'}
word = 'apple'

print(count_word(example_dictionary, word))


def count_word(dict,word):
    count = 0
    for key,value in dict.items():
        if key == word:
            count +=1
        elif value == word:
            count += 1
        return count
example_dictionary = {"apple":"red",'banana':'yellow','apple':'green','pink':'orange'}
word = 'apple'

print(count_word(dict,word))


l = [1,4,5,8,9,7,9,5,2,3]

sum = 0
for i in l:
    sum = sum+i
print("Sum of the list is:",sum)


class A:
    def test(self):
        print('This is Class A Method')
class B(A):
    def test(self):
        print("This is Class B Method")
obj = B()
print(obj.test())




