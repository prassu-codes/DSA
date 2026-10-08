class Solution:
    def twoSum(self, num: list[int], target: int) -> list[int]:
        a,b=0,len(num)-1
        while a < b:
            total=num[a]+num[b]
            if total> target:
                b -= 1
            elif total < target:
                a += 1
            elif total == target:
                return [a+1,b+1]
        return[]