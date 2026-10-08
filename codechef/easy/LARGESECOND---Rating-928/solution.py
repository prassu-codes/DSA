t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    p=a[-1]
    if len(a)==2:
        print(a[0]+a[1])
        break
    for i in range(len(a)-2,0,-1):
        if a[i]!=p:
            print(p+a[i])
            break