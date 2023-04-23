l = [1, 2, 3, 4, 5, 6]
print(l)

count = 0
for i in l:
    count += 1
print(count)

sum = 0
for i in l:
    sum = sum + i
print(sum)

result = 1
for i in l:
    result = result * i
print(result)

l = [1, 2, 3, 4, 5, 6, 1, 2, 3]
duplicate = []

for i in l:
    if l.count(i) > 1:
        if i not in duplicate:
            duplicate.append(i)
print(duplicate)

# Print a different data in different list
l = ['vaishu', 1, 2, 3, 'Vijay', 0.3]

String = []
value = []
Float = []

for i in l:
    if isinstance(i, str):
        String.append(i)
    if isinstance(i, int):
        value.append(i)
    if isinstance(i, float):
        Float.append(i)
print(String)

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

my_list.append(6)
print(my_list)

my_list.insert(6, 7)
print(my_list)

# Print a duplicate values in given list
l = [9, 8, 7, 6, 8, 9]

duplicate_values = []
unique_values = []

for i in l:
    if i not in unique_values:
        unique_values.append(i)
    else:
        if i not in duplicate_values:
            duplicate_values.append(i)

print(duplicate_values)

# Print a Maximum and Minimum Values in given list
l = [4, 5, 56, 78, 90]

maximum = l[0]
minimum = l[0]
for i in l:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i
print(maximum)

# Print a second largest value in given list

my_list = [10, 5, 8, 20, 15]
second_highest = max([x for x in my_list if x != max(my_list)])
print(second_highest)

# Print third-highest value in list using sort method

my_list = [10, 5, 8, 20, 15]
list_sorted = sorted(my_list, reverse=True)
third_largest = list_sorted[2]
print(third_largest)

# Print third-largest value in the list without using the sort method

import heapq

my_list = [10, 5, 8, 20, 15, 12]
third_largest = heapq.nlargest(3, my_list)[-1]
print(third_largest)

# Print a square the even values in given list

l = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']

for i in range(len(l)):
    if type(l[i]) == int and l[i] % 2 == 0:
        l[i] = l[i] ** 2
print(l)

# Print Reverse input integer values

# num = int(input("Enter a value:"))
# num_convert = str(num)
# num_str_reverse = num_convert[::-1]
# num_reverse = int(num_str_reverse)
# print(num_reverse)

# Remove the different data types in list

l = [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c', 12.0]
l = [x for x in l if type(x) != str]
print(l)

l = [1, 2, 3, True]
l.pop()
print(l)


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l1 = []

for i in l:
    if isinstance(i, int):
        l1.append(i)
    else:
        l1.extend(i)
print(l1)

# output : [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiplication of two lists

x = [[3,2,1], [6,5,4], [9,8,7]]
y = [[8,9,7], [8,5,2], [9,5,1]]

x_rows = len(x)
x_cols = len(x[0])
y_cols = len(x[0])

result = [[0 for j in range(x_cols)] for i in range(y_cols)]

for i in range(x_rows):
    for j in range(x_cols):
        for k in range(y_cols):
            result[i][j] += x[i][k] *y[k][j]
print(result)

# output : [[49, 42, 26], [124, 99, 56], [199, 156, 86]]


l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
falttend_list = [ele for tup in l for ele in tup ]
print(falttend_list)

# Output : [1, 2, 3, 4, 5, 6, 7, 8, 9]


x = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
y = [(3, 2, 3), (1, 5, 6), (3, 8, 9)]


result = []
for i in range(len(x)):
    tuple_result = tuple(x[i][j] *y[i][j] for j in range(len(x[i])))
    result.append(tuple_result)
print(result)


l = [1,2,3, [4, 5, 6], (7, 8, 9),'Vaishu']
new_list = []
for sublist in l:
    if type(sublist) == list:
        for item in sublist:
            new_list.append(item)

    elif type(sublist) == tuple:
        for item in sublist:
                new_list.append(item)
    else:
        new_list.append(sublist)

print(new_list)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 'Vaishu']

# Common elements in two lists

def find_common_elements(list1, list2):
    common_elements = [n for n in list1 if n in list2]
    return common_elements

list1 = [1,2,3,4]
list2 = [6,2,5,1]

print(find_common_elements(list1,list2))


input = 1
output = [[input], [input+1], [input+2],[input+3]]
print(output)

# Output : [[1], [2], [3], [4]]

input = 2
output = [[int(str(input) + '1')],[int('3' + '4')]]
print(output)
# Output : [[21], [34]]


# Add particular number end of the list

l = [1,2,3,4,1,5,2,3,1]

for num in l:
    if num==1:
        l.remove(num)
        l.append(num)
print(l)

# Output : [2, 3, 4, 5, 2, 3, 1, 1, 1]

# Reverse a list

l = [6,5,4,3]
l.reverse()
print(l)


# Second Approach

l = [6,5,4,3]
new_list = l[::-1]
print(new_list)

# Third Approach

my_list = [6,5,4,3]
reverse_list = []
for i in range(len(my_list)-1, -1, -1):
    reverse_list.append(my_list[i])
print(reverse_list)

# Find a target value in given list

data = [3, 6, 5, 7, 3]
sum = 9
for n1 in data:
    for n2 in data:
        if n1 + n2 == sum:
            print(n1, n2)


l = ["Vijay", "Job", "Kala", "Demo", "Onion", "Ball", "Car", "egle"]
n = len(l)
for i in range(n):
    for j in range(i+1, n):
        # compare adjacent elements and swap if out of order
        if l[i].lower() > l[j].lower():
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

# print the sorted list as a formatted string
output = "[" + ", ".join(["\"" + elem + "\"" for elem in l]) + "]"
print(output)


# Find the maximum characters in string in given list

data = ["Javascript", "Java", "Python","Springboot", "PythonDeveloper"]
max_length = len(max(data, key=len))
result = []

for item in data:
    if len(item) == max_length:
        result.append(item)

print("Results :", result)

l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

output = [str(l2[i])+str(l1[i]) for i in range(len(l1))]

print(output)  # ['a1', 'b2', 'c3']

# Find a largest and smallest value in the list

def find_extremes(lst):
    largest = smallest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    return largest, smallest

print(find_extremes([10,20,45,8,49,98,2]))

l1 = ["My","Name"]
l2 = ['is', "Vaishu"]
l1.extend(l2)
print(l1)
m = " ".join(l1)
print(m)

