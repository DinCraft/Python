import numpy as np

try:
	N = int(input("Enter matrix size: "))
	if N < 0:
		raise ValueError('Value must be positive')
except ValueError as e:
	print(f'Error: {e}')

A = np.random.randint(1, 101, size=(N, N))
B = np.random.randint(1, 101, size=(N, N))

print(f'Matrix A:\n{A}')
print(B)

print(A > B)
print(A < B)
print(A == B)
