keys = [1, 2, 3]
values = ['a', 'b', 'c']

my_dict = {keys[i]: values[i] for i in range(len(keys))}
print(my_dict)
print(dict(zip(keys, values)))

# Print Duplicate values in dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 3}

duplicate_value = {}
for value in my_dict.values():
    keys = [key for key, val in my_dict.items() if val == value]
    if len(keys) > 1:
        duplicate_value[value] = keys
print(duplicate_value)

keys = ['1', '2', '3']
values = ['q', 'r', 's']
my_dict = {int(keys[i]): values[i] for i in range(len(keys))}
print(my_dict)

# Print a dictionary in different

keys = [1, 2, 3]
values = ['a', 'b', 'c', 'd']
my_dict = {}
for i in range(min(len(keys), len(values))):
    my_dict[keys[i]] = values[i]
print(my_dict)

# Update the same key value in dictionary

d = {'a': 11, 'b': 22, 'c': 22, 'd': 44}
for key, value in d.items():
    if value == 22 and key == "c":
        d[key] = 33
output = d
print(output)

date = {
    "name": "Vijay",
    "Depart": "IT",
    "Salary": "50k",
}

print(date['name'])  # It will return  dictionary value
print(date.get('Dep'))  # If in case not there key value in dict it will return None using the get Method

dict = {"a": 10, "b": 20, "c": 30}

new_dict = {}
for key, value in dict.items():
    new_dict[value] = key
print(new_dict)

# output {10: 'a', 20: 'b', 30: 'c'}
