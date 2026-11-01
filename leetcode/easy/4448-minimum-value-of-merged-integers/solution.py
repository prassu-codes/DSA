class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        l,r=0,1
        mini=float('inf')
        while l<(len(nums)-1):
            a=(str(nums[l]))+(str(nums[r]))
            if int(a)<mini :
                mini=int(a)
            l+=2
            r+=2 
        return mini
            
        