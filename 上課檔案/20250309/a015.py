# A_row, A_col = input().split()
# A_row, A_col = int(A_row), int(A_col)

# A = []
# for _ in range(A_row):
#     r = input().split()
#     A.append(r)

# AT = []
# for col in range(len(A[0])):
#     r = []
#     for row in range(len(A)):
#         r.append(A[row][col])
#     AT.append(r)

# for row in AT:
#     print(*row)
import sys
for i in sys.stdin:
    down, right = i.split()
    down, right = int(down), int(right)
    old = []
    new = []
    for i in range(down):
        num = input().split()
        small = []
        for j in range(right):
            small.append(num[j])
        old.append(small)
    for k in range(right):
        short = []
        for l in range(down):
            short.append(old[l][k])
        new.append(short)
    for m in new:
        print(*m)