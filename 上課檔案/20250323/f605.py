n, d = map(int, input().split())
cost = 0
for i in range(n):
    s = map(int, input().split())
    if max(s) - min(s) >= d:
        cost += int(sum(s) / 3)
print(cost)