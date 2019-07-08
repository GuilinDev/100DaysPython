"""
练习4
输入三条边长如果能构成三角形就计算周长和面积
"""
import math

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
  print("Can form a triangle")
  perimeter = a + b + c;
  print("Perimeter: %f" % (perimeter))
  p = perimeter / 2
  area = math.sqrt(p * (p - a) * (p - b) * (p - c))
  print("Area: %.1f" % (area))
else:
  print("Cannot form a triangle")