class Solution:
    def maxProductPair(self, nums: List[int], target: int) -> List[int]:
        m = float('-inf')
        r = [-1, -1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target and nums[i] > nums[j]:
                    p = nums[i] * nums[j]
                    if p > m:
                        m = p
                        r = [i, j]
        return r