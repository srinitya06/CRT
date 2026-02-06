
import numpy as np
'''
arr = np.array([10,20,30])
print(arr)

print(np.max(arr))
print(np.min(arr))
print(np.sum(arr))
print(np.mean(arr))
print("Even numbers list is:", np.arange(2,10,2))
print("Odd numbers list is:",np.arange(1,10,2))


n = int(input("Enter the size:"))
ele = list(map(int,input("enter ele").split()))
print("Array Ele are:",np.array(ele))

#sum of two array elements
arr1 = np.array([13,14,15])
arr2 = np.array([12,34,56])
print(np.sum(arr1) + np.sum(arr2))


arr = list(map(int,input("Enter nums:").split()))
if len(set(arr)) >= 2:
    print(sorted(set(arr))[-3])
else:
    print(max(arr))
    '''
# monotonic array
nums = list(map(int,input("Enter nums").split()))
inc = True 
doc = False 
for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
        doc = False
    if nums[i] < nums[i-1]:
        inc = False 
if inc or doc:
    print("Monotonic array")
else:
    print("not monotonic array")