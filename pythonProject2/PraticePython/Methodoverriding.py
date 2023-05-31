class Demo:

    def m1(self):
        print("This is m1 Method")


class Live(Demo):

    def m1(self):
        print("This is m2 Method")
        super().m1()



obj = Live()
obj.m1()
