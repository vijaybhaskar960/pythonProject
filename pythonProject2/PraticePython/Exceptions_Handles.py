try:
    a = 10
    b = '20'

    c = a + b
    print(c)

except TypeError:
    print("Type Error")
except ModuleNotFoundError:
    print("Module Error")
except NameError:
    print("Name Error")

else:
    print("Code is correct")
finally:
    pass

# Using raise keyword we can raise exception manually.

name = 'VijayReddy'

if name != 'VijayReddy':
    #raise AssertionError("Name Should Matched as Expected")
    raise AssertionError(' Name should not matched as expected ')
print('Close')

