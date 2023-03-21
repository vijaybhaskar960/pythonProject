import re

# Maths the special characters only
t = "35467sdbufnadwreg@#$%&8"
pattern = r"[^\w\s]"
d = re.findall(pattern, t)
print(d)

# Get Ip Address only

v = "This is talent ip address 192.168.10.8080"
pattern = r"\d+[.]\d+[.]\d+[.]\d+"
m = re.findall(pattern, v)
print(m)

# Output : ['192.168.10.8080']

a = "my name is Vijay and age 26 and frd name Vaishu age is 24"
# Get age only
pattern = "\d+"
u = re.findall(pattern, a)
print(u)

# Get the Names only
pattern = r"\b[A-Z][a-z]*\b"
v = re.findall(pattern, a)
print(v)

g = "my life is morning123"
t = re.search("\d+", g)
print(t.group())

k = "Vijay"
l = re.match("\w+", k)
print(l.group())

num = [1, 2, 3, 4, 5]

m = map(lambda x: x + 100, num)
print(list(m))

f = filter(lambda x: x % 2 == 0, num)
print(list(f))

from functools import reduce

r = reduce(lambda x, y: x + y, num)
print(r)

v = "Vijay"

x = print
x(v)

