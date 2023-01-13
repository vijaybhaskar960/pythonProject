
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


