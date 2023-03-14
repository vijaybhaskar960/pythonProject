def sum(*agrs):
    s = 0
    for i in agrs:
        s += i
    print("Sum is:", s)


sum(10, 20)


# Approach 2

def my_three(a, b, c):
    print(a, b, c)


args = [1, 2, 3]
my_three(*args)


# Approach 3

def Args(a, b, *c):
    print(a, b, c)


Args(1, 2, 3, 4, 5, 6, )
