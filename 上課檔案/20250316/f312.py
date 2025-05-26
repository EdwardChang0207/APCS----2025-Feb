def y1(n):
    return A1*n**2+B1*n+C1

def y2(n):
    return A2*n**2+B2*n+C2

#1.input
#(1)A1,B1,C1
A1,B1,C1 = map(int,input().split())
#(2)A2,B2,C2
A2,B2,C2 = map(int,input().split())
#(3)n
n = int(input())
#2.算，找最大組合
r = []
for i in range(n+1):
    r.append(y1(n-i)+y2(i))
#3.輸出
print(max(r))