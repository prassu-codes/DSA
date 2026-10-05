# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.remove(min(a))
    summ=0
    for i in a:
        summ+=i 
    print(summ)