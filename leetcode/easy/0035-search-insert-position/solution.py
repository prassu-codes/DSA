class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
        else: 
            for j in range(1,len(nums)):
                if target<nums[j] and target>nums[j-1]:
                    return j 
                    break 
            return len(nums) if target>nums[-1] else 0


        