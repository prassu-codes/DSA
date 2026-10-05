t=int(input())
for _ in range(t):
    n=int(input())
    l=1
    h=n
    c=0
    while l<=h: 
        m=(l+h)//2 
        if m*(m+1)//2<=n:
            c=m 
            l=m+1 
        else:
            h=m-1 
    print(c)
            
        
    