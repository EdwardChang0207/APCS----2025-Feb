#1.input
#(1)人數
n = int(input())
#(2)成績
'''
<法一>
s = input().split()
for i in range(len(s)):
    s[i] = int(s[i])
'''
'''
<法二>
s = [int(i) for i in input().split()]
'''
#<法三>
s = list(map(int, input().split()))
#2.排序
s.sort()
#3.輸出排序後的成績
print(*s)
#4.分析
#(1)worst case -> 全班不及格
if s[-1] < 60:
    print(s[-1])
    print('worst case')
#(2)best case -> 全班及格
elif s[0] >= 60:
    print('best case')
    print(s[0])
#(3)normal case
else:
    for i in range(len(s)):
        if s[i] >= 60:
            print(s[i-1])
            print(s[i])
            break