'''
1. write a python code to count the digits of the number 

n = int(input())
count = 0 
while n > 0:
    count += 1 
    n //= 10  

print("Number of digits:", count)
'''
'''
2. sum of digits of a number

n = int(input("Enter a number: "))
sum_digits = 0

while n > 0:
    digit = n % 10
    sum_digits += digit
    n //= 10

print("Sum of digits:", sum_digits)
'''

'''
3. products of digits of a number

n = int(input("Enter a number: "))
product = 1

while n > 0:
    digit = n % 10
    product *= digit
    n //= 10

print("Product of digits:", product)
'''

'''
4. reverse of a number

n = int(input("Enter a number: "))
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

print("Reversed number:", reverse)
'''
''' 
5. count even and odd

n = int(input("Enter a number: "))
even_count = 0
odd_count = 0

n = abs(n)

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    n //= 10

print("Even digits:", even_count)
print("Odd digits:", odd_count)
'''

'''
6.largest digit of a numbber

n = int(input("Enter a number: "))
largest = 0

n = abs(n)

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    n //= 10

print("Largest digit:", largest)
''' 
