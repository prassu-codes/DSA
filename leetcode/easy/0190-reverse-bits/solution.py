class Solution:
    def reverseBits(self, n: int) -> int:
        b=""
        while n>0:
            p=n%2
            n=n//2 
            b+=str(p)
        b=b+'0'*(32-len(b)) 
        a=int(b,2)
        return a
