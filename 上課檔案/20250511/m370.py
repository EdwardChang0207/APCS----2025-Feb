x, n = map(int, input().split())
l = list(map(int,input().split()))
greater, lower, min_p, max_p= 0, 0, l[0], l[0]
for i in l:
    if i > x: greater += 1
    elif i < x: lower += 1
    if i < min_p: min_p = i
    if i > max_p: max_p = i

if greater > lower:
    print(greater, max_p)
else:
    print(lower, min_p)