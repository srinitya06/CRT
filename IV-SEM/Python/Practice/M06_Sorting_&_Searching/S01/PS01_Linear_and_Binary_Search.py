'''
1.Linear search(sequential)
2./binary search(interval)
def Linear_Search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

li = list(map(int,input().split()))
target = int(input())

print(Linear_Search(li,target))
'''
# Binary Search
def Binary_Search(arr,target):
    low,high = 0,len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(Binary_Search([2,5,7,8,10,20,36,45],7))#2

#leetcode - Question no: 35
# 35. Search Insert Position solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low,high = 0,len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low