# cook your dish here
x,k,y=map(int,input().split())
p=[]
i,q=0,0
while i<x:
    q+=k
    p.append(q) 
    i+=1 
if y in p:
    print("yes")
else:
    print("no")