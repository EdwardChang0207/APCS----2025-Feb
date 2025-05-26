'''
1.what's operator?
eg. 123 + 456 = 579
123、456 -> 運算元(operatee)
+ -> 運算子(operator)

分類：
1.Number(num * num -> num)
+,-,*,/
(1)指數(次方): **
eg.print(2**3) -> 2*2*2
(2)取餘數: % 10/3=3(商)...1(餘)
eg.print(10%3)
(3)整數除法(取商):
eg.print(10//3)

2.Logic
(num * num -> bool)
(1)assign 定義: =
eg. a = 1
(2)equal 等於: ==
eg. print(1 == 1)
(3)not equal 不等於: !=
eg. print(1 != 1)
(4)greater, less 大於小於:
eg.
print(3>2)
print(1<8)
(5)greater(less) or equal大於等於、小於等於:
eg.
print(1 >= 1)
print(2 <= 1)
------boolean------ (bool * bool -> bool)
(6)not 反閘
周杰倫：哎呦！不錯喔！
eg.1
不錯(not False) -> 好(True)
錯 -> 不好(False)
eg.2
不行(not True) -> 不好(False)
行 -> 好(True)
(7)or 或閘
期中考 
數學或英文考100 -> 3000
真值表
a     b            c
T     F            T
F     T            T
T     T            T
F     F            F
eg.
a = False
b = False
print(a or b)
(8) and 且閘
7-11
紅茶 and 綠茶 -> 開心？
a        b      c
T        F      F
F        T      F
T        T      T
F        F      F
eg.
a = False
b = False
print(a and b)
(9)xor (excursive or) 斥或閘
50嵐
珍奶 xor 烏龍拿鐵 -> 開心？
a         b         c 
T         F         T
F         T         T
T         T         F
F         F         F
a = False
b = False
print((a or b) and (not(a and b)))
'''
if 's' in 'sdfghj':
    print('hi')