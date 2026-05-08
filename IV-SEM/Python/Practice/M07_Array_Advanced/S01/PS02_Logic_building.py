#Missing number 

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        s1 = (n*(n+1)) // 2
        s2 = sum(nums)
        return s1 - s2