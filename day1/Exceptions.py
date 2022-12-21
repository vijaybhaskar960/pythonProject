for i in range(0,5):
    print(i)
try:
    a= 10
    b='6'
    c = a+b
    print(c)
except TypeError :
    print("typeError")
except ModuleNotFoundError:
    print("ModuleNotFoundError")
except IndentationError:
    print("indentation error")
else:
    print("Good Code")
finally:
    pass

import sys

d = {'A':1,'B':2}
try:
    d['C']
    'we' + '123'
    sys.ok()
    import re
    open('2_else.py')
except ModuleNotFoundError:
    print(' Module is not defined ')
except NameError:
    print(' name is not defined please define ')
except KeyError:
    print(' KeyError ')
except FileNotFoundError as e:
    print(' Please define file ', e)
except:
    print(' Try block got failed ')

'''
1. else block will execute when the try block executed successfully with out any errors.
'''
try:
    a = '10'
    b = '20'
    c = a + b
except:
    print(' c ')

else:
    print('Else block is')


'''
1. finally block will execute both times when try block executed successfully or fail.
2. It is used to do cleanup process(Closing File, Killing process, close remote connections like that).
'''
try:
    fh = open('3_finally.py')
    print(fh.readline())
    print('12' + '13')
except:
    print(' Try block got failed')
else:
    print(' Else block ')
finally:
    pass
    # fh.close()
    print(' Finally block ')

# Using raise keyword we can raise exception manually.

name = 'VijayReddy'

if name != 'VijayReddy':
    raise AssertionError("Name Should Matched as Expected")
    raise AssertionError(' Name should not matched as expected ')
print('Close')



