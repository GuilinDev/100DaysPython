"""
练习2
掷骰子
"""
from random import randint
face = randint(1, 6)
if (face == 1):
  result = "sing a song"
elif face == 2:
  result = "dance"
elif face == 3:
  result = "walking"
elif face == 4:
  result = "running"
elif face == 5:
  result = "swimming"
else:
  result = "whatever else"

print(result)