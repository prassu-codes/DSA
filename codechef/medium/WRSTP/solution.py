# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    d=[0,0]
    for i in s:
        if i=='U':
            d[1]=d[1]+1
        elif i=='D':
            d[1]=d[1]-1 
        elif i=='L':
            d[0]=d[0]-1
        else:
            d[0]=d[0]+1 
    if (d[0] or d[1]==0) and (d[0] or d[1]==(2)) or ((d[0] or d[1]==(-2))):
        print("yes")
    else:
        print("no")