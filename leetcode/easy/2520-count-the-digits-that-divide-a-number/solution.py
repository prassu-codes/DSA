class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        i=num
        while num>0:
            p=num%10
            if i%p==0:
                c+=1
            num=num//10
        return c
        