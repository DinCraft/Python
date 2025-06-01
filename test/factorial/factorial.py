def factorial(n):
  if not isinstance(n, int):
    raise TypeError('Введенное значение не целое число')
  if n < 0:
    raise ValueError('Введенное значение должно быть неотрицательным')
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result
