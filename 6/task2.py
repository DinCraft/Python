import numpy as np

try:
  N = int(input("Enter matrix size: "))
  if N < 0:
    raise ValueError("Value must be positive")
except ValueError as e:
  print(e)

A = np.random.randint(1, 101, size=(N,N))
print(f'Matrix A:\n{A}')
column_sum = A.sum(axis=0)
min_index = np.argmin(column_sum)
print(f'Index of minimum sum column: {min_index}')