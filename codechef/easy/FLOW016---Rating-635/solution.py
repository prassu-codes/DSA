t=int(input())
for _ in range(t):
    a,b=map(int,input().split())
    def gcd(a,b):
        while b!=0:
            a,b=b,a%b 
        return abs(a)
    p=gcd(a,b)
    q=a*b//p
    print(p,q)
    