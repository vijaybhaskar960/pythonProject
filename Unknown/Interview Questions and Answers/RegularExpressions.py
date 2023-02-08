
# Program to extract numbers from a string

import re
string = 'hello 12 hi 89. Howdy 34'
result = re.findall("\d+",string)
print(result)


string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string)
print(result)



string = 'Twelve:12 Eighty nine:89.'
pattern = '\d+'
result = re.split(pattern, string,1)
print(result)

# Program to remove all whitespaces

string = 'abc 12\
de 23 \n f45 6'
result = "\s+"
replace = ""
m = re.sub(result,replace,string)
print(m)


#  Three digit number followed by space followed by two digit number

string = '39801 356, 2102 1111'
pattern = "(\d{3}) (\d{2})"
result = re.search(pattern,string)
print(result.group())


string = "Python is fun"
# check if 'Python' is at the beginning
match = re.search('\APython', string)

if match:
  print("pattern found inside the string")
else:
  print("pattern not found")


string = '\n and \r are escape sequences.'

result = re.findall(r'[\n\r]', string)
print(result)


print(1,2,3,end=" ")

for i in range(0,5):
  print('\n',i,end="")

print(end="")

n = "Vijay"
print(n.isalnum())


l = "ABC&#$DEF"
n =l[2::-1]+l[3:6]+l[6:][2::-1]
print(n)


s = "The network vlan is 10.234.23.41 8080"

import re

p = '\d+[.]\d+[.]\d+[.]\d+\s\d+'
l = re.findall(p, s)
for i in l:
    print(i)

# Output :10.234.23.41 8080


import re

s = "Welcome123 reddy 192.168.10.12 8000"
r = ".+"
mo = re.findall(r,s)
print(mo)

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
#
# print(even_numbers)

import functools
f = filter(lambda x:x%2==0,range(1,11))
print(f)


f = list(filter(lambda x:x%2==0,range(1,11)))
print(f)

numbers = [1,5,6,8]
R = functools.reduce(lambda x,y:x+y,numbers)
print(R)

