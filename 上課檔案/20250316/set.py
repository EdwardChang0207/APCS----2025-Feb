#集合 Set
l = [1, 2, 3, 5, 3, 2, 1, 1]
s = set()
for i in l:
    if i in s:
        print(f'{i}重複了')
    s.add(i)
print(s)