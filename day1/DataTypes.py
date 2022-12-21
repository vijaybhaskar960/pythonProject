# List Data type

list = [1,5,6,8,9,4,8]
print(list)
list.append(99)
list[1] = 'Vijay'
print(list)
for i in list:
    print(i)
del list[0]
del list
#print(list)

# Tuple Data type

tuple =(45,78,96,32,41,62)
print(tuple)
for i in tuple:
    print(i)

del tuple
print(tuple)

'''
1. multi-dimensional list contains another list.
'''
l = [1,2,['A',{"name":"Reddy","dep":"IT"},'b'],"Vijay",(89,32)]
#    0 1               2                            3     4
print(l)
print(l[2][2])
print(l[4][1])
print(l[2][1])
print(l[2][0])
print(l[3])
print(l)

# String Data type

S = "Tegalapalli Prasad Reddy"
print(S)
# for i in S:
#     print(i)

print(S.upper())
print(S.lower())
print(S.isupper())
print(S.islower())

M = "Rama Krishnna Reddy"

N = "Pavitra Reddy Rama Pavitra"

print(M.split('K'))
print(M.split('nna'))
print(M.split())
print(M.replace('Rama',"Lucky"))
print(N.replace("Pavitra",'Lucky',1))
print(N.count("a"))
j = " * "
print(j.join(["Vijay",'Pavitra',"Lucky","Prasad"]))


# Dictionary Data type

Dict = {"name ":"Vijay",'empid': 736,"empsal":"39k",'empdep':"IT",'empcwl':"Hyderbab"}
print(Dict)
Dict['empid'] = 893
print(Dict)
del Dict['empsal']
print(Dict)
# del Dict
# print(Dict)

#  Set Data type

set = {45,78,45,62,32,45,89,32}
print(set)

set.add(87)
print(set)
set.update("Vijaya")
print(set)
del set
print(set)


# Assignment Operators

n = 8
print(n+10)  # Addition
print(n-10)  # Subtraction
print(n*10)  # Multiplication
print(n/10)  # Division
print(n//10) # Modulus

# Outputs
'''
18
-2
80
0.8
0 '''




















