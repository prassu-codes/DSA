class Solution:
    def checkDivisibility(self, n: int) -> bool: 
        s,p=0,1
        i=n
        while i>0:
            q=i%10
            s+=q
            p*=q 
            i=i//10
        total=s+p
        if n%(total)==0:
            return True
        return False
         


        