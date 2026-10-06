class Solution:
    def count_non_minimum(self, nums):
        mini=min(nums)
        p=nums.count(mini)
        return (len(nums)-p)
        
        # write your code here
        
