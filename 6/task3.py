import numpy as np

try:
	with open('6/test.txt', 'r') as file:
		lines = [line.strip() for line in file]
	metadata = lines[0].split()
	N = int(metadata[0])
	M = int(metadata[1])
	
	if N <= 0 or M <= 0:
		raise ValueError('Dimensions must be positive.')
	A = np.array([list(map(float, lines[i].split()[:-1:])) for i in range(1, N)])
	b = np.array([list(map(float, lines[i].split()[-1::])) for i in range(1, N)])

	x = np.linalg.solve(A, b)
	print(f'Matrix solve:\n{x}')
		
except Exception as e:
	print(e)