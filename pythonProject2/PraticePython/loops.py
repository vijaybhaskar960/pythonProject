'''
3. Loop statements
    1. break     ==> break is used to terminates the loop
    2. continue  ==> continue is used to skipe the current iteration
    3. pass      ==>
        1. pass will do nothing
        2. we use pass when statement is require to aviod syntax issues.
'''

for i in range(1, 11):
    print(i, end="")
# Print Add numbers
for i in range(1, 20, 2):
    print(i, end=" ")
# Print Even Numbers
for u in range(2, 20, 2):
    print(u, )
#
# n = int(input("\n Enter  number is :"))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd Number")


for i in range(90, 100):
    if i == 95:
        break
    print(i)

for i in range(20, 31):
    if i == 25: continue
    print(i)
    if i == 26: break
    print(i)

for i in range(30, 40):
    if i == 33:
        pass
    print(i, end=" ")

n = 10
while n > 5:
    n -= 2
    print("\n Output value is:", n)

sal = 300
while sal > 250:
    sal -= 10
    print("\n while loop output is :", sal)

# Nested Loops
for x in [1, 2, 3, 4, ]:
    print('-----', x)
    for y in "Vijay":
        print("+++++++", y)

for x in [1, 2, 3]:
    print('----', x)
    for y in 'AB':
        print('=======>', y)
        for z in {'n': 'sri', 88: 99}:
            print('++++++++++', z)
