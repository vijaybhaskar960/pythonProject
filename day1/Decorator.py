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
    return "hello"+" world"

a = add()
print(a)

from abc import ABC,abstractmethod

class demo(ABC):

    @abstractmethod
    def display(self):
        pass

class live(demo):
    def display(self):
        print("This is display method")

obj = live()
obj.display()




