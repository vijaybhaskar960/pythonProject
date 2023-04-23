rows = 5
for i in range(1, rows+1):
    print("* " * i)

'''
* 
* * 
* * * 
* * * * 
* * * * *
'''

rows = 5
number = 1
for i in range(1,rows+1):
    for j in range(1, i+1):
        print(number, end=" ")
        number +=1
    print()

'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''

rows = 5
for i in range(rows, 0, -1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''

rows = 4
for i in range(rows):
    for j in range(i+1):
        print(j+1 ,end=" ",)
    print()

'''
1 
1 2 
1 2 3 
1 2 3 4
'''

