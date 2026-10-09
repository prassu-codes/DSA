# cook your dish here
n,k=map(int,input().split())
a=list(map(int,input().split()))
s=0
for i in range(0,len(a),2):
    if a[i]>2*k:
        s+=a[i]
print(s)