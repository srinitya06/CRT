'''
input : [1,2,3,4,5,1]
output:[true]
input:[1,2,3]
output: false
def check_duplicates(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False
print(check_duplicates([1,2,3,4,5,1]))
       or
def check_duplicates_optimal(nums):
    s=set()
    for ele in nums:
        if ele in s:
            return True
        s.add(ele)
    return False
print(check_duplicates_optimal([1,2,3,4,5,1]))
'''