a,b = map(int, input().split())
n = int(input())
result = 0
for i in range(n):
    s = list(map(int, input().split()))
    s.sort()
    for i in s:
        if i > 0: break
        s.remove(i*-1)
    if a in s and b in s:
        result += 1
print(result)