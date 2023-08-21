for i in range(0,5):
    for j in range(i+1):
        print("*",end=" ")
    print()

'''output
* 
* * 
* * * 
* * * * 
* * * * * '''

for i in range(5):
    for j in range(i+1):
        print(j+1,end=" ")
    print()

'''Output:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

'''Output:
* * * * * 
* * * * 
* * * 
* * 
* '''

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

'''Output:
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 '''


number =1
for i in range(1, 5+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number += 1
    print()

'''Output:
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 '''

for i in range(5, 1, -1):
    for space in range(0, 5-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()

'''Output:

* * * * * * * 
  * * * * * 
    * * * 
      * '''

# 1
# 2 3
# 4 5 6
# 7 8 9 10

num = 1

for i in range(1,5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()