import re

n = "VijayVishu Reddy's"
r = re.search("\w+\s\w+",n)

print(r.group())
print(help('False'))


result = 0
for i in range(10,21):
    # print(i)
    result = result + i
print("sum is :",result)


