a1 = sum([int(i) for i in input().split()])
b1 = sum([int(i) for i in input().split()])
a2 = sum([int(i) for i in input().split()])
b2 = sum([int(i) for i in input().split()])
print(f'{a1}:{b1}')
print(f'{a2}:{b2}')
if (a1 > b1) and (a2 > b2):
    print('Win')
elif (a1 < b1) and (a2 < b2):
    print('Lost')
else:
    print('Tie')

