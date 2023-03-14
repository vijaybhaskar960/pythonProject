l = [1,2,3,4]

r = map(lambda x : x+10,l)
print(list(r))


m = map(lambda a: a*5, l)
print(list(m))


a = [1,2,3,4,5,6,7,8]

result = filter(lambda x:x%2==0,a)
print(list(result))

from functools import reduce

num = [1,2,3,4]

result = reduce(lambda x, y : x+y,num)
print(result)

