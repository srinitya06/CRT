import math
print(math.factorial(5))
print(math.floor(12.45))
print(math.ceil(12.45))
print(math.pi)
#gcd
a = int(input())
b = int(input())
min_num = min(a,b)
for i in range(1,min_num+1):
    if a % i == 0 and b %i == 0:
        gcd = i 
print(gcd)
#Solution 2
a = int(input())
b = int(input())
while b != 0:
    a, b = b, a % b
print(a)

#LCM ==> a*b = GCD * LCM
import math 
a = int(input())
b = int(input())
GCD = math.gcd(a,b)
LCM = (a*b)//GCD
print(LCM)