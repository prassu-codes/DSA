class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        a,b,c=0,1,1
        for i in range(n+1):
            if (a+b+c)==n:
                return True
            elif (a+b+c)>n:
                return False
            else:
                a,b,c=b,c,b+c 
        return False
        