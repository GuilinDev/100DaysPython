"""
Perfect Number
完美数是一些特殊的自然数。它所有的真因子（即除了自身以外的约数）的和（即因子函数），
恰好等于它本身。如果一个数恰好等于它的因子之和，则称该数为“完全数”。
第一个完全数是6，第二个完全数是28，第三个完全数是496，后面的完全数还有8128、33550336等等。

这道题假设寻找10000以内的所有完美数。
"""
candidates = range(1, 10001)
result = []
for candidate in candidates:
    divisors = range(1, candidate // 2 + 1)  # 从2到该自然数的一半, +1是因为左开右闭
    sum = 0  # 存因子的总和
    for divisor in divisors:
        if candidate % divisor == 0:  # 检查是否是因子
            sum += divisor

    if sum == candidate:
        result.append(candidate)
print(result)