t = int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    c=0
    d=0
    for i in a:
        if i==0:
            c+=1
        elif i<0:
            d+=1
    if (a[0]<0 and a[1]<0 and a[2]<0) or (a[0]>0 and a[1]>0 and a[2]>0):
        print("no")
    elif c>=2 or d>=2:
        print("no")
    else:
        print("yes")
    
        
   