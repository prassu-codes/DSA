class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool: 
        p=set(nums)
        q=list(p)
        if q.sort()==nums.sort():
            return False 
        else:
            return True