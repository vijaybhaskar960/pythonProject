import re

n = "Vijay Vishu Reddy's"
r = re.search("\w+\s\w+\s\w+",n)

print(r.group())
# print(help('False'))


result = 0
for i in range(10,31):
    # print(i)
    result = result + i
print("sum is :",result)

list = [2,3,45,6]

m = iter(list)
print(next(m))
print(next(m))
print(next(m))
print(next(m))





