def Filp(m:list):
    m.reverse()
    return m

def Rotate(m):
    mt = []
    for C in range(len(m[0])):
        row = []
        for R in range(len(m)):
            row.append(m[R][C])
        mt.append(row)
    mt = Filp(mt)
    return mt

R, C, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]
# for i in range(R):
#     B.append(list(map(int, input().split)))
k = list(map(int, input().split()))
k.reverse()
for i in k:
    if i == 0:#rotate
        B = Rotate(B)
    else: #filp
        B = Filp(B)

print(len(B),len(B[0]))
for i in B:
    print(*i)