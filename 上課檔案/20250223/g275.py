n = int(input())
for i in range(n):
    a1, a2 = input(), input()
    r = []
    #A
    for x in [a1, a2]:
        if (x[1] == x[3]) or (x[1] != x[5]):
            r.append('A')
            break
    #B
    if (a1[-1] == '0') or (a2[-1] == '1'):
        r.append('B')
    
    #C
    if (a1[1] == a2[1]) or (a1[3] == a2[3]) or (a1[5] == a2[5]):
        r.append('C')

    #output    
    if r:
        print(*r)
    else:
        print('None')