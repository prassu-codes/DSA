class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        l=0
        c=0
        while l<len(nums)-1:
            if nums[l]==nums[l+1]:
                c+=1
            else:
                l+=1
                continue
            l+=1
        return c
        
                
        