class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        p=set(nums)
        q=sorted(list(p))
        if len(nums)>2:
            return (q[-3])
        else:
            return (q[-1])
