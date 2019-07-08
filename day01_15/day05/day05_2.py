"""
百钱百鸡
古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？

自然是设方程来解
5x + 3y + 1/3z = 100，朴素解法 O(n ^ 3)
"""
results = []
for cocks in range(0, 100):
  for hens in range(0, 100 - cocks + 1):
    for chicks in range(0, 100 - cocks - hens + 1):
      if chicks % 3 == 0: # 小鸡的数不能整除,就不必考虑该组数据了
        if (cocks * 5 + hens * 3 + chicks // 3 == 100 and
            cocks + hens + chicks == 100):
          results.append({'cocks': cocks, 'hens': hens, 'chicks': chicks})
print(results)