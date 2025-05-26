t = []
s = []
wrong = 0
high = 0
hitext = 0
round = int(input())
for i in range(round):
    ti,si = map(int,input().split())
    t.append(ti)
    s.append(si)
    if si == -1:
        wrong += 1
    if si > high:
        high = si
        hitext = i
score = max(s) - round - wrong * 2
if score < 0: score = 0
print(score,end=" ")
print(t[hitext])