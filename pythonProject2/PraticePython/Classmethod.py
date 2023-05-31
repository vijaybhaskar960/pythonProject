class Demo:
    name = "Vaishu"
    @classmethod
    def sub(cls,a,b):
        print(a-b)
        print(cls.name)
        cls.name = "Vijay"
        print(cls.name)

    @classmethod
    def mul(cls,x,y):
        print(x*y)


Demo.sub(10,5)
obj = Demo()
obj.mul(5,60)