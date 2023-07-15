from abc import ABC, abstractmethod


class Amazon(ABC):
    @abstractmethod
    def add(self):
        pass


class B(Amazon):
    def add(self):
        print("This is Add Method")


obj = B()
obj.add()


class A:
    @staticmethod
    def sub():
        print("This is Sub Method")


A.sub()


class C:
    @classmethod
    def mul(cls):
        print("This is Mul Method")


C.mul()

l = [1, 2, 3, 4, 5]

m = map(lambda x: x + 100, l)
print(list(m))

f = filter(lambda a: a % 2 == 0, l)
print(list(f))

from functools import reduce

r = reduce(lambda x, y: x + y, l)
print(r)


class Demo:
    def add(self):
        print("A and B")


class Live(Demo):
    def Abs(self):
        print("Abs Method")


obj = Live()
obj.Abs()
obj.add()


class Myclass:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        print(self.name, self.id, self.salary)


obj = Myclass("Vaishu", "52011739", '90k')
obj.display()

keys = [1, 2, 3]
values = ['a', 'b', 'c']
print(dict(zip(keys, values)))

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 3}
new_dict = {}
for value in my_dict.values():
    keys = [key for key, val in my_dict.items() if val == value]
    if len(keys) > 1:
        new_dict[value] = keys

print(new_dict)
keys = [1, 2, 3]
values = ['a', 'b', 'c', 'd']
demo_dict = {}
for i in range(min(len(keys), len(values))):
    demo_dict[keys[i]] = values[i]
print(demo_dict)

d = {'a': 11, 'b': 22, 'c': 22, 'd': 44}
for key, value in d.items():
    if type(value) == int and key == 'c':
        d[key] = 33
print(d)

date = {
    "name": "Vijay",
    "Depart": "IT",
    "Salary": "50k",
}

print(date['name'])
print(date.get('Dep'))

l = [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

for i in range(len(l)):
    if type(l[i]) == int and l[i] % 2 != 0:
        l[i] = l[i] ** 2

print(l)

l = [9, 8, 7, 'Vaishu', 'Vijay']
string = []
value = []
for i in l:
    if isinstance(i, str):
        string.append(i)

    else:
        if isinstance(i, int):
            value.append(i)

print(string)
print(value)

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l1 = []
for i in l:
    if isinstance(i, int):
        l1.append(i)
    else:
        l1.extend(i)
print(l1)

l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

new_tuple = [ele for tup in l for ele in tup]
print(new_tuple)

list1 = [1, 2, 3, 4]
list2 = [6, 2, 5, 1]

new_list = [n for n in list1 if n in list2]
print(new_list)

l = [1, 2, 3, 4, 1, 5, 2, 3, 1]

for i in l:
    if i == 1:
        l.remove(i)
        l.append(i)
print(l)

s = 'KARRAK1'
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

reverse = ''
for i in s:
    reverse = i + reverse
print(reverse)

m = 'This is sky blue'
n = m.split()
o = n[::-1]
p = ' '.join(o)
print(p)

v = "aaabbbcccddeev"

output = ''
count = 0
char = v[0]

for ch in v:
    if ch == char:
        count = count + 1
    else:
        output = output + str(count) + char
        char = ch
        count = 1

print(output)

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def demo(self):
        pass


class B(A):

    def demo(self):
        print("This is Demo Method")


obj = B()
obj.demo()


def upper(func):
    def inner():
        str = func()
        return str.upper()

    return inner


@upper
def display():
    return "Hello vaishu"


print(display())

l = ["Vijay", "Job", "Kala", "Demo", "Onion", "Ball", "Car", "Grapes", "Egle"]

n = len(l)
for i in range(n):
    for j in range(i + 1, n):
        if l[i].lower() > l[j].lower():
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

output = "[" + ", ".join(["\"" + elem + "\"" for elem in l]) + "]"
print(output)

my_list = [1, 2, 2, 3, 4, 4, 5]
new_list = []
for i in my_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

import re

# def add(a,b):
#     print(3+5)
#
# m = map(add, my_list)
# print(list(m))

l = [1, 2, 3, 4, 1, 2]
new_list1 = []
for i in l:
    if i not in new_list1:
        new_list1.append(i)

print(new_list1)

l = [1, 2, 3, 4, 1, 2]

l1 = list(set(l))
print(l1)

d = {10: 'a', 20: 'b', 30: 'c'}

new_d = {v: k for k, v in d.items()}
print(new_d)

l = [1, 2, 3, 4, 5, 6, 1, 2, 3]
duplicate = []

for i in l:
    if l.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)

l =[9,8,7,6,5]
print(l/2)