F = input()
N = input()
s = list(map(int, input().split()))
last = -1
b = []
lost = {'2':'0', '5':'2', '0':'5'}
game = False
for i in range(len(s)):
    b.append(F)
    #判斷輸贏
    if F == s[i]: #tie
        #下一輪出什麼
        if s[i] == last:
            F = lost[s[i]]
        else:
            F = s[i]
        last = s[i]
    elif lost[s[i]] == F: #哥哥贏了
        game = True
        print(*b, ':', f'Won at round {i+1}')

    else:#哥哥輸了
        game = True
        print(*b, ':', f'Lost at round {i+1}')

if not game:
    print(*b, ':', f'Drew at round {N}')