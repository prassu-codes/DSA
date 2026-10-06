t = int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m,o=0,0
    for i in a:
        if i>m:
            m=i 
    a.remove(m)
    for j in a:
        if j>o:
            o=j
    if o==m:
        while o==m:
            a.remove(o)
            p=0
            for k in a:
                if k>p:
                    p=k
            o=p
        print(m+p)
    else:
        print(o+m)