al = []
dl = []
r = []
a,d= 0,0
n = int(input())
for i in range(n):
    a,d = map(int,input().split())
    al.append(a)
    dl.append(d)
    r.append(a**2+d**2)
i = r.index(max(r))
al.pop(i)
dl.pop(i)
r.pop(i)
print(al[r.index(max(r))],dl[r.index(max(r))])