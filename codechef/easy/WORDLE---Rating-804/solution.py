t=int(input())
for _ in range(t):
    s=input()
    t=input()
    b=""
    for i in range(5):
        if s[i]==t[i]:
            b+='G'
        else:
            b+='B'
    print(b)           
