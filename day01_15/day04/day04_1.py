"""
练习2
输入两个正整数，计算最大公约数和最小公倍数
"""
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x # 让y成为较大的那个值
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break