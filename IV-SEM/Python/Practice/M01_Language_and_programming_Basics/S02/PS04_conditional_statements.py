# Read a number from the user and check whether it is +ve,-ve or zero
'''
Input: 10
Output: '+ve

Input: 0 
Output: /zero

Input: -5
Output: '-ve'
'''
x = int(input())
if(x > 0):
    print("+ve")
elif(x == 0):
    print("zero")
else:
    print("-ve")
