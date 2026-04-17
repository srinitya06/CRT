#Traditinal Approach
def sum_of_N(n):
    s = 0 
    for i in range(n,0,-1):
        s +=  i
    return s 
print(sum_of_N(5))
print(sum_of_N(10))
#Recursive Approach
def sum_of_N1(n):
    if n == 0:
        return 0
    return n + sum_of_N1(n-1)
print(sum_of_N1(5))
print(sum_of_N1(10))

#Factorial of a number
def Factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(Factorial(5))  # 120
print(Factorial(3))  # 6

#RECURSIVE METHOD
def Factorial1(n):
    if n < 0:
        return "no factorial -ves"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * Factorial1(n - 1)

print(Factorial1(5))  # 120
print(Factorial1(3))  # 6
