#input
A = list(map(int,input())) #1 1 3
c = [] #每個元素有幾個 [2, 2, 1]
l = []
for i in A:
    c.append(A.count(i))
    if i not in l:
        l.append(i)
print(max(c))
l.sort()
l.reverse()
print(*l)

#A1 A2
#A2 A3
#A1 A3