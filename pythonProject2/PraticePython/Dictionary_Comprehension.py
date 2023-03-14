d = {i:i**2 for i in range(1,6)}
print(d)

my_dict = {'apple': 2, 'banana': 4, 'orange': 1, 'kiwi': 3}

new_dict = {k:v*2 for k, v in my_dict.items()}
print(new_dict)

my_dict = {'apple': 2, 'banana': 4, 'orange': 1, 'kiwi': 3}

filter_dict = {k:v for k, v in my_dict.items() if v>2}
print(filter_dict)

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

my_dict = {keys[i]:values[i] for i in range(len(keys))}
print(my_dict)



