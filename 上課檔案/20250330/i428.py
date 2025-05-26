n = int(input())
s = []
for i in range(n):
    s.append(list(map(int,input().split())))
d = []
for i in range(n-1):
    d.append(abs(s[i][0]-s[i+1][0])+abs(s[i][1]-s[i+1][1]))
print(max(d),min(d))