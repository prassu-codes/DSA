t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=sorted(a)
    if a!=b:
        print("no")
    else:
        print("yes")