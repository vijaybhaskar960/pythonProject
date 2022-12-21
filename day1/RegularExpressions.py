'''
1. Match is used to find a patran from starting positon
'''

import re
v = "Tegalapalli Reddy"

mo = re.match("Tegalapall",v)
print(mo.group())

'''
2. Search is used to find a pattern from any where in the string.
'''

name = "T Prasad Reddy"
mo = re.search("Reddy",name)
print(mo.group())

mo = re.search("Prasad",name)
print(mo.group())

# mo = re.search("Prasad1",name)
# print(mo.group())

s = "Vijay123"
mo = re.match("\w*",s)
print(mo.group())

mo = re.match("\w+",s)
print(mo.group())

w = "Swaraj123"
mo = re.search("\d+",w)
print(mo.group())

w = "Swaraj123"
mo = re.search("^Swa",w)
print(mo.group())

w = "Swaraj123"
mo = re.search("raj123$",w)
print(mo.group())

D = "Discoveryviyay"
mo = re.search("vijay|Discovery",name)
print(D)

G = "MyGarden"
mo = re.match(".*",G)
print(mo.group())

name = "T Vijaya Bhaskar Reddy"
mo = re.match('(\w)\s(\w+)\s(\w+)\s(\w+)', name)
print("All Groups Are :",mo.group())

print("First name is :",mo.group(1))

print("Sceond name is :",mo.group(2))

print("Third name is :",mo.group())


K = "RamaKrishna"
mo = re.match('[A-R]ama',K)
print(mo.group())

M = "Vijayareddy"
mo = re.search('[a-z]reddy',M)
print(mo.group())

name = 'Vishureddy'
mo = re.match('\w{3,10}', name)
print('Pattern :',mo.group())

mo = re.match('\w{0,6}', name)
print('Pattern :',mo.group())

mo = re.match('\w{8,10}', name)
print('Pattern :',mo.group())

'''
1. Using findall we can search all matching pattrens in a string
2. It will return all matching values in list format
'''
import re

s = '345vijay89reddy99yes9678'
v = re.findall('[a-z]+', s)
print(v)
