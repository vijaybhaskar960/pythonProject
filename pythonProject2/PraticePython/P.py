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




