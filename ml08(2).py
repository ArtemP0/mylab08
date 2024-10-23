import random
import numpy as np

N = int(input("Введіть число N: "))

matrix = np.random.randint(0, N, size=(5, 7))
print(matrix)

c = np.array([], dtype = int)
for x in matrix[0]:
  if x in matrix[-1] and x not in c:
     c = np.append(c, x)
print(f"Перший і останній рядок : {c}")