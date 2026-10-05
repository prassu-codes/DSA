# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m=0
    for i in a:
        if i>m:
            m=i
    print(m)