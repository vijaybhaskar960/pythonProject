my_dict = {'apple': 2, 'banana': 4, 'orange': 1, 'kiwi': 3}
for i in my_dict.values():
    print(i, end=" ")

for i in my_dict.keys():
    print(i)

for i, j in my_dict.items():
    print(i,':',j)

print(my_dict)
m = my_dict.copy()
print("New Dictionary is:",m)

'''Python Dictionary get() Method return the value for the given key if present in the dictionary. 
If not, then it will return None (if get() is used with only one argument)
Syntax : Dict.get(key, default=None)
'''

new_dict = {'apple': 2, 'banana': 4, 'orange': 1, 'kiwi': 3}
print(new_dict.get("banana"))
''''
The keys() method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion using Python.
Syntax: dict.keys()
'''
Dictionary1 = {'Geeks':1, 'For':2, 'Geeks1':3}

# Printing keys of dictionary
print(Dictionary1.keys())


'''
Python dictionary popitem() method removes the last inserted key-value pair from the dictionary and returns it as a tuple.
Syntax : dict.popitem() 
'''
Dictionary2 = {'apple': 2, 'banana': 4, 'orange': 1, 'kiwi': 3}
print(Dictionary2.popitem())

# Remove the
print(Dictionary2.pop("orange"))
print(Dictionary2)


# Dictionary update method

Dictionary1 = {'Geeks':1, 'For':2, 'Geeks1':3}
Dictionary2 = {'apple': 2, 'banana': 4, 'orange': 1, 'kiwi': 3}


d = Dictionary1.update(Dictionary2)
print(Dictionary1)

my_dict = {"Javascript":2, "Python":1, "C":2}
print(my_dict)
m = sorted(my_dict, key=lambda x: my_dict[x])
print(m)


