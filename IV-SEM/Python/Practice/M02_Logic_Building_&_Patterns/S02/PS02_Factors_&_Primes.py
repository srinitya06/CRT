'''' 
Read a number from the user and count the factors 

n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1
        print(i,end = " ")
print("Number of factors:", count)
'''

'''  
Reverse integer 

n = int(input())
if n >= 0:
    print(int(str(n)[::-1]))
else:
    n = -1 * n
    print(-1*int(str(n)[::-1]))
'''

'''
check whether the given number is prime or not
'''
n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")
