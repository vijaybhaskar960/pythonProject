numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# returns True if number is even
def check_even(number):
    if number % 2 == 0:
          return True

    return False

# Extract elements from the numbers list for which check_even() returns True
even_numbers_iterator = filter(check_even, numbers)

# converting to list
# even_numbers = list(even_numbers_iterator)
#
# print(even_numbers)

import functools
f = filter(lambda x:x%2==0,range(1,11))
print(f)


f = list(filter(lambda x:x%2==0,range(1,11)))
print(f)

numbers = [1,5,6,8]
R = functools.reduce(lambda x,y:x+y,numbers)
print(R)