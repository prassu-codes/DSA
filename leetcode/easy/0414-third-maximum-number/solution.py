class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        p=set(nums)
        q=list(p)
        c=0
        if len(q)>2:
            while c<3:
                b=max(q)
                q.remove(b)
                c+=1
            return b
        else:
            return max(q)  