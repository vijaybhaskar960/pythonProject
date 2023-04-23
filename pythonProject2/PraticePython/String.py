s = "Welcome"
print(s[::-1])
reverse = ""
for i in s:
    reverse = i + reverse
print(reverse)

m = 'this sky is bule'
l = m.split()
l = l[::-1]
n = " ".join(l)
print(n)

v = "aaabbbcccddeev"

output = ""
count = 1
char = v[0]

for ch in v:
    if ch == char:
        count += 1
    else:
        output = output + str(count) + char
        count = 1
        char = ch
print(output)

import re

s = "my name is Vijay and age 26 my friend Hari and age 28"

pattern = "\d+"
result = re.findall(pattern, s)
print(result)

m = "Python"
if m == m[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

import re

s = "my name is Vijay and age 26 my friend Hari and age 28"
pattern = r"\b[A-Z][a-z]*\b"
result = re.findall(pattern, s)
print(result)

import re

m = "my name is Vijay and age 25 and Hari age 26"
pattern = "\d+"
n = re.findall(pattern, m)
print(n)
pattern = r"\b[A-Z][a-z]*\b"
r = re.findall(pattern, m)
print(r)

y = "This is ip address 192.168.10.120"
t = re.findall(r"\d+[.]\d+[.]\d+[.]\d+", y)
print(t)

def repeated_string(s):
    words = s.split()
    word_list = []
    repeat_list = []

    for word in words:
        if word not in word_list:
            word_list.append(word)

        else:
            if word not in repeat_list:
                repeat_list.append(word)

    return repeat_list


print(repeated_string("This is my name and is age"))

String = "PrasadReddy"

print(String[0:2], String[-2:])

String = "python is very easy Language"
print(String[0].upper() + String[1:])


# Compare two strings matching character
from itertools import zip_longest
data1 = "Python"
data2 = "Pytha"

i = 1
for x, y in zip_longest(data1, data2, fillvalue=" "):
    if x != y:
        print(x,y,"-",i)
        i = i+1

s = " Hello Vaishu "
s = s.strip()
print(s)

s = "  hello Dharshana   "
s = s.lstrip()
print(s)  # "hello world   "

s = "  hello Reddy   "
s = s.rstrip()
print(s)  # "  hello world"


s = "aaahello worldaaa"
s = s.strip('a')
print(s)  # "hello world"

# Write python function to count the number of vowels in a given string

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count +=1
    return count
print(count_vowels("developer"))

# find a unique values in the below list

s = "test"
unique =[]
for char in s:
    if s.count(char) == 1 and char not in unique:
        unique.append(char)
print(unique)



# find a duplicate values in the below list

l1 = ["india", "is", "my", "country"]
m = "".join(l1)
print(m)

duplicate =[]
for char in m:
    if m.count(char)>1 and char not in duplicate:
        duplicate.append(char)

print(duplicate)

