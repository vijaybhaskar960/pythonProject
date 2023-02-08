s = "Welcome"
if s == s[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

s = "aabbbccddaa"
c = 1
x = " "
print(len(s))
for i in range(len(s) - 1):
    # print(i)
    if s[i] == s[i + 1]:
        c += 1
    else:
        x = x + str(c) + s[i]
        c = 1
x = x + str(c) + s[i + 1]
print(x)

# output :2a3b2c2d2a


String = "PrasadReddy"

print(String[0:2], String[-2:])


def add(String):
    if len(String) < 2:
        return " "
    return String[0:2] + String[-2:]


print(add("PrasadReddy"))

String = "python is very easy Language"

print(String[0].upper() + String[1:])

# Python Program to Calculate the Length of String
char = "subscribe the channel"


def length_string(char):
    count = 0
    for i in char:
        count = 1 + count
    return count


print(length_string(char))

import re

n = "Vijay Vishu Reddy's"
r = re.search("\w+\s\w+\s\w+", n)

print(r.group())
# print(help('False'))


str1 = 'welcome'
print(id(str1), '\n')
str1 = str1 + 'to python'
print(id(str1), '\n')

string = "hello the python developer"
print(string.count("lo"))


# Second Approach

def find_repeated_words(string):
    words = string.split()
    word_list = []
    repeat_list = []
    for word in words:
        if word not in word_list:
            word_list.append(word)
        else:
            if word not in repeat_list:
                repeat_list.append(word)
    return repeat_list



