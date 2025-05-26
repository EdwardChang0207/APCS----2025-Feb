n = int(input())#n個點
p = [list(map(int, input().split())) for _ in range(n)]#p:[全部的點]
p_cur = [0,0]#目前的起點
v = []#所有的向量
left, right, Uturn = 0, 0, 0#左轉,右轉,迴轉
for point in p:#計算n個點所成路徑中的n-1個向量
    x = point[0]-p_cur[0]
    y = point[1]-p_cur[1]
    v.append([x,y])
    p_cur = [point[0],point[1]]
for i in range(len(v)-1):#n-1個向量兩倆外積
    cross = v[i][0]*v[i+1][1] - v[i][1]*v[i+1][0]#外積結果
    if cross > 0:
        left += 1
    elif cross < 0:
        right += 1
    else: #==0
        Uturn += 1
print(left, right, Uturn)
