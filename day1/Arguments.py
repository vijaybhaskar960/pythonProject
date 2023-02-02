def sum(*args):
    s = 0

    for i in args:
        s = s+i
    print("sum is:",s)

sum(1,2,7,8,9,4,2,5,4,5,8,9,8,30)


# Approach 2
def Three(a,b,c,d):

    print(a,b,c,d)

args = [1,2,3,4]
Three(*args)


def my_name(**kwargs):

    for i ,j in kwargs.items():
        print(i ,":" ,j)

my_name(name="Vijay",surname="Tegalapalli",job="SoftwareEngineer")


def My_dad(a,b,c):
    print(a,b,c)
a = {'a':'One','b':'Two','c':'Three'}

My_dad(**a)

