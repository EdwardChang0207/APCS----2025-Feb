l = input().split()
l = [int(l[0]), int(l[1], int(l[2]))]
l.sort()
a, b, c = l[0], l[1], l[2]
print(a,b,c)
if a + b <= c:
    print('No')
else:
    if a**2 + b**2 < c**2:
        print('Obtuse')
    elif a**2 + b**2 == c**2:
        print('Right')
    else:
        print('Acute')
