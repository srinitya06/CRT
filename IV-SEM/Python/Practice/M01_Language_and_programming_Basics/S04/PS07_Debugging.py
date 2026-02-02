'''
Debugging in python:
bug --> error 
finding and fixing errors --> Debugging
Types of errors:
1. Syntax erroes --> missing of colon, or intendation
2. Runtime erros --> Divison by zero
3. Logical errors --> missing of logics

Debugging Techniques:
1. print()
2. try-except
3. using pdb --> python debugger 
   purpose:
   1. Pause the execution
   2. Inspect the varibles value 
   3. To run the code line by line
pdb commands:
   1. n --> execute the output in next line
   2.p variable --> to get the value of variable
   3. l --> list nearby code 
   4. c --> continue the execution 
   5. s --> to start a function
   6. r --> return from the function 
   7. h --> help
   8. q --> quit the execution
'''

'''
try:
    a = int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError:
    print("Cannot divisble by zero.")
except ValueError:
    print("Invalid input")
'''

import pdb 

def add(a,b):
    pdb.set_trace()   
    return a+b 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(add(a,b))
