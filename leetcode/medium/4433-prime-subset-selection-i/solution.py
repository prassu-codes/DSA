class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n==1 or s==1:
            return []
        a=[True]*(n+1)
        p=2
        while p*p<=n:
            if a[p]:
                for i in range(p*p,n+1,p):
                    a[i]=False
            p+=1
        res=[]
        summ=0
        for j in range(2,n+1):
            if a[j]==True:
                if summ+j<=s:
                    summ+=j
                    res.append(j)
        return res
                
        