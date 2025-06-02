import decimal
import pytest
from task import factorial

def test_true_factorial():
	assert factorial(0) == 1
	assert factorial(1) == 1
	assert factorial(2) == 2
	assert factorial(3) == 6
	assert factorial(8) == 40320


def test_errors_factorial():
	with pytest.raises(TypeError):
		factorial(-0.5)
		factorial(4.5)
		factorial('a')
		factorial([1, 2, 3])
		factorial({1, 2, 3})
		factorial({'a': 1, 'b': 2})

	with pytest.raises(ValueError):
		factorial(-2)
		factorial(-3)
