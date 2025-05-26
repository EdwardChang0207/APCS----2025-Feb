'''
#while loop
x = 1
while x <= 10:
    print(x)
    x += 1

#for loop
for i in range(1,11):
    print(i)

p = ['鮭魚','鮪魚','玉子燒']
for sushi in p:
    print(sushi)
s = 'abcdef'
for i in s:
    print(i)

range(start(init:0), end, interval(init:1))
start -> end-1, increase interval for each time
for i in range(5,7):
    print(i)
'''

for i in range(20):
    if i % 3 == 0:
        continue
    if i == 10:
        break
    print(i)

