''' 
input = 4
output:
* * * * *
* * * * *
* * * * *
* * * * *
--------------------------------------
n = int(input())

for i in range(n):          
    for j in range(n):      
        print("*", end=" ")
    print()                
'''

''' 
n = 4
*
* * 
* * * 
* * * *
--------------------------------------
n = int(input())
for i in range(1, n + 1):      
    for j in range(i):    
        print("*", end=" ")
    print()
''' 
'''
n = 4 
output:
* * * * 
* * *
* *
* 
-------------------------------------------
n = int(input())
for i in range(n,0,-1):      
    for j in range(i):    
        print("*", end=" ")
    print()
'''

''' 
n = 4
1 
2 3 
4 5 6
7 8 9 10
-----------------------------------------------
n = int(input())
s = 0
for i in range(1,n+1):
    for j in range(i):
        s += 1
        print(s, end = " ")
    print()
'''

''' 
n = 4
output:
A
A B 
A B C
A B C D

print(ord('A'))
print(chr(65))
---------------------------------------------------
n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ") 
    print()
'''

''' 
Hollow Square 
n = 4 
* * * *
*     *
*     *
* * * *
'''
n = int(input())

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
