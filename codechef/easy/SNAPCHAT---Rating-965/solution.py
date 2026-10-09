t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for i in range(len(a)):
        if a[i]!=0 and b[i]!=0:
            c+=1
    print(c)
        