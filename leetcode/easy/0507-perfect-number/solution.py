class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        s=1
        for p in range(2,int(num**0.5)+1):
            if num%p==0:
                s+=p
                if num//p!=num:
                    if p!=num//p:
                        s+=num//p 
        return s==num