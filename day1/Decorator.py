def div(a, b):
    print(a / b)


def smart_div(func):
    def inner(a, b):
        if a > b:
            a, b = b, a
            return func(a, b)
        return inner


d = smart_div(div)
div(4, 2)


# Example 2

def str_upper(func):
    def inner():
        str1 = func()
        return str1.upper()

    return inner


@str_upper
def str_print():
    return "Good Morning"


print(str_print())


def upper(func):
    def inner():
        str = func()
        return str.upper()

    return inner


@upper
def add():
    return "hello" + " world"


a = add()
print(a)


# Example

def display(func):
    def inner():
        print("Executing", func.__name__, "Function")
        func()
        print("Funishing Execution")

    return inner


@display
def printer():
    print("Hello World!")

printer()

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