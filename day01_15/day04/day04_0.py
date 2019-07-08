"""
练习1
输入一个正整数判断它是不是素数
"""
from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True

if num % 2 == 0:
    is_prime = False

for x in range(3, end + 1, 2):  # 检查了2以后，剩下的只检查奇数即可
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
