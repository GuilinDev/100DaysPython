"""
练习2
根据半径求周长和面积
"""
import math

radius = float(input('请输入半径： '))
perimeter = 2 * math.pi * radius
print("Perimeter: " + str(perimeter))
area = math.pi * radius ** 2
print("Area: " + str(area))

"""
练习3
判断闰年
"""
year = int(input('Please input year: '))
print(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)