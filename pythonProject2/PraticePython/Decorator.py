def upper(func):
    def inner():
        Str = func()
        return Str.upper()
    return inner

@upper
def display():
    return "python is my world"

print(display())

# Aprroach 2

# example

def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner

def percentage(func):
    def inner(arg):
        print("%" *30)
        func(arg)
        print("%" * 30)
    return inner


@star
@percentage
def display(msg):
    print(msg)


display("Decorator is a wonderful!")

# Example

def outer(expr):
    def upper(func):
        def inner():
            return func() + expr
        return inner
    return upper

@outer(" Vijay ")
def display():
    return "Good morning"

print(display())

# how to pass parameters in decorator function with example
def my_decorator(parameter):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            print(f"Decorator parameter: {parameter}")
            return func(*args, **kwargs)
        return inner_wrapper
    return wrapper

@my_decorator("hello")
def my_function():
    print("Inside my function")

my_function()
