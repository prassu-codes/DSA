class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s=0
        for p in range(1,int(num**0.5)+1):
            if num%p==0:
                if p==num:
                    continue
                s+=p
                if num//p==num:
                    continue
                if p!=num//p:
                    s+=num//p 
        return s==num and num!=1