class Animal:

    @classmethod
    def add(cls, a, b):
        print("Add a two value is :", a + b)

    @classmethod
    def mul(cls, x, y):
        print("Multiplication of value is:", x * y)

    @classmethod
    def sub(cls, i, j):
        print("Subtraction of value is:", i - j)


Animal.add(4, 9)
Animal.mul(45, 9)
Animal.sub(89, 80)
