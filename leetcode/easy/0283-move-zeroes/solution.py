class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        if len(nums)==2:
            nums[0],nums[1]==nums[1],nums[0]
        else:   
            for i in range(1,len(nums)-1):
                if nums[i-1]==0 and nums[i]!=0:
                    nums[i],nums[i-1]=nums[i-1],nums[i]
                else:
                    nums[i],nums[i+1]=nums[i+1],nums[i] 
                    nums[i],nums[i-1]=nums[i-1],nums[i]
                



        