def palindrome(s: str) -> bool:
	if len(s) < 3:
		raise ValueError('Длина палиндрома минимум 3 символа')
	if not isinstance(s, str):
		raise TypeError('Тип данных должен быть str')
	s = s.lower()
	return s == s[::-1]
