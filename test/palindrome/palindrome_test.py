import pytest
from palindrome import palindrome


def test_true_palindrome():
	assert palindrome('aba')
	assert palindrome('1234554321')


def test_false_palindrome():
	assert not palindrome('abcdcdfjaslfja')
	assert not palindrome('1232')


def test_errors_palindrome():
	with pytest.raises(ValueError):
		palindrome('12')
		palindrome('a')
	with pytest.raises(TypeError):
		palindrome(123)
		palindrome(12.3)
		palindrome([1, 2, 3])
		palindrome({"1": 1, "2": 3, "3": 5})
