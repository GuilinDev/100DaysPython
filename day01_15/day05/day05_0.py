"""
水仙花数Narcissistic number
水仙花数是指一个3位数，它的每个位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
"""
narcc_numbers = range(100, 1000)
result = []
for narcc_number in narcc_numbers:
  temp = ((narcc_number % 10) ** 3 + ((narcc_number // 10) % 10) ** 3
   + (narcc_number // 100) ** 3)
  if temp == narcc_number:
    result.append(narcc_number)
print(result)