'''
Formatting the data with % and {}
%s string
%d int
%f or %g float '''

name = "Vijay"
sal = 4500.45
age = 25

# approach 1
print(name,sal,age)

# approach 2
print("Name is the:",name)
print("Sal is the:",sal)
print("Age is the:",age)

# Approach 3
print("Name:%s Sal:%g Age:%d"%(name,sal,age))

# Approach 4
print("Name : {}  Sal : {} Age :{}".format(name,sal,age))

# Approach 5
print("Name : {0}  Sal : {1} Age :{2}".format(name,sal,age))
