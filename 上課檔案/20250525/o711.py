n = int(input())
w1,w2,h1,h2 = map(int, input().split())
v = list(map(int, input().spilt()))
cup_v = 0
cup_h = 0

for i in range(len(v)):
    cup_v += v[i]
    if cup_h < h1: #第一層還沒有滿

    elif cup_h < h1+h2: #第一層已滿

        if cup_h > h2:#第二層滿了

        else:#第二層還沒滿