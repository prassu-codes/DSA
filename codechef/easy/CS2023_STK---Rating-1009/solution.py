t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c,d,e,f=0,0,0,0 
    for i in range(len(a)):
        if a[i]!=0:
            c+=1
            d=max(c,d)
        else:
            c=0
    for j in range(len(b)):
        if b[j]!=0:
            e+=1
            f=max(e,f)
        else:
            e=0
    if d>f:
        print("Om")
    elif f>d:
        print("Addy")
    else:
        print("Draw")