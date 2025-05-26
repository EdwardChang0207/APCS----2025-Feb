n = list(input())
ans = abs(sum([int(n[i])*(-1)**i for i in range(len(n))]))
print(ans)