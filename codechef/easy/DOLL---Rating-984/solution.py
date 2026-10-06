# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    for i in a:
        if i>k:
            c+=1
    print(c)            