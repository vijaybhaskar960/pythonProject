def demo(a,b,**c):
    print(a,b,c)

demo(9,8,name="Vaishu",dep="IT",roll="132")


def myFun(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Vijay", mid="for", last="Vaishu")