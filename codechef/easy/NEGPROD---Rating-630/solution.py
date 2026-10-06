t = int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    d=0
    for i in a:
        if i<0:
            d+=1
    if a.count(0)>=2 or d>=2 or d==0:
        print("no")
    else:
        print("yes")
    
        
   