"""
练习1
华氏温度转换为摄氏温度
F = 1.8C + 32
"""
f = float(input('f =  '))
c = (f - 32) / 1.8
print('%.1fF = %.1fC' % (f, c))