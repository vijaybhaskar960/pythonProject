a = [x for x in range(0, 10)]
print(a)

b = [x for x in range(0, 10) if x % 2 == 0]
print(b)

c = [x if x > 2 else x + 1 for x in range(1, 11)]
print(c)

num = [1, 2, 3, 4]
d = [x * 10 for x in num]
print(d)

words = ['hello', 'vaishu', 'im waiting for you']
e = [x.upper() for x in words]
print(e)


String = "Vaishu12345"

f = [x for x in String if x.isdigit()]
print(f)

g = [x for x in String if x.isalpha()]
print(g)


def square(x):
    return x * x


h = [square(x) for x in range(1, 11)]
print(h)

z = [1,2,3]
y = [9,8,7]

v = [z[i]+y[i] for i in range(0,len(z))]
print(v)

# Find out common values in given two lists

l1 = [4,5,6]
l2 = [2,4,3]

new_list = [n for n in l1 if n in l2]
print(new_list)