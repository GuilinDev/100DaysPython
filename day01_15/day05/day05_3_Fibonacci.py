"""
生成斐波那契数列
(0) 1 1 2 3 5 8 13 ...
"""
numbers = int(input("想生成多少个斐波那契数？ "))
num0, num1 = 0, 1
result = [num0, num1]

# 自底向上的方法
if numbers < 2:
    print(numbers)
else:
    for number in range(2, numbers + 1):
        temp = num0 + num1
        num0 = num1
        num1 = temp
        result.append(temp)

print(result)

# 记忆化搜索
memo = {0: 0, 1: 1}  # 用字典来记忆


def main(keys):
    if numbers < 2:
        print(numbers)
    else:
        if not keys in memo:  # 遍历keys，第keys个
            # print(value, end = ' ')
            memo[keys] = main(keys - 1) + main(keys - 2)

    return memo[keys]


if __name__ == "__main__":
    print("The Nth fibonacci is: " + str(main(numbers)))