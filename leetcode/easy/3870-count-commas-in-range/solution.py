class Solution:
    def countCommas(self, n: int) -> int:
        c=0
        if len(str(n))>3:
            c+=(n-999)
        return c
        