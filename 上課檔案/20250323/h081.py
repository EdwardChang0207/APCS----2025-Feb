#input
n, D = map(int, input().split())# n:有幾個價格, D:目標差價
p = list(map(int, input().split()))#p:所有價格
x = p[0]#上一次成本或上一次賣價
r = 0#最後收益
hold = True #現在手上有沒有股票
for i in p[1::]:#檢視所有價格, i:當下的價格
    if hold and i >= x + D:#賣
        r += i - x
        x = i
        hold = False
    elif (not hold) and i <= x - D:#買
        x = i
        hold = True
print(r)