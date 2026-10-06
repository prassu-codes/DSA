class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num==1:
            return False
        s=1
        p=2
        while p*p<=num:
            if num%p==0:
                s+=p 
                if p!=num//p:
                    s+=num//p 
            p+=1 
        return s==num