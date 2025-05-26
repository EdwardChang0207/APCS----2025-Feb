'''
#串列取值
l = [1,2,3,4,5,6,7]
#    0 1 2 3 4 5 6
print(l[1:5:2]) #[start:end:interval], from start, to end, increase interval each time

#list在for loop的應用
l = [1,2,3,4,5,6,7]
(1)
for i in range(len(l)):
    l[i] = 0

(2)
for i in l:
    i = 0

print(l)
#串列方法
l = [3,3]
l.append(3)
l.append(4)
l.append(5)
#print(l.index(3)) #index:找第一個出現的元素的位址
l.insert(1, 7) #insert(pos, item):原本在pos的元素會被往後擠
x = l.pop(3)#poop, pop:指定位子
print(l)
print(x)
l.remove(5)#remove:指定元素
print(l)
l.reverse()
print(l)
l.sort()
print(l)
# l = [A,B,C]
l = [
    ['O','X','O'],#A
    ['X','X','O'],#B
    ['X','O','X'] #C
]
#l[0] -> ['O','X','O'],#A
#          0   1   2
print(l[0][1])
'''
l = [[],[]]
l = [
    [1,2,3],
    [4,5,6]
    ]