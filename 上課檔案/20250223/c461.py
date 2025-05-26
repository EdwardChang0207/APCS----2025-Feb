a, b, c = [int(i) for i in input().split()]
r = []
if (a and b) == c:
    r.append('AND')
if (a or b) == c:
    r.append('OR')
if ((a or b) and (a and b)) == c:
    r.append('XOR')
if r:
    print(*r, sep='\n')
else:
    print('IMPOSSIBLE')