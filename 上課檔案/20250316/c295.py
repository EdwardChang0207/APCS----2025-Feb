#1.input
#(1)N, M
N, M = list(map(int, input().split()))
t = []
#(2)N群數字
for i in range(N):
    #一群要做的事：
    #(1)input -> int -> max -> store
    l = list(map(int, input().split()))
    t.append(max(l))
#2.算S
s = sum(t)
r = []
#3.整除?
for i in t:
    if s % i == 0:
        r.append(i)

#4.output
print(s)
print(*r)