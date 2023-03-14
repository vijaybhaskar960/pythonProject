
l = [1, 2, 3, 4, 1, 2, 3]

count = 0
for i in l:
    count += 1
print(count)

sum = 0
for i in l:
    sum = sum + i

print(sum)

mul = 1
for i in l:
    mul = mul * i
print(mul)

duplicate_value = []
unique_value = []
for i in l:
    if i not in unique_value:
        unique_value.append(i)
    else:
        if i not in duplicate_value:
            duplicate_value.append(i)
print(duplicate_value)

new_list = ['Vaishu', 1, 2, 3, "Vijay"]
String = []
value = []
for i in new_list:
    if isinstance(i, str):
        String.append(i)
    if isinstance(i, int):
        value.append(i)
print(String)

l = [4, 5, 56, 78, 90]

maximum = l[0]
minimum = l[0]
for i in l:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i
print(maximum)

a = [x for x in range(0, 10, 2)]
print(a)

b = [x for x in range(0, 10) if x % 2 == 0]
print(b)

words = ['hello', 'vaishu', 'im waiting for you']
e = [x.upper() for x in words]
print(e)

num = [1, 2, 3]
d = [x * 10 for x in num]
print(d)

keys = [1, 2, 3]
values = ['a', 'b', 'c']
print(dict(zip(keys, values)))

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)

keys = [1, 2, 3, 4]
values = ['a', 'b', 'c']
my_dict = {}
for i in range(min(len(keys), len(values))):
    my_dict[keys[i]] = values[i]
print(my_dict)

d = {'a': 11, 'b': 22, 'c': 22, 'd': 44}
for key, value in d.items():
    if value == 22 and key == "c":
        d[key] = '33'
print(d)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 3}
duplicate_value = {}
for value in my_dict.values():
    keys = [key for key, val in my_dict.items() if val == value]
    if len(keys) > 1:
        duplicate_value[value] = keys
print(duplicate_value)

s = "welcome"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

m = "this sky bule"
n = m.split()
l = n[::-1]
print(l)

import re

m = "my name is Vijay and age 25 and Hari age 26"
pattern = "\d+"
n = re.findall(pattern, m)
print(n)
pattern = r"\b[A-Z][a-z]*\b"
r = re.findall(pattern, m)
print(r)

v = 'aaabbccddeeffcc'

output = ''
count = 0
char = v[0]

for ch in v:
    if ch == char:
        count += 1

    else:
        output = output + str(count) + char
        count = 1
        char = ch
output = output + str(count) + char
print(output)

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

num = [1, 2, 3, 4]
g = map(lambda x: x * 2, num)
print(list(g))

h = filter(lambda x: x % 2 == 0, num)
print(list(h))

from functools import reduce

i = reduce(lambda x, y: x + y, num)
print(i)

a, b = 10, 200


class A:

    def add(self):
        print("This is Add Method")


class B(A):

    def sub(self):
        print("This is Sub Method")
        print(a + b)


obj = B()
obj.add()
obj.sub()


class C:

    def amazon(self):
        print("This is Amazon")


class D(C):

    def flipkart(self):
        print("This is flipkart")


class E(D):

    def snapdeal(self):
        print("This is snapdeal")


obj = E()
obj.amazon()
obj.flipkart()
obj.snapdeal()


class Vai:

    def m1(self):
        print("M1 method")


class Vij(Vai):

    def m2(self):
        print("M2 method")


class Man(Vai):
    def m3(self):
        print("M3 method")


obj = Man()
obj.m3()
obj.m1()


class Demo:
    def n1(self):
        print("This is n1 method")


class Live:
    def n2(self):
        print("This is n2 method")


class Boss(Demo, Live):
    def n3(self):
        print("This is n3 method")


obj = Boss()
obj.n3()
obj.n2()
obj.n1()


@staticmethod
def q():
    print("values")


q()


class H:
    name = "vijay"

    @classmethod
    def ego(cls):
        print("Ego Method")
        print(cls.name)


H.ego()

from abc import ABC,abstractmethod

class Q(ABC):

    @abstractmethod
    def add(self):
        pass

class R(Q):
    def add(self):
        print("This is Abstractmethod")

obj = R()
obj.add()

def upper(func):
    def inner():
        Str = func()
        return Str.upper()
    return inner

@upper
def display():
    return "hello python world"
print(display())

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)

dict = {}
for i in range(min(len(keys),len(values))):
    dict[keys[i]] = values[i]
print(dict)

filter_dict = {k:v for k, v in dict.items() if v>2 }
print(filter_dict)

l = [1,2,3,4]

f = map(lambda x : x+2,l)
print(list(f))

r = filter(lambda x:x%2==0, l)
print(list(r))

from functools import reduce

v = reduce(lambda x,y : x+y, l)

print(v)

# num = int(input("Enter a value:"))
# num_convert = str(num)
# num_str_reverse = num_convert[::-1]
# num_reverse = int(num_str_reverse)
#
# print(num_reverse)

l = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']

# for i in range(len(l)):
#     if type (l[i]) == int and l[i]%2==0:
#         l[i] = l[i] ** 2
# print(l)

String = []
Values = []
for i in l:
    if isinstance(i,str):
        String.append(i)
    if isinstance(i,int):
        Values.append(i)
print(Values)
my_list  = [x*2 for x in Values if x%2 == 0]
print(my_list)

my_list = [10, 5, 8, 20, 15]
list_sorted = sorted(my_list,reverse=True)
third_largest = list_sorted[2]
print(third_largest)

import heapq
my_list = [10, 5, 8, 20, 15, 12]
third_largest = heapq.nlargest(5, my_list)[-1]
print(third_largest)
