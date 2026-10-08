t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p=list(set(a))
    c=len(a)
    if p==a:
        print(c)
    elif len(a)==2:
        if a[0]==a[1]:
            print(1)
    else :
        for i in range(1,len(a)-2):
            if a[i]==a[i-1] and a[i]==a[i+1]:
                c-=1 
            if a[-1]==a[len(a)-2]:
                c-=1 
        print(c)
        
        

        