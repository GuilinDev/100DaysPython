"""
练习3
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
"""
rows = int(input("Input rows: "))

for i in range(0, rows):
    for j in range(i + 1):
        print('*', end='')
    print()

print("\n")

for i in range(0, rows):
    for j in range(0, rows):  # 最多打rows个
        if j < rows - i - 1:  # i从0开始
            print(' ', end='')
        else:
            print('*', end='')
    print()

print("\n")

for i in range(rows):
    for j in range(2 * rows - 1):  # 最底下一行最多2 * rows - 1个
        if (j < rows - i - 1 or j > rows + i - 1):  # 两边不打印
            print(' ', end='')
        else:
            print('*', end='')
    print()