class Solution:
    def twoSum(self, num: list[int], target: int) -> list[int]:
        a = 0
        b = len(num)-1
        while a < b:
            if num[a] + num[b] > target:
                b -= 1
            elif num[a] + num[b] < target:
                a += 1
            elif num[a] + num[b] == target:
                return [a+1,b+1]
