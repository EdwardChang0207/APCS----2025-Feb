n = input()
A = list(n[0::2])
if len(n) >= 2:
    B = list(n[1::2])
else:
    B = 0
for i in range(len(A)):
    A[i] = int(A[i])     
if B:
    for i in range(len(B)):
        B[i] = int(B[i])
print(abs(sum(A) - sum(B)))