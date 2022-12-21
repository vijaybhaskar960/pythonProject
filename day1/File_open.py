
#
# f = open(r"C:\Users\Vijay Bhaskar Reddy\PycharmProjects\pythonProject\SeleniumPratice\Open_file.py",'r')

# we can read entire file  data
# fdate = f.read()
# print(fdate)

# We can read one line

# fdata = f.readlines()
# print(fdata)


## Using readline we can read only one line and return in string format
# line  = f.readline()
# print(' 1 :: ', line)
#
# line  = f.readline()
# print(' 2 :: ', line)
#
# line = f.readline()
# print("3 :",line)

## Using readlines we can read total lines in a file and  return in list format

# lines  = f.readlines(4)
# print(' READ LINES ', lines)
# f.close()

'''
1. To do write operation on file we have to open a file with 'w' mode
2. If you open a file with write mode if file is not exist it will crate a new file, if file is exist it will remove old data and write new data.

'''

# f = open(r"C:\Users\Vijay Bhaskar Reddy\PycharmProjects\pythonProject\SeleniumPratice\Open_file.py",'w')

# fdata = f.write("\nvijay")
# print(fdata)
# fdata = f.write("\nPrasad Reddy")
# print(fdata)
#

'''
1. To do append operation on file we have to open a file with 'a' mode
2. If you open a file with append mode if file is not exist it will crate file, if file is exist it will add new data after old data.

'''
f = open(r"C:\Users\Vijay Bhaskar Reddy\PycharmProjects\pythonProject\SeleniumPratice\Open_file.py",'a')

data = f.write("\n Hi Guys")
print(data)

data = f.write("\n How are you?")
print(data)


