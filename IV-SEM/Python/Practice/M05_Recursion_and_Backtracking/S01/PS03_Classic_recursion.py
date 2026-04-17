#Fibonacci series
#0 1 1 2 3 5 8 13....
def Fibonacci(n):
    if n == 1:
        return 0 
    elif n == 2:
        return 1 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(5))
print(Fibonacci(8))

# GCD of 2 numbers - TRADITIONAL APPROACH
def GCD(a,b):
    while b != 0:
        a,b = b, a%b 
    return a 
print(GCD(4,10))

#RECURSIVE APPROACH
def GCD1(a,b):
    if b == 0:
        return a 
    return GCD1(b,a%b)
print(GCD1(4,10))