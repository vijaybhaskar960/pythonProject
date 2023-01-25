dictionary = {"apple":"red",'banana':'yellow','apple1':'green','pink':'orange'}

dictionary.clear()
print(dictionary)


dict = {'name':'vijay','ename':'vijay','sname':'vijay'}

m = dict.copy()
print('Original Dictionary is:',dict)
print("New dictionary is:", m)

seq = ('a','b','c','c')
print(dict.fromkeys(seq,1))

seques = {'a','b','c','d'}

result = dict.fromkeys(seques)
print('The New dictionary is:' +str(result))

result1 = dict.fromkeys(seques,1)
print('The New dictionary is:' +str(result1))

'''Python Dictionary get() Method return the value for the given key if present in the dictionary. 
If not, then it will return None (if get() is used with only one argument)
Syntax : Dict.get(key, default=None)
'''

d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))

'''
In Python Dictionary, items() method is used to return the list with all dictionary keys with values.
Syntax: dictionary.items()

'''

Dictionary1 = {'A': 'Geeks', 'B': 4, 'C': 'Geeks'}

print("Dictionary items:")

# Printing all the items of the Dictionary
print(Dictionary1.items())

'''
The keys() method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary in order of insertion using Python.
Syntax: dict.keys()
'''
Dictionary1 = {'A': 'Geeks', 'B': 'For', 'C': 'Geeks'}

# Printing keys of dictionary
print(Dictionary1.keys())

'''
Python dictionary pop() method removes and returns the specified element from the dictionary.
Syntax : dict.pop(key, def)
'''

# initializing dictionary
test_dict = {"Nikhil": 7, "Akshat": 1, "Akash": 2}

# Printing initial dict
print("The dictionary before deletion : " + str(test_dict))

# using pop to return and remove key-value pair.
pop_ele = test_dict.pop('Akash')

# Printing the value associated to popped key
print("Value associated to popped key is : " + str(pop_ele))

# Printing dictionary after deletion
print("Dictionary after deletion is : " + str(test_dict))

'''
Python dictionary popitem() method removes the last inserted key-value pair from the dictionary and returns it as a tuple.
Syntax : dict.popitem() 
'''
d = {1: '001', 2: '010', 3: '011'}
print(d.popitem())

'''
Python Dictionary setdefault() returns the value of a key (if the key is in dictionary). Else, it inserts a key with the default value to the dictionary.
Syntax: dict.setdefault(key, default_value)
'''

d = {'a': 97, 'b': 98, 'c': 99, 'd': 100}
# space key added using setdefault() method
d.setdefault(' ', 32)
print(d)

'''
Python Dictionary update() method updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.

Syntax: dict.update([other])
'''

Dictionary1 = {'A': 'Geeks', 'B': 'For', }
Dictionary2 = {'B': 'Geeks'}

# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)

# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)

