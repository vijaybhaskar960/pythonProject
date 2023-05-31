num = 7
# 7%7 =0 and 7%1= 0

for i in range(2, num):
    if num%i == 0:
        print(num, "Not a prime number")
        break
else:
    print(num, "Prime Number")
# Second Approach
num = 10
if num%2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Print the matching the sum values

data = [2,3,6,5,4,9,8,5,1]
sum = 5

for n1 in data:
    for n2 in data:
        if n1+n2 == sum:
            print(n1,n2)


# Print the list contains names of last names only

names = ["Vaishu Reddy", "Vijay Reddy","Chandrababu Naidu", "Bill Gates","Rathan TATA"]
result =[]
for name in names:
    lastname = name.split(" ")[-1]
    result.append(lastname)
print(result)

# Print a Alternative number in given list
nums = [1,2,3,4,5,6,7,8,9]
print(nums[::2])

# Print a string in correct order

data = "oediv eht ekil esaelP"
print(data[::-1].title())

# Output:  Please Like The Video

row = 5
for i in range(row):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

# Calculate the sum of the all the numbers  from 1 to a given number

# s = 0
# n = int(input("Enter a value is:"))
# for i in range(1, n+1, 1):
#     s+=i
# print("sum is:", s)

#Second Approach

# n = int(input("Enter a value is:"))
# x = sum(range(1,n+1))
# print("sum is:", x)


# Check if first and last number of a list is the same

l1 = [1,2,3,4,5,6]
l2 = [9,2,4,5,6,9]

def First(numbers):
    print("Given list", numbers)
    first_num = numbers[0]
    last_num = numbers[-1]
    if first_num == last_num:
        return True
    else:
        return False

l1 = [1,2,3,4,5,6]
print("result is:", First(l1))
l2 = [9,2,4,5,6,9]
print("result is:", First(l2))

# Count the total number of digits in a given number

num = 451236512789546218
count =0
while num !=0:
    num = num//10
    count = count+1
print("Total digits are :", count)

# Sceond Approach

# n = int(input("Enter a digits:"))
# print("Total digits are:", len(str(n)))

# Add a elements to list from set

x = {"Green","Apple","Orange"}
y = ["Mango","Carrot"]
x.update(y)
print(x)

# Return a new set of identical items from two sets
set1 = {10,20,30,4,50}
set2 = {50,20,10,5,6}
new_set = set1.intersection(set2)
print(new_set)

# Display the numbers divisible by 5 from a list

x = [10,29,8,65,34,78,95,45,63]
for i in x:
    if i%5 == 0:
        print(i)

# Second Approach
x = [10,29,8,65,34,78,95,45,63,86,235,452,985]
demo_list = [i for i in x if i%5 == 0]
print(demo_list)

# Print a Fibonacci Series
n = 10
a,b = 0,1
while a<n:
    print(a, end=' ')
    a, b = b, a+b

# Swap two numbers

a = 10
d = 50

a, d = d, a
print(a)
print(d)

# Convert Decimal value to Binary Value
decimal_num = 42
binary_num = bin(decimal_num)

print(binary_num)  # '0b101010'
binary_num = bin(decimal_num)[2:]
print(binary_num)

# Write program to count the number of times a class is called
class A:
    count =0
    def __init__(self):
        A.count +=1
        print("Class is called")

a1 = A()
a2 = A()
print(A.count)

# find a duplicate values in the below list

l1 = ["india", "is", "my", "country"]
m = "".join(l1)
print(m)

duplicate =[]
for char in m:
    if m.count(char)>1 and char not in duplicate:
        duplicate.append(char)

print(duplicate)


# find a unique values in the below string

s = "test"
unique =[]
for char in s:
    if s.count(char) == 1 and char not in unique:
        unique.append(char)
print(unique)

# print the values startswith "i"

list1 = ["india", "is", "my", "country"]
list2 = [word for word in list1 if word.startswith('i')]
print(list2)

# Print factorial of a number

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))
l1 = [1,2,3]
l2 = ['a','b','c']

# output ['a1','b2','c3']

new_list = [str(l2[i])+str(l1[i]) for i in range(len(l1))]
print(new_list)

# Write python function to count the number of vowels in a given string

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count +=1
    return count
print(count_vowels("developer"))


number = input("Enter phone number: ")

if number.startswith("+91") and len(number) == 13 and number[1:].isdigit():
    print("The given number is an Indian number starting with +91.")
else:
    print("The given number is not an Indian number starting with +91.")

l = ["Vijay", "Job", "Kala", "Demo", "Onion", "Ball", "Car", "Egle", "reddy",'apple']

# Selection sort algorithm to sort list alphabetically (case-insensitive)
for i in range(len(l)):
    min_index = i
    for j in range(i+1, len(l)):
        if l[j].lower() < l[min_index].lower():
            min_index = j
    l[i], l[min_index] = l[min_index], l[i]

# Print sorted list
print(l)

import re

def is_indian_number(number):
    # Regular expression to match Indian phone numbers
    regex = r"^(\+91|0)?[6789]\d{9}$"
    # Check if the number matches the regex
    if re.match(regex, number):
        return True
    else:
        return False
print(is_indian_number('+919603449098'))





