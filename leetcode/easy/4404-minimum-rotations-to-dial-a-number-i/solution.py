class Solution:
    def minRotations(self, s: str) -> int:
        curr=0
        su=0
        for i in s:
            p=int(i)
            d=abs(curr-p)
            su+=min(d,10-d)
            curr=p
        return su