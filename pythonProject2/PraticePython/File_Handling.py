
file = open(r"C:\Users\vijay\PycharmProjects\pythonProject2\PraticePython\String.py",'r')
#fdata = file.read()
#print(fdata)

# Using readline we can read only one line and return in string format

# line = file.readline()
# print('1 ::', line)
# line = file.readline()
# print('2 ::', line)
# line = file.readline()
# print('3 ::', line)

# Using readlines we can read total lines in a file and  return in list format

lines = file.readlines()
print(lines)
file.close()

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
f = open(r"C:\Users\vijay\PycharmProjects\pythonProject2\PraticePython\String.py", 'a')

data = f.write("\n Hi Guys")
print(data)

data = f.write("\n How are you?")
print(data)