class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum=0
        for i in range(1,(num//2)+1):
            if num%i==0:
                sum+=i
        return True if sum==num else False 
        