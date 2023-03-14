l = [[1,2,3], [4,5,6], [9,8,7]]
new_list = []
for i in l:
    if isinstance(i, int):
        new_list.append(i)
    else:
        new_list.extend(i)

print(new_list)

l = [1,2,3,4,5,6]
count = 0
for i in l:
    count += 1
print(count)

sum = 0
for i in l:
    sum = sum+i
print(sum)

mul = 1
for i in l:
    mul = mul*i
print(mul)

l = [1,2,34,1,2]

duplicate_value = []
unique_value = []
for i in l:
    if i not in unique_value:
        unique_value.append(i)
    else:
        if i not in duplicate_value:
            duplicate_value.append(i)
print(duplicate_value)


l = [10,20,50,63,89]
import heapq
list = heapq.nlargest(3,l)[-1]
print(list)

maximum = l[0]
minimum = l[0]
for i in l:
    if i>maximum:
        maximum = i
    else:
        if i<minimum:
            minimum = i

print(maximum)

list1 = ['Vaishu',1,2,3,'Vijay']
new_list = [x for x in list1 if type(x) == str]
print(new_list)
new_list = [x for x in list1 if type(x) != str]
print(new_list)

l = [(1,2,3),(9,8,7)]
tuple_convert = [ele for tup in l for ele in tup]
print(tuple_convert)

x = [[3,2,1], [6,5,4], [9,8,7]]
y = [[8,9,7], [8,5,2], [9,5,1]]

x_rows = len(x)
x_colos = len(x[0])
y_colos = len(x[0])

result = [[0 for i in range(x_colos)] for j in range(y_colos)]

for i in range(x_rows):
    for j in range(x_colos):
        for k in range(y_colos):
            result[i][j] += x[i][k] *y [k][j]

print(result)

l = [1,2,3, [4, 5, 6], (7, 8, 9),'Vaishu']
new_list = []
for i in l:
    if type(i) == list:
        for item in i:
            new_list.append(item)
    elif type(i) == tuple:
        for item in i:
            new_list.append(item)
    else:
        new_list.append(i)
print(new_list)





























