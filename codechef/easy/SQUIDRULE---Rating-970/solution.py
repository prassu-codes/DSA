t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    p=min(a)
    q=sum(a)
    print(q-p)
