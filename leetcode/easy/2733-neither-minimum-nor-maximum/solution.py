class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1 
        else:
            return nums[len(nums)//2]