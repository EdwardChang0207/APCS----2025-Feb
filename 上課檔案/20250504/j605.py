n = int(input())
t = []
s = []
for i in range(n):
    ti, si = map(int, input().split())
    t.append(ti)
    s.append(si)
highest = max(s)
wrong = s.count(-1)
score = highest - n - wrong*2
if score < 0: score = 0
hightest_t = s.index(highest)
print(score,t[hightest_t])
