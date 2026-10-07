t=int(input())
for _ in range(t):
    n, m = map(int,input().split())
    s = input()
    l = input()
    b = ""
    for i in s:
        if i in l:
            b += 'L'
        else:
            b += 'R'
    c, d = 1, 1
    for k in range(1, len(b)):
        if b[k] == b[k - 1]:
            c += 1
            d = max(c, d)
        else:
            c = 1
    print(d)