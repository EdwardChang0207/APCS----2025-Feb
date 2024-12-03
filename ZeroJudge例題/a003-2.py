#input:
#line1: M D

x = input().split() 
M = int(x[0])
D = int(x[1])

#process:
s = (M*2+D)%3
#2. judge 吉 大吉 普通 by s
if s == 0:
    print("普通")
elif s == 1:
    print("吉")
else:
    print("大吉")

#output:吉 大吉 普通