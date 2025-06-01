import pytest
from task3 import character_counter

def test_result_character_counter():
    assert character_counter("1123") == 1
    assert character_counter("123") == 0
    assert character_counter("asfdss") == 1
    assert character_counter("223343") == 2

def test_error_character_counter():
    with pytest.raises(TypeError):
        character_counter(1234)
        character_counter({1, 2, 3})