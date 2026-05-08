'''Maximum SubArray'''
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        s1 = nums[0]
        s2 = nums[0]
        for i in range(1, len(nums)):
            s1 = max(nums[i], s1 + nums[i])
            s2 = max(s1, s2)
        return s2
