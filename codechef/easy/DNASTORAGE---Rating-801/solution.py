t = int(input())
for _ in range(t):
    n=int(input())
    s=input()
    l=0
    r=1
    b=""
    while r<=len(s):
        if s[l]=='0' and s[r]=='0':
            b+='A'
        elif s[l]=='0' and s[r]=='1':
            b+='T'
        elif s[l]=='1' and s[r]=='0':
            b+='C'
        else:
            b+='G'
        l+=2
        r+=2
    print(b)
            
        
