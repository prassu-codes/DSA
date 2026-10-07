# cook your dish here
t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    s=input()
    l=input()
    b=""
    for i in s:
        for j in l:
            if i==j:
                b+='L'
            else:
                b+='R'
    c,d=0,0
    while i<=len(b)-1:
        if b[d]==b[d+1]:
            c+=1 
        d+=1
        